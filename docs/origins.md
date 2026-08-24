# Extraction evidence

The first portable skills were distilled on 2026-08-23 from clean, committed
skill surfaces in the following repositories. Revisions are full Git object
identities so later work can distinguish the observed implementation from a
newer edit.

## `gzs-git-sync`

- `tvproductions/gzkit` at
  `5dcb96f2bb8d5c0fd5777fad8449b5200c1d67a4`:
  `src/gzkit/skills/git-sync/SKILL.md`
- `tvproductions/xplane-health` at
  `ce1852fd0e6f0dbb1e4c39badb95b8b7a6fbbec6`:
  `.agents/skills/gz-git-sync/SKILL.md`
- `tvproductions/q4xpcc` at
  `a7cc2682ca4289f498fffc409a091e28f528fe9a`:
  `.codex/skills/git-sync/SKILL.md`
- `tvproductions/xplane-webapi` at
  `a855b8d885c75f8dda54daec1f54eb48f111b105`:
  `.codex/skills/git-sync/SKILL.md`
- `tvproductions/airlineops` at
  `a972f08bc0f4f6d6a05178362529b50cc0798583`:
  `.agents/skills/git-sync/SKILL.md`

Shared behavior retained: whole-tree scope review, repository-owned quality
gates, guarded commit, non-destructive remote reconciliation, push, and final
ahead/behind verification. Project commands, branch defaults, test frameworks,
and governance ceremonies were left local.

## `gzs-update-dependencies`

- `tvproductions/gzkit` at
  `5dcb96f2bb8d5c0fd5777fad8449b5200c1d67a4`:
  `src/gzkit/skills/gz-deps-upgrade/SKILL.md`
- `tvproductions/q4xpcc` at
  `a7cc2682ca4289f498fffc409a091e28f528fe9a`:
  `.codex/skills/refresh-dependencies/SKILL.md`
- `tvproductions/xplane-webapi` at
  `a855b8d885c75f8dda54daec1f54eb48f111b105`:
  `.codex/skills/hygiene/SKILL.md`

Shared behavior retained: complete dependency-surface inventory, live
authoritative version resolution, owning-tool lock regeneration, coherent
updates, full project verification, and precise reporting of constrained or
unverifiable results. Python versions, package lists, artifact inventories, and
project-specific acceptance commands were left local.

## `gzs-quality-gate`

- `tvproductions/gzkit` at
  `5dcb96f2bb8d5c0fd5777fad8449b5200c1d67a4`:
  `src/gzkit/skills/gz-check/SKILL.md`
- `tvproductions/airlineops` at
  `a972f08bc0f4f6d6a05178362529b50cc0798583`:
  `.agents/skills/quality-gate/SKILL.md`
- `tvproductions/Ortho4XP` at
  `e528b20d61e26b91250061a819f3f88b632c7087`:
  `.codex/skills/quality-check/SKILL.md`

Shared behavior retained: discover the repository's authoritative gates, run
them at the right scope, distinguish failures from unavailable checks, and
report evidence without inventing success.

## `gzs-repository-hygiene`

- `tvproductions/gzkit` at
  `5dcb96f2bb8d5c0fd5777fad8449b5200c1d67a4`:
  `src/gzkit/skills/gz-tidy/SKILL.md`
- `tvproductions/q4xpcc` at
  `a7cc2682ca4289f498fffc409a091e28f528fe9a`:
  `.codex/skills/repo-hygiene/SKILL.md`
- `tvproductions/Ortho4XP` at
  `e528b20d61e26b91250061a819f3f88b632c7087`:
  `.codex/skills/maintenance-qa/SKILL.md`

Shared behavior retained: inspect before cleanup, classify generated and
tracked artifacts from repository policy, use recoverable actions, and verify
that cleanup did not damage the working tree.

## `gzs-session-handoff`

- `tvproductions/gzkit` at
  `5dcb96f2bb8d5c0fd5777fad8449b5200c1d67a4`:
  `src/gzkit/skills/gz-session-handoff/SKILL.md`
- `tvproductions/airlineops` at
  `a972f08bc0f4f6d6a05178362529b50cc0798583`:
  `.agents/skills/gz-session-handoff/SKILL.md`

Shared behavior retained: capture objective, state, evidence, decisions,
constraints, and the next executable action while avoiding stale narrative.

## `gzs-agent-context-diet`

- `tvproductions/gzkit` at
  `5dcb96f2bb8d5c0fd5777fad8449b5200c1d67a4`:
  `src/gzkit/skills/gz-context-diet/SKILL.md`

The portable invariant is to measure persistent agent context, remove
duplication and stale detail, preserve authority and routing, and validate that
shorter context still enables correct work.

## `gzs-plan-audit`

- `tvproductions/gzkit` at
  `5dcb96f2bb8d5c0fd5777fad8449b5200c1d67a4`:
  `src/gzkit/skills/gz-plan-audit/SKILL.md`
- `tvproductions/airlineops` at
  `a972f08bc0f4f6d6a05178362529b50cc0798583`:
  `.agents/skills/gz-plan-audit/SKILL.md`

Shared behavior retained: audit a plan against current repository evidence,
surface hidden assumptions and missing verification, and amend only when the
plan's authority permits it.

## `gzs-intent-audit`

- `tvproductions/gzkit` at
  `5dcb96f2bb8d5c0fd5777fad8449b5200c1d67a4`:
  `src/gzkit/skills/gz-intent-trace/SKILL.md`

The portable invariant is to trace stated intent through decisions,
implementation, tests, and documentation, distinguishing divergence from
deliberate evolution.

## `gzs-tech-debt-review`

- `tvproductions/gzkit` at
  `5dcb96f2bb8d5c0fd5777fad8449b5200c1d67a4`:
  `src/gzkit/skills/gz-tech-debt-review/SKILL.md`

The portable invariant is an evidence-based debt review that distinguishes
maintainability risk from preference and prioritizes findings by consequence.

## `gzs-cross-platform-python`

- `tvproductions/airlineops` at
  `a972f08bc0f4f6d6a05178362529b50cc0798583`:
  `.agents/skills/cross-platform/SKILL.md`

The portable invariant is to audit Python and project automation for operating
system assumptions, replace accidental platform coupling with standard-library
or repository-owned seams, and test representative path and process behavior.

## `gzs-router`

- `tvproductions/gzkit` at
  `5dcb96f2bb8d5c0fd5777fad8449b5200c1d67a4`:
  `src/gzkit/skills/gz-skill-router/SKILL.md`

The portable invariant is a user-invoked curator that maps an immediate goal to
the smallest useful skill or sequence without executing the selected workflow.
The source router's decision-tree pattern credits `using-agent-skills` from
`addyosmani/agent-skills` under MIT; the portable catalog and routing text here
were rewritten for GovZero's independently authored skills.
