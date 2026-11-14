# Skill roadmap and backlog

Reconciled: 2026-11-14. This is the repository's planning index; detailed
contracts and evidence remain in the linked records. The order below is the
recommended next-work order, not approval to implement or publish a proposal.
It introduces no issue graph or adopting-project lifecycle.

## Delivered releases

The latest published and verified release, `v0.12.0`, adds actionable routing,
standalone/Superpowers-complementary workflow guidance and direct dependency
updates, with current locked development tools. Its
[release receipt](evidence/2026-11-14-0.12.0-release.md) records immutable source,
artifacts and all four tagged installation checks. Release `v0.11.0` added Git
sync release follow-through and corrected gate applicability and dependency-update
authority.
Its [release receipt](evidence/2026-11-14-0.11.0-release.md) records publication,
artifact identities and all four tagged installation checks. Release `v0.10.1`
corrected uv_build packaging; see its [receipt](evidence/2026-11-08-0.10.1-release.md).
Release `v0.10.0` removed the gzkit installer surface and
integration examples; see the [release receipt](evidence/2026-11-08-0.10.0-release.md)
for its publication and channel status. The earlier release is `v0.9.0`:
project setup and dependency update follow
consumer-owned Python policy, while this publisher independently selects Python
3.14. The [release receipt](evidence/2026-11-07-0.9.0-release.md) records its scope
and verification. Twenty canonical skills remain; the `v0.8.3` patch previously
promoted the accepted Git sync contract to skill 1.0.0. The
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

## Completed 0.11.0 scope

Published minor **0.11.0** adds Git sync release follow-through and includes
both corrections: pre-implementation gate applicability and dependency
update authority. It supersedes unpublished 0.10.2 because the release checkpoint
is compatible new capability. The maintainer requested sync and publication and
asked for version increments to lead reliably to new releases.

Requirements: identify unpublished package/component versions against actual
remote releases, including committed pending work; discover publication authority;
complete authorized releases through their owning workflow; honor explicit
no-release instructions and report deferred or blocked publication. Bind that
standing authority only in this repository. Preserve project gates, immutable
release identity, explicit invocation and consumer-owned publication policy.

Acceptance: static scenario review for authorized publication, ordinary sync,
explicit deferral, committed pending versions, no version bump and unavailable
remote evidence; the existing full repository/skill/native-plugin/package gates;
then an immutable GitHub release and tagged installs in each supported channel.
The [release receipt](evidence/2026-11-14-0.11.0-release.md) records classification,
checks and actual publication boundaries. No new runtime helper, lifecycle state,
setup schema, registry channel or automatic consumer update is included. Native
model behavioral qualification and the remaining stable-review backlog stay
separate. All release gates and tagged channel checks passed; the selected
scope is complete. No further minor scope is selected.

## Completed 0.12.0 scope

Published minor **0.12.0**, against baseline v0.11.0, serves reliable task
initiation and completion. The maintainer expanded the completed dependency
maintenance scope to include adopter workflow guidance learned from Superpowers.
Direct dependency invocation completes updates; router action requests enter the
owning workflow, while explicit checks/recommendations remain read-only.

The guide must teach both gz-skills independently present and complementary use
alongside installed Superpowers. It must explain typical requests, outputs,
transitions, decision points and completion; preserve active project/Backplane
ownership and avoid redundant processes, gates or handoffs. Neither installation
case chooses a profile or proves integrated heavy readiness. The existing
first-use/hook/schema proof work below remains separate.

Included: dependency skill 0.4.2 → 0.5.0, router 0.5.1 → 0.6.0, its packaged
workflow reference, prominent adopter README guidance and locked current Python
tools. Both changed contracts require minors during 0.x; bundle 0.12.0 covers
the complete coherent scope across its mirrors. No major PRD or stable
promotion is required. Runtime family, installer/lock/setup contracts and optional components
remain unchanged. No new required orchestrator or authored harness mirror.

Acceptance: standalone and complementary scenario review, preserved advice-only
and consequential-operation boundaries, metadata/activation/link checks, full
required repository checks, native candidate loading and installed package proof
including the new reference. Native model execution, automatic session bootstrap
and heavy compatibility qualification must be reported separately. The
[maintenance receipt](evidence/2026-11-14-dependency-maintenance.md) retains its
original completed scope/evidence; the
[workflow case review](review/adopter-workflows-2026-11-14.md) records the extension
and final candidate checks. The subsequent explicit Git sync authorized 0.12.0
publication under AGENTS.md; all release gates, GitHub asset verification and
four tagged installation checks passed. Marketplace pins and examples name
v0.12.0. The [release receipt](evidence/2026-11-14-0.12.0-release.md) records
source, artifacts, publication and limits. The selected scope is complete; no
next minor scope is selected. Existing-consumer propagation remains separate.


## Current backlog

