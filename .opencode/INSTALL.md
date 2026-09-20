# Install gz-skills for OpenCode

Add the released git package to the `plugin` array in the applicable
`opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": [
    "gz-skills@git+https://github.com/tvproductions/gz-skills.git#v0.3.2"
  ]
}
```

Restart OpenCode. Its managed plugin runtime loads the bundled adapter, which
registers the package's canonical `skills/` directory with OpenCode's native
skill tool.

Use `gzs-router` when you want help choosing a GovZero workflow.

OpenCode owns installation and updates for this channel. Do not edit the
managed package cache. Pin a release tag for reproducible use and change that
tag deliberately when updating.

This installation does not require a Node command or add a Node dependency to
the consuming project.
