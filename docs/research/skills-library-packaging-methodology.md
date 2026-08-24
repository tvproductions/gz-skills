# Skills library and packaging methodology

This note compares established skills libraries as product and distribution
systems, not merely as collections of Markdown files. Each source-specific
section records observed mechanics before the final recommendations are drawn.

Research date: 2026-08-23.

## Superpowers

### Evidence boundary

The current canonical source is `obra/superpowers` at tag `v6.3.0`, commit
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797`. The local installed Codex copy at
`C:\Users\Jeff\source\repos\xp\xplane-webapi\.codex\plugins\superpowers` is
version `6.0.3`; it corroborates the installed artifact shape but is not used as
authority for current behavior.

Superpowers is both a methodology and its distribution. Its current design is
a single repository containing one canonical, harness-neutral skill tree plus
thin harness adapters. This is an important historical choice: version 2 moved
skills into a separately cloned `obra/superpowers-skills` repository, but commit
`9c9547cc042d05906d0eb26506f275ff6c82f679` restored them to the primary plugin
once skills became a first-class harness feature. The former skills repository
is now archived. Superpowers therefore provides evidence against maintaining a
second source repository merely to separate content from packaging when native
plugin packaging can carry the canonical tree directly.

### Repository model

The source tree has four distinct layers:

```text
skills/                         canonical skill content
  <skill>/SKILL.md
  <skill>/<supporting files>
.<harness>-plugin/              harness manifests
hooks/, .opencode/, .pi/        bootstrap/discovery adapters
scripts/                        release and packaging automation
tests/<harness>/                adapter and artifact tests
```

At `v6.3.0`, `skills/` is a flat namespace of 14 top-level skills. A skill owns
its references, prompt templates, examples, and deterministic helper scripts.
There are no harness-specific copies of the core skill bodies. The porting guide
states the governing rule explicitly: skill prose names actions such as “invoke
a skill,” “read a file,” or “dispatch a subagent,” never a harness tool name.
Harness vocabulary belongs in a tool mapping, not in rewritten skill variants.

This produces one-directional dependency flow:

```text
canonical skills <- packaged unchanged by each harness adapter
                 <- interpreted through a harness tool mapping
