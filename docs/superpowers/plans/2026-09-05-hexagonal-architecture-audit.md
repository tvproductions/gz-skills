# Hexagonal Architecture Audit Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a portable, read-only `gzs-hexagonal-architecture-audit` skill that analyzes greenfield and brownfield boundaries and provides evidence-based, right-sized improvement coaching.

**Architecture:** Keep applicability, authority, mode selection, workflow, and output guarantees in a concise `SKILL.md`; place detailed design, implementation, interoperability, and supporting-principle criteria in one progressively disclosed reference. Integrate the new independently versioned skill into the canonical catalog and pending bundle minor release without adding scripts, generated mirrors, consumer updates, or project-specific enforcement.

**Tech Stack:** Agent Skills Markdown and YAML, JSON and TOML package manifests, Python 3.11+ standard-library `unittest`, `uv`, the official `skills-ref` validator, and Git inspection.

**Spec:** `docs/superpowers/specs/2026-09-05-hexagonal-architecture-audit-design.md`

---

## Execution constraints

- Preserve all existing uncommitted work. The router expansion,
  `gzs-root-cause-debugging`, roadmap, documentation, and repository-test edits
  in the current tree are part of the accumulated unreleased change.
- Do not modify `xplane-fdau`, `q4xpcc`, or any consumer installation. They are
  read-only forward-test subjects.
- Do not add generated skill mirrors or a generic dependency-analysis script.
- Keep the new skill read-only. It may analyze and coach but must not edit an
  audited project, create its architecture artifacts, or implement corrections.
- Never recommend pytest. Use this repository's existing standard-library
  `unittest` suite for implementation verification and avoid recommending test
  runners or libraries in the skill.
- Do not commit, push, publish, release, or update consumers without separate
  explicit user authorization. Commit steps below are proposed checkpoints;
  skip them during execution unless that authorization is given.
- Use delegation only if the user selects and authorizes subagent-driven
  execution. Independent forward tests must use fresh-context, read-only agents.

## File map

**Create:**

- `skills/gzs-hexagonal-architecture-audit/SKILL.md` — activation, authority,
  applicability, mode routing, shared workflow, coaching, and output contract.
- `skills/gzs-hexagonal-architecture-audit/agents/openai.yaml` — human-readable
  interface metadata and implicit-invocation policy.
- `skills/gzs-hexagonal-architecture-audit/references/audit-criteria.md` —
  detailed design, implementation, interoperability, strict-contract, and
  Pareto-principle guidance.

**Modify:**

- `tests/test_repository_contract.py` — require implicit discovery for the new
  read-only architecture guide.
- `skills/gzs-router/SKILL.md` — route architecture-boundary and interoperability
  requests to the new skill.
- `README.md` — list thirteen installable skills and explain the new capability.
- `CHANGELOG.md` — record the new skill and bundle minor release behavior.
- `.claude-plugin/plugin.json` — add the explicit skill path and set bundle
  version `0.2.0`.
- `.codex-plugin/plugin.json` — set bundle version `0.2.0`.
- `package.json` — set bundle version `0.2.0`.
- `pyproject.toml` — set bundle version `0.2.0`.
- `docs/origins.md` — record pinned user-owned case-study provenance.
- `docs/review/README.md` — add the implemented skill to the review queue.

**Inspect without changing:**

- `docs/roadmap.md` — confirm the skill is not described as a future item. It is
  currently absent, so implementation requires no roadmap edit unless the file
  changes before execution.
- `C:/Users/Jeff/source/repos/xp/xplane-fdau` — read-only forward test.
- `C:/Users/Jeff/source/repos/xp/q4xpcc` — read-only forward test.

### Task 1: Pin the invocation-policy contract

**Files:**

- Modify: `tests/test_repository_contract.py`
- Test: `tests/test_repository_contract.py`

- [ ] **Step 1: Write the failing repository-contract test**

Add this method before
`test_router_covers_catalog_and_explicit_skills_have_codex_policy`:

```python
    def test_read_only_catalog_guides_have_implicit_codex_policy(self) -> None:
        catalog = load_catalog(REPOSITORY_ROOT / "skills")

        for name in (
            "gzs-hexagonal-architecture-audit",
            "gzs-router",
        ):
            metadata = (catalog[name].path / "agents" / "openai.yaml").read_text(
                encoding="utf-8"
            )
            self.assertIn("allow_implicit_invocation: true", metadata)
```

Remove the now-duplicated router-specific metadata assertion from
`test_router_covers_catalog_and_explicit_skills_have_codex_policy`:

