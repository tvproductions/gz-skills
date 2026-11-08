"""Verify built archives and exercise a wheel outside the source checkout."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import tomllib
from pathlib import Path
from zipfile import ZipFile

IGNORED = {"__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache", ".git"}


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resource_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): file_hash(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
        and not any(part in IGNORED for part in path.parts)
        and path.suffix not in {".pyc", ".pyo"}
    }


def run(arguments: list[str], cwd: Path, expected: int = 0) -> str:
    result = subprocess.run(
        arguments,
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode != expected:
        raise RuntimeError(
            f"{arguments}: exit {result.returncode}\n{result.stdout}{result.stderr}"
        )
    return result.stdout


def installed_probe() -> None:
    # Imported here so the controller never depends on a source-tree import.
    from gz_skills.core import load_catalog, tree_sha256

    catalog = load_catalog()
    print(
        json.dumps(
            {
                "resources": {
                    f"{name}/{relative}": digest
                    for name, skill in catalog.items()
                    for relative, digest in resource_hashes(skill.path).items()
                },
                "skills": {
                    name: tree_sha256(skill.path) for name, skill in catalog.items()
                },
                "roots": sorted(
                    {str(skill.path.parent.resolve()) for skill in catalog.values()}
                ),
            }
        )
    )


def check(source: Path, artifacts: Path) -> None:
    uv = shutil.which("uv")
    if uv is None:
        raise RuntimeError("uv is required")
    with (source / "pyproject.toml").open("rb") as stream:
        version = tomllib.load(stream)["project"]["version"]
    expected_resources = resource_hashes(source / "skills")
    wheel_name = f"govzero_skills-{version}-py3-none-any.whl"
    archive_name = f"govzero_skills-{version}.tar.gz"
    wheel = artifacts / "first" / wheel_name
    digests = {}
    for name in (wheel_name, archive_name):
        digest = file_hash(artifacts / "first" / name)
        if digest != file_hash(artifacts / "second" / name):
            raise RuntimeError(f"non-reproducible archive: {name}")
        digests[name] = digest
    if file_hash(wheel) != file_hash(artifacts / "direct" / wheel_name):
        raise RuntimeError("direct wheel differs from sdist-built wheel")
    with ZipFile(wheel) as archive:
        prefix = f"govzero_skills-{version}.data/purelib/"
        actual = {
            name.removeprefix(prefix): hashlib.sha256(archive.read(name)).hexdigest()
            for name in archive.namelist()
            if name.startswith(prefix) and not name.endswith("/")
        }
        if actual != expected_resources:
            raise RuntimeError("wheel resources differ from canonical skills")
    with tempfile.TemporaryDirectory(prefix="gz-skills-package-") as temporary:
        outside = Path(temporary)
        shutil.unpack_archive(str(artifacts / "first" / archive_name), str(outside))
        extracted = outside / f"govzero_skills-{version}"
        if resource_hashes(extracted / "skills") != expected_resources:
            raise RuntimeError("sdist resources differ from canonical skills")
        for path in extracted.rglob("*"):
            if any(
                part in IGNORED | {"node_modules", ".venv", "dist"}
                for part in path.relative_to(extracted).parts
            ):
                raise RuntimeError(f"unwanted sdist content: {path}")
        environment = outside / "environment"
        run([uv, "venv", "--python", "3.14.10", str(environment)], outside)
        executable_dir = environment / ("Scripts" if os.name == "nt" else "bin")
        interpreter = executable_dir / ("python.exe" if os.name == "nt" else "python")
        run([uv, "pip", "install", "--python", str(interpreter), str(wheel)], outside)
        probe = outside / "probe.py"
        shutil.copyfile(Path(__file__), probe)
        observed = json.loads(
            run(
                [
                    uv,
                    "run",
                    "--no-project",
                    "--python",
                    str(interpreter),
                    "python",
                    str(probe),
                    "--probe",
                ],
                outside,
            )
        )
        if observed["resources"] != expected_resources:
            raise RuntimeError("installed resources differ from canonical skills")
        cli = str(
            executable_dir / ("gz-skills.exe" if os.name == "nt" else "gz-skills")
        )
        if run([cli, "--version"], outside).strip() != version:
            raise RuntimeError("installed CLI version differs")
        if len(run([cli, "list"], outside).splitlines()) != len(observed["skills"]):
            raise RuntimeError("installed CLI catalog differs")
        project = outside / "consumer"
        run([cli, "install", "--all", "--project", str(project)], outside)
        lock = project / "gz-skills.lock.json"
        document = json.loads(lock.read_text(encoding="utf-8"))
        for entry in document["skills"]:
            if entry["sha256"] != observed["skills"][entry["name"]]:
                raise RuntimeError("installed snapshot hash differs")
            if entry["source"] != {
                "repository": "https://github.com/tvproductions/gz-skills.git",
                "revision": f"package:{version}",
                "path": f"skills/{entry['name']}",
            }:
                raise RuntimeError("wheel lock provenance differs")
        run([cli, "status", "--lock", str(lock)], outside)
        run([cli, "update", "--lock", str(lock), "--apply"], outside)
        edited = project / ".agents/skills" / document["skills"][0]["name"] / "SKILL.md"
        edited.write_text(
            edited.read_text(encoding="utf-8") + "\nlocal edit\n", encoding="utf-8"
        )
        before = edited.read_bytes()
        run([cli, "update", "--lock", str(lock), "--apply"], outside, expected=2)
        if edited.read_bytes() != before:
            raise RuntimeError("update overwrote a local modification")
        run(
            [
                uv,
                "pip",
                "install",
                "--python",
                str(interpreter),
                "--editable",
                str(source),
            ],
            outside,
        )
        editable = json.loads(
            run(
                [
                    uv,
                    "run",
                    "--no-project",
                    "--python",
                    str(interpreter),
                    "python",
                    str(probe),
                    "--probe",
                ],
                outside,
            )
        )
        if editable["resources"] != expected_resources or editable["roots"] != [
            str(source / "skills")
        ]:
            raise RuntimeError(
                "editable installation did not resolve canonical checkout resources"
            )
    print(
        json.dumps(
            {
                "version": version,
                "skills": len(observed["skills"]),
                "resources": len(expected_resources),
                "sha256": digests,
            },
            indent=2,
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--artifacts", type=Path)
    parser.add_argument("--probe", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.probe:
        installed_probe()
    elif args.artifacts is None:
        parser.error("--artifacts is required")
    else:
        check(args.source.resolve(), args.artifacts.resolve())


if __name__ == "__main__":
    main()
