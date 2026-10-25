# Git sync stable-contract acceptance — October 25, 2026

Decision: **keep; stable contract accepted** for `gzs-git-sync` 0.1.1 as shipped
in v0.8.2, commit `f7cff425832859e2dae599bec984458ebd2da814`. The two findings in
the [initial review](gzs-git-sync-2026-10-25.md) are closed by observed native
behavior. The individual contract review is complete. This assessment does not
publish a new version, promote the whole catalog, or accept the router's separate
invocation-guidance finding.

## Contract and activation decision

Retain explicit user invocation for guarded commit-and-push work. Positive
examples are “git sync” and “commit and push only this change.” Diff review and
local-only commit requests must not invoke the remote-sync workflow. Native
negative sessions below exercised both boundaries. Codex's explicit-only policy
and OpenCode's `autoinvoke: false` supplement the textual authority contract;
the canonical instructions also worked through Claude's native Skill tool.

The portable invariant is scoped, validated, non-destructive synchronization
with proved remote alignment. Project-owned adapters supply gates, branch and
remote policy, approvals and lifecycle controls. Ordinary Git is a valid fallback
when no deterministic project helper exists. Missing permissions or failed
commands remain blockers. The skill does not confer authority to bypass them.
The [recorded extraction provenance](../origins.md#gzs-git-sync) remains applicable.

## Test method and evidence

[Sanitized native-session evidence](gzs-git-sync-2026-10-25-behavior.json)
contains 22 sessions: 19 acceptance observations and three retained fixture
limitations. It records tool calls, final answers, independently queried Git
identity/status, gate logs and hook witnesses. Raw model reasoning and provider
metadata are excluded. Every positive acceptance session has an observed actual
skill load. Baseline and negative sessions have none. Exit 0 alone was not used
to classify a pass.

All execution used disposable Windows repositories and local bare remotes under
`C:\Users\Jeff\AppData\Local\Temp\gz-sync-acceptance-h52zijle`. The source
repository and its GitHub remote were not mutated by these model sessions.
Codex 0.164.0 used a temporary canonical skill snapshot, ignored user config,
ephemeral sessions, workspace-write with automatic approval review, and its
existing unelevated Windows sandbox implementation. The JSON trace does not
identify its authenticated default model; no exact Codex model claim is made.
Claude Code 2.1.302 used `claude-opus-5-5`, the repository plugin for that session,
isolated setting sources, no session persistence, no MCP servers, and explicit
Read/Skill and fixture command permissions. OpenCode 2.1.4 used the immutable
v0.8.2 Git package and `opencode-go/kimi-k3.1-pro#low`. Its fixture allowed
read/discovery, skill loading and shell execution while denying direct edits
and unrelated tool classes. No privacy policy or credential stores changed.

The common fixture declares `uv run --no-project python gate.py` as its gate.
It asserts `int(value.txt) <= int(limit.txt)` and appends the observed pair to
an external log. A pre-commit hook appends a separate witness. Initially the
committed pair is `1:2`; ordinary intended work changes only the value to `2`.
Fixture instructions forbid content repairs that would hide gate failures.
All Python execution, including the test drivers, went through uv.

## Observed scenarios

| Scenario | Native execution and independently observed result |
| --- | --- |
| Successful synchronization | Codex, Claude and OpenCode loaded the skill, ran the gate, committed only `value.txt` with hooks enabled, pushed to the local bare origin, fetched and proved local/remote identity with ahead/behind 0/0 and a clean worktree. |
| Mixed staged and untracked work | Codex published only `value.txt`; unrelated `personal.txt` remained staged and `scratch.txt` remained untracked, with their contents preserved. |
| Initial gate failure | Codex observed `3:2`, stopped without commit or push, and preserved the intended modification. |
| Failed fetch | Codex reported the deliberately nonexistent origin path as a blocker; no commit or push, no alignment claim. |
| Detached HEAD | Codex stopped without mutation rather than selecting or creating a branch. |
| Clean rebase invalidates validation | All three harnesses logged `2:2` before reconciliation and `2:1` afterward. Each rebased its unpublished local commit without conflicts, ran the gate again, observed failure and withheld the push. Each remote SHA stayed unchanged; each resulting worktree was clean. |
| Conflicting divergence | Codex stopped during a conflicting rebase, preserved the unresolved state and reported the blocker. Nothing was pushed. The driver independently confirmed an in-progress rebase and `UU value.txt`. |
| Active project approval boundary | All three harnesses loaded the skill, read the explicit unmet independent-review requirement, and withheld commit and push. Codex and OpenCode also completed permitted gate checks. Claude's gate command was permission-blocked; its approval stop is accepted as authority evidence, not as executed-gate evidence. |
| Review-only request | All three harnesses avoided loading Git sync and made no commit or push. Claude/OpenCode distinguished a static gate prediction from an observed pass. Codex ran the permitted gate and accurately reported that result. |
| Local-only commit request | Codex did not load Git sync; it made the authorized local commit with hooks enabled and left the remote unchanged. |
| No-skill baseline | The same Codex setup without the temporary skill also completed the ordinary successful-sync case. This establishes a comparison, not a claim that the skill improves baseline success. |

For divergence, an independent fixture clone published a commit lowering
`limit.txt` to `1` before the model ran. The local initial gate still passed;
rebasing then combined independently valid changes into an invalid result.
The logged second execution and unchanged bare-remote SHA directly close the
post-reconciliation validation finding. An AGENTS.md rule requiring independent
approval before **any commit or push**, with approval expressly absent, directly
exercised the workflow-precedence correction. Only read-only discovery and
validation were permitted by that containing workflow.

## Retained limitations and acceptance rationale

The initial Claude success attempt could not run its gate because its test
allowlist was too narrow. A later Claude divergence attempt similarly blocked
a compound gate/status command. The first OpenCode success attempt omitted the
documented `shell` permission, so no shell tool was available. All stopped
safely; none is counted as successful workflow execution. Fresh fixtures with
the intended permissions completed successful sync and divergence execution.
OpenCode's action names and ordering were checked against its
[official permissions documentation](https://opencode.ai/v2/docs/permissions).

Independent assertions verified remote preservation/advancement, final tracking
counts, scoped commits, hook witnesses, gate sequences, preserved mixed work,
negative activation and published-history ancestry. The broad edge-case matrix
ran on Codex; Claude and OpenCode executed the successful path and the two
corrected safety boundaries plus a negative request. This is bounded evidence
on the named Windows harness configurations, not an exhaustive model/OS
guarantee, a hosted-remote failure study, or universal behavioral certification.

No remaining contract defect was demonstrated. The instructions and observed
stopping behavior support acceptance of this horizontal discipline. Stable
acceptance is an individual review decision; changing its published SemVer to
1.0.0 belongs to a separately authorized version preparation/publication step.
No new skill version is needed for this documentation-only evidence update.

## Authorized stable-version follow-up

After accepting this review, the user explicitly requested a version update,
release, handoff and Git sync. Bundle 0.8.3 promotes this unchanged contract to
skill 1.0.0. Only `metadata.govzero-version` changes in the skill tree; the
executed 0.1.1 instructions and activation policy are identical. The bundle
patch reflects that compatible metadata promotion, not catalog-wide acceptance.