```

### Discovery and activation

Superpowers treats files being present as insufficient. A working integration
must solve two separate problems:

1. Register or expose the canonical `skills/` directory for lazy discovery.
2. Ensure the agent is taught at session start to check and invoke applicable
   skills.

The `using-superpowers` skill supplies the common activation policy. Harnesses
then use one of three adapter shapes:

- A session-start shell hook injects the bootstrap for Claude-compatible hook
  systems.
- An in-process JavaScript or TypeScript extension registers the skill path and
  injects bootstrap context for OpenCode and Pi.
- An extension-declared context file includes the bootstrap for Gemini.

Kimi exposes a manifest-level `sessionStart.skill`, while the Codex manifest
declares the `skills/` directory but deliberately sets `hooks` to `{}` so Codex
does not auto-load the Claude hook. Codex relies on its native skill discovery
surface rather than a copied or rewritten skill tree.

The porting guide makes native installation a safety boundary: an adapter ships
through the harness's own plugin, extension, marketplace, or package mechanism.
It must not edit a user's global instruction or configuration files to simulate
integration. If a harness cannot carry both discovery and automatic activation,
Superpowers considers that a platform limitation rather than permission to
mutate user-owned configuration.

### Packaging and installation

There is no universal Superpowers installer. Installation and updating are
delegated to each harness's native channel: marketplaces for Claude, Codex,
Cursor, and Kimi; Git URL installs for several extension systems; and package
manifest fields for Pi and OpenCode. A user who works in multiple harnesses
installs the product separately in each one.

The repository root remains the common source artifact. Harness manifests point
at the same `./skills/` directory. The root `package.json` carries the product
version and declares the OpenCode and Pi entry points; other harnesses use small
manifest files such as `.codex-plugin/plugin.json`,
`.cursor-plugin/plugin.json`, and `gemini-extension.json`. Runtime adapters are
kept dependency-free.

The Codex marketplace artifact demonstrates a stronger packaging boundary than
“zip the repository”:

- It is built from an explicit Git ref, not incidental working-tree contents.
- A dirty worktree is rejected by default.
- The payload is an allowlisted, rootless subset containing the Codex manifest,
  assets, license/community files, and `skills/`.
- Source-only docs, tests, scripts, hooks, and other harness adapters are
  rejected if they leak into the archive.
- File modes and timestamps are normalized, and ZIP and tar outputs are checked
  for equivalent paths.
- Every packaged skill must contain its Codex `agents/openai.yaml` metadata.
- The build reports a SHA-256 digest, and its test proves byte-identical output
  from equivalent metadata sources.

One contextual caveat is worth preserving: current Superpowers source does not
author the OpenAI marketplace metadata beside each canonical skill. The Codex
packager imports that metadata from a prior official package and refuses an
incomplete source. That accommodates an externally owned marketplace layer, but
it also means a completely fresh Codex package cannot be produced from the
repository alone. This is an ecosystem constraint, not a generally desirable
property of a personal skills library.

### Release and update model

Superpowers versions and releases the library as one product. Individual
`SKILL.md` files have Agent Skills `name` and `description` frontmatter but no
independent version field. At `v6.3.0`, nine version-bearing manifests share the
same semantic version.

`.version-bump.json` is the registry of every version-bearing file.
`scripts/bump-version.sh` provides three controls:

- update every registered field together;
- detect version drift among registered manifests;
- audit the repository for matching version strings in unregistered files.

The immutable Git tag identifies the complete content and adapter set. Actual
updates remain harness-owned: marketplace update, extension update, reinstall,
or package update depending on the platform. Superpowers does not maintain
consumer-project lock files or propagate copied snapshots across a repository
collection.

### Testing and validation

Superpowers separates packaging correctness from agent behavior:

- `tests/` verifies deterministic helpers, manifests, hooks, plugin loading,
  bootstrap caching, cross-platform behavior, and packaged archive contents.
- `evals/` uses the separate Drill harness to run real model sessions and judge
  whether skills trigger and change behavior.

The harness port acceptance test is behavioral, not structural. In a clean
session, “Let's make a react todo list” must activate `brainstorming` before any
code is written, and the full transcript is retained. Unique-marker tests prove
that an apparent context-injection mechanism really reaches the model rather
than merely making a file available.

The `writing-skills` skill applies red-green-refactor to process documentation:

1. Run a realistic scenario without the skill and record the failure and the
   agent's rationalizations.
2. Write the smallest skill that addresses observed failure.
3. Run the same scenario with the skill.
4. Add counters only for newly observed loopholes and repeat.

It distinguishes discipline, technique, pattern, and reference skills because
each requires different evaluations. Discipline skills need pressure scenarios;
techniques need application and edge cases; patterns need recognition and
counterexamples; reference skills need retrieval and gap tests. It also calls
for repeated, fresh-context wording micro-tests with a no-guidance control before
expensive end-to-end scenarios.

### Authoring conventions

Superpowers treats discoverability and context cost as part of correctness:

- Use a flat namespace and action-oriented, usually gerund, names.
- Keep the required `name` and `description` frontmatter minimal.
- Make `description` start with “Use when...”, describe only observable trigger
  conditions, and avoid summarizing the workflow. Their evaluations found that
  workflow summaries can become shortcuts that cause agents not to load the
  skill body.
- Put searchable symptoms and synonyms in the description and early prose.
- Keep frequently loaded content very short; move heavy reference material and
  reusable helpers into supporting files loaded only when needed.
- Refer to another skill by stable skill name and state whether it is required;
  avoid forced file includes that consume context prematurely.
- Prefer one complete, adaptable example over several shallow language variants.
- Use prose and tables for information; reserve diagrams for non-obvious
  decisions and loops.
- Do not create skills for one-off solutions, project policy, or constraints
  that a deterministic validator can enforce.

### Transferable Superpowers lessons

The strongest general lessons are methodological:

1. Keep one canonical skill tree. Package it through adapters; do not maintain
   harness-specific prose forks.
2. Treat discovery, activation, and installation as separate contracts. Test all
   three in a clean installed environment.
3. Prefer the harness's native installer and updater. A cross-harness tool may
   orchestrate those channels, but should not impersonate them by editing global
   user configuration.
4. Release from an explicit immutable source identity. Make artifacts minimal,
   reproducible, checksummed, and tested for both required and forbidden paths.
5. Keep bundle versions synchronized mechanically. Content hashes may add
   provenance, but they do not replace a coherent product release.
6. Test skill behavior, not just YAML validity and copying. Baseline failures,
   trigger tests, pressure scenarios, and retained transcripts are the functional
   tests for this kind of product.
7. Optimize descriptions as dispatch predicates rather than summaries. The
   body remains the executable guidance.
8. Add and validate one skill at a time. A batch extraction can establish an
   inventory, but it is not behavioral validation.
9. Keep the library and its thin packaging adapters together unless an external
   ecosystem forces a separate repository. Superpowers tried independent skill
   cloning and returned to an integrated repository when native skill packaging
   made the split unnecessary.

## Matt Pocock skills

### Evidence boundary

The current canonical source inspected was `mattpocock/skills` at commit
`5b15a47f2d7150f545fbcacbfe381787fc0230dc` on 2026-08-21. It contained 36
discoverable `SKILL.md` files, of which 25 were promoted by the native Claude
plugin. Its bundle version was `1.2.3`.

### Product model

Matt's library is a composable toolbox rather than one mandatory methodology.
The skills are small enough to use independently, but the promoted engineering
set also defines useful chains such as discovery and grilling through specs,
tickets, implementation, and review. `ask-matt` is a human-facing router over
the user-invoked skills; `setup-matt-pocock-skills` moves repository variability
such as issue tracker, triage labels, and domain-document locations into
consumer-owned configuration.

Invocation mode is a first-class catalog axis:

- user-invoked skills orchestrate a substantial workflow and are prevented from
  implicit activation;
- model-invoked skills provide reusable disciplines and carry rich trigger
  descriptions.

The policy is encoded twice where the harnesses differ:
`disable-model-invocation: true` in applicable `SKILL.md` frontmatter for
Claude, and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`
for Codex. This is a practical example of keeping one skill body while allowing
small harness metadata adapters.

