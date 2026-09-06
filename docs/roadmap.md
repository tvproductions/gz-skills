# Near-term skill roadmap

This roadmap records the next planned additions to `gz-skills`. They extend the
portable-primitives layer established by `gzs-root-cause-debugging`; they do not
introduce an alternate planning, execution, review, or closeout lifecycle.

These names describe intended public contracts, but the skills are not yet
installable, versioned, or available through `gzs-router`. Promotion requires a
canonical `skills/<name>/` implementation, provenance evidence, activation and
negative-trigger review, behavioral scenarios, and the full repository
validation suite.

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

## Planned order

1. `gzs-change-review`
2. `gzs-dependency-risk-audit`
3. `gzs-test-driven-change`

The order reflects current readiness, not importance. A later skill may move
forward first if its portable contract and provenance become clearer sooner.

## `gzs-change-review`

### Intended goal

Review a bounded implementation change for defects, regressions, unsafe
assumptions, and maintainability risks, then return prioritized findings backed
by concrete repository evidence. The primary output is an actionable review,
not an approval ritual or a rewritten patch.

### Expected activation

Use when a user asks for code review, diff review, pre-merge review, regression
review, or an independent assessment of a completed change. Do not activate for
a request that merely asks to run tests, compare delivery with an owning
specification, survey repository-wide technical debt, or implement a feature.

### Proposed workflow

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

### Promotion criteria

- Establish consistent severity and evidence rules from proven user-owned
  review implementations.
- Test positive triggers such as “review this diff” and negative triggers such
  as “run the full test suite” or “fix these findings.”
- Demonstrate that the skill finds substantive defects without generating
  speculative, stylistic, or scope-expanding noise.
- Decide whether ordinary review requests justify implicit activation while
  keeping remediation separately authorized.

## `gzs-dependency-risk-audit`

### Intended goal

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

### Proposed workflow

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

### Promotion criteria

- Prove a vendor-neutral core across at least two package ecosystems without
  pretending their advisory, licensing, and lock semantics are identical.
- Define an authoritative-source hierarchy and honest offline fallback.
- Specify how to handle conflicting advisories, withdrawn vulnerabilities,
  unreachable registries, private packages, and incomplete transitive graphs.
- Validate negative triggers against dependency updating, general security
  auditing, and machine or infrastructure patch management.

## `gzs-test-driven-change`

### Intended goal

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

### Proposed workflow

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

### Promotion criteria

- Extract a framework-neutral contract that works beyond Python and does not
  prescribe test file layout, commands, or mocking libraries.
- Define useful handling for legacy code, characterization tests, nondeterminism,
  migrations, generated artifacts, and changes whose first valid red requires a
  minimal importable scaffold.
- Test that activation remains narrow enough not to hijack ordinary
  implementation or project-owned execution workflows.
- Demonstrate behavioral improvement over a no-skill baseline without turning
  red-green-refactor into evidence-free ceremony.

## Promotion process

For each planned skill:

1. Confirm provenance and the portable invariant from real implementations.
2. Draft the skill and its OpenAI metadata under the canonical `skills/` tree.
3. Review intended and unintended activation, mutation authority, and project
   workflow precedence.
4. Run a no-skill baseline and with-skill behavioral scenarios.
5. Add the promoted skill to plugin manifests, `gzs-router`, provenance,
   changelog, and the one-by-one review queue.
6. Assign independent skill version `0.1.0` only when the installable contract
   enters the catalog.
