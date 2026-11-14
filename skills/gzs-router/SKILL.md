---
name: gzs-router
description: Select and enter the appropriate workflow for an engineering task using standalone GovZero skills or complementary skills alongside installed Superpowers. Use when choosing how to start or continue work, explaining typical workflows, or diagnosing skill discovery. Execute an authorized task through its owner; recommendation-only questions remain read-only.
compatibility: Works wherever the installed GovZero skills are discoverable by name.
metadata:
  govzero-version: "0.6.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Skill Router

Route the user's outcome to its owning workflow and carry authorized work into
that workflow. Explain the selection briefly, load the applicable instructions,
and continue to the requested completion boundary. A request for a recommendation
or catalog explanation remains read-only. Routing does not grant new authority.

Use the [adopter workflow guide](references/workflows.md) when establishing a
workflow, explaining what happens next, or deciding how gz-skills complements
installed Superpowers. It covers typical requests, ownership, handoffs and done
conditions. Read only the relevant recipe after selecting the installation case.

## Establish ownership

- With gz-skills alone, choose the applicable standalone discipline. Ordinary
  engineering work fills gaps the catalog does not cover; no additional plugin
  is required to complete a bounded task.
- When Superpowers is installed and applicable, follow its installed entry and
  process guidance. It owns its feature, debugging, test, review and branch
  workflows. Add a GovZero discipline for a distinct supporting need; do not
  rerun a second debugging, planning, review or verification workflow by default.
- An active project-owned workflow takes precedence in either case. Preserve
  its approvals, stages, state, locks, evidence and release/handoff ownership.
  If Backplane governs the project, retain its authority. Do not introduce
  another lifecycle, tracking file or mandatory orchestration dependency.

Discover actual availability through the harness and project instructions;
do not infer installation from a profile, a directory name or this guide.
Unknown availability is an explicit gap, not a reason to install another plugin
or stop an independent standalone task. Presence of Superpowers selects neither
lite nor heavy and grants no architecture, publication or setup approval.

## Discovery and fallback

Prefer, in order:

1. An active project-owned workflow, which stays in control while a portable
   skill serves as a supporting primitive.
2. The project's selected workflow or local skill, including installed
   Superpowers where applicable to development work.
3. The catalog in this bundle.

The third rung is the floor and ships with the router itself. When no catalog
skill fits, explain or perform ordinary agent work according to the request;
a routing answer does not require a matching skill or another plugin.

## Route a task

1. Identify the requested outcome. Distinguish action from a recommendation,
   diagnosis from a fix, review from revision, and Git sync from publication.
   Carry established authority through handoffs and corrections.
2. Resolve the owner from project instructions, active workflow and actual
   installed capabilities. Consult the relevant installation case and recipe in
   the guide. Keep a running workflow in control rather than starting it again.
3. Select one primary workflow. Add another only for a distinct missing concern
   or actual next phase. Do not duplicate gates or collect every related skill.
4. For an action request, name the owner briefly and load/invoke its instructions
   through the observed harness. Continue within the authorized scope instead of
   stopping at a skill menu or asking the user to repeat the request with another
   invocation. Preserve the destination's required approvals. Explicit-only
   operations need explicit authority for their effect, such as commit/push,
   release publication or durable handoff; router activation alone supplies none.
   If invocation is unavailable, read the workflow where supported or identify
   the limitation and continue independent work. Never claim an unperformed step.
5. For a recommendation or usage question, give the exact invocation supported
   by the observed harness, preserving its plugin namespace, and a short starting
   prompt. Do not assume a universal dollar, slash or at-sign command. If syntax
   is unverified, name the skill and give a native discovery step. Do not execute
   the recommended workflow merely to explain it.
6. Preserve the original outcome across transitions. Reuse applicable evidence
   for an unchanged tree, obey actual approval points, and report the achieved
   result and remaining blockers. Routing alone does not complete an action task
   or its containing project workflow.

## Explain discovery and adoption

