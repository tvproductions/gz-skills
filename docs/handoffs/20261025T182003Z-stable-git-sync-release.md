# Stable Git sync release handoff

Observed: 2026-10-25 18:20:03 UTC (13:20:03 America/Chicago).
Workspace: `U:\repos\agents\gz-skills`.

## Resume point

The requested version update and release are complete: bundle **v0.8.3**
publishes **gzs-git-sync 1.0.0** after its individual stable-contract acceptance.
This handoff is the final documentation save point and will be committed and
pushed after validation under the same explicit request. No release or sync
step should be repeated merely because a new session starts.

First permissible action on resume: inspect `git status --short`, the latest
commit, and the [review queue](../review/README.md). Expect a clean `main` whose
tip is the documentation commit containing this handoff, one descendant of the
immutable release commit below. Verify that expectation before acting. The next
unreviewed backlog item is **gzs-update-dependencies**; when the user requests
the next review, read its contract and provenance and establish behavioral
scenarios. Review completion requires observed evidence and a recorded decision.
Stop before unrequested fixes, consumer updates or another publication.

## Release identity and verification

- [Published v0.8.3](https://github.com/tvproductions/gz-skills/releases/tag/v0.8.3)
  is neither a draft nor a prerelease.
- Annotated immutable tag: `v0.8.3`.
- Release commit: `d6acc26e28ca1c4f43e5bb46d8973021d7d006c3`.
- At observation, `main` and the remote release tag resolved to that commit and
  the worktree was clean before creating this handoff. The subsequent handoff
  commit is intentionally outside the release tag and artifacts. Locate it with
  `git log -1 --format=fuller -- docs/handoffs/20261025T182003Z-stable-git-sync-release.md`.
- Bundle 0.8.3 is synchronized across all four manifests, source fallback and
  uv lock. Both marketplace manifests pin v0.8.3. Only Git sync's skill version
  changes, from 0.1.1 to 1.0.0; other skill versions are unchanged.
- An exact comparison with v0.8.2 proved the promoted skill differs only in
  `metadata.govzero-version`. Its body, activation and authorization are the
  same contract exercised by the acceptance sessions.
- GitHub had no open issues or PRs in the 2026-10-25 18:19 UTC check. Issue #1
  remains closed; this is a dated snapshot, not continuous tracker sync.

The corrected clean release commit passed Ruff lint/format, ty, all **28**
unittests, all **20** Agent Skills specification validations, offline lock
consistency and Claude strict plugin/marketplace validation. Wheel and source
archive match all **44** canonical skill files byte-for-byte. A preparation-time
encoding drift was caught by the metadata-only comparison, repaired before
tagging, and followed by a fresh clean-checkout gate/build. The discarded
unpublished candidate was not tagged or released.

Codex and Claude HTTPS installs of preceding v0.8.2 passed before tagging.
Tagged v0.8.3 verification passed separately:

- Codex repository marketplace: installed bundle 0.8.3; all twenty complete
  skill trees match the tagged source.
- Claude repository marketplace: installed bundle 0.8.3 through its HTTPS-pinned
  plugin source; all twenty complete skill trees match.
- Native OpenCode v2 Git package: all twenty skill bodies and activation flags
  match the tagged adapter contract.
- uvx snapshot: installed Git sync 1.0.0 and quality gate 0.1.2; its lock records
  the exact release commit above.

Downloaded published assets match these SHA-256 values:

```text
0dbaea90aa92ff6458000e5270cfe2a52e4d74befe0dc3494f28d48f6ec59166  govzero_skills-0.8.3-py3-none-any.whl
f2114a32f159bcda0d1d617c351998b69b3844d70e4de9abe53c087408bf2b93  govzero_skills-0.8.3.tar.gz
```

The release also includes `SHA256SUMS-0.8.3.txt`. No npm/PyPI publication,
universal plugin-directory listing or consumer propagation occurred. No separate
hosted exact-commit CI is configured as an additional required release gate;
the observed checks above ran locally on the clean release commit.

## Accepted contract and remaining backlog

The [Git sync acceptance decision](../review/gzs-git-sync-2026-10-25-acceptance.md)
and [sanitized evidence](../review/gzs-git-sync-2026-10-25-behavior.json) preserve
22 native sessions: 19 acceptance observations and three fixture limitations.
Codex exercised the broad edge-case matrix and baseline. Claude and OpenCode
also executed successful sync, post-rebase gate failure, project approval and
negative-request scenarios. All three reran the gate after a clean rebase and
withheld failing work. Preserve failed attempts and scope limitations; do not
describe this as universal model/OS certification.

The catalog itself remains pre-1.0. The router still has its independent
[invocation-guidance finding](../review/gzs-router-2026-10-25-opencode-followup.md#remaining-invocation-guidance-finding).
Its provider/privacy blocker is resolved and must not be reopened as pending.
The broader backlog and ownership are already in the [roadmap](../roadmap.md);
do not duplicate that planning narrative or treat proposals as implemented.

## Local state, tools and authorization

Use **uv exclusively** for Python execution and environment/dependency/build
management; use Ruff and ty through uv-managed tooling. Do not invoke Python or
the `.venv` interpreter directly. See [AGENTS.md](../../AGENTS.md).
Useful verification commands are `uv run python -m unittest discover -s tests -v`,
`uvx ruff check .`, `uvx ruff format --check .`, `uvx ty check`, and
`git diff --check`. Sandbox restrictions can block temp Git metadata, native
subprocesses and the protected uv cache; required escalation is an environment
access issue rather than evidence of a product failure.

OpenCode's nonsecret local config was rechecked at observation: model
`opencode-go/kimi-k3.1-pro`, `reasoningEffort: low`. The earlier user-authorized
default remains selected. This is machine-local state, not a catalog model
requirement. Credential stores and privacy policy were not modified.

Temporary evidence and installation scopes remain machine-local under
`C:\Users\Jeff\AppData\Local\Temp\gz-sync-acceptance-h52zijle` and
`C:\Users\Jeff\AppData\Local\Temp\gz-release-083-r38nep6p`. They may be
removed by normal temp cleanup. Repository evidence and GitHub release assets
are the durable sources; do not depend on raw temp logs or expose reasoning,
server passwords, credentials or provider headers.

The user's explicit request was: “do a version update, release, then handoff
and git sync.” It authorizes this release and final handoff commit/push, not
future releases or consumer propagation. Earlier native provider validation
authority persists for its scoped work. The handoff itself grants no new action.
Suggested next-session skills: `gzs-session-handoff` to verify resume state,
then `gzs-intent-audit` for the next authorized contract review.