```python
        router_metadata = (
            catalog["gzs-router"].path / "agents" / "openai.yaml"
        ).read_text(encoding="utf-8")
        self.assertIn("allow_implicit_invocation: true", router_metadata)
```

- [ ] **Step 2: Run the focused test and verify the intended red**

Run:

```powershell
uv run python -m unittest tests.test_repository_contract.RepositoryContractTests.test_read_only_catalog_guides_have_implicit_codex_policy -v
```

Expected: ERROR with `KeyError: 'gzs-hexagonal-architecture-audit'` because the
canonical skill does not exist yet. An import, syntax, or collection error is
not the intended red.

- [ ] **Step 3: Inspect the test-only diff**

Run:

```powershell
git diff -- tests/test_repository_contract.py
git diff --check
```

Expected: only the new implicit-policy contract and removal of the duplicate
router assertion; whitespace check passes.

- [ ] **Step 4: Create the optional test checkpoint**

Only with explicit commit authorization:

```powershell
git add tests/test_repository_contract.py
git commit -m "test: pin architecture audit discovery"
```

Otherwise leave the verified failing test uncommitted and continue.

### Task 2: Add the portable architecture audit skill

**Files:**

- Create: `skills/gzs-hexagonal-architecture-audit/SKILL.md`
- Create: `skills/gzs-hexagonal-architecture-audit/agents/openai.yaml`
- Create: `skills/gzs-hexagonal-architecture-audit/references/audit-criteria.md`
- Test: `tests/test_repository_contract.py`

- [ ] **Step 1: Create the concise skill entrypoint**

Create `skills/gzs-hexagonal-architecture-audit/SKILL.md` with this content:

```markdown
---
name: gzs-hexagonal-architecture-audit
description: Analyze greenfield designs and brownfield implementations against right-sized hexagonal architecture, then coach boundary-preserving design or refactoring. Use for explicit hexagonal or ports-and-adapters audits, architecture work involving dependency direction or cross-project interoperability, or projects that declare these guardrails; do not use for ordinary code review, generic SOLID questions, or structurally simple projects.
compatibility: Works with inspectable code or design documentation in any language or project ecosystem.
metadata:
  govzero-version: "0.1.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Hexagonal Architecture Audit

Analyze architectural facts and help the project move toward right-sized
hexagonal architecture. Report violations without scoring or automatically
blocking work, acknowledge sound existing boundaries, and coach an attainable
path from the current state to a clearer target.

## Authority

- Remain read-only. Inspect and run safe read-only probes, but do not edit code,
  restructure modules, write architecture documents, amend plans, create work
  items, or implement corrections.
- Return findings to any active project-owned design, implementation, or
  governance workflow. Do not bypass its scope, stages, gates, state, receipts,
  reviewer independence, or human decisions.
- Never recommend pytest. Discover existing testing conventions and avoid
  prescribing test runners or libraries.

## Decide applicability

Resolve and explain the audit population before assessing it. Classify each
population independently when a repository contains different kinds of work.

- **Applicable:** applications, services, plugins, orchestration systems, and
  integration-heavy libraries with meaningful external dependencies or runtime
  boundaries.
- **Not Applicable:** small leaf libraries, schemas, data-only repositories,
  generated artifacts, and simple scripts without meaningful architectural
  boundaries.
- **Unassessable:** the requested mode lacks enough declared intent or observable
  implementation to establish responsibilities and dependency direction.

Invocation establishes hexagonal architecture as the target for an Applicable
population. Do not force it onto a Not Applicable population.

## Choose the audit mode

- **Design:** inspect intended cores, use cases, ports, adapters, composition,
  ownership, dependency direction, interoperability, and acceptance rules. Read
  [Design audit][criteria-design].
- **Implementation:** inspect actual imports, calls, types, construction, side
  effects, composition, and tests. Read
  [Implementation audit][criteria-implementation].
- **Combined:** when both kinds of evidence exist, audit both by default and
  compare their architectural claims. Read both mode sections and
  [Interoperability][criteria-interoperability].

An explicitly bounded request may select one mode. Keep combined comparison to
architectural boundaries; do not duplicate a general plan or intent audit.

## Audit

1. Read project guidance, identify the active workflow, and record why every
   selected surface entered the audit population.
2. Infer responsibilities from behavior, imports, calls, construction, side
   effects, ownership, and declared intent rather than folder names.
3. Map domain policy, application use cases, inbound and outbound ports, driving
   and driven adapters, boundary translations, composition roots, external and
   peer dependencies, and architecture tests.
4. Record what each component owns, what it depends on, who constructs it, where
   effects occur, and the observed dependency direction. Use repository-owned
   analyzers when available, but interpret their evidence rather than treating
   an import graph as architectural truth.
5. Apply the selected mode criteria and the Pareto-relevant supporting
   principles in [Audit criteria][criteria]. Consult current
   authoritative ecosystem sources when language or framework facts are
   uncertain and access is available.
6. Distinguish stable semantic contracts from coupling to provider types,
   concrete implementations, private modules, repository paths, or delivery
   order.
7. Classify every evaluated criterion as **Fulfilled**, **Violation**,
   **Unassessable**, or **Not Applicable** with file-and-line evidence.

## Coach improvements

For each Violation, explain the impact, target boundary, owning correction
route, and behavior or strict contract that must be preserved. Organize the
overall path only where useful:

1. **Stabilize now:** contain the most consequential coupling.
2. **Improve next:** add the next high-leverage boundary, ownership,
   composition, or testing improvement.
3. **Target state:** show the right-sized hexagonal architecture to grow toward.

Every Applicable audit assesses TDD, BDD, and DDD posture. When one is absent or
materially weak, include a proportionate recommendation. Treat absence as a
Violation only when it directly permits coupling or leaves a promised boundary
unenforced. Gherkin may be suggested as a behavior-description language when it
clarifies executable examples; do not require it.

## Output

Report the mode and population, applicability rationale, evidence and missing
evidence, observed component and dependency map, criterion results, strict
contract assessment, consequence-based severity for Violations, the three
improvement horizons, TDD/BDD/DDD recommendations, owning correction routes,
and coverage limits. Include no numeric score, maturity grade, or global
PASS/FAIL verdict. A Violation guides improvement; this skill does not itself
block delivery.

[criteria]: references/audit-criteria.md
[criteria-design]: references/audit-criteria.md#design-audit
[criteria-implementation]: references/audit-criteria.md#implementation-audit
[criteria-interoperability]: references/audit-criteria.md#interoperability
```

