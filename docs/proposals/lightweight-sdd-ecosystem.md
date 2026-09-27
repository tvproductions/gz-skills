# Lightweight SDD ecosystem: candidate design

Status: candidate for review, not an implementation or release approval.
Recorded: 2026-09-27. This continues the [session handoff](../handoffs/2026-09-27-lightweight-sdd-ecosystem.md).

## Purpose and ownership

Give adopting repositories a choice between standalone portable skills (`lite`)
and a deliberately opinionated but lighter-than-gzkit SDD ecosystem (`heavy`).
This proposal concerns adopting projects, not the architecture of `gz-skills`
itself. A repository with `.gzkit/` remains incompatible with this profile.

| Owner | Responsibility |
| --- | --- |
| `gz-skills` | Portable disciplines, project profile setup, attributed MPAS adaptations, and guidance for checking the complement. No central project lifecycle CLI. |
| Superpowers (SP) | Design discussion, approved feature specifications, implementation plans, execution, test-first work, and review. |
| Superpowers Backplane (SP-BP) | Python implementation of the GitHub Issue-backed catalog and delivery graph, FDAU-inspired taxonomy, traceability, derived views, and release records. |
| Adopting project | Governing documents, approvers, public compatibility contract, verification commands, supported harnesses, and native plugin configuration. |

The target supported harnesses are Claude Code, Codex, and OpenCode. A project verifies
only the harnesses it uses. Prefer repository-scoped native plugin enablement;
do not copy physical skill trees into the adopting repository. The released
Python snapshot installer remains a separate existing contract until reviewed.
SP-BP is a Python project. Implement its catalog, issue reconciliation, trace
and V&V logic, view generation, release logic, CLI/helpers, and tests in
Python. Harness-specific adapters may use the minimal code required by a host,
but they must delegate to the Python core. Do not introduce a Go core, service,
module, or toolchain. If a prototype was written in Go, preserve its useful
behavior and tests as migration input, then replace that implementation with
Python rather than maintaining parallel cores. SP-BP owns its exact Python
runtime and packaging policy.

## Profiles and adoption

