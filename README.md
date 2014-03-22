# Dissertate: a LaTeX dissertation template

This package provides all the files needed to support the production and typesetting of a PhD dissertation at Harvard, Princeton, and NYU, though it can easily be adapted to meet the requirements of other schools. The format and styling is based closely on the requirements published by each university's registrar.


## Getting started
1. Install LaTeX (see below for basic instructions for Mac OS X, Windows, and Ubuntu).
1. Install the default font, EB Garamond and Lato. The files are provided in `fonts/EB Garamond`, `fonts/Lato`, and `fonts/Source Code Pro`.
2. Pick your school by editing line 26 of `dissertate.cls` to use the package `Harvard`, `Princeton`, or `NYU`. Then install the relevant package, located in `packages/`, either in the usual LaTeX way or by moving everything in that folder into the top level directory with `Dissertate.cls`.
3. Personalize the document by filling out your name and all the other info in the file `frontmatter/personalize.md`.
4. Build your dissertation with `build.command`, located in the `scripts` directory (e.g., you can `cd` into the main directory and then run `./scripts/build.command`).


## Contributions, questions, and bug reports
Contributions, questions, and bug reports should be made on Github using pull requests and issues. Dissertate uses semantic versioning (semver.org). Submit questions here: https://github.com/suchow/Dissertate/issues/new. First take a look at the FAQ:

## FAQ

### How do I make the text justified instead of ragged right?
Remove or comment out the line `\RaggedRight` from the .cls file.

## Acknowledgments
Thanks to Andrew Leifer for many code and README contributions and to Clemens Eppner for the Ubuntu instructions.

## Basic LaTeX installation instructions

### Windows XP ###
1. Download basic-miktex-2.9.4244.exe  http://miktex.org/
2. Download SumatraPDF v 1.5.1 http://blog.kowalczyk.info/software/sumatrapdf/free-pdf-reader.html
3. Download this Git Repo
4. Copy the contents of `fonts\` into
`C:\Program Files\MiKTeX 2.9\fonts\opentype\public\EB Garamond`
5. To complie, from the MSYS command prompt run:
`xelatex -synctex=-1 thesis.tex`

### Mac OS X ###
1. Downlaod MacTex (http://tug.org/mactex/). It's big, roughly 2 GB.
2. To compile, from the terminal (e.g., Terminal.app) run: `xelatex thesis`

Install whatever fonts you'll be using in the usual way for OS X. For example, to install the included fonts, you can open the `fonts` directory, select all the font files, double click on any one of them, and then click the `Install font` button on the Font Book window that appears.

### Ubuntu ###
1. Install xetex: `sudo apt-get install texlive-xetex`
2. Copy the fonts (from the template folder): `sudo cp fonts/*/usr/local/share/fonts/`
3. Add `\aliasfontfeatureoption{Ligatures}{Historic}{Historical}` in harvard-thesis.cls just above the \setromanfont... command. This is because the syntax changed at some point from "Historical" to "Historic" but the Ubuntu package is obviously a little behind. See here: http://tug.org/pipermail/xetex/2010-September/018106.html.
4. Run `xelatex thesis.tex`.
