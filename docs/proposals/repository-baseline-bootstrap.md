# Opt-in repository baseline: discussion handoff

Status: proposal for a later gz-skills session; this document does not approve implementation.
Recorded: 2026-09-20.

## Maintainer direction

The maintainer wants a consistent, opinionated baseline for new and existing repositories. Adoption is optional; an adopter should receive enforceable checks rather than loose advice. Initial scope is Python and Go, with C/C++ considered from concrete projects. The baseline should audit an existing repository, show a migration plan, apply missing setup without destroying custom work, and verify the result.

The request arose after delivery drift in xplane-health: four open draft PRs, nine remote branch names already merged into main, one remote branch with unmerged work and no PR, no project-owned GitHub Actions test workflow, and no required main-branch check as observed on 2026-09-20. PR #34 had been review-clean since September 7; PR #42 was stacked on draft design PR #41. These are a dated snapshot, not fleet-wide counts. See [PR #34](https://github.com/tvproductions/xplane-health/pull/34), [PR #41](https://github.com/tvproductions/xplane-health/pull/41), and [PR #42](https://github.com/tvproductions/xplane-health/pull/42).

Matt Pocock's [implement documentation](https://github.com/mattpocock/skills/blob/main/docs/engineering/implement.md) says its run commits to the current branch and leaves PR creation and ticket closure outside the skill. The desired finishing behavior resembles [Superpowers' finish workflow](https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md): verify, present the integration choice, execute it, and clean up. Each repository still governs merge authorization and required checks.

## Evidence from adjacent repositories

These observations are pinned to local checkout commits. They show maintainer preferences; they do not make every tool setting a fleet standard.

