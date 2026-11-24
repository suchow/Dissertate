# Contributions, questions, and bug reports

Contributions, questions, and bug reports should be made on Github using pull requests and issues. Dissertate uses semantic versioning (semver.org). Submit questions here: https://github.com/suchow/Dissertate/issues/new. First take a look at the FAQ.

## Building distribution packages

[Download the repository ZIP](https://github.com/suchow/Dissertate/archive/refs/heads/master.zip) and extract it, or clone the repository. From the repository root (`Dissertate-master` if extracted from the ZIP), run:

```sh
python3 scripts/package-latex Harvard Dissertate-Harvard-LaTeX.zip
```

Pass `Harvard`, `NYU`, `Princeton`, `Berkeley`, `Chicago`, or `Generic` as the first argument. The resulting ZIP contains the template sources, fonts, and school-specific guidance in `AGENTS.md`. Add `--compile` to include a PDF; this requires XeLaTeX and BibTeX. Extract the generated ZIP before editing the template.
