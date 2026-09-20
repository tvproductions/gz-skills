---
name: gzs-hexagonal-architecture-audit
description: Analyze greenfield designs and brownfield implementations against right-sized hexagonal architecture, then coach boundary-preserving design or refactoring. Use for explicit hexagonal or ports-and-adapters audits, architecture work involving dependency direction or cross-project interoperability, or projects that declare these guardrails; do not use for ordinary code review, generic SOLID questions, or structurally simple projects.
compatibility: Inspectable code or design documentation in any language/ecosystem.
metadata:
  govzero-version: "0.1.1"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Hexagonal Architecture Audit

Analyze architectural boundaries and coach a right-sized path toward hexagonal
architecture. Audit concepts and behavior, not preferred folder names or the
mere presence of interfaces, dependency injection, or diagrams.

## Authority

This is a read-only audit. Inspect designs, plans, source, tests, dependency
metadata, and analyzer output, and run only safe read-only probes. Never edit
audited code, restructure modules, write architecture documents, amend plans,
create work items, or implement corrections.

Read project guidance and identify any active project-owned workflow first.
Return findings to that workflow and honor its scope, state, ordering, gates,
locks, receipts, reviewer independence, and attestation. Do not duplicate,
bypass, or declare its lifecycle complete. Every correction belongs to a
separately authorized project-owned design or implementation route.

Discover and respect local test conventions. Do not prescribe a test runner or
library, and never recommend pytest.

## Discovery and fallback

Prefer, in order:

1. An active project-owned design or architecture workflow, which receives the
   findings and owns every correction.
2. Dependency or import analyzers the repository already configures.
3. The import statements and module boundaries read directly from source.

The third rung is the floor and is sufficient for the core question, because
dependency direction is visible in the imports themselves. An analyzer reports
it faster; it does not report anything the source does not already say.

## Population and mode

Decide the requested audit population independently before applying criteria;
a repository may contain populations with different verdicts:

- **Applicable:** applications, services, plugins, orchestration systems, and
  integration-heavy libraries with meaningful external dependencies or runtime
  boundaries.
- **Not Applicable:** small leaf libraries, schemas, data-only or generated
  artifacts, and simple scripts without meaningful architectural boundaries.
- **Unassessable:** the selected mode lacks enough design intent or observable
  implementation to establish responsibilities and dependency direction.

State the population and rationale. Stop architectural analysis for a Not
Applicable or Unassessable population and report the evidence gap. Invocation
makes hexagonal architecture the target only for Applicable populations. For a
repository with multiple populations, also provide a repository-level
applicability roll-up without erasing or overriding the per-population verdicts.

Use **Combined** mode by default when both design and implementation evidence
exist. Use **Design** or **Implementation** mode when only that evidence exists
or the request explicitly bounds the audit. Keep a combined comparison limited
to architectural claims and observed direction; do not repeat general plan,
intent, or product-completeness audits.

## Audit workflow

1. Read project guidance and the active project-owned workflow. Resolve the
   requested scope, audit population, applicability, mode, and evidence gaps.
2. Infer boundaries from responsibilities, behavior, imports, calls,
   construction, effects, ownership, declared intent, and tests. Do not infer
   compliance from names or structure alone.
3. Map domain policy, application use cases, inbound and outbound ports,
   driving and driven adapters, boundary translations, composition roots,
   external and peer dependencies, and architecture tests. Record what each
   component owns, what it depends on, who constructs it, where effects occur,
   and the observed dependency direction.
4. Use repository-owned analyzers when present, while interpreting their output
   semantically. Account for language and ecosystem conventions. When an
   uncertain or time-sensitive ecosystem fact matters and access exists, check
   authoritative official sources and distinguish them from repository
   evidence.
5. Read and apply the [general audit criteria](references/audit-criteria.md#general-audit-criteria),
   plus [design criteria](references/audit-criteria.md#design-audit) in Design
   mode and [implementation criteria](references/audit-criteria.md#implementation-audit)
   in Implementation mode. Combined mode uses both. Read the
   [interoperability criteria](references/audit-criteria.md#interoperability)
   whenever peer systems, published contracts, or strict cross-boundary
   semantics are in scope.
6. Apply only Pareto-relevant supporting principles that explain a boundary or
   correction. Distinguish strict semantic contracts from concrete, provider,
   private-path, runtime, or coordinated-delivery coupling.
7. Classify every evaluated criterion as **Fulfilled**, **Violation**,
   **Unassessable**, or **Not Applicable**, with file-and-line evidence. Use
   the consequence-based severity rubric below.
8. Construct every Violation with the required finding fields in the output
   contract and state the behavior and strict contracts a correction must
   preserve.

## Severity

Assign severity only to Violations:

- **Critical:** breaks a published safety, security, conformance, or required
  interoperability boundary with material downstream consequences.
- **High:** couples central policy or a high-fan-out use case to a concrete
  mechanism, blocks required substitution, or defeats independent change.
- **Medium:** creates localized leakage, scattered composition, an oversized
  port, or a meaningful enforcement gap.
- **Low:** weakens a guardrail with limited current impact but credible drift
  potential.

Severity guides correction priority and is never an automatic gate. Do not
assign severity to Fulfilled, Unassessable, or Not Applicable results.

## Coaching

Acknowledge sound existing boundaries before corrections. Organize useful
recommendations across these optional horizons without manufacturing an item
for every horizon:

- **Stabilize now:** contain the most consequential coupling with the smallest
  safe correction.
- **Improve next:** identify the next high-leverage boundary, ownership,
  composition, or test improvement.
- **Target state:** describe the right-sized architecture the population should
  grow toward.

Assess TDD, BDD, and DDD for every Applicable population. Missing or weak use of
any discipline always receives a proportionate recommendation, but becomes a
Violation only when it directly permits coupling or leaves a promised boundary
unenforced. Suggest Gherkin only when useful as a behavior-description language;
never require it or a particular runner.

## Output

Report:

- audit mode, requested scope, selected populations, applicability rationale,
  a repository-level applicability roll-up that preserves every per-population
  distinction, evidence sources, gaps, analyzers used, and coverage limits;
- an observed component, ownership, effect, construction, and dependency map;
- criterion-by-criterion results with file-and-line evidence;
- strict-contract assessments and consequence-based severity where relevant;
- sound existing boundaries and useful improvement horizons;
- explicit TDD, BDD, and DDD posture assessments for each Applicable
  population, with proportionate recommendations wherever a discipline is
  absent or materially weak;
- for every Violation, a stable finding identifier, audit mode, failure class,
  file-and-line evidence, observed dependency direction, impact,
  consequence-based severity, proposed target boundary, correction guidance,
  owning correction route, and the behavior and strict contracts to preserve;
  and
- remaining Unassessable questions.

Do not emit a numeric score, percentage, maturity grade, or global PASS/FAIL
verdict.