- [ ] **Step 2: Create the detailed criteria reference**

Create
`skills/gzs-hexagonal-architecture-audit/references/audit-criteria.md` with this
content:

```markdown
# Hexagonal architecture audit criteria

Read the sections selected by `SKILL.md`. Apply architectural concepts to the
observed language and ecosystem; do not require these labels or a standard
directory layout.

## Component model

- **Domain policy:** business rules and domain meaning independent of delivery
  and infrastructure mechanisms.
- **Application behavior:** use cases that coordinate domain policy through
  owned boundaries.
- **Inbound ports:** application-owned entry contracts used by driving adapters.
- **Outbound ports:** application-owned capability contracts implemented by
  driven adapters.
- **Driving adapters:** transports, user interfaces, schedulers, commands, or
  hosts that invoke application behavior.
- **Driven adapters:** persistence, external services, filesystems, devices,
  messaging, clocks, randomness, and other effectful implementations.
- **Composition root:** outer wiring that selects and constructs concrete
  adapters and supplies them to application behavior.
- **Anti-corruption layer:** explicit translation that prevents another bounded
  context or provider model from controlling local meaning.

Infer these responsibilities from evidence. An interface is not automatically a
port, a folder is not automatically a layer, and dependency injection alone is
not proof of dependency inversion.

## Design audit

Inspect proposed responsibilities, use cases, contracts, dependency arrows,
construction, external systems, tests, and acceptance rules.

Check whether:

1. The core purpose and business policy are identifiable without naming a
   provider or framework as their organizing model.
2. Inbound and outbound ports are owned by the application and shaped around
   use-case needs rather than reproducing a provider SDK.
3. Adapters own transport, persistence, framework lifecycle, provider calls,
   translation, and effect-specific recovery.
4. Composition has one or more explicit outer owners; core components do not
   select their implementations.
5. Collaborating projects exchange stable public contracts and can release or
   replace implementations independently.
6. Exact wire, identity, timing, lineage, and conformance rules have clear
   semantic owners and do not smuggle concrete implementation types inward.
7. Acceptance rules can demonstrate dependency direction, provider isolation,
   port behavior, adapter translation, and independent core testing.
8. The plan orders migration or delivery through stable seams rather than making
   one repository's private implementation a prerequisite for another.

A design promise without an enforceable acceptance rule is a Violation when the
missing witness can permit the promised boundary to collapse.

## Implementation audit

Trace actual code and tests. Prefer repository-owned import, dependency, build,
and architecture analyzers when available, then verify their semantic meaning
against callers and behavior.

Check whether:

1. Domain or application code imports infrastructure, frameworks, provider
   packages, concrete adapters, or peer-project internals.
2. External SDK, transport, persistence, filesystem, UI, or framework types
   cross application ports instead of being translated by adapters.
3. Provider-owned interfaces define what application use cases can request.
4. Side effects occur through explicit adapters rather than within policy code.
5. Business decisions, validation meaning, or orchestration policy have leaked
   into adapters.
6. Concrete implementations are selected and constructed in composition roots
   rather than scattered through core code.
7. Ports expose the smallest coherent behavior needed by their consumers rather
   than provider-wide or generic CRUD surfaces.
8. Core behavior can run under focused tests using owned fakes, stubs, or in-
   memory adapters without concrete infrastructure.
9. Adapter contract and integration tests exercise translation and strict public
   contracts at the boundary.
10. Dependency-direction tests or equivalent repository checks protect
    load-bearing boundaries against regression.

Follow imports beyond the first edge when necessary. Dynamic loading,
reflection, generated code, service locators, callbacks, configuration strings,
and build-time wiring can conceal the real dependency direction. Mark a result
Unassessable rather than inventing certainty when the relevant route cannot be
observed.

## Interoperability

For every collaborating project or external provider, identify:

- which side owns the semantic contract;
- whether the dependency is on a stable published boundary or on repository
  internals, adjacent checkouts, private modules, or delivery order;
- where translation and anti-corruption occur;
- whether provider objects or error types leak through local ports;
- how versions, capabilities, compatibility, identity, and failure are
  represented without importing a concrete implementation; and
- whether each participant can test, release, replace, and evolve independently.

A consumer may depend on a published provider package inside an adapter. The
Violation occurs when provider ownership controls application policy or crosses
the owned port, not merely because an adapter has a concrete dependency.

## Strict contracts

Do not equate rigidity with coupling. Exact schemas, hashes, version identities,
timestamps, ordering, lineage, provenance, timing, and conformance rules can be
necessary semantic contracts that enable independent implementations.

For each strict contract, ask:

1. Who owns its meaning?
2. Is it public, stable, versioned, and independently implementable?
3. Does an adapter translate provider representation into it?
4. Does it preserve interoperability rather than expose private storage or SDK
   shape?
5. Can participating implementations change internally without changing the
   contract?

Classify concrete package types, private module paths, provider factories,
runtime objects, source-checkout assumptions, and coordinated delivery order as
coupling when they cross inward. Preserve exact semantic requirements when they
belong to the boundary.

## Required failure classes

Retain a finding when evidence demonstrates any of these classes:

- outward core dependency on infrastructure, framework, provider, or adapter;
- provider-owned interface controlling the application boundary;
- external mechanism type leaking through a port;
- peer-project implementation access outside an adapter or anti-corruption
  layer;
- side effect outside an adapter or composition boundary;
- business policy embedded in an adapter;
- scattered adapter selection or construction;
- port broader than its consuming use cases;
- tests coupled only to concrete infrastructure; or
- promised hexagonal boundary without an acceptance witness.

Add another class only when it describes a distinct, evidenced architectural
failure rather than style preference.

## Pareto-selected supporting principles

Use only principles that clarify an observed boundary or correction:

- **Dependency inversion:** policy owns abstractions and mechanisms implement
  them.
- **Interface segregation:** ports match consuming use cases instead of
  provider-wide capabilities.
- **Single responsibility and cohesion:** policy, translation, effects, and
  construction have distinct reasons to change.
- **Information hiding:** provider and peer internals remain behind owned
  boundaries.
- **Bounded contexts and anti-corruption layers:** collaborating systems retain
  their own language and translate deliberately.
- **Functional core, imperative shell:** deterministic decisions remain
  independently testable while effects stay at the edge where useful.
- **Clean/onion dependency direction:** reinforces the same inward rule without
  replacing hexagonal architecture as the target.

Pareto selection is not a percentage, score, or exhaustive checklist.

## TDD, BDD, and DDD coaching

Assess all three for every Applicable population:

- Recommend TDD through a test-first correction sequence, characterization
  coverage before brownfield refactoring, focused core and port behavior tests,
  adapter contract tests, and dependency-direction regression checks.
- Recommend BDD through observable use-case examples and executable acceptance
  behavior. Suggest Gherkin only when its language improves collaboration or
  precision; do not require it or a specific runner.
- Recommend DDD through explicit domain language, policy ownership, bounded
  contexts, and anti-corruption seams proportionate to the domain.

If a discipline is absent or materially weak, include it in the improvement
path. Treat it as a Violation only when the absence directly permits coupling or
leaves a promised boundary unenforced. Never recommend pytest or prescribe a
testing library.

## Language and ecosystem interpretation

Identify the actual languages, frameworks, build and packaging model, testing
ecosystem, and repository conventions. Translate the criteria into idiomatic
local mechanisms rather than applying a canonical language matrix.

When an ecosystem fact is uncertain or time-sensitive and authoritative sources
are accessible, verify it against official language, framework, or tool
documentation and cite the source. Separate those external facts from
repository evidence. State uncertainty when source access, tooling, or language
competence cannot support a confident recommendation.

The absence of a dependency analyzer does not make a semantic audit impossible
when code and documentation remain inspectable. Conversely, a clean analyzer
result does not prove that responsibilities and runtime construction are sound.

## Coaching shape

Acknowledge sound existing boundaries first. Then provide only useful horizons:

- **Stabilize now:** contain the highest-consequence coupling without a broad
  rewrite.
- **Improve next:** establish the next owned seam, translation, composition
  boundary, or architectural test.
- **Target state:** describe the right-sized hexagonal model appropriate to the
  population's purpose and ecosystem.

For each recommended correction, name the behavior and strict contracts to
preserve, the dependency to invert or translate, the boundary that should own
the responsibility, acceptance evidence, and the project-owned workflow that
should implement it. Do not modify the audited project.
```

