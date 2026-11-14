# Evening three-repository continuation — November 14, 2026

## Canonical gz-starter migration — November 14 follow-up

The maintainer explicitly chose execution of the rename/migration tonight.
GitHub is now `tvproductions/gz-starter`, verified to retain the same repository
ID and history. The checkout is relocated to `gz-starter`. GZ Starter is the
display name. Pending distribution/CLI is `gz-starter` at **0.10.0**, from
published 0.9.0; no extra per-task version bump or release publication occurs.

The old `skills-first-starter` command remains an equivalent alias. The Python
import `skills_first_starter`, marketplace/plugin IDs and `.skills-first/`
provenance directory remain intentional compatibility interfaces. New source
URLs/provenance use the canonical repository; historical adoption records and
immutable receipts remain intact. Source detection accepts old and new origins.
The update skill remains `update-gz-template`. See the starter's
`docs/rename-gz-starter.md` for reviewed downstream migration guidance; no blanket
downstream edits or native cache/user-scope activation were performed.

The paired designs remain drafts. Their format examples now use
`gz-starter-records/v1` and `gz-starter-commit/v1`, not activated schemas.
Current draft SHA-256: starter 951a78aa9ddfdce7bfe88b38888deafaa0f0bf32d968142e180a47c3029aea61; Backplane f680c70202138c77d34a881f0e081c32f17847b1bf34c9390ad6d0ddd9b8e0e6.
Earlier hashes below identify the pre-rename drafts and remain historical.
No sidecar/ledger/Backplane workflow implementation is authorized by naming work.

The relocated starter environment and four normal hooks were rebuilt from the
same locked dependency selections on Python 3.14.10; the new and legacy commands
both report 0.10.0. The desktop app's primary-folder binding requires the user:
Computer Use cannot control the app, and no project-folder edit API is exposed.
The old folder contains only a temporary relocation notice for the active chat,
not a second checkout. Remove that placeholder after the desktop task/project
has been rebound and no active runtime depends on it.

Companion names, versions and remotes are unchanged. All three repositories must
receive follow-up commits/sync and exact-final CI observation where configured.
No tag/release is authorized. The original wrap-up commits below remain valid
save points, not the final renamed-candidate identities.

