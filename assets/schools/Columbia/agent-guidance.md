# Guidance for working with this dissertation

This template covers Columbia GSAS Ph.D. dissertations. DES and other degrees require their own title wording. Consult the current [GSAS guide](https://www.gsas.columbia.edu/content/formatting-guidelines-and-dissertation-template) and its linked samples before changing the layout.

Use Letter paper with equal left and right margins of at least 1 inch. Center page numbers at the bottom, at least 0.75 inch from the bottom edge. Double-space text, abstract, dedication, acknowledgments, and contents. Single-space footnotes and bibliography entries, with double spacing between entries. Indent and single-space quotations of eight lines or more.

Title, copyright, and abstract pages are unnumbered and excluded from counting. Contents begin at Roman i; the preface or body begins at Arabic 1. References precede appendices. Remove unused lists of figures or tables from the `\frontmatter` definition in `Dissertate.cls`.

Edit `frontmatter/personalize.tex`. Set the conferral year with `\degreeyear{...}` and, when different, the manuscript year with `\columbiacopyrightyear{...}`. Preserve the author's text. Compile with XeLaTeX and BibTeX, inspect the PDF, and check font embedding. Keep the abstract free of images, abbreviations, and formulae.

Consult Columbia’s [brand guide](https://visualidentity.columbia.edu/branding) before adding institutional branding. Add a seal or logo only when the author requests it and the applicable guidelines allow it.
