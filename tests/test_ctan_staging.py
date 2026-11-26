import hashlib
import importlib.machinery
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
loader = importlib.machinery.SourceFileLoader('ctan_stage', str(ROOT/'scripts/stage-ctan-generic'))
spec = importlib.util.spec_from_loader(loader.name, loader)
module = importlib.util.module_from_spec(spec)
loader.exec_module(module)


def hashes(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


def manuals(root):
    class_pdf, font_pdf = root/'dissertate-doc.pdf', root/'dissertate-historical-fonts-doc.pdf'
    class_pdf.write_bytes(b'%PDF-1.5\n% class fixture\n%%EOF\n')
    font_pdf.write_bytes(b'%PDF-1.5\n% font fixture\n%%EOF\n')
    return class_pdf, font_pdf


class StagingTest(unittest.TestCase):
    def test_separate_components_and_deterministic_all_tree(self):
        with tempfile.TemporaryDirectory(prefix='dissertate-stage-') as name:
            root = Path(name)
            class_pdf, font_pdf = manuals(root)
            first, second = root/'first', root/'second'
            manifest = module.stage(ROOT, first, class_pdf, font_pdf)
            module.stage(ROOT, second, class_pdf, font_pdf)
            self.assertEqual(hashes(first), hashes(second))
            self.assertEqual(len(manifest['fonts']), 10)
            for font in manifest['fonts']:
                self.assertEqual(hashes(first)[font['prefixed']], font['sha256'])
            # Class source without a font tree must still stage independently.
            class_source = root/'class-source'
            for rel in ['LICENSE', 'assets/latex-base/Dissertate.cls', 'assets/schools/Generic/style.sty',
                        'docs/ctan-generic/README.md', 'docs/ctan-generic/dissertate-doc.tex']:
                p = class_source/rel
                p.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT/rel, p)
            class_tree = root/'class-tree'
            class_manifest = module.stage(class_source, class_tree, class_pdf, component='class')
            self.assertEqual(class_manifest['fonts'], [])
            self.assertFalse(any(p.endswith(('.otf', '.ttf')) for p in hashes(class_tree)))
            self.assertFalse(any('assets/fonts/' in p for p in class_manifest['inputs']))
            font_tree = root/'font-tree'
            font_manifest = module.stage(ROOT, font_tree, font_manual_pdf=font_pdf, component='fonts')
            self.assertFalse(any(p.endswith(('.cls', '.sty')) for p in hashes(font_tree)))
            self.assertFalse(any('latex-base' in p for p in font_manifest['inputs']))
            self.assertEqual({k:v for k,v in hashes(first).items() if k in class_manifest['outputs']}, class_manifest['outputs'])
            self.assertEqual({k:v for k,v in hashes(first).items() if k in font_manifest['outputs']}, font_manifest['outputs'])

    def test_refusals_precede_creation_and_preserve_existing_tree(self):
        with tempfile.TemporaryDirectory(prefix='dissertate-stage-safety-') as name:
            root = Path(name)
            output = root/'output'
            module.stage(ROOT, output, component='class')
            before = hashes(output)
            with self.assertRaises(ValueError):
                module.stage(ROOT, output, component='class')
            self.assertEqual(before, hashes(output))
            link = root/'link'
            link.symlink_to(output, target_is_directory=True)
            with self.assertRaises(ValueError):
                module.stage(ROOT, link, component='class')
            rejected = root/'rejected'
            bad_pdf = root/'bad.pdf'
            bad_pdf.write_text('not a PDF')
            with self.assertRaises(ValueError):
                module.stage(ROOT, rejected, bad_pdf, component='class')
            self.assertFalse(rejected.exists())
            with self.assertRaises(ValueError):
                module.stage(ROOT, rejected, font_manual_pdf=bad_pdf, component='fonts')
            self.assertFalse(rejected.exists())


if __name__ == '__main__':
    unittest.main()
