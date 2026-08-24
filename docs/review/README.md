# One-by-one skill review

This queue reviews each promoted skill as a product interface before the first
stable release. Review the skill body, activation boundary, provenance,
portability, side effects, and behavioral scenarios; do not batch-approve the
catalog from structural validation alone.

| Order | Skill | Review status | Why this position |
| ---: | --- | --- | --- |
| 1 | [`gzs-router`](../../skills/gzs-router/SKILL.md) | Pending | Establishes the catalog map and review vocabulary. |
| 2 | [`gzs-git-sync`](../../skills/gzs-git-sync/SKILL.md) | Pending | Highest-risk remote mutation and explicit-invocation boundary. |
| 3 | [`gzs-update-dependencies`](../../skills/gzs-update-dependencies/SKILL.md) | Pending | One of the motivating workflows and the broadest maintenance surface. |
| 4 | [`gzs-quality-gate`](../../skills/gzs-quality-gate/SKILL.md) | Pending | Shared completion contract used by other workflows. |
| 5 | [`gzs-repository-hygiene`](../../skills/gzs-repository-hygiene/SKILL.md) | Pending | Includes conditional cleanup authority and artifact classification. |
| 6 | [`gzs-session-handoff`](../../skills/gzs-session-handoff/SKILL.md) | Pending | Explicit continuity workflow with durable artifact choices. |
| 7 | [`gzs-agent-context-diet`](../../skills/gzs-agent-context-diet/SKILL.md) | Pending | Changes persistent agent context and generated surfaces. |
| 8 | [`gzs-plan-audit`](../../skills/gzs-plan-audit/SKILL.md) | Pending | Defines pre-implementation alignment evidence. |
| 9 | [`gzs-intent-audit`](../../skills/gzs-intent-audit/SKILL.md) | Pending | Defines post-delivery fulfillment evidence. |
| 10 | [`gzs-tech-debt-review`](../../skills/gzs-tech-debt-review/SKILL.md) | Pending | Must distinguish evidenced risk from preference. |
| 11 | [`gzs-cross-platform-python`](../../skills/gzs-cross-platform-python/SKILL.md) | Pending | Narrower Python-specific portability discipline. |

For each review, record:

1. Keep, revise, incubate, or remove.
2. User-invoked or model-invoked.
3. Positive and negative trigger examples.
4. Project-independent invariant and project-owned adapter points.
5. Mutation, authorization, and stopping boundaries.
6. A no-skill baseline and with-skill behavioral scenario.
7. Observable completion evidence.

The next review is `gzs-router`.
