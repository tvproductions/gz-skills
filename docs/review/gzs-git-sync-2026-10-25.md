# Git sync contract review — October 25, 2026

Reviewed released `gzs-git-sync` 0.1.0 in bundle 0.8.1. Outcome: **revise**;
stable-contract acceptance remains pending. This review does not invoke git sync
or authorize changes to the skill, commits, pushes or releases.

## Findings

1. **High: reconciliation can invalidate the gate before push.** Workflow step 5
   validates the current tree; step 7 then permits fast-forward or rebase; step 8
   pushes without requiring validation of the resulting tree. This fails the
   declared goal of publishing a save point that passed repository gates.
   A disposable local Git fixture reproduced the gap: base `value=1, limit=2`;
   upstream independently changes `limit=1`; unpublished local work changes
   `value=2`. The gate `value <= limit` passed before reconciliation (exit 0),
   the rebase completed without conflicts, and the same gate failed afterward
   (exit 1), with a clean worktree. No external remote was used. Fixture:
   `C:\Users\Jeff\AppData\Local\Temp\gz-sync-review-l06_9q18`.
   Correction route: workflow steps 5–8 must require applicable gates on the
   reconciled tree before push whenever reconciliation changes validated content.
   Stop or correct within scope when that validation fails.
2. **Medium: project-orchestrator precedence is not explicit.** The opening says
   to own the complete ritual and treats explicit invocation as commit/push
   authority. Discovery delegates to project commands, but no instruction yields
   sequencing, approval, locks or receipts to an active containing workflow.
   Repository AGENTS.md and the roadmap's shared architecture require that
   precedence. A project with a required independent approval between validation
   and publication has no explicit stopping instruction here. This is a contract
   omission, not an observed unauthorized push. Correction route: state that the
   primitive runs within the active project's authority and does not bypass or
   duplicate its lifecycle controls.

## Interface and portable boundary

Keep the skill as an explicitly user-invoked remote-save-point primitive.
Positive triggers: “git sync”, “commit and push this work”, “create a remote
save point”. Negative triggers: “review this diff”, “run tests”, “commit locally
only”, or “is my branch current?” None authorizes a push merely by mentioning Git.
Codex metadata sets `allow_implicit_invocation: false`; the native OpenCode
adapter test checks the same explicit-only boundary. Other hosts must retain
the textual authorization boundary even when they ignore that metadata.

Project-independent invariants: scoped staging, preserved user work and published
history, enabled hooks, successful gates, safe reconciliation and proved final
alignment. Adopters own commands, branch/upstream policy, approvals and gates.
The fallback to ordinary Git supplies a mechanism, not missing credentials,
permission or absent project validation evidence.

## Evidence and remaining behavioral work

The bounded sample is the next queued skill, selected for remote-mutation risk.
Intent sources were fixed from AGENTS.md, the roadmap shared architecture and
the skill's declared guarded-save-point goal before running the Git fixture.
The fixture exercised real Git commits and rebase in a temporary repository,
not a live agent following the skill. Its first sandboxed attempt could not
create `.git`; the isolated rerun succeeded with sandbox escalation.

Static inspection supports the explicit activation, discovery, preservation,
conflict-stop and final-evidence requirements. It does not establish reliable
model behavior. No fresh no-skill/with-skill inference comparison was run, and
no stable promotion is claimed.

Before acceptance, compare baseline and loaded-skill responses using disposable
repositories for: mixed staged/untracked scope; gate failure; failed fetch;
detached HEAD; clean divergence that breaks a semantic gate; conflicting
divergence; active project approval boundary; and successful synchronization to
a local bare remote. Record actual loaded skill/tool calls, final local/remote
commit identity, ahead/behind, preserved unrelated work and any stopping action.
Include negative requests that must not commit or push. Simulation alone must
not be reported as execution evidence.

## Authorized correction follow-up

The user subsequently authorized both corrections. Candidate skill 0.1.1 in
pending bundle 0.8.2 now explicitly yields lifecycle authority to an active
project workflow and requires applicable gates on content changed by
reconciliation before push. Its evidence section requires reporting that
validation. These are compatible corrections to existing preservation and
validation intent, not a new publication authority or stable-contract promotion.

Next action: collect the behavioral evidence above before deciding stable
acceptance. The Git fixture establishes why revalidation is required; it does
not prove a model follows the corrected instructions. No commit or publication
is part of this correction request.

Correction validation: all 28 unittests and all 20 Agent Skills specification
validations pass; offline lock consistency and Claude marketplace validation
pass. Wheel and sdist build successfully, and every packaged canonical skill
file matches the working-tree source byte-for-byte. `git diff --check` passes.
These checks establish structural and packaging integrity, not native model
compliance with the corrected workflow.
