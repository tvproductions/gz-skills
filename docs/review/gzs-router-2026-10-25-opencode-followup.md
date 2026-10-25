# OpenCode inference follow-up — October 25, 2026

**Provider blocker resolved.** Native OpenCode 2.1.4 now completes inference
against released bundle v0.8.1 and router 0.5.1 while preserving the workspace's
no-training privacy policy. The published tag and skill instructions are unchanged.

## Cause and configuration fix

The global config had no selected model. The native model registry selected
`opencode-go/iceman-contributor-free` as its fallback. OpenCode's
[Go privacy table](https://dev.opencode.ai/v2/docs/console/go#privacy) identifies
that contributor model as training on request data. The existing workspace
privacy policy correctly rejected it; valid authentication alone could not fix
that incompatibility.

Both Kimi K2.7 Code and Kimi K3.1 Pro were enabled in the existing Go account.
The same privacy table lists them as non-training with zero-day retention.
These are provider-documented terms, not independently measured retention.
Validation selected Kimi K3.1 Pro at low reasoning effort after Kimi K2.7
produced unreliable invocation guidance.

The user explicitly requested making the tested model the default. Existing
global settings were preserved and backed up locally before adding:

```json
{
  "model": "opencode-go/kimi-k3.1-pro",
  "providers": {
    "opencode-go": {
      "models": {
        "kimi-k3.1-pro": {
          "settings": { "reasoningEffort": "low" }
        }
      }
    }
  }
}
```

The native `/api/model/default` response confirms that model/provider and
`reasoningEffort: low`. A fresh run without `--model` loaded the router and
returned the correct poem-translation no-match answer. Workspace privacy
settings and credential stores were not edited. This local user choice is not
a model requirement imposed by the portable catalog.

## Native behavioral evidence

Tests ran in separate temporary projects with the released Git package,
read/skill permissions, and mutation actions denied. No destination workflow,
installation into an existing consumer, Git operation or publication was
performed by the model. The existing global compatibility skills and host
built-ins remained discoverable; the no-plugin control records that context.

[Sanitized session evidence](gzs-router-2026-10-25-opencode-behavior.json)
records 18 native runs, including the failed guidance examples and discarded
instruction experiment. Only source hashes, model identities, tool-call
metadata and final answers are retained; provider credentials, workspace
headers and raw reasoning are excluded.

| Kimi K3.1 Pro scenario | Observed result |
| --- | --- |
| Automatic catalog orientation | Loaded native `opencode` guidance and `gzs-router`; described workflow precedence, selection, invocation and missing-skill diagnosis without executing a destination. |
| Explicit bounded-diff routing | Loaded `gzs-router` and recommended only `gzs-change-review`, giving a valid skill-tool input rather than an invented wrapper. |
| Explicit no-match | Loaded `gzs-router` and recommended ordinary agent work for poem translation. |
| Negative activation | Returned `Hola` without any skill/tool calls. |
| Active project workflow | Loaded the router and retained the project's reviewer roles, gates and approval authority. |
| No-plugin control | Could not identify a registered GovZero review skill; did not fabricate one. This is a same-model control, not proof of a general quality improvement. |
| Hidden-skill diagnosis without host syntax evidence | Correctly identified explicit-only registration, but suggested an unverified `/gzs-git-sync` command. This is a separate review finding below. |
| Hidden-skill diagnosis with observed host evidence | Loaded the router, supplied `@gzs-git-sync`, described commit/push effects and did not invoke it. |
| Saved-default smoke test | Without a command-line model override, loaded the released router and produced the correct no-match answer. |

All these sessions completed with exit 0 and no provider privacy rejection.
Exit status is not treated as proof that every semantic answer passed.

## Remaining invocation-guidance finding

Provider access is no longer pending. A separate weakness remains when the
model has not established the harness's invocation syntax: Kimi K2.7 emitted
XML/tool wrappers, and an ungrounded Kimi K3.1 diagnostic suggested a slash
command. The observed native command registry listed only `init` and `review`;
it did not establish a `gzs` slash command. Official
[OpenCode skill loading](https://dev.opencode.ai/v2/docs/skills#loading)
documents `@skill-id` for explicit user loading.

Supplying that actual host evidence yielded the correct `@gzs-git-sync`
recommendation. Do not certify the earlier slash claim or infer that every
host/model combination always emits correct user syntax. The router already
requires observed syntax or a discovery step; an attempted four-line prompt
reinforcement did not reliably change Kimi K2.7's behavior and was removed.
The trial's version and bundle edits were also removed. No new skill version
or release is necessary to resolve the provider blocker.

Review outcome: **keep; native inference evidence complete for the tested
configuration, invocation-guidance robustness still needs review before stable
acceptance**. Route further work to host-syntax discovery and verification,
not to relaxing privacy settings. Promotion to 1.0.0 is not approved here.
