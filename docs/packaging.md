# Packaging contracts

`gz-skills` has one canonical flat skill tree and two supported installation
contracts. The managed plugin is the primary product; Python vendoring is for
repositories that require pinned, reviewable copies. Choose one contract per
agent scope.

| Contract | Owner of installed files | Update mechanism | Local edits |
| --- | --- | --- | --- |
| Native managed plugin | Publisher/harness | Harness plugin manager | Unsupported in the installed cache. |
| Python vendored snapshot | Consumer with upstream provenance | `uvx ... gz-skills update` or `propagate` | Detected by complete tree hash and blocks replacement. |

The plugin contract has three harness adapters over the same tagged source.
Codex and Claude Code can both read the repository's
[marketplace manifest](../.claude-plugin/marketplace.json); Codex supports this
[legacy-compatible location](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work).

| Harness | Distribution mechanism | Evidence before claiming availability |
| --- | --- | --- |
| Codex | Git-backed repository marketplace pinned to a tag; public directory is separate | Installation from the tagged marketplace; directory listing only after separate publication. |
| Claude Code | Repository marketplace entry pinned to a Git tag | Marketplace validation and installation of that tag. |
| OpenCode | Git-backed package pinned to a Git tag | Plugin-manager installation of that tag. |

The Python contract uses the same Git tag through `uvx` and records each
installed skill in the consumer lock. Registry publication to `npm` or
PyPI is outside the supported release contract.

## 1. Native managed plugins

- [`.codex-plugin/plugin.json`](../.codex-plugin/plugin.json) exposes the flat
  canonical `skills/` directory and passes the Codex plugin validator.
- [`.claude-plugin/plugin.json`](../.claude-plugin/plugin.json) explicitly lists
  all promoted skills and its repository marketplace passes
  `claude plugin validate . --strict`.
- [`package.json`](../package.json) exposes the package-local
  [OpenCode adapter](../.opencode/plugins/gz-skills.js). OpenCode's own managed
  runtime loads the adapter, which registers the canonical `skills/` directory
  through the native skill loader. This adds no Node command, dependency, or
  project toolchain to the supported contract.

Claude's `disable-model-invocation` frontmatter and Codex's explicit-invocation
metadata are not mutually accepted by the Codex plugin validator. The canonical
tree therefore uses `agents/openai.yaml` for Codex policy.

The `v0.2.0` Claude package deliberately ships that canonical Agent Skills tree
unchanged. It does not build a Claude-specific transformed copy. Explicit-only
intent remains part of each affected skill's activation description and
authority boundary, while Codex additionally enforces its invocation policy
through `agents/openai.yaml`. This is a documented 0.x harness limitation, not
permission for an implicitly selected skill to perform a remote mutation.

## 2. Python vendored snapshots

The Python distribution bundles the canonical skill trees and exposes:

```text
gz-skills list
gz-skills install
gz-skills status
gz-skills update
gz-skills propagate
```

Install from a tagged Git revision with `uvx`; Node is not part of the supported
consumer toolchain:

```powershell
uvx --from git+https://github.com/tvproductions/gz-skills.git@v0.3.0 `
  gz-skills install --project C:\path\to\project gzs-git-sync
```

The fleet lock records source identity, bundle path, independent skill version,
installed path, and complete tree hash. Local edits block replacement until the
consumer reconciles them explicitly.

## Release identity

The public bundle version is synchronized across `pyproject.toml`, the Codex
manifest, the Claude manifest, and the OpenCode package manifest. An immutable
Git tag identifies a released catalog. Individual skill versions identify the
changed subset for fleet administration.

Every publication requires a clean, validated release commit, synchronized
bundle manifests, reproducible artifacts with recorded SHA-256 values, and an
immutable Git tag. The repository is licensed under the
[MIT License](../LICENSE).

The one-by-one skill review and behavioral evidence in
[`docs/review/README.md`](review/README.md) gate the stable `1.0.0` release.
They remain intentionally in progress during the 0.x development series.

## Release governance

A version in `main` is a candidate, not a release. The remote immutable tag
identifies the released catalog. A plugin cache or a manifest's version string
does not prove that a release exists. Check each harness's publication and
installation state separately.

### Decide versions from the last released tag

Compare each changed skill with its version at the last release tag. The skill
contract includes its invocation, activation, workflow, output, safety, and
authorization behavior. Version the bundle separately for changes to its catalog,
installer, lock, and plugin distribution contract. A packaged skill change
also advances the bundle even if catalog membership stays the same. Record the
reason and consumer impact in `CHANGELOG.md`; the highest applicable change sets
each next version.

While a bundle or skill is in the 0.x development series, advance its minor
version for a new capability or a changed contract, including an incompatible
change. Advance its patch version for a compatible correction. Call out breaking
behavior and any migration in the changelog. An individual skill reaches 1.0.0
only after its one-by-one review accepts a stable public contract; the bundle
reaches 1.0.0 only after the catalog review is complete. Once an identity is
stable, use major for incompatible contracts, minor for compatible capabilities,
and patch for compatible fixes. Repository-only tests and documentation do not
advance skill versions. Pending versions can be amended before publication;
released versions and tags are immutable.

### Publish a bundle

1. Inventory changes since the last tag. For each changed skill, record its old
   and proposed version, classification, user-visible impact, and migration if
   needed. Confirm the four bundle manifests agree and the changelog covers
   every user-visible change.
2. Prepare one release commit: move `Unreleased` to the bundle version and ISO
   date, add a fresh `Unreleased` section, update installation examples to the
   proposed tag, and advance the Claude marketplace source ref to that tag.
   Confirm all examples and refs name the same candidate version.
3. On that clean commit, run the repository validation commands in the README,
   native plugin validators, and package-content checks. Build the Python wheel
   and source archive from the release commit, check their contents, and record
   their SHA-256 digests. Resolve failures before tagging.
4. Create an annotated, immutable `vX.Y.Z` tag on the validated commit with the
   artifact digests. When publication is authorized, push the commit and tag so
   the marketplace never points at a missing ref. Starting with `0.3.0`, create
   a GitHub Release from that tag with notes, artifacts, and checksums. Verify
   the remote tag resolves to the validated commit.
5. Verify Codex and Claude Code installation from the tagged repository
   marketplace, OpenCode installation from its Git package, and `uvx` snapshot
   installation. A universal public Plugins Directory listing is separate:
   submit the tagged Codex package for review, then publish it after approval.
   Record each channel's actual availability. See the official
   [Codex publication flow](https://developers.openai.com/plugins/deploy/submission#public-publishing-flow)
   and [Claude Git ref support](https://code.claude.com/docs/en/plugin-marketplaces#github-repositories).

The shared Codex and Claude marketplace uses a GitHub source pinned to the
latest released tag. Advancing `main` alone therefore does not promote
development skills to marketplace adopters. Consumer propagation is a separate action after release; never change
consumer locks or installed trees as part of publisher-side tagging.
