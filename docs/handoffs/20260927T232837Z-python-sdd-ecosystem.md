# Python SDD ecosystem: session handoff

Observed 2026-09-27 23:28 UTC in `gz-skills` on `main` at
`39c830a9cfd15748fbc43b1e2637d4a9527e620c`. The worktree was clean and
local `main` matched `origin/main` after the preceding git-sync. Recheck both
when resuming; this observation is not a claim about later remote state.

## Resume point

Continue the adopting-project lite/heavy SDD ecosystem from the
[candidate design](../proposals/lightweight-sdd-ecosystem.md), not from the
[older superseded handoff](2026-09-27-lightweight-sdd-ecosystem.md). The latest
result is the committed Python alignment and clarified project boundaries in
`39c830a`. First check the separate SP-BP agent's current ADR, plan, branch, and
worktree: the user explicitly requires a **Python SP-BP project**, but reported
that agent had implemented something in Go. The SP-BP checkout visible from
this session was clean on `plan/issue-19-claude-lifecycle-draft`; the reported
Go work was not visible here, and its location and migration status are
unverified. The next observable result is an SP-BP design and implementation
path that preserves useful Go prototype behavior while replacing its core with
Python. Do not disturb unrelated SP-BP work or infer that a correction posted
in this chat reached its separate agent.

## Settled decisions and ownership

- `gz-skills`, Superpowers (SP), and Superpowers Backplane (SP-BP) are the three
  intended installed components. Four attributed MPAS adaptations are planned
  inside `gz-skills`, not as a fourth required plugin. The full documents,
  identity, taxonomy, traceability, V&V, view, and release decisions are in the
  candidate design; do not repeat the earlier grilling sequence.
- SP-BP's catalog, issue reconciliation, trace and V&V logic, view generation,
  release logic, CLI/helpers, and tests belong in Python. Thin host-specific
  adapters may use the language a harness requires and delegate to that core.
  No Go core, service, module, or parallel implementation is intended. SP-BP's
  exact Python runtime and packaging policy remain its own design decision.
- This repository's development interpreter is pinned to Python `3.13.15` in
  [`.python-version`](../../.python-version). The pending Python package floor
  is `>=3.13` in [`pyproject.toml`](../../pyproject.toml) and `uv.lock`.
  The standalone `gzs-project-setup` helper still supports Python 3.11 or newer;
  do not silently apply this repository's package floor to every adopting
  project or to SP-BP without its own decision.
- The [README](../../README.md), [AGENTS guidance](../../AGENTS.md), and
  [`gzs-project-setup`](../../skills/gzs-project-setup/SKILL.md) reflect these
  boundaries. This design is a candidate, not a shipped heavy workflow.
- The [Python environment baseline](../guides/heavy-python-environment.md) is
  working candidate guidance for adopting heavy Python projects. Review the
  [gzkit tool profile](../research/gzkit-python-environment-profile-2026-09-27.md)
  before selecting default tools; do not copy gzkit's full stack. The candidate
  covers a declared support range, isolated and locked dependencies, and
  project-owned gates, with brownfield migration and project-specific versions.

## Completed and verified here

- `7bd8f8d` committed the candidate design; `e5e3a39` updated README/AGENTS;
  `39c830a` aligned Python tooling and clarified the SP-BP Python boundary.
  All three commits were pushed to `origin/main`. No SP-BP files were edited,
  committed, or pushed from this session.
- At the final sync, 28 Python unit tests, all 17 Agent Skills validations, two
  OpenCode adapter tests, `uv lock --check`, `uv build`, and staged diff checks
  passed. The `0.6.0` wheel metadata declared `Requires-Python: >=3.13`.
- The latest immutable release remains `v0.5.0`. Bundle `0.6.0` and
  `gzs-project-setup` 0.1.0 are pending candidates; no tag or channel
  publication was performed. The release contract and gates are in
  [`docs/packaging.md`](../packaging.md) and [`CHANGELOG.md`](../../CHANGELOG.md).

## Follow-on work

1. Reconcile the SP-BP agent's actual artifacts with the Python requirement.
   Its own ADR, plan, README, and AGENTS.md need to state the Python core and
   document any Go-to-Python migration. Coordinate through that agent's active
   session; this handoff does not authorize overwriting its worktree.
2. In `gz-skills`, prove first-use setup routing on Codex, Claude Code, and
   OpenCode, including direct and model-selected invocation when hooks are
   unavailable. Define and migrate any extension of the shared settings schema.
3. Curate the four MPAS adaptations with source-commit attribution and a
   maintenance chore. Keep the SP and SP-BP ownership boundaries in the
   candidate design.
4. Pilot the integrated flow in an adopting project after SP-BP's schema and
   release design have been reconciled. Verify only the harnesses that project
   declares. Treat the proposal's remaining proof list as the detailed scope.
5. Review the gzkit Python tool profile with the user and select which tools
   become defaults for new heavy Python projects. Keep the guide marked
   candidate until those choices are settled.

The user authorized creating and git-syncing this handoff in `gz-skills`.
That authorization does not publish `0.6.0`, change SP-BP, or grant a future
unrelated commit or push.
