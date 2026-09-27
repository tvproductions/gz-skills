from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "gzs-project-setup"
    / "scripts"
    / "project_settings.py"
)
SPEC = importlib.util.spec_from_file_location("project_settings", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
project_settings = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(project_settings)


class ProjectSetupTests(unittest.TestCase):
    def test_initialize_select_and_promote_preserve_minimal_schema(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / ".gz-skills" / "settings.json"
            self.assertEqual(project_settings.run("inspect", root)["status"], "absent")
            self.assertEqual(project_settings.run("initialize", root)["status"], "created")
            self.assertEqual(project_settings.run("initialize", root)["status"], "present")
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), {
                "schema_version": 1,
                "profile": None,
            })
            project_settings.run("select", root, "lite")
            project_settings.run("select", root, "heavy")
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), {
                "schema_version": 1,
                "profile": "heavy",
            })
            with self.assertRaisesRegex(project_settings.SettingsError, "reversal"):
                project_settings.run("select", root, "lite")
            self.assertEqual(project_settings.run("inspect", root)["profile"], "heavy")

    def test_gzkit_blocks_setup_without_creating_project_home(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".gzkit").mkdir()
            with self.assertRaisesRegex(project_settings.SettingsError, "incompatible"):
                project_settings.run("initialize", root)
            self.assertFalse((root / ".gz-skills").exists())

    def test_existing_unknown_settings_are_never_replaced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            home = root / ".gz-skills"
            home.mkdir()
            path = home / "settings.json"
            original = '{"schema_version": 1, "profile": "lite", "note": "mine"}\n'
            path.write_text(original, encoding="utf-8")
            with self.assertRaisesRegex(project_settings.SettingsError, "reconcile"):
                project_settings.run("initialize", root)
            self.assertEqual(path.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
