# Consumer install layouts: Matt Pocock Skills and Superpowers

Research date: 2026-08-23.

## Conclusion

`gzkit/.agents/skills/` is a correct path for a **project-owned editable
install**, especially for Codex. It is not the layout used by a native managed
plugin.

The two upstream projects deliberately represent different choices:

- Matt Pocock Skills offers both choices and tells users to pick one. Its
  Claude plugin is a managed bundle in Claude's user cache. For Codex and other
  agents, its documented route is the universal `npx skills` installer, which
  puts the canonical project copy under `.agents/skills/` and tracks it for
  explicit updates.
- Superpowers uses native, harness-specific plugin or extension installers. Its
  Claude and Codex installs live in their respective managed plugin caches, not
  in the consumer repository. It does not document `npx skills` as an install
  route because the plugin also carries the activation/bootstrap integration
  that makes Superpowers a methodology rather than only a directory of skills.

For `gz-skills`, the question should therefore be “who owns the installed
copy?” rather than “which path is universally right?”

| Contract | Consumer layout | Update model | Best fit |
| --- | --- | --- | --- |
| Managed subscription | Native Claude/Codex plugin cache | Publisher releases and harness updates | Personal or centrally managed use across many repositories |
| Editable project dependency | `<repo>/.agents/skills/gzs-*` for Codex/universal agents | Explicit Python `gz-skills update` | Reproducible, reviewable repository dependencies |

Do not install the same skill through both contracts in one harness scope. Both
Matt's README and install policy warn that the result is duplicate discovery.

## Matt Pocock Skills

Evidence was taken from `mattpocock/skills` commit
`5b15a47f2d7150f545fbcacbfe381787fc0230dc`. The official Claude marketplace
catalog was inspected at `anthropics/claude-plugins-official` commit
`340e33aef211d95769d252324854497af871dafe`. The universal installer was
inspected at `vercel-labs/skills` commit
`435076e78988e1e6ec40d00b0b1d76bdbbc5419a`.

### Claude Code: managed plugin, not project vendoring

Matt's documented Claude route is:

```text
claude plugins install mattpocock-skills
```

The official Anthropic catalog points `mattpocock-skills` at a SHA-pinned Git
source. The plugin's `.claude-plugin/plugin.json` explicitly enumerates the
promoted skill directories. Claude Code copies marketplace plugins into the
user cache at `~/.claude/plugins/cache`; it does not execute the checkout in
place and it does not copy the skill folders to the consumer project's
`.agents/skills/` or `.claude/skills/` directory.

Claude's installation *scope* and the payload location are separate concepts.
User scope is the default. Project scope records enablement in
`.claude/settings.json`, but the plugin payload still lives in the user plugin
cache. Plugin skills receive the plugin namespace, such as
`/mattpocock-skills:tdd`, which helps avoid command collisions.

At the inspected marketplace revision, the official listing pins Matt's source
to `0ab1b63a410a03d3627979a109c8695de27af954`, behind the inspected upstream
head. Matt's own ADR calls out this release boundary explicitly: publishing an
upstream commit and advancing the official marketplace pin are separate steps.

### Codex and other agents: editable project install

Matt has intentionally deferred a native Codex plugin. His canonical install
policy says to use:

```text
npx skills@latest add mattpocock/skills
npx skills@latest update <name>
```

His repository characterizes this as editable files copied into the project,
in contrast to the read-only Claude plugin subscription.

The concrete layout comes from the current `vercel-labs/skills` implementation:

- Project installs use `.agents/skills/<skill-name>` as their canonical copy.
- Codex's registered project skill directory is itself `.agents/skills`, so a
  Codex-targeted project install lands directly there; no second Codex-specific
  project path is required.
- Claude Code's registered project path is `.claude/skills`. In the default
  recommended mode, the installer keeps the canonical copy under
  `.agents/skills` and links the Claude path to it. On Windows it requests a
  junction. If linking fails, it falls back to a copy.
- `--copy` skips the shared canonical/link arrangement and writes an independent
  copy directly to each selected agent's directory.
- Project installs are recorded in `skills-lock.json`, which the CLI uses for
  project update and restore operations.

