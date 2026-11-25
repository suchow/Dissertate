# Dissertate Generic: local TDS candidate

This experimental staging tool prepares the Generic class and a synthetic example for local testing. Redistribution review remains unresolved. The tool does not submit to CTAN or publish a release. Package-manager availability remains unestablished.

## Stage from source

Run with Python 3 and a Dissertate source checkout:

```sh
python3 /path/to/Dissertate/scripts/stage-ctan-generic /path/to/Dissertate /tmp/dissertate-candidate
```

The output parent must exist. The output directory must be new and outside the source checkout. Existing destinations, including symlinks, are refused. Unexpected source patterns are rejected before output creation. An I/O failure during writing can leave a partial new directory; the tool does not delete or overwrite caller data. Use a private output parent without concurrent writers.

## Test in isolation

The output is a TeX Directory Structure (TDS) tree. With an existing TeX Live installation and XeLaTeX dependencies, set `TEXMFHOME` for each test command. Keep the document directory separate from the tree, with no local class or font copies. For example, with a new `/tmp/dissertate-example` directory:

```sh
mkdir /tmp/dissertate-example
cp -R /tmp/dissertate-candidate/doc/latex/dissertate/examples/generic/. /tmp/dissertate-example/
cd /tmp/dissertate-example
TEXMFHOME=/tmp/dissertate-candidate kpsewhich dissertate.cls
TEXMFHOME=/tmp/dissertate-candidate xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -recorder main.tex
```

Check that the class resolves inside the candidate tree. This temporary environment setting does not install files globally. Dependencies are not supplied or installed by the staging tool.

## Dependencies and resource scope

Preparation requires Python 3. The runtime requires XeLaTeX and these TeX packages: `etoolbox`, `geometry`, `ragged2e`, `graphicx`, `fixltx2e`, `lettrine`, `setspace`, `verbatim`, `color`, `xcolor`, `hyperref`, `url`, `amssymb`, `amsmath`, `mathspec`, `caption`, `microtype`, `fancyhdr`, `titlesec`, `titling`, `tocloft`, `appendix`, `natbib`, and `quotchap`. Modern LaTeX incorporates `fixltx2e`; the historical class still requests its compatibility package. The ten bundled historical fonts remain required. Building the supplied manual separately requires `geometry`, `fontenc`, `lmodern`, `hyperref`, and `verbatim`.

The supplied example exercises the title, body, fonts, caption, and an inline bibliography. It skips the Generic `\frontmatter` and `\backmatter` hooks. Authors using those hooks must supply `frontmatter/personalize.tex`, `frontmatter/abstract.tex`, `frontmatter/dedication.tex`, `frontmatter/thanks.tex`, `chapters/appendixA.tex`, `endmatter/personalize.tex`, and `references.bib`. The bibliography also requires BibTeX and the `apalike2` style. The four supplied frontmatter files are empty placeholders. Colophon toggles default to enabled in the base class; keep both disabled unless supplying the separate colophon resources. This candidate supplies no colophon text or artwork. Full-hook behavior remains untested.

## Class and files

Use `\documentclass[school=generic]{dissertate}`. Generic is the only school selection and the default. Accepted paper options are `a4paper`, `letterpaper`, `dpaperafour`, and `dpaperletter`; spacing options are `dsingle` and `ddouble`. Defaults are US Letter and double spacing. Choose one paper setting and one spacing setting. The loader reports unsupported options as class errors.

The tree contains a loader, shared base, and Generic style under `tex/latex/dissertate/`. Editable synthetic resources are under `doc/latex/dissertate/examples/generic/`. The example disables the colophon and its image. Artwork, official guides, site files, and legacy packages are excluded. Normal school ZIP packaging is unchanged.

Ten historical font files have unique `dissertate-historical-` filenames in the OpenType and TrueType TDS subtrees. Their bytes and internal font names are unchanged. The candidate retains the historical fonts. `doc/latex/dissertate/candidate-manifest.json` records source hashes, original and prefixed font paths, and payload hashes. The manifest excludes its own hash. Notices are in the adjacent `notices/` directory; the generator source is under `source/latex/dissertate/`.

## Validation limits

A clean Generic example compiled under TeX Live 2025 on macOS. PDF-driver logs identified all ten exercised historical font files as embedding sources. Those files matched the manifest hashes. This verifies the exercised filename lookup and embedding behavior. Existing Palatino-bold and mono-italic shape substitutions remain; the log reports them. MiKTeX and full dissertation behavior have not been verified. The synthetic example does not demonstrate university compliance or PDF accessibility. Preserved notices and successful compilation do not establish redistribution permission.

To include a separately built and reviewed manual PDF, add `--manual-pdf /path/to/manual.pdf` to the staging command. Staging checks the PDF file header and records its hash; it does not compile the manual or verify that the PDF matches the manual source. Without this option, the tree contains the manual source but no manual PDF.

## Licenses

Project code, documentation, and synthetic examples are distributed under the repository’s GNU Affero General Public License, version 3. Fonts retain their separate SIL Open Font License, version 1.1, terms. Preserve the accompanying font notices and embedded copyright and Reserved Font Name metadata. The external filename prefix leaves font bytes and internal font names unchanged. This candidate remains subject to redistribution review; local staging does not submit it to CTAN or publish a release.

## Reconstruct candidate inputs

The candidate includes the original base-class and Generic-style bytes under `source/latex/dissertate/inputs/`, alongside the generator. The original files use unique staged filenames to avoid case-insensitive filename collisions. To recreate the generator input tree, copy `dissertate-base-original.cls` to `assets/latex-base/Dissertate.cls` and `dissertate-school-generic-original.sty` to `assets/schools/Generic/style.sty`. Copy the candidate README and manual source to `docs/ctan-generic/`. For each manifest font entry, copy the file at its prefixed path to its original path and verify its SHA-256 hash. Restore each notice using the explicit `NOTICES` list in the generator; do not infer paths by splitting flattened filenames. Copy the generator to `scripts/stage-ctan-generic`, then stage into a new directory. Supply any included manual PDF separately with `--manual-pdf`. The option copies the PDF without rebuilding it. These steps reconstruct candidate inputs, not the full repository, historical font build sources, or the manual build environment. Rights review and CTAN acceptance remain separate.
