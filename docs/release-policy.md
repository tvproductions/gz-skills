# gz-skills release policy binding

## Authority

The operator designated
[gz-skills-first-starter](https://github.com/tvproductions/gz-skills-first-starter)
as the authoritative shared engineering and release policy alignment source.
Its [versioning policy](https://github.com/tvproductions/gz-skills-first-starter/blob/main/docs/versioning.md)
owns SemVer classification, 0.x treatment, coherent minor-release bundles,
compatible patches, newly written PRDs for every major including 1.0.0,
independent component versions and immutable release identities.
This document binds that source to this repository; it is not a competing policy.

Apply the rules prospectively to the bundle and each independently versioned
skill. A new coordinated PRD may cover explicitly identified component majors;
it must contain newly written requirements for each. Keep the individual
stable-contract and catalog reviews as additional gates. The already published
gzs-git-sync 1.0.0 and its historical acceptance are not retroactively changed.
[Packaging](packaging.md#release-governance) owns this project's release channels,
manifest synchronization, artifacts, installation checks and publication sequence.

The source's engineering guidance must be checked for applicability during
scoped maintenance. This release-policy alignment does not certify broader
Python/tooling conformance or authorize dependency/runtime changes.
Local departures require evidence, maintainer approval, an owner and dated revisit.

## Check in with the source

Before release preparation, during scoped policy/tooling maintenance, and when
notified of relevant starter changes:

1. Read the canonical starter's current versioning policy, changelog and relevant
   baseline/engineering guidance. Resolve and record the exact source revision;
   distinguish published release policy from unreleased development guidance.
2. Compare with the previous reviewed source and this repository's instructions,
   release documents and applicable acceptance evidence. Record the date, paths,
   source SHA, applicability, differences and adopt/defer decisions in the
   existing release or handoff record.
3. Reconcile applicable differences before claiming consistency. An unavailable
   source or unresolved difference remains an explicit gap. Record approved
   exceptions with evidence, owner and dated revisit; local silence is no waiver.
4. Recheck final source identity before a published-alignment claim. For an
   operator-authorized working-tree review, record the base SHA plus content
   hashes, and identify the edits as uncommitted/unreleased.

This is an on-demand responsibility, not an automatic schedule or an automatic
update. Independent versions and release dates remain independent.

## Workflow boundary

[Backplane owns lite/heavy definitions](https://github.com/tvproductions/superpowers-backplane/blob/main/docs/superpowers-backplane/modes.md),
requirements tracking, labeling, backlog/release monitoring and handoffs.
Superpowers owns feature development. gz-skills provides portable procedures,
including release preparation/publication verification and handoff primitives,
beneath the active project workflow; it does not become the lifecycle owner.

Do not bootstrap the starter bundle into either companion repository. Policy
flows from the starter to repository bindings; workflow ownership does not
create a reverse policy dependency. Shipped skills remain usable by unrelated
projects under those projects' own policy. No blanket consumer PRD, Python,
tooling or installation requirement follows from this repository's alignment.

## Initial local review — October 26, 2026

The reviewed starter is development version 0.7.0, with base commit
`eef2e858bba709988eb859b17739d2989d8825ab` plus the operator-authorized
working-tree policy changes. The base commit alone does not contain this binding.
Source inputs: `docs/versioning.md`, `docs/baseline-policy.md`,
`docs/architecture.md`, `templates/AGENTS.skills-first.md` and `CHANGELOG.md`.
The exact edited input hashes are recorded below.

Adopted: source authority, SemVer/release planning and prospective major PRDs,
source consistency checks, and Backplane ownership of modes/product continuity.
No release-policy exception is taken. Broader engineering conformance, end-to-end
mode readiness, remote publication and installed discovery are not established
by this documentation review. Reconcile the final committed source before the
next release preparation. No shipped skill, version pin, tag or release is changed.

| Source path | SHA-256 of reviewed working-tree content |
| --- | --- |
| docs/versioning.md | d2a293779e80811c08f1311c8bf54961abe9f1638967ed6a71b3babe4a0d54eb |
| docs/baseline-policy.md | fcb2ae18dc19f80043709286270ea200bc17721b89a5e484c9e24f255738b660 |
| docs/architecture.md | 645a929b00bbfaaf0f7ef4e188e936e44682f1989ddccb21228374ce824663b0 |
| templates/AGENTS.skills-first.md | 4cd3bf70359a5e888a317a28232be86cf0233af423f5bc413a426fdcffa86322 |
| CHANGELOG.md | 515f78f591d2326205619da9352e45f02002593f8c2208729c29bfd71ff4d8b0 |

## Committed source reconciliation — October 26, 2026

The operator authorized Git synchronization of all three repositories. The
reviewed source policy is now committed and verified on the starter's remote main
at [`35ac0578dab0c7b603a9545d9b6b630ee006e551`](https://github.com/tvproductions/gz-skills-first-starter/commit/35ac0578dab0c7b603a9545d9b6b630ee006e551).
The five policy inputs above retain their recorded hashes in that commit;
the initial working-tree review is reconciled to this immutable source identity.
Development version 0.7.0 remains unreleased. This record verifies source-policy
alignment; release acceptance, installation and native readiness remain separate.
