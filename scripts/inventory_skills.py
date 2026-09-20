#!/usr/bin/env python3
"""Inventory Agent Skills across a directory tree without third-party packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from pathlib import Path

IGNORED_DIRECTORIES = frozenset(
    {
        ".git",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        ".tmp_pytest",
        ".tox",
        ".venv",
        "__pycache__",
        "node_modules",
        "site-packages",
        "venv",
    }
)

IGNORED_DIRECTORY_PREFIXES = (".tmp_pytest", "pytest-cache-files-")

TRANSIENT_SKILL_DIRECTORIES = frozenset(
    {".git", "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache"}
)

SURFACE_MARKERS = (
    ".agents/skills/",
    ".claude/skills/",
    ".codex/skills/",
    ".github/skills/",
    ".gzkit/skills/",
)


@dataclass(frozen=True)
class SkillRecord:
    """One discovered skill installation or authored source."""

    name: str
    description: str
    project: str
    repository_root: str
    path: str
    relative_path: str
    surface: str
    skill_sha256: str
    tree_sha256: str


def _frontmatter_scalar(text: str, key: str) -> str:
    """Read a simple scalar from YAML frontmatter without parsing all YAML."""

    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) != 3:
        return ""
    prefix = f"{key}:"
    for raw_line in parts[1].splitlines():
        line = raw_line.strip()
        if line.startswith(prefix):
            value = line[len(prefix) :].strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                value = value[1:-1]
            return value
    return ""


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def skill_tree_sha256(skill_root: Path) -> str:
    """Hash a complete skill directory using the gz-skills provenance contract."""

    digest = hashlib.sha256()
    files = []
    for path in skill_root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(skill_root)
        if any(part in TRANSIENT_SKILL_DIRECTORIES for part in relative.parts):
            continue
        files.append((relative.as_posix(), path))

    for relative, path in sorted(files, key=lambda item: item[0].encode("utf-8")):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        digest.update(b"\0")
    return digest.hexdigest()


def _repository_root(path: Path, scan_root: Path) -> Path:
    current = path
    while current != scan_root.parent:
        if (current / ".git").exists():
            return current
        if current == scan_root:
            break
        current = current.parent
    return scan_root


def _surface(relative_path: str) -> str:
    normalized = f"/{relative_path.replace(os.sep, '/')}"
    for marker in SURFACE_MARKERS:
        if f"/{marker}" in normalized:
            return marker.split("/", 1)[0]
    if "/src/" in normalized and "/skills/" in normalized:
        return "package"
    return "other"


def discover_skills(
    scan_root: Path, excluded_projects: Iterable[str] = ()
) -> list[SkillRecord]:
    """Discover skills below *scan_root*, excluding dependency and cache trees."""

    scan_root = scan_root.resolve()
    exclusions = frozenset(excluded_projects)
    records: list[SkillRecord] = []

    def on_error(error: OSError) -> None:
        print(f"warning: {error}", file=sys.stderr)

    for directory, directory_names, file_names in os.walk(scan_root, onerror=on_error):
        directory_names[:] = sorted(
            name
            for name in directory_names
            if name not in IGNORED_DIRECTORIES
            and not name.startswith(IGNORED_DIRECTORY_PREFIXES)
        )
        if "SKILL.md" not in file_names:
            continue

        skill_file = Path(directory) / "SKILL.md"
        repository_root = _repository_root(skill_file.parent, scan_root)
        project = repository_root.name
        if project in exclusions:
            continue

        text = skill_file.read_text(encoding="utf-8", errors="replace")
        relative_path = skill_file.relative_to(repository_root).as_posix()
        records.append(
            SkillRecord(
                name=_frontmatter_scalar(text, "name") or skill_file.parent.name,
                description=_frontmatter_scalar(text, "description"),
                project=project,
                repository_root=str(repository_root),
                path=str(skill_file),
                relative_path=relative_path,
                surface=_surface(relative_path),
                skill_sha256=_sha256(skill_file),
                tree_sha256=skill_tree_sha256(skill_file.parent),
            )
        )

    return sorted(
        records, key=lambda record: (record.name, record.project, record.relative_path)
    )


def summarize(records: Iterable[SkillRecord]) -> list[dict[str, object]]:
    """Collapse installations into one row per declared skill name."""

    groups: dict[str, list[SkillRecord]] = {}
    for record in records:
        groups.setdefault(record.name, []).append(record)

    return [
        {
            "name": name,
            "projects": sorted({record.project for record in group}),
            "installations": len(group),
            "instruction_variants": len({record.skill_sha256 for record in group}),
            "tree_variants": len({record.tree_sha256 for record in group}),
            "surfaces": sorted({record.surface for record in group}),
            "descriptions": sorted(
                {record.description for record in group if record.description}
            ),
        }
        for name, group in sorted(groups.items())
    ]


FLOOR_SECTION = "## Discovery and fallback"

#: Skills authored before the floor contract gained a mechanical witness.
#:
#: This set may only SHRINK. Removing a name is the repair; adding one is a
#: regression. A skill that gains the section while still listed here fails
#: the check, which is what makes this a countdown rather than a standing
#: exemption.
FLOOR_PENDING: frozenset[str] = frozenset(
    {
        "gzs-agent-context-diet",
        "gzs-change-review",
        "gzs-dependency-risk-audit",
        "gzs-hexagonal-architecture-audit",
        "gzs-intent-audit",
        "gzs-plan-audit",
        "gzs-quality-gate",
        "gzs-repository-hygiene",
        "gzs-root-cause-debugging",
        "gzs-router",
        "gzs-session-handoff",
        "gzs-tech-debt-review",
        "gzs-test-driven-change",
        "gzs-update-dependencies",
    }
)


def _declares_floor(text: str) -> bool:
    """Return True when the skill carries a non-empty floor section.

    Witnesses that the section exists and says something, never that what it
    says is a good fallback. Whether a named rung is actually universal is a
    reading, not a state this script can model. The check is still worth
    having: the catalog's failure was not bad floors, it was absent ones.
    """
    _, marker, rest = text.partition(f"\n{FLOOR_SECTION}")
    if not marker:
        return False
    body = rest.split("\n## ", 1)[0]
    return bool(body.strip())


def _authored_skill_paths(records: Iterable[SkillRecord]) -> dict[str, Path]:
    """Map each authored skill name to its SKILL.md, ignoring consumer mirrors."""
    authored: dict[str, Path] = {}
    for record in records:
        relative = record.relative_path.replace(os.sep, "/")
        if not relative.startswith("skills/"):
            continue
        authored.setdefault(record.name, Path(record.path))
    return authored


def floor_violations(
    records: Iterable[SkillRecord],
    pending: Iterable[str] = FLOOR_PENDING,
) -> list[str]:
    """Report authored skills whose floor declaration disagrees with the ledger.

    Two arms, and the second is what makes this a ratchet. A skill missing the
    section and absent from *pending* fails, which stops new drift. A skill
    carrying the section while still listed in *pending* also fails, which
    forces the list down as skills are repaired.
    """
    pending = frozenset(pending)
    messages: list[str] = []
    for name, path in sorted(_authored_skill_paths(records).items()):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as error:  # pragma: no cover - unreadable source tree
            messages.append(f"{name}: SKILL.md could not be read ({error}).")
            continue
        declares = _declares_floor(text)
        if declares and name in pending:
            messages.append(
                f"{name} no longer needs its exemption: it declares a floor, so "
                "remove it from FLOOR_PENDING."
            )
        elif not declares and name not in pending:
            messages.append(
                f"{name} states no floor: add a non-empty '{FLOOR_SECTION}' section "
                "naming what to run when no project surface is found."
            )
    return messages


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Directory tree to scan")
    parser.add_argument(
        "--exclude-project",
        action="append",
        default=[],
        help="Repository directory name to exclude; repeat as needed",
    )
    parser.add_argument(
        "--records",
        action="store_true",
        help="Emit every installation instead of the per-name summary",
    )
    parser.add_argument(
        "--check-floor",
        action="store_true",
        help=(
            "Verify every authored skill declares a discovery-and-fallback "
            "floor; exit 1 when any does not"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    records = discover_skills(args.root, args.exclude_project)
    if args.check_floor:
        violations = floor_violations(records)
        for message in violations:
            print(message, file=sys.stderr)
        print(f"{len(violations)} floor violation(s).", file=sys.stderr)
        return 1 if violations else 0
    payload = (
        [asdict(record) for record in records] if args.records else summarize(records)
    )
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if callable(reconfigure):
        reconfigure(encoding="utf-8")
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
