"""Command-line interface for installing and propagating GovZero skills."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .core import (
    SURFACES,
    SkillInstallError,
    find_locks,
    install,
    load_catalog,
    resolve_destination,
    states,
    update,
)


def _destination_arguments(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--project", type=Path, help="Project root")
    group.add_argument(
        "--user", action="store_true", help="Install under the user profile"
    )
    group.add_argument("--target", type=Path, help="Exact skills directory")
    parser.add_argument("--surface", choices=sorted(SURFACES), default="agents")
    parser.add_argument("--lock", type=Path, help="Override lock-file path")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gz-skills", description=__doc__)
    parser.add_argument("--version", action="version", version=__version__)
    subcommands = parser.add_subparsers(dest="command", required=True)

    subcommands.add_parser("list", help="List bundled skills")

    install_parser = subcommands.add_parser(
        "install", help="Install pinned skill snapshots"
    )
    install_parser.add_argument("skills", nargs="*")
    install_parser.add_argument(
        "--all", action="store_true", help="Install the complete catalog"
    )
    install_parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an unlocked or locally modified target",
    )
    _destination_arguments(install_parser)

    status_parser = subcommands.add_parser("status", help="Inspect one consumer lock")
    status_parser.add_argument("--lock", type=Path, required=True)

    update_parser = subcommands.add_parser(
        "update", help="Preview or update one consumer lock"
    )
    update_parser.add_argument("--lock", type=Path, required=True)
    update_parser.add_argument("--apply", action="store_true")

    propagate_parser = subcommands.add_parser(
        "propagate", help="Preview or update every gz-skills consumer below a root"
    )
    propagate_parser.add_argument("root", type=Path)
    propagate_parser.add_argument("--apply", action="store_true")
    return parser


def _print_states(lock_path: Path, rows) -> None:
    if not rows:
        print(f"{lock_path}: no installed skills")
        return
    for row in rows:
        available = row.available_version or "-"
        print(
            f"{row.state:16} {row.name:32} "
            f"installed={row.installed_version} available={available} {row.installed_path}"
        )


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "list":
            for skill in load_catalog().values():
                print(f"{skill.name:32} {skill.version:12} {skill.description}")
            return 0

        if args.command == "install":
            catalog = load_catalog()
            if args.all and args.skills:
                raise SkillInstallError("use skill names or --all, not both")
            names = list(catalog) if args.all else args.skills
            if not names:
                raise SkillInstallError("name at least one skill or use --all")
            destination, lock_path = resolve_destination(
                project=args.project,
                user=args.user,
                target=args.target,
                surface=args.surface,
                lock=args.lock,
            )
            for name in install(names, destination, lock_path, force=args.force):
                print(f"installed {name} -> {destination / name}")
            print(f"lock {lock_path}")
            return 0

        if args.command == "status":
            rows = states(args.lock.resolve())
            _print_states(args.lock.resolve(), rows)
            return 1 if any(row.state != "current" for row in rows) else 0

        if args.command == "update":
            lock_path = args.lock.resolve()
            rows = update(lock_path, apply=args.apply)
            _print_states(lock_path, rows)
            return (
                1
                if any(row.state not in {"current", "update-available"} for row in rows)
                else 0
            )

        if args.command == "propagate":
            lock_paths = find_locks(args.root)
            if not lock_paths:
                print(
                    f"no {Path('gz-skills.lock.json')} files found below {args.root.resolve()}"
                )
                return 0
            exit_code = 0
            for lock_path in lock_paths:
                print(f"\n[{lock_path}]")
                try:
                    rows = update(lock_path, apply=args.apply)
                except SkillInstallError as error:
                    print(f"blocked: {error}")
                    exit_code = 1
                    continue
                _print_states(lock_path, rows)
                if any(
                    row.state not in {"current", "update-available"} for row in rows
                ):
                    exit_code = 1
            return exit_code
    except SkillInstallError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
