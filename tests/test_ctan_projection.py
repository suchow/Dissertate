import importlib.machinery
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from test_ctan_staging import ROOT, hashes, manuals, module as staging

loader = importlib.machinery.SourceFileLoader('ctan_projection', str(ROOT/'scripts/prepare-ctan-source'))
spec = importlib.util.spec_from_loader(loader.name, loader)
projection = importlib.util.module_from_spec(spec)
loader.exec_module(projection)


class ProjectionTest(unittest.TestCase):
    def make_stage(self, root):
        class_pdf, font_pdf = manuals(root)
        stage = root/'stage'
        staging.stage(ROOT, stage, class_pdf, font_pdf)
        return stage

    def test_independent_source_packages_roundtrip(self):
        with tempfile.TemporaryDirectory(prefix='dissertate-split-') as name:
            root = Path(name)
            stage = self.make_stage(root)
            output = root/'packages'
            projection.project(stage, output, '0.2.0')
            for component, package_id in projection.PACKAGES.items():
                package = output/package_id
                files = hashes(package)
                if component == 'class':
                    self.assertFalse(any(p.endswith(('.otf', '.ttf')) for p in files))
                    self.assertIn('doc/dissertate-doc.tex', files)
                else:
                    self.assertEqual(len(list((package/'fonts').iterdir())), 10)
                    self.assertFalse(any(p.endswith(('.cls', '.sty')) for p in files))
                    self.assertIn('doc/dissertate-historical-fonts-doc.pdf', files)
                self.assertFalse(any(p.endswith('/manual.tex') or p.endswith('/manual.pdf') for p in files))
                self.assertFalse((package/'tex').exists())
                self.assertFalse((package/'source/reconstruct.py').exists())
                self.assertEqual((package/('source/'+package_id+'-prepare.py')).read_bytes(),
                                 (ROOT/'scripts/prepare-ctan-source').read_bytes())
                inputs = root/(component+'-inputs')
                projection.reconstruct(package, inputs)
                # Execute only exact reviewed program bytes copied by these tools.
                self.assertEqual((inputs/'scripts/stage-ctan-generic').read_bytes(), (ROOT/'scripts/stage-ctan-generic').read_bytes())
                staged_again = root/(component+'-stage')
                flag = '--manual-pdf' if component == 'class' else '--font-manual-pdf'
                pdf = inputs/('provided-manual.pdf' if component == 'class' else 'provided-font-manual.pdf')
                subprocess.run([sys.executable, '-I', str(inputs/'scripts/stage-ctan-generic'), str(inputs),
                                str(staged_again), '--component', component, flag, str(pdf)], check=True)
                repeated = root/(component+'-packages')
                subprocess.run([sys.executable, '-I', str(inputs/'scripts/prepare-ctan-source'),
                                str(staged_again), str(repeated), '0.2.0'], check=True)
                self.assertEqual(files, hashes(repeated/package_id))

    def test_projection_refusals_create_no_output(self):
        with tempfile.TemporaryDirectory(prefix='dissertate-projection-safety-') as name:
            root = Path(name)
            stage = self.make_stage(root)
            output = root/'output'
            with self.assertRaises(ValueError):
                projection.project(stage, output, '2026-11-26')
            self.assertFalse(output.exists())
            projection.project(stage, output, '0.2.0')
            before = hashes(output)
            with self.assertRaises(ValueError):
                projection.project(stage, output, '0.2.0')
            self.assertEqual(before, hashes(output))
            readme = stage/(projection.CD+'README.md')
            readme.write_bytes(b'tampered')
            rejected = root/'rejected'
            with self.assertRaises(ValueError):
                projection.project(stage, rejected, '0.2.0')
            self.assertFalse(rejected.exists())
            readme.unlink()
            readme.symlink_to(ROOT/'docs/ctan-generic/README.md')
            with self.assertRaises(ValueError):
                projection.project(stage, rejected, '0.2.0')
            self.assertFalse(rejected.exists())

    def test_reconstruction_refusals_preserve_destination(self):
        with tempfile.TemporaryDirectory(prefix='dissertate-reconstruct-safety-') as name:
            root = Path(name)
            packages = root/'packages'
            projection.project(self.make_stage(root), packages, '0.2.0')
            package = packages/'dissertate-historical-fonts'
            output = root/'inputs'
            projection.reconstruct(package, output)
            before = hashes(output)
            with self.assertRaises(ValueError):
                projection.reconstruct(package, output)
            self.assertEqual(before, hashes(output))
            font = next((package/'fonts').iterdir())
            font.unlink()
            rejected = root/'rejected'
            with self.assertRaises(ValueError):
                projection.reconstruct(package, rejected)
            self.assertFalse(rejected.exists())


if __name__ == '__main__':
    unittest.main()