| Surface | Observed practice | Source |
| --- | --- | --- |
| Python | xplane-fdau and xplane-webapi use uv, committed uv.lock, standard-library unittest, Ruff, ty, and repo-owned quality commands. Their PR CI runs those gates; package and compatibility jobs reflect product needs. | [xplane-fdau policy](https://github.com/tvproductions/xplane-fdau/blob/4b08f860d5c82fad915aec22a49fb326430b2dd5/AGENTS.md), [CI](https://github.com/tvproductions/xplane-fdau/blob/4b08f860d5c82fad915aec22a49fb326430b2dd5/.github/workflows/ci.yml), [xplane-webapi CI](https://github.com/tvproductions/xplane-webapi/blob/a855b8d885c75f8dda54daec1f54eb48f111b105/.github/workflows/ci.yml) |
| Python constraints | xplane-fdau, xplane-webapi, q4xpcc, and Ortho4XP explicitly use unittest rather than pytest. q4xpcc records uv, Ruff, ty, and pinned development tooling. | [q4xpcc policy](https://github.com/tvproductions/q4xpcc/blob/dea9bffd06aff3806ed6cc15a9e540abf9f50257/AGENTS.md), [Ortho4XP policy](https://github.com/tvproductions/Ortho4XP/blob/e528b20d61e26b91250061a819f3f88b632c7087/AGENTS.md) |
| Go | xplane-health uses gofmt, go mod tidy -diff, go list, go test, go vet, and pinned Staticcheck. A PowerShell aggregate gate tests under Windows PowerShell 5.1 and PowerShell 7. No project CI invokes it yet. | [Go standards](https://github.com/tvproductions/xplane-health/blob/ed3a1f4067e127a8a5194816729c91701cacb5ec/docs/agents/go.md), [gate](https://github.com/tvproductions/xplane-health/blob/ed3a1f4067e127a8a5194816729c91701cacb5ec/scripts/Test.ps1) |
| Native C/C++ | Ortho4XP's current native utility is C, built with LLVM/Clang, Ninja, and CMake presets; it has clang-format and clang-tidy configuration and CI builds on Linux, Windows, and macOS. q4xpcc describes the same toolchain for a future C++ sidecar. | [Ortho4XP presets](https://github.com/tvproductions/Ortho4XP/blob/e528b20d61e26b91250061a819f3f88b632c7087/Utils/CMakePresets.json), [CMake](https://github.com/tvproductions/Ortho4XP/blob/e528b20d61e26b91250061a819f3f88b632c7087/Utils/CMakeLists.txt), [q4xpcc policy](https://github.com/tvproductions/q4xpcc/blob/dea9bffd06aff3806ed6cc15a9e540abf9f50257/AGENTS.md) |

CTest is a possible future baseline choice, not an observed requirement: the inspected Ortho4XP native CMake file defines no CTest tests. The C++ test contract needs a concrete pilot. Mixed-language repositories need composable language and platform adapters.

## Proposed baseline contract

1. **Local quality:** each repository declares one complete aggregate command covering its applicable formatting, static analysis, tests, build, package, and documentation gates. CI invokes the same command or documented component commands with equivalent coverage.
2. **Hosted checks:** PR and default-branch CI run with minimal permissions and pinned tools. A stable quality check becomes required after it has run successfully and its exact identity is verified. Extra compatibility, packaging, and platform jobs follow product needs.
3. **Delivery:** reviewed work receives an explicit integration decision. A PR path verifies current head, required checks, merge result, originating issue transition, and branch/worktree cleanup. Deferred drafts remain visibly pending. A routine audit identifies branches already merged into the default branch and branches without PRs.
4. **Adoption:** the baseline has a version and a small explicit exception record. An audit distinguishes compliant, missing, conflicting, unavailable, and deliberately excepted states. Partial evidence is reported as partial.
5. **Ownership:** project commands and domain constraints remain project-owned. The opt-in baseline owns common minimum expectations. This expands the current boundary stated in this repository's AGENTS.md and README.md; amend that boundary explicitly before implementation.

Candidate interfaces are a focused repository-baseline skill for contextual audit, migration planning, and verification, backed by deterministic CLI checks and file templates. A separate finishing workflow would perform recurring per-change integration. Existing gzs-quality-gate and gzs-repository-hygiene are useful primitives, but neither should be stretched into the full bootstrap and delivery lifecycle.

For an existing repository, migrate through read-only audit, exact plan/diff, idempotent file application, local verification, then separately authorized GitHub settings changes. Preserve custom workflows and user edits; refuse ambiguous overwrites. Repo settings, merge, and remote branch deletion need the authority required by the consuming repository.

## First implementation slice

1. Write an accepted baseline v0.1 specification, including mandatory rules, conditional packaging/platform rules, and exception format. Decide whether its source lives inside gz-skills or in an organization baseline; keep one authoritative version.
2. Pilot read-only audit on xplane-health and xplane-fdau. Show evidence and proposed diffs. Include Ortho4XP as a mixed Python/native probe.
3. Build deterministic audit/apply tests with fixture repositories: empty Python, existing Python with custom CI, Go/Windows, mixed Python/native, dirty worktree, conflicting files, and a second apply that makes no changes.
4. Apply and validate in pilots. Confirm a hosted check runs on the submitted head before configuring it as required. Evaluate real C++ work before promoting a C++ test profile.
5. Add recurring finish and branch audit, then migrate other repositories from the proven baseline. Keep release publication separate from ordinary integration.

## Decisions for the next design session

- Does gz-skills itself own the opt-in baseline and its versioned templates, or consume an organization-owned baseline package? Current AGENTS.md and README.md say it does not own project branch policy.
- Which GitHub merge and branch-deletion actions receive standing authorization, and which need a per-PR maintainer decision?
- Which Python coverage, type-check, and package-smoke thresholds are minimum rules versus application or distributable-package rules?
- Which concrete C++ repository establishes testing, compiler, standard, and platform requirements? CTest remains open.
- Do existing repositories migrate in place immediately, or start with audit-only reports until the pilot passes?

This handoff lets the next session choose baseline ownership and write an implementation spec without repeating the repository survey. It changes no skill, CI, branch policy, or GitHub setting.