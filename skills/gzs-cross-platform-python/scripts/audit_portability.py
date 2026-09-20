#!/usr/bin/env python3
"""Audit a Python repository for cross-platform portability defects.

Two checks, both static, both standard-library only, and both safe to run on
any platform. Neither needs the defect to reproduce locally, which is the
point: these failures are usually invisible on whichever platform CI runs.

``line-endings``
    A text surface committed with CRLF, or a missing ``.gitattributes``
    normalization directive. Inspects the git index rather than the working
    tree, because a Windows checkout renders LF blobs as CRLF on disk and git
    normalizes them away again on commit. Trusting the index lets
    ``.gitattributes`` do the work instead of re-deriving it at every write
    site.

``subprocess-errors``
    A text-mode subprocess capture that decodes child output without
    ``errors=``. Undecodable bytes raise ``UnicodeDecodeError``, which is a
    ``ValueError``, so ``except OSError`` does not catch it and the command
    aborts mid-run. Bytes-mode calls are never flagged: adding ``errors=``
    there would silently switch the call to text mode and flip its return type.

Usage::

    python audit_portability.py [--root DIR] [--check NAME]... [--path DIR]...
    python audit_portability.py --format json

Exit status: 0 clean, 1 findings reported, 2 usage error.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

GITATTRIBUTES_LF_DIRECTIVE = re.compile(r"^\s*\*\s+text=auto\s+eol=lf\b", re.MULTILINE)

TEXT_SUFFIXES = frozenset(
    {
        ".cfg",
        ".feature",
        ".ini",
        ".json",
        ".jsonl",
        ".md",
        ".py",
        ".toml",
        ".txt",
        ".yaml",
        ".yml",
    }
)

#: Directories never worth walking: vendored code, build output, caches.
PRUNED_DIRS = frozenset(
    {
        ".git",
        ".hg",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        ".svn",
        ".tox",
        ".venv",
        "__pycache__",
        "build",
        "dist",
        "node_modules",
        "site-packages",
        "venv",
    }
)

SUBPROCESS_CAPTURE_FUNCS = frozenset({"run", "Popen", "check_output"})

GITATTRIBUTES_MISSING_MESSAGE = (
    "Missing .gitattributes. Add the LF normalization directive so git "
    "normalizes line endings in the index on every platform, regardless of a "
    "clone's local core.autocrlf setting."
)

GITATTRIBUTES_WEAK_MESSAGE = (
    ".gitattributes lacks the LF normalization directive, so line endings "
    "depend on each clone's local core.autocrlf setting."
)

CRLF_SURFACE_MESSAGE = (
    "Committed with CRLF line endings. Normalize to LF. A text-mode write "
    "without an explicit newline argument emits the platform separator, which "
    "is CRLF on Windows."
)

SUBPROCESS_ERRORS_MESSAGE = (
    "Text-mode subprocess capture decodes child output but passes no errors=. "
    "Non-UTF-8 output raises UnicodeDecodeError, which is a ValueError, so a "
    "handler catching OSError does not catch it and the command aborts "
    "mid-run. Pass an explicit errors= argument."
)


@dataclass(frozen=True)
class Finding:
    """One portability defect, located and explained."""

    check: str
    artifact: str
    message: str

    def render(self) -> str:
        """Return a human-readable rendering of this finding."""
        return f"{self.check}: {self.artifact}\n    {self.message}"


def _iter_python_files(root: Path, scan_roots: list[Path]) -> list[Path]:
    """Return every Python file under the scan roots, skipping vendored trees."""
    found: list[Path] = []
    for base in scan_roots:
        if not base.is_dir():
            continue
        for path in base.rglob("*.py"):
            try:
                parts = path.relative_to(root).parts
            except ValueError:
                continue
            if PRUNED_DIRS.intersection(parts):
                continue
            found.append(path)
    return sorted(set(found))


def check_gitattributes(root: Path) -> list[Finding]:
    """Fail when .gitattributes is absent or omits the LF directive."""
    path = root / ".gitattributes"
    if not path.is_file():
        return [Finding("line-endings", ".gitattributes", GITATTRIBUTES_MISSING_MESSAGE)]
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        content = ""
    if not GITATTRIBUTES_LF_DIRECTIVE.search(content):
        return [Finding("line-endings", ".gitattributes", GITATTRIBUTES_WEAK_MESSAGE)]
    return []


def scan_committed_crlf(root: Path) -> list[Finding]:
    """Fail on any tracked text surface whose git index EOL is CRLF or mixed."""
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--eol"],
            capture_output=True,
            check=True,
            timeout=30,
            text=True,
            errors="replace",
        )
    except (OSError, subprocess.SubprocessError):
        # Not a git work tree. The .gitattributes arm still gates the contract.
        return []
    findings: list[Finding] = []
    for entry in result.stdout.splitlines():
        meta, tab, rel_posix = entry.partition("\t")
        if not tab:
            continue
        fields = meta.split()
        if not fields or not fields[0].startswith("i/"):
            continue
        if fields[0][2:] not in ("crlf", "mixed"):
            continue
        if Path(rel_posix).suffix.lower() not in TEXT_SUFFIXES:
            continue
        findings.append(Finding("line-endings", rel_posix, CRLF_SURFACE_MESSAGE))
    return findings


def audit_line_endings(root: Path, scan_roots: list[Path]) -> list[Finding]:
    """Run both line-ending arms: the git contract and the committed bytes."""
    del scan_roots  # A whole-repository contract; scan roots do not narrow it.
    return check_gitattributes(root) + scan_committed_crlf(root)


def _subprocess_func_name(node: ast.Call) -> str | None:
    """Return the subprocess capture function name, or None if not one."""
    func = node.func
    if isinstance(func, ast.Attribute) and func.attr in SUBPROCESS_CAPTURE_FUNCS:
        value = func.value
        if isinstance(value, ast.Name) and value.id == "subprocess":
            return func.attr
    return None


def _call_kwargs(node: ast.Call) -> dict[str, ast.expr]:
    """Return the call's named keyword arguments, dropping any double-star form."""
    return {kw.arg: kw.value for kw in node.keywords if kw.arg}