Verified canonical starter migration is pushed at
`5845e8fb488f0674636a6c1748e3f0a97e1d8c08` on `origin/main`.
[Exact-commit CI](https://github.com/tvproductions/gz-starter/actions/runs/43647770059)
passes both configured jobs: the four routine checks, catalog validation,
source-independent build/installed verification and separate X-Plane baseline.
Canonical and legacy CLI checks pass; external dependency selections are
unchanged. This is sync/rename evidence, not release acceptance or publication.

Backplane companion migration is pushed at
`c1b63d8f72fba9996f0857120f8c97e9e8d5700d`; its four normal hooks pass.
[Exact-commit three-platform CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/43647870548)
is observed through completion by the coordinating sync before its final report.
All 32 gz-skills repository unittest tests pass again after these documentation
changes. Earlier unchanged-source Ruff/format/ty and 20-skill checks remain
applicable; no hosted workflow is configured here. Final transport identities
and CI results belong to the final sync response, without receipt-only commits.

## Prior wrap-up save point (superseded by the migration above)

The maintainer explicitly requested handoffs and ordinary Git synchronization
for **all three** coordinated repositories: GZ Starter, gz-skills and Backplane.
Keep designs as drafts, implement nothing and publish no release. This current
instruction supersedes earlier cross-repository authorization limits below and
controls the repository's conditional sync/publication standing rule. GZ Starter
is the short conversational name; canonical identifiers remain unchanged.

The shared discussion is preserved in the starter's
`docs/handoffs/2026-11-14-opinionated-cli-design-discussion.md` and paired drafts:

- Starter repository `tvproductions/gz-skills-first-starter`:
  `docs/superpowers/specs/2026-11-14-lite-record-and-commit-contract-draft.md`.
- Backplane repository `tvproductions/superpowers-backplane`:
  `docs/superpowers-backplane/specs/2026-11-14-lite-record-and-commit-alignment-design.md`.

Read those candidates before dependent design changes. Starter sidecars follow
Backplane semantic cues; they do not redefine its authority. JSON structured
facts, Markdown narrative/generated views, a hand-written changelog, Git history
and bounded recovery are selected. No SQLite, Dolt, permanent ledger or gzkit
integration is selected. A small typed per-commit JSON record in a Git trailer
is proposed for the project binding, not implemented in portable skills or
imposed on unrelated consumers. Preserve four routine checks where adopted.
Superpowers remains the feature inner loop. No cloud execution is requested.

Starter cognitive qualification is explicitly deferred across its two lanes,
retaining ceiling 15, eventual qualification, UNKNOWN measurement and conditional
acceptance without strict-conformance claims. A separately maintained gzkit-derived
engine is future project work: small Python API/CLI with eventual PyPI/uv
distribution, MCP/plugins deferred. This is starter policy/direction, not a
blanket exception imposed on unrelated gz-skills consumers or a delivered engine.

gz-skills remains at published v0.12.0, with no pending skill/bundle behavior or
version changes. This handoff/changelog-only save point requires no release or
version bump. No skills, helpers, profiles, runtime pins, locks, native settings
or published tags are changed. Existing standalone helper and published-dogfood
proposals remain as recorded below; do not remove helpers before a reviewed
ownership/migration decision or implement the unapproved dogfood proposal.

Next work here remains the assurance-role review (plan audit, intent audit,
change review, quality gate), under the reconciled shared design and published
development-tooling decision. Keep standalone and active-owner use, evidence
reuse, native discovery and actual behavioral qualification distinct. The
starter's draft commit contract grants no new portable lifecycle ownership.

Use existing locked validation and preserve hooks if present. This repository
currently has no configured hosted quality CI; report that limitation rather
than inventing exact-commit CI success. Confirm final remote/main alignment and
clean worktree in the sync response. Previous observations below remain history.

Observed evening checks: fresh fetch gives main ahead/behind 0/0; actual
manager is uv 0.13.8 on managed Python 3.14.10. All 32 unittest tests pass;
Ruff check, format (84 Python files), ty and all 20 Agent Skills validations
pass. The unchanged skill identities, relative links and explicit OpenAI
prompts are covered by repository tests; activation descriptions remain exactly
the published v0.12.0 descriptions. No current model-workflow qualification is
inferred. These are local checks; hosted quality CI is not configured here.

Companion save points now verified on their respective origin/main branches:

- GZ Starter: `454c59643013bd9aea4c5e3f4760ab873b86934e`;
  [immutable draft](https://github.com/tvproductions/gz-skills-first-starter/blob/454c59643013bd9aea4c5e3f4760ab873b86934e/docs/superpowers/specs/2026-11-14-lite-record-and-commit-contract-draft.md).
  Both exact-commit jobs pass in
  [run 43645889085](https://github.com/tvproductions/gz-skills-first-starter/actions/runs/43645889085),
  including the full four-check gate, catalogs, build/installed proof and the
  separate X-Plane baseline. These are sync checks, not strict release acceptance.
- Backplane: `5822c6b78acd08d7f90faefaf984f257c625d7a4`;
  [immutable paired draft](https://github.com/tvproductions/superpowers-backplane/blob/5822c6b78acd08d7f90faefaf984f257c625d7a4/docs/superpowers-backplane/specs/2026-11-14-lite-record-and-commit-alignment-design.md).
  All four normal commit hooks pass and local adapter checks pass 9/9.
  Exact-commit three-platform CI is observed separately in the final sync response.

Their designs remain drafts after committing. No release was published. The
maintainer's unnamed additional final item was never specified; do not infer
another requirement. GZ Starter naming is included with canonical IDs preserved.
No gz-skills source/version changes are needed to save these coordination facts.

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
