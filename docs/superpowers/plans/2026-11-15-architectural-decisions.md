# Architectural Decisions Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the portable ADR procedure/template and evidenced gz-skills binding required by the starter's approved ADR contract.

**Architecture:** Add one project-governed supporting skill, its template and existing router integration. Consumers retain policy, lifecycle and operation authority; decision approval remains separate from design, plan and delivery approval.

**Tech Stack:** Agent Skills Markdown/YAML, existing native adapters, existing uv-managed Python validation/package tooling; no new runtime dependency.

**Spec:** [Owning design](../specs/2026-11-15-architectural-decisions-design.md) and [Current ADR-0001 edition 1](../../decisions/ADR-0001-001-standalone-architectural-decision-procedure.md), including its separate actual approval and preserved original bytes.

**Status:** APPROVED for Native execution; actual main-conversation approval is captured below. This document does not approve changed ADR bytes. Use **Native execution** through `superpowers:executing-plans`: three sequential tasks share one cohesive instruction contract; use one fresh final reviewer. Preserve an execution choice the maintainer actually supplies.

## Global Constraints

- Preserve original dirty checkout and user settings; use the registered detached worktree based on `4a7abd79f483c6c9abfc8f9470694be847f1347d` until deliberate main integration.
- Starter authority: `f42e6f186f062493c09fc2c2dc935e9a64310e33`; COB source: `dd1ab883c04e884678ed723959b17c5c364263d1`; naming precedent: GZKit `8208381d149b8b8704bd012849332ed3a1f2fb38`, classic-ADR change order/H5. This is provenance, not GZKit integration.
- Stable identity `ADR-[0-9]{4,}`; filename `ADR-[0-9]{4,}-[0-9]{3,}-<slug>.md`; slug `[a-z0-9-]+`. Widths are minimums, with no cap/overflow rename. Preserve suitable existing conventions through explicit semantic mapping.
- No ledger, service, CLI/schema extension, starter runtime prerequisite, SP fork, Backplane activation or new consumer lifecycle. No global/user activation or background plugin installation.
- Baseline bundle 0.12.0 -> proposed 0.13.0; new skill 0.1.0; router 0.6.0 -> 0.7.0. No stable promotion or major; all other skill trees stay unchanged.
- Use current project-managed tools, locked execution and managed Python 3.14.10; uv >=0.13.5 is compatibility policy. Reconcile any authorized release-time freshness migration through its owner.
- Plain transcripts and existing evidence/review records suffice. Add no evaluation-controller framework without a repeated demonstrated need. Invent fixtures, never approval history.

## Review Focus

- Changed naming text versus original approved bytes: Task 1 must preserve and reconcile approval applicability before dependent work.
- Editorial edition overflow/legacy naming versus material replacement: Task 1 pressure cases and Task 2 B08/B09 must prove the distinction without renaming legacy collections.
- Policy/source available while approval or skill content is unavailable: Task 2 B14 must withhold affected claims and continue independent work.
- Native catalog presence versus actual loaded procedure/model action: Task 2 discovery probes and transcripts must prove both separately.
- Publication or repeated permission accidentally inferred from ADR approval: Task 2 B02/B05/B13 must show correct continuation and preserved operation authority.

---

### Task 1: Deliver the approved portable procedure and publisher binding

**Files:** Create `skills/gzs-architectural-decisions/{SKILL.md,references/adr-template.md,agents/openai.yaml}`; modify `skills/gzs-router/{SKILL.md,references/workflows.md}`, `AGENTS.md`, `README.md`, `.claude-plugin/plugin.json`, `docs/{origins.md,roadmap.md,release-policy.md}`, `docs/review/README.md`, `CHANGELOG.md`, `pyproject.toml`, `.codex-plugin/plugin.json`, `package.json`, `src/gz_skills/__init__.py`, and owning-tool-generated `uv.lock`. Validate existing approval/history at `docs/decisions/ADR-0001-001-standalone-architectural-decision-procedure.md` and `docs/decisions/approvals/{ADR-0001-001-approval.md,ADR-0001-001-reviewed.txt}`; preserve their exact approval provenance. Evidence: `docs/review/architectural-decisions-2026-11-15.md` and its adjacent evidence directory.

