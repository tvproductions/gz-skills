---
name: gzs-update-dependencies
description: Reconcile an adopted project profile and refresh project-managed dependencies, runtime pins, package-manager tooling, lockfiles, and development tools to current supported releases, then run full verification. Use when the user asks to update all dependencies and tools, upgrade packages, refresh lockfiles, bump runtimes, or bring a project's toolchain current.
compatibility: Requires network access to authoritative package and tool sources plus the package managers used by the target repository.
metadata:
  govzero-version: "0.2.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Update Dependencies

Refresh the complete project-managed dependency and toolchain surface as one
reviewable maintenance change. Discover the repository's actual ecosystems and
policy first; do not assume Python, Node, a particular runtime version, or a
particular quality command.

This skill covers versions recorded by the project. Updating unrelated global
machine tools, operating-system packages, editor extensions, cloud resources, or
deployed environments requires separate explicit authorization.

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
tooling. Profile reconciliation is part of this update: add missing required
tools, correct dependency-group placement, refresh stale constraints and
locks, and align CI and documentation. Do not limit the pass to packages
already declared. Read project-specific exceptions before treating a difference
as drift. A repository using `.gzkit/` has its own project workflow; yield
execution to that workflow and report any standard mismatch to its owner.

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

Use the latest supported 3.13.x patch for ordinary Python and 3.12.x for
XPPython3-oriented code. The `.python-version` file records the exact current
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
   current project policy says to advance it.
4. Resolve target versions from authoritative live sources: official package
   registries, runtime release indexes, vendor release metadata, or the
   package-manager's own current-version command. Read release notes for major
   versions and for any release whose compatibility is uncertain. Record
   unavailable or ambiguous evidence rather than guessing.
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

Report each discovered ecosystem, adopted-profile mismatches and resolutions,
before/after runtime and tool versions,
manifest and direct-dependency changes, lockfile changes, constrained or skipped
updates with reasons, vulnerability results, verification commands and results,
and final worktree scope. Never describe the project as fully current when an
inventoried surface lacks authoritative status evidence.
