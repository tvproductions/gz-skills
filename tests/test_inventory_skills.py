from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path

from gz_skills.core import tree_sha256
from scripts.inventory_skills import (
    discover_skills,
    floor_violations,
    skill_tree_sha256,
    summarize,
)


class InventorySkillsTests(unittest.TestCase):
    def test_discovers_skill_and_collapses_mirrors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repository = root / "sample"
            (repository / ".git").mkdir(parents=True)
            for surface in (".agents", ".claude"):
                skill = repository / surface / "skills" / "gzs-example"
                skill.mkdir(parents=True)
                (skill / "SKILL.md").write_text(
                    "---\n"
                    "name: gzs-example\n"
                    "description: Example workflow.\n"
                    "---\n\n"
                    "Do the work.\n",
                    encoding="utf-8",
                )

            records = discover_skills(root)
            summary = summarize(records)

            self.assertEqual(len(records), 2)
            self.assertEqual(summary[0]["name"], "gzs-example")
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


class FloorContractTests(unittest.TestCase):
    """The floor contract: every authored skill declares a discovery fallback.

    AGENTS.md has required discovery-or-fallback since it was authored, and the
    catalog still drifted to one compliant skill in sixteen with no signal at
    all. These cover the witness that makes that drift visible.
    """

    def _write_skill(self, root: Path, name: str, body: str) -> None:
        skill = root / "sample" / "skills" / name
        skill.mkdir(parents=True, exist_ok=True)
        (skill / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Example.\n---\n\n# Example\n\n{body}",
            encoding="utf-8",
            newline="",
        )

    def _records(self, root: Path, name: str, body: str) -> list:
        (root / "sample" / ".git").mkdir(parents=True, exist_ok=True)
        self._write_skill(root, name, body)
        return discover_skills(root)

    def test_a_skill_declaring_the_floor_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            records = self._records(
                Path(directory),
                "gzs-example",
                "## Discovery and fallback\n\nUse the project command, else plain git.\n",
            )
            self.assertEqual(floor_violations(records, pending=frozenset()), [])

    def test_a_skill_without_the_floor_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            records = self._records(
                Path(directory), "gzs-example", "## Workflow\n\nDo the work.\n"
            )
            violations = floor_violations(records, pending=frozenset())
            self.assertEqual(len(violations), 1)
            self.assertIn("gzs-example", violations[0])

    def test_a_pending_skill_without_the_floor_is_tolerated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            records = self._records(
                Path(directory), "gzs-example", "## Workflow\n\nDo the work.\n"
            )
            self.assertEqual(floor_violations(records, pending={"gzs-example"}), [])

    def test_a_pending_skill_that_gained_the_floor_must_leave_the_list(self) -> None:
        """The ratchet arm: a stale exemption fails, so the list can only shrink.

        Without it the pending list is a permanent excuse rather than a
        countdown, and a repaired skill could keep its exemption indefinitely.
        """
        with tempfile.TemporaryDirectory() as directory:
            records = self._records(
                Path(directory),
                "gzs-example",
                "## Discovery and fallback\n\nUse the project command, else plain git.\n",
            )
            violations = floor_violations(records, pending={"gzs-example"})
            self.assertEqual(len(violations), 1)
            self.assertIn("no longer needs its exemption", violations[0])

    def test_an_empty_floor_section_does_not_satisfy_the_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            records = self._records(
                Path(directory),
                "gzs-example",
                "## Discovery and fallback\n\n## Evidence\n\nReport it.\n",
            )
            violations = floor_violations(records, pending=frozenset())
            self.assertEqual(len(violations), 1)
            self.assertIn("gzs-example", violations[0])


if __name__ == "__main__":
    unittest.main()