**Interfaces:** Consumes approved design plus separately evidenced applicable architectural approval. Produces the three canonical skill resources, router integration, mandatory gz-skills binding, consistent candidate metadata and frozen source hashes for Task 2. No Python API changes.

- [ ] **1. Validate actual approvals and reuse the Current decision.** Read the existing Current ADR, actual-approval capture and preserved reviewed bytes identified above. Run `Get-FileHash docs/decisions/approvals/ADR-0001-001-reviewed.txt -Algorithm SHA256`; expect `807749ec03853e673b4f2f431cf3c5b277615fedf9dd552016d98b655e72d7ff`, matching original proposal at `f847de530acb3e1ef0716b18b09a2ea48c2fdcae`. Confirm the capture preserves the actual separate response “Approve gz-skills ADR-0001 edition 1 as written”, named edition/content, human identity/date, side-prompt source context and honest agent-transcription labeling. Distinguish original design approval and later “proceed with that design” from architectural approval. Compare the Current record against original bytes: administrative fields/status/links changed, architecture unchanged; later naming clarification remains design-attributed. Reuse this applicable approved decision without another ADR or redundant approval request. Report only a demonstrated content/provenance mismatch as a gap before dependent work; do not fabricate or infer replacement approval. Implementation still requires review of this plan.
- [ ] **2. Run bounded pre-skill pressure scenarios.** Create invented isolated fixture repositories and prompts for B01 missing approval with a vague plan assent (B04), B08 typo/edition transition including overflow and suitable legacy naming, and B09 changed source-of-truth choice/retirement. Run the existing instructions without the proposed skill; retain all actual outputs/actions and baseline verdicts. An observed failure establishes the regression to fix; passing baselines remain passes, never fabricated failures. Preserve source hashes and operator turns for exact reruns.
- [ ] **3. Author the three canonical resources.** Implement every design behavior: discovery floor/project authority, recognition/reuse/alignment, exact-edition explicit approval, independent continuation, honest evidence/backfill, editorial/material/retirement distinction, independent lifecycles and both policy-access forms. Put the full self-contained fields/content/provenance/history in the template, with unfilled draft approval fields and no authoritative draft state. Explain mapping for existing forms. Apply the naming grammar above, not a stricter parser. Metadata: skill 0.1.0, GovZero Architectural Decisions, explicit skill-naming prompt, implicit invocation allowed. No scripts or extra runtime.
- [ ] **4. Integrate routing, binding and release scope.** Add the skill to existing router/catalog and guide at design/execution/review without restarting an active workflow; router 0.7.0. Bind AGENTS.md to the immutable starter policy, actual `docs/decisions/` collection and canonical skill path. Update dynamic catalog claims to twenty-one and Claude's explicit list; retain historical twenty-skill evidence. Record provenance, individual review status and finite 0.13.0 scope/remaining gates in existing authorities. Synchronize the four bundle mirrors plus source version fallback; regenerate lock metadata through `uv lock`, then `uv lock --check`. Do not hand-edit lock resolution or advance marketplace refs before release preparation.
- [ ] **5. Run structural checks and replay pressure cases.** `uv run --locked python -m unittest discover -s tests -p test_repository_contract.py -v`; `uv run --locked agentskills validate skills/gzs-architectural-decisions`; `uv run --locked agentskills validate skills/gzs-router`; `git diff --check`. Expect zero failures, canonical names/prompts/links/versions/catalog coverage and discovery floor. Replay Step 2 using exact candidate sources; compare actions semantically. Add a deterministic regression only for a demonstrated public packaging/discovery defect, not instruction-keyword mirrors.
- [ ] **6. Freeze Task 2 inputs.** Record full base SHA plus dirty-candidate hashes, independent versions and all regular files of both changed skill trees. Use `Get-FileHash -Algorithm SHA256` for files; the existing complete-tree algorithm in `scripts/inventory_skills.py:skill_tree_sha256` owns tree identity. Include policy/template/fixtures/binding hashes and actual commands. Reject mixed-input evidence; no self-referential commit hash.

