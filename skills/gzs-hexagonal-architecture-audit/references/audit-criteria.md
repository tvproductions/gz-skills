# Hexagonal architecture audit criteria

Apply these criteria conceptually and with language-aware judgment. Infer
responsibilities and dependency direction from actual behavior, ownership,
construction, effects, contracts, and tests; do not require fixed directories,
interface syntax, or one dependency-injection mechanism.

## Component model

- **Domain policy:** business meaning, invariants, decisions, and rules that
  should remain independent of delivery and infrastructure mechanisms.
- **Application behavior:** use-case orchestration that applies domain policy
  and coordinates effects through owned boundaries.
- **Inbound ports:** application-owned entry contracts shaped around supported
  use cases.
- **Outbound ports:** application-owned contracts for capabilities a use case
  needs from external mechanisms or collaborators.
- **Driving adapters:** outer mechanisms that translate UI, transport, command,
  event, scheduled, or test input into inbound port calls.
- **Driven adapters:** outer implementations that translate outbound port calls
  to databases, filesystems, networks, frameworks, devices, providers, or peer
  systems and translate results and failures back.
- **Composition root:** outer wiring that selects and constructs concrete
  adapters and connects them to application behavior.
- **Anti-corruption layer:** an owned translation seam that prevents another
  bounded context's language, types, policy, and evolution from leaking inward.

An interface, a folder named `domain` or `adapter`, a dependency-injection
container, or a diagram is not by itself evidence of a boundary. Verify who owns
the contract, what crosses it, how dependencies point, and how behavior is
enforced.

## General audit criteria

Hexagonal architecture is the target for an Applicable population. Evaluate:

- domain and application policy remain independent of concrete external
  mechanisms;
- ports are owned by the application and narrowly shaped by consuming use cases;
- adapters own mechanism access, translation, and mechanism-specific recovery;
- side effects and concrete construction stay at outer boundaries;
- business decisions stay in domain or application behavior;
- core behavior is testable through ports without concrete infrastructure; and
- important promised boundaries have acceptance evidence that can detect
  direction, ownership, translation, or isolation regressions.

Classify each evaluated criterion as Fulfilled, Violation, Unassessable, or Not
Applicable and cite file-and-line evidence. Analyzer output can strengthen the
evidence, but analyzer absence does not prevent a semantic audit, and a clean
dependency graph does not prove correct ownership, translation, or behavior.

## Design audit

Check whether the intended architecture provides:

- a provider-independent organizing model for domain policy and application
  behavior;
- application-owned, use-case-shaped inbound and outbound ports rather than
  provider-owned or provider-shaped contracts;
- adapters that own external mechanisms, translation, and recovery decisions
  specific to those mechanisms;
- composition at an outer boundary rather than construction embedded in core
  behavior;
- independently evolvable collaboration through stable public contracts;
- explicit semantic ownership for strict wire, identity, timing, lineage, and
  conformance rules without concrete provider or runtime types leaking inward;
- acceptance rules for dependency direction, isolation, port behavior,
  translation, and core tests; and
- migration through stable seams rather than peer private implementation,
  adjacent source layout, or coordinated delivery order.

A promised boundary without an enforcement witness is a Violation when that
gap permits the promised dependency direction or isolation to collapse. Do not
expand the audit into general plan completeness or full product-intent tracing.

## Implementation audit

Trace actual imports, calls, construction, effects, data and error types,
configuration, and tests. Verify semantics beyond import graphs. Evaluate all
ten failure classes:

1. **Outward core dependency:** domain or application code imports
   infrastructure, a framework, provider, or concrete adapter implementation.
2. **Provider-owned boundary:** a provider-owned interface controls the
   application boundary instead of implementing an application-owned port.
3. **Mechanism type leaking:** external SDK, transport, persistence, filesystem,
   UI, framework, or provider types cross an owned port into core behavior.
4. **Peer internals outside an adapter or ACL:** core code imports peer source,
   private modules, adjacent checkouts, or shared implementation details.
5. **Side effect outside adapter or composition:** core behavior directly
   performs I/O or another external effect instead of invoking an explicit port.
6. **Business policy in adapter:** mechanism-facing code owns business decisions
   rather than translating and delegating to domain or application behavior.
7. **Scattered construction:** adapter selection or concrete construction occurs
   across core code instead of an outer composition root or equivalent wiring.
