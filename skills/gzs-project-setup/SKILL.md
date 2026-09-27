---
name: gzs-project-setup
description: Initialize or inspect a repository's GovZero skills profile. Use on first GovZero skill use in a project, when choosing lite or heavy, or when promoting an existing lite project to heavy; stop if the project uses gzkit.
compatibility: Requires Python 3.11 or newer for the setup helper.
metadata:
  govzero-version: "0.1.0"
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
   backlog, or release management. Heavy also calls for Superpowers,
   Superpowers Backplane, and a curated Matt Pocock skill set. Record the
   answer with `python scripts/project_settings.py select --project <root> --profile lite`
   or the same command with `heavy`.
   Do not infer a choice from
   installed tools.
4. Report the profile and the file created or found. For heavy, inspect each
   harness's installed plugins through its native facilities before claiming
   the complement is ready. Guide missing installs using that harness's
   project-scope plugin instructions; do not copy skill trees into the project.

On demand, a user may promote `lite` to `heavy` with `select`. The helper
rejects `heavy` to `lite`; reversal is not part of this version. Never edit
another project's settings or alter a gzkit project to make setup pass.

## Output

State the project root, current profile, and whether settings were created,
already present, or blocked. A heavy declaration alone does not prove its
plugins are installed, current, or aligned; report those checks separately.