### Repository and maturity model

Skills are grouped by audience and maturity under `skills/`:

```text
skills/
  engineering/       promoted
  productivity/      promoted
  misc/              available but not promoted
  in-progress/       public beta, direct install only
  deprecated/        retirement record
docs/<bucket>/        human-facing promoted-skill pages
```

The distinction between promoted and in-progress is excellent product
discipline. Experimental skills can be tried without being represented as
stable, and retirement is explicit.

The exact physical layout has a portability cost. Claude's plugin manifest can
enumerate many skill directories and therefore exposes only promoted skills.
The repository's own ADR records that Codex's single skill-path manifest could
not express two promoted buckets without also exposing drafts and miscellaneous
skills. Symlink curation failed because installed plugin copies dropped the
links. A native Codex plugin was therefore deferred. The lesson is to keep the
maturity distinction but not necessarily this nested discoverable layout.

### Two installation philosophies

The README deliberately offers two mutually exclusive modes:

1. **Managed subscription.** The native Claude plugin installs the promoted set
   as a read-only bundle and receives publisher-controlled updates.
2. **Editable vendoring.** `npx skills@latest add mattpocock/skills` discovers
   the repository through the open `skills` CLI, lets the user select skills and
   target agents, and copies ordinary editable files. Updates happen only when
   the user runs `npx skills update`.

That distinction is clearer than treating every install as one compromise
between mutability and automatic updates. The README warns users not to install
both because duplicate discovery produces duplicate skills.

The universal installer is not part of Matt's repository; it is supplied by
`vercel-labs/skills`. This keeps his package free of cross-harness installation
code. A local compatibility probe confirmed that the same installer discovers
all ten current `gz-skills` entries with:

```powershell
npx --yes skills@latest add . --list
```

The universal installer's lock is useful update metadata, but it is not a fully
reproducible package lock. Its own issue tracker documents missing-install-mode
state, replacement of local edits during updates, and historical inability to
reconstruct a missing installation from a current lock. `gz-skills` should not
give up its stricter content-hash and local-modification safeguards merely to
match that tool.

### Release model

Matt versions the repository as one product. `package.json` is private—the Node
package is release metadata rather than the portable skill payload. Changesets
records user-visible changes, maintains `CHANGELOG.md`, opens a release pull
request, and tags the bundle. A small script copies the bundle version into the
Claude plugin manifest and provides a drift-check mode.

This is compatible with skill-level provenance: a bundle release answers “what
coherent catalog did I install?”, while an individual tree hash answers “what
exact files does this installed skill contain?” They solve different problems.

### Human documentation

Promoted skills have human-facing pages separate from `SKILL.md`. The agent file
is an executable runbook; the docs page answers what the skill does, when to
reach for it, prerequisites, how to recognize success, and where it fits among
neighboring skills. The pages act as a distributed human router and do not copy
the procedure.

This separation prevents the catalog from optimizing solely for agent
activation. People need a map, especially for explicitly invoked skills the
model will never suggest.

### Transferable Matt Pocock lessons

1. State whether a skill is user- or model-invoked and encode that policy for
   every supported harness.
2. Offer managed subscription and editable vendoring as separate install
   contracts; do not blur their update and ownership semantics.
3. Maintain a human catalog and router in addition to machine discovery.
4. Put repository-specific variation behind one setup/configuration seam rather
   than repeating discovery questions across skills.
