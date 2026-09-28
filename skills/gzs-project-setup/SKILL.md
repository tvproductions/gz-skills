---
name: gzs-project-setup
description: Initialize or inspect a repository's GovZero skills profile. Use on first GovZero skill use in a project, when choosing lite or heavy, or when promoting an existing lite project to heavy; stop if the project uses gzkit.
compatibility: Requires Python 3.11 or newer for the setup helper.
metadata:
  govzero-version: "0.2.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Project Setup

Keep the project's profile in `.gz-skills/settings.json`. The only initial
fields are `schema_version` and `profile`. `profile` is `null` until the user
chooses `lite` or `heavy`. The file is project configuration, not an installed
skill copy or proof that other plugins are available.

## Discovery and fallback

Find the active project root from the repository or harness context. If it is
unclear which project should receive settings, ask before writing. Run this
skill's [settings helper](scripts/project_settings.py) with an explicit
`--project` path. It uses only the Python standard library. If Python is
unavailable, explain that setup needs Python and leave the project untouched.
Do not use the bundle's vendoring installer for this workflow.

## First use

1. Inspect the project with `python scripts/project_settings.py inspect --project <root>`.
   A `.gzkit/` directory means this
   ecosystem is incompatible with the project: strongly advise the user to
   back out and use gzkit, and do not create `.gz-skills/` or continue setup.
2. If settings are absent, run `python scripts/project_settings.py initialize --project <root>`.
   This creates a minimal pending file.
   Existing valid settings are preserved. A malformed or unexpected file is
   reported for reconciliation, never replaced.
3. If the profile is pending, ask **one question**: lite or heavy? Lite uses
   the portable `gzs-*` skills without project-wide feature, requirements,
   backlog, or release management. Heavy also calls for Superpowers and the
   Python-based Superpowers Backplane. The planned attributed Matt Pocock
   adaptations belong in this `gz-skills` catalog, not a fourth plugin. Record the
   answer with `python scripts/project_settings.py select --project <root> --profile lite`
   or the same command with `heavy`.
   Do not infer a choice from
   installed tools.
4. Report the profile and the file created or found. For heavy, inspect each
   harness's installed plugins through its native facilities before claiming
   the complement is ready. Guide missing installs using that harness's
   project-scope plugin instructions; do not copy skill trees into the project.

## Heavy Python environment guidance

When a heavy adopter implements in Python, inspect its `pyproject.toml`,
`.python-version`, lockfile, CI, and actual host runtime before recommending
changes. A 3.12.x pin hints at XPPython3 orientation; confirm whether code
loads in XPPython3 or is shared with it. Recommend the latest supported
3.12.x patch for that profile and 3.13.x for ordinary Python. Keep the exact
development patch in `.python-version` and the tested support range in
`requires-python`; update CI and the committed lock together.

Guide both profiles toward one development assortment: uv, Ruff, ty; Bandit,
Vulture, Interrogate, detect-secrets; standard-library unittest, Coverage,
Behave, unittest-parallel, Cosmic Ray; Radon, Xenon, Lizard, Cohesion; MkDocs
and MkDocs Material. Prefer uv_build for pure-Python distributions, verifying
wheel/sdist content and installed resources during migration. PyInstaller is
available when a project ships a standalone executable. The project's
quality gate defines scan scopes, thresholds, mutation targets, and commands;
do not copy gzkit's numeric floors. Refresh current compatible versions through
the project's update workflow or `gzs-update-dependencies` when available.

Start shipped code with the standard library. Pydantic is an approved runtime
option for the ordinary Python profile, not for the XPPython3-oriented profile.
Other runtime packages need a product capability and verification under the
actual interpreter. Keep development tools out of the shipped runtime unless
the product explicitly uses one as a library. For XPPython3-loaded code,
test plugin startup against the real host and do not mistake the development
environment for the host's site-packages. After the user selects `heavy`,
reconcile missing or stale standard tools, interpreter pin, development group,
lock, and CI through the project's own update workflow or
`gzs-update-dependencies` when installed. A profile selection does not prove
the checks run: report completed work and any unresolved compatibility or
packaging migration before claiming environment readiness.

On demand, a user may promote `lite` to `heavy` with `select`. The helper
rejects `heavy` to `lite`; reversal is not part of this version. Never edit
another project's settings or alter a gzkit project to make setup pass.

## Output

State the project root, current profile, and whether settings were created,
already present, or blocked. A heavy declaration alone does not prove its
plugins are installed, current, or aligned; report those checks separately.
