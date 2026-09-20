from __future__ import annotations

import json
import re
import tomllib
import unittest
from pathlib import Path

from gz_skills.core import load_catalog
from scripts.inventory_skills import discover_skills, floor_violations

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")
SEMVER = re.compile(
    r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)


class RepositoryContractTests(unittest.TestCase):
    def test_repository_uses_mit_license(self) -> None:
        license_text = (REPOSITORY_ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertTrue(license_text.startswith("MIT License\n"))
        self.assertIn("Copyright (c) 2026 GovZero", license_text)

        with (REPOSITORY_ROOT / "pyproject.toml").open("rb") as stream:
            python_metadata = tomllib.load(stream)["project"]
        opencode_metadata = json.loads(
            (REPOSITORY_ROOT / "package.json").read_text(encoding="utf-8")
        )

        self.assertEqual(python_metadata["license"], "MIT")
        self.assertEqual(opencode_metadata["license"], "MIT")

    def test_skill_names_and_openai_prompts_match_directories(self) -> None:
        catalog = load_catalog(REPOSITORY_ROOT / "skills")

        for name, skill in catalog.items():
            self.assertTrue(name.startswith("gzs-"), name)
            self.assertEqual(name, skill.path.name)
            self.assertIsNotNone(SEMVER.fullmatch(skill.version), skill.version)
            metadata = skill.path / "agents" / "openai.yaml"
            self.assertTrue(metadata.is_file(), metadata)
            interface = metadata.read_text(encoding="utf-8")
            self.assertIn(f"${name}", interface)

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
        self.assertIsNotNone(SEMVER.fullmatch(bundle_version), bundle_version)
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
        source_fallback = (
            REPOSITORY_ROOT / "src" / "gz_skills" / "__init__.py"
        ).read_text(encoding="utf-8")

        self.assertEqual(codex["version"], bundle_version)
        self.assertEqual(claude["version"], bundle_version)
        self.assertEqual(opencode["version"], bundle_version)
        self.assertIn(f'__version__ = "{bundle_version}"', source_fallback)
        self.assertEqual(codex["skills"], "./skills/")
        self.assertEqual(
            set(claude["skills"]), {f"./skills/{name}" for name in catalog}
        )
        self.assertEqual(opencode["main"], ".opencode/plugins/gz-skills.js")
        self.assertEqual(opencode["type"], "module")

    def test_marketplace_entries_pin_each_harness_to_bundle_tag(self) -> None:
        with (REPOSITORY_ROOT / "pyproject.toml").open("rb") as stream:
            tag = "v" + tomllib.load(stream)["project"]["version"]
        codex = json.loads(
            (REPOSITORY_ROOT / ".agents" / "plugins" / "marketplace.json")
            .read_text(encoding="utf-8")
        )
        claude = json.loads(
            (REPOSITORY_ROOT / ".claude-plugin" / "marketplace.json")
            .read_text(encoding="utf-8")
        )

        self.assertEqual(codex["name"], "gz-skills")
        self.assertEqual(claude["name"], "gz-skills")
        self.assertEqual(len(codex["plugins"]), 1)
        self.assertEqual(len(claude["plugins"]), 1)
        codex_entry = codex["plugins"][0]
        claude_entry = claude["plugins"][0]
        self.assertEqual(codex_entry["name"], "gz-skills")
        self.assertEqual(claude_entry["name"], "gz-skills")
        self.assertEqual(
            codex_entry["source"],
            {
                "source": "url",
                "url": "https://github.com/tvproductions/gz-skills.git",
                "ref": tag,
            },
        )
        self.assertEqual(
            codex_entry["policy"],
            {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        )
        self.assertEqual(codex_entry["category"], "Developer Tools")
        self.assertEqual(
            claude_entry["source"],
            {
                "source": "url",
                "url": "https://github.com/tvproductions/gz-skills.git",
                "ref": tag,
            },
        )

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

    def test_python_sdist_excludes_opencode_development_dependencies(self) -> None:
        with (REPOSITORY_ROOT / "pyproject.toml").open("rb") as stream:
            configuration = tomllib.load(stream)

        excluded = set(
            configuration["tool"]["hatch"]["build"]["targets"]["sdist"][
                "exclude"
            ]
        )
        self.assertTrue(
            {
                "/.opencode/.gitignore",
                "/.opencode/node_modules",
                "/.opencode/package-lock.json",
                "/.opencode/package.json",
            }.issubset(excluded)
        )

    def test_opencode_adapter_registers_the_canonical_skill_tree(self) -> None:
        adapter = (
            REPOSITORY_ROOT / ".opencode" / "plugins" / "gz-skills.js"
        ).read_text(encoding="utf-8")

        self.assertIn("../../skills", adapter)
        self.assertIn("config.skills.paths", adapter)
        self.assertIn("skillsPath", adapter)

    def test_read_only_catalog_guides_have_implicit_codex_policy(self) -> None:
        catalog = load_catalog(REPOSITORY_ROOT / "skills")

        for name in (
            "gzs-change-review",
            "gzs-dependency-risk-audit",
            "gzs-hexagonal-architecture-audit",
            "gzs-router",
        ):
            metadata = (catalog[name].path / "agents" / "openai.yaml").read_text(
                encoding="utf-8"
            )
            self.assertIn("allow_implicit_invocation: true", metadata)

    def test_router_covers_catalog_and_explicit_skills_have_codex_policy(self) -> None:
        catalog = load_catalog(REPOSITORY_ROOT / "skills")
        router = (catalog["gzs-router"].path / "SKILL.md").read_text(encoding="utf-8")

        for name in catalog:
            if name != "gzs-router":
                self.assertIn(f"`{name}`", router)

        for name in ("gzs-git-sync", "gzs-session-handoff"):
            metadata = (catalog[name].path / "agents" / "openai.yaml").read_text(
                encoding="utf-8"
            )
            self.assertIn("allow_implicit_invocation: false", metadata)

    def test_every_authored_skill_declares_a_discovery_floor(self) -> None:
        """AGENTS.md requires discovery-or-fallback; this is its witness.

        The contract predates the check, and the catalog drifted to one
        compliant skill in sixteen with nothing reporting it. FLOOR_PENDING
        carries the skills authored before the witness existed and may only
        shrink: a skill that gains the section while still listed there fails
        this test too, so the exemption is a countdown, not a standing waiver.
        """
        violations = floor_violations(discover_skills(REPOSITORY_ROOT))
        self.assertEqual(violations, [], "\n".join(violations))


if __name__ == "__main__":
    unittest.main()