5. Publish stable and experimental maturity clearly.
6. Version and document the catalog as one released product even when users can
   install a subset.
7. Reuse an existing installer when its runtime contract fits. GovZero later
   chose a Python-only vendoring contract, so this particular Node-based route
   remains comparative evidence rather than an adopted channel.
8. Keep the useful editorial buckets, but do not let them force duplicated
   plugin payloads or prevent a stable-only native package.

## Comparison and recommendations for `gz-skills`

### Where the models agree

Superpowers and Matt differ in product shape, but agree on the important
foundations:

| Concern | Shared lesson |
| --- | --- |
| Canonical content | One source skill tree; harness packaging is an adapter. |
| Skill format | Plain Agent Skills directories with supporting files owned by each skill. |
| Portability | Core prose describes actions and invariants, not harness tool names. |
| Discovery | Names and descriptions are product interfaces, not incidental frontmatter. |
| Invocation | Explicit orchestration and implicit disciplines need different policies. |
| Releases | The library has one coherent semantic version and immutable release identity. |
| Validation | Structural checks are necessary but do not prove model behavior. |
| Documentation | Humans need a catalog and map separate from the agent runbooks. |

### Recommended product architecture

Keep the repository integrated and give each layer one job:

```text
skills/                 flat, promoted, canonical skill tree only
docs/skills/            human-facing catalog pages
adapters or manifests   thin native harness packaging metadata
src/gz_skills/          optional GovZero fleet/locked-snapshot administration
tests/                  format, lock, installer, manifest, and artifact tests
evals/                  trigger, pressure, and outcome scenarios using real agents
```

Drafts should not appear anywhere a recursive installer will discover
`SKILL.md`. Keep them on a development branch or under an incubation tree whose
instruction file is deliberately not named `SKILL.md`. This preserves Matt's
maturity discipline and Superpowers' flat-package compatibility.

### Distribution model

The subsequent GovZero packaging decision narrows the supported product to two
channels:

1. **Native managed bundle:** add native plugin manifests where a harness can
   expose the canonical `skills/` tree without copies. The plugin is a
   subscription: update as one release and do not locally edit it.
2. **Python vendoring and fleet administration:** use the `gz-skills` CLI through
   `uvx` for pinned snapshots, exact tree hashes, local-edit detection, and
   controlled propagation across repositories. Node is not part of the
   supported consumer toolchain.

These modes must be mutually intelligible. Documentation should warn against
installing the same skill through two channels into one discovery scope.

### Versioning and releases

Use a bundle semantic version and immutable Git tag as the public release
identity. Keep independent skill versions only because the fleet updater can
usefully report a changed subset; automate the rule that a changed skill tree
requires its version to advance. Add a registry/check that keeps the Python
package and every native manifest on the same bundle version.

Build release artifacts from an explicit clean Git ref with an allowlist,
normalized archive metadata, a SHA-256 digest, and tests for both required and
forbidden paths. The wheel should package the fleet CLI plus canonical skills;
native plugin archives should omit Python administration code unless their
runtime actually needs it.

### Validation gap

The current catalog has strong structural and installer validation, but the ten
skills were extracted as a batch. On Superpowers' standard they are candidates,
not behaviorally validated skills.

Before a `1.0.0` release, give each skill:

- positive trigger scenarios;
- negative near-miss scenarios that should not activate it;
- a no-skill baseline showing the failure the skill corrects;
- a with-skill run under realistic pressure;
- outcome assertions and a retained transcript;
- fresh-context repetitions where wording or trigger reliability is uncertain.

Remote-mutating skills need additional authorization and refusal scenarios.
`gzs-git-sync`, for example, must not activate from an ordinary request to edit a
file and must refuse destructive reconciliation pressure.

Descriptions should be reviewed as dispatch predicates. Prefer a leading “Use
when...” containing observable conditions and symptoms; move workflow summaries
into the body or human docs. Syntax validation cannot catch an agent that sees a
summary, skips loading the body, and improvises the workflow.

### What not to copy

- Keep the Python CLI focused on the small, declared destination-surface matrix.
- Do not rely on floating branches, live consumer symlinks, or silent replacement
  for fleet propagation.
- Do not put promoted and draft `SKILL.md` files under one recursively
  discoverable root if native packaging cannot select them cleanly.
- Do not add an always-loaded `using-gz-skills` bootstrap merely because
  Superpowers has one. Superpowers is a cohesive methodology that needs global
  activation discipline; the current GovZero catalog is a toolbox. Add a router
  or bootstrap only if observed failures prove it necessary.
- Do not treat a valid YAML file, a successful copy, or a package build as proof
  that a skill changes agent behavior correctly.

