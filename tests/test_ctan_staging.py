import hashlib
import importlib.machinery
import importlib.util
from pathlib import Path
import tempfile
import subprocess
import sys
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
            pdf = root / "manual.pdf"
            pdf.write_bytes(b"%PDF-1.5\n%%EOF\n")
            manifest = module.stage(ROOT, first, pdf)
            module.stage(ROOT, second, pdf)
            before = hashes(first)
            self.assertEqual(before, hashes(second))
            self.assertEqual(len(manifest["fonts"]), 10)
            for font in manifest["fonts"]:
                self.assertEqual(before[font["prefixed"]], font["sha256"])
            self.assertTrue(all(before[p] == h for p, h in manifest["outputs"].items()))
            self.assertEqual(len(list((first / "tex").rglob("*.cls"))), 2)
            self.assertIn("README.md", before)
            self.assertIn("doc/latex/dissertate/manual.tex", before)
            self.assertTrue(manifest["manual_pdf_included"])
            self.assertEqual((first / "doc/latex/dissertate/manual.pdf").read_bytes(), pdf.read_bytes())
            self.assertFalse(any(p.endswith((".png", ".jpg")) for p in before))
            with self.assertRaises(ValueError):
                module.stage(ROOT, first)
            self.assertEqual(before, hashes(first))
            link = root / "link"
            link.symlink_to(first, target_is_directory=True)
            with self.assertRaises(ValueError):
                module.stage(ROOT, link)
            self.assertEqual(before, hashes(first))
            reconstructed = root / "reconstructed"
            mapping = {
                "source/latex/dissertate/inputs/dissertate-base-original.cls": "assets/latex-base/Dissertate.cls",
                "source/latex/dissertate/inputs/dissertate-school-generic-original.sty": "assets/schools/Generic/style.sty",
                "README.md": "docs/ctan-generic/README.md",
                "doc/latex/dissertate/manual.tex": "docs/ctan-generic/manual.tex",
                "source/latex/dissertate/stage_generic.py": "scripts/stage-ctan-generic",
            }
            for notice in module.NOTICES:
                mapping["doc/latex/dissertate/notices/" + notice.replace(" ", "-").replace("/", "--")] = notice
            for font in manifest["fonts"]:
                mapping[font["prefixed"]] = font["original"]
            for staged, original in mapping.items():
                target = reconstructed / original
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((first / staged).read_bytes())
            self.assertEqual((reconstructed / "assets/latex-base/Dissertate.cls").read_bytes(), (ROOT / "assets/latex-base/Dissertate.cls").read_bytes())
            self.assertEqual((reconstructed / "assets/schools/Generic/style.sty").read_bytes(), (ROOT / "assets/schools/Generic/style.sty").read_bytes())
            rebuilt = root / "rebuilt"
            subprocess.run([sys.executable, "-I", str(reconstructed / "scripts/stage-ctan-generic"), str(reconstructed), str(rebuilt), "--manual-pdf", str(pdf)], check=True)
            self.assertEqual(before, hashes(rebuilt))

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
            invalid_pdf = root / "invalid.pdf"
            invalid_pdf.write_text("not a PDF")
            with self.assertRaises(ValueError):
                module.stage(ROOT, output, invalid_pdf)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
