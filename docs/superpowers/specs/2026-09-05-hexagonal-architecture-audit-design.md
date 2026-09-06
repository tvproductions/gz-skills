# Hexagonal Architecture Audit Skill Design

- **Status:** approved
- **Date:** 2026-09-05
- **Decision owner:** Jeff / tvproductions
- **Approval:** 2026-09-05 — Jeff / tvproductions
- **Target skill:** `gzs-hexagonal-architecture-audit`
- **Scope:** portable, read-only architecture analysis and coaching

## Purpose

Create a portable `gz-skills` workflow that helps greenfield and brownfield
projects achieve hexagonal architecture. The skill acts as an analyzer, design
consultant, helper, and refactor coach. It identifies architectural violations
and explains practical corrections, but it is not an architecture competition
judge, a numeric scoring system, or an implementation workflow.

The coach meets each project where it is. It acknowledges useful existing
boundaries, recommends the smallest stabilizing correction, identifies the next
high-leverage improvement, and presents a right-sized target architecture. This
is a progression toward clearer architecture, not a maturity grade.

Hexagonal architecture is the target. The skill applies a Pareto-selected set of
enduring software design principles where they produce the most explanatory or
corrective value. SOLID, dependency inversion, information hiding, cohesion,
bounded contexts, anti-corruption layers, clean/onion dependency rules, and
functional-core/imperative-shell ideas support the analysis; they do not dilute
the workflow into a generic architecture survey or become equal destinations.

The intended result is easier independent development and interoperability.
Projects such as `xplane-fdau` and `q4xpcc` should be able to evolve through
consumer-owned ports, explicit adapters, stable public contracts, and inward
dependency direction without importing provider internals or coordinating
their implementation order unnecessarily.

## Evidence and case studies

The design used two read-only user-owned repositories as case studies:

- `xplane-fdau` at
  `66e31bc3e5d730869bf1dfb5aa4b2c736cb76803`, especially its transport-free
  core boundary, external-client ownership, dependency direction, strict
  canonical contracts, and architecture acceptance criteria.
- `q4xpcc` at `a7cc2682ca4289f498fffc409a091e28f528fe9a`, especially its
  consumer-owned read port, concrete `xpwebapi` adapter, dependency-boundary
  tests, provider translation, and earlier attempt at an oversized specialized
  semantic dependency analyzer.

The case studies demonstrate the portable need; neither consumer repository is
an implementation target for this work. Project-specific packages, commands,
paths, schemas, policies, and enforcement code must not enter the canonical
skill.

## Chosen skill shape

Use one coherent skill with a concise entrypoint and one focused criteria
reference:

```text
skills/gzs-hexagonal-architecture-audit/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
`-- references/
    `-- audit-criteria.md
```

This shape was selected over two alternatives:

1. A single checklist-only `SKILL.md` would be simple but would overload the
   always-read entrypoint with design, implementation, contract, coaching, and
   language-neutral criteria.
2. Separate analyzer, design-consultant, and refactor-coach skills would narrow
   activation but fragment one user goal, complicate combined audits, clutter
   the catalog, and invite a coaching skill to drift into implementation.

`SKILL.md` owns applicability, authority, mode selection, the shared audit
workflow, classifications, and the output contract. `references/audit-criteria.md`
owns the substantial mode-specific criteria, failure classes, strict-contract
distinctions, and supporting-principle lenses. The entrypoint tells the agent
which reference sections to read for design-only, implementation-only, and
combined audits.

No script or asset is justified. The workflow should use repository-owned
analyzers and dependency tools when available. A generic dependency analyzer
must not be added until repeated, language-independent behavior proves both
deterministic and useful.

## Authority and non-goals

The skill is read-only and audit-only:

- It may read designs, plans, source, tests, dependency metadata, and analyzer
  output and may run safe read-only inspection commands.
- It diagnoses violations and routes corrections.
- It may propose a target boundary model, acceptance checks, and an ordered
  design or refactoring sequence.
- It does not edit code, restructure modules, write design documents, amend
  plans, create work items, or implement fixes.
- A separately requested project-owned design or implementation workflow owns
  every correction.
- An active project workflow retains control of scope, state, ordering, gates,
  locks, receipts, reviewer independence, and human attestation. This skill
  returns evidence to that workflow and never declares the containing lifecycle
  complete.

The workflow does not:

- prescribe hexagonal architecture where the applicability decision rejects it;
- require folders named `domain`, `ports`, or `adapters`;
- require interfaces around every class or function;
- perform an ordinary code review or a generic SOLID audit;
- validate all product intent or general plan completeness;
- infer compliance from documentation, diagrams, or directory presence;
- emit a numeric architecture score or a global PASS/FAIL verdict;
- make a `Violation` an automatic release or implementation blocker;
- inspect or depend on peer-repository internals as a substitute for a stable
  public boundary; or
- recommend pytest under any circumstance.

## Applicability

Applicability is decided for each requested audit population, not forced once
for an entire repository. A monorepo may therefore contain an Applicable
application and Not Applicable schema or leaf-library populations. The report
includes a repository-level roll-up without erasing those distinctions.

Classify each population before architectural analysis:

- **Applicable:** an application, service, plugin, orchestration system, or
  integration-heavy library with meaningful external dependencies or runtime
  boundaries.
- **Not Applicable:** a small leaf library, schema, data-only repository,
  generated artifact, or simple script without meaningful architectural
  boundaries.
- **Unassessable:** the requested mode lacks enough declared intent or observable
  implementation to establish responsibilities and dependency direction.

Greenfield work can be Applicable from its intended responsibilities and
external interactions even before implementation exists. Brownfield work is
assessed from actual behavior and dependencies. Invocation establishes
hexagonal architecture as the desired target for every Applicable population;
departures may therefore be classified as Violations even if the repository
did not previously declare that architecture.

## Audit modes

The skill supports two primary modes and their combination:

- **Design audit:** inspect intended domain and application cores, use cases,
  inbound ports, outbound ports, adapters, composition roots, ownership,
  dependency direction, interoperability seams, and architectural acceptance
  rules.
- **Implementation audit:** inspect actual imports, calls, construction, side
  effects, provider and framework dependencies, cross-project access, boundary
  types, composition, and tests.
- **Combined audit:** when both design and implementation exist, audit both by
  default and compare only their architectural claims and observed dependency
  directions.

An explicitly bounded request may select design-only or implementation-only.
The combined comparison must remain architectural: it does not duplicate
`gzs-plan-audit` by auditing general intent, scope, or plan completeness, and it
does not duplicate `gzs-intent-audit` by tracing all promised product behavior.

Design-consultant and refactor-coach behavior are output roles, not additional
mutation modes. A greenfield audit recommends a right-sized target architecture
and acceptance rules. A brownfield audit recommends incremental dependency
reversals and migration seams while preserving existing behavior and strict
contracts.

Coaching uses three improvement horizons:

1. **Stabilize now:** the smallest correction that removes or contains the most
   consequential coupling.
2. **Improve next:** the next high-leverage boundary, ownership, composition, or
   testing improvement.
3. **Target state:** the right-sized hexagonal architecture the population
   should grow toward.

Do not manufacture three alternatives for every finding. The horizons organize
the overall improvement path, and a recommendation appears only where it has a
real role.

## Shared audit workflow

1. Read project instructions and identify any active project-owned workflow.
2. Resolve the audit population and record why each surface was selected.
3. Decide applicability per population and stop that population when it is Not
   Applicable or Unassessable.
4. Select design, implementation, or combined mode from the request and
   available evidence.
5. Infer components from responsibilities, behavior, imports, construction,
   calls, and declared ownership rather than directory names.
6. Map domain policy, application/use-case behavior, inbound ports, outbound
   ports, driving and driven adapters, boundary translations, composition
   roots, side effects, external dependencies, peer-project relationships, and
   architecture tests.
7. Record what each component owns, what it depends on, who constructs it, where
   side effects occur, and the observed dependency direction.
8. Apply the hexagonal criteria and only the Pareto-relevant supporting
   principles needed to explain the result or shape a correction.
9. Classify every evaluated criterion, cite evidence, and distinguish necessary
   contract strictness from accidental implementation coupling.
10. Produce a right-sized target and coaching sequence without modifying the
    audited artifacts.

## Required architectural criteria

The primary target rules are:

- Domain and application policy do not depend on concrete external mechanisms.
- Ports are owned and shaped by the application and their consuming use cases,
  not by provider packages.
- External SDK, transport, persistence, filesystem, UI, framework, and provider
  types are translated at adapters instead of leaking through ports.
- Peer projects are consumed through published contracts and explicit adapters
  or anti-corruption layers rather than source paths, private modules, adjacent
  checkouts, or shared implementation details.