### Task 2: Qualify actual behavior, discovery and genuine internal use

**Files:** Complete `docs/review/architectural-decisions-2026-11-15.md` with durable fixture/prompt/transcript/action artifacts under `docs/review/architectural-decisions-2026-11-15/`; update existing roadmap/evidence and owning ADR alignment record. Correct only Task 1's affected instruction files when observed failures justify it.

**Interfaces:** Consumes frozen Task 1 sources. Produces case-to-evidence verdicts for B01-B16/B14 subcases, loaded-source/native metadata, gz-skills binding controls, genuine internal-use alignment review and clearly scoped UNKNOWNs for release/starter qualification.

- [ ] **1. Prepare exact-source execution and rubric.** Make one isolated fixture per case; preserve complete authority/ADR content and prompt bytes. Use direct Codex CLI, whose observed 0.169 interface supports JSONL and resumed turns; record `codex --version` and `codex exec --help` at execution. Do not override the default model; observe resolved model/settings/session metadata, or mark unavailable fields UNKNOWN. Preserve actual loaded policy/procedure/template, native scope, tool actions, operator responses, final files/diffs and reviewer decisions. Avoid unrelated user settings/secrets in receipts.

```powershell
Get-Content -Raw -LiteralPath <prompt-file> | codex exec --ignore-user-config --json --sandbox workspace-write --cd <fixture-root> --output-last-message <answer-file> - 1> <events.jsonl> 2> <stderr.txt>
Get-Content -Raw -LiteralPath <operator-turn-file> | codex exec resume --ignore-user-config --json <observed-session-id> - 1> <continuation.jsonl> 2> <continuation-stderr.txt>
```

Use fresh sessions between cases and the observed session id within a multi-turn case. Keep user configuration out of fixture runs with the supported child invocation flag above, while reusing existing authentication without copying credentials or editing normal settings. Do not use ephemeral mode for a session that must later resume; preserve its exact scoped session identity. Native installation acceptance uses a separately supported isolated scope and must never silently fall back to a normal profile. Constrain fixture tasks to their workspace; preserve normal sandbox/approval controls. A run that cannot execute/resume or load identified inputs is unverified, not PASS. Manually supplied procedure text proves behavior only; native discovery requires a separate fresh-process observation.

- [ ] **2. Run the complete shared matrix.** Apply the exact starter specification's B01-B16 setup/verdicts, with post-approval continuation and independent tasks where specified. Record separate B14 runs for immutable link, selected provenance-bound offline local copy, local/source conflict, missing policy, missing procedure/template and unreadable approval. Exercise identity/edition overflow and existing-convention mapping in B08/B09 alongside ordinary cases. Fictional operator approval is fixture input. Inspect actual file/tool actions: no dependent writes before required approval; genuine reuse/continuation without duplicate ADRs/redundant permission; no unsupported authority/history. Green shell exit or matching keywords cannot establish these results.
- [ ] **3. Resolve failures honestly.** Preserve failed transcripts and precise violated invariant. Correct only implicated source/binding, freeze new hashes and rerun every affected case/control; broaden when shared-behavior applicability is uncertain. Every mandatory case must pass; do not average away failures. Retain untested platforms/model metadata as explicit limits and distinguish qualified inputs from earlier runs.
- [ ] **4. Exercise the actual publisher binding and fresh native discovery.** In supported isolated project configuration, demonstrate the candidate skill/template loaded in a new native process at the intended source and scope. Exercise actual gz-skills design, execution and review checkpoints plus B01 stop/B02 continue controls with its binding. Preserve installed/resource identities separately from source selection and actual inference. Do not modify real user activation, run unscoped plugin add, or infer heavy readiness. Record unsupported host behavior as unverified.
- [ ] **5. Record genuine internal use and alignment.** Use this contribution's real approved/reused owning ADR during authorized implementation, cite its exact edition/evidence, then review implemented ownership/dependencies/history against it. Preserve which behavior actually occurred. Invented runs cannot replace this record. Map shared-result applicability and hand off exact evidence needed by starter and SP-BP owners for their own targeted bindings, lite/heavy disabled paths and supported active integration; do not assert their acceptance here.

