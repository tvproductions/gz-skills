# Router review and OpenCode inference handoff

Observed: 2026-10-25 17:48:31 UTC (12:48:31 America/Chicago).
Workspace: `U:\repos\agents\gz-skills`.

## Resume point

The latest requested fix is complete: **OpenCode inference works without
relaxing the workspace's no-training privacy policy**. The user asked for this
handoff to clear/compact context, not for another release or implementation.

First permissible action on resume: inspect `git status --short` and the
uncommitted documentation diff, then read the
[OpenCode follow-up](../review/gzs-router-2026-10-25-opencode-followup.md#remaining-invocation-guidance-finding).
Expect six pre-handoff documentation/evidence paths, plus this handoff, with
no skill or version changes. Preserve them. The next substantive router work,
if the user requests it, is validating host-invocation guidance rather than
reopening the resolved provider/privacy blocker. Stop before new source
changes or remote mutations unless the current request authorizes them.

## Git and release state

- Branch: `main`.
- HEAD: `58c1b752307979b9d62e6247469176c0aa18005e`.
- Commit: `Release gz-skills v0.8.1 with router corrections and reconciled backlog`.
- At the last remote verification, `main` and `origin/main` were aligned,
  ahead 0 / behind 0. No fresh fetch was needed solely to write this handoff;
  fetch again before relying on remote alignment for another publication.
- [v0.8.1 is published](https://github.com/tvproductions/gz-skills/releases/tag/v0.8.1),
  neither draft nor prerelease. Annotated tag resolves to HEAD above.
- Released versions: bundle 0.8.1, router 0.5.1, quality-gate 0.1.2. All bundle
  manifests, lock and fallback agree; both marketplaces pin v0.8.1.
- [Issue #1](https://github.com/tvproductions/gz-skills/issues/1) is closed with
  resolution evidence. Its last quality-gate correction was committed in
  `c5703ef12061217a2866fbb9f482f168f768a193` and included in v0.8.1.

Release checks passed on a clean clone: 28 unittests, all 20 Agent Skills
validations, native validators/loading, and complete packaged skill-tree byte
comparisons. Codex/Claude marketplace, OpenCode Git-package and uvx tagged
installs passed. Downloaded GitHub artifacts matched checksums:

```text
eae0d08c75cf11a53358d73614e6fd8673fe8d6ac4d9294310df96a566eaa748  govzero_skills-0.8.1-py3-none-any.whl
b2d656c0d766a92e294ff5658ec3391185b0d5bbfea2114cb1ceb1b23d142cc2  govzero_skills-0.8.1.tar.gz
```

No npm/PyPI upload, universal Plugins Directory publication, consumer migration,
or stable 1.0.0 acceptance was claimed. The release notes accurately preserve
the inference limitation observed at publication; later evidence is local and
uncommitted below.

## Uncommitted work to preserve

These six paths existed before writing this handoff; none is staged:

| Path | Content |
| --- | --- |
| [CHANGELOG.md](../../CHANGELOG.md) | Unreleased documentation-only entry for completed OpenCode inference and the remaining guidance finding. |
| [Review queue](../review/README.md) | Provider blocker resolved; invocation robustness still precedes stable acceptance. |
| [Original router review](../review/gzs-router-2026-10-25.md) | New pointer to the latest follow-up, preserving historical failed attempts. |
| [Roadmap](../roadmap.md) | Distinguishes verified native inference from remaining host-syntax guidance. |
| [OpenCode behavioral evidence](../review/gzs-router-2026-10-25-opencode-behavior.json) | New, untracked; 18 sanitized native session records, including failures and controls. |
| [OpenCode follow-up](../review/gzs-router-2026-10-25-opencode-followup.md) | New, untracked; root cause, configuration fix, observations and remaining finding. |

There are **no retained skill edits or version bumps**. An attempted four-line
router instruction reinforcement did not reliably improve Kimi K2.7's answers.
It and its trial router 0.5.2 / bundle 0.8.2 metadata were removed. The two
generated 0.8.2 archives from that discarded trial were also removed. Do not
resurrect that candidate or describe it as released.

## OpenCode fix and machine-local state

OpenCode is now 2.1.4. With no configured model it selected
`opencode-go/iceman-contributor-free`; the provider documents request-data
training for that model, so the existing privacy policy correctly rejected it.
Replacing the previously expired API key fixed authentication but not that
model-policy incompatibility.

The user explicitly authorized the tested model as their default. The saved
global config at `C:\Users\Jeff\.config\opencode\opencode.jsonc` now selects:

- Model: `opencode-go/kimi-k3.1-pro`.
- Per-model setting: `reasoningEffort: low`.
- Equivalent test override: `--model opencode-go/kimi-k3.1-pro#low`.

Existing settings were preserved. A backup was created at
`C:\Users\Jeff\AppData\Local\Temp\gz-opencode-default-backup-1bbua9cx\opencode.jsonc`.
These paths are **machine-local**, not repository artifacts or portable
requirements. Both the selected default and backup existence were rechecked for
this handoff. Workspace privacy and credential stores were not edited by the
agent. Do not print credentials, provider headers or raw reasoning.

OpenCode's native `/api/model/default` confirmed the model/provider and low
effort. A fresh inference run without `--model` loaded the released router and
returned the correct no-match response. The provider documentation identifies
Kimi K3.1 Pro as non-training with zero-day retention; those are documented
provider terms, not a locally measured guarantee. Sources and configuration
details are in the follow-up report.

Raw test files remain in temporary directories named
`gz-router-opencode-behavior-20261025-*`; they may disappear and are not the
only evidence. The repository JSON is the durable sanitized record. Some
temporary fixtures and native CLI caches need sandbox escalation to read.

## Remaining finding and next work

Do not conflate successful inference with universally correct routing output.
Kimi K2.7 emitted invented XML/tool invocation wrappers; a Kimi K3.1 diagnostic
correctly recognized explicit-only registration but guessed an unverified
`/gzs-git-sync` command. Native command discovery listed only `init` and
`review`. Official OpenCode skill guidance documents `@skill-id`.

Supplying that actual host evidence produced the correct `@gzs-git-sync`
recommendation and remote-effects warning without invoking the workflow.
The router already instructs agents to use observed syntax or a discovery
step. Any future correction should demonstrate a reusable discovery/verification
improvement, not repeat ineffective prompt hardening or weaken privacy policy.
Read the exact failed and successful sessions in the follow-up and JSON first.

The next queued catalog review is `gzs-git-sync`; the broader backlog is in the
roadmap. Do not duplicate it here. The heavy integration, MPAS adaptations and
repository-baseline proposal remain proposals; SP-BP work stays in SP-BP.

## Verification and authority

Most recent checks on the documentation-only final state: all 12 repository
contract tests pass; `git diff --check` passes; evidence JSON parses and the
saved-default smoke contains a real router skill load. Earlier complete
28-test and 20-skill validation runs passed. No tests were added to mirror prose.

Useful local commands:

```powershell
git status --short
git diff --stat
git diff --check
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_repository_contract.py -v
```

The `.venv` interpreter is Python 3.13.15; system `python` may select 3.14.
Tests involving temporary files or Node subprocesses can require sandbox
escalation. `uv` uses a protected cache at `U:\packages\uv`; use normal approval
review for required cache access instead of treating access failures as defects.

Explicit user authority already exercised: issue #1 closure; v0.8.1 commit,
push, tag and release; native Claude/Codex/OpenCode validation with repository
skill payloads sent to their configured model services; setting the tested
OpenCode model as the local default. Earlier Claude payload approval rejection
was resolved by the user's explicit authorization and reauthentication.

Those actions do not grant blanket permission for subsequent releases,
consumer propagation or unrelated remote mutation. The current request is a
handoff. No commit/push/release of the latest six paths or this handoff has
been requested. Preserve them until authorized. GitHub's connector lacked
issue-write permission; authenticated `gh` successfully performed the authorized
closure. No need to repeat closed issue work.

Suggested next-session disciplines: `gzs-session-handoff` to resume;
`gzs-intent-audit` for the remaining invocation claim, or `gzs-git-sync` only
when the user authorizes committing/pushing the documentation.
