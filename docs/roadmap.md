# Skill roadmap and backlog

Reconciled: 2026-10-25. This is the repository's planning index; detailed
contracts and evidence remain in the linked records. The order below is the
recommended next-work order, not approval to implement or publish a proposal.
It introduces no issue graph or adopting-project lifecycle.

## Delivered releases

The `v0.8.3` patch retains twenty canonical skills and promotes the accepted
Git sync contract to skill 1.0.0. The
[README catalog](../README.md) lists them and the [changelog](../CHANGELOG.md)
records their release history. Implemented capabilities include project profile
setup, Pythonic pattern detection/application, Python-version-aware guidance,
and the release primitive. Implementation does not establish stable-contract
acceptance or integrated heavy-profile readiness.

[Issue #1](https://github.com/tvproductions/gz-skills/issues/1) is closed.
Discovery/fallback declarations and their regression check shipped in v0.4.0;
the remaining quality-gate final-step contradiction was corrected in
`c5703ef12061217a2866fbb9f482f168f768a193`. The `0.8.1` release includes that
correction (quality-gate skill `0.1.2`) and router `0.5.1`; see the
[release record](https://github.com/tvproductions/gz-skills/releases/tag/v0.8.1)
for publication, artifacts and channel-install evidence.

## Current backlog

| Order | Work | Status and owner | Next action and completion evidence |
| ---: | --- | --- | --- |
| 1 | One-by-one stable-contract reviews | In progress; gz-skills | Git sync 0.1.1 has [stable-contract acceptance](review/gzs-git-sync-2026-10-25-acceptance.md) with native execution evidence; `gzs-update-dependencies` is next unreviewed. Router 0.5.1 has selected native inference evidence; ungrounded host-invocation claims remain a separate finding. Cover all twenty skills in the [review queue](review/README.md); record individual decisions and behavioral evidence before claiming stable acceptance. |
| 2 | First-use and heavy-profile integration | Candidate design; gz-skills with SP/SP-BP and adopter owners | Prove native discovery, direct/model-selected routing, hook-independent operation and task resumption on supported harnesses. Design and test any settings schema migration and publish a verified compatibility set. Selecting heavy alone is insufficient. |
| 3 | Four attributed MPAS adaptations | Proposed catalog additions; gz-skills | Pin upstream sources, verify attribution/licenses, adapt the four named skills, define refresh maintenance and test interactions. Follow the [ecosystem proposal](proposals/lightweight-sdd-ecosystem.md); do not require a fourth installed plugin. |
| 4 | Opt-in repository baseline | Discussion proposal; ownership undecided | Decide source ownership, accept a baseline specification and run read-only pilots before implementing audit/apply or delivery workflows. See the [baseline handoff](proposals/repository-baseline-bootstrap.md). |

Backlog reconciliation itself is complete in this documentation update: the
review queue includes all twenty implemented skills, shipped additions are
separate from proposals, and closed issue #1 is retained as resolution history.
No other open GitHub issues or PRs were found in the preceding 2026-10-25 check;
that observation is a dated snapshot, not a continuously synchronized view.

## External dependencies and ownership

The [ecosystem proposal's remaining work](proposals/lightweight-sdd-ecosystem.md#remaining-design-and-proof-work)
also depends on SP-BP's issue-kind/relationship schema, reconciliation,
traceability and V&V, snapshot-derived views, release gate and migration pilots.
Those contracts, Python implementation, ADRs and tests belong in SP-BP; this
index neither approves them nor establishes their current implementation state.
Superpowers retains feature specification and execution ownership. Adopters own
governing-document approval, runtime choices and project verification.

## Completed 0.3.0 promotion history

The sections below preserve the promotion contracts for `gzs-change-review`,
`gzs-dependency-risk-audit` and `gzs-test-driven-change`. They are implemented
catalog members, not future additions. They extend the portable-primitives layer
without introducing an alternate planning, execution, review or closeout lifecycle.

## Shared architecture

Every roadmap skill must satisfy the same composition rules:

- It solves one horizontal engineering goal and remains useful without `gzkit`.
- It discovers repository-owned commands and policies instead of embedding a
  project toolchain, branch model, or governance ceremony.
- An active project-owned workflow retains control of scope, ordering, state,
  gates, locks, receipts, reviewer independence, and human attestation.
- It neither creates parallel lifecycle state nor declares a containing
  workflow complete.
- Diagnosis or review does not silently expand into implementation. External or
  remote mutation requires authority from the request or governing workflow.

## Historical promotion order

1. `gzs-change-review`
2. `gzs-dependency-risk-audit`
3. `gzs-test-driven-change`

This was the promotion order for the completed 0.3.0 additions, not the current
backlog priority or stable-contract review order.

## `gzs-change-review`

### Promoted goal

Review a bounded implementation change for defects, regressions, unsafe
assumptions, and maintainability risks, then return prioritized findings backed
by concrete repository evidence. The primary output is an actionable review,
not an approval ritual or a rewritten patch.

### Expected activation

Use when a user asks for code review, diff review, pre-merge review, regression
review, or an independent assessment of a completed change. Do not activate for
a request that merely asks to run tests, compare delivery with an owning
specification, survey repository-wide technical debt, or implement a feature.

### Workflow contract

1. Resolve the review base, changed-file set, stated intent, and repository
   rules before judging the patch.
2. Read the changed code in context, including immediate callers, consumers,
   tests, error paths, and relevant public contracts.
3. Examine correctness, edge cases, compatibility, security boundaries,
   failure behavior, operability, and maintainability in proportion to the
   change's risk.
4. Prove each retained finding with a reachable scenario, violated invariant,
   failing check, or precise code path. Exclude taste-only commentary and state
   uncertainty when evidence is incomplete.
5. Rank findings by user or system consequence and present findings before any
   summary. Do not edit the change unless separately authorized.

### Relationship to the catalog

- `gzs-quality-gate` executes the project's declared automated checks;
  `gzs-change-review` supplies human-style semantic inspection that automation
  may not encode.
- `gzs-intent-audit` asks whether shipped behavior fulfills authoritative
  intent; `gzs-change-review` asks whether this implementation introduces a
  concrete defect or risk.
- `gzs-tech-debt-review` surveys a scoped surface for accumulated debt;
  `gzs-change-review` stays anchored to a particular change and its regressions.
- A gzkit review stage may compose this discipline, but gzkit continues to own
  reviewer roles, independence requirements, receipts, verdicts, and gates.

### Promotion basis

- Severity and evidence rules were reconciled from proven user-owned review
  implementations.
- Positive triggers such as “review this diff” and negative triggers such as
  “run the full test suite” or “fix these findings” are separated in the
  activation description and workflow boundaries.
- Findings require a reachable scenario, violated invariant, failing check, or
  precise code path, which filters speculative and stylistic noise.
- Ordinary review requests allow implicit activation while remediation remains
  separately authorized.

## `gzs-dependency-risk-audit`

### Promoted goal

Assess the risk carried by a project's direct and transitive dependencies
without automatically upgrading them. The audit should turn manifests,
lockfiles, authoritative advisories, compatibility constraints, maintenance
signals, and repository usage into a prioritized decision record.

Relevant risk classes include known vulnerabilities, unsupported versions,
abandonment or low maintenance capacity, license incompatibility, dependency
confusion or provenance concerns, excessive privilege or install-time behavior,
single-maintainer concentration, transitive duplication, and upgrades blocked
by runtime or platform constraints. A risk class is included only when evidence
for that ecosystem is available.

### Expected activation

Use when a user asks to audit dependency risk, supply-chain exposure,
vulnerable or abandoned packages, license compatibility, or whether a
dependency remains safe to retain. Do not activate for a straightforward “bring
all dependencies current” request, a machine-wide software audit, or a general
application security review.

### Workflow contract

1. Inventory every owning manifest, lockfile, runtime pin, package source, and
   generated dependency surface within the requested scope.
2. Distinguish direct choices from transitive resolution and identify where the
   project actually imports, executes, bundles, or distributes each relevant
   dependency.
3. Query current authoritative ecosystem and advisory sources when available,
   recording timestamps and source limitations because risk data changes over
   time.
4. Evaluate exploitability and operational relevance in project context rather
   than treating every advisory or stale version as equal.
5. Report the affected surface, evidence, consequence, feasible response, and
   confidence for each retained finding. Keep upgrades, removals, exceptions,
   and external issue creation separately authorized.

### Relationship to the catalog

- `gzs-update-dependencies` changes project-managed versions and verifies the
  resulting tree; `gzs-dependency-risk-audit` is read-first decision support and
  may recommend retaining, replacing, constraining, or upgrading a dependency.
- `gzs-tech-debt-review` may flag dependency drift as one category;
  `gzs-dependency-risk-audit` performs the deeper ecosystem, provenance, and
  project-exposure analysis.
- `gzs-root-cause-debugging` may diagnose a failure caused by a dependency, but
  it does not assess the dependency portfolio.
- A consuming security or release workflow owns its risk thresholds, exception
  policy, remediation deadlines, and attestations.

### Promotion basis

- The contract was checked against Python/uv and Go module surfaces while
  preserving ecosystem-specific graph, lock, advisory, and license semantics.
- It defines an authoritative-source hierarchy and an honest offline fallback.
- It handles conflicting and withdrawn advisories, unreachable registries,
  private packages, and incomplete transitive graphs explicitly.
- Its activation boundary excludes dependency updating, general security
  auditing, and machine or infrastructure patch management.

## `gzs-test-driven-change`

### Promoted goal

Apply a tight red-green-refactor loop to one authorized behavior change. The
skill should make the failing test a meaningful negative control, implement the
smallest behavior that satisfies it, and preserve fast feedback while the
project's containing workflow retains ownership of the broader delivery.

### Expected activation

Use when the user explicitly asks for test-driven development, a test-first
change, or a red-green-refactor implementation. Do not activate merely because
any implementation request could benefit from tests. Skip or adapt when the
work has no executable behavioral surface, and never invent a low-value test
solely to perform the ceremony.

### Workflow contract

1. Confirm the authorized behavior, its observable seam, and the smallest next
   example before editing production code.
2. Write one test that expresses the missing behavior through the real public or
   stable internal surface with the least necessary mocking.
3. Run it and verify an assertion-level failure for the intended reason. Import,
   collection, fixture, or environment errors are not a valid red.
4. Implement the minimum behavior needed to make that test pass, then re-run
   the focused test and relevant neighboring coverage.
5. Refactor only after green, preserving observable behavior, and repeat for the
   next independent example rather than batching all tests or all production
   code.
6. Return focused evidence to the active project workflow. Run or recommend
   `gzs-quality-gate` only when the containing workflow does not already own the
   complete verification stage.

### Relationship to the catalog

- `gzs-root-cause-debugging` establishes an unknown cause; once a fix is
  authorized, `gzs-test-driven-change` can encode the demonstrated failure as a
  regression witness and drive the correction.
- `gzs-plan-audit` checks whether an implementation plan is adequate;
  `gzs-test-driven-change` governs only the inner implementation loop.
- `gzs-quality-gate` verifies the completed repository change;
  `gzs-test-driven-change` supplies focused incremental evidence and does not
  replace the full gate.
- gzkit continues to own task dispatch, allowed paths, stage transitions,
  independent review, receipts, attestation, and closeout around the loop.

### Promotion basis

- The contract is framework-neutral and prescribes no test layout, command, or
  mocking library.
- It covers legacy code, characterization tests, nondeterminism, migrations,
  generated artifacts, and a minimal importable scaffold.
- Activation is limited to explicit TDD, test-first, or red-green-refactor
  requests so ordinary implementation and project-owned execution retain
  control.
- Assertion-level red evidence remains mandatory, preventing an evidence-free
  ceremony.

## Promotion record

Each promoted skill:

1. Has provenance and a portable invariant recorded from real repository use.
2. Lives with OpenAI metadata under the canonical `skills/` tree.
3. Encodes intended and unintended activation, mutation authority, and project
   workflow precedence.
4. Was compared with its source behavior and negative-trigger baseline.
5. Is present in plugin manifests, `gzs-router`, provenance, changelog, and the
   one-by-one review queue.
6. Enters the catalog at independent skill version `0.1.0`.

## Candidate under discussion

An [opt-in repository baseline handoff](proposals/repository-baseline-bootstrap.md)
records maintainer direction and cross-project evidence from 2026-09-20.
It is a proposal, not an approved implementation specification or catalog addition.
