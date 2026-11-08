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

### Astral/uv alignment clarification — November 8, 2026

The maintainer explicitly reaffirmed a strict Astral/uv alignment preference for
gz-skills, consistent with gz-skills-first-starter. Rechecked canonical source
main at `a483e382146c6082e590e31494c07d1812645014`, unchanged from the 0.10.0
review, and read `docs/engineering/astral-alignment.md` at that revision. Its
pure-Python backend choice is `uv_build`; another backend requires a concrete
need and verified package behavior. Adopt that preference for this repository
and track the existing Hatchling backend as migration debt in the
[roadmap](roadmap.md#uv_build-migration-acceptance). No current incompatibility
or approved permanent backend exception has been established.

Record any justified departure with evidence, maintainer approval, an owner and
a dated revisit. Prior releases' bounded-scope deferrals remain historical;
they do not establish continuing alignment. This clarification does not certify
full conformance, formally adopt the starter, change a published release, or
authorize a backend migration or new consumer requirement by itself.

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

## Python authority correction — November 7, 2026

The maintainer explicitly authorized cross-repository alignment and reaffirmed
current policy: 3.14 for ordinary projects, 3.12 for X-Plane/XPPython3-bound code.
Reviewed starter source is `4f8bb09633655473cd6aab9e1ddc60963c487bb1`, including
baseline, Python engineering, versioning, mapping, AGENTS and changelog. This
adds the previously missing explicit runtime binding for this repository; the
earlier release-governance-only scope is historical, not current permission
to retain an unexplained 3.13 development baseline.

This ordinary Python repository selects managed 3.14.10 and declares the 3.14
family. uv uses the source's minimum-only compatibility rule. The portable setup
and update workflows instead read each consuming project's governing source;
they maintain no competing family, analyzer assortment or package restrictions.
Starter-governed projects follow their reviewed starter baseline. Unrelated
consumers preserve their own approved policies, and an absent/unavailable
source leaves dependent choices unresolved. No circular adoption, blanket
consumer runtime mandate, plugin installation or full conformance claim follows.

The [correction receipt](evidence/2026-11-07-python-policy-alignment.md) records
baseline failure cases, migration/version classification and scoped proof.
This working-tree correction is unpublished; recheck committed source identities
and applicable candidate evidence before any release-alignment claim.

## Committed authority reconciliation for authorized sync

The maintainer subsequently authorized ordinary Git synchronization of this
correction. The reviewed starter authority is now committed and verified on
origin/main at `a483e382146c6082e590e31494c07d1812645014`. This reconciles the earlier working-tree review to an
immutable source; its runtime/ownership declarations are unchanged from the
accepted correction. Preserve published 0.8.3 refs and installed copies. This
candidate remains unreleased; no tag or plugin propagation is authorized.
Local tests, schema/resource and isolated-artifact results above remain the
applicable scope. This repository has no configured quality CI; report remote
arrival separately from unavailable exact-commit hosted quality evidence.

## Release planning and version advancement

PRDs guide major releases; selected work and requirements drive minor releases;
fixes drive patch releases. Follow the canonical starter policy at
https://github.com/tvproductions/gz-skills-first-starter/blob/main/docs/versioning.md#plan-releases-from-their-governing-work
and this project binding. Every major, including 1.0.0, requires a newly written
PRD defining that major's outcomes, requirements and acceptance criteria.

Before implementation planning, identify the release scope served by the work.
Keep a current release-scope record in this project's existing backlog, roadmap
or release authority: actual last published version/tag/revision (or evidence of
no prior release), proposed next version, governing PRD/requirements/fixes,
included completed and remaining work, deferred work, compatibility impact and
acceptance gates. Reconcile completed changes into that record before closeout.
Missing scope/version evidence blocks release-preparation acceptance. Do not
silently shrink approved scope or include the entire future backlog in one release.

Apply SemVer to the complete selected scope since the published baseline.
After 1.0, incompatible contracts require major, compatible requirements/capability
or public deprecations require minor, and compatible fixes require patch. During
0.x, requirements/capability and incompatible changes require minor; compatible
fixes require patch. Multiple tasks in one release share its pending version.
An initial unpublished 0.1.0 may cover an explicitly selected first-release scope;
review scope growth instead of using unpublished status to avoid release accounting.
Keep metadata/runtime mirrors, affected lock metadata and changelog aligned when
the pending version is selected. Preserve published versions/tags, independent
product/template/plugin versions and existing release gates. These instructions
do not authorize publication or enable deferred Backplane.

### Required version decision checks

At requirements intake, planning and closeout, agents MUST derive the pending
target from the actual published baseline and the complete pending scope.
Identify the new major PRD, selected minor requirements or commitment corrected
by a patch. A ticket labeled fix cannot turn new requirements into patch work.
Use the highest required increment and reset lower components: 1.4.2 becomes
1.4.3 for fixes, 1.5.0 for compatible requirements, or 2.0.0 for a breaking
major guided by a newly written PRD. During 0.x, requirements drive 0.4.2 to
0.5.0; compatible fixes drive 0.4.3. Reuse an adequate pending target rather
than incrementing once per task. Reconcile version mirrors and changelog in
the same authorized change; do not ask the maintainer to choose routine numbers.

Require a finite release outcome, included requirements, exclusions and an
acceptance gate, including for the initial 0.1.0. Assign future requirements
to later minor bundles. Preserve approved scope; ask only for unresolved
product decisions. Missing required PRD, scope or consistent version evidence
blocks the applicable planning and closeout claims as well as release preparation.
Report published baseline -> pending target, governing source, compatibility,
version agreement, completed/remaining/deferred work and publication status.
A selected target does not assert readiness or authorize publication. Use the
canonical policy's required-version-decision-procedure; keep the record in
existing project authorities rather than creating another tracker.

### November 1, 2026 local release-accounting review

Published baseline is v0.8.3, commit d6acc26e28ca1c4f43e5bb46d8973021d7d006c3.
Pending repository-policy clarifications modify no shipped skill tree and do not
independently require a skill bump. Select the next bundle scope in the existing
changelog/release authority before assigning its version. Preserve per-skill
classification and catalog/individual acceptance gates; a changed skill and its
containing bundle remain independently classified.

Reviewed source: starter base commit
`8d090f88bf45b9a755808a62c1445beeb005daff` plus the authorized, uncommitted
0.8.1 clarification. This is development guidance, not a published template
upgrade. Reviewed `docs/versioning.md` SHA-256:
`960cc4052cb87696980be23a393553079f254ac8105240dbcbac5244a52c4460`;
`templates/AGENTS.skills-first.md` SHA-256:
`0383bc3330756600b2d9e0ae2393af0143836b7e6bc3b5b8d407e39f361b51b4`.
No adoption lock, component pin, plugin activation or product version is changed.