- [ ] **Step 3: Create OpenAI interface metadata**

Create `skills/gzs-hexagonal-architecture-audit/agents/openai.yaml`:

```yaml
interface:
  display_name: "GovZero Hexagonal Architecture Audit"
  short_description: "Audit and coach hexagonal boundaries"
  default_prompt: "Use $gzs-hexagonal-architecture-audit to analyze this project's architectural boundaries and suggest a right-sized path toward hexagonal architecture."
policy:
  allow_implicit_invocation: true
```

- [ ] **Step 4: Run the focused contract test and verify green**

Run:

```powershell
uv run python -m unittest tests.test_repository_contract.RepositoryContractTests.test_read_only_catalog_guides_have_implicit_codex_policy -v
```

Expected: one test passes.

- [ ] **Step 5: Validate the new skill contract and links**

Run:

```powershell
uvx --from skills-ref agentskills.exe validate .\skills\gzs-hexagonal-architecture-audit
uv run python -m unittest tests.test_repository_contract.RepositoryContractTests.test_skill_names_and_openai_prompts_match_directories tests.test_repository_contract.RepositoryContractTests.test_relative_markdown_links_resolve -v
git diff --check
```

Expected: official validator reports `Valid skill`; both repository-contract
tests pass; whitespace check passes.

- [ ] **Step 6: Review activation and read-only boundaries manually**