Establish the harness and installation channel before diagnosing visibility or
suggesting installation commands. Model-selected skills can activate when the
request matches; explicit-only skills still require the user's authorization
for their operation. Skill registration and automatic session-start loading are
separate observations; do not promise bootstrap behavior from an installed file.

Managed plugins use the native manager; do not edit their cache. Vendored
snapshots use their project lock and complete tree hashes; preserve local edits.
Distinguish absent, hidden explicit-only, wrong scope, duplicate installation and
unavailable host syntax. Installation, updates, setup and configuration changes
need authority from the user's request or project policy. Explain them read-only
when that is all the user asked. Profile selection and integrated heavy readiness
remain with their owning setup/project workflow and evidence.

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
| Initialize or promote a project's GovZero profile | `gzs-project-setup` | Creates minimal project settings after checking for gzkit; does not install other plugins. |
| Review Python design-pattern refactor candidates | `gzs-pythonic-pattern-detect` | Read-only review of concrete code shapes; scanner hits are leads, not findings. |
| Apply one Pythonic pattern refactor | `gzs-pythonic-pattern-apply` | Requires an authorized candidate and passing before/after behavior evidence. |
| Run the repository's complete verification | `gzs-quality-gate` | Uses project-owned commands and reports unavailable dimensions honestly. |
| Recommend, prepare, or publish a release | `gzs-release` | Explicit-only; project policy determines versions and gates, and publication requires established authority. |
| Audit or repair repository hygiene | `gzs-repository-hygiene` | Begins read-only; cleanup requires authorization from the request or project workflow. |
| Diagnose a bug, failing test, regression, or unexplained slowness | `gzs-root-cause-debugging` | Establishes root cause from reproducible evidence and yields to active project-owned workflows. |
| Preserve or resume engineering state | `gzs-session-handoff` | Explicit-only; creates or consumes a durable continuity artifact. |
| Survey and prioritize technical debt | `gzs-tech-debt-review` | Produces an evidenced report without fixing findings. |
| Implement an explicitly test-first behavior change | `gzs-test-driven-change` | Runs a verified red-green-refactor loop inside the owning project workflow. |
| Update project dependencies and tools, or explicitly review freshness | `gzs-update-dependencies` | Direct invocation requests completed scoped updates; an explicit check leaves pins unchanged. |

## Common sequences

The guide describes each transition and completion boundary. These are useful
compositions when no active owner already supplies the same work:

- Bug fix: diagnosis through `gzs-root-cause-debugging`, authorized correction,
  then project verification. A diagnosis-only request stops before the fix.
- Dependency maintenance: `gzs-update-dependencies` through update and validation;
  `gzs-git-sync` follows only when commit/push is authorized.
- Release: `gzs-release` through the requested advice, preparation or publication
  boundary. `gzs-git-sync` follows pending versions through that owning workflow
  only when publication authority is already established.
- Refactoring: `gzs-pythonic-pattern-detect` for requested candidate review, then
  `gzs-pythonic-pattern-apply` for an authorized candidate. Use
  `gzs-hexagonal-architecture-audit` for a distinct boundary question.
- Explicit test-first change: `gzs-test-driven-change`, with an appropriate
  `gzs-change-review` when requested or project-required.
- Plan/fulfillment uncertainty: `gzs-plan-audit` before execution or
  `gzs-intent-audit` after delivery; neither is a mandatory extra stage for every
  small task. Keep technical-debt and dependency-risk surveys read-only unless
  corrective work is separately authorized.
- Save or resume state: use the active owner's handoff mechanism; otherwise
  `gzs-session-handoff` handles an explicit continuity request.

## Output

For an action request, briefly name the selected owner and proceed; report
results after the requested work, its verification and applicable handoffs.
For guidance, give the smallest useful recommendation or sequence, rationale,
actual invocation/discovery step and material side effects. Explain only the
workflow or catalog question asked; do not reproduce the entire catalog.
