---
name: gzs-router
description: Orient users to the GovZero portable skill catalog. Use when they need the right skill or sequence, ask how to discover, invoke, install, or update GovZero skills, or need help diagnosing skill availability or invocation behavior.
compatibility: Works wherever the installed GovZero skills are discoverable by name.
metadata:
  govzero-version: "0.3.1"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Skill Router

Act as the curator and usage guide for this catalog. Route a user's goal to the
smallest useful skill or sequence, or explain how the catalog is discovered,
invoked, installed, and updated. This is a map, not an orchestrator: recommend
skills and next actions but do not silently start workflows, install or update
packages, or change configuration.

## Choose the mode

- **Task routing:** The user needs the right skill or sequence for an immediate
  goal.
- **Catalog guidance:** The user asks how GovZero skills work, how they are
  installed or updated, or why an expected skill is not visible or activating.

Answer only the mode asked for. Do not reproduce the full catalog when a focused
answer is enough.

## Discovery and fallback

Prefer, in order:

1. An active project-owned workflow that governs the task, which stays in
   control while a portable skill serves as a supporting primitive.
2. A project-local skill that already covers the goal.
3. The catalog in this bundle.

The third rung is the floor and ships with the router itself, so this skill is
never unable to answer. Routing to a portable skill is always possible; what
varies is whether a project surface should take precedence over it.

## Route a task

1. Identify the user's immediate outcome and whether they want action, an audit,
   maintenance, publication, or orientation.
2. Check for an active project-owned workflow. When one governs the task, keep
   it in control and recommend a `gzs-*` skill only as a supporting primitive;
   do not create a parallel lifecycle or bypass its gates and state.
3. Choose one primary skill from the catalog below. Add another only when it is
   a genuine next phase, not merely related.
4. State prerequisites, mutation or remote effects, and whether explicit user
   invocation is required.
5. Give the exact `$skill-name` invocation and a one-sentence starting prompt.
6. When no skill fits, say so. Recommend ordinary agent work rather than forcing
   a catalog match.

## Explain catalog usage

1. Establish the relevant harness and installation channel from available
   evidence. Do not assume that a managed plugin and a vendored snapshot behave
   the same way.
2. Explain the smallest relevant part of the catalog contract:

   - Harnesses discover installed skill names and activation descriptions, then
     load a matching skill's body when needed.
   - Model-invoked skills may activate when the request matches. Explicit-only
     skills require the user to invoke their exact `$gzs-*` name.
   - Managed plugins are read-only subscriptions updated by the harness's plugin
     manager. Do not direct users to edit an installed plugin cache.
   - Vendored snapshots are installed and updated with the `gz-skills` Python
     CLI and recorded in `gz-skills.lock.json`; local modifications block safe
     replacement until reconciled.
3. For availability problems, distinguish among not installed, explicit-only
   and therefore absent from a model-visible list, installed through the wrong
   channel or scope, and duplicated through multiple channels. Do not report a
   skill missing solely because it is hidden from automatic invocation; inspect
   an available plugin manifest, catalog listing, or lock before concluding.
4. Give the exact invocation or next diagnostic step supported by the observed
   environment. Explain commands without executing installation, update, or
   configuration changes unless the user's request separately authorizes them.

## Catalog

| Goal | Skill | Boundary |
| --- | --- | --- |
| Reduce persistent agent-instruction weight | `gzs-agent-context-diet` | Preserves binding rules while pruning or disclosing context. |
| Review a bounded implementation change | `gzs-change-review` | Reports prioritized, evidenced defects without implementing fixes or owning approval. |
| Review Python for operating-system assumptions | `gzs-cross-platform-python` | Applies to Python portability, not general cross-platform product design. |
| Assess dependency and supply-chain risk | `gzs-dependency-risk-audit` | Read-first portfolio evidence; does not update packages or own risk acceptance. |
| Commit and publish a guarded save point | `gzs-git-sync` | Explicit-only; commits and pushes after repository gates pass. |
| Analyze and improve hexagonal architecture boundaries | `gzs-hexagonal-architecture-audit` | Read-only design and implementation coaching; does not replace general plan, intent, or code review. |
| Compare delivered behavior with its owning intent | `gzs-intent-audit` | Diagnoses and routes gaps; does not implement corrections unless separately requested. |
| Check intent, scope, and plan alignment | `gzs-plan-audit` | Runs before implementation and audits existing artifacts. |
| Run the repository's complete verification | `gzs-quality-gate` | Uses project-owned commands and reports unavailable dimensions honestly. |
| Audit or repair repository hygiene | `gzs-repository-hygiene` | Begins read-only; cleanup requires authorization from the request or project workflow. |
| Diagnose a bug, failing test, regression, or unexplained slowness | `gzs-root-cause-debugging` | Establishes root cause from reproducible evidence and yields to active project-owned workflows. |
| Preserve or resume engineering state | `gzs-session-handoff` | Explicit-only; creates or consumes a durable continuity artifact. |
| Survey and prioritize technical debt | `gzs-tech-debt-review` | Produces an evidenced report without fixing findings. |
| Implement an explicitly test-first behavior change | `gzs-test-driven-change` | Runs a verified red-green-refactor loop inside the owning project workflow. |
| Refresh project dependencies and pinned tools | `gzs-update-dependencies` | Covers project-managed versions, not machine-wide or deployed infrastructure. |

## Common sequences

- Dependency risk response: `gzs-dependency-risk-audit` →
  `gzs-update-dependencies` only when an upgrade is the authorized response.
- Dependency maintenance: `gzs-update-dependencies` → `gzs-git-sync` when the
  verified update should be published.
- Failure resolution: `gzs-root-cause-debugging` → `gzs-quality-gate` after an
  authorized fix, unless the active project workflow already owns verification.
- Architecture alignment: `gzs-hexagonal-architecture-audit` for boundary and
  dependency-direction analysis; add `gzs-plan-audit` only when the broader
  plan also needs intent, scope, and completeness review.
- Pre-publication confidence: `gzs-quality-gate` → `gzs-git-sync` when no broader
  maintenance workflow already ran the complete gate.
- Test-first delivery: `gzs-test-driven-change` → `gzs-change-review` when the
  completed implementation needs an independent semantic review.
- Plan integrity: `gzs-plan-audit` before implementation; `gzs-intent-audit` after
  delivery when fulfillment is uncertain.
- Repository maintenance: `gzs-repository-hygiene` → `gzs-quality-gate` when the
  hygiene workflow did not already include the full final gate.
- Session continuity: `gzs-session-handoff` at a stopping boundary; invoke it
  again to resume from the artifact.

Avoid redundant sequences. A skill that already requires the complete quality
gate does not need a second quality invocation unless the tree changed afterward.

## Output

For task routing, return the primary recommendation, optional sequence,
rationale, prerequisites or side effects, and exact invocation. For catalog
guidance, state the relevant channel or invocation mode, answer the question,
and give one concrete next step. Keep either response short enough to function
as orientation rather than reproducing another skill or the installation docs.
