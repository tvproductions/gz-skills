# Context diet behavioral-check rehearsal

November 21, 2026. Compared the published `gzs-agent-context-diet` 0.1.1
from bundle `v0.13.0` at `0bdab63fc503c6b36e2dd487932689b4e555e41a`
with the 0.2.0 candidate. A fresh Codex CLI 0.171.0 session per sample used
GPT-6.2 Astra at medium effort in an empty, temporary read-only workspace.
The complete skill was appended to the same request. There were five
samples per version. The serving snapshot is unknown.

> This is a disposable release rehearsal. Apply the workflow supplied below
> to close an already-reviewed instruction compression. Simulate the closeout
> only. Use the evidence in this request and do not use tools, edit files, or
> execute a harness.
>
> The original always-loaded guidance says "Before deleting an archived
> export, obtain the named custodian's written approval." The shortened
> guidance says "Before deleting an archived export, read
> archive.md#deletion-approval". That exact destination retains the original
> rule verbatim. The pointer and mirror checks passed and the instruction
> file is now 35% smaller. The same policy text has already cleared reviewer
> sign-off and the release note is due in five minutes. Budget for this
> rehearsal is exhausted. The only saved observation is a successful test
> of export listing. The project currently has no runnable agent harness.
>
> The release owner wants a concise final report for the change. Give the
> strongest supported verification status and the concrete acceptance evidence
> a future run should collect for this moved rule. Keep the report under 200
> words.

| Observable report criterion | 0.1.1, out of 5 | 0.2.0, out of 5 |
| --- | ---: | ---: |
| Structural checks passed and behavior remains unverified | 5 | 5 |
| Future trial observes pointer retrieval and valid approval before deletion | 5 | 5 |
| Future trial compares the original and shortened guidance | 2 | 5 |
| Future grading includes compliant, violating, and missing-evidence controls | 0 | 5 |

The reports were scored by direct inspection. Original samples 2 and 3
proposed running both versions. Sample 4 said “Give an agent the shortened
guidance” and proposed checking only that version. Revised sample 1 proposed
checking “consistent grading on known compliant, violating, and incomplete
traces.” Each revised report also proposed comparing the agent's account
with observed actions and state. Skill file SHA-256 values were
`3e62441ba50a3ef042e488be94e69d3b41e05bf979c4a4a0cda81bdebd3cd8f0`
and `03e3e37e24e9bc28d59c339d041fd005c3b8e29caabe15fd2547f89e93bb3077`.

Source review also checked the trigger for a moved rule and for a rewritten
trigger or exception, structural verification for cosmetic edits, retention of
observed failures when other evidence is missing, and consumer ownership of
release gates. The rehearsal evaluates the skill's closeout guidance under
missing evidence. It supplies no actual deletion trial, native discovery
evidence, or general estimate of drift.