| Order | Work | Status and owner | Next action and completion evidence |
| ---: | --- | --- | --- |
| 1 | One-by-one stable-contract reviews | In progress; gz-skills | Git sync has [stable-contract acceptance](review/gzs-git-sync-2026-10-25-acceptance.md). The [dependency-update initial review](review/gzs-update-dependencies-2026-11-08.md) is complete: keep corrected candidate 0.4.1, with the initial finding closed. Native baseline and execution evidence are next for stable acceptance. Quality gate is next without an initial review. Router invocation-guidance findings remain separate. Cover all twenty skills in the [review queue](review/README.md). |
| 2 | Migrate Hatchling to uv_build | Delivered in v0.10.1; gz-skills | Backend and resource lookup migrated; package/CLI proof is in the [migration receipt](evidence/2026-11-08-uv-build-migration.md), and publication/tagged channel checks are in the [release receipt](evidence/2026-11-08-0.10.1-release.md). |
| 3 | First-use and heavy-profile integration | Candidate design; gz-skills with SP/SP-BP and adopter owners | Prove native discovery, direct/model-selected routing, hook-independent operation and task resumption on supported harnesses. Design and test any settings schema migration and publish a verified compatibility set. Selecting heavy alone is insufficient. |
| 4 | Four attributed MPAS adaptations | Proposed catalog additions; gz-skills | Pin upstream sources, verify attribution/licenses, adapt the four named skills, define refresh maintenance and test interactions. Follow the [ecosystem proposal](proposals/lightweight-sdd-ecosystem.md); do not require a fourth installed plugin. |
| 5 | Opt-in repository baseline | Discussion proposal; ownership undecided | Decide source ownership, accept a baseline specification and run read-only pilots before implementing audit/apply or delivery workflows. See the [baseline handoff](proposals/repository-baseline-bootstrap.md). |

Backlog reconciliation itself is complete in this documentation update: the
review queue includes all twenty implemented skills, shipped additions are
separate from proposals, and closed issue #1 is retained as resolution history.
No other open GitHub issues or PRs were found in the preceding 2026-10-25 check;
that observation is a dated snapshot, not a continuously synchronized view.

## uv_build migration acceptance

Added November 8, 2026 at the maintainer's direction. gz-skills has a strict
Astral/uv alignment preference, consistent with the canonical starter policy.
The intended default for this pure-Python package is `uv_build`. Earlier
release-scope deferrals are history, not a technical blocker or permanent waiver.

The migration preserves supported package behavior, not Hatchling's
implementation or byte-for-byte equality between the two backends:

1. Replace Hatchling configuration with a verified, appropriately constrained
   `uv_build` requirement. Resolve how the canonical root `skills/` tree reaches
   the installed package without adding separately authored skill copies.
2. Verify wheel and sdist contain all twenty current skill trees and their
   44 canonical resources, with file contents matching the selected source.
   Preserve bundled-resource lookup, package imports and the `gz-skills` entry point.
3. From outside the checkout, verify installed catalog discovery and public
   install/update behavior, lock provenance and local-modification protection.
   Preserve supported surfaces, invocation contracts and the ecosystem boundary.
4. Verify editable installation and source-independent `uv build --no-sources`;
   exclude generated caches and unrelated development files. Two builds from
   the same source must be reproducible; archives from different backends need
   not be byte-identical.
5. Run the repository's required gates and package checks. Classify actual
   compatibility impact against published v0.10.0 before selecting a pending
   version; record migration evidence and any demonstrated exception.

The maintainer subsequently authorized implementation on November 8, 2026.
The selected patch shipped as 0.10.1 against published v0.10.0: a compatible
packaging-policy correction that preserves public CLI, lock and skill behavior.
Its finite scope includes uv_build configuration, installed resource lookup,
regression/package checks and evidence. No skill tree changes, new capabilities,
stable-contract promotions, consumer updates or publication are included.
Acceptance is the five criteria above and the complete repository gate; the
[migration receipt](evidence/2026-11-08-uv-build-migration.md) records proof and
limits. The next minor remains 0.11.0 with scope unselected.

If another backend proves necessary, record the concrete need, evidence,
maintainer approval, owner and dated revisit condition. Do not infer a blocker
merely from the existing resource-copy layout. This repository preference does
not impose an Astral backend on unrelated portable-skill consumers.

## Selected pending 0.10.0 scope

The scope selected below has shipped as v0.10.0; its title preserves the original
planning anchor. Publication and all required tagged channel checks are verified
in the release receipt. The next minor number is 0.11.0, with scope unselected.

Baseline: published v0.9.0. Outcome: enforce the maintainer's separate lightweight
alternative boundary, with no designed gzkit interoperability. Included work:
remove `--surface gzkit`, replace integration-specific skill examples with
standalone/general project guidance, and reconcile review and boundary records.
The removed installer option is incompatible during 0.x, requiring minor
0.10.0; the four affected skills receive compatible patch increments detailed
in the changelog. All bundle mirrors and generated lock metadata agree.

Acceptance: the CLI must reject the removed surface before writing; remaining
installer behavior and setup exclusion must pass the repository tests; all
skill specification, identity, prompt and link checks and package builds must
pass. Existing consumer installs and release refs remain untouched. Full native
stable-contract acceptance, heavy integration, MPAS additions and baseline
proposals are deferred. The maintainer subsequently authorized release of this
selected scope; the release receipt records its status. The scope does not
claim stable acceptance.

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

- It solves one horizontal engineering goal and works standalone; this ecosystem
  is a lightweight alternative to gzkit, with no designed interoperability.
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
- An active adopting-project review workflow continues to own
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
- An active adopting-project workflow continues to own task dispatch, allowed paths, stage transitions,
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
