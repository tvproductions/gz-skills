# One-by-one skill review

This queue reviews each promoted skill as a product interface before the first
stable release. Review the skill body, activation boundary, provenance,
portability, side effects, and behavioral scenarios; do not batch-approve the
catalog from structural validation alone.

| Order | Skill | Review status | Why this position |
| ---: | --- | --- | --- |
| 1 | [`gz-skill-router`](../../skills/gz-skill-router/SKILL.md) | Pending | Establishes the catalog map and review vocabulary. |
| 2 | [`gz-git-sync`](../../skills/gz-git-sync/SKILL.md) | Pending | Highest-risk remote mutation and explicit-invocation boundary. |
| 3 | [`gz-update-dependencies`](../../skills/gz-update-dependencies/SKILL.md) | Pending | One of the motivating workflows and the broadest maintenance surface. |
| 4 | [`gz-quality-gate`](../../skills/gz-quality-gate/SKILL.md) | Pending | Shared completion contract used by other workflows. |
| 5 | [`gz-repository-hygiene`](../../skills/gz-repository-hygiene/SKILL.md) | Pending | Includes conditional cleanup authority and artifact classification. |
| 6 | [`gz-session-handoff`](../../skills/gz-session-handoff/SKILL.md) | Pending | Explicit continuity workflow with durable artifact choices. |
| 7 | [`gz-agent-context-diet`](../../skills/gz-agent-context-diet/SKILL.md) | Pending | Changes persistent agent context and generated surfaces. |
| 8 | [`gz-plan-audit`](../../skills/gz-plan-audit/SKILL.md) | Pending | Defines pre-implementation alignment evidence. |
| 9 | [`gz-intent-audit`](../../skills/gz-intent-audit/SKILL.md) | Pending | Defines post-delivery fulfillment evidence. |
| 10 | [`gz-tech-debt-review`](../../skills/gz-tech-debt-review/SKILL.md) | Pending | Must distinguish evidenced risk from preference. |
| 11 | [`gz-cross-platform-python`](../../skills/gz-cross-platform-python/SKILL.md) | Pending | Narrower Python-specific portability discipline. |

For each review, record:

1. Keep, revise, incubate, or remove.
2. User-invoked or model-invoked.
3. Positive and negative trigger examples.
4. Project-independent invariant and project-owned adapter points.
5. Mutation, authorization, and stopping boundaries.
6. A no-skill baseline and with-skill behavioral scenario.
7. Observable completion evidence.

The next review is `gz-skill-router`.
