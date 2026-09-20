---
name: gzs-change-review
description: Review a bounded implementation change for defects, regressions, unsafe assumptions, and maintainability risks, then report prioritized evidence-backed findings. Use for code review, diff review, pre-merge review, or independent assessment of a completed change; not for running only automated checks, auditing broad technical debt, or implementing fixes.
compatibility: Requires a readable change set and enough repository context to trace its affected behavior.
metadata:
  govzero-version: "0.1.1"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Change Review

Review one bounded change as an independent reader. Find defects that can affect
users, operators, data, security, compatibility, or future changes; do not turn
the review into an approval ceremony, style rewrite, or implementation pass.

## Precedence and scope

1. Read applicable repository instructions and any active project-owned review
   workflow first. Supply the review discipline below without replacing its
   reviewer roles, independence rules, gates, receipts, or verdicts.
2. Resolve the comparison base and exact changed-file set from the request,
   pull-request metadata, upstream branch, or merge base. State the chosen base
   and include relevant uncommitted changes when they are part of the requested
   review. Stop if different reasonable bases would materially change the scope.
3. Locate the change's stated intent when available, but keep this review
   defect-focused. Use `gzs-intent-audit` instead when the primary question is
   whether delivered behavior completely fulfills an authoritative plan or
   specification.
4. Review is read-only. Do not edit code, publish comments, approve, merge, or
   create issues unless separately authorized.

## Discovery and fallback

Prefer, in order:

1. An active project-owned review workflow, whose reviewer roles, gates, and
   verdicts stay in control.
2. Repository review tooling or pull-request metadata that resolves the
   comparison base.
3. The diff against the resolved base, read directly from version control.

The third rung is the floor and is always available: the diff is the review's
actual subject, and every other rung only organizes how it is read. This skill
therefore needs no project surface to function, only a base it can name.

## Review workflow

1. Read the complete diff, then inspect changed code in context: immediate
   callers and consumers, relevant public contracts, nearby tests, error paths,
   persistence boundaries, and a working analogue where one exists.
2. Trace affected behavior through inputs, state transitions, outputs, and
   failure handling. Check correctness, edge cases, compatibility, security and
   trust boundaries, concurrency, resource ownership, observability, and
   maintainability in proportion to the change's actual risk.
3. Use focused tests, analyzers, or history as evidence when they can confirm or
   refute a suspected defect. Do not duplicate the repository's complete
   quality gate merely to make the review look comprehensive.
4. Retain a finding only when it has a reachable scenario, violated invariant,
   failing check, or precise code path. Cite the narrowest useful file and line,
   explain the consequence, and give a fix direction without writing the patch.
5. Remove findings that are taste-only, speculative, unrelated pre-existing
   debt, or already enforced by tooling without a demonstrated escape. State
   uncertainty and the missing observation instead of overstating confidence.
6. Rank retained findings by consequence and urgency:

   - **Critical:** immediate security, safety, irreversible-data, or published-
     contract failure that should block use or release.
   - **High:** likely user-visible regression or major operational failure that
     should block merging the change.
   - **Medium:** bounded correctness or maintainability defect with a concrete
     future cost or narrower trigger.
   - **Low:** real but limited risk whose remediation can safely follow later.

## Output

Present findings first, ordered by severity. For each finding provide a concise
title, location, triggering scenario, consequence, evidence, and fix direction.
Then state the reviewed base and scope, checks used, assumptions, and residual
risk. If no findings survive, say so explicitly; do not imply that review alone
proves the change correct or that the containing workflow is complete.
