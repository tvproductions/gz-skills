# Install gz-skills for OpenCode v2

The OpenCode v2 adapter is included in the v0.5.0 bundle. Install the
immutable Git tag in each adopting repository.

In each adopting repository, add the package to that repository's
`opencode.jsonc`:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "plugins": [
    "git+https://github.com/tvproductions/gz-skills.git#v0.5.0"
  ]
}
```

OpenCode loads the package's adapter and registers the canonical `skills/`
tree. Invoke `gzs-router` to choose a workflow. `gzs-git-sync` and
`gzs-session-handoff` require explicit selection.

OpenCode owns installation and updates for this project. Change the pinned
tag in that repository when deliberately updating. Avoid installing a
second vendored copy of the same skills in its discovery scope.

The package entry point lives outside this publisher repository's local
OpenCode plugin directory. The published v0.4.0 package uses the earlier
OpenCode adapter and does not support v2.
