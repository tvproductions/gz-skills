from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from gz_skills.core import SkillInstallError, install, states, update

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_SKILLS = REPOSITORY_ROOT / "skills"


class InstallerTests(unittest.TestCase):
    def test_install_writes_complete_snapshot_and_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            destination = project / ".agents" / "skills"
            lock = project / "gz-skills.lock.json"

            installed = install(
                ["gz-git-sync"],
                destination,
                lock,
                source_root=SOURCE_SKILLS,
                revision="test-revision",
            )

            self.assertEqual(installed, ["gz-git-sync"])
            self.assertTrue((destination / "gz-git-sync" / "SKILL.md").is_file())
            document = json.loads(lock.read_text(encoding="utf-8"))
            self.assertEqual(document["skills"][0]["version"], "0.1.0")
            self.assertEqual(
                document["skills"][0]["source"]["revision"], "test-revision"
            )
            self.assertEqual(states(lock, SOURCE_SKILLS)[0].state, "current")

    def test_update_refuses_locally_modified_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            destination = project / ".agents" / "skills"
            lock = project / "gz-skills.lock.json"
            install(
                ["gz-git-sync"],
                destination,
                lock,
                source_root=SOURCE_SKILLS,
                revision="test-revision",
            )
            skill_file = destination / "gz-git-sync" / "SKILL.md"
            skill_file.write_text(
                skill_file.read_text(encoding="utf-8") + "\nlocal edit\n"
            )

            self.assertEqual(states(lock, SOURCE_SKILLS)[0].state, "modified")
            with self.assertRaisesRegex(SkillInstallError, "modified"):
                update(lock, apply=True, source_root=SOURCE_SKILLS)

    def test_update_replaces_unchanged_old_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            destination = root / "project" / ".agents" / "skills"
            lock = root / "project" / "gz-skills.lock.json"
            source_skill = source / "gz-example"
            source_skill.mkdir(parents=True)
            skill_file = source_skill / "SKILL.md"
            skill_file.write_text(
                "---\nname: gz-example\ndescription: Example.\nmetadata:\n"
                '  govzero-version: "0.1.0"\n---\n\nFirst.\n',
                encoding="utf-8",
            )
            install(
                ["gz-example"],
                destination,
                lock,
                source_root=source,
                revision="old",
            )
            skill_file.write_text(
                "---\nname: gz-example\ndescription: Example.\nmetadata:\n"
                '  govzero-version: "0.2.0"\n---\n\nSecond.\n',
                encoding="utf-8",
            )

            self.assertEqual(states(lock, source)[0].state, "update-available")
            final = update(lock, apply=True, source_root=source)

            self.assertEqual(final[0].state, "current")
            self.assertEqual(final[0].installed_version, "0.2.0")
            self.assertIn(
                "Second.",
                (destination / "gz-example" / "SKILL.md").read_text(encoding="utf-8"),
            )

    def test_multi_install_preflights_all_targets_before_replacing_any(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            destination = project / ".agents" / "skills"
            lock = project / "gz-skills.lock.json"
            install(
                ["gz-git-sync", "gz-quality-gate"],
                destination,
                lock,
                source_root=SOURCE_SKILLS,
                revision="test-revision",
            )
            first = destination / "gz-git-sync" / "SKILL.md"
            second = destination / "gz-quality-gate" / "SKILL.md"
            first_before = first.read_bytes()
            second.write_text(second.read_text(encoding="utf-8") + "\nlocal edit\n")

            with self.assertRaisesRegex(SkillInstallError, "locally modified"):
                install(
                    ["gz-git-sync", "gz-quality-gate"],
                    destination,
                    lock,
                    source_root=SOURCE_SKILLS,
                    revision="new-revision",
                )

            self.assertEqual(first.read_bytes(), first_before)
            document = json.loads(lock.read_text(encoding="utf-8"))
            self.assertTrue(
                all(
                    entry["source"]["revision"] == "test-revision"
                    for entry in document["skills"]
                )
            )


if __name__ == "__main__":
    unittest.main()