Confirm from the created files:

- Positive triggers include explicit hexagonal/ports-and-adapters audits,
  dependency-direction architecture work, cross-project interoperability, and
  declared project guardrails.
- Negative triggers include ordinary code review, generic SOLID explanation,
  general implementation, and structurally simple repositories.
- The workflow cannot be read as authorization to edit an audited project.
- No recommendation adopts a language, harness, test runner, or framework.
- The only occurrences of `pytest` are explicit prohibitions, never examples or
  commands.

- [ ] **Step 7: Create the optional skill checkpoint**

Only with explicit commit authorization:

```powershell
git add skills/gzs-hexagonal-architecture-audit tests/test_repository_contract.py
git commit -m "feat: add hexagonal architecture audit"
```

Otherwise leave the verified skill uncommitted and continue.

### Task 3: Integrate the catalog and SemVer surfaces

**Files:**

- Modify: `skills/gzs-router/SKILL.md`
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.codex-plugin/plugin.json`
- Modify: `package.json`
- Modify: `pyproject.toml`
- Modify: `docs/origins.md`
- Modify: `docs/review/README.md`
- Test: `tests/test_repository_contract.py`

- [ ] **Step 1: Add the skill to the router without duplicating adjacent audits**

In the `gzs-router` catalog table, add this row in name-appropriate position:

```markdown
| Analyze and improve hexagonal architecture boundaries | `gzs-hexagonal-architecture-audit` | Read-only design and implementation coaching; does not replace general plan, intent, or code review. |
```

Add this common sequence after failure resolution:

```markdown
- Architecture alignment: `gzs-hexagonal-architecture-audit` for boundary and
  dependency-direction analysis; add `gzs-plan-audit` only when the broader
  plan also needs intent, scope, and completeness review.
