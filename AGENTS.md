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
- Prefer portable primitives beneath project orchestrators. This repository owns
  standalone horizontal disciplines; consuming systems such as `gzkit` own
  lifecycle stages, governance state, gates, receipts, locks, and attestation.
- Keep composition one-way: a `gzs-*` skill must remain useful without `gzkit`,
  while `gzkit` or another project workflow may invoke or wrap it. When such a
  workflow is active, the portable skill must yield to it rather than duplicate,
  bypass, or create parallel lifecycle state.

## Skill contract

- Follow the open Agent Skills directory and frontmatter specification.
- Prefix public skill names with `gzs-` to identify the `gz-skills` release
  contract and avoid collisions with project-local `gz-*` skills.
- Apply `gzs-` to the skill directory, frontmatter `name`, and invocation token.
  Keep headings and UI display names human-readable; prefer the established
  `GovZero ...` labels rather than exposing a raw identifier as display copy.
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

- Follow Semantic Versioning 2.0.0 for both the bundle and each skill. With
  every shipped skill or bundle change, compare against the last released tag,
  maintain the correct pending version and `CHANGELOG.md` entry in the same
  change, and record the reason.
  Follow the release gates in `docs/packaging.md`. An unreleased version may be
  corrected; never decrement, change, or reuse a published version.
- Keep the bundle version synchronized across `pyproject.toml`,
  `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, and `package.json`.
  During 0.x development, use minor for new or incompatible bundle capability
  and patch for compatible corrections. Promote the bundle to 1.0.0 only after
  the catalog review. Thereafter use major for incompatible installer, lock, or
  bundle contracts; minor for compatible capability; and patch for fixes.
  Any changed released skill tree also advances the bundle version.
- Version each skill independently with `metadata.govzero-version`. During 0.x
  development, use minor for new or incompatible skill capability and patch for
  compatible corrections. Promote a skill to 1.0.0 only after its individual
  review accepts a stable contract. Thereafter use major for incompatible
  invocation, workflow, safety, or authorization changes; minor for compatible
  capability; and patch for fixes, prompts, activation metadata, or resources.
  Repository-only tests and documentation do not change a skill version.
- Classify every addition, removal, or edit under `skills/`, including
  behavior-preserving refactors and packaged resources. Start a new skill at
  0.1.0. Raise the version of a changed released skill by at least a patch;
  multiple pending edits may share one version if it covers the highest change
  since release. Record skill removals and migration in the changelog and
  advance the bundle version.
- Record every user-visible bundle or skill change under `Unreleased` in
  `CHANGELOG.md`. At release, rename that section to the released bundle version
  and ISO date, then create a fresh `Unreleased` section.
- Consumers install immutable snapshots and record the fields defined by
  `schemas/skill-lock.schema.json`.
- An updater may replace an installed skill only when its current hash still
  matches the prior lock. Treat a mismatch as a local modification and stop for
  reconciliation.
- Issue the catalog as a managed plugin first. Codex, Claude Code, and OpenCode
  are harness adapters over one tagged skill tree, not separate authored copies.
  Support one additional contract: Python `uvx` snapshots when a repository must
  vendor skills. Do not add other distribution channels or Node tooling to the
  supported install and update contract; OpenCode owns its bundled runtime.
- Treat versions on `main` as candidates. A release requires the validated
  immutable tag and channel-specific publication and install evidence. Keep the
  Codex and Claude marketplace manifests separately pinned to the same
  released tag. Validate each harness schema and install from that tag before
  claiming availability. Do not call a Codex, Claude Code, or OpenCode plugin
  published based on a manifest or local cache.
  Do not install both a managed plugin and vendored copy into one discovery scope.

## Validation

Before handoff:

1. Validate every `skills/*/SKILL.md` against the Agent Skills specification.
2. Confirm the frontmatter name matches its parent directory.
3. Confirm every relative file link resolves.
4. Confirm each `agents/openai.yaml` default prompt names its skill explicitly.
5. Review activation descriptions for both intended and unintended triggers.

Preserve user changes. Do not commit or push unless explicitly requested.
