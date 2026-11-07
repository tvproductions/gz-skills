---
name: gzs-project-setup
description: Initialize or inspect a repository's GovZero skills profile. Use on first GovZero skill use in a project, when choosing lite or heavy, or when promoting an existing lite project to heavy; stop if the project uses gzkit.
compatibility: Requires Python 3.11 or newer for the setup helper.
metadata:
  govzero-version: "0.4.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Project Setup

Keep the project's profile in `.gz-skills/settings.json`. The only initial
fields are `schema_version` and `profile`. `profile` is `null` until the user
chooses `lite` or `heavy`. The file is project configuration, not an installed
skill copy or proof that other plugins are available.

## Project Python version and policy

For Python work, read project instructions and adopted policy before selecting
idioms, APIs or runtime targets. Resolve version evidence from the relevant
project's `.python-version` first, `pyproject.toml` second, and `.venv` third.
The version file records an execution selection; `requires-python` declares a
support range; the environment supplies an observed installed version. Use later
signals for fallback and consistency checks, not to override declared policy.
Inspect `pyvenv.cfg` and the environment interpreter when available; do not
create, activate or update an environment just to discover its version.

Reconcile these signals with tool/CI targets and the actual validation
interpreter. Report absent, ambiguous or conflicting evidence; do not infer
freshness from an installed version or a minimum supported version from one pin.
For host-bound code, inspect the host runtime separately; a development
interpreter does not establish the host's version or installed packages.

Within this skill's existing task scope, observe the selected family's current
Python idioms, stdlib advances and deprecations using versioned official
documentation. Preserve the project's tested support range and public behavior;
record concrete benefits, risks and adopt/defer/retain decisions. Follow project
policy over upstream defaults. A runtime upgrade alone does not establish code
currency, and this guidance does not authorize a broad modernization campaign or
turn this skill into a comprehensive Python-version audit.

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

## Project customization

Read the adopter's instructions, governing documents, and any starter's adopted
policy before applying defaults. Keep application dependencies, optional features,
development groups, settings, and project-owned skills or adapters. Extend the
existing declarations for the requested work rather than replacing them with a
closed baseline. Project-specific additions and reviewed exceptions belong in
the project's guidance and manifests; an approved project policy takes precedence
over this skill's environment recommendations.

Keep application settings in the project's existing configuration namespace or
separate settings file. Its loader owns defaults, override precedence, collection
merging, and validation. `.gz-skills/settings.json` accepts only `schema_version`
and `profile`; do not put application settings or customization keys there.
Changing that contract requires a separately designed and tested schema migration.

Customize workflows through project instructions, documented commands, or a
separate project-prefixed skill that may compose a `gzs-*` primitive. Preserve
upstream identifiers and managed plugin caches. A vendored skill with local edits
requires reconciliation before its locked snapshot can be updated. Record which
project policy supplies each departure so later maintenance preserves it.

## Heavy Python environment guidance

Resolve the consuming project's governing runtime and engineering authority
before selecting a family, tool assortment or package policy. If the project
has adopted a starter, read its recorded revision and applicable baseline;
that authority supplies the standards. Preserve approved local exceptions.
A mode selection does not adopt a starter or establish a Python/tool baseline.

Report the effective authority, selected family, exact development pin, declared
support range, host constraints and required verification separately. A stored
pin is execution evidence, not the source of policy. If governing policy is
missing, inaccessible or contradictory, keep that decision unresolved and ask
for the missing authority; do not fill it with a library-maintained default.
The rest of a bounded settings operation may proceed where independent of it.

Use only the consuming project's required tools and package choices. Do not
supply a second standard assortment, reintroduce retired analyzers or impose
runtime-package exclusions. Selecting heavy does not authorize unrelated tool
installation, a family change or replacement of approved project dependencies.
Use the project's update workflow or `gzs-update-dependencies` for authorized
reconciliation, preserving its managed-file, environment and verification rules.

For host-bound code, determine the actual loading boundary and inspect the host
interpreter separately. A version pin alone does not prove host orientation.
Verify startup and packages in the real host; the standalone development
environment cannot establish host compatibility. Keep development tools out of
shipped runtime dependencies unless the product actually uses them as libraries.

On demand, a user may promote `lite` to `heavy` with `select`. The helper
rejects `heavy` to `lite`; reversal is not part of this version. Never edit
another project's settings or alter a gzkit project to make setup pass.

## Output

State the project root, current profile, and whether settings were created,
already present, or blocked. A heavy declaration alone does not prove its
plugins are installed, current, or aligned; report those checks separately.