On first use of any `gzs-*` skill in a repository without settings, route through
project setup, ask once for `lite` or `heavy`, record the choice, and resume the
original task. Each skill needs a small invocation-time settings check as the
portable baseline. Harness hooks may improve discovery, but cannot be the only
route: [Codex skips plugin hooks until they are trusted](https://developers.openai.com/plugins/build/plugins),
while [Claude Code](https://code.claude.com/docs/en/hooks) and
[OpenCode](https://opencode.ai/docs/plugins/) expose different lifecycle events.
Test direct invocation and model-selected use for each supported harness.
Commit shared `.gz-skills/settings.json`; exclude secrets and
machine-specific installation state. The current helper records only
`schema_version` and `profile`; an extension needs its own schema and migration
design. Promotion from lite to heavy is supported. Heavy-to-lite reversal is
outside this proposal.

Lite supplies standalone portable skills without a project-wide architecture,
requirements, backlog, or release preference. Heavy is a selected intent until
the project has approved governing documents and a verified compatible set of
gz-skills, SP, and SP-BP on each declared harness. The attributed MPAS curation
is part of gz-skills, not a fourth installed plugin. A portable `gzs-*` skill may
still run while heavy readiness is pending, but must not claim the integrated
workflow is ready. Publish a tested compatibility set, record selected versions
in project configuration, and recheck after updates. The exact native-harness
discovery and verification commands remain to be proven.

For a brownfield project, discover existing governing material, map it into
the canonical shapes, show the translation and source mapping to reviewers,
and obtain recorded human approval. Do not overwrite or silently promote
legacy text. The project names its approver; an approved and merged document
change is one acceptable record of approval.

## Governing documents

Every heavy project has distinct, approved constitution and project PRD
documents before feature approval, plus a current architecture description.
Use ADRs for material decisions. A document change becomes binding when its
project-named human approver accepts it. A feature conflicting with a governing
document waits for that document to be amended and approved. Issues may link
governing text but do not become its authority.

| Document | Canonical content | Guide |
| --- | --- | --- |
| Constitution | Principles, binding engineering rules, amendment governance, and project-specific exceptions. | [GitHub Spec Kit constitution template](https://github.com/github/spec-kit/blob/main/templates/constitution-template.md) |
| Project PRD | Purpose, users, scope, stable requirement IDs and wording, assumptions, and measurable success criteria. Feature specs refine it. | [Atlassian PRD template](https://www.atlassian.com/software/confluence/templates/product-requirements) and [Spec Kit specification template](https://github.com/github/spec-kit/blob/main/templates/spec-template.md) |
| Architecture | Goals and quality needs, constraints, system context, major building blocks and interfaces, important runtime and deployment views, and links to ADRs. | [arc42](https://arc42.org/overview/) for structure and [C4](https://c4model.com/diagrams) for useful diagrams; start with context and container views. |
| ADR | One material choice with status, context, considered options, rationale, consequences, and links to affected architecture and capabilities. | [MADR](https://github.com/adr/madr/blob/develop/template/adr-template.md) |

Heavy projects favor [hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture)
where meaningful domain and external boundaries exist. The constitution states
the preference; the architecture document names actual ports, adapters, and
material departures. [Architecture Patterns with Python](https://www.cosmicpython.com/)
is the preferred Python guide. Simple scripts and leaf libraries need no
ceremonial port structure. Existing code does not require a blanket rewrite:
record departures, recommend valuable refactors, preserve behavior, and migrate
in small verified steps through SP-BP and SP. The existing
`gzs-hexagonal-architecture-audit` can identify boundary problems and coach
refactoring but does not implement it. [Incremental displacement](https://martinfowler.com/bliki/StranglerFigApplication.html)
and expand-contract are guides where they fit.

Heavy projects also favor TDD, BDD, and DDD as proportional working practices.
Relevant specs and plans show how they apply, or explain a material departure.
For BDD, agree on concrete behavior examples and trace them to verification;
neither Gherkin nor Cucumber is mandatory. This follows [Cucumber's BDD
practice](https://cucumber.io/docs/bdd/) without mandating its tool.

## MPAS curation

Start with four attributed, self-contained adaptations:

- `gzs-mpas-grill-with-docs`, incorporating the upstream `grilling` behavior
  and writing to the approved document locations and ADR shape;
- `gzs-mpas-domain-modeling`;
- `gzs-mpas-codebase-design`; and
- `gzs-mpas-improve-codebase-architecture`.

Do not ship `grilling` as a separate public dependency. SP remains the feature
specification and implementation spine; SP-BP owns issue and release state.
MPAS `to-spec`, `to-tickets`, `implement`, `triage`, TDD, review, debugging,
and handoff workflows are not in this initial curation because their roles
overlap the chosen components. The upstream [MPAS catalog](https://github.com/mattpocock/skills/blob/main/README.md)
and [MIT license](https://github.com/mattpocock/skills/blob/main/LICENSE) inform
the adaptation. A repository maintenance chore records each source path and
commit, checks upstream changes, reviews each adaptation, preserves attribution,
and updates its skill version and changelog when shipped behavior changes.
Never overwrite an adaptation automatically.

## Semantic identity and issue graph

Use [FDAU's taxonomy and identity rationale](https://github.com/tvproductions/xplane-fdau/blob/cba17ec67e458db5a007a19f8c7b0885e53e46fa/docs/project/backlog-governance-model.md)
as a starting point, adapting its Markdown authority to SP-BP's GitHub Issue
substrate. Each approved PRD requirement receives a stable semantic ID and a
GitHub Issue anchor. The PRD owns its wording and approval state; the issue
links to it, the delivery outcomes it governs, and change discussion. Issue
edits cannot approve or supersede a requirement.

Capability families and planned reviewable outcomes also receive stable,
release-independent semantic IDs, such as FDAU's `C2` and `C2.3`. Their GitHub
Issue numbers are tracker addresses, not semantic IDs. Epics, milestones,
release gates, and external boundaries each receive one node kind, semantic ID,
and issue anchor; only local reviewable outcomes are execution candidates.
GitHub Issues also track proposals, bugs, defects, surprises, and refactors.
An incidental issue needs no additional semantic ID unless promoted to an
enduring requirement or planned roadmap node. A release has its own stable
record and issue anchor, separate from a planned or published version.

Approved IDs are never reused. An administrative family move preserves the ID
and records the current family. A changed meaning receives a new ID with an
explicit successor, split, merge, or supersession link. Preserve old aliases
and historical references. Requirements, outcomes, ADRs, and releases have
many-to-many typed relationships; no single record carries all their statuses.
Keep target release mutable and `released_in` immutable once published.

SP-BP's current [issue contract](https://github.com/tvproductions/superpowers-backplane/blob/27679be948042cf2f6a698508ea34b19648eae71/skills/managing-superpowers-backlog/references/github-issue-contract.md)
applies one execution-label ladder to tracked open issues and excludes local
roadmap/backlog authority. The new design must explicitly supersede those
parts: execution labels belong to executable leaves; requirement approval,
epic grouping, gates, external boundaries, and release state have their own
typed semantics. A native issue relationship represents decomposition or
blocking when it fits; typed semantic links represent requirements, decisions,
evidence, and releases. Issue bodies and comments remain untrusted input.

## Traceability, V&V, and views

SP-BP reconciles approved requirement definitions, their issue anchors,
capability/outcome issues, SP specs and plans, agreed behavior examples,
verification evidence, review, and release records. A derived trace view shows
both forward and reverse links and flags missing, ambiguous, or stale ones.
An outcome cannot become `verified` while a governing requirement it claims
lacks current verification evidence. A changed approved requirement triggers
impact analysis and review of affected evidence before a later release;
earlier verification stays in history.

Use [ISO/IEC/IEEE 29148](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29148%3Aed-2%3Av1%3Aen)
for requirements identity and traceability concepts, and [NASA's verification
and validation matrices](https://www.nasa.gov/reference/system-engineering-handbook-appendix/)
as examples of distinct evidence. Verification shows that specified
requirements were fulfilled. Validation checks intended use and stakeholder
needs against the PRD's users and success criteria. The project chooses
appropriate tests, demonstrations, stakeholder review, or measured outcomes;
the release record links the result and accepting person. Aviation-specific
FAA guidance belongs in an applicable project's own standards profile, not in
every adopting repository. FDAU's `S1.1` traceability contract is still queued,
so its implemented node/status model is precedent, not proof of completed V&V.

GitHub Issues own roadmap node kind, outcome, dependencies, and mutable
delivery state. Commit `ROADMAP.md` and `BACKLOG.md` as readable derived views,
not alternative editing surfaces. Generate them from a validated issue and
approved-document snapshot. Record an input hash, recheck revisions before
publishing, and retry collection when a source changes. A project-owned check
compares a proposed view with its source; inability to verify freshness must
not be reported as current state. The exact snapshot and offline policy need
implementation design and proof.

## Releases and compatibility

An adopting project declares the public APIs, formats, behavior, or other
compatibility promises to which [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html)
applies. A release record selects outcomes and links its gate, trace, V&V,
compatibility review, and human publication decision. Publication requires all
included outcomes verified, current requirement traces, a distinct validation
result against intended use, compatibility review, and explicit human
authorization. `verified`, candidate release assignment, approved publication,
and a published tag are separate facts. SP-BP must not import gzkit's ledger,
locks, receipts, or full lifecycle.

During `0.x`, new or incompatible capability advances minor and compatible
fixes or behavior-preserving refactors advance patch. A human decides when to
declare `1.0.0`. After `1.0.0`, compatible capability advances minor,
compatible fixes advance patch, and breaking public-contract changes require
major with human discussion before publication. A release version never
serves as a requirement, outcome, ADR, or issue ID.

## Remaining design and proof work

1. Prove first-use routing and native installation/version discovery on Claude
   Code, Codex, and OpenCode. Test with and without available hooks, both direct
   and model-selected invocation, and resumption of the original task. Specify
   the shared settings schema extension and a tested compatibility set without
   storing machine-local installation state.
2. Write the SP-BP issue-kind and relationship schema, reconciliation rules,
   snapshot algorithm, view formats, and release gate. State the Python core
   decision in SP-BP's ADR and plan, including migration of any Go prototype.
   Explicitly supersede conflicting issue-only decisions only after review in
   the SP-BP repository.
3. Pilot migration on representative existing documents and FDAU-like nodes.
   Test family moves, splits, requirement changes, multi-outcome traces,
   stale evidence, changing issues during snapshot collection, and a release
   slip without renaming identities.
4. Select the exact MPAS upstream commits, record attribution and licenses,
   adapt the four skills, and establish the refresh chore. Validate their
   cross-harness invocation and interactions with SP and SP-BP.
5. Add source-backed traceability and V&V rationale to the SP-BP design,
   including applicable FAA material only where a consuming project declares
   an aviation or other regulated context.

This candidate changes no skill, SP-BP repository, adopting project, plugin
installation, GitHub issue, or release configuration.
