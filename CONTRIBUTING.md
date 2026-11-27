# Contributions, questions, and bug reports

Contributions, questions, and bug reports should be made on Github using pull requests and issues. Dissertate uses semantic versioning (semver.org). Submit questions here: https://github.com/suchow/Dissertate/issues/new. First take a look at the FAQ.

## Building distribution packages

[Download the repository ZIP](https://github.com/suchow/Dissertate/archive/refs/heads/master.zip) and extract it, or clone the repository. From the repository root (`Dissertate-master` if extracted from the ZIP), run:

```sh
python3 scripts/package-latex Harvard Dissertate-Harvard-LaTeX.zip
```

Pass the name of a school directory in `assets/schools/` as the first argument. Each supported directory contains `style.sty` and `agent-guidance.md`. The resulting ZIP contains the template sources, fonts, and school-specific guidance in `AGENTS.md`. Add `--compile` to include a PDF; this requires XeLaTeX and BibTeX. Extract the generated ZIP before editing the template.

The legacy `scripts/build` entry point accepts the same school, output path, and options. It packages one school per invocation and requires an explicit output path.

For a hosted project import, add `--flat` to the packaging command. This places `dissertation.tex`, the class, fonts, and resources at the ZIP root. The release workflow prepares separate `Dissertate-<school>-Overleaf.zip` assets in this layout. Ordinary `LaTeX.zip` downloads retain their enclosing project folder.

Overleaf's documented import interface accepts a public ZIP URL in `snip_uri` and supports `engine=xelatex` and `main_document=dissertation.tex`. Publish the flat archive before adding a launch link. Archive layout is checked locally; a live Overleaf import and compilation still need verification. See the [Overleaf interface](https://www.overleaf.com/devs) and [project-upload guidance](https://docs.overleaf.com/managing-projects-and-files/uploading-a-project).

## Distribution licenses

The repository software license is in `LICENSE`. Bundled fonts and artwork have separate terms:

- EB Garamond: `assets/fonts/EB Garamond/COPYING` for the original OTF faces and `OFL.txt` in the same directory for the contributed bold TTF faces.
- Lato: `assets/fonts/Lato/SIL Open Font License 1.1.txt`.
- Source Code Pro: `assets/fonts/Source Code Pro/OFL.txt`.
- Colophon illustration: `assets/latex-base/endmatter/colophon-image.LICENSE`.

Disabling the colophon image does not remove its file from a source ZIP. University guides and institutional artwork also require their own distribution review. The Toronto cover notice is in `assets/schools/Toronto/resources/cover.png.LICENSE`; the repository software license does not license university marks.

The school ZIPs are editable project templates. The experimental CTAN tools below prepare separate class and font source packages. CTAN acceptance and TeX distribution inclusion remain unverified.

## Experimental CTAN staging

The CTAN class candidate is `dissertate`, a LaTeX-only class with an internal `school=generic` school-neutral layout. Its historical fonts are a separate `dissertate-historical-fonts` dependency. Normal school ZIP packaging is unchanged.

Run `python3 scripts/stage-ctan-generic /path/to/Dissertate /path/to/new-class-tree --component class` for the class TDS tree. This component does not read or copy font binaries or font notices. Use `--component fonts` and a different new destination for the separate font TDS tree. The default `--component all` prepares a combined local test tree, not a combined upload. Output parents must exist, and destinations must be new and outside the source checkout.

Build and review the package-specific manuals separately. Class staging accepts `--manual-pdf /path/to/dissertate-doc.pdf`; font staging accepts `--font-manual-pdf /path/to/dissertate-historical-fonts-doc.pdf`. Staging checks PDF headers and records hashes without compiling manuals or verifying PDF/source correspondence.

To prepare source uploads from reviewed stages with their PDFs, run `python3 scripts/prepare-ctan-source /path/to/reviewed-stage /path/to/new-packages MAJOR.MINOR.PATCH`. The output has separate `dissertate/` and `dissertate-historical-fonts/` directories; a single-component stage produces only its own package. Class source contains no font binaries, and font source contains no class/style files. Each package includes its original inputs, notices, package-specific manual, and handwritten preparation programs. Its README documents independent copy-only reconstruction. Generated runtime files, examples, and manifests are omitted. The explicit version identifies local candidates. These commands do not create a tag, publish a release, submit to CTAN, or establish TeX distribution inclusion.

## Checking rendered layouts

For chapter-heading changes, render the shipped chapter example with its `savequote` epigraph, a following chapter without an epigraph, and a starred chapter when supported. Inspect the heading, quote, attribution, and first body paragraph for overlap. A successful compilation alone does not verify page layout.

Before a release, inspect every page of each complete example affected by the changes. Record the PDF hash, pages inspected, and any examples that only compiled. For suspected text overlap, compare an enlarged render with PDF text coordinates before changing the artwork.
