## Harvard dissertation template
This template matched the requirements of Harvard GSAS's document *Form of the PhD dissertation*, located at http://www.gsas.harvard.edu/images/stories/pdfs/form%20of%20dissertation.pdf and included in this directory.

## General Links
Harvard Approved Binding Sites:
- http://www.acmebook.com/
- http://www.lbibinders.org/index.php?option=com_content&view=article&id=32&Itemid=80

## Known Bugs
There is a minor bug regarding figure captions for full page figures. Harvard requires that full page figures be preceded by a page containing only a figure caption. I have modified the fltpage package to do this. Now the bug: on rare occasions, if LaTeX has many small floats in the queue, a second float can appear on the page that is supposed to have only the figure caption. This is a known bug in the fltpage package, see for example the comments in the original (unmodified) source: http://www.tex.ac.uk/CTAN/macros/latex/contrib/fltpage/fltpage.dtx
