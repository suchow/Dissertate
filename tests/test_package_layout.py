from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


class PackageLayoutTest(unittest.TestCase):
    def test_flat_import_preserves_project_files_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory(prefix="dissertate-layout-") as name:
            root = Path(name)
            normal, flat = root / "normal.zip", root / "flat.zip"
            command = [sys.executable, "-I", str(ROOT / "scripts/package-latex"), "Generic"]
            subprocess.run(command + [str(normal)], check=True, capture_output=True)
            subprocess.run(command + [str(flat), "--flat"], check=True, capture_output=True)
            with ZipFile(normal) as package:
                prefix = "Dissertate-Generic-LaTeX/"
                original = {p.filename[len(prefix):]: package.read(p) for p in package.infolist() if not p.is_dir()}
            with ZipFile(flat) as package:
                imported = {p.filename: package.read(p) for p in package.infolist() if not p.is_dir()}
                self.assertIsNone(package.testzip())
            self.assertEqual(original, imported)
            for required in ("dissertation.tex", "Dissertate.cls", "AGENTS.md", "frontmatter/personalize.tex"):
                self.assertIn(required, imported)
            self.assertTrue(any(p.startswith("fonts/") for p in imported))
            before = flat.read_bytes()
            result = subprocess.run(command + [str(flat), "--flat"], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(flat.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
