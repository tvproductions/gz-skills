# gz-skills agent guidance

Build this repository as the canonical, vendor-neutral library of portable
GovZero skills.

## Source and boundary

- Author skills only under `skills/<skill-name>/`.
- Keep project-specific commands, paths, versions, branch names, and governance
  ceremonies in the consuming project.
- Preserve the invariant and completion criteria shared by proven project
  implementations.
- Treat `.agents/skills`, `.claude/skills`, `.github/skills`, and `.gzkit/skills`
  as consumer installation surfaces. Do not add generated mirrors here.
- Keep `gzkit` runtime behavior in `gzkit`; a portable skill may use a documented
  `gz` command when present but must state a safe discovery or fallback path.

## Skill contract

- Follow the open Agent Skills directory and frontmatter specification.
- Prefix public skill names with `gz-` to avoid collisions in user-level skill
  catalogs.
- Keep each skill focused on one user goal.
- Put branch-specific detail in `references/` and deterministic repeated logic in
  `scripts/` only after real usage proves it useful.
- Store GovZero-specific string metadata under `metadata` keys prefixed with
  `govzero-`.
- Use `agents/openai.yaml` only for OpenAI UI metadata or invocation policy; the
  workflow must remain usable when a harness ignores that file.
- Remote-mutating skills default to explicit invocation where the harness
  supports it.

## Versioning and provenance

- Version each skill independently with `metadata.govzero-version`.
- Increment the skill version when its observable workflow, safety boundary, or
  completion criteria change.
- Consumers install immutable snapshots and record the fields defined by
  `schemas/skill-lock.schema.json`.
- An updater may replace an installed skill only when its current hash still
  matches the prior lock. Treat a mismatch as a local modification and stop for
  reconciliation.

## Validation

Before handoff:

1. Validate every `skills/*/SKILL.md` against the Agent Skills specification.
2. Confirm the frontmatter name matches its parent directory.
3. Confirm every relative file link resolves.
4. Confirm each `agents/openai.yaml` default prompt names its skill explicitly.
5. Review activation descriptions for both intended and unintended triggers.

Preserve user changes. Do not commit or push unless explicitly requested.