The universal installer's global story is different and currently internally
inconsistent for some “universal” agents. Its README documents Codex global
skills at `~/.codex/skills/`, while the inspected implementation treats every
agent whose project path is `.agents/skills` as universal and places the global
canonical copy at `~/.agents/skills/` without creating an agent-specific link.
That discrepancy is another reason to prefer project installs when the desired
contract is repository vendoring, and native plugins when the desired contract
is user-wide subscription.

### What Matt's model means for `gzkit`

If `gzkit` chooses editable, checked-in dependencies, this is the direct Matt
Pocock analogue:

```text
gzkit/
  .agents/skills/
    gzs-git-sync/
    gzs-update-dependencies/
  skills-lock.json
```

The files are ordinary repository content. They can be reviewed and pinned, but
updates are deliberate and may overwrite edits. The durable customization seam
must therefore remain in `AGENTS.md`, configuration, or a separate local skill.

## Superpowers

Evidence was taken from the `obra/superpowers` `v6.3.0` source at commit
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797`. The official Codex marketplace
repository was inspected at `openai/plugins` commit
`11c74d6ba24d3a6d48f54a194cd00ef3beea18f9`.

### Claude Code: managed plugin cache

Superpowers documents installation from Anthropic's official marketplace:

```text
/plugin install superpowers@claude-plugins-official
```

Its Claude plugin keeps the canonical `skills/` tree and session-start hook in
one installed bundle. Claude copies that bundle into
`~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`. No project-local
`.agents/skills` or `.claude/skills` copy is part of the supported installation.

The official Claude marketplace entry points directly to the Superpowers Git
repository at the exact inspected commit. Updating therefore means the
marketplace advances its source pin and Claude refreshes its managed cache.

### Codex App and CLI: managed Codex plugin cache

Superpowers documents the official Codex plugin marketplace for both the Codex
app and CLI. Its canonical `.codex-plugin/plugin.json` points the `skills` field
at `./skills/` and suppresses Claude-style hook auto-discovery with an empty
`hooks` object. Codex discovers the skill folders inside the installed plugin
bundle; it does not vendor them into the current project.

OpenAI's current plugin documentation defines the installed location as:

```text
~/.codex/plugins/cache/<marketplace>/<plugin>/<version>/
```

The official `openai/plugins` catalog carries a complete vendored Superpowers
plugin under `plugins/superpowers/`, and its marketplace entry points at that
local directory. The consumer sees only the cached installed plugin.

There is a useful publisher-side detail: Superpowers maintains a deterministic
sync script that copies an allowlisted subset of the canonical repository into
`prime-radiant-inc/openai-codex-plugins` and opens a pull request. That is
**marketplace vendoring**, not consumer-project vendoring. At the inspected
OpenAI catalog revision, the bundled manifest is version `5.1.3`, while
canonical Superpowers is `6.3.0`, demonstrating that upstream publication and
marketplace propagation can be separate release steps.

### No supported universal `npx skills` route

Superpowers' README says installation differs by harness and users of multiple
harnesses install it separately for each one. Its porting guide makes the native
harness installer a design rule and rejects hand-copying files or editing user
configuration as integration mechanisms.

Although a generic Agent Skills scanner can discover the repository's
`skills/` directory, `npx skills add obra/superpowers` is not a documented
Superpowers install contract. A raw skill copy would omit or bypass parts of
the harness-specific activation/bootstrap integration. It should not be
presented as equivalent to the supported plugin.

### What Superpowers' model means for `gzkit`

If `gz-skills` is installed as a native Codex or Claude plugin, `gzkit` should
contain no vendored `gzs-*` directories. The project may record policy or setup
requirements, but the harness owns the bundle and cache:

```text
gzkit/                         no gzs-* payload
~/.codex/plugins/cache/...     Codex-managed gz-skills bundle
~/.claude/plugins/cache/...    Claude-managed gz-skills bundle
```

This most closely serves the original goal “change it once and let updates
propagate,” but it is a user/harness dependency rather than a repository-pinned
dependency. A collaborator or CI environment still needs the plugin installed,
and marketplace review or source-pin movement can add release latency.

## Recommendation for `gz-skills`

Publish both contracts, but name them accurately and keep them mutually
exclusive per harness scope.

1. **Default personal/fleet use: native managed plugin.** This is the best match
   for a centrally maintained library that should update across projects. It
   avoids repository churn and benefits from plugin namespacing. The plugin
   cache is an implementation detail and should not be edited.
2. **Repository dependency: Python project vendoring.** Use `uvx` and
   `gzkit/.agents/skills/gzs-*` when `gzkit` must pin, review, and carry exact
   skill snapshots with the source tree. Commit the lock/provenance file, treat
   the installed directories as generated dependencies, and update explicitly.
   Node-based installation is outside the supported GovZero contract.
3. **Never install both into the same effective discovery scope.** A native
   plugin plus `.agents/skills/gzs-*` creates duplicate semantic skills even if
   plugin namespacing prevents a filesystem collision.

Thus the path previously proposed is not wrong. It is specifically the
**editable vendoring** path. It should not be the only or default answer if the
primary requirement is frictionless propagation across all local projects.

## Primary sources

### Matt Pocock Skills

- Current install contracts and duplicate-install warning:
  [`README.md`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/README.md) and
  [canonical install block](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/.agents/install-block.md).
- Claude plugin's explicit skill allowlist:
  [`.claude-plugin/plugin.json`](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/.claude-plugin/plugin.json).
- Native Claude decision, deferred Codex plugin, and marketplace pin behavior:
  [ADR 0002](https://github.com/mattpocock/skills/blob/5b15a47f2d7150f545fbcacbfe381787fc0230dc/.agents/adr/0002-ship-as-a-claude-code-plugin.md).
- Official Anthropic marketplace entry and pinned source:
  [`marketplace.json`](https://github.com/anthropics/claude-plugins-official/blob/340e33aef211d95769d252324854497af871dafe/.claude-plugin/marketplace.json).
- Claude's cache and installation-scope behavior:
  [Claude Code plugin reference](https://code.claude.com/docs/en/plugins-reference) and
  [marketplace guide](https://code.claude.com/docs/en/discover-plugins).

### Universal `skills` installer

- Commands, symlink/copy modes, supported project paths, and global paths:
  [`README.md`](https://github.com/vercel-labs/skills/blob/435076e78988e1e6ec40d00b0b1d76bdbbc5419a/README.md).
- Canonical `.agents/skills` placement, copy mode, symlink mode, Windows junction,
  fallback behavior, and the current global-universal shortcut:
  [`src/installer.ts`](https://github.com/vercel-labs/skills/blob/435076e78988e1e6ec40d00b0b1d76bdbbc5419a/src/installer.ts).
- Claude and Codex directory registrations and the definition of a universal
  agent:
  [`src/agents.ts`](https://github.com/vercel-labs/skills/blob/435076e78988e1e6ec40d00b0b1d76bdbbc5419a/src/agents.ts).
- Project lock and update implementation:
  [`src/local-lock.ts`](https://github.com/vercel-labs/skills/blob/435076e78988e1e6ec40d00b0b1d76bdbbc5419a/src/local-lock.ts) and
  [`src/update.ts`](https://github.com/vercel-labs/skills/blob/435076e78988e1e6ec40d00b0b1d76bdbbc5419a/src/update.ts).

### Superpowers

- Harness-specific installation policy:
  [`README.md`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/README.md).
- Native installation as a porting rule, adapter shapes, and Codex marketplace
  propagation:
  [`docs/porting-to-a-new-harness.md`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/docs/porting-to-a-new-harness.md).
- Canonical manifests:
  [Claude plugin](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/.claude-plugin/plugin.json) and
  [Codex plugin](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/.codex-plugin/plugin.json).
- Publisher-side Codex marketplace synchronization:
  [`scripts/sync-to-codex-plugin.sh`](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/scripts/sync-to-codex-plugin.sh).
- Official OpenAI marketplace listing and installed payload:
  [`marketplace.json`](https://github.com/openai/plugins/blob/11c74d6ba24d3a6d48f54a194cd00ef3beea18f9/.agents/plugins/marketplace.json) and
  [vendored Superpowers manifest](https://github.com/openai/plugins/blob/11c74d6ba24d3a6d48f54a194cd00ef3beea18f9/plugins/superpowers/.codex-plugin/plugin.json).
- Codex plugin cache, marketplace, and package layout:
  [official OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work).
