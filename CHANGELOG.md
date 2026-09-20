# Changelog

All notable changes to the released GovZero skills bundle are recorded here.
Each skill also carries an independent `metadata.govzero-version` for selective
fleet updates.

## Unreleased

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
