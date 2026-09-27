#!/usr/bin/env python3
"""Manage one project's minimal gz-skills settings for the setup skill."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

SETTINGS_DIRECTORY = ".gz-skills"
SETTINGS_FILENAME = "settings.json"
SCHEMA_VERSION = 1


class SettingsError(Exception):
    """The project cannot safely be initialized or changed."""


def _paths(project: Path) -> tuple[Path, Path, Path]:
    root = project.resolve(strict=True)
    if not root.is_dir():
        raise SettingsError(f"project is not a directory: {root}")
    directory = root / SETTINGS_DIRECTORY
    return root, directory, directory / SETTINGS_FILENAME


def _check_project(root: Path, directory: Path, settings_path: Path) -> None:
    if (root / ".gzkit").is_dir():
        raise SettingsError(
            f"{root} uses .gzkit; gzkit and gz-skills are incompatible here. "
            "Back out and use the gzkit workflow."
        )
    if directory.is_symlink() or settings_path.is_symlink():
        raise SettingsError("refusing a symlinked .gz-skills directory or settings file")
    if directory.exists() and not directory.is_dir():
        raise SettingsError(f"not a directory: {directory}")


def _read(settings_path: Path) -> dict[str, object] | None:
    if not settings_path.exists():
        return None
    try:
        data = json.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise SettingsError(f"cannot read valid JSON from {settings_path}: {error}") from error
    if (
        not isinstance(data, dict)
        or set(data) != {"schema_version", "profile"}
        or type(data.get("schema_version")) is not int
        or data.get("schema_version") != SCHEMA_VERSION
        or not (
            data.get("profile") is None
            or data.get("profile") in ("lite", "heavy")
        )
    ):
        raise SettingsError(f"unsupported settings in {settings_path}; reconcile manually")
    return data


def _write_new(settings_path: Path, data: dict[str, object]) -> None:
    payload = json.dumps(data, indent=2) + "\n"
    try:
        with settings_path.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(payload)
    except FileExistsError as error:
        raise SettingsError(f"settings appeared during setup: {settings_path}") from error


def _replace(settings_path: Path, data: dict[str, object]) -> None:
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="\n", dir=settings_path.parent,
            prefix=".settings-", suffix=".json", delete=False,
        ) as stream:
            temporary = Path(stream.name)
            json.dump(data, stream, indent=2)
            stream.write("\n")
        os.replace(temporary, settings_path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def run(command: str, project: Path, profile: str | None = None) -> dict[str, object]:
    root, directory, settings_path = _paths(project)
    _check_project(root, directory, settings_path)
    data = _read(settings_path)
    result: dict[str, object] = {"project": str(root), "settings": str(settings_path)}

    if command == "inspect":
        result.update(status="absent" if data is None else "present", profile=None if data is None else data["profile"])
        return result

    if command == "initialize":
        if data is None:
            directory.mkdir(exist_ok=True)
            data = {"schema_version": SCHEMA_VERSION, "profile": None}
            _write_new(settings_path, data)
            result["status"] = "created"
        else:
            result["status"] = "present"
        result["profile"] = data["profile"]
        return result

    if command == "select":
        if profile not in ("lite", "heavy"):
            raise SettingsError("select requires a lite or heavy profile")
        if data is None:
            raise SettingsError("settings are absent; initialize the project first")
        current = data["profile"]
        if current == "heavy" and profile == "lite":
            raise SettingsError("heavy-to-lite reversal is not supported")
        if current != profile:
            data["profile"] = profile
            _replace(settings_path, data)
            result["status"] = "updated"
        else:
            result["status"] = "present"
        result["profile"] = profile
        return result

    raise SettingsError(f"unknown command: {command}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    for name in ("inspect", "initialize", "select"):
        subcommand = subcommands.add_parser(name)
        subcommand.add_argument("--project", type=Path, required=True)
        if name == "select":
            subcommand.add_argument("--profile", choices=("lite", "heavy"), required=True)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(run(args.command, args.project, getattr(args, "profile", None))))
    except (SettingsError, OSError) as error:
        print(f"setup blocked: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
