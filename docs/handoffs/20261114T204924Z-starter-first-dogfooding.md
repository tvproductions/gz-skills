# Starter-first dogfooding and lifecycle review handoff

Observed November 14, 2026, 20:49:24 UTC; local macOS arm64 checkout
`/Users/jbabb/Documents/Devel/gz-skills`, branch `main`, origin
`https://github.com/tvproductions/gz-skills.git`.
HEAD before this save point: `e3c908363a68a0a9f4d89a59612b194c59d06ed0`.
Fresh fetch showed ahead 0 / behind 0. The save-point commit is the subsequent
commit containing this file; locate it with
`git log -1 --format=fuller -- docs/handoffs/20261114T204924Z-starter-first-dogfooding.md`.

## Resume in the starter repository

The maintainer's latest direction is: “do a handoff and gitsync, I'll be making
most needed changes from the starter template repo.” Continue policy and shared
development-tooling design in
[gz-skills-first-starter](https://github.com/tvproductions/gz-skills-first-starter),
then reconcile applicable decisions here. This supersedes immediate local
implementation of the proposed dogfooding setup. No executable implementation
plan is active. The [design](../superpowers/specs/2026-11-14-published-dogfood-design.md)
is saved as a proposal, not an approved contract.

First permissible action: in the starter checkout, read its current AGENTS.md,
Git status and authoritative Astral/Python policy, compare with reviewed starter
commit `1c633f869ad3757961a4f734b0203eb558aaf718`, and use this handoff to identify
the shared policy work versus publisher-specific implementation. Expect a
bounded starter-owned design or requirements change that can later flow into
this repository's existing policy binding. Preserve unrelated starter changes;
the Git sync request here does not authorize committing another repository.
Resolve consequential design choices with the maintainer under the applicable
Superpowers workflow before implementing an unapproved proposal.

## Settled direction and proposed implementation

- User decisions: dogfood this project's **published skills and published Python
  CLI** as development dependencies; follow the starter's strict Astral project
  discipline; ask meaningful questions. Keep published output current as a driver
  of development here, rather than leaving installed gz-skills behind releases.
- Standalone skills remain a requirement. Their skill-local helpers travel with
  their directories. The installer CLI manages snapshots; skills do not acquire
  a shared CLI execution dependency. The current helper scripts are
  [project settings](../../skills/gzs-project-setup/scripts/project_settings.py)
  and [portability audit](../../skills/gzs-cross-platform-python/scripts/audit_portability.py);
  neither imports `gz_skills`.
- The separate locked `dev/published/` uv project, project Codex pin/configuration
  and post-publication development-pin promotion are **agent proposals** in the
  design. No such project, lock or project Codex configuration was created.
  The design approval question was not answered; a request to save the proposal
  does not approve its implementation.
- Strict Astral acceptance is incomplete. The reviewed starter requires an
  A01–A18 evidence matrix, routine hooks/CI, selected on-demand tools and actual
  compatibility/installed-artifact verification. None of those gaps is waived
  by existing routine checks. Re-read current starter authority before choosing
  exact changes. The starter's cognitive-engine qualification remains its own
  unresolved upstream dependency; do not invent a private scorer here.
- Do not bootstrap the starter bundle into this publisher, add consumer skill
  mirrors, introduce gzkit integration, or adopt Backplane implicitly. Policy
  flows from the starter; horizontal skill behavior remains portable.

## Local-only tooling changes actually completed

These installed/configured machine changes are outside the Git save point and
will not follow a clone:

- Native Codex 0.169.0 upgraded `gz-skills@gz-skills` from 0.8.3 to **0.12.0**.
  Its registered Git marketplace now selects `v0.12.0`. The published release
  commit is `a8f67160475a6995391d2244188d7c38eda65dfb`.
- Installed `superpowers@superpowers-dev` **7.0.2** from upstream tag `v7.0.2`;
  marketplace checkout resolved to
  `22f0b463e7a5e579904dd6211a520321035526f7`. Native installation enabled it in
  the **user configuration**. Project-only enablement has not been implemented;
  do not describe the current setup as project-scoped or reproducible from this
  repository. Reconcile that scope in the approved tooling work.
- The existing disabled `superpowers@skills-first-starter` and
  `gz-skills@skills-first-starter` choices were preserved. A structured before/
  after comparison found only the target marketplace repin and the new
  Superpowers marketplace/plugin entries changed; no unrelated config section
  changed. Do not publish private user config or alter managed plugin caches.
- A fresh `codex app-server` `skills/list` request with this repository's cwd and
  `forceReload: true` discovered **20** GZS and **15** Superpowers skills, no
  discovery errors. Qualified router/update paths resolve under installed
  `gz-skills/0.12.0`; brainstorming/using-superpowers resolve under installed
  `superpowers/7.0.2`. This proves discovery, not model workflow qualification.
- Superpowers `using-superpowers`, its Codex reference and `brainstorming` were
  read for the tooling proposal. Earlier lifecycle-role work used Superpowers
  as reference material; do not retroactively label it Superpowers execution.
- uv is **0.13.8**, using managed CPython **3.14.10** on arm64. Root environment
  still imports the candidate checkout. The independently pinned published CLI
  development consumer is **not installed/configured**. Temporary probes and a
  private config recovery copy exist locally; neither is portable evidence or
  a credential source for a future session.

## Durable review work and next evaluation

The [lifecycle contribution review](../review/lifecycle-fit-2026-11-14.md) maps
all twenty skills to needs, results and receiving owners. The
[review queue](../review/README.md) now includes lifecycle contribution and
distinguishes historical acceptance from qualification of current versions.
These are static instruction reviews; no skill body, activation, version or
runtime behavior changed.

After tooling decisions are reconciled, resume the focused assurance review:
plan audit, intent audit, change review and quality gate. Test standalone use,
an active Superpowers workflow and reuse of equivalent fresh checks already
completed by the owner. The role map is preparation, not behavioral acceptance.
Keep each skill's useful result distinct; do not turn four disciplines into
four mandatory new lifecycle gates. Make only corrections supported by evidence,
under the applicable authoring workflow and normal versioning rules.

## Release, validation and save-point authority

[v0.12.0 is published](https://github.com/tvproductions/gz-skills/releases/tag/v0.12.0);
the [release receipt](../evidence/2026-11-14-0.12.0-release.md) records immutable
identity, artifacts and all four tagged installation channels. This handoff
does not replace that receipt. No pending bundle/skill version exists: all
published skill trees and four bundle-version manifests are unchanged from the
release. The later changelog edit only links the completed release receipt.
This documentation save point requires no new release or version bump.

The latest request explicitly authorizes this handoff, repository checks,
ordinary commit and push. It does not authorize starter-repository commits,
design implementation or another consumer's propagation. Preserve the proposed
status and report Git alignment independently of tooling acceptance.

Observed save-point checks passed: **32 unittest tests**, Ruff lint and format
(84 Python files), ty, all **20 Agent Skills validators**, `uv lock --check`,
`uv build --no-sources --out-dir dist/handoff-20261114` (sdist and wheel), and
`git diff --check`. Generated artifacts are ignored local files, not a release.
Repository contract tests cover relative links, frontmatter names and explicit
OpenAI default prompts. The twenty activation descriptions were reviewed in the
lifecycle role assessment; they remain unchanged from v0.12.0 and establish no
new behavioral evidence. Fresh GitHub queries found no open issues or PRs. No
pre-commit configuration or hosted quality CI currently exists here; full strict
Astral acceptance remains outstanding, and a local gate must not be described
as hosted evidence. Final command results and remote alignment are recorded in
the Git sync response for this commit.
