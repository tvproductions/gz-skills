# Changelog

All notable changes to the released GovZero skills bundle are recorded here.
Each skill also carries an independent `metadata.govzero-version` for selective
fleet updates.

## Unreleased

## 0.8.3 - 2026-10-25

Bundle **0.8.3**, compared with released v0.8.2: promote the individually
accepted `gzs-git-sync` contract from 0.1.1 to **1.0.0**. Its workflow,
activation and authorization instructions are unchanged. The compatible
stability-metadata change advances the bundle by one patch; no migration is
needed. Other skill versions are unchanged, and the bundle remains pre-1.0
until the catalog review completes. Both marketplace pins select v0.8.3.

### Changed

- Complete the individual `gzs-git-sync` stable-contract review against released
  0.1.1 in v0.8.2. Record 22 native sessions across Codex, Claude and OpenCode,
  including baseline, negative requests and retained fixture limitations.
  Execution verifies post-rebase validation and project approval boundaries.
  The evidence itself changes no workflow; this release promotes only the
  accepted Git sync contract, not the catalog as a whole.

## 0.8.2 - 2026-10-25

Bundle **0.8.2**, compared with released v0.8.1: compatible Git sync
contract corrections advance `gzs-git-sync` from 0.1.0 to 0.1.1 and the bundle
by one patch. No migration or stable-contract promotion is included. Marketplace
pins and installation examples select v0.8.2.

### Fixed

- Enforce uv-only Python execution, Ruff lint/format and ty checking in repository
  guidance. Correct existing test lint/type issues and format packaged helpers.
  `gzs-project-setup` 0.3.0 → 0.3.1 adds an explicit initialization type annotation;
  `gzs-cross-platform-python` 0.3.0 → 0.3.1 formats its helper. Both are compatible,
  behavior-preserving corrections covered by bundle 0.8.2.

- Require applicable quality gates on reconciled content before Git sync pushes,
  including conflict-free rebases, and explicitly retain the active project's
  sequencing, approvals, locks, gates and lifecycle authority. Report any
  post-reconciliation validation in completion evidence.

- Record native OpenCode inference under the existing no-training policy,
  replacing the contributor-model fallback with a tested non-training model.
  The user authorized that model as their local default; workspace privacy
  settings remain unchanged. Preserve prior failures and the separate
  invocation-guidance finding instead of claiming universal behavioral success.
  This evidence update itself changes no skill contract and grants no stable-version
  promotion.

## 0.8.1 - 2026-10-25

Bundle **0.8.1**, compared with released v0.8.0: compatible router and
quality-gate corrections require a patch. All bundle manifests, source fallback
and lock select 0.8.1; marketplace refs and installation examples select v0.8.1.
No consumer migration or stable-contract promotion is included.

| Skill | Previously released | This release | Classification |
| --- | --- | --- | --- |
| `gzs-router` | 0.5.0 | 0.5.1 | Compatible fallback and host-invocation wording corrections |
| `gzs-quality-gate` | 0.1.1 | 0.1.2 | Compatible final-verification fallback correction |

### Fixed

- Correct the router fallback to allow an explicit no-match orientation answer,
  and reconcile extraction provenance with current user/model invocation.
  Native Claude validation also exposed a hard-coded dollar invocation; prefer
  the observed harness command syntax and plugin namespace, or report it as
  unverified instead of presenting an assumed exact command.
  Compared with released v0.8.0, `gzs-router` advances from 0.5.0 to 0.5.1 as a
  compatible wording correction, covered by bundle 0.8.1. No activation
  policy or migration changes. The review records correction evidence.
  Seven authorized native Claude sessions provide selected positive,
  negative, no-match, host-syntax, diagnostic and workflow-precedence evidence,
  including a no-skill control. Earlier authentication/approval blockers were
  resolved. Selected native Codex snapshot checks also pass after restoring its
  existing Windows sandbox implementation for the isolated process. OpenCode
  authentication and its launcher were restored. OpenCode 2.1.4 loads the
  candidate skill tree; provider privacy restrictions still block behavioral
  inference. Full cross-harness stable acceptance remains pending.

- Reconcile the roadmap with the twenty-skill catalog, pending patch publication,
  closed issue #1 and remaining proposals; complete the stable-contract review
  queue with project setup and both Pythonic pattern skills. Keep SP-BP work
  with its owner and integrated heavy readiness explicitly unproven. This is
  repository-only planning documentation; skill and bundle versions are unchanged.

