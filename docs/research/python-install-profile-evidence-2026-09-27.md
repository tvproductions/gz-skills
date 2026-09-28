# Python install profile evidence

Read-only inventory on 2026-09-27 of `pyproject.toml` and `.python-version`
under `C:/Users/Jeff/source/repos/{agents,va,xp}`. Local worktrees may contain
uncommitted changes; this records observed files, not released package claims.
The user supplied the local interpreter observations for the XP projects; those
are distinct from checked-in version pins.

| Project | Declared Python | Local pin | Relevant development tools and role |
| --- | --- | --- | --- |
| `agents/gz-skills` | `>=3.13` | 3.13.15 | Portable skill package and Python helpers; uv lock, Hatchling build. |
| `va/gzkit` | `>=3.13` | 3.13.15 | uv, Ruff, ty, unittest-parallel, Behave, Coverage, Bandit, detect-secrets, code metrics, MkDocs, PyInstaller. [Detailed inventory](gzkit-python-environment-profile-2026-09-27.md). |
| `va/rhea` | `>=3.13` | 3.13.13 | Ruff; gzkit consumer. |
| `va/flightops` | `>=3.13,<3.14` | none found | Hatchling, Ruff and ty configuration, pre-commit. |
| `va/airlineops` | `>=3.13` | 3.13 | Ruff, ty, Coverage, Behave and documentation tools; data/automation runtime dependencies. |
| `va/caprock-web` | `>=3.14,<3.15` | 3.14 | Ruff, ty; web application. |
| `va/caprock-connect` | `>=3.14,<3.15` | 3.14 | Documentation tools; connector. |
| `xp/q4xpcc` | `==3.12.*` | 3.12.13 | Direct XPPython3 plugin; uv, Ruff, ty, Radon, Lizard, Cohesion, Xenon. Reported local interpreter 3.12.14. |
| `xp/xplane-fdau` | `>=3.12,<3.13` | 3.12 | Standard-library-only future XPPython3/XPLM core; uv, Ruff, ty, Coverage and additional QA tools. Reported local interpreter 3.12.14. |
| `xp/xplane-webapi` | `>=3.12,<3.14` | 3.13 | External Web API client; uv, Ruff, ty, Coverage, HTTP/WebSocket runtime packages. Reported local interpreter 3.13.14. |
| `xp/Ortho4XP` | `>=3.13,<3.14` | 3.13.14 | Separate scenery generator; uv, Ruff, ty, Coverage, GIS/numerical packages. Reported local interpreter 3.13.15. |
| `xp/xpcl` | `>=3.9` | none found | Separate telemetry UI; PySide6, pynng, uv, Ruff, ty. Reported local interpreter 3.13.14. |

The inventory supports a common **development-tool** baseline, but not one
interpreter range for all products. Python 3.13 is the practical default in
the sampled general-purpose projects; existing 3.14 projects remain valid.
Direct XPPython3 code has a narrower 3.12 runtime target. Web API, scenery,
and telemetry programs do not inherit that target merely because they belong
to the X-Plane ecosystem. A checked-in `.python-version` is a development
request, not evidence that every supported minor was tested.