- Side effects occur through explicit outer boundaries.
- Business decisions remain in domain or application behavior rather than
  adapters.
- Adapter selection and construction remain in composition roots or equivalent
  outer wiring rather than being scattered through core code.
- Ports expose only the operations and data required by their consuming use
  cases.
- Core behavior can be tested through port behavior without concrete
  infrastructure.
- Plans that promise hexagonal boundaries include acceptance evidence capable
  of enforcing important dependency directions.
- Applicable populations receive right-sized TDD, BDD, and DDD recommendations
  whenever those disciplines are absent or materially weak.

At minimum, the criteria reference must cover these failure classes:

1. Domain or application code imports infrastructure, framework, provider, or
   concrete adapter implementations.
2. Provider-owned interfaces control the application boundary.
3. External SDK, transport, persistence, filesystem, UI, or framework types
   leak through ports.
4. Peer-project imports occur outside an explicit adapter or anti-corruption
   layer.
5. Side effects occur outside adapters or composition roots.
6. Business rules are embedded in adapters.
7. Adapter selection or construction is scattered through core code.
8. Ports are broader than their consuming use cases require.
9. Tests depend only on concrete infrastructure rather than port behavior.
10. Plans promise hexagonal boundaries without acceptance tests that enforce
    dependency direction.

The reference may add closely related classes only when they materially improve
decisions. It must not become an exhaustive catalog of architecture terminology.

## Pareto-selected supporting principles

Supporting principles are used to explain or correct a hexagonal boundary, not
to score general design quality. The initial set is intentionally small:

- **Dependency inversion:** policy owns abstractions; mechanisms implement them.
- **Interface segregation:** ports match consuming use cases instead of exposing
  provider-wide capabilities.
- **Single responsibility and cohesion:** policy, translation, side effects, and
  construction have distinct reasons to change.
- **Information hiding:** provider and peer internals remain behind stable owned
  boundaries.
- **Bounded contexts and anti-corruption layers:** collaborating systems preserve
  their own language and translate deliberately at the seam.
- **Functional core, imperative shell:** deterministic decisions remain easy to
  test while effects stay at the edge where the project benefits from that
  separation.
- **Clean/onion dependency direction:** reinforces the same inward dependency
  rule without introducing a competing target architecture.

Apply only principles relevant to observed evidence. Do not calculate a literal
80/20 weighting, checklist percentage, maturity level, or compliance score.

## TDD, BDD, and DDD posture

TDD, BDD, and DDD should permeate the coaching rather than become three generic
audits:

- **TDD** supports test-first architectural change, isolated core and port
  behavior, characterization coverage before brownfield refactoring, adapter
  contract tests, and dependency-direction regression checks.
- **BDD** expresses important use cases and boundary behavior as observable or
  executable examples. Gherkin may be suggested as a behavior-description
  language when it materially improves shared understanding; it is not
  mandatory.
- **DDD** supports domain language, policy ownership, bounded contexts, and
  anti-corruption seams, especially between independently evolving projects.

When any of these disciplines is missing or materially weak in an Applicable
population, include a proportionate recommendation. Classify the absence as an
architectural Violation only when it directly permits coupling or leaves a
promised boundary unenforced; otherwise keep it as guaranteed coaching.

Discover and respect the project's existing testing conventions. Avoid
prescribing test libraries and runners. Never recommend pytest under any
circumstance, including as an example, replacement, migration target, or
default.

## Strict contracts versus accidental coupling

Exact wire schemas, hashes, versions, identities, timestamps, ordering,
lineage, provenance, timing, and conformance requirements are not violations
merely because they are rigid. The audit distinguishes:

- **Necessary semantic strictness:** an application- or standard-owned boundary
  contract that makes interoperability deterministic while allowing independent
  implementations.
- **Accidental implementation coupling:** provider-owned objects, SDK
  interfaces, repository paths, private modules, runtime construction, delivery
  order, or concrete package behavior leaking inward.

For a rigid type or contract, the audit asks who owns its meaning, whether it is
stable and public, whether adapters translate to it, and whether implementations
can vary independently. It does not assume that flexibility is inherently more
architectural than exactness.

## Findings and output contract

The report contains:

