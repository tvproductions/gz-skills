from __future__ import annotations

import json
import re
import tomllib
import unittest
from pathlib import Path

from gz_skills.core import load_catalog

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")


class RepositoryContractTests(unittest.TestCase):
    def test_skill_names_and_openai_prompts_match_directories(self) -> None:
        catalog = load_catalog(REPOSITORY_ROOT / "skills")

        for name, skill in catalog.items():
            self.assertEqual(name, skill.path.name)
            metadata = skill.path / "agents" / "openai.yaml"
            self.assertTrue(metadata.is_file(), metadata)
            self.assertIn(f"${name}", metadata.read_text(encoding="utf-8"))

    def test_relative_markdown_links_resolve(self) -> None:
        markdown_files = [REPOSITORY_ROOT / "README.md"]
        markdown_files.extend((REPOSITORY_ROOT / "docs").rglob("*.md"))
        markdown_files.extend((REPOSITORY_ROOT / "skills").rglob("*.md"))

        for markdown_file in markdown_files:
            text = markdown_file.read_text(encoding="utf-8")
            for raw_target in MARKDOWN_LINK.findall(text):
                target = raw_target.strip().strip("<>").split("#", 1)[0]
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                resolved = (markdown_file.parent / target).resolve()
                self.assertTrue(resolved.exists(), f"{markdown_file}: {raw_target}")

    def test_lock_schema_is_valid_json(self) -> None:
        schema = json.loads(
            (REPOSITORY_ROOT / "schemas" / "skill-lock.schema.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(
            schema["$schema"], "https://json-schema.org/draft/2020-12/schema"
        )
        self.assertEqual(schema["properties"]["schema_version"]["const"], 1)

    def test_bundle_versions_and_plugin_catalogs_are_synchronized(self) -> None:
        with (REPOSITORY_ROOT / "pyproject.toml").open("rb") as stream:
            bundle_version = tomllib.load(stream)["project"]["version"]
        codex = json.loads(
            (REPOSITORY_ROOT / ".codex-plugin" / "plugin.json").read_text(
                encoding="utf-8"
            )
        )
        claude = json.loads(
            (REPOSITORY_ROOT / ".claude-plugin" / "plugin.json").read_text(
                encoding="utf-8"
            )
        )
        opencode = json.loads(
            (REPOSITORY_ROOT / "package.json").read_text(encoding="utf-8")
        )
        catalog = load_catalog(REPOSITORY_ROOT / "skills")

        self.assertEqual(codex["version"], bundle_version)
        self.assertEqual(claude["version"], bundle_version)
        self.assertEqual(opencode["version"], bundle_version)
        self.assertEqual(codex["skills"], "./skills/")
        self.assertEqual(
            set(claude["skills"]), {f"./skills/{name}" for name in catalog}
        )
        self.assertEqual(opencode["main"], ".opencode/plugins/gz-skills.js")
        self.assertEqual(opencode["type"], "module")

    def test_supported_installation_contract_has_no_node_commands_or_dependencies(
        self,
    ) -> None:
        operational_docs = [
            REPOSITORY_ROOT / "README.md",
            REPOSITORY_ROOT / "docs" / "packaging.md",
        ]

        for document in operational_docs:
            text = document.read_text(encoding="utf-8").lower()
            self.assertNotIn("npx ", text, document)
            self.assertNotIn("npm ", text, document)
            self.assertNotIn("skills@latest", text, document)

        package = json.loads(
            (REPOSITORY_ROOT / "package.json").read_text(encoding="utf-8")
        )
        self.assertNotIn("dependencies", package)
        self.assertNotIn("devDependencies", package)
        self.assertNotIn("scripts", package)

    def test_opencode_adapter_registers_the_canonical_skill_tree(self) -> None:
        adapter = (
            REPOSITORY_ROOT / ".opencode" / "plugins" / "gz-skills.js"
        ).read_text(encoding="utf-8")

        self.assertIn("../../skills", adapter)
        self.assertIn("config.skills.paths", adapter)
        self.assertIn("skillsPath", adapter)

    def test_router_covers_catalog_and_explicit_skills_have_codex_policy(self) -> None:
        catalog = load_catalog(REPOSITORY_ROOT / "skills")
        router = (catalog["gzs-router"].path / "SKILL.md").read_text(encoding="utf-8")

        for name in catalog:
            if name != "gzs-router":
                self.assertIn(f"`{name}`", router)

        for name in ("gzs-git-sync", "gzs-session-handoff", "gzs-router"):
            metadata = (catalog[name].path / "agents" / "openai.yaml").read_text(
                encoding="utf-8"
            )
            self.assertIn("allow_implicit_invocation: false", metadata)


if __name__ == "__main__":
    unittest.main()