### Recommended sequence

1. Reframe the README around native plugins first and Python `uvx` vendoring
   second.
2. Add bundle release metadata, changelog discipline, version-drift checks, and
   CI for the validation already present.
3. Add matching explicit-invocation metadata for Claude and Codex.
4. Create one human catalog page per promoted skill and a concise catalog index.
5. Build behavior evaluations, starting with the two motivating skills and the
   highest-risk implicit triggers.
6. Publish the native managed-plugin adapters from the canonical flat tree.
7. Publish `0.x` releases while evaluations mature; call the catalog `1.0.0`
   only when every promoted skill has behavioral evidence.

## Primary sources

### Superpowers

- Canonical repository and release identity:
  [obra/superpowers at `b36e0829`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797),
  tag [`v6.3.0`](https://github.com/obra/superpowers/releases/tag/v6.3.0).
- Product layout, install channels, contribution rules, and update statement:
  [`README.md`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/README.md).
- Cross-harness invariants, adapter shapes, acceptance criteria, distribution,
  and test expectations:
  [`docs/porting-to-a-new-harness.md`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/docs/porting-to-a-new-harness.md).
- Structural versus behavioral testing:
  [`docs/testing.md`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/docs/testing.md).
- Skill authoring and behavioral test methodology:
  [`skills/writing-skills/SKILL.md`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/writing-skills/SKILL.md).
- Shared activation policy:
  [`skills/using-superpowers/SKILL.md`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/using-superpowers/SKILL.md).
- Version registry and coordinated bump implementation:
  [`.version-bump.json`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/.version-bump.json) and
  [`scripts/bump-version.sh`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/scripts/bump-version.sh).
- Deterministic Codex package construction and its acceptance tests:
  [`scripts/package-codex-plugin.sh`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/scripts/package-codex-plugin.sh) and
  [`tests/codex/test-package-codex-plugin.sh`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/tests/codex/test-package-codex-plugin.sh).
- Representative harness adapters:
  [Codex manifest](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/.codex-plugin/plugin.json),
  [OpenCode plugin](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/.opencode/plugins/superpowers.js), and
  [Pi extension](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/.pi/extensions/superpowers.ts).
- Historical reintegration of the skill tree:
  [commit `9c9547cc`](https://github.com/obra/superpowers/commit/9c9547cc042d05906d0eb26506f275ff6c82f679).
- Former independently cloned library, archived 2025-10-27:
  [`obra/superpowers-skills` at `cdcd624a`](https://github.com/obra/superpowers-skills/tree/cdcd624ad3fd8026deb692e565351854569798dd).
- Local installed artifact inspected:
  `C:\Users\Jeff\source\repos\xp\xplane-webapi\.codex\plugins\superpowers`
  (`.codex-plugin/plugin.json` reports version `6.0.3`).

### Matt Pocock skills

- Canonical repository identity inspected:
  [`mattpocock/skills` at `5b15a47f`](https://github.com/mattpocock/skills/tree/5b15a47f2d7150f545fbcacbfe381787fc0230dc).
- Product philosophy, dual installation contracts, catalog, and workflow map:
  [`README.md`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/README.md).
- Bundle version, private release package, and Changesets commands:
  [`package.json`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/package.json).
- Curated native Claude package:
  [`.claude-plugin/plugin.json`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/.claude-plugin/plugin.json).
- Plugin layout decision and the native Codex curation constraint:
  [ADR 0002](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/.agents/adr/0002-ship-as-a-claude-code-plugin.md).
- Coordinated release automation:
  [release workflow](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/.github/workflows/release.yml),
  [Changesets configuration](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/.changeset/config.json), and
  [plugin-version synchronization](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/scripts/sync-plugin-version.mjs).
- Stable and experimental maturity contracts:
  [engineering catalog](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/engineering/README.md) and
  [in-progress catalog](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/in-progress/README.md).
- Project configuration seam:
  [`setup-matt-pocock-skills`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/skills/engineering/setup-matt-pocock-skills/SKILL.md).
- Human documentation contract:
  [`.agents/writing-docs.md`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/.agents/writing-docs.md).

### Universal `skills` installer

- Supported sources, target agents, and update commands:
  [`vercel-labs/skills` README](https://github.com/vercel-labs/skills/blob/main/README.md).
- Current documented update limitations relevant to local ownership:
  [copy-mode loss on update](https://github.com/vercel-labs/skills/issues/1199),
  [local-edit replacement](https://github.com/vercel-labs/skills/issues/455), and
  [lock versus reproducible install](https://github.com/vercel-labs/skills/issues/283).
