# How work proceeds with GovZero skills

Start with the outcome in ordinary language: “Fix this failure,” “Update the
dependencies,” “Review this change,” or “Commit and push this work.” The agent
selects the appropriate workflow, loads its instructions and completes the
authorized work. You do not need to invoke each internal step yourself.

“Which skill would help?” and “Check freshness without changes” request advice
or inspection. They do not authorize executing the suggested change. A direct
`gzs-update-dependencies` invocation requests updates and verification.

## Choose the installation case

These cases describe available capabilities, not project profiles. Check the
harness's actual skills and project instructions. Installing Superpowers does
not select heavy, adopt a starter, approve an architecture or authorize a
release. An existing project workflow stays in control in either case.

### gz-skills independently present

1. Establish the requested result and relevant project constraints. Clarify a
   material unknown when it affects the result; routine implementation choices
   do not need another approval.
2. Use the applicable standalone GovZero discipline. For a feature without a
   matching catalog workflow, follow the project's normal design and development
   practices and implement the authorized change. Do not require installation
   of Superpowers or invent a mandatory project lifecycle to make progress.
3. Continue through the requested correction or maintenance and the project's
   applicable verification. Use explicit test-first work when the user or
   project requires it. Audits and surveys retain their read-only boundary
   unless the user also requested fixes.
4. Report the actual outcome, evidence and unresolved items. Commit, push,
   publish or create a durable handoff only within established authority.

The destination skill provides the detailed discipline. The router selects and
enters it; it does not replace its instructions with a generic checklist.

### gz-skills alongside installed Superpowers

1. Read the installed Superpowers entry/process guidance when it governs the
   requested work. Resume an already-selected workflow at its current stage;
   do not restart design or planning merely because the router was consulted.
2. Let Superpowers own its development sequence and its actual approval points.
   Follow the installed version and project instructions rather than assuming
   that an upstream name, command or example is available locally.
3. Use gz-skills for a distinct supporting concern: dependency maintenance,
   portability, architecture or intent analysis, repository hygiene, project
   verification, guarded Git sync, or authorized release work. Feed the results
   back into the owning workflow's existing artifacts and evidence.
4. Continue the original task under that owner. Avoid a second diagnosis,
   implementation plan, TDD loop, generic review or gate run covering the same
   unchanged work. If the new concern changes scope or invalidates evidence,
   use the owner's adjustment and revalidation rules.
5. Preserve project/Backplane ownership of tracking, release and handoff state
   where active. Superpowers availability alone does not install Backplane or
   prove an integrated heavy environment is ready.

| Concern | Owner alongside Superpowers | Useful GovZero complement |
| --- | --- | --- |
| Feature intent, design and execution | Installed Superpowers process under project policy | A requested plan audit, architecture analysis or distinct fulfillment check. |
| Debugging | Existing Superpowers diagnostic workflow | A specific portability or dependency investigation; avoid a second generic debugger. |
| Tests and review during development | Existing Superpowers/project stages | A distinct bounded audit or project gate dimension the owner has not covered. |
| Dependency/tool maintenance | `gzs-update-dependencies`, inside any active project stage | Current versions, scoped migration and installed-output verification. |
| Commit/push and branch completion | Project/Superpowers branch workflow | `gzs-git-sync` at the authorized save point; preserve branch/worktree decisions. |
| Release or durable continuity | Active project/Backplane owner when present | `gzs-release` or `gzs-session-handoff` as supporting primitives, without parallel records. |

## Typical requests and completion

Choose the installation case above, then use the relevant recipe. These recipes
do not require running every listed skill or manufacturing missing artifacts.

### “Build this feature”

With gz-skills alone, use ordinary project development for the agreed behavior;
the catalog supplies targeted supporting disciplines. With Superpowers, use its
applicable development workflow. Resolve design choices and approvals that the
task or project actually requires, implement, verify and review as required.
Completion is the working requested behavior and its evidence. A recommendation,
design document or plan alone is incomplete when implementation was requested.
No commit, push or release follows merely because implementation passed.

### “Fix this failure”

The diagnostic owner is `gzs-root-cause-debugging` independently, or the active
Superpowers/project debugger. Reproduce the failure and establish its cause,
then implement the authorized fix and exercise the affected behavior. Keep the
same owner across diagnosis and correction. Completion includes the causal
explanation, changed behavior and verification, or a concrete unresolved blocker.
A request only to diagnose stops at findings; a demonstrated mechanical cause
does not need a new diagnostic ceremony.