### Task 3: Complete owning release gates and hand off the immutable contribution

**Files:** Existing release preparation/roadmap/handoff plus `docs/evidence/2026-11-15-0.13.0-release.md`; finalize CHANGELOG.md, current examples and `.agents/plugins/marketplace.json`/`.claude-plugin/marketplace.json` only when publication preparation is authorized. Artifacts: `dist/release-0.13.0/{first,second,direct}` and `SHA256SUMS-0.13.0.txt`.

**Interfaces:** Consumes accepted source/behavior/binding/internal-use evidence. Produces independently released immutable source, artifacts/checksums, observed channel acceptance and source-bound starter handoff. A push, tag or installation alone does not fulfill combined-stack acceptance.

- [ ] **1. Recheck authority, live state and finite scope.** Review current starter consistency, actual publication authorization, latest released tag, remote divergence and original dirty files before integration. Complete required release-time dependency/tool freshness maintenance through its owner with dated official evidence and owned exceptions, preserving Python-family policy. Reconcile only approved scope on main; preserve unrelated changes and normal hooks, no destructive reset/force push. Record baseline 0.12.0 -> target 0.13.0, governing work, compatibility and all mirrors. Do not claim release readiness with unresolved mandatory approval or behavioral evidence.
- [ ] **2. Run the owning full gate on actual candidate inputs.** Use README/package commands below; `uv sync --locked` is required when environment state needs reconciliation. Validate every canonical skill; twenty-one expected, with dynamic resource count from actual source. Run `claude plugin validate . --strict` and `claude plugin validate .claude-plugin/marketplace.json --strict`. Codex 0.169 has no `plugin validate` subcommand: record actual supported native parser/discovery/install checks rather than inventing one. Perform preceding v0.12.0 HTTPS marketplace smoke tests in disposable isolated configurations before candidate tagging, as packaging requires.

```powershell
uv sync --locked
uv run --locked python -m unittest discover -s tests -v
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked ty check
uv lock --check
Get-ChildItem .\skills -Directory | ForEach-Object { uv run --locked agentskills validate $_.FullName }
git diff --check
uv build --no-sources --out-dir dist/release-0.13.0/first
uv build --no-sources --out-dir dist/release-0.13.0/second
uv build --no-sources --wheel --out-dir dist/release-0.13.0/direct
uv run --locked python scripts/check_package.py --artifacts dist/release-0.13.0
```

Expect every required command to pass. The existing package checker must report version 0.13.0, 21 skills, canonical resource/hash equality, byte-identical repeated archives/direct wheel and clean external installed CLI/provenance/local-edit protection. If a tool/runtime migration changes its hardcoded Python input, reconcile that demonstrated consumer through owning maintenance and rerun affected checks; do not bypass it.

