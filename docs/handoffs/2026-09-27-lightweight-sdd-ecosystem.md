# Lightweight SDD ecosystem: session handoff

Observed 2026-09-27 20:58 UTC in `gz-skills` on `main`. The pre-sync HEAD was
`27e0a58746b5b18b149ba5609d2e739cd1a8cba2` (`origin/main` at the time of
observation). This handoff and the candidate changes below were uncommitted at
observation; check current Git and remote state when resuming.

## Resume point

The user paused the ecosystem design discussion to request this handoff and a
Git sync. The integrated design is **not approved or complete**. After the sync,
resume with one question at a time about heavy-profile document authority. The
last unanswered question was whether every heavy project should have distinct
constitution and PRD documents before approving features, with ADRs for material
decisions. First inspect this handoff, the current worktree, and any newer
SP-Backplane design before asking it. Stop design implementation until the
relevant choices are settled; a profile choice alone does not install or prove
the heavy complement.

## Current repository work

- `skills/gzs-project-setup/` is a new **candidate** skill with a Python
  standard-library helper. It creates `.gz-skills/settings.json` with
  `schema_version: 1` and pending `profile`, asks for `lite` or `heavy`, blocks
  `.gzkit/` projects, preserves unfamiliar settings for manual reconciliation,
  and permits lite-to-heavy promotion. It does not perform cross-harness first-use
  activation, install SP/SP-BP/MPAS, or verify their alignment.
- `skills/gzs-router/SKILL.md` routes profile setup. `README.md` explains the
  candidate profile and native repo-scoped plugin posture. Bundle versions are
  pending `0.6.0` in the four manifests and lockfile; the new skill is `0.1.0`,
  router `0.3.2`. `CHANGELOG.md` records these as Unreleased. Marketplace
  manifests remain pinned to the **released** `v0.5.0`; no `0.6.0` release or
  publication has occurred.
- `tests/test_project_setup.py` and `tests/test_repository_contract.py` cover
  the new settings behavior and release-tag pinning. The repository's declared
  gates are in `README.md` under Validate. Prior to this handoff, unittest
  passed 28 tests, OpenCode Node tests passed 2, official `skills-ref`
  validation passed for all skill directories, `uv build` succeeded, and
  `git diff --check` passed. Re-run required gates before sync. **Never run
  pytest in the user's projects.**

## Settled direction from the user

- `gz-skills` is a standalone portable skill catalog. Lite means gz-skills
  only: no project-wide feature, requirements, backlog, or release management.
  The intended heavy complement is Superpowers (SP) as the spec/plan/workflow
  spine, SP-Backplane (SP-BP) for issue-backed backlog/features/releases,
  curated Matt Pocock Agent Skills (MPAS), and gz-skills governance. This is a
  lighter SDD ecosystem than gzkit. A consuming project with `.gzkit/` should
  be warned strongly that the two ecosystems are incompatible.
- Prefer repository-scoped **native plugin enablement** for Claude Code,
  Codex, and OpenCode. Do not copy physical skill trees into consuming projects.
  Python is an acceptable disclosed dependency. Avoid creating a central
  project lifecycle CLI. The existing Python snapshot installer is a released
  alternate contract; its future was not decided, so do not delete it by
  inference. Basic `.gz-skills/settings.json` is appropriate; its commit policy
  remains open.
- SP-BP, rather than gz-skills, owns FDAU-like taxonomy, requirements/features
  catalog, derived `ROADMAP.md` and `BACKLOG.md`, traceability, V&V, and release
  management. GitHub Issues (GHI) form the durable tracker/substrate for all
  entries, including features, proposals, bugs, defects, surprises, refactors,
  and releases. Link stable semantic IDs, GHI numbers, and SP specs/plans in
  issues. Approved enduring requirement wording belongs in governing project
  documents (constitution, PRD, architecture authority, ADRs), **not** issue
  bodies. A requirement becomes binding when its governing document change is
  approved; then reconcile its GHI and catalog. The stable ID lives at the
  definition and is referenced elsewhere. Keep catalog, roadmap, backlog,
  execution commitment, release target, and published tag distinct.
- Revisit SP-BP's earlier issue-only design and its prior exclusion of
  `ROADMAP.md`/`BACKLOG.md`; do not assume it remains authoritative. Strengthen
  the FDAU taxonomic design case and traceability/V&V with substantiated
  ISO/IEEE/FAA guidance and citations. Preserve FDAU origins, rules, and
  rationale. Avoid importing gzkit's ledger or full governance lifecycle.
- Heavy-project authority may involve constitution, PRD, ADRs, and architecture
  documents. Discover existing material, appropriate and adapt it where sound,
  or establish it through a **one-question-at-a-time grill-me** discussion.
  Curated MPAS likely includes adapted grill-me plus TDD and domain modeling;
  BDD integration is unresolved. The user advocates TDD, BDD, and DDD.

## Open design work

1. Resolve the unanswered document-authority question above; identify which
   documents are required and how approval works without imposing a premature
   template on every project.
2. Finish the SP/SP-BP/MPAS/gz-skills boundary and integration contract,
   including first-use activation across three harnesses, plugin version and
   alignment checks, and the exact curated MPAS subset.
3. Transfer the FDAU taxonomy and evidence into SP-BP design, explicitly
   superseding conflicting earlier SP-BP decisions. Define issue/catalog/view
   reconciliation, stable IDs, traceability, V&V, SemVer, and release lifecycle.
   No SP-BP or gzkit repository changes were made in this session.
4. Decide whether `.gz-skills/settings.json` should be committed by adopting
   projects. Keep heavy-to-lite reversal out of scope until separately designed.

## Authorization and next action

The current user request authorizes writing this handoff and normal Git commit
and push for the inspected candidate changes. It does not authorize tagging or
publishing `0.6.0`, modifying SP-BP/gzkit, or filling unsettled design choices
by implementation. After sync, report the actual commit SHA, remote alignment,
worktree state, and gate results. The next design session should resume the
document-authority question one at a time.
