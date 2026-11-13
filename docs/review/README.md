# One-by-one skill review

This queue reviews each promoted skill as a product interface before the first
stable release. Review the skill body, activation boundary, provenance,
portability, side effects, and behavioral scenarios; do not batch-approve the
catalog from structural validation alone.

This table covers all twenty implemented skills as of 2026-10-25. The current
backlog and historical promotion record are in [`docs/roadmap.md`](../roadmap.md).
Pending means stable-contract acceptance has not been recorded; a release or
structural validation alone does not complete that review. The release primitive
is the latest implemented addition; see its
[initial behavioral review](gzs-release-2026-10-11.md).

| Order | Skill | Review status | Why this position |
| ---: | --- | --- | --- |
| 1 | [`gzs-router`](../../skills/gzs-router/SKILL.md) | Native inference verified; invocation robustness pending ([follow-up](gzs-router-2026-10-25-opencode-followup.md)) | Claude/Codex checks and OpenCode 2.1.4 inference pass in the tested configuration; review ungrounded user-syntax claims before stable acceptance. |
| 2 | [`gzs-git-sync`](../../skills/gzs-git-sync/SKILL.md) | Stable contract accepted ([decision](gzs-git-sync-2026-10-25-acceptance.md)) | The unchanged 0.1.1 contract passed the bounded native execution matrix and is promoted to 1.0.0; all three harnesses revalidated after rebase and preserved project approval authority. |
| 3 | [`gzs-update-dependencies`](../../skills/gzs-update-dependencies/SKILL.md) | Initial review complete: keep corrected 0.4.1; stable acceptance pending ([review](gzs-update-dependencies-2026-11-08.md)) | The initial finding is closed in 0.4.1, released with bundle 0.10.0. Collect native baseline and execution evidence next; the skill works standalone. |
| 4 | [`gzs-quality-gate`](../../skills/gzs-quality-gate/SKILL.md) | Pending | Shared completion contract used by other workflows. |
| 5 | [`gzs-repository-hygiene`](../../skills/gzs-repository-hygiene/SKILL.md) | Pending | Includes conditional cleanup authority and artifact classification. |
| 6 | [`gzs-session-handoff`](../../skills/gzs-session-handoff/SKILL.md) | Pending | Explicit continuity workflow with durable artifact choices. |
| 7 | [`gzs-agent-context-diet`](../../skills/gzs-agent-context-diet/SKILL.md) | Pending | Changes persistent agent context and generated surfaces. |
| 8 | [`gzs-plan-audit`](../../skills/gzs-plan-audit/SKILL.md) | Pending | Defines pre-implementation alignment evidence. |
| 9 | [`gzs-intent-audit`](../../skills/gzs-intent-audit/SKILL.md) | Pending | Defines post-delivery fulfillment evidence. |
| 10 | [`gzs-tech-debt-review`](../../skills/gzs-tech-debt-review/SKILL.md) | Pending | Must distinguish evidenced risk from preference. |
| 11 | [`gzs-cross-platform-python`](../../skills/gzs-cross-platform-python/SKILL.md) | Pending | Narrower Python-specific portability discipline. |
| 12 | [`gzs-root-cause-debugging`](../../skills/gzs-root-cause-debugging/SKILL.md) | Pending | First horizontal primitive explicitly composed beneath project-owned workflows. |
| 13 | [`gzs-hexagonal-architecture-audit`](../../skills/gzs-hexagonal-architecture-audit/SKILL.md) | Pending | Read-only architecture analysis must remain helpful, language-aware, and distinct from plan and intent audits. |
| 14 | [`gzs-change-review`](../../skills/gzs-change-review/SKILL.md) | Pending | Must prioritize concrete defects without duplicating intent audit, debt review, or project-owned approval. |
| 15 | [`gzs-dependency-risk-audit`](../../skills/gzs-dependency-risk-audit/SKILL.md) | Pending | Current external evidence, private-package handling, and ecosystem differences need realistic review. |
| 16 | [`gzs-test-driven-change`](../../skills/gzs-test-driven-change/SKILL.md) | Pending | Explicit activation must preserve a meaningful red while adapting to difficult behavioral seams. |
| 17 | [`gzs-release`](../../skills/gzs-release/SKILL.md) | Pending stable-contract review | Version recommendations, publication authority and partial-release recovery require behavioral evidence. |
| 18 | [`gzs-project-setup`](../../skills/gzs-project-setup/SKILL.md) | Pending | Review first-use selection, preservation of settings, gzkit exclusion, promotion boundaries and honest heavy-readiness claims. |
| 19 | [`gzs-pythonic-pattern-detect`](../../skills/gzs-pythonic-pattern-detect/SKILL.md) | Pending | Review concrete candidate evidence, project-version policy and read-only scope without requiring an external scanner or corpus. |
| 20 | [`gzs-pythonic-pattern-apply`](../../skills/gzs-pythonic-pattern-apply/SKILL.md) | Pending | Review one authorized refactor with before/after behavior evidence, project-owned gates and preserved architecture boundaries. |

For each review, record:

1. Keep, revise, incubate, or remove.
2. User-invoked or model-invoked.
3. Positive and negative trigger examples.
4. Project-independent invariant and project-owned adapter points.
5. Mutation, authorization, and stopping boundaries.
6. A no-skill baseline and with-skill behavioral scenario.
7. Observable completion evidence.

The `gzs-git-sync` contract review is complete; `gzs-update-dependencies` now
has an initial review and portability correction and remains next for behavioral evidence.
The [pre-implementation applicability correction](gate-applicability-2026-11-13.md)
adds a bounded static case review for Git sync and quality gate; it does not
extend the historical native execution evidence or accept quality gate as stable.
The next skill without an initial review is `gzs-quality-gate`.
The router's provider blocker is
resolved; its remaining invocation-guidance finding precedes stable acceptance.
