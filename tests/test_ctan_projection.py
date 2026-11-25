import importlib.machinery
import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from test_ctan_staging import ROOT, hashes, module as staging

loader = importlib.machinery.SourceFileLoader("ctan_projection", str(ROOT / "scripts/prepare-ctan-source"))
spec = importlib.util.spec_from_loader(loader.name, loader)
projection = importlib.util.module_from_spec(spec)
loader.exec_module(projection)


class ProjectionTest(unittest.TestCase):
    def make_stage(self, root):
        pdf = root / "manual.pdf"
        pdf.write_bytes(b"%PDF-1.5\n%%EOF\n")
        stage = root / "stage"
        staging.stage(ROOT, stage, pdf)
        return stage

    def test_closed_source_roundtrip(self):
        with tempfile.TemporaryDirectory(prefix="dissertate-projection-") as name:
            root = Path(name)
            stage = self.make_stage(root)
            first = root / "first"
            records = projection.project(stage, first, "0.1.0")
            self.assertEqual((first / "source/prepare_ctan_source.py").read_bytes(),
                             (ROOT / "scripts/prepare-ctan-source").read_bytes())
            inputs = root / "inputs"
            # Execute only helpers generated here by the reviewed project tools.
            subprocess.run([sys.executable, "-I", str(first / "source/reconstruct.py"), str(inputs)], check=True)
            for relative, original, digest in records:
                self.assertEqual(hashes(first)[relative], digest)
                self.assertEqual((first / relative).read_bytes(), (inputs / original).read_bytes())
            rebuilt = root / "rebuilt"
            subprocess.run([sys.executable, "-I", str(inputs / "scripts/stage-ctan-generic"),
                            str(inputs), str(rebuilt), "--manual-pdf", str(inputs / "provided-manual.pdf")], check=True)
            second = root / "second"
            subprocess.run([sys.executable, "-I", str(inputs / "scripts/prepare-ctan-source"),
                            str(rebuilt), str(second), "0.1.0"], check=True)
            self.assertEqual(hashes(first), hashes(second))
            self.assertEqual(len(list((first / "fonts").iterdir())), 10)
            self.assertFalse((first / "tex").exists())
            self.assertFalse(any(p.name == "candidate-manifest.json" for p in first.rglob("*")))

    def test_refusals_preserve_existing_data_and_create_no_output(self):
        with tempfile.TemporaryDirectory(prefix="dissertate-projection-safety-") as name:
            root = Path(name)
            stage = self.make_stage(root)
            output = root / "output"
            with self.assertRaises(ValueError):
                projection.project(stage, output, "2026-11-25")
            self.assertFalse(output.exists())
            projection.project(stage, output, "0.1.0")
            before = hashes(output)
            with self.assertRaises(ValueError):
                projection.project(stage, output, "0.1.0")
            self.assertEqual(before, hashes(output))
            bad = root / "bad"
            shutil.copytree(stage, bad)
            readme = bad / "README.md"
            readme.write_bytes(b"tampered")
            rejected = root / "rejected"
            with self.assertRaises(ValueError):
                projection.project(bad, rejected, "0.1.0")
            self.assertFalse(rejected.exists())
            readme.unlink()
            readme.symlink_to(stage / "README.md")
            with self.assertRaises(ValueError):
                projection.project(bad, rejected, "0.1.0")
            self.assertFalse(rejected.exists())
            readme.unlink()
            with self.assertRaises(ValueError):
                projection.project(bad, rejected, "0.1.0")
            self.assertFalse(rejected.exists())


if __name__ == "__main__":
    unittest.main()