### “Update the dependencies”

Use `gzs-update-dependencies` to inventory the project-managed surface, resolve
current stable versions, update tools/declarations/locks through their owners,
adapt integration where needed and verify the resulting project and artifacts.
Preserve the project's runtime/host policy, additions and approved constraints.
Completion is applied and verified maintenance with before/after evidence;
a table of proposed versions is an intermediate result. Explicit freshness-only
requests instead return findings without changing dependency state. Continue
to Git sync or publication only when that additional work is authorized.

### “Review this change”

Use the active review process, or `gzs-change-review` for an independent bounded
diff. Use `gzs-intent-audit` when the actual question is whether delivered
behavior fulfills its specification. Completion is prioritized, evidenced
findings and material limitations. Fixing findings requires authority from the
request or owner; “review and fix” already supplies that scope. Do not repeat
an equivalent completed review simply to add another skill name.

### “Commit and push this work”

Use `gzs-git-sync` inside the owner's permitted branch/save-point sequence.
Understand the complete intended scope, pass applicable gates, commit, reconcile
safely, push and verify local/remote alignment. Completion includes the remote
commit, final ahead/behind state and accounted-for worktree. A pending version
also needs the owning release procedure when publication authority is already
established. Otherwise report the pending release separately from Git alignment.
Do not infer publication authority from the version number or routing decision.

### “Release this version”

Use the active release owner, or `gzs-release` under project policy. Establish
the published baseline, select and validate the finite scope, finalize metadata,
create the immutable identity, publish the declared channels and verify remote
artifacts and required installs. Completion is the authorized published and
verified result; report partial publication precisely. A version recommendation
or prepare-only request ends at that expressly narrower boundary. A development
branch's completion alone does not establish release approval.

### “Hand this off” or “Resume this work”

Use the active owner's handoff mechanism; use `gzs-session-handoff` when no
project owner supplies one. Preserve the original outcome, existing authority,
decisions, current source/worktree, evidence, blockers and next concrete action.
Create or update the existing durable artifact for a handoff request. For a
resume request, reconcile the recorded state with the actual project and
continue the authorized work. The handoff records authority; it grants none
for unrelated changes. Avoid a second competing handoff or backlog.

## Decision points and recovery

The user should make substantive product choices, required project approvals and
any still-ungranted consequential operation. Moving between skills within an
already-authorized task does not itself require another go-ahead. Ask only for
the missing decision; continue independent authorized work while it is pending.

If an owner, command or skill is unavailable, distinguish unknown availability
from a verified absence. Use native discovery or the packaged instructions
where supported. Continue safe independent work and report the blocked dependent
step. An approval conflict, failed required gate or missing release authority
must stay visible; a routing fallback cannot erase it.

Verification belongs to the actual deliverable. Reuse checks that still cover an
unchanged tree, rerun checks invalidated by a change, and preserve stronger
project requirements. Report observed results without equating structural skill
validation, installation, fresh-session activation and model behavior.

## Adoption and first use

Install once through one supported channel in a discovery scope. Use the
harness's native skill picker/loading mechanism; invocation syntax differs.
An installed directory alone does not prove automatic session-start activation.
Ask the agent to use `gzs-router` for your task when automatic selection has not
been established. Do not edit managed plugin caches to simulate activation.

An adopter can explicitly adopt this entry rule in its existing project
instructions after review:

> When selecting an engineering workflow, consult gzs-router unless an active
> owner already establishes the path. With Superpowers installed, follow its
> applicable process and use GovZero skills for distinct complementary work.
> Otherwise use standalone GovZero disciplines and ordinary project practices.
> Execute authorized tasks through completion; questions asking only for advice
> remain read-only. Preserve project approvals and do not duplicate lifecycle
> state, reviews, gates or handoffs.

This is a suggested project instruction, not an automatic file write or a
mandatory dependency. Explicit setup/profile requests use `gzs-project-setup`;
it retains its own profile choice and narrow settings contract. These two
installation cases do not claim that automatic first-use hooks or integrated
heavy readiness have been implemented or qualified.

## Design reference

The presentation and process-selection approach learns from Superpowers'
[basic workflow](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/README.md#the-basic-workflow)
and [entry guidance](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md),
reviewed at that source revision. Superpowers retains its methodology; these
recipes describe GovZero task routing and complementary ownership. Consumers
follow their actual installed version and governing project policy.