def _is_truthy_constant(value: ast.expr) -> bool:
    """Return True when the node is a literal constant that is truthy."""
    return isinstance(value, ast.Constant) and bool(value.value)


def _decodes_text(kwargs: dict[str, ast.expr]) -> bool:
    """Return True when the call decodes bytes to str, meaning it runs in text mode."""
    if _is_truthy_constant(kwargs.get("text", ast.Constant(value=False))):
        return True
    if _is_truthy_constant(kwargs.get("universal_newlines", ast.Constant(value=False))):
        return True
    encoding = kwargs.get("encoding")
    return encoding is not None and not (
        isinstance(encoding, ast.Constant) and encoding.value is None
    )


def _captures_output(func_name: str, kwargs: dict[str, ast.expr]) -> bool:
    """Return True when the call captures child stdout or stderr."""
    if func_name == "check_output":
        return True
    if _is_truthy_constant(kwargs.get("capture_output", ast.Constant(value=False))):
        return True
    for stream in ("stdout", "stderr"):
        value = kwargs.get(stream)
        if isinstance(value, ast.Attribute) and value.attr == "PIPE":
            return True
    return False


def _subprocess_findings_in(tree: ast.Module, rel: str) -> list[Finding]:
    """Return every unguarded text-mode capture in one parsed module."""
    findings: list[Finding] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func_name = _subprocess_func_name(node)
        if func_name is None:
            continue
        kwargs = _call_kwargs(node)
        if not (_decodes_text(kwargs) and _captures_output(func_name, kwargs)):
            continue
        if "errors" in kwargs:
            continue
        findings.append(
            Finding("subprocess-errors", f"{rel}:{node.lineno}", SUBPROCESS_ERRORS_MESSAGE)
        )
    return findings


def audit_subprocess_errors(root: Path, scan_roots: list[Path]) -> list[Finding]:
    """Flag text-mode subprocess captures that decode output without errors=."""
    findings: list[Finding] = []
    for py_path in _iter_python_files(root, scan_roots):
        try:
            tree = ast.parse(py_path.read_text(encoding="utf-8", errors="replace"))
        except (OSError, SyntaxError):
            continue
        findings.extend(_subprocess_findings_in(tree, py_path.relative_to(root).as_posix()))
    return findings


CHECKS = {
    "line-endings": audit_line_endings,
    "subprocess-errors": audit_subprocess_errors,
}


def build_parser() -> argparse.ArgumentParser:
    """Return the command-line parser."""
    parser = argparse.ArgumentParser(
        prog="audit_portability.py",
        description="Audit a Python repository for cross-platform portability defects.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root to audit (default: the current directory).",
    )
    parser.add_argument(
        "--check",
        action="append",
        choices=sorted(CHECKS),
        help="Run only this check. Repeatable. Default: every check.",
    )
    parser.add_argument(
        "--path",
        action="append",
        type=Path,
        help=(
            "Narrow source scanning to this directory, relative to the root. "
            "Repeatable. Default: the whole repository."
        ),
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format (default: text).",
    )
    return parser


def _resolve_scan_roots(root: Path, paths: list[Path] | None) -> list[Path] | None:
    """Return resolved scan roots, or None when one of them is not a directory."""
    if not paths:
        return [root]
    resolved = [(root / p).resolve() for p in paths]
    for scan_root in resolved:
        if not scan_root.is_dir():
            print(f"error: --path is not a directory: {scan_root}", file=sys.stderr)
            return None
    return resolved


def main(argv: list[str] | None = None) -> int:
    """Run the selected checks and report findings."""
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: --root is not a directory: {root}", file=sys.stderr)
        return 2

    scan_roots = _resolve_scan_roots(root, args.path)
    if scan_roots is None:
        return 2

    selected = args.check or sorted(CHECKS)
    findings: list[Finding] = []
    for name in selected:
        findings.extend(CHECKS[name](root, scan_roots))

    if args.format == "json":
        payload = [
            {"check": f.check, "artifact": f.artifact, "message": f.message} for f in findings
        ]
        print(json.dumps(payload, indent=2))
    else:
        for finding in findings:
            print(finding.render())
        print(f"\n{len(findings)} finding(s) across {len(selected)} check(s).")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
