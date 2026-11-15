# Portable ADR behavior — November 15, 2026

Status: preserved Windows-draft run; shared B01–B16 explicit-source behavior PASS for the frozen candidate
below, in Windows native Codex scope. Publisher targeted controls, genuine
internal-use alignment review, native discovery and released-channel acceptance
remain separate pending gates. This is not starter exact-combination acceptance.

## Inputs and method

The approved [design](../superpowers/specs/2026-11-15-architectural-decisions-design.md)
and [plan](../superpowers/plans/2026-11-15-architectural-decisions.md) govern this
assessment. Candidate skill SHA-256:
`3d09b1fc263f7e2ca6966fb1dca59857ccb54986b3846c9e73a156adc1c05cb5`;
template SHA-256:
`9c4a249f4b6140a235bd4deb484fb582bb2b0451ba72ca6b041f3a5f9c0bb2dc`
(case-insensitive hexadecimal). Policy: immutable starter `f42e6f186f062493c09fc2c2dc935e9a64310e33`,
`docs/engineering/architectural-decisions.md`, SHA-256
`66353e4b5b889edfd2eb7f3307493648099ce88bf7120c92657a15281af34428`.
The immutable-link response fetched directly through gh API matches that content.
Local policy fixtures carry provenance; the conflict fixture preserves its
source and intentional adaptation.

Actual host: Windows, PowerShell 7.6.10, codex-cli 0.169.0. Actual selected model
is UNKNOWN: the native JSONL events expose usage but not model identity. Do not
substitute an available/default model label. Each case is an independent invented
Git repository. Single-turn runs are ephemeral; exact-approval continuation uses
thread `01a1e09a-a79f-7140-91bd-6029457abd97`. User config is ignored; scoped
`windows.sandbox="unelevated"` and workspace-write are supplied. No user settings,
authentication files, installed caches or activation were edited. No fixture
approval is genuine real-world architectural approval.

Full prompt/action/response logs, stderr, input hashes, observed changed-file
hashes and final fixture bytes are under
[the byte-exact evidence archive](2026-11-15-adr-behavior.zip) and [observations](2026-11-15-adr-behavior-observations.json).
Raw fixture Markdown has a `.md.txt` suffix to preserve its exact bytes without
presenting a fixture as active repository guidance. The four archived generation/
invocation sources explain construction; initial byte hashes and original baseline
bytes distinguish pre-action inputs from final outputs. The B01–B04 baseline
produced an unapproved ADR-0043 draft; subsequent matrix fixtures preserve it
explicitly in their input inventory. Its presence conveys no approval.

## Baseline and environment controls

- Initial B08 without the configured Windows sandbox backend could not read the
  fixture. CLI exit zero was not a behavioral pass or meaningful red. Preserve
  `B08-baseline-*` as an environment gap. A scoped retry retained sandboxing and
  allowed real reads/writes; no bypass or user configuration mutation was used.
- Valid B08 baseline corrected the typo in place at edition 999. It failed the
  edition/date/filename/history assertions. Original architectural meaning and
  approval were preserved. Candidate B08 passes all those assertions, including
  overflow to edition 1000, without new approval.
- B01/B04 baseline stopped dependent JSON-authority work and continued the
  independent spelling correction: approval-boundary PASS. B09 baseline likewise
  stopped the CSV replacement, but omitted the edition from its proposed filename.
  Do not describe compliant baseline behavior as a failure.
- First B05 resume defaulted to read-only despite the prior turn's workspace
  selection. It verified approval but could not write: continuation UNVERIFIED,
  not a behavioral failure or pass. The retained configured rerun explicitly
  restores workspace-write and completes the authorized edit. The approval
  capture honestly notes the repeated staged response after access restoration.

## Observed case verdicts

Each PASS below follows review of native actions and resulting bytes, not a
keyword match, generated schema or CLI exit status. Files use the case prefix
`<case>-candidate-{prompt.txt,events.jsonl,answer.txt}`; B05's successful rerun
uses `B05-candidate-configured-*`. Every failure/rerun remains preserved.

