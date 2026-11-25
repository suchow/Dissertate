import hashlib
import importlib.machinery
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
loader = importlib.machinery.SourceFileLoader("ctan_stage", str(ROOT / "scripts/stage-ctan-generic"))
spec = importlib.util.spec_from_loader(loader.name, loader)
module = importlib.util.module_from_spec(spec)
loader.exec_module(module)


def hashes(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


class StagingTest(unittest.TestCase):
    def test_reproducible_payload_and_existing_destination_safety(self):
        with tempfile.TemporaryDirectory(prefix="dissertate-ctan-test-") as name:
            root = Path(name)
            first, second = root / "first", root / "second"
            manifest = module.stage(ROOT, first)
            module.stage(ROOT, second)
            before = hashes(first)
            self.assertEqual(before, hashes(second))
            self.assertEqual(len(manifest["fonts"]), 10)
            for font in manifest["fonts"]:
                self.assertEqual(before[font["prefixed"]], font["sha256"])
            self.assertTrue(all(before[p] == h for p, h in manifest["outputs"].items()))
            self.assertEqual(len(list((first / "tex").rglob("*.cls"))), 2)
            self.assertFalse(any(p.endswith((".png", ".pdf", ".jpg")) for p in before))
            with self.assertRaises(ValueError):
                module.stage(ROOT, first)
            self.assertEqual(before, hashes(first))
            link = root / "link"
            link.symlink_to(first, target_is_directory=True)
            with self.assertRaises(ValueError):
                module.stage(ROOT, link)
            self.assertEqual(before, hashes(first))

    def test_unexpected_source_creates_no_destination(self):
        with tempfile.TemporaryDirectory(prefix="dissertate-ctan-test-") as name:
            root = Path(name)
            source = root / "source"
            for relative in ("assets/latex-base/Dissertate.cls", "assets/schools/Generic/style.sty"):
                p = source / relative
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text("unexpected source")
            output = root / "output"
            with self.assertRaises(ValueError):
                module.stage(source, output)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
