---
name: gzs-release
description: Recommend a release version, prepare a release candidate, or publish and verify an authorized release under project policy. Use only when explicitly asked for release management or version-bump advice; ordinary commit/push requests belong to gzs-git-sync.
compatibility: Requires repository history and project release policy; publication also requires the selected host or registry tools and credentials.
metadata:
  govzero-version: "0.1.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Release

Carry a release from an evidence-backed version decision through the requested
completion boundary. The consumer owns its versioning policy, gates, release
channels and lifecycle. Follow an active project workflow, including Backplane
or gzkit, rather than creating parallel release state or bypassing its approvals.

## Establish mode and authority

- **Recommend:** Inspect changes and suggest a version with reasons. Version
  advice or a bare skill invocation is read-only; do not edit metadata or publish.
- **Prepare:** An explicit preparation request authorizes the scoped metadata,
  owning-tool lock refresh, changelog and verification work. Commit/push only
  when the request or existing workflow authorizes it. Stop at a concrete,
  reviewable candidate when publication authority is absent.
- **Publish:** An explicit request to publish a release authorizes preparation
  plus the ordinary release commits, pushes, immutable tag and declared release
  channel operations needed to complete that release. Execute the authorized
  workflow without asking again for authority already established.

Commit/push alone does not publish a release. If wording combines these goals
ambiguously, prepare the candidate first and ask one focused clarification about
publication; do not silently publish or describe Git synchronization as a release.
When the target version or channel is ambiguous, resolve it from project evidence
or request the missing choice before that mutation. Do not create every historical
unreleased version merely because several changelog sections exist.

## Discovery and fallback

Prefer, in order:

1. The active project-owned release skill or orchestrator with its documented
   helper and state contract. This remains the owner of lifecycle transitions.
2. The project's documented release command, configuration and policy.
3. Inspect manifests, release history and tags, then use the owning package tools,
   ordinary Git and the declared publication host's supported API or CLI.

The third rung works without a special release helper. Do not assume a language,
branch, host, tag prefix or package registry. With no declared version policy,
recommend a stated SemVer-based convention rather than silently establishing
one. Missing history, credentials or a required approval is an explicit gap,
not permission to fabricate a release or bypass the owning workflow.

## Recommend the version

1. Inspect agent instructions, complete worktree status, branch/tracking state,
   release policy, manifests, changelog and the relevant component's published
   releases. Resolve its last released tag to a commit; distinguish published
   releases, prereleases, pending versions and unrelated component tags. Fetch
   authoritative remote evidence before claiming current publication state.
2. Compare the intended candidate with that release, including all changes since
   it, not just the latest commit. Separate public behavior/contract changes,
   policy requirements, dependency pins and internal corrections. Review actual
   compatibility evidence; an upstream major does not automatically determine
   the consuming project's bump.
3. Apply the project's policy, including its 0.x and prerelease rules. Under
   stable SemVer, incompatible public contracts imply major, compatible new
   capability minor, and compatible fixes patch. Do not invent a universal 0.x
   rule. Independent components may require separate version decisions.
4. Report base release/SHA, proposed version, classification, reasons, consumer
   impact and unresolved compatibility evidence. The highest applicable change
   since release determines the recommendation. Honor an explicit user version
   choice, recording a policy exception and its impact when appropriate; never
   reuse or decrement a published version. Required project approvals still apply.

## Prepare the candidate

Review the intended file set and preserve unrelated work. Discover every owning
version surface, lock generator and release-note requirement; synchronize only
the intended component. Regenerate locks with their owning tools, preserving
unrelated dependency pins. Document compatibility/migration, policy changes
versus pin refreshes, verification and remaining limitations.

Run the project's complete release gates and inspect generated/package contents
when required. Retain hooks and numeric thresholds. Use prior evidence only when
it still covers the exact source and required environment. Validate final
release metadata too; source changes after validation require affected checks
again. Do not claim native loading, installation or compatibility from a manifest
check alone.

Report the candidate version, source identity, changed scope, notes and checks.
If publication is not authorized, leave the project-prescribed pending status
and identify that publication remains outstanding. Do not ask to approve an
unprepared plan in place of making the authorized result reviewable.

## Publish and verify

1. Inventory remote tags, release records and required registry versions before
   creation. If the intended release already exists, verify its identity and
   contents and report it; do not recreate it or move its tag. A same-name tag
   pointing elsewhere or ambiguous partial publication stops mutation for review.
2. Follow the owning release sequence for finalized notes, mirrored versions,
   required approvals and CI, release commit, artifacts and checksums. Resolve
   remote divergence without rewriting published history. If reconciliation
   changes the source, rerun affected release gates. Build required artifacts
   from the final candidate source and confirm no unintended source changes.
3. Tag exactly the validated release commit using the project's tag convention
   and signing/annotation policy. Push the commit and tag to the intended remote
   in the project-required order. Publish the declared release record and required
   assets or packages with notes identifying the source and known limitations.
   Do not add registry uploads, deployments or consumer migrations to a Git-host
   release unless they belong to the authorized project release contract.
4. Query the remote: resolve the tag to the intended full commit, verify release
   version, published/draft/prerelease status and required artifacts/checksums.
   Complete the project's tagged-install or channel acceptance checks. Check CI
   for the exact release commit when required; queued or failed CI is not success.
5. Verify the intended branch's remote alignment and worktree scope. Report each
   channel separately. A pushed commit, a local tag or a draft release does not
   establish publication. Installation does not prove fresh-session discovery.

If publication fails partway, report completed effects and the precise remaining
step. Preserve tags and artifacts. Retry only incomplete operations after checking
that existing identities match; no force pushes, tag replacement, automatic
rollback or unrelated release deletion. Stop on a conflict or missing authority.

## Completion evidence

State the requested mode and achieved boundary, base/proposed/published version,
reason or explicit override, candidate/release SHA, validation and exact-commit CI,
commit/push/tag results, release URL/status, required artifact and channel results,
and final remote/worktree state. Name unresolved or unverified steps. Report
"prepared" when publication is outstanding, "partially published" when only some
required channels completed, and "published and verified" only after the owning
contract is satisfied. Version strings are not publication evidence.
