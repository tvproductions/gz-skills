# Skill provenance contract

Portable skills are vendored code. A consumer must be able to answer exactly
what it installed, from where, and whether the installed copy has been edited.

## Lock record

Record one entry per installed skill in a consumer-owned lock file validated by
[`schemas/skill-lock.schema.json`](../schemas/skill-lock.schema.json):

```json
{
  "schema_version": 1,
  "skills": [
    {
      "name": "gzs-git-sync",
      "version": "0.1.0",
      "source": {
        "repository": "https://github.com/<owner>/gz-skills.git",
        "revision": "<full-git-commit-sha>",
        "path": "skills/gzs-git-sync"
      },
      "sha256": "<sha256-of-the-installed-skill-tree>",
      "installed_path": ".agents/skills/gzs-git-sync"
    }
  ]
}
```

An `uvx` installation from Git records the full PEP 610 commit identity. A
released wheel may use its immutable distribution identity, such as
`package:0.1.0`. Tags and branches are discovery aids, not immutable identities.
A development install from a dirty checkout records
`working-tree:<current-HEAD>`; treat that as test provenance and replace it with
a released Git-backed snapshot before committing a consumer lock.

## Tree hash

The `sha256` value identifies the installed skill directory, not only
`SKILL.md`. Compute it from every regular file below the skill root:

1. Use forward-slash relative paths sorted by ordinal byte order.
2. Exclude transient files such as `__pycache__`, `.DS_Store`, and editor state.
3. For each file, feed its UTF-8 relative path, one NUL byte, its raw bytes, and
   one NUL byte into a single SHA-256 digest in that order.

This commits the instructions and every bundled reference, script, asset, and
harness metadata file as one unit.

## Install and update behavior

- Install from a clean checkout at the locked revision.
- Validate the source skill before copying it.
- Copy the complete skill directory to the consumer's canonical skill surface.
- Record the resulting tree hash and installed path.
- Generate harness mirrors only after the canonical snapshot and lock agree.

Before an update, hash the installed directory and compare it with the current
lock:

- Equal: the installed snapshot is unchanged and may be replaced atomically.
- Different: the consumer contains local edits; stop and require an explicit
  keep, discard, or extraction decision.
- Missing: report the broken installation rather than silently recreating it.

This preserves local project authority while allowing safe upstream refreshes.