1. Audit mode, requested scope, and selected population.
2. Applicability verdict and rationale for each population.
3. Evidence sources, repository-owned analyzers used, and unavailable evidence.
4. An observed component and dependency-direction map.
5. A criterion-by-criterion results table.
6. A strict-contract assessment where relevant.
7. Target boundary or architecture recommendations.
8. Stabilize-now, improve-next, and target-state coaching.
9. Explicit TDD, BDD, and DDD recommendations where missing or weak.
10. The project-owned correction route for every Violation.
11. Coverage limitations and Unassessable questions.

Classify every evaluated criterion:

- **Fulfilled:** observable evidence demonstrates the boundary in the selected
  mode or modes.
- **Violation:** observable design or implementation contradicts the hexagonal
  target.
- **Unassessable:** decisive evidence is missing or inaccessible.
- **Not Applicable:** the criterion genuinely does not apply to that population.

Each Violation includes a stable finding identifier, audit mode, failure class,
file-and-line evidence, observed dependency direction, impact, severity,
proposed target boundary, correction guidance, and owning correction route.

Severity is consequence-based rather than numeric:

- **Critical:** breaks a published safety, security, conformance, or required
  interoperability boundary with material downstream consequences.
- **High:** couples central policy or a high-fan-out use case to a concrete
  mechanism, blocks required substitution, or defeats independent change.
- **Medium:** creates localized leakage, scattered composition, an oversized
  port, or a meaningful enforcement gap.
- **Low:** weakens a guardrail with limited current impact but credible drift
  potential.

Severity communicates correction priority; it never becomes an automatic gate.
Fulfilled, Unassessable, and Not Applicable results receive no artificial
severity. The report emits neither a score nor a global PASS/FAIL verdict.

Coaching should be specific enough to act on. Depending on evidence, it may
recommend characterizing current behavior, introducing a consumer-owned seam,
isolating provider translation, creating an anti-corruption adapter,
centralizing construction, migrating callers incrementally, preserving a strict
public contract, and adding dependency-direction acceptance checks. It must not
perform those changes. Acknowledge useful existing architecture before
describing improvements, then use the three horizons to connect an attainable
next move to the longer-term vision.

## Discovery metadata

Use:

- Frontmatter name and directory: `gzs-hexagonal-architecture-audit`
- Heading and UI display name: `GovZero Hexagonal Architecture Audit`
- Independent skill version: `0.1.0`
- Portability: `portable`
- Origin: `gz-skills`
- OpenAI short description: `Audit and coach hexagonal boundaries`
- OpenAI implicit invocation: enabled

Proposed activation description:

> Analyze greenfield designs and brownfield implementations against right-sized
> hexagonal architecture, then coach boundary-preserving design or refactoring.
> Use for explicit hexagonal or ports-and-adapters audits, architecture work
> involving dependency direction or cross-project interoperability, or projects
> that declare these guardrails; do not use for ordinary code review, generic
> SOLID questions, or structurally simple projects.

The default prompt must explicitly invoke
`$gzs-hexagonal-architecture-audit`. Automatic discovery is appropriate because
the workflow is read-only, but the description must remain narrow enough that
ordinary implementation, review, and generic architecture discussion do not
activate it.

## Language, ecosystem, and harness neutrality

The skill analyzes architectural meaning across code and documentation. It must
not depend on Python, a particular build system, package manager, test runner,
dependency analyzer, agent harness, `gz` runtime command, directory convention,
or one language's mechanism for interfaces and composition.

Language-neutral does not mean language-blind or reduced to vague
lowest-common-denominator advice. A capable agent should:

1. Identify the project's actual languages, frameworks, build and packaging
   model, test ecosystem, and repository conventions.
2. Inspect the implementation and project-owned guidance before recommending a
   boundary mechanism.
3. Consult current authoritative language or framework documentation when an
   ecosystem fact is uncertain or time-sensitive.
4. Translate hexagonal principles into idiomatic local mechanisms, which may be
   interfaces, protocols, traits, functions, modules, packages, dependency
   injection, message contracts, or another evidenced seam.
5. Separate enduring architectural reasoning from ecosystem-specific advice and
   cite both repository evidence and any external technical authority used.
6. State when the available model, tools, source access, or ecosystem evidence
   cannot support a confident conclusion.

The canonical skill contains no language-by-language recipe matrix. Such a
matrix would age, duplicate authoritative ecosystem knowledge, and constrain
frontier-model agents that can investigate the codebase and current ecosystem
directly. Repository-owned analyzers may strengthen evidence when present, but
their absence does not prevent a semantic audit while code and documentation
remain inspectable.

