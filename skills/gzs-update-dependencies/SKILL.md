---
name: gzs-update-dependencies
description: Assess freshness or update project-managed dependencies, runtime pins, tools, adopted templates, and agent plugins against project policy. Use for dependency freshness checks, outdated-version reviews, package/tool upgrades, lockfile refreshes, or bringing a project's toolchain current; a freshness-only request leaves dependency state unchanged.
compatibility: Requires network access to authoritative package and tool sources plus the package managers used by the target repository.
metadata:
  govzero-version: "0.2.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Update Dependencies

Assess or refresh the complete project-managed dependency and toolchain surface.
Discover the repository's actual ecosystems and policy first; do not assume
Python, Node, a particular runtime version, or a particular quality command.

This skill covers versions recorded by the project. Updating unrelated global
machine tools, operating-system packages, editor extensions, cloud resources, or
deployed environments requires separate explicit authorization.

## Choose the requested mode

- **Freshness review:** Requests to check freshness, find outdated dependencies,
  or assess whether versions need updating authorize assessment only. Inventory
  and query authoritative sources, then recommend adopt or defer decisions.
  Leave manifests, pins, locks, installed plugins, and environments unchanged;
  use read-only queries rather than installs, synchronization, or lock generation.
  Run workflow steps 1-4 and report findings with checked dates and evidence.
  Verification of a proposed version remains pending unless it was actually
  tested in an authorized isolated environment. Do not infer an upgrade request
  from this skill's invocation alone; if no mode is established, review first.
- **Update:** Requests to upgrade or refresh dependencies authorize the scoped
  maintenance change and verification in steps 1-9. Preserve the approved release
  families, project additions, and exceptions. A reviewed recommendation from an
  earlier assessment does not itself authorize applying it.

An on-demand review does not create schedules, hooks, or new CI gates. Use
`gzs-dependency-risk-audit` when the requested result is a broader vulnerability,
support, license, or supply-chain assessment; release age alone is not evidence
of abandonment.

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
as drift. A repository using `.gzkit/` has its own project workflow; yield
execution to that workflow and report any standard mismatch to its owner.

An approved project or adopted starter policy defines the effective baseline;
the defaults below apply where that policy leaves a choice open. Preserve its
selected runtime family, additional runtime packages, optional features,
development groups, package sources, and reviewed constraints or overrides.
Inventory and update those additions within the authorized scope alongside the
baseline. Never replace the project's declarations with a baseline-only list or
reintroduce a tool its approved policy has retired. Record compatibility evidence
and reasons for intentional differences; unexplained drift remains a finding.
Application settings and local workflow extensions retain their project-owned
schemas and precedence. Do not put them in the minimal gz-skills profile file.

For the GovZero heavy Python standard, use the same development assortment in
both profiles:

- Astral: uv, Ruff, ty.
- Code quality: Bandit, Vulture, Interrogate, detect-secrets.
- Tests: standard-library unittest, Coverage, Behave, unittest-parallel,
  Cosmic Ray.
- Complexity: Radon, Xenon, Lizard, Cohesion.
- Documentation: MkDocs, MkDocs Material.
- Packaging: uv_build is the target for pure-Python packages; inspect wheel,
  sdist, installed entry point, and resources before replacing a backend.
  PyInstaller is included only when shipping a standalone executable.

Use the latest supported patch within the project's approved runtime family;
the default guidance is 3.13.x for ordinary Python and 3.12.x for
XPPython3-oriented code when no other family is adopted. A family change is a
separate compatibility decision, not an automatic consequence of refreshing
the patch. The `.python-version` file records the exact current
development patch; a 3.12.x pin is a hint, so confirm host orientation from
the code and project policy. Keep `requires-python` as the tested package
compatibility range. The XPPython3 development environment is separate from
the host interpreter. Pydantic is an approved, optional runtime dependency
for ordinary Python and excluded by policy from the XPPython3 profile; do not
add it merely because it is permitted. Start runtime dependencies from the
standard library and add others only for shipped capabilities. Development
tools must not enter the runtime unless the product actually uses them as
libraries.

The project defines quality commands, thresholds, accepted exceptions, and
mutation scope. Bring missing standard packages into its development group
and lock, but do not invent a numeric gate, impose a repo-wide mutation score,
remove an approved dependency, or change a published compatibility claim
without evidence. If package-layout parity, host compatibility, or another
binding constraint prevents reconciliation, preserve the working state and
report the precise unresolved item; do not claim the profile is current.

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
