An introduction
===============

This package provides all of the files needed to support the production and typesetting of a PhD thesis at Harvard. For contributions, comments, and bug reports, please contact Jordan Suchow at suchow@fas.harvard.edu.

Contributions were made by Andrew Leifer (leifer@fas.harvard.edu), and thanks to Clemens Eppner for the Ubuntu instructions.

Installation
============

### For Windows XP: ###

Download basic-miktex-2.9.4244.exe  http://miktex.org/
Download SumatraPDF v 1.5.1 http://blog.kowalczyk.info/software/sumatrapdf/free-pdf-reader.html
Download this Git Repo

Installatioan instructions:
Copy the contents of fonts\ into
C:\Program Files\MiKTeX 2.9\fonts\opentype\public\ChaparralPro

To complie, from the MSYS command prompt run:
xelatex -synctex=-1 thesis.tex


### For Mac OS X ###

Downlaod MacTex (when I tried, the main site was down so I used this mirror)
http://mirror.unl.edu/ctan/systems/mac/mactex/MacTeX.mpkg.zip
it should be roughly 2 GB
Install.

Install whatever fonts you'll be using in the usual way for OS X. For example, to install the included fonts, you can open the `fonts` directory, select all the font files, double click on any one of them, and then click the `Install font` button on the Font Book window that appears.

I use the free PDF reader Skim and the non-free editor TextMate. Both integrate well with latex:

Skim is available http://skim-app.sourceforge.net/
Set Skim->Preferences->Sync to the Preset "TextMate." You can command-shift-click in the PDF to pull up a line in the code in Textmate.

Now to setup TextMate, go to the Bundle->LaTex->Preferences and choose xelatex and Skim respectively.
Then go to Bundles->Latex-> File Preferences -> Set Master file and select your master file.. thesis.tex

To compile, from the terminal run:
xelatex  thesis

I also use Zotero http://www.zotero.org/ with the following modification to enable drag and drop cite keys:
For Bibtex Drag and Drop Functionality from Zotero see:
http://forums.zotero.org/discussion/5094/drag-and-drop-bibtex-cite/
and in particular:
http://pastebin.com/GXmCJevn

If this is your first time you are working with LaTeX in TextMate then you would need to install the LaTeX bundle first.
TextMate->Bundles->LaTeX: tick the box (the installation kicks in automatically)

### For Ubuntu ###

1. Installing xetex:

	sudo apt-get install texlive-xetex

2. Copy the fonts (from the template folder):

	sudo cp fonts/*/usr/local/share/fonts/

3. Add

	\aliasfontfeatureoption{Ligatures}{Historic}{Historical}

in harvard-thesis.cls just above the \setromanfont... command.
This is because the syntax changed at some point from "Historical" to
"Historic" but the ubuntu package is obviously a little behind. See
here: http://tug.org/pipermail/xetex/2010-September/018106.html

4. Run xelatex thesis.tex


General Links
=============

Harvard Approved Binding Sites:
http://www.acmebook.com/
http://www.lbibinders.org/index.php?option=com_content&view=article&id=32&Itemid=80

=======

Known Bugs
==========
There is a minor bug regarding figure captions for full page figures. Harvard requires that full page figures be preceded by a page containing only a figure caption. I have modified the fltpage package to do this. Now the bug: on rare occasions, if LaTeX has many small floats in the queue, a second float can appear on the page that is supposed to have only the figure caption. This is a known bug in the fltpage package, see for example the comments in the original (unmodified) source: http://www.tex.ac.uk/CTAN/macros/latex/contrib/fltpage/fltpage.dtx

License
=======

This software is free and is covered under the MIT License, given here:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
