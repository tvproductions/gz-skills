# Changelog

All notable changes to the released GovZero skills bundle are recorded here.
Each skill also carries an independent `metadata.govzero-version` for selective
fleet updates.

## 0.1.0 - Unreleased

### Added

- Eleven portable GovZero skills, including the `gz-skill-router` curator.
- Universal Agent Skills discovery through the canonical flat `skills/` tree.
- Native Codex and Claude plugin manifests.
- A Python fleet CLI for pinned installation, status, safe update, and
  collection-wide propagation.
- Full-tree provenance locks that block replacement of locally modified skills.
- Preserved all-project and candidate-user-authored inventory snapshots.
- Structural, installer, manifest, link, formatting, lint, and type validation.

### Release blockers

- Complete the one-by-one skill review and behavioral scenarios.
- Decide whether the Claude managed artifact should transform explicit-only
  invocation metadata while retaining the Codex-valid canonical tree.
- Choose and add the repository license.
- Create and publish the `tvproductions/gz-skills` remote.
