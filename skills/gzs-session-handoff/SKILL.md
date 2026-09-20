---
name: gzs-session-handoff
description: Create or resume a durable engineering-session handoff that preserves state, decisions, evidence, and next actions without duplicating existing artifacts. Use when the user explicitly asks to hand off, checkpoint, resume, or preserve work for another session or agent.
compatibility: Designed for Git repositories that can store or reference a Markdown handoff; adapt GitHub issue and PR checks when another tracker is used.
metadata:
  govzero-version: "1.0.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Session Handoff

A handoff is an evidence-backed continuity artifact. It records where to resume;
the artifact itself does not authorize an action.

## Create

1. Discover the repository's handoff command, template, and canonical storage
   location. Follow the active project workflow when one owns handoff. Otherwise
   use the user's requested location or a predictable Markdown path in the
   repository without replacing unrelated content. If no repository file is
   appropriate, use a user-designated durable location or put the complete
   handoff in the response. State where it is available; never leave a
   temporary file as its only copy.
2. Capture observed state before summarizing: observation time, Git branch,
   HEAD, worktree, verification already run, active plan or work item, and
   material artifact paths. Mark local-only state so a successor does not assume
   it is available in another workspace.
3. Reference existing specs, plans, GitHub issues and PRs, ADRs, commits, diffs,
   audit findings, and reports by path or URL. Summarize only context not already
   durable there; do not repeat a project's backlog or plan narrative.
4. Start with a short resume point: current objective; exact plan or work-item
   step and source link when one exists, otherwise the unfinished task; latest
   result and supporting evidence; first concrete permissible action; expected
   observable result; and the condition for stopping or seeking approval. Link
   the exact failed finding when it determines the next action. If work is
   blocked, name the prerequisite instead of implying execution can begin. Use
   any user-specified next-session focus to select the action.
5. Include the remaining context, combining sections when that is clearer:

   - Current state and last completed action
   - Important context and constraints
   - Decisions, distinguishing user rulings from agent choices; record the scope
     and source of standing authorization separately from pending approvals
   - Follow-on actions in order
   - Pending work, blockers, and open loops
   - Verification already run and verification still required
   - Evidence and artifact references
   - Suggested skills for the next session, when relevant

6. Redact credentials, tokens, authentication headers, private personal data,
   and sensitive captured output. Verify paths to existing local artifacts;
   identify intentionally missing paths as missing.
7. Report the handoff location and its first advised next action.

## Resume

1. Read the selected handoff and the authoritative artifacts needed to verify
   its resume point. Treat its observations as dated evidence, not current truth.
2. Compare its Git branch, HEAD, worktree assumptions, relevant GitHub issue or
   PR state, and evidence paths with current state. Increase verification with
   age and drift.
3. Present the current state, stale assumptions, and next action. Continue work
   within the current request or standing authorization verified from its
   source, following any active project approval rules. Seek approval when
   authorization is absent, unclear, or no longer covers the action; do not
   request it again solely because the work crossed a session boundary.

Completion requires a successor to locate the exact resumption point and
distinguish settled decisions, observed state, authorized actions, and unresolved
uncertainty without reconstructing the previous conversation.
