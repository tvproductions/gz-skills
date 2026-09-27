# Python environment baseline for adopting heavy projects

Status: working candidate for review, not an approved or enforced baseline.
First review the [gzkit Python and tool profile](../research/gzkit-python-environment-profile-2026-09-27.md);
its tool list is evidence, not a template. A heavy profile does not enforce
these checks yet. The adopting project's approved constitution and architecture
description make its chosen versions, tools, exceptions, and quality gate
binding. This guide applies when the adopting project's implementation is
Python; it does not turn every `gzs-*` skill or lite project into a Python
project.

## Proposed project contract

| Area | Baseline |
| --- | --- |
| Python support | Declare the supported interpreter range with `[project].requires-python` in `pyproject.toml`. Record an exact patch release for routine local development and CI, and test the lowest supported minor version before claiming that range. Review the version at adoption; the `gz-skills` pin of 3.13.15 and floor of `>=3.13` are an example, not a universal mandate. |
| Metadata and dependencies | Use `pyproject.toml` as the reviewed source for package metadata, build backend, runtime dependencies, and optional dependencies. Put test, lint, type, and documentation tools in development dependency groups or an equivalent declared project-managed surface. Keep runtime and development dependencies distinct. |
| Isolation and reproducibility | Use a project-local isolated environment, keep it out of Git, and commit the project's resolved dependency lock for applications and development tooling. `uv` with `uv.lock` is a candidate default for a new heavy project; preserve another established manager when it meets the same reproducibility checks. CI installs from the committed lock without silently changing it. |
| Verification | Document one complete project-owned quality gate. It exercises behavior tests, appropriate static checks, lock freshness, and a build or install smoke test when the project ships a package. Test on every claimed operating system or narrow the support claim. Record verification commands and their results with the change. |
| Secrets and external tools | Keep credentials and machine-local environment data outside tracked manifests and locks. Declare any required external runtime or tool version and its installation method; do not rely on an unexplained global executable. |

For a new project, prefer a currently supported Python minor and a current
patch release. For an adopting brownfield project, inventory its existing
`requirements` files, package-manager files, runtime pins, CI environments,
and actual deployment constraints before selecting the canonical surfaces.
Translate those into the baseline incrementally, preserve behavior, and record
any temporary exception with an owner and migration condition. Do not change
the interpreter floor or replace the package manager merely to make adoption
appear complete.

Keep the project-facing commands and supported versions in that project's
README or contributor guide. Its constitution states the obligation; its
architecture description explains material environment choices; an ADR records
a material exception or migration. SP-BP has its own Python runtime and
packaging decision; this guide does not set it by implication.

The exact default tool set remains to be selected after reviewing gzkit's
declared Astral and Python tools. Ruff and ty are candidates; Behave,
PyInstaller, documentation generators, security scanners, and code-metric
tools need an adopter-specific reason. No runner prohibition is inherited.

## Standards and tool guidance

- The [Python Packaging User Guide for `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
  describes `requires-python`, build metadata, and dependency declarations.
- The [dependency-groups specification](https://packaging.python.org/en/latest/specifications/dependency-groups/)
  separates development requirements from built package metadata.
- Python's [`venv` documentation](https://docs.python.org/3.13/library/venv.html)
  explains isolated project environments.
- The [uv project guide](https://docs.astral.sh/uv/guides/projects/) and
  [locking guidance](https://docs.astral.sh/uv/concepts/projects/sync/)
  describe committed locks and locked environment checks when `uv` is chosen.
