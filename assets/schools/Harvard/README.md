## Harvard dissertation template
Consult the current [Harvard Griffin GSAS dissertation formatting guidance](https://gsas.harvard.edu/resource/dissertation-formatting-guidance) and your department instructions before submitting. The included `guidelines.pdf` is an older reference.

## Full-page figures and tables
Full-page figures and tables use the independently implemented `dissertate-fullpage` package. Load it with `\usepackage{dissertate-fullpage}` after `\documentclass{Dissertate}` in `dissertation.tex`. The legacy `fltpage2` package name loads this implementation. A full-page environment flushes earlier floats. Its caption occupies the next page alone; the image or table occupies the following page. Later body text begins on a new page.

With the `twoside` package option, a blank page is inserted when necessary to put the caption on an even page facing the content on an odd page. Use `\caption[Short title]{Full caption}` and `\label{...}` inside `FPfigure` or `FPtable`. The content page repeats the number and optional short title. Ordinary float placement arguments such as `[h]` are unsupported. Leave room for the short heading when sizing the content.
