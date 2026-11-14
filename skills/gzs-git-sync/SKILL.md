---
name: gzs-git-sync
description: Create and publish a guarded Git save point after reviewing scope and passing the repository's own quality gates. Use only when the user explicitly asks to git sync, commit and push, publish the current work, or create a remote save point.
compatibility: Requires Git, a configured repository remote, and permission to commit and push.
metadata:
  govzero-version: "1.1.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Git Sync

Own the complete save-point ritual: review the work, validate it through the
repository's declared gates, commit the intended unit, reconcile safely with the
remote, push, and prove local and remote are aligned.

The user's explicit invocation authorizes the ordinary commit and push steps for
the current repository. It does not authorize destructive history changes,
unrelated cleanup, or bypassing repository safeguards.

When a project-owned workflow is active, perform this save point within its
scope, sequencing, approvals, locks, gates, and evidence requirements. That
workflow retains lifecycle authority; explicit invocation does not waive its
controls. Do not duplicate its state or declare the containing workflow complete.

## Workflow

1. Read the repository's applicable agent guidance and inspect the current
   branch, remote tracking branch, complete worktree status, staged diff, and
   unstaged diff. Completion means every changed path is understood.
2. Decide whether the changed paths form one truthful save point. Preserve
   unrelated user work. If the tree contains changes that cannot truthfully ship
   together and the intended subset cannot be established from context, stop
   and name the boundary.
3. Discover the repository's canonical sync command per the order in
   § Discovery and fallback. Do not substitute remembered commands for
   documented ones. Resolve gate applicability from the project stage and
   actual tree as described in § Stage-aware verification. Check version changes
   and release authority as described in § Release follow-through.
4. Preview mutations when the selected adapter supports a dry run. Fetch current
   remote state before trusting ahead/behind counts. Completion means the plan
   identifies the branch, remote, changed-file scope, validation, commit, remote
   reconciliation, and push.
5. Run every quality gate required for the changed scope. Keep commit hooks
   enabled. Diagnose a zero-test result before classifying it as a failed
   behavioral gate. Fix an in-scope failure or authorized applicability mismatch
   and rerun its owning gate; stop on a failure that cannot be resolved within
   the requested work.
6. Stage only the intended save point and inspect the staged diff. Compose a
   concise commit message that describes the whole staged unit. Do not commit an
   empty or misleading unit.
7. Commit, fetch, and reconcile without rewriting published history. Use a
   fast-forward when available. Rebase only unpublished local commits when the
   repository permits it. Stop on conflicts or ambiguous divergence. If
   reconciliation changes the validated content, rerun every applicable quality
   gate on the resulting tree before pushing, even when reconciliation had no
   conflicts. Correct an in-scope failure and rerun its owning gate; otherwise
   stop. Completion means the tree to be pushed has passed its required gates.
8. Push the current branch to its configured remote. When the remote branch does
   not exist, create it with upstream tracking if repository policy permits.
9. Fetch once more and verify the final state. Completion requires the intended
   commit to exist locally and remotely, `ahead=0`, `behind=0`, and no unintended
   staged or unstaged changes.

## Discovery and fallback

Treat the portable skill as the invariant and the project surface as the
adapter. Prefer, in order:

1. A repo-local `gzs-git-sync` or `git-sync` skill with a deterministic helper.
2. A documented project sync command.
3. The repository's documented quality commands followed by ordinary Git.

The third rung is the floor, and it always exists: any repository with a remote
can be synced with Git alone. A project surface above it is enrichment, never a
prerequisite, so this workflow never degrades into having nothing to run.

## Stage-aware verification

Planning, research, documentation and instruction repositories are valid save
points before runtime implementation exists. A configured test runner does not
by itself make behavioral tests applicable. Inspect the governing project stage,
the complete tree (including scripts and untracked files), existing test assets,
discovery configuration, hooks and CI. A documentation-only diff does not excuse
required tests for an existing implementation or executable tooling.

Where project policy permits it and there is no implemented behavior or test
suite to exercise, record behavioral testing as **not applicable: pre-implementation**
with the inspected scope and reason. Run the checks applicable to the actual
artifacts, such as configured document/link checks, configuration validation,
skill-contract checks and whitespace checks. Do not invent a test requirement,
write placeholder tests or claim a passing test suite to save planning work.

Zero discovered tests require diagnosis, regardless of the runner's exit code.
If tests or implementation exist, investigate discovery paths, naming, imports,
environment and missing coverage; an empty discovery result is not evidence of
inapplicability. Inspect the actual command and output rather than assuming what
a numeric status means across tools or versions.

If an unconditional bootstrap hook contradicts the project's permitted
pre-implementation scope, identify the owning gate as a configuration mismatch.
When repairing that mismatch is authorized, correct its project-owned command,
hook, CI and guidance together as applicable. The condition must report why
tests are inapplicable and automatically require real tests when implementation,
executable tooling or test assets appear; a permanent allow-empty switch or
manual phase label alone is insufficient. Rerun the complete canonical gate
with hooks enabled before committing. Preserve required thresholds and genuine
test/discovery failures; do not use hook skips or blanket exit-code suppression.

An ordinary sync request does not authorize changing an explicit project test
requirement. If policy requires tests unconditionally or forbids gate edits,
name that precise conflict and the smallest policy/configuration correction
needed. A request to correct this mismatch permits the bounded repair where
project authority allows it; complete that repair instead of repeatedly rerunning
the same empty suite. No portable skill waives an active project approval rule.

## Release follow-through

Check the intended scope for unpublished package or independently versioned
component versions, including already committed pending changes rather than
only the current diff. Compare them with the last published release. Check the
project's changelog, release policy and remote publication evidence; a version
string or pushed commit alone does not
establish a release. Resolve unavailable evidence as unknown.

If the user's request, established instructions or explicit project policy also
authorizes publication, continue through the owning release workflow and its
gates. Use `gzs-release` when available and appropriate, or the project's documented
release procedure. Preserve the release owner's sequencing, including preparation
before the save-point commit when required. Complete and verify the authorized
publication instead of ending with an offer to release. Do not duplicate release
mechanics or lifecycle state in this skill.

A version increment alone grants no publication authority. Honor an explicit
prepare-only, no-release or deferred-release instruction. When publication is
outside the established authority, complete the authorized Git save point and
report the pending version and remaining publication step. When an authorized
release is blocked or partial, name the completed effects and blocker; Git
alignment does not establish release completion. A sync with no pending version
change does not require inventing a release.

## Safety invariants

- Preserve published history: no force push or destructive reset.
- Preserve hooks and gates: no `--no-verify` or equivalent bypass.
- Preserve user work: no automatic clean, stash deletion, branch deletion, or
  unrelated file edits.
- Treat failed fetches, unresolved conflicts, detached HEAD, and unexplained
  divergence as blockers.
- Never claim synchronization from a successful push alone; prove final remote
  alignment.

## Evidence

Report the branch, remote, changed-file scope, validation commands and results,
commit SHA and message, reconciliation performed, push result, and final
ahead/behind and worktree state. Identify validation performed after any
content-changing reconciliation. Distinguish passed checks, justified
inapplicable dimensions and unresolved failures; include the project authority
and evidence for each applicability decision or gate repair. Name any skipped
gate or unresolved warning. For changed versions, report the last published and
pending versions, publication authority or explicit deferral, and the owning
release workflow's verified result or remaining publication step.
