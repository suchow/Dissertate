# Contributions, questions, and bug reports

Contributions, questions, and bug reports should be made on Github using pull requests and issues. Dissertate uses semantic versioning (semver.org). Submit questions here: https://github.com/suchow/Dissertate/issues/new. First take a look at the FAQ.

## Building distribution packages

[Download the repository ZIP](https://github.com/suchow/Dissertate/archive/refs/heads/master.zip) and extract it, or clone the repository. From the repository root (`Dissertate-master` if extracted from the ZIP), run:

```sh
python3 scripts/package-latex Harvard Dissertate-Harvard-LaTeX.zip
```

Pass the name of a school directory in `assets/schools/` as the first argument. Each supported directory contains `style.sty` and `agent-guidance.md`. The resulting ZIP contains the template sources, fonts, and school-specific guidance in `AGENTS.md`. Add `--compile` to include a PDF; this requires XeLaTeX and BibTeX. Extract the generated ZIP before editing the template.

## Distribution licenses

The repository software license is in `LICENSE`. Bundled fonts and artwork have separate terms:

- EB Garamond: `assets/fonts/EB Garamond/COPYING` for the original OTF faces and `OFL.txt` in the same directory for the contributed bold TTF faces.
- Lato: `assets/fonts/Lato/SIL Open Font License 1.1.txt`.
- Source Code Pro: `assets/fonts/Source Code Pro/OFL.txt`.
- Colophon illustration: `assets/latex-base/endmatter/colophon-image.LICENSE`.

Disabling the colophon image does not remove its file from a source ZIP. University guides and institutional artwork also require their own distribution review. The Toronto cover notice is in `assets/schools/Toronto/resources/cover.png.LICENSE`; the repository software license does not license university marks.

The school ZIPs are editable project templates. A CTAN installation layout remains to be defined. A CTAN submission still needs a defined package structure, a complete file inventory, and documentation with its source.

## Experimental CTAN staging

For a local Generic-only CTAN staging experiment, run `python3 scripts/stage-ctan-generic /path/to/Dissertate /path/to/new-output`. The output directory must not exist. The tool creates a TeX Directory Structure (TDS) tree with uniquely named historical font files, unchanged font bytes, license notices, and a hash manifest. It does not upload or release a package. Redistribution review, complete documentation, and compatibility checks remain required before submission. Existing school ZIP packaging is unchanged.

To include a separately built and reviewed manual PDF, add `--manual-pdf /path/to/manual.pdf` to the staging command. Staging checks the PDF file header and records its hash; it does not compile the manual or verify that the PDF matches the manual source. Without this option, the tree contains the manual source but no manual PDF.

To prepare a separate local source candidate, run `python3 scripts/prepare-ctan-source /path/to/reviewed-stage /path/to/new-source-output MAJOR.MINOR.PATCH`. The reviewed stage must include the manual PDF. The destination must not exist. This tool verifies the staged manifest and copies original sources, documentation, fonts, and notices into a source layout. It includes both preparation programs; the projection program also provides copy-only reconstruction. Generated runtime files, examples, and the manifest are omitted. The supplied version identifies the local candidate; this command does not create a tag, publish a release, or submit to CTAN. Redistribution review and CTAN acceptance remain unresolved.
