# Guidance for working with this dissertation

This template covers Columbia GSAS Ph.D. dissertations. DES and other degrees require their own title wording. Consult the current [GSAS guide](https://www.gsas.columbia.edu/content/formatting-guidelines-and-dissertation-template) and its linked samples before changing the layout.

Use Letter paper with equal left and right margins of at least 1 inch. Center page numbers at the bottom, at least 0.75 inch from the bottom edge. Double-space text, abstract, dedication, acknowledgments, and contents. Single-space footnotes and bibliography entries, with double spacing between entries. Indent and single-space quotations of eight lines or more.

Title, copyright, and abstract pages are unnumbered and excluded from counting. Contents begin at Roman i; the preface or body begins at Arabic 1. References precede appendices. Remove unused lists of figures or tables from the school style’s `\frontmatter` definition.

Edit `frontmatter/personalize.tex`. Set the conferral year with `\degreeyear{...}` and, when different, the manuscript year with `\columbiacopyrightyear{...}`. Preserve the author's text. Compile with XeLaTeX and BibTeX, inspect the PDF, and check font embedding. Keep the abstract free of images, abbreviations, and formulae.

Consult Columbia’s [brand guide](https://visualidentity.columbia.edu/branding) before adding institutional branding. Include an institutional logo or seal only when the applicable dissertation formatting rules require or recommend it. Use the specified mark and placement. When those rules are silent, omit institutional marks.

## House design and school overrides

The [GSAS guide](https://www.gsas.columbia.edu/content/formatting-guidelines-and-dissertation-template) permits legible standard serif or sans-serif fonts. Arial and Times New Roman are preferred examples. Ornamental and script fonts are excluded. Retain the embedded EB Garamond body, Lato captions, house small caps, original large chapter numeral, and original epigraph composition. The guide does not specify chapter-number size or color. Dark blue `1D4F91` comes from the university’s [official color palette](https://visualidentity.columbia.edu/content/color); using it for limited chapter and link accents is a design choice. The title and abstract page appearance remains unchanged pending comparison with the official samples.

The centered 5.75-inch text block has 1.375-inch lateral margins on Letter paper. The one-inch top margin, 1.1-inch bottom text margin, and 0.2-inch footer skip preserve clearance for the centered page number. Disabling microtype protrusion prevents punctuation from extending beyond the text block. Check all chapter decoration against the physical margin in the rendered PDF.

The school overrides retain double body and ordinary-list spacing, single compressed quotations, single bibliography entries with double gaps, and additional footnote separation. These implement the GSAS spacing instructions. Base contents fonts and chapter-entry spacing are restored; the contents remains double-spaced. Required preliminary order, uncounted cover pages, Roman preliminary numbers, Arabic body numbers, the copyright-year distinction, and references before appendices remain in place. The bibliography link targets its heading. The optional illustrated colophon follows the appendices and uses single spacing.

These changes require a fresh rendered review. Font embedding, margin clearance, contents spacing, title-page wrapping, and epigraph placement have not been established by source inspection alone.