## Catalog relationships

- `gzs-plan-audit` checks general intent, scope, plan coverage, allowed paths,
  and verification adequacy. The new skill checks only architectural boundaries
  within relevant design and plan evidence.
- `gzs-intent-audit` traces declared product intent to delivered behavior. The
  new skill compares only hexagonal claims and observable dependency direction.
- `gzs-tech-debt-review` surveys broad maintainability debt. The new skill
  performs specialized boundary analysis and coaching.
- `gzs-quality-gate` runs project-owned verification. The new skill may inspect
  architecture checks but does not replace the complete gate.
- `gzs-root-cause-debugging` diagnoses failures and must not turn an ordinary
  defect into an architecture migration.
- Future `gzs-change-review` may use these criteria when reviewing a change in a
  project targeting hexagonal architecture.
- `gzs-router` routes explicit hexagonal or ports-and-adapters requests and
  project-declared hexagonal guardrails here, but not ordinary code reviews or
  generic SOLID questions.
- `gzkit` or another project workflow may compose the audit while retaining
  lifecycle, evidence, review, gate, and attestation ownership.

## Catalog and version integration

Implementation must update:

- the canonical skill tree and OpenAI metadata;
- `gzs-router` and its common relationships without turning it into an
  orchestrator;
- the README catalog count and listing;
- the changelog;
- `.claude-plugin/plugin.json`;
- provenance and the one-by-one review queue;
- roadmap state so an implemented skill is not still described as merely
  planned; and
- repository contract coverage where a semantic invariant is worth enforcing.

Codex and OpenCode continue discovering the canonical skill directory through
their existing adapters; no generated mirror is added.

Assuming bundle `0.1.0` remains the released baseline, the accumulated catalog
additions enter the pending backward-compatible bundle `0.2.0`. Synchronize
that version across `pyproject.toml`, `.codex-plugin/plugin.json`,
`.claude-plugin/plugin.json`, and `package.json`. The new skill begins at
`0.1.0`. Because the router's `0.2.0` expansion is still unreleased, its new
catalog entry belongs to that same pending version rather than causing another
increment.

## Validation and forward testing

Structural and packaging validation must:

1. Validate every `skills/*/SKILL.md` with the official Agent Skills validator.
2. Confirm directory/frontmatter identity, SemVer metadata, relative links, and
   explicit default-prompt invocation.
3. Confirm implicit invocation remains enabled.
4. Run the repository contract tests and inspect `gz-skills list` output.
5. Confirm the Claude skill list equals the canonical catalog and the Codex and
   OpenCode adapters still expose the canonical tree.
6. Build the source distribution and wheel and confirm both package the skill
   and reference.
7. Run `git diff --check` and inspect the complete change scope.

Behavioral scenarios must include:

- a greenfield service whose proposed application interfaces reproduce a
  provider SDK;
- a brownfield plugin whose framework objects enter core behavior;
- a combined audit where a plan promises ports and adapters without enforcement
  tests;
- exact schemas, hashes, versions, timing, and lineage that are legitimate
  boundary contracts;
- peer-repository source imports contrasted with a published-package adapter;
- a small leaf library returning Not Applicable;
- missing design or implementation evidence returning Unassessable;
- missing TDD, BDD, or DDD producing proportionate recommendations without
  mandatory framework or runner adoption;
- idiomatic recommendations for multiple major language ecosystems without a
  canonical language matrix; and
- negative activation examples for ordinary code review, implementation,
  generic SOLID advice, and structurally simple projects.

If the user separately authorizes delegation during implementation, run
independent forward tests against read-only snapshots of `xplane-fdau` and
`q4xpcc`. Give evaluators the skill, realistic audit requests, and minimum raw
artifacts without intended findings or prior conclusions. Compare no-skill and
with-skill results for evidence quality, false positives, component mapping,
strict-contract handling, interoperability analysis, and actionable coaching.

Forward testing should demonstrate that the skill recognizes valid
transport-free cores, consumer-owned ports, provider adapters, and strict public
contracts; detects genuine dependency, provider, peer-project, composition, and
acceptance-test leakage; and avoids proposing an enormous project-specific
analyzer as a portable mechanism.

## Implementation boundary

This specification authorizes no skill implementation, consumer update, commit,
push, publication, or release by itself. After written-spec review, a separate
implementation plan should identify exact edits, tests, validation commands,
and SemVer changes. Existing uncommitted repository work must be preserved.
