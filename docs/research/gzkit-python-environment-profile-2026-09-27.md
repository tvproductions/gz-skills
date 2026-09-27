# gzkit Python and tool profile for heavy-project guidance

Read-only observation on 2026-09-27 from `gzkit` commit
[`3960c214`](https://github.com/tvproductions/gzkit/tree/3960c214e1c35f7d55810ed65fced9da3b351894).
Its worktree had unrelated active changes; the files referenced here were not
among them. This inventory comes from [`pyproject.toml`](https://github.com/tvproductions/gzkit/blob/3960c214e1c35f7d55810ed65fced9da3b351894/pyproject.toml)
and [`.python-version`](https://github.com/tvproductions/gzkit/blob/3960c214e1c35f7d55810ed65fced9da3b351894/.python-version).
It records declared tools, not a recommendation to copy them all.

| Surface | Declared value |
| --- | --- |
| Python development pin | `3.13.15` in `.python-version` |
| Package support | `requires-python = ">=3.13"` |
| Astral tools | `ruff>=0.16.2` for lint and format; `ty>=0.0.69` for type checking. The repository uses `uv`, but does not declare a uv version in `pyproject.toml`. |
| Build | `hatchling` build backend, without a version constraint |
| Tests and behavior | `unittest-parallel>=1.7.2`, `behave>=1.3.3`, `coverage>=7.15.4` |
| Security checks | `bandit>=1.9.4`, `detect-secrets>=1.5.0` |
| Code analysis | `cohesion>=1.2.0`, `interrogate>=1.7.0`, `lizard>=1.23.0`, `pygount>=3.2.0`, `radon>=6.0.1`, `vulture>=2.16`, `wily>=1.12.2`, `xenon>=0.9.3` |
| Packaging and docs | `pyinstaller>=6.22.0`; `mkdocs==1.6.1` and `mkdocs-material==9.7.7` appear in both the `dev` group and `docs` extra |

These are the 18 declared development tools plus the build backend and Python
policy. `radon`, `lizard`, and `cohesion` also appear as runtime dependencies
because gzkit measures adopter source code. The exact resolved versions are in
its `uv.lock`; the constraints above are what the project itself declares.

For heavy-project guidance, review each tool by the capability it supplies.
The Python pin/range distinction, uv workflow, Ruff, ty, testing, and coverage
are plausible defaults. Behave, PyInstaller, documentation generators,
security scanners, and code-metric tools depend on the adopter's product and
risk. gzkit's exact versions, prohibition on pytest, and governance-specific
checks are not automatically inherited.
