# Dependency and tool inventory

Use this checklist for discovery. An adopted project profile may require
adding a missing tool; otherwise do not add technology the repository does not
already use.

## Project manifests and lockfiles

- Python: `pyproject.toml`, `uv.lock`, requirements or constraints files, runtime
  dependencies, optional features, every development/on-demand dependency group,
  build backend pins, package sources, constraints/overrides, and tool configuration
  with version floors. Preserve additions beyond an adopted baseline.
- JavaScript/TypeScript: `package.json`, npm/pnpm/yarn/bun lockfiles, package
  manager declarations, and workspace manifests.
- Other ecosystems: Cargo, Go modules, .NET/NuGet, Ruby/Bundler, JVM build
  files, PHP/Composer, and language-specific tool manifests evidenced in the
  tree.

## Runtime and package-manager pins

- Runtime-version files and manifest constraints.
- Package-manager version or required-version fields.
- Dev-container, toolchain, environment-manager, and CI setup versions.

## Repository automation

- Pre-commit hook revisions and hook-managed tool versions.
- GitHub Actions or other CI actions pinned to release tags or commit SHAs.
- Container base images and explicitly versioned build images.
- Documentation-generation, packaging, release, and code-generation tools.

## Vendored or separately installed tools

- Checked-in binaries, downloaded archives, Git submodules, or Git-based tool
  installs.
- Project bootstrap scripts that install named global tools.
- Agent workflow dependencies such as a separately pinned skill or helper
  repository.

Treat machine-global tools as project-managed only when the repository records
their required version or its bootstrap process owns their installation.

## Adopted templates and agent plugins

When evidenced by project instructions, native configuration, catalogs, or locks,
include the adopted starter/template version and exact source revision, skill
snapshot locks, and independently pinned agent plugins. Inspect project-owned
bundle records and every declared harness's source configuration for disagreement.
Distinguish the selected revision, the newest immutable upstream release, local
discovery or installation evidence, and a tested compatibility set. A candidate
version on an upstream branch is not a released update target. A deferred or
disabled component stays deferred or disabled during ordinary maintenance.

In update mode, reconcile reviewed source pins, catalogs, instructions, and
provenance records together through their owning tools. Preserve project profile
choices and application settings. Do not overwrite starter-managed files or
locally modified vendored skills without reviewed reconciliation, fabricate a
lock hash, or edit a managed plugin cache directly. Use the harness's native
manager for authorized project-scoped plugin updates, keeping unrelated user
installs out of scope. An unproven compatibility set or unavailable host check
must remain an explicit gap; manifest validation alone does not prove skill
discovery. Commit, push, tag/release publication, or enabling deferred components
requires the authority of the request or active project workflow.