```

Keep `metadata.govzero-version: "0.2.0"`; the router expansion is still
unreleased and this catalog entry joins that pending backward-compatible
capability.

- [ ] **Step 2: Update bundle versions atomically**

Change only the owning version fields from `0.1.0` to `0.2.0` in:

```text
pyproject.toml                    [project].version
.codex-plugin/plugin.json         version
.claude-plugin/plugin.json        version
package.json                      version
```

Do not change example installation tags in README during this task; those
describe the latest released immutable snapshot until an actual `0.2.0` release
is prepared.

- [ ] **Step 3: Register the Claude skill path**

Add this entry alphabetically after `gzs-git-sync`:

```json
    "./skills/gzs-hexagonal-architecture-audit",
```

Codex and OpenCode already expose the complete canonical `skills/` tree. Do not
add generated mirrors or new adapters.

- [ ] **Step 4: Update the README catalog**

Change the catalog count from twelve to thirteen and add:

```markdown
- `gzs-hexagonal-architecture-audit`
```

Place it alphabetically after `gzs-git-sync`. Do not add it to the near-term
roadmap because it is now an implemented catalog member.

- [ ] **Step 5: Record the release-facing change**

Under `CHANGELOG.md` → `Unreleased` → `Added`, add:

```markdown
- Added `gzs-hexagonal-architecture-audit` 0.1.0 as a read-only analyzer,
  design consultant, and refactor coach for right-sized hexagonal architecture,
  cross-project interoperability, and Pareto-selected supporting principles.
```

Under `Changed`, add:

```markdown
- Advanced the synchronized bundle manifests to 0.2.0 for the accumulated
  backward-compatible catalog and router expansion.
```

Retain the existing root-cause, router, namespace, and SemVer entries.

- [ ] **Step 6: Add pinned provenance**

Append this section to `docs/origins.md`:

```markdown
## `gzs-hexagonal-architecture-audit`

- `tvproductions/xplane-fdau` at
  `66e31bc3e5d730869bf1dfb5aa4b2c736cb76803`:
  `docs/architecture/xplane_fdau_core_scope_amendment.md` and
  `docs/superpowers/specs/2026-08-23-xplane-fdau-acquisition-recording-projection-pinning-contracts-design.md`
- `tvproductions/q4xpcc` at
  `a7cc2682ca4289f498fffc409a091e28f528fe9a`:
  `docs/superpowers/specs/2026-05-17-q4xpcc-project-spec.md`,
  `src/q4xpcc_dev/xplane_read_port.py`,
  `src/q4xpcc_dev/xpwebapi_adapter.py`, and
  `tests/test_supervisor_dependency_boundary.py`

