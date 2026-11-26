# Dissertate historical fonts: local TDS component

The separate `dissertate-historical-fonts` package provides ten unchanged historical font files used by the `dissertate` LaTeX class. It contains no class or style files. External filenames begin with `dissertate-historical-`; font bytes and internal names are unchanged.

Prepare a new local font TDS tree with Python 3:

```sh
python3 scripts/stage-ctan-generic /path/to/Dissertate /path/to/new-font-tree --component fonts
```

The output parent must exist. The output must not exist and must be outside the source checkout. Staging refuses missing or symlinked sources and existing destinations. It never overwrites or deletes caller data. An I/O failure may leave partial new output; use a private parent without concurrent writers.

Add `--font-manual-pdf /path/to/dissertate-historical-fonts-doc.pdf` to copy a separately built and reviewed manual. Staging checks the PDF file header and records its hash; it does not compile the manual or verify PDF/source correspondence. The source is `docs/ctan-fonts/dissertate-historical-fonts-doc.tex`.

## Inventory and notices

- EB Garamond OTF: regular and italic, with the retained historical `COPYING` notice.
- EB Garamond TTF: bold and bold italic, with the separate `OFL.txt` notice.
- Lato TTF: regular, italic, bold, and bold italic, with the retained OFL text and embedded copyright/RFN metadata.
- Source Code Pro TTF: regular and bold, with the retained OFL notice and embedded copyright/RFN metadata.

All fonts retain SIL Open Font License, version 1.1, terms. The prefix changes only external filenames. Embedded notices remain intact, including Reserved Font Names Lato and Source. Font bytes are not rebuilt, renamed internally, or substituted. The preparation programs and documentation use the repository's GNU Affero General Public License, version 3; its text is retained separately. This does not replace the fonts' OFL terms.

Fonts are staged under `fonts/opentype/public/dissertate/` and `fonts/truetype/public/dissertate/`. Font documentation and notices are under `doc/fonts/dissertate-historical-fonts/`. The package-specific manual basenames are `dissertate-historical-fonts-doc.tex` and `dissertate-historical-fonts-doc.pdf`.

## Installation and limits

Make the font TDS tree available alongside the separate class tree. On TeX Live for Unix-like systems, set `TEXMFHOME='/path/to/class-tree:/path/to/font-tree'` for a test command. Check a prefixed font with `kpsewhich dissertate-historical-EBGaramond12-Regular.otf`; it must resolve in the font tree. Do not put local class or font copies in the test document directory.

A separate-tree fixture compiled on TeX Live 2025/macOS. The class resolved from the class tree, and PDF-driver logs identified all ten historical fonts from the font tree as embedding sources. All used fonts were embedded. MiKTeX and complete dissertations remain unverified. Historical font source-to-binary correspondence is not established by byte-preserving packaging.

To prepare source uploads, use `scripts/prepare-ctan-source` on a reviewed font stage with its manual PDF. It creates a separate `dissertate-historical-fonts/` source directory with unchanged fonts, notices, manual PDF/source, and handwritten preparation tools. Its README documents independent copy-only input reconstruction. The tool does not upload, create a release, or create a tag. CTAN acceptance and TeX distribution inclusion remain separate.
