"""Install and update immutable GovZero skill snapshots."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import uuid
from collections.abc import Iterable
from dataclasses import dataclass
from importlib import resources
from pathlib import Path
from typing import TypedDict, cast

from . import __version__

SOURCE_REPOSITORY = "https://github.com/tvproductions/gz-skills.git"
LOCK_FILENAME = "gz-skills.lock.json"
SURFACES = {
    "agents": Path(".agents/skills"),
    "claude": Path(".claude/skills"),
    "codex": Path(".codex/skills"),
    "github": Path(".github/skills"),
    "gzkit": Path(".gzkit/skills"),
}
TRANSIENT_DIRECTORIES = frozenset(
    {".git", "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache"}
)
SCAN_IGNORES = frozenset(
    {
        ".git",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        ".tox",
        ".venv",
        "__pycache__",
        "node_modules",
        "site-packages",
        "venv",
    }
)


class SkillInstallError(RuntimeError):
    """A safe install or update could not be completed."""


@dataclass(frozen=True)
class CatalogSkill:
    """A skill available from the current gz-skills distribution."""

    name: str
    version: str
    description: str
    path: Path
    sha256: str


@dataclass(frozen=True)
class SkillState:
    """Observed state of one locked installation."""

    name: str
    installed_path: Path
    state: str
    installed_version: str
    available_version: str | None


class LockSource(TypedDict):
    """Immutable source identity stored for one installed skill."""

    repository: str
    revision: str
    path: str


class LockEntry(TypedDict):
    """One installed skill snapshot."""

    name: str
    version: str
    source: LockSource
    sha256: str
    installed_path: str


class LockDocument(TypedDict):
    """Versioned consumer lock document."""

    schema_version: int
    skills: list[LockEntry]


def _frontmatter_scalar(text: str, key: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) != 3:
        return ""
    prefix = f"{key}:"
    in_metadata = False
    for raw_line in parts[1].splitlines():
        if raw_line and not raw_line[0].isspace():
            in_metadata = raw_line.strip() == "metadata:"
        stripped = raw_line.strip()
        if key == "govzero-version" and not in_metadata:
            continue
        if stripped.startswith(prefix):
            value = stripped[len(prefix) :].strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                value = value[1:-1]
            return value
    return ""


def tree_sha256(skill_root: Path) -> str:
    """Hash every durable file in a skill using the provenance contract."""

    digest = hashlib.sha256()
    files: list[tuple[str, Path]] = []
    for path in skill_root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(skill_root)
        if any(part in TRANSIENT_DIRECTORIES for part in relative.parts):
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


def catalog_root() -> Path:
    """Resolve authored skills in a checkout or bundled skills in a wheel."""

    checkout = Path(__file__).resolve().parents[2] / "skills"
    if checkout.is_dir():
        return checkout
    bundled = resources.files("gz_skills").joinpath("bundled")
    path = Path(str(bundled))
    if not path.is_dir():
        raise SkillInstallError("the installed distribution contains no bundled skills")
    return path


def load_catalog(source_root: Path | None = None) -> dict[str, CatalogSkill]:
    """Load and validate the distributable skill catalog."""

    root = (source_root or catalog_root()).resolve()
    catalog: dict[str, CatalogSkill] = {}
    for skill_dir in sorted(root.iterdir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_dir.is_dir() or not skill_file.is_file():
            continue
        text = skill_file.read_text(encoding="utf-8")
        name = _frontmatter_scalar(text, "name")
        version = _frontmatter_scalar(text, "govzero-version")
        description = _frontmatter_scalar(text, "description")
        if name != skill_dir.name:
            raise SkillInstallError(
                f"catalog name mismatch: directory {skill_dir.name!r}, frontmatter {name!r}"
            )
        if not version:
            raise SkillInstallError(
                f"catalog skill {name!r} has no metadata.govzero-version"
            )
        catalog[name] = CatalogSkill(
            name=name,
            version=version,
            description=description,
            path=skill_dir,
            sha256=tree_sha256(skill_dir),
        )
    return catalog


def source_revision(source_root: Path | None = None) -> str:
    """Return a Git identity when available, otherwise the package version."""

    root = (source_root or catalog_root()).resolve()
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return f"package:{__version__}"
    revision = result.stdout.strip()
    return revision or f"package:{__version__}"


def resolve_destination(
    *,
    project: Path | None,
    user: bool,
    target: Path | None,
    surface: str,
    lock: Path | None,
) -> tuple[Path, Path]:
    """Resolve the skills directory and its consumer-owned lock file."""

    selected = sum(
        value is not None and value is not False for value in (project, user, target)
    )
    if selected != 1:
        raise SkillInstallError("choose exactly one of --project, --user, or --target")
    if surface not in SURFACES:
        raise SkillInstallError(f"unknown surface {surface!r}")

    if project is not None:
        base = project.resolve()
        destination = base / SURFACES[surface]
        lock_path = lock.resolve() if lock else base / LOCK_FILENAME
    elif user:
        base = Path.home()
        destination = base / SURFACES[surface]
        lock_path = lock.resolve() if lock else base / ".agents" / LOCK_FILENAME
    else:
        assert target is not None
        destination = target.resolve()
        lock_path = lock.resolve() if lock else destination.parent / LOCK_FILENAME
    return destination, lock_path


def read_lock(lock_path: Path) -> LockDocument:
    """Read a lock file or return an empty lock document."""

    if not lock_path.exists():
        return {"schema_version": 1, "skills": []}
    try:
        document = json.loads(lock_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SkillInstallError(f"cannot read lock {lock_path}: {error}") from error
    if document.get("schema_version") != 1 or not isinstance(
        document.get("skills"), list
    ):
        raise SkillInstallError(f"unsupported or malformed lock {lock_path}")
    return cast(LockDocument, document)


def _write_lock(lock_path: Path, document: LockDocument) -> None:
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(document, indent=2, sort_keys=False) + "\n"
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{lock_path.name}.", suffix=".tmp", dir=lock_path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(serialized)
        os.replace(temporary, lock_path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _stored_path(path: Path, lock_path: Path) -> str:
    try:
        return path.resolve().relative_to(lock_path.parent.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())


def _resolved_installed_path(value: str, lock_path: Path) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (lock_path.parent / path).resolve()


def _entry_for(
    document: LockDocument, name: str, installed_path: Path, lock_path: Path
) -> LockEntry | None:
    for entry in document["skills"]:
        if entry.get("name") != name:
            continue
        value = entry.get("installed_path")
        if (
            isinstance(value, str)
            and _resolved_installed_path(value, lock_path) == installed_path
        ):
            return entry
    return None


def _replace_directory(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = destination.parent / f".{destination.name}.staging-{uuid.uuid4().hex}"
    backup = destination.parent / f".{destination.name}.backup-{uuid.uuid4().hex}"
    shutil.copytree(source, staging)
    try:
        if tree_sha256(staging) != tree_sha256(source):
            raise SkillInstallError(f"staged copy hash mismatch for {destination.name}")
        if destination.exists():
            destination.rename(backup)
        staging.rename(destination)
    except Exception:
        if destination.exists() and backup.exists():
            shutil.rmtree(destination)
        if backup.exists() and not destination.exists():
            backup.rename(destination)
        raise
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    if backup.exists():
        shutil.rmtree(backup)


def install(
    names: Iterable[str],
    destination: Path,
    lock_path: Path,
    *,
    force: bool = False,
    source_root: Path | None = None,
    revision: str | None = None,
) -> list[str]:
    """Install selected snapshots and update their lock entries."""

    catalog = load_catalog(source_root)
    selected = list(dict.fromkeys(names))
    unknown = sorted(set(selected) - set(catalog))
    if unknown:
        raise SkillInstallError(f"unknown skill(s): {', '.join(unknown)}")
    document = read_lock(lock_path)
    installed: list[str] = []
    revision_value = revision or source_revision(source_root)

    # Check the complete request before changing any target. This avoids a
    # later blocked skill leaving an earlier skill partially propagated.
    for name in selected:
        skill = catalog[name]
        installed_path = (destination / name).resolve()
        if installed_path.parent != destination.resolve():
            raise SkillInstallError(f"unsafe destination for {name}: {installed_path}")
        entry = _entry_for(document, name, installed_path, lock_path)
        if installed_path.exists() and not force:
            if entry is None:
                raise SkillInstallError(
                    f"{installed_path} exists without a matching lock; use --force to replace it"
                )
            expected = entry.get("sha256")
            observed = tree_sha256(installed_path)
            if observed != expected:
                raise SkillInstallError(
                    f"{name} is locally modified ({observed} != {expected}); reconcile or use --force"
                )

    for name in selected:
        skill = catalog[name]
        installed_path = (destination / name).resolve()
        entry = _entry_for(document, name, installed_path, lock_path)
        _replace_directory(skill.path, installed_path)
        new_entry: LockEntry = {
            "name": name,
            "version": skill.version,
            "source": {
                "repository": SOURCE_REPOSITORY,
                "revision": revision_value,
                "path": f"skills/{name}",
            },
            "sha256": skill.sha256,
            "installed_path": _stored_path(installed_path, lock_path),
        }
        if entry is None:
            document["skills"].append(new_entry)
        else:
            document["skills"][document["skills"].index(entry)] = new_entry
        installed.append(name)
        document["skills"] = sorted(
            document["skills"], key=lambda item: (item["name"], item["installed_path"])
        )
        # Keep a multi-skill operation recoverably consistent if a later
        # filesystem operation fails after the preflight.
        _write_lock(lock_path, document)
    return installed


def states(lock_path: Path, source_root: Path | None = None) -> list[SkillState]:
    """Compare locked installations with their installed and available content."""

    document = read_lock(lock_path)
    catalog = load_catalog(source_root)
    result: list[SkillState] = []
    for entry in document["skills"]:
        name = str(entry.get("name", ""))
        installed_path = _resolved_installed_path(
            str(entry.get("installed_path", "")), lock_path
        )
        available = catalog.get(name)
        if not installed_path.exists():
            state = "missing"
        elif tree_sha256(installed_path) != entry.get("sha256"):
            state = "modified"
        elif available is None:
            state = "unavailable"
        elif available.sha256 != entry.get("sha256") or available.version != entry.get(
            "version"
        ):
            state = "update-available"
        else:
            state = "current"
        result.append(
            SkillState(
                name=name,
                installed_path=installed_path,
                state=state,
                installed_version=str(entry.get("version", "")),
                available_version=available.version if available else None,
            )
        )
    return result


def update(
    lock_path: Path, *, apply: bool, source_root: Path | None = None
) -> list[SkillState]:
    """Preview or apply every safe update represented by a lock file."""

    observed = states(lock_path, source_root)
    if not apply:
        return observed
    blocked = [state for state in observed if state.state in {"modified", "missing"}]
    if blocked:
        details = ", ".join(f"{state.name}:{state.state}" for state in blocked)
        raise SkillInstallError(f"lock contains blocked installations: {details}")

    for state in observed:
        if state.state != "update-available":
            continue
        install(
            [state.name],
            state.installed_path.parent,
            lock_path,
            source_root=source_root,
        )
    return states(lock_path, source_root)


def find_locks(root: Path) -> list[Path]:
    """Find consumer lock files below a repository collection."""

    found: list[Path] = []
    for directory, directory_names, file_names in os.walk(root.resolve()):
        directory_names[:] = [
            name for name in directory_names if name not in SCAN_IGNORES
        ]
        if LOCK_FILENAME in file_names:
            found.append(Path(directory) / LOCK_FILENAME)
    return sorted(found)
