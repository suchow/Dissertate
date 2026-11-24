## Harvard dissertation template
Consult the current [Harvard Griffin GSAS dissertation formatting guidance](https://gsas.harvard.edu/resource/dissertation-formatting-guidance) and your department instructions before submitting. The included `guidelines.pdf` is an older reference.

## Known Bugs
There is a minor bug regarding figure captions for full page figures. Harvard requires that full page figures be preceded by a page containing only a figure caption. I have modified the fltpage package to do this. Now the bug: on rare occasions, if LaTeX has many small floats in the queue, a second float can appear on the page that is supposed to have only the figure caption. This is a known bug in the fltpage package, see for example the comments in the original (unmodified) source: https://ctan.org/pkg/fltpage
