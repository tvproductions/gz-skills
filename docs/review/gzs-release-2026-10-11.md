# Release primitive review — October 11, 2026

Candidate: `gzs-release` 0.1.0 in pending bundle 0.8.0. Keep as an
explicitly invoked portable release primitive; stable-contract review remains
pending. Source implementation is not publication or native host discovery.

## Interface and boundaries

Positive requests: recommend a patch/minor/major, prepare a release candidate,
or publish and verify a named release. Negative triggers: ordinary commit/push,
dependency maintenance without a release request, deployments and consumer
migration. Bare invocation recommends only. Codex and OpenCode disable implicit
activation; other harnesses rely on the activation/authority instructions.

The invariant is an evidence-backed version decision and completion of the
requested boundary, with immutable published identity and verified remote
results. Consumers own version policy (including 0.x), commands, approvals,
channels and lifecycle. The primitive yields to an active SP-BP/gzkit workflow.
No language, Python baseline, hosting vendor or package registry is selected.

## Independent forward scenarios

A separate evaluator read the implemented skill with invented evidence and
simulated five user requests without modifying files or publishing anything:

| Scenario | Observed decision |
| --- | --- |
| Bare invocation; stable 1.4.0; bug fix plus compatible CLI command | Read-only 1.5.0 recommendation covering all changes since release, subject to project policy |
| Commit/push a prepared release with no published tag/record | Synchronize authorized work; ask a focused publication clarification and report publication outstanding |
| Publish 2.1.0; matching remote tag; draft missing an asset | Verify identity, complete missing asset/publication steps, preserve the tag, verify required channels |
| Publish latest; several pending note sections; project orchestrator owns approvals | Select evidenced current candidate, avoid creating every pending version, preserve required approval boundary |
| User chooses patch where policy suggests minor | Honor the choice without tag reuse/decrement, record policy exception and impact, retain mode authority |

No demonstrated workflow defect was found. These are read-only simulated
behavioral results, not live publishing or multi-host execution proof. Before
this addition the catalog routed remote save points to `gzs-git-sync`; it had no
release/version recommendation primitive. The new route distinguishes those
outcomes rather than claiming a baseline agent cannot perform releases.

## Validation status

All twenty canonical skills passed the documented Agent Skills specification
validator. The older skill-creator quick validator rejects the canonical
`compatibility` field used throughout this repository, so it is not a valid
specification gate here; retain compatibility metadata and use the repository's
validator. Its initial missing PyYAML was resolved through a temporary tool
environment without changing project dependencies.

The first unittest run exposed an LF-only OpenCode title assertion after two
newly written skill files used Windows CRLF. Adapter inspection identified those
prefixes directly. The assertion now accepts both normal line endings while
still requiring the canonical GovZero heading; source content preservation and
explicit-only activation remain independently checked.

All 28 unittest cases pass on Python 3.13.15, as does offline lock consistency.
Claude strict plugin/marketplace validation passes. Wheel/sdist contain all twenty
skills; new release/router wheel bodies match source and explicit-only metadata
is packaged. Codex native loading remains unverified. Final results are recorded
in the Unreleased changelog. Tagged installations, remote release
operations and fresh-session discovery remain unverified. No consumer pins or
installed caches changed.
