---
name: gzs-repository-hygiene
description: Audit and, when requested, repair repository hygiene across workspace state, generated artifacts, packaging boundaries, lockfiles, caches, and control-surface drift. Use for maintenance, cleanup, tidy, repository-health, or generated-artifact verification requests; use project-owned hygiene commands when present.
compatibility: Requires Git and any hygiene or build tools declared by the target repository.
metadata:
  govzero-version: "0.1.1"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Repository Hygiene

Inspect the repository as a delivered system, not only as source code. Hygiene
finds drift between authored inputs, generated surfaces, build outputs, package
contents, and version-control state.

## Discovery and fallback

Prefer, in order:

1. A project-owned hygiene script in check or dry-run mode.
2. The repository's documented maintenance commands for the categories it
   declares.
3. Read-only inspection with the version control system itself: tracked and
   untracked inventory, ignored-file status, and a dry-run clean that reports
   without deleting, alongside a direct read of the manifest and lockfile.

The third rung is the floor and needs nothing but the repository. It can
establish drift; it cannot repair. Keep it read-only, and never treat an
untracked path as safe to delete on its evidence alone.

## Workflow

1. Read repository guidance and inspect branch, worktree, staged and unstaged
   diffs, ignored files relevant to the task, and existing maintenance scripts.
2. Discover the canonical hygiene command. Prefer a project-owned deterministic
   script in check or dry-run mode. Read what it checks before adding ad-hoc
   commands around it.
3. Inventory evidenced hygiene surfaces:

   - manifest and lock consistency;
   - generated files and mirrored control surfaces;
   - build and package contents versus declared runtime boundaries;
   - documentation and link integrity;
   - stale temporary output, caches, or untracked generated artifacts;
   - executable hooks, configuration references, and repository metadata.

   Keep categories absent from the repository out of the run.
4. Run read-only checks first. Classify each finding as drift, expected generated
   state, intentional local state, or unknown. Never equate “untracked” with
   “safe to delete.”
5. Apply repairs only when the user requested cleanup or the repository's
   documented hygiene workflow makes that mutation part of the requested task.
   Prefer regeneration and recoverable moves. Preserve user-authored work.
6. Inspect actual built or packaged artifacts when the change can affect them;
   source-tree inspection alone does not prove the delivery boundary.
7. Rerun the complete hygiene check and the repository quality gate on the
   unchanged final tree.

## Evidence

Report checks performed, findings and classifications, files regenerated or
removed, artifact-boundary results, validation exit codes, skipped checks, and
final Git state. If anything material was removed, state whether it is
recoverable.
