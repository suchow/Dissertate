LaTeX template for a Harvard Dissertation
===============

This package provides all the files needed to support the production and typesetting of a PhD dissertation at Harvard. The format and styling is based closely on GSAS's document *Form of the PhD dissertation* (http://www.gsas.harvard.edu/images/stories/pdfs/form%20of%20dissertation.pdf). Contributions and bug reports should be made on Github using pull requests and issues.

Basic installation instructions
============

### Windows XP ###

1. Download basic-miktex-2.9.4244.exe  http://miktex.org/
2. Download SumatraPDF v 1.5.1 http://blog.kowalczyk.info/software/sumatrapdf/free-pdf-reader.html
3. Download this Git Repo
4. Copy the contents of `fonts\` into
`C:\Program Files\MiKTeX 2.9\fonts\opentype\public\ArnoPro`
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


General Links
=============

Harvard Approved Binding Sites:
- http://www.acmebook.com/
- http://www.lbibinders.org/index.php?option=com_content&view=article&id=32&Itemid=80

Known Bugs
==========
There is a minor bug regarding figure captions for full page figures. Harvard requires that full page figures be preceded by a page containing only a figure caption. I have modified the fltpage package to do this. Now the bug: on rare occasions, if LaTeX has many small floats in the queue, a second float can appear on the page that is supposed to have only the figure caption. This is a known bug in the fltpage package, see for example the comments in the original (unmodified) source: http://www.tex.ac.uk/CTAN/macros/latex/contrib/fltpage/fltpage.dtx


Acknowledgments
=======

Thanks to Andrew Leifer for many code and README contributions and to Clemens Eppner for the Ubuntu instructions.


License
=======

This software is free and is covered under the MIT License, given here:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
