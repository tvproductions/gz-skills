---
name: gzs-update-dependencies
description: Update project-managed dependencies, runtime pins, tools, adopted templates, and agent plugins and verify the result under project policy. Direct invocation requests completed updates. Use for dependency maintenance, upgrades, lockfile refreshes, and toolchain updates; an explicit check, freshness review, or no-changes request remains read-only.
compatibility: Requires network access to authoritative package and tool sources plus the package managers used by the target repository.
metadata:
  govzero-version: "0.5.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Update Dependencies

Update the complete project-managed dependency and toolchain surface and verify
the result. Perform a read-only assessment only when the user requests one.
Discover the repository's actual ecosystems and policy first; do not assume
Python, Node, a particular runtime version, or a particular quality command.

This skill covers versions recorded by the project. Updating unrelated global
machine tools, operating-system packages, editor extensions, cloud resources, or
deployed environments requires separate explicit authorization.

This skill works standalone and requires no project orchestrator. When a
project-owned workflow is already active, preserve its scope, sequencing,
approvals, locks, gates and evidence requirements for updates and reviews. Stop before
mutations whose required approval is absent. Do not create parallel lifecycle
state or declare the containing workflow complete.

## Act on the request

Invoking `$gzs-update-dependencies` is a request to update dependencies, including
when the invocation is the entire message. Discover the project scope and policy,
then complete the updates and verification in steps 1–9. Do not stop after an
inventory, version table, recommendation or offer to apply, and do not ask for
another go-ahead for ordinary work already authorized by that invocation.

Honor the user's request, established conversation instructions and applicable
project policy. A handoff records existing authority; it does not grant new
permission. Carry an authorized update through handoffs and workflow corrections
unless the user stops, narrows or changes it. A correction to how the work proceeds is not by
itself a request to stop or return to review. Continue the authorized work
without another permission round for ordinary resolution, configuration,
compatibility fixes and verification within that scope.

- **Freshness review:** Requests to check freshness, find outdated dependencies,
  or assess whether versions need updating authorize assessment only. Inventory
  and query authoritative sources, then recommend adopt or defer decisions.
  Leave manifests, pins, locks, installed plugins, and environments unchanged;
  use read-only queries rather than installs, synchronization, or lock generation.
  Run workflow steps 1-4 and report findings with checked dates and evidence.
  Verification of a proposed version remains pending unless it was actually
  tested in an authorized isolated environment. An explicit review-only request
  controls even when the skill is invoked in the same message.
- **Update:** Requests to maintain, update, upgrade or refresh dependencies
  authorize the scoped maintenance change and verification in steps 1-9.
  Complete the update rather than ending with recommendations or an offer to
  apply them. Follow the governing compatibility and release-family policy,
  including migration to newer stable families when that authority calls for it;
  an old pin or allowed range alone does not override an authorized migration.
  Preserve project additions and approved exceptions. A reviewed recommendation
  from an earlier assessment does not itself authorize applying it.

Automatic skill selection follows the surrounding task: merely finding this
skill relevant does not turn an unrelated task into an update request. Preserve
project-required approvals and scope restrictions; name a concrete blocker when
one prevents completion rather than falling back to an unrequested review.

An on-demand review does not create schedules, hooks, or new CI gates. Use
`gzs-dependency-risk-audit` when the requested result is a broader vulnerability,
support, license, or supply-chain assessment; release age alone is not evidence
of abandonment.

## Project Python version and policy

For Python work, read project instructions and adopted policy before selecting
idioms, APIs or runtime targets. Resolve version evidence from the relevant
project's `.python-version` first, `pyproject.toml` second, and `.venv` third.
The version file records an execution selection; `requires-python` declares a
support range; the environment supplies an observed installed version. Use later
signals for fallback and consistency checks, not to override declared policy.
Inspect `pyvenv.cfg` and the environment interpreter when available; do not
create, activate or update an environment just to discover its version.

Reconcile these signals with tool/CI targets and the actual validation
interpreter. Report absent, ambiguous or conflicting evidence; do not infer
freshness from an installed version or a minimum supported version from one pin.
For host-bound code, inspect the host runtime separately; a development
interpreter does not establish the host's version or installed packages.

Within this skill's existing task scope, observe the selected family's current
Python idioms, stdlib advances and deprecations using versioned official
documentation. Preserve the project's tested support range and public behavior;
record concrete benefits, risks and adopt/defer/retain decisions. Follow project
policy over upstream defaults. A runtime upgrade alone does not establish code
currency, and this guidance does not authorize a broad modernization campaign or
turn this skill into a comprehensive Python-version audit.

## Discovery and fallback

Prefer, in order:

1. The repository's documented upgrade command, which already encodes its
   floors and intentional pins.
2. The project's package manager, used for resolution, lock regeneration, and
   its own current-version query.
3. The declared manifests and lockfiles read directly, with target versions
   resolved from the authoritative registry for each ecosystem present.

The third rung is the floor and needs only the manifest and network access to
the registry. Offline, it degrades honestly: inventory and current constraints
remain establishable, target versions do not. Record the unavailable evidence
rather than guessing a version.

## Adopted heavy Python profile

If the repository has selected `heavy` in `.gz-skills/settings.json`, or has
an equivalent approved Python environment standard, compare that profile with
the actual manifests, `.python-version`, lock, CI, and installed development
tooling. In update mode, profile reconciliation includes adding missing required
tools, correcting dependency-group placement, refreshing stale constraints and
locks, and aligning CI and documentation. Do not limit the pass to packages
already declared. Read project-specific exceptions before treating a difference
as drift.