Shared behavior retained: infer architectural responsibilities rather than
folder names, keep policy dependent on application-owned ports, translate
provider and peer-project mechanisms in adapters, centralize composition,
preserve strict semantic contracts, and require observable boundary evidence.
Project packages, paths, commands, schemas, delivery gates, and specialized
dependency-enforcement implementations remain local.
```

- [ ] **Step 7: Add the implemented skill to the review queue**

Append an order 13 row using the existing table syntax with these exact values:

```text
Skill label: gzs-hexagonal-architecture-audit
Skill link target: ../../skills/gzs-hexagonal-architecture-audit/SKILL.md
Review status: Pending
Why this position: Read-only architecture analysis must remain helpful, language-aware, and distinct from plan and intent audits.
```

- [ ] **Step 8: Verify bundle and catalog synchronization**

Run:

```powershell
uv run python -m unittest tests.test_repository_contract.RepositoryContractTests.test_bundle_versions_and_plugin_catalogs_are_synchronized tests.test_repository_contract.RepositoryContractTests.test_router_covers_catalog_and_explicit_skills_have_codex_policy -v
uv run gz-skills list
git diff --check
```

Expected: both tests pass; the CLI lists
`gzs-hexagonal-architecture-audit 0.1.0`, `gzs-root-cause-debugging 0.1.0`, and
`gzs-router 0.2.0`; whitespace check passes.

- [ ] **Step 9: Create the optional catalog checkpoint**

Only with explicit commit authorization:

```powershell
git add pyproject.toml .codex-plugin/plugin.json .claude-plugin/plugin.json package.json README.md CHANGELOG.md docs/origins.md docs/review/README.md skills/gzs-router/SKILL.md
git commit -m "feat: integrate architecture audit catalog"
```

Otherwise leave the synchronized catalog changes uncommitted and continue.

### Task 4: Validate the complete portable bundle

**Files:**

- Verify: `skills/*/SKILL.md`
- Verify: `tests/`
- Verify: package artifacts under ignored `dist/`

- [ ] **Step 1: Run the complete repository test suite**

Run:

```powershell
uv run python -m unittest discover -s tests -v
```

Expected: all tests pass, including catalog equality, SemVer synchronization,
relative links, router coverage, and implicit/explicit invocation policy.

- [ ] **Step 2: Validate every canonical skill officially**

Run:

```powershell
Get-ChildItem .\skills -Directory | ForEach-Object {
    uvx --from skills-ref agentskills.exe validate $_.FullName
}
```

Expected: thirteen `Valid skill` results and no failures.

- [ ] **Step 3: Build the `0.2.0` distribution artifacts**

Run:

```powershell
uv build
```

Expected:

```text
Successfully built dist\govzero_skills-0.2.0.tar.gz
Successfully built dist\govzero_skills-0.2.0-py3-none-any.whl
```

- [ ] **Step 4: Inspect packaged skill resources**

Run:

```powershell
tar -tf dist\govzero_skills-0.2.0-py3-none-any.whl | Select-String "gzs-hexagonal-architecture-audit"
tar -tf dist\govzero_skills-0.2.0.tar.gz | Select-String "gzs-hexagonal-architecture-audit"
```

Expected: both artifacts contain `SKILL.md`, `agents/openai.yaml`, and
`references/audit-criteria.md` for the new skill.

- [ ] **Step 5: Inspect the complete change surface**

Run:

```powershell
git diff --check
git diff --stat
git status --short
```

Expected: no whitespace errors, no generated mirrors or consumer files, and no
unexpected source or script changes. Preserve the pre-existing uncommitted work
listed in this plan's execution constraints.

### Task 5: Forward-test decisions and coaching

**Files:**

- Read only: `C:/Users/Jeff/source/repos/xp/xplane-fdau`
- Read only: `C:/Users/Jeff/source/repos/xp/q4xpcc`
- Read only: `skills/gzs-hexagonal-architecture-audit/`

- [ ] **Step 1: Confirm delegation authority**

Use independent agents only if the user selected subagent-driven execution or
otherwise explicitly authorized delegation for this implementation. If not
authorized, run the same prompts inline, label the results non-independent, and
do not claim the forward-testing requirement was fully satisfied.

- [ ] **Step 2: Capture a fresh-context q4xpcc baseline**

Give an evaluator with no inherited conversation or target skill this prompt:

```text
Read C:/Users/Jeff/source/repos/xp/q4xpcc/AGENTS.md, then perform a read-only
combined architecture audit of q4xpcc's boundary with xplane-fdau and xpwebapi.
Analyze the current design, implementation, tests, dependency direction, and
ability of the projects to evolve independently. Cite file-and-line evidence,
acknowledge sound boundaries, and give incremental improvement guidance. Do not
modify files or run mutating commands.
```

Retain the response in session evidence; do not write it into either consumer.

- [ ] **Step 3: Run the same q4xpcc case with the new skill**

Give a separate fresh-context evaluator this prompt:

```text
Use $gzs-hexagonal-architecture-audit from
C:/Users/Jeff/source/repos/agents/gz-skills/skills/gzs-hexagonal-architecture-audit
to perform a read-only combined audit of
C:/Users/Jeff/source/repos/xp/q4xpcc, focusing on its boundaries with
xplane-fdau and xpwebapi. Read the consumer's AGENTS.md first. Do not modify
files or run mutating commands.
```

Do not provide expected findings or conclusions.

- [ ] **Step 4: Capture a fresh-context xplane-fdau baseline**

Give another evaluator with no target skill this prompt:

```text
Read C:/Users/Jeff/source/repos/xp/xplane-fdau/AGENTS.md, then perform a
read-only combined architecture audit of xplane-fdau's intended core boundary
and its interoperability with q4xpcc. Analyze current design, implementation,
tests, dependency direction, and strict public contracts. Cite file-and-line
evidence, acknowledge sound boundaries, and give incremental improvement
guidance. Do not modify files or run mutating commands.
```

- [ ] **Step 5: Run the same xplane-fdau case with the new skill**

Give a separate fresh-context evaluator this prompt:

```text
Use $gzs-hexagonal-architecture-audit from
C:/Users/Jeff/source/repos/agents/gz-skills/skills/gzs-hexagonal-architecture-audit
to perform a read-only combined audit of
C:/Users/Jeff/source/repos/xp/xplane-fdau, focusing on its intended core
boundary and interoperability with q4xpcc. Read the consumer's AGENTS.md first.
Do not modify files or run mutating commands.
```

Do not provide expected findings or conclusions.

- [ ] **Step 6: Compare decisions qualitatively**

Review baseline and with-skill results without assigning numeric scores. Confirm
that the skill-guided audits materially improve these dimensions:

- correct applicability and population selection;
- evidence-backed component and dependency mapping;
- recognition of consumer-owned ports, provider adapters, and sound existing
  boundaries;
- distinction between strict semantic contracts and concrete implementation
  coupling;
- detection of genuine provider, peer-project, composition, and acceptance-test
  leakage without speculative findings;
- stabilize-now, improve-next, and target-state coaching;
- right-sized TDD, BDD, and DDD recommendations;
- idiomatic ecosystem guidance without a built-in language matrix;
- no numeric score, automatic gate, mutation, or pytest recommendation.

If the new skill does not materially improve a dimension or creates a false
positive, revise only the relevant instruction, rerun the official validator
and repository tests, and repeat the affected forward test.

- [ ] **Step 7: Exercise activation boundaries**

Present only catalog names and descriptions to a fresh-context evaluator and ask
which skill, if any, should handle each request:

```text
1. Review this bug-fix diff for correctness.
2. Explain the SOLID principles to a student.
3. Audit whether our service leaks the AWS SDK into application use cases.
4. Our AGENTS.md requires ports and adapters; review this proposed integration.
5. Suggest a folder layout for this ten-line standalone conversion script.
6. Help two independently released projects interoperate without importing each
   other's internal modules.
```

Expected routing:

- Cases 3, 4, and 6 select `gzs-hexagonal-architecture-audit`.
- Cases 1, 2, and 5 do not select it.

Treat a disagreement as activation-description evidence, not as evaluator
failure; revise and rerun when the reasoning reveals a real ambiguity.

- [ ] **Step 8: Verify consumer repositories remained untouched**

Run in each consumer:

```powershell
git -c safe.directory=* status --short
```

Expected: status matches its pre-test state exactly. Do not clean, reset, or
otherwise change either repository.

### Task 6: Final verification and handoff

**Files:**

- Verify: complete working tree
- Update during execution only: this plan's checkboxes and execution metadata if
  the repository's chosen execution workflow requires it

- [ ] **Step 1: Re-run all required verification after forward-test revisions**

Run:

```powershell
uv run python -m unittest discover -s tests -v
Get-ChildItem .\skills -Directory | ForEach-Object {
    uvx --from skills-ref agentskills.exe validate $_.FullName
}
uv run gz-skills list
uv build
git diff --check
```

Expected: tests pass, thirteen skills validate, the catalog lists the new skill
at `0.1.0`, bundle `0.2.0` artifacts build, and the diff is clean.

- [ ] **Step 2: Audit final scope and versions**

Run:

```powershell
git status --short
git diff --stat
git diff -- pyproject.toml .codex-plugin\plugin.json .claude-plugin\plugin.json package.json
```

Expected: all four bundle manifests say `0.2.0`; the new skill says `0.1.0`;
the router remains `0.2.0`; no consumer or generated mirror changed.

- [ ] **Step 3: Create the optional final checkpoint**

Only with explicit commit authorization:

```powershell
git add .claude-plugin/plugin.json .codex-plugin/plugin.json AGENTS.md CHANGELOG.md README.md docs package.json pyproject.toml skills tests/test_repository_contract.py
git commit -m "feat: add portable architecture audit"
```

Before committing, inspect `git diff --cached --stat` and confirm every staged
file belongs to the accumulated user-approved unreleased change. Never push,
publish, release, or update consumers from this step.

- [ ] **Step 4: Report the handoff**

Report:

- the new skill and resource paths;
- applicability, read-only, coaching, and portability boundaries;
- skill, router, and bundle versions;
- test, validator, build, package-content, and forward-test outcomes;
- whether forward testing was independent or inline;
- consumer repositories' unchanged status; and
- the exact uncommitted or committed Git state.
