# Dissertate LaTeX class: local TDS component

This experimental tool prepares separate class and historical-font components. The CTAN class package identifier is `dissertate`. The separate dependency is `dissertate-historical-fonts`. The class is LaTeX-only. Its internal `school=generic` option means a school-neutral dissertation layout; it does not mean Plain TeX compatibility.

## Prepare separate TDS trees

Preparation requires Python 3. Run these commands with an existing source checkout and two new output directories whose parents already exist:

```sh
python3 /path/to/Dissertate/scripts/stage-ctan-generic /path/to/Dissertate /tmp/dissertate-class --component class
python3 /path/to/Dissertate/scripts/stage-ctan-generic /path/to/Dissertate /tmp/dissertate-fonts --component fonts
```

Class staging does not read or copy font binaries or font notices. Font staging contains no class or style files. The default `--component all` prepares a combined local test tree; it is not a combined CTAN upload. Normal school ZIP packaging is unchanged.

The output directory must not exist and must be outside the source checkout. Existing destinations, including symlinks, are refused. Input checks precede output creation. An I/O failure during writing may leave a partial new directory. The tool does not delete or overwrite caller data. Use a private parent without concurrent writers.

To include a separately built and reviewed class manual, add `--manual-pdf /path/to/dissertate-doc.pdf` to class staging. Font staging accepts `--font-manual-pdf /path/to/dissertate-historical-fonts-doc.pdf`. The tool checks each PDF file header and records its hash. It does not compile a manual or verify PDF/source correspondence. Source-only staging is also supported.

## Test with the separate font dependency

Use an existing TeX Live installation. Keep the document directory separate from both TDS trees, with no local class or font copies. Copy the synthetic example into a new document directory, then make both trees available to Kpathsea:

```sh
mkdir /tmp/dissertate-example
cp -R /tmp/dissertate-class/doc/latex/dissertate/examples/generic/. /tmp/dissertate-example/
cd /tmp/dissertate-example
TEXMFHOME='/tmp/dissertate-class:/tmp/dissertate-fonts' kpsewhich dissertate.cls
TEXMFHOME='/tmp/dissertate-class:/tmp/dissertate-fonts' xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -recorder main.tex
```

The colon-separated path example is for TeX Live on Unix-like systems. Check that the class resolves inside the class tree and that prefixed font filenames resolve inside the font tree. These command-specific settings do not install files globally. A separate-tree fixture compiled on TeX Live 2025/macOS. The class resolved from the class tree, and PDF-driver logs identified all ten historical fonts from the font tree as embedding sources. All used fonts were embedded. MiKTeX and complete dissertations remain unverified.

## Dependencies and resources

The runtime requires XeLaTeX, the separate `dissertate-historical-fonts` component, and these TeX packages: `etoolbox`, `geometry`, `ragged2e`, `graphicx`, `fixltx2e`, `lettrine`, `setspace`, `verbatim`, `color`, `xcolor`, `hyperref`, `url`, `amssymb`, `amsmath`, `mathspec`, `caption`, `microtype`, `fancyhdr`, `titlesec`, `titling`, `tocloft`, `appendix`, `natbib`, and `quotchap`. Modern LaTeX incorporates `fixltx2e`; the historical class still requests its compatibility package. Building the supplied manual separately requires `geometry`, `fontenc`, `lmodern`, `hyperref`, and `verbatim`.

The synthetic example exercises the title, body, fonts, caption, and an inline bibliography. It skips the Generic `\frontmatter` and `\backmatter` hooks. Authors using those hooks must supply `frontmatter/personalize.tex`, `frontmatter/abstract.tex`, `frontmatter/dedication.tex`, `frontmatter/thanks.tex`, `chapters/appendixA.tex`, `endmatter/personalize.tex`, and `references.bib`. The bibliography also requires BibTeX and `apalike2`. Supplied frontmatter files are empty placeholders. Both colophon toggles default to enabled in the base class; keep them disabled unless supplying separate colophon resources. No colophon text or artwork is included. A prior nine-page combined-tree check exercised both hooks with author resources and the colophon disabled. Citations, the appendix cross-reference, and contents entries resolved.

## Options, files, and licenses

Use `\documentclass[school=generic]{dissertate}`. Generic is the only school selection and the default. Paper options are `a4paper`, `letterpaper`, `dpaperafour`, and `dpaperletter`; spacing options are `dsingle` and `ddouble`. Defaults are US Letter and double spacing. Choose one paper setting and one spacing setting. Unsupported options produce class errors.

Class runtime files are under `tex/latex/dissertate/`. Original class/style inputs and the handwritten staging program are under `source/latex/dissertate/`. Documentation uses `dissertate-doc.tex` and `dissertate-doc.pdf`. The component manifest records input/output hashes. The original 2014 class header is retained alongside a dated transformation notice. No artwork, official guides, or legacy packages are included.

Project code, documentation, and synthetic examples use the repository's GNU Affero General Public License, version 3; its text is in the class notice directory. Font licensing is supplied by the separate font package. Inherited Palatino-bold and mono-italic substitutions remain. Preserved notices and successful compilation do not establish CTAN acceptance or TeX distribution inclusion. Local preparation does not submit, publish, or tag anything.

## Prepare source packages

Stage both components with their reviewed manual PDFs, then run `python3 scripts/prepare-ctan-source /path/to/stage /path/to/new-packages MAJOR.MINOR.PATCH`. The output contains separate `dissertate/` and `dissertate-historical-fonts/` source directories. Each has a README, version, package-specific manual PDF/source, original inputs, notices, and handwritten preparation programs. Generated runtime files, examples, and manifests are omitted. Class source contains no font binaries; font source contains no class/style files. A single-component stage produces only its own source package.

Each source package's README gives an independent `--reconstruct` command. Reconstruction copies finite inputs to a new source root and verifies written bytes against bytes read. It runs no staged program. Review those sources before invoking the staging tool. Historical font build sources and the manual build environment are not reconstructed. No distribution or submission occurs during reconstruction.