- [ ] **3. Finalize and validate the clean release commit.** Date the 0.13.0 changelog, add fresh Unreleased, update current refs/examples and preserve history. Commit only reviewed scope with normal hooks; rerun applicable clean-commit gate/artifact checks required by packaging. Record wheel/sdist SHA-256 from `Get-FileHash`; write checksum asset and exact commands/logs. Confirm task-source hashes match qualified inputs or repeat affected qualification. Obtain one fresh final semantic review of the complete change and close material findings.
- [ ] **4. Publish and verify under preserved authority.** Follow `docs/packaging.md#publish-a-bundle`: annotated immutable v0.13.0 tag on the validated commit with artifact digests; ordinary main/tag push; GitHub Release with wheel/sdist/checksum assets. Use direct git/gh, body files for multiline notes. Verify remote main/tag SHA and downloaded asset hashes; inspect exact-commit CI if configured, otherwise report unavailable. Never move a published tag or claim publication from version strings.
- [ ] **5. Observe all tagged channels and fresh sources.** Verify Codex and Claude HTTPS marketplace installs, OpenCode per-project Git package, and `uvx --from git+https://github.com/tvproductions/gz-skills.git@v0.13.0 gz-skills install --all --project <disposable-consumer>`. Use explicitly isolated disposable homes/project scopes for host acceptance; no real user/global activation. Confirm 21 skills, every canonical resource/hash, full immutable provenance and packaged template access. Record actual native commands, loaded scope and limitations; public-directory/registry publication and existing-consumer propagation remain separate. Recheck relevant behavior against unchanged published bytes; changed inputs require affected reruns.
- [ ] **6. Close owning scope and hand off.** Record release URL/tag/source SHA/artifact hashes, skill/template/router identities, approvals, full shared matrix, native/binding/internal-use evidence and remaining UNKNOWNs in existing authorities. Recheck remaining worktree/local-remote alignment. Give the starter owner exact immutable inputs; it still must obtain other publisher/internal-use/integration evidence and qualify its actual combination before starter 0.10.0 publication/propagation. No synchronized component versions, automatic consumer update or endless receipt-only commit chain.

## Plan self-review and execution handoff

Self-review: Task 1 covers ownership, naming/source provenance, all procedure/template semantics, metadata/catalogs and finite versions; Task 2 covers the complete shared matrix, native source distinctions, publisher controls and real use; Task 3 covers release tooling/artifacts/channels and exact starter handoff. The five Review Focus risks have explicit Task 1/2 checks. No new function/API/type or evaluation framework is introduced. External companion/adopter results remain owning prerequisites, not work silently claimed by this plan. Execution-time model/native capabilities, approval applicability and fresh release state must be observed; no evidence is invented now.

Review this plan in the main conversation before execution. Native execution is recommended for its cohesive sequential work; preserve the maintainer's actual choice and current authority. Design assent does not approve this unwritten plan retrospectively, and plan assent does not create architectural approval.

## Execution approval — November 15, 2026

The maintainer approved this plan in the main conversation, responding
“approve, are we sure "native" is the best term?” to the review of the immutable
plan at `32a6673a34a5e06d502e5bdf9f953f59c85489f0`. Subsequent discussion confirmed retaining Superpowers'
**Native** label rather than contradicting its owning skill; the maintainer
then directed “so, we'll just move on”. Native means the controller implements
in this session, with one fresh independent final review. No duplicate plan or
architectural approval is requested. Original reviewed plan bytes remain in
that immutable Git history; this section is administrative execution capture.

## Execution checkpoint — November 15, 2026

Task 1 source/catalog/binding implementation is present; the exact canonical
procedure/template bytes are now LF under repository attributes. Existing Current
ADR-0001 edition 1 and separate actual approval were reused without changing their
bytes. No runtime, service, lifecycle or setup schema was added. Source gates:
32 unittest checks, Ruff lint/format, ty, 21 Agent Skills validators and strict
Claude validation PASS (nonblocking directory-icon warning).

The first shared B01-B16 Windows-draft behavior run passed, preserving a genuine
B08 baseline gap and two environment failures/reruns. Git byte reconciliation
found CRLF draft versus LF release bytes. The canonical-source transition is
newline-only; exact-source reruns are in progress and remain a release gate.
See [preserved behavior evidence](../../evidence/2026-11-15-adr-behavior.md).
Task 2 remains active; Task 3 publication has not started. Existing release target
0.13.0 is unchanged. Native candidate discovery and publisher controls do not
substitute for immutable tagged-channel acceptance or genuine alignment review.
