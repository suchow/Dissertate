## Chicago dissertation template
This template matched the requirements of Chicago's Economics format, although most departments have a similar, if not identical, format. It is included in the directory.

## Citations
For citations, use the bibtex style "Chicago".

## Known Bugs
There is a minor bug regarding figure captions for full page figures. This is built on the Havard package. Harvard requires that full page figures be preceded by a page containing only a figure caption. I have modified the fltpage package to do this. Now the bug: on rare occasions, if LaTeX has many small floats in the queue, a second float can appear on the page that is supposed to have only the figure caption. This is a known bug in the fltpage package, see for example the comments in the original (unmodified) source: http://www.tex.ac.uk/CTAN/macros/latex/contrib/fltpage/fltpage.dtx