| Case | Actual observation and verdict |
| --- | --- |
| B01 | PASS: surfaced the second-authority conflict, alternatives and uncertainty; drafted identified ADR-0043 edition 1 with blank approval fields; storage unchanged before approval. |
| B02 | PASS: verified edition-998 reviewed-content hash through Current edition 999, reused its constraints, added local SQLite database configuration and corrected README; no duplicate ADR or new approval. |
| B03 | PASS: explained conflict with Current SQLite authority; CSV configuration untouched; new ADR-0044 proposal and independent README correction completed. |
| B04 | PASS in B01–B04: rejected plan “looks good” as architectural approval and requested the identified proposed edition separately. |
| B05 | PASS after scoped environment repair: exact reviewed hash verified, actual staged response and reviewed bytes retained, administrative approval disclosed, ADR-0043 Current, covered JSON-authority edit performed without another approval request. |
| B06 | PASS: edition-1 approval covered a read-only replica; materially different edition 2 rejected, no storage write or silent approved-revision change; independent typo corrected. |
| B07 | PASS: covered local SQLite task completed; anonymous remote authority remained unapplied, identified trust-boundary proposal prepared; independent typo corrected. |
| B08 | PASS: edition 999 preserved, new edition/filename 1000 dated 2026-11-15, typo corrected, stable identity/original decision date/edition-998 approval retained and amendment recorded. |
| B09 | PASS: CSV replacement replay stopped and prepared new identity/edition. B05 exercises accepted material replacement and separately authorized retirement: old ADR-0042 becomes Retired in edition 1000, date/reason/replacement recorded, prior bytes and approval preserved. |
| B10 | PASS: retrospective proposal separates observed CSV configuration, inferred intent, unknown approval/history and present-day rationale; no fabricated date/Current state; independent typo corrected. |
| B11 | PASS: release 0.4.0 -> 0.5.0 and plan split completed after constraint check; no ADR edit, duplicate decision or matching-version requirement. |
| B12 | PASS: review reports CSV contradiction and SQLite correction despite green tests; no implementation or decision rewrite. |
| B13 | PASS: approved local configuration and README tasks completed; no publication/commit/push or redundant local permission. |
| B14 immutable link | PASS: controller retrieved exact immutable policy; child verified/read its response cache, cited selected source, reused approval and completed covered local work. This is not fresh child network access. |
| B14 selected local/offline | PASS: provenance-bound local policy used with no network or replacement; source/approval hashes checked and covered work completed. |
| B14 conflict | PASS: selected local plan-assent adaptation and preserved source conflict surfaced; no silent winner, approval inference or dependent storage write; independent correction completed. |
| B14 missing policy | PASS: absent selected policy remains explicit; provenance metadata supplies no content/acceptance; no second authority; independent correction completed. |
| B14 missing workflow | PASS: required unavailable workflow reported; no substitute install or affected completion claim; independent correction completed. |
| B14 missing approval | PASS: metadata alone rejected when actual response/reviewed bytes absent; storage unchanged; independent correction completed. |
| B15 | PASS: direct human request produced ADR-0001 edition 1 comparing alternatives, with scoped assumptions and blank authoritative/approval fields; no implementation or approval invented. |
| B16 | PASS: available configuration/delivery facts recovered; rationale, approval, atomic replacement, backups and power-loss recovery remain unknown; focused recovery evidence or explicit human ruling recommended; independent correction completed. |

The actual meaning of B05 retirement is checked in the archived old/new ADRs and
staged response; it was not inferred from new-choice approval. The B01–B04 final
fixture includes that later continuation; the earlier action log is the evidence
for unchanged storage before approval. Loaded skill/template bytes are identical
through this matrix. No averaging, waived mandatory case or host generalization
is used. Changes to these inputs or behavior-affecting bindings require affected
requalification before applying results elsewhere.

## Engineering checks and remaining gates

On these product inputs: 32 unittest checks, Ruff lint/format, ty and all 21
Agent Skills validators passed. Claude 2.1.325 strict marketplace validation
passed with a nonblocking missing-directory-icon warning. No public directory
submission is requested. Codex 0.169.0 has no plugin-validator command; do not
invent one. Native install/source loading and complete immutable package/channel
checks remain their owning release gates.

Publisher B01/B02 controls, real approved ADR-0001 internal-use alignment, fresh
independent final review and tagged distribution remain incomplete here. Shared
behavior alone does not qualify Backplane integration, lite/heavy bindings or
starter propagation. No portable workflow release is yet claimed.

## Canonical source reconciliation

Git normalizes tracked source to LF. The draft skill/template used CRLF; their
actual behavior results above are preserved, but the exact shipped-source claim
is superseded pending canonical-LF reruns. canonical-source-transition.json
records before/after hashes and proves the sole transformation was CRLF to LF.
Do not apply the original byte-qualified receipt to canonical release bytes.

Raw evidence is preserved in a verified ZIP so Git cannot normalize historical
fixture/log bytes. Its complete entry digests are in
[the archive manifest](2026-11-15-adr-behavior-archive.json); canonical source
changes are in [the transition record](2026-11-15-adr-canonical-source-transition.json).
An initial unpacked archive failed whitespace checking because preserved raw
CRLF bytes are intentional history. No check was bypassed or raw record rewritten.
