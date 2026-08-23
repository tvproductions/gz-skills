from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path

from gz_skills.core import tree_sha256
from scripts.inventory_skills import discover_skills, skill_tree_sha256, summarize


class InventorySkillsTests(unittest.TestCase):
    def test_discovers_skill_and_collapses_mirrors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repository = root / "sample"
            (repository / ".git").mkdir(parents=True)
            for surface in (".agents", ".claude"):
                skill = repository / surface / "skills" / "gz-example"
                skill.mkdir(parents=True)
                (skill / "SKILL.md").write_text(
                    "---\n"
                    "name: gz-example\n"
                    "description: Example workflow.\n"
                    "---\n\n"
                    "Do the work.\n",
                    encoding="utf-8",
                )

            records = discover_skills(root)
            summary = summarize(records)

            self.assertEqual(len(records), 2)
            self.assertEqual(summary[0]["name"], "gz-example")
            self.assertEqual(summary[0]["projects"], ["sample"])
            self.assertEqual(summary[0]["installations"], 2)
            self.assertEqual(summary[0]["instruction_variants"], 1)

    def test_tree_hash_matches_provenance_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory)
            (skill / "SKILL.md").write_bytes(b"skill")
            (skill / "references").mkdir()
            (skill / "references" / "notes.md").write_bytes(b"notes")
            (skill / "__pycache__").mkdir()
            (skill / "__pycache__" / "ignored.pyc").write_bytes(b"ignored")

            expected = hashlib.sha256()
            for relative, content in (
                ("SKILL.md", b"skill"),
                ("references/notes.md", b"notes"),
            ):
                expected.update(relative.encode("utf-8"))
                expected.update(b"\0")
                expected.update(content)
                expected.update(b"\0")

            self.assertEqual(skill_tree_sha256(skill), expected.hexdigest())
            self.assertEqual(skill_tree_sha256(skill), tree_sha256(skill))


if __name__ == "__main__":
    unittest.main()
