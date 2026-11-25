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