8. **Port broader than consumers:** a port exposes provider-wide capabilities or
   operations and data not required by its consuming use cases.
9. **Tests only through concrete infrastructure:** core behavior cannot be
   exercised through port behavior independently of real mechanisms.
10. **Promised boundary without acceptance witness:** a declared hexagonal
    direction or isolation rule lacks a test or check capable of detecting its
    collapse.

Account for dynamic imports, reflection, generated code, service locators,
callbacks, configuration-driven wiring, and build or packaging rules. When the
available evidence cannot resolve their behavior or direction, classify the
criterion Unassessable rather than guessing.

Also check that driven adapters have contract or integration evidence for
translation of requests, results, errors, identity, and relevant failure
semantics, and that dependency-direction checks cover the important inward
boundary. Absence is a Violation only when it has the direct architectural
consequence described in the general criteria.

## Interoperability

Identify who owns the semantic contract and whether the dependency crosses a
stable, published boundary or instead relies on internals, an adjacent checkout,
a private module, or coordinated delivery order. Check:

- explicit adapter or anti-corruption-layer translation;
- provider and peer types or error models leaking across the owned port;
- version, capability, compatibility, identity, and failure representation; and
- whether participants can be tested, released, replaced, and evolved
  independently.

A concrete provider package inside its adapter is acceptable. The Violation is
provider ownership crossing the application-owned port or entering policy, not
the adapter's use of its mechanism.

### Strict contracts

Rigidity is not coupling. Exact schemas, hashes, version identifiers,
timestamps, ordering, lineage, provenance, timing, and conformance rules can
enable independent implementations. Ask:

- Who owns the meaning?
- Is the contract public, stable, versioned where appropriate, and independently
  implementable?
- Do adapters translate between the contract and concrete mechanisms?
- Does its strictness enable interoperability, or reproduce a provider's private
  shape?
- Can internal implementations change without changing the semantic boundary?

Concrete provider types, private paths, factories, runtime objects, source
checkouts, and coordinated delivery crossing inward are implementation coupling,
even when convenient.

## Pareto support principles

Use supporting principles only when they explain a hexagonal boundary or shape
a correction:

- dependency inversion: policy owns abstractions and mechanisms implement them;
- interface segregation: ports fit consuming use cases rather than providers;
- single responsibility and cohesion: policy, translation, effects, and
  construction have distinct reasons to change;
- information hiding: provider and peer internals remain behind owned seams;
- bounded contexts and anti-corruption layers: collaborators retain their own
  language and translate deliberately;
- functional core and imperative shell where useful: deterministic decisions
  remain isolated from effects; and
- clean or onion inward dependency direction as reinforcement of the same
  target.

This is not a percentage, score, maturity checklist, or generic principles
survey. Hexagonal architecture remains the target.

## TDD, BDD, and DDD coaching

Assess all three disciplines for every Applicable population:

- **TDD:** recommend test-first correction, characterization before brownfield
  refactoring, core and port behavior tests, adapter contract tests, and
  dependency-direction regression evidence where proportionate.
- **BDD:** express important use cases and boundary behavior as observable or
  executable acceptance examples. Gherkin is optional as a description
  language; require neither it nor a runner.
- **DDD:** strengthen domain language, policy ownership, bounded contexts, and
  anti-corruption seams in proportion to domain complexity.

Missing or weak use belongs in the improvement path. Classify it as a Violation
only when the absence directly permits coupling or leaves a promised boundary
unenforced. Discover local testing conventions. Never recommend pytest or any
other testing library or runner.

## Language and ecosystem interpretation

Inspect the project's actual languages, frameworks, build and packaging model,
testing ecosystem, and conventions. Translate the criteria into idiomatic local
mechanisms such as protocols, traits, functions, modules, packages, message
contracts, or evidenced composition techniques; do not use a canned language
matrix.

When a material ecosystem fact is uncertain or time-sensitive and access
exists, verify it through authoritative official documentation. Distinguish
external technical sources from repository evidence and state any remaining
uncertainty. A missing analyzer does not preclude semantic analysis, and a clean
graph does not prove the architecture.

## Coaching shape

Acknowledge sound boundaries first. Use Stabilize now, Improve next, and Target
state only when each horizon helps. Every proposed correction names the behavior
and strict contracts to preserve, the dependency to invert or translate, the
owning boundary, the acceptance evidence, and the project-owned workflow that
must perform the change. Never modify the audited project.