An approved project or adopted starter policy defines the effective baseline.
Resolve the recorded authority and applicable revision before selecting runtime
families, tools, package permissions or gate cadence. Preserve its approved
exceptions, additional packages, optional features, development groups, sources
and compatibility constraints. A mode selection does not itself adopt a starter
or supply an environment standard.

Record authority, selected family, exact execution pin, supported range, host
constraints, required tools and verification commands as separate findings.
Where governing policy is missing, unavailable or contradictory, report that
requirement UNKNOWN and request the missing decision. Do not substitute an
internal default, infer policy from the installed runtime, or interpret an
unavailable adopted source as permission to choose another baseline. Continue
independent authorized inventory while leaving dependent changes unresolved.

Use the project's required assortment when reconciling missing tools. This
portable skill owns no fallback Python family, fixed tool list or runtime-package
allow/deny policy. Never replace a project's declarations with a library-owned
baseline or reintroduce tools the project has retired. Keep application settings
in their owning schema, not the minimal gz-skills profile file.

Refresh patches within the approved runtime family unless governing project
policy or the user authorizes a family migration. Distinguish package support
from development execution and host interpreter compatibility. Inspect actual
host-bound loading behavior; a development pin alone does not establish that a
project loads in a host.
Keep development tools outside shipped runtime dependencies unless the product
uses them as libraries. Preserve project manager compatibility requirements
separately from an exact tested CI version; do not impose a matching-version
rule the governing policy does not require.

The project defines quality commands, thresholds, exceptions and mutation scope.
Reconcile required packages in their existing groups and lock without inventing
new numeric gates, removing approved dependencies or expanding public support
claims without evidence. If a binding constraint prevents reconciliation,
preserve the working state and name the unresolved item; do not claim readiness.

## Workflow

1. Read the repository's applicable agent guidance and inspect the worktree.
   Identify pre-existing changes that overlap dependency surfaces before any
   metadata or lockfile mutation.
2. Inventory every project-managed dependency surface and applicable adopted
   profile. Read [references/inventory.md](references/inventory.md) and retain
   only categories evidenced by the repository. Completion means every
   manifest, lockfile, runtime pin, package-manager pin, CI action, hook,
   container base, and bundled
   external tool in use is either included or explicitly classified as outside
   the user's requested project scope.
3. Capture current versions and constraints, including required tools absent
   from an adopted profile. Identify the repository's stated compatibility
   floors, intentional pins, generated files, update commands, and complete
   verification command. Preserve an intentional compatibility range unless
   current project policy says to advance it. Keep the declared support floor,
   tested exact pin, newest stable release in the selected family, and newest
   upstream family distinct. Include optional/deferred components as such; a
   recorded pin does not establish installation or readiness.
4. Resolve target versions from authoritative live sources: official package
   registries, runtime release indexes, vendor release metadata, or the
   package-manager's own current-version command. Read release notes for major
   versions and for any release whose compatibility is uncertain. Record
   unavailable or ambiguous evidence rather than guessing. Compare within each
   explicitly selected release family first; report newer families separately
   with migration implications. A lock or installed interpreter is not evidence
   of freshness. For a freshness review, stop mutations here and report.
5. Update the package manager or project-pinned tool that performs resolution
   before using it to regenerate dependency state. Reconcile missing or misplaced
   adopted-profile tools, update declared manifests and exact runtime pins
   intentionally, then regenerate lockfiles with their owning tools. Never edit
   a generated lockfile by hand.
6. Apply updates in coherent ecosystem-sized batches so a failure can be traced
   to its owner. Adapt source and tests for breaking changes supported by release
   evidence. Do not weaken a quality rule, lower a tested floor, or silently pin
   an offender merely to make the upgrade appear green.
7. Synchronize all declared dependency groups and verify that a second lock or
   resolution check produces no unexplained churn. Run the package manager's
   outdated and vulnerability checks when available, and classify constrained,
   yanked, vulnerable, or unverifiable results precisely.
8. Run the repository's complete required verification, including generated
   artifact or packaging checks when dependency changes can affect shipped
   output. Fix failures caused by the update and rerun from the first affected
   gate.
9. Inspect the final manifest, lockfile, code, documentation, and generated-file
   diffs. Confirm no dependency surface was silently omitted and no unrelated
   user change was absorbed.

## Failure posture

- A network, registry, parse, resolver, vulnerability, compatibility, or
  verification failure blocks a claim that the project is current.
- When one release is incompatible, keep the last verified compatible version,
  state the precise constraint, and leave the rest of the completed upgrade in a
  reviewable state when project policy permits.
- Do not delete lockfiles, caches, or environments as a first response. Diagnose
  the owning tool and preserve recoverable user state.
- Do not expand a project dependency refresh into deployment or machine-wide
  maintenance.

## Evidence

State the requested mode and checked date. For each package, tool, template,
or plugin, report the current pin/revision, declared support range or selected
family, latest stable compatible target and upstream release, authoritative
evidence, compatibility constraints, and adopt/defer decision. Distinguish
unknown latest status, missing installation evidence, and untested compatibility
from verified results. A freshness review reports recommendations and pending
checks, not a completed upgrade or a claim that a new target is tested.

For updates, also report each discovered ecosystem, adopted-profile mismatches
and resolutions, before/after runtime and tool versions,
manifest and direct-dependency changes, lockfile changes, constrained or skipped
updates with reasons, vulnerability results, verification commands and results,
and final worktree scope. Never describe the project as fully current when an
inventoried surface lacks authoritative status evidence.