- Correct `gzs-quality-gate` final verification for repositories without an
  aggregate gate (issue #1): run the complete sequence resolved during discovery,
  require every command to succeed, and retain missing required commands as
  explicit gaps that prevent a full-pass claim. Compared with released v0.8.0,
  the skill advances from 0.1.1 to 0.1.2 and the bundle from 0.8.0 to
  0.8.1 as compatible corrections. Bundle manifests, source fallback and lockfile
  agree; marketplace pins select v0.8.1. No migration is required.

Validation: all 28 unittest cases and all twenty Agent Skills specification
checks pass. Claude strict plugin/marketplace validation and Codex native
candidate loading pass. Codex and Claude HTTPS marketplace installs from the
preceding immutable v0.8.0 pass in disposable configurations. OpenCode 2.1.4
loads the local candidate through its native skill registry; this is distinct
from inference. Artifact digests and tagged-channel acceptance are recorded
with the GitHub release after publication.

## 0.8.0 - 2026-10-11

Bundle **0.8.0**, compared with published v0.7.0: a new portable release
capability requires a bundle minor under the 0.x policy. Four manifests and the
source version fallback select 0.8.0; marketplace refs and installation examples
select v0.8.0 for this authorized release.

| Skill | Previously released | This release | Classification |
| --- | --- | --- | --- |
| `gzs-release` | Absent | 0.1.0 | New version recommendation, candidate preparation and authorized release publication primitive |
| `gzs-router` | 0.4.0 | 0.5.0 | New release routing and distinction from ordinary Git synchronization |

Add `gzs-release` to the canonical tree, Claude catalog and explicit-only Codex
and OpenCode activation. Follow consumer policy for patch/minor/major decisions,
0.x behavior, gates and publication channels. Bare invocation recommends only;
preparation and publication require their respective request authority. Preserve
explicit version choices, immutable published tags and existing project
orchestrators. Verify remote release identities, artifacts and required channel
acceptance; report partial publication rather than treating a push as a release.

Consumer impact: the released catalog has twenty skills. Existing consumers
update explicitly; publisher-side release work does not change their pins or
installed caches. Validation and behavioral evidence are
recorded in [the initial release-skill review](docs/review/gzs-release-2026-10-11.md).
The OpenCode title assertion now accepts LF and CRLF without altering registered
content or activation behavior.

Verification: 28 unittest tests pass on the repository's actual Python 3.13.15,
including canonical catalog, relative links, explicit-only activation and
OpenCode adapter behavior. All twenty skills pass Agent Skills specification
validation; Claude strict marketplace/plugin validation and offline lock
consistency pass. The wheel and source archive contain all twenty canonical
skills, and the new release/router wheel bodies match source. Five independent
read-only forward scenarios found no demonstrated workflow defect. Native Codex marketplace loading passed in isolated
configuration, and preceding v0.7.0 HTTPS installs passed in Codex/Claude.
Fresh-session workflow execution remains unverified; tagged channel installs
and publication are verified separately after tagging. The older skill-creator quick validator's incompatible frontmatter allowlist is
recorded in the review evidence.

## 0.7.0 - 2026-10-11

Bundle **0.7.0**; new project-version-aware Python guidance extends the
five existing workflows without adding a skill or changing their activation
scope. Version decisions against v0.6.0:

| Skill | Released | This release | Classification |
| --- | --- | --- | --- |
| `gzs-pythonic-pattern-detect` | 0.1.0 | 0.2.0 | Runtime evidence and version-aware pattern review |
| `gzs-pythonic-pattern-apply` | 0.1.0 | 0.2.0 | Runtime evidence and version-aware authorized refactoring |
| `gzs-cross-platform-python` | 0.2.0 | 0.3.0 | Runtime evidence and version-aware OS-seam review |
| `gzs-project-setup` | 0.2.0 | 0.3.0 | Project runtime/policy discovery before environment guidance |
| `gzs-update-dependencies` | 0.2.0 | 0.3.0 | Project runtime/policy discovery and scoped code-currency assessment |

Resolve project version evidence from `.python-version`, then `pyproject.toml`,
then `.venv`, distinguishing selected execution patch, declared support range and
observed installed interpreter. Report missing/conflicting evidence and verify
host runtimes separately. Respect adopted project/starter family and engineering
policy over defaults. Within the existing task scope, assess relevant current
idioms, stdlib advances and deprecations against versioned official documentation;
record benefits, risks and adopt/defer/retain decisions. Do not equate a runtime
upgrade with current code or authorize a broad modernization campaign.

No project-specific Python family, tool assortment, gate or template identity is
introduced. Existing environment defaults, profile schema, installer behavior,
read-only/update boundaries and catalog membership remain intact. Bundle/skill
minors cover the added workflow requirements; all other skill versions are
unchanged. Both marketplace refs select v0.7.0. Consumer updates remain explicit; this
release does not migrate installed plugins or consumer pins.

Verification: 28 unittest tests pass on the repository's Python 3.13.15; all
nineteen skills pass Agent Skills specification validation. The 0.7.0 wheel and
source archive build successfully; both contain nineteen canonical skills and
the five changed wheel instruction bodies match source. Claude strict plugin
and marketplace validation passed; Codex's native loader accepted the 0.7.0
candidate. Disposable HTTPS marketplace installs of the preceding v0.6.0 passed
in both hosts. Published-tag installs are verified separately after publication;
fresh-session workflow execution and combined SP/SP-BP readiness remain distinct
from installation evidence. Artifact SHA-256 values accompany the GitHub release.


## 0.6.0 - 2026-10-11

Version decisions against v0.5.0:

| Skill | Released | This release | Classification |
| --- | --- | --- | --- |
| `gzs-project-setup` | Absent | 0.2.0 | New setup and profile guidance, including customization. |
| `gzs-pythonic-pattern-detect` | Absent | 0.1.0 | New bounded Pythonic pattern review. |
| `gzs-pythonic-pattern-apply` | Absent | 0.1.0 | New authorized Pythonic refactor workflow. |
| `gzs-router` | 0.3.1 | 0.4.0 | New catalog routes and freshness-review routing. |
| `gzs-update-dependencies` | 0.1.1 | 0.2.0 | New profile reconciliation, review mode, and template/plugin inventory. |

Other skill versions are unchanged. The bundle minor covers the new capabilities
and incompatible Python CLI floor change. Python CLI consumers need Python 3.13
or newer; standalone setup helpers still support 3.11. Bare dependency-skill
invocation now starts with review unless update intent is established; explicitly
request upgrades to apply them. Existing template and plugin pins require a
deliberate consumer update; heavy profile integration remains candidate work.

### Added

- `gzs-project-setup` 0.2.0 creates minimal `.gz-skills/settings.json` on
  first project setup, asks for lite or heavy, blocks projects with `.gzkit/`,
  and supports lite-to-heavy promotion without claiming that other plugins are
  installed. Its Python helper lives inside the skill. Its heavy-profile
  guidance names the Python SP-BP project, carries and reconciles the agreed
  Python tool assortment, and keeps attributed MPAS adaptations inside this
  catalog. The new capability advances the bundle version
  to 0.6.0.
- `gzs-pythonic-pattern-detect` 0.1.0 reviews bounded Python pattern
  candidates without mutating code or requiring gzkit's scanner or corpus.
- `gzs-pythonic-pattern-apply` 0.1.0 applies one authorized refactor with
  unchanged before/after behavior evidence and project-owned verification.

### Changed

- Extend `gzs-update-dependencies` 0.2.0 with a freshness-only mode
  that queries current releases without changing dependency state, and an
  inventory of evidenced starter/template and agent plugin revisions alongside
  packages and tools. Distinguish support floors, tested pins, selected release
  families, compatible targets, and newer upstream families. Update mode keeps
  native source catalogs and provenance consistent while preserving local
  customizations and deferred components. `gzs-router` 0.4.0 routes both modes.
  These new capabilities share the accumulated skill minors and bundle 0.6.0.
- Clarify project customization in `gzs-project-setup` 0.2.0 and
  `gzs-update-dependencies` 0.2.0: preserve application dependencies, optional
  features, development groups, settings, and local workflow extensions;
  honor an approved project or starter baseline before environment defaults.
  Runtime refreshes stay within the adopted family, and retired baseline tools
  are not silently restored. Keep the setup helper's two-field schema unchanged.
  These edits share the accumulated versions: setup is new since v0.5.0,
  and the updater's new profile capability already requires its 0.2.0 minor.
  The 0.6.0 bundle minor covers the accumulated capability changes.
- `gzs-router` 0.4.0 routes project setup and the Pythonic review/application
  pair without substituting them for architecture auditing.
- `gzs-update-dependencies` 0.2.0 reconciles missing or stale tools,
  interpreter pins, and lock/CI state against an adopted heavy Python profile
  during a dependency refresh. It preserves project-owned exceptions and yields
  to an active gzkit workflow.
- Pin this repository's local development interpreter to Python 3.13.15 and
  raise the Python package compatibility floor from 3.11 to 3.13. This
  incompatible 0.x packaging change is covered by the 0.6.0 minor
  bundle version; standalone skill helper compatibility is unchanged.
- Define the reviewed normal Python and XPPython3-oriented install profiles
  for adopting heavy projects, grounded in the agents, va, and xp manifests.
  The shared development assortment covers Astral tools, code quality, tests,
  metrics, docs, and packaging; runtime dependencies remain capability-based.
  Interpreter support, exact versions, host compatibility, and verification
  remain project-owned decisions.
- Clarify the adopting-project plan for separate, portable Pythonic candidate
  review and behavior-preserving application, alongside hexagonal architecture
  auditing and the planned MPAS architecture curation.
- Advance both marketplace source refs and current installation examples to
  the immutable v0.6.0 release tag. Existing consumers update deliberately;
  this release does not change their locks, pins, or installed trees.

## 0.5.0 - 2026-09-20

### Changed

- The OpenCode package now targets v2: its adapter registers the canonical skill
  files through the v2 skill transform, with `gzs-git-sync` and
  `gzs-session-handoff` available only by explicit selection. Installation can
  be pinned in an adopting repository's `plugins` config. The adapter is
  outside this publisher repository's local plugin discovery path. The
  earlier v1 plugin contract is removed; v1 users remain on the immutable
  v0.4.0 bundle. This new bundle capability advances the pending version to
  0.5.0. Skill trees and their independent versions are unchanged.

## 0.4.0 - 2026-09-20

### Added

- `gzs-cross-platform-python` now carries `scripts/audit_portability.py`, the
  first deterministic helper in the catalog. Two static checks, standard
  library only, runnable on any platform: `line-endings` reads the git index
  for surfaces committed with CRLF and for a missing normalization directive,
  and `subprocess-errors` walks the syntax tree for text-mode captures that
  decode child output without an errors argument. Neither check needs the
  defect to reproduce locally, which is what makes them useful: both failure
  classes are invisible on whichever platform continuous integration runs.
  Ported from a proven gzkit implementation and verified to report the same
  result at the same scope. The bundled script is a fallback, never a
  dependency for a project that already gates these seams.
- A repository `.gitattributes` normalizing every text file to LF, which this
  repository had been missing entirely. Its own new `line-endings` check found
  the gap. All 70 tracked files were already LF in the index, so the directive
  locks in the current state rather than renormalizing anything.
- `gzs-cross-platform-python` gained a byte-exact fixture rule. A test that
  asserts exact bytes must not build its fixture with a text-mode write, which
  translates the newline to the platform separator.

- `scripts/inventory_skills.py --check-floor` verifies that every authored
  skill declares a non-empty discovery-and-fallback section, and the repository
  contract suite runs it. `AGENTS.md` has required discovery-or-fallback since
  it was authored, and the catalog still drifted to one compliant skill in
  sixteen because nothing reported it. `FLOOR_PENDING` carries the fourteen
  skills authored before the witness existed and may only shrink: a skill that
  gains the section while still listed there also fails, so the exemption is a
  countdown rather than a standing waiver. Both arms were verified to fire
  against real catalog entries. The check witnesses that a floor is declared,
  never that the floor named is a good one.

- All fourteen remaining skills now declare a discovery-and-fallback floor, so
  `FLOOR_PENDING` is empty and the countdown it existed for is finished. Each
  floor is written to that skill's own terminal action rather than stamped from
  a template: the review skill falls back to the diff, the architecture audit to
  reading imports, the router to the catalog that ships with it, the handoff to
  the response itself. Three floors state a limit rather than a command,
  because the honest floor for those skills is a narrowed claim: an offline
  dependency audit can establish exposure but not current safety, a context diet
  with no owning tool cannot regenerate mirrors, and a debt review without
  probes reaches fewer categories. Each skill advances a patch version.
- `gzs-session-handoff` and `gzs-git-sync` move their existing inline ladders
  into the canonical section. Neither changed what it does.

### Changed

- `gzs-cross-platform-python` states a discovery and fallback order, as the
  skill contract in `AGENTS.md` requires. It prefers a repository-local check,
  then a documented project command, then the bundled script, and records that
  a fail-closed project gate keeps its implementation in the repository it
  guards.
- Skill version advanced to 0.2.0 for new capability; bundle advanced to 0.4.0.

## 0.3.2 - 2026-09-20

### Fixed

- Switched the Claude marketplace plugin source to a pinned HTTPS Git URL.
  The `github` source in 0.3.1 attempted an SSH clone, so public installs
  failed on machines without a GitHub SSH key. Verified HTTPS installation
  with Claude Code against the 0.3.1 tag before this release.
- Advanced both marketplace refs, installation examples, and synchronized
  bundle metadata to 0.3.2. Skill trees and independent skill versions remain
  unchanged.

## 0.3.1 - 2026-09-20

### Fixed

- Added a Codex-specific repository marketplace manifest with the supported
  Git URL source format. The 0.3.0 Claude marketplace entry was skipped by
  Codex, so Codex marketplace installation failed.
- Pinned both Codex and Claude marketplace entries and all installation
  examples to the 0.3.1 release tag; advanced synchronized bundle metadata.
  No skill tree changed, so individual skill versions remain unchanged.

## 0.3.0 - 2026-09-20

### Changed

- Advanced gzs-session-handoff from the released 0.1.0 to 0.2.0. The new
  resume point, durable fallback, and standing-authorization handling expand its
  0.x workflow; its individual stable-contract review remains pending.
- Pinned the shared Codex and Claude repository marketplace to the released
  bundle tag; corrected the OpenCode install example and documented version
  and release decisions.
- Advanced the synchronized bundle manifests to 0.3.0 for the backward-
  compatible catalog expansion.
- Extended `gzs-router` to 0.3.0 with routing and composition guidance for the
  three promoted workflows.

### Added

- Added `gzs-change-review` 0.1.0 for prioritized, evidence-backed review of a
  bounded implementation change without silently implementing fixes.
- Added `gzs-dependency-risk-audit` 0.1.0 for read-first assessment of
  vulnerability, support, license, provenance, privilege, and supply-chain
  exposure across direct and transitive dependencies.
- Added `gzs-test-driven-change` 0.1.0 for explicitly requested test-first
  behavior changes using a verified red-green-refactor loop.

## 0.2.0 - 2026-09-06

### Changed

- Advanced the synchronized bundle manifests to 0.2.0 for the accumulated
  backward-compatible catalog and router expansion.
- Adopted the MIT License across the repository and package metadata.
- Defined the first 0.x release contract: immutable `v0.2.0` installs, clean
  build checksums, and unchanged canonical skills in the Claude package while
  behavioral reviews continue toward 1.0.0.
- Excluded local OpenCode development dependencies from Python source
  distributions and added a repository contract test for that boundary.
- Established a one-way composition boundary: `gz-skills` supplies standalone
  portable primitives beneath, and without duplicating, project-owned lifecycle
  orchestrators such as `gzkit`.
- Extended `gzs-router` 0.2.0 with guidance for discovering, invoking,
  installing, updating, and troubleshooting the GovZero skill catalog, with
  narrow implicit activation for catalog-specific questions.
- Clarified that `gzs-` namespaces canonical skill identifiers and invocation
  tokens, while skill headings and UI display names retain human-readable
  `GovZero ...` labels.
- Defined Semantic Versioning rules for the bundle and independently versioned
  skills, including changelog maintenance and unreleased-version handling.

### Added

- Added `gzs-hexagonal-architecture-audit` 0.1.0 as a read-only analyzer,
  design consultant, and refactor coach for right-sized hexagonal architecture,
  cross-project interoperability, and Pareto-selected supporting principles.
- Added `gzs-root-cause-debugging` 0.1.0 for evidence-led diagnosis that yields
  to active project-owned incident, execution, and governance workflows.
- Documented `gzs-change-review`, `gzs-dependency-risk-audit`, and
  `gzs-test-driven-change` as the next planned portable primitives, including
  their proposed boundaries and promotion criteria.
- The initial eleven portable GovZero skills under the collision-resistant `gzs-`
  namespace, including the `gzs-router` curator.
- Universal Agent Skills discovery through the canonical flat `skills/` tree.
- Native Codex, Claude Code, and OpenCode plugin adapters.
- A Python fleet CLI for pinned installation, status, safe update, and
  collection-wide propagation.
- Native plugins as the preferred consumer channel and Python `uvx` as the only
  supported project-vendoring toolchain.
- Full-tree provenance locks that block replacement of locally modified skills.
- Preserved all-project and candidate-user-authored inventory snapshots.
- Structural, installer, manifest, link, formatting, lint, and type validation.
