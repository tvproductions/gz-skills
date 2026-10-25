# Router contract review — October 25, 2026

Reviewed: `gzs-router` 0.5.0 at repository HEAD
`c5703ef12061217a2866fbb9f482f168f768a193`. The initial findings below refer to
that version. The follow-up applies candidate 0.5.1 in the worktree; the
pre-existing backlog documentation edits are preserved.

Initial decision: **revise before stable acceptance**. Keep the router in the
catalog and keep model-invoked activation. Follow-up status: **corrections
applied; Claude and selected Codex scenario checks passed, OpenCode blocked**.
This review does not approve a 1.0.0
release or promote the candidate to a published release.

## Findings

1. **Resolve the unconditional fallback claim.** In `Discovery and fallback`,
   the router says routing to a portable skill is always possible. `Route a
   task`, step 6, instead correctly requires an ordinary-agent-work response
   when no skill fits. A request to choose a workflow for translating a poem
   has no matching discipline in this catalog. The fallback should guarantee
   an orientation answer, including an explicit no-match result, rather than
   guarantee a skill recommendation. Retain step 6 as the intended behavior.
   This is a wording correction, not a request to expand the catalog.
2. **Reconcile provenance with current activation.** The router entry in
   [origins](../origins.md#gzs-router) describes the portable invariant as
   user-invoked, while `agents/openai.yaml` permits implicit invocation and the
   OpenCode adapter registers the router with `autoinvoke: true`. The
   repository contract suite explicitly expects implicit Codex policy. Update
   the provenance wording to distinguish source history from the current
   read-only, model-invoked contract; do not disable implicit activation to fit
   the older description.

## Contract and activation

The portable invariant is the smallest useful recommendation or diagnostic next
step, without executing the selected workflow. Project workflows and local
skills take precedence; the bundle catalog is the final discovery source.
Project commands, lifecycle state, installation scope, gates and publication
authority remain with their owners.

Keep both user and model invocation for catalog orientation. Positive triggers
include “which GovZero skill reviews this diff?”, “how do I update the vendored
snapshot?” and “why is git-sync missing from automatic discovery?”. Negative
triggers include a direct feature implementation request, generic debugging
already owned by an active workflow, or ordinary writing unrelated to skill
selection. An explicit skill-selection question about an unrelated task should
receive a no-match response.

The body prohibits silent workflow execution, package installation/update and
configuration mutation. A recommendation of git-sync, release or handoff does
not itself grant their execution authority. Installation guidance must first
resolve harness/channel evidence and preserve locally modified snapshots.

## Scenario walkthroughs

Method: one reviewer applied the current router text to the inputs below and
compared the result with the destination skill bodies, activation metadata,
installer documentation and adapter registration. These are manual contract
walkthroughs, not independent agent runs or fresh-session harness trials.

The no-skill baseline below is the direct reasoning needed without this router;
it is an analytical comparison, not a measured control run. No latency,
quality improvement or activation success is inferred from it.

| Input and evidence | No-skill baseline | With-router walkthrough and result |
| --- | --- | --- |
| “Which skill should review this diff?” | Find the review discipline and separate review from fixes. | Recommend `$gzs-change-review` with a bounded diff prompt; no implementation. Catalog and destination agree. |
| “Which skill checks whether a completed feature meets its spec?” | Distinguish fulfillment from defects in a patch. | Recommend `$gzs-intent-audit`, not a redundant review sequence. Destination agrees. |
| “Recommend a skill to check dependency freshness; do not update.” | Separate current-version research from changes. | Recommend `$gzs-update-dependencies` in review mode, keeping pins unchanged. Destination agrees. |
| “Which skill commits and pushes this work?” | Distinguish a remote save point from release publication. | Recommend explicit `$gzs-git-sync`, explain gates and remote effects, and do not execute it as part of orientation. Destination agrees. |
| “Which skill recommends a release version?” | Separate advice, preparation and publication. | Recommend explicit `$gzs-release` with a recommendation prompt; no publishing authority follows. Destination agrees. |
| An active project review workflow owns gates and reviewer roles. | Read and preserve project policy. | Keep that workflow primary and use change-review only as its supporting discipline. Precedence is explicit. |
| “Git-sync is not visible”; manifest lists it and implicit activation is false. | Inspect installation evidence before reinstalling. | Explain explicit-only discovery and give the exact invocation; do not report it missing or install a duplicate. Metadata agrees. |
| A vendored skill hash differs from its lock. | Read updater safety rules before replacement. | Explain that local modifications block replacement; recommend reconciliation without editing the snapshot. Channel guidance agrees. |
| “Which skill translates a poem?” | Answer that the catalog has no matching discipline. | Step 6 yields ordinary agent work, but the fallback's unconditional routing claim conflicts. Finding 1. |

## Evidence and acceptance limits

Read the complete router body and OpenAI metadata, all catalog descriptions,
the git-sync/release/handoff authority clauses, the OpenCode adapter and
repository contract tests, plus the linked provenance and installation policy.
The catalog table names all nineteen other current skills; the router need not
route to itself as a task discipline. Codex metadata and OpenCode registration
both allow implicit router activation and restrict the three explicit-only
destinations. These source checks do not prove native-host execution.

The walkthroughs alone do not establish native behavior. The later Claude
results below cover positive/negative selection, host-specific spelling and
hidden-skill diagnostics. Selected Codex checks are recorded separately below.
OpenCode behavioral evidence remains outstanding; do not claim complete
cross-harness acceptance from the completed results.

## Correction follow-up

Both findings are addressed in candidate `gzs-router` 0.5.1. The fallback now
guarantees an orientation answer and explicitly permits ordinary agent work
when no catalog skill fits. Origins now distinguishes the user-invoked
extraction history from the current user/model-invoked contract. Activation
metadata and adapter registration are unchanged. The patch classification
against released 0.5.0 is a compatible wording correction; pending bundle
0.8.1 covers it alongside the quality-gate correction.

Rechecked the unmatched input manually: “Which skill translates a poem?” now
yields “No catalog skill fits; use ordinary agent work” consistently under both
the fallback section and task-routing step 6. A matching diff-review request
still yields `$gzs-change-review`; project-workflow precedence and the
prohibition on silent execution remain intact. Diff review confirms the skill
changes are confined to its version and fallback paragraph. These are manual
checks, not fresh-session activation evidence.

The next queued skill remains `gzs-git-sync`; the router awaits the remaining
cross-harness evidence before stable acceptance.

## Native-session validation attempt

On 2026-10-25, local CLI discovery found Codex 0.164.0, Claude Code 2.1.302
and OpenCode 2.0.11. Installed executables alone do not establish authentication
or behavioral readiness.

Two fresh Claude processes were started in separate temporary directories with
the candidate repository passed through session-only `--plugin-dir`, permission
mode `dontAsk`, tools restricted to `Skill,Read`, strict MCP configuration and
no session persistence. No persistent plugin installation was performed.

| Probe | Observed result | Verdict |
| --- | --- | --- |
| Implicit selection: ask which GovZero skill reviews a bounded diff, recommendation only | Initialization reports inline `gz-skills` 0.8.1 from the candidate repository and lists `gz-skills:gzs-router`; authentication then fails with an expired OAuth session that cannot be refreshed. Exit 1; zero model input/output tokens. | Candidate discovery observed; implicit activation and answer untested. |
| Explicit invocation: `/gz-skills:gzs-router` for a poem-translation no-match request | Candidate router appears in initialization, but the same authentication error prevents inference. Exit 1; zero model input/output tokens. | Command discovery observed; invocation execution and fallback behavior untested. |
| Negative activation: translate a single word, with no catalog request | Automatic approval review rejected process execution because candidate repository instructions could be transmitted to an external model service without specific payload authorization. | Not run; no behavioral conclusion. |

The successful discovery observation is session-only candidate loading, not a
tagged marketplace install. User-level plugins were also visible in Claude's
initialization, so even a later successful answer needs a duplicate-source and
interference check before calling the environment isolated.

Further external-model probes were stopped after the approval rejection. The
user subsequently authorized the candidate payload and restored Claude
authentication; the successful follow-up is recorded below. Codex/OpenCode
native behavioral probes remain outstanding. The
local OpenCode adapter test passes, but is not a native inference run.

Local-only follow-up: all 12 repository contract tests pass, the inventory
reports zero floor violations, and `git diff --check` passes. The preceding
complete 28-test suite, all 20 Agent Skills validations and candidate build also
passed. These checks do not resolve the native behavioral acceptance gap.

## Authorized Claude behavioral follow-up

After explicit user authorization and reauthentication, seven fresh Claude Code
2.1.302 sessions completed successfully. Each used its own temporary working
directory, `--setting-sources ''`, `--permission-mode dontAsk`, strict MCP
configuration, no session persistence and only `Skill,Read` tools (the baseline
used only `Read`). Candidate sessions used session-only `--plugin-dir` pointing
to this repository. Initialization confirms the only non-builtin plugin is the
inline candidate `gz-skills` 0.8.1. Built-in host skills remain available; this
is not a host stripped of all built-ins. No persistent plugin configuration,
Git or downstream workflow mutation was authorized or observed.

The [sanitized session evidence](gzs-router-2026-10-25-claude-evidence.json)
preserves session IDs, model and CLI versions, candidate plugin identity,
actual tool calls and final answers. It excludes raw thinking and unrelated
host metadata. The initial three cases precede the invocation-wording fix;
the remaining candidate cases exercise the corrected tree whose SHA-256 is
recorded in the artifact. This is local candidate loading, not tagged installation.

| Case | Observed behavior | Result |
| --- | --- | --- |
| No-skill control | With custom skills disabled and no candidate loaded, the same diff-routing prompt could not identify a reliable GovZero skill and requested catalog evidence. | Measured baseline; no claim of general quality or speed improvement. |
| Implicit selection | Called `Skill` with `gz-skills:gzs-router`, then recommended change-review without executing it. | Selection and mutation boundary pass; initially exposed the invocation defect below. |
| Explicit no-match | `/gz-skills:gzs-router` answered that no catalog skill translates poems and suggested ordinary agent work; no tool calls. | Corrected fallback passes. |
| Unrelated negative request | Replied `Hola` to the translation request, with no skill/tool calls. | Negative activation passes for this input. |
| Host syntax after correction | Automatically called the router, recommended `/gz-skills:gzs-change-review` with the observed namespace, and did not call the destination. | Host command guidance passes. |
| Hidden explicit-only skill | Distinguished implicit visibility from missing installation based on supplied manifest/policy evidence; gave `/gz-skills:gzs-git-sync`, explained commit/push effects and made no tool calls. | Diagnostic and authority boundary pass; not an independent inspection of a colleague's installation. |
| Active workflow precedence | Kept project reviewer roles, gates and approval in control, recommended only supporting change-review, used the Claude namespace and made no tool calls. | Precedence and no-execution boundary pass. |

The first successful implicit case emitted `$gzs-change-review`, exposing the
router's hard-coded dollar syntax. Candidate 0.5.1 now requires the observed
harness syntax and namespace, with a discovery step when syntax is unverified;
catalog guidance no longer assumes a universal dollar command. The host-syntax
case is the positive rerun after that correction. This remains a compatible
correction covered by the existing pending patch versions.

All seven sessions exited 0 with `is_error: false`; no permission denials were
reported. Outputs were sometimes longer than the router's concise orientation
goal, but selected the correct primary discipline and preserved execution
boundaries. A finite scenario set does not prove universal activation behavior.
Claude's selected scenarios now have native evidence. The later Codex/OpenCode
attempts below update the remaining cross-harness evidence gap.

## Codex and OpenCode follow-up

The user authorized continuation with the remaining harnesses. Native Codex
0.164.0 sessions used a temporary project-scoped `.agents/skills` snapshot of
the candidate tree, whose router file hash matches the source. This exercises
the supported snapshot discovery surface, not managed-plugin installation.
Runs used `--ignore-user-config`, `--ephemeral`, `--skip-git-repo-check` and
`--sandbox read-only`; no persistent user config or installed plugin was changed.

The initial implicit run selected the router but failed to read its body because
the isolated configuration omitted the user's selected Windows sandbox
implementation. Exit 0 and a correct recommendation were insufficient for body
validation. A process-only `windows.sandbox="unelevated"` override restored the
existing user setting while retaining read-only mode; the rerun successfully
read the candidate router and the change-review definition. That inspection
supports routing and does not constitute executing the destination review.
See [Codex evidence](gzs-router-2026-10-25-codex-evidence.json).

| Codex case | Observed result |
| --- | --- |
| Implicit routing after sandbox correction | Read candidate router 0.5.1 and recommended change-review only; preserved project precedence and reported no workflow execution. |
| Explicit `$gzs-router` no-match | Returned ordinary agent work for poem translation, without tool calls or file changes. |
| Unrelated translation | Returned `Hola`, without router activation or tool calls. |
| Active workflow precedence | Recommended supporting change-review with `$gzs-change-review`, preserving owning reviewer roles, gates, state and approval. |
| Hidden explicit-only skill | Correctly distinguished automatic visibility from absence, warned that successful activation of hidden git-sync was unverified, and recommended checking the explicit skill picker without installing or running Git. |

Explicit cases are handled through native skill invocation; the implicit rerun
provides the observable candidate body read. These finite probes establish
selected Codex behavior, not every install channel or universal activation.

OpenCode 2.0.11 used a separate temporary project config with the local candidate
package directory and permissions denying mutations while allowing skill/read
inspection. Local-directory loading and ordered action rules follow the
[OpenCode plugin](https://dev.opencode.ai/v2/docs/plugins) and
[permission](https://opencode.ai/v2/docs/permissions) documentation. The Windows
sandbox implementation is documented in the
[Codex Windows guide](https://learn.chatgpt.com/docs/windows/windows-sandbox).

The native OpenCode run exited 1 before inference with `provider.auth` HTTP 401:
the stored OpenCode Go API key has expired, and signing in again will not renew
it. Provider inventory showed only that stored integration. No credential values
were read or printed. Native candidate loading and router behavior are therefore
unverified; a configured local path alone is not loading evidence. The local
adapter contract test remains a separate passing check.
See [OpenCode evidence](gzs-router-2026-10-25-opencode-evidence.json).

The user replaced the key and confirmed readiness. A retry then reached the
provider but exited 1 with `provider.invalid-request` HTTP 400: the selected Go
model trains on request data and the workspace privacy setting disallows that.
The privacy setting was preserved. Follow-up model discovery could not run
because the previously discovered npm `opencode` launcher had disappeared;
temporary update/reinstall artifacts were visible, but their cause was not
established. Do not run an obsolete hidden launcher as a workaround.

The user was asked to finish local OpenCode setup with a privacy-compatible
provider/model and confirm that `opencode --version` works. Resume the OpenCode
implicit, explicit no-match, negative activation, host-invocation, diagnostic and
precedence checks after that. No key was shared in chat or written into this
repository. Full stable cross-harness acceptance remains pending that evidence.

## Release loading follow-up

During authorized 0.8.1 release preparation, the restored OpenCode launcher
reported 2.1.4. A temporary loopback-only native server initialized the test
location and exposed the candidate through `/api/skill`: the registry included
the router from this repository with the candidate body and `autoinvoke: true`.
One-shot registry requests made before location initialization returned an empty
registry and were not accepted as loading evidence. The server was stopped
after inspection. No inference or privacy setting change was involved.

Codex's native loader accepted the 0.8.1 candidate through a disposable local
marketplace with a marketplace-relative source path. Preceding-tag HTTPS
marketplace installations passed in both Codex and Claude disposable configs.
These results clear candidate loading checks, not the remaining OpenCode
behavioral acceptance. Tagged installation and artifact evidence belongs to the
[0.8.1 release record](https://github.com/tvproductions/gz-skills/releases/tag/v0.8.1).
