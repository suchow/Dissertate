# Guidance for working with this dissertation

This template is for a Yale Graduate School of Arts and Sciences Ph.D. dissertation. Check the current [Registrar formatting guide](https://registrar.yale.edu/student-records/dissertations/dissertation-submission/dissertation-formatting-guide), its sample pages, and the department's instructions before changing the layout.

Keep 1-inch text margins, a consistent 10–12-point font family, double-spaced body text, and page numbers in the bottom-right corner about 0.5 inch from the edges. The title and copyright pages are counted as i and ii without printed numbers. The abstract begins at iii, followed by a lay summary of at most 250 words, the table of contents, and other preliminary sections. Body page numbering starts at 1. Single-space entries in the table of contents and bibliography, with double spacing between entries. Enable optional lists of figures and tables alongside the table of contents in the `\frontmatter` definition of `Dissertate.cls`.

Edit `frontmatter/personalize.tex` for the author's details and `resources/lay-summary.tex` for the lay summary. Use title case for the dissertation title and repeat it unchanged on the abstract page. Use the same author name on the title, copyright, and abstract pages. Add `\yalecommitteechair{...}` to the personalization file when the committee chair differs from the adviser. For December degrees, the copyright year is the following year; the template applies this rule when `\degreemonth{December}` is used.

The copyright-page placement in the Registrar's written guide differs from that in the sample PDF. This template uses the written instruction: the first line of the copyright notice is 3 inches below the top text margin. Confirm the placement before submission.

The main document is `dissertation.tex`; chapters are in `chapters/`. Preserve the author's text and verify changes in the compiled PDF. The template uses XeLaTeX and BibTeX. It sets text in EB Garamond, including headings and captions, to maintain a consistent font family.

Consult [Yale's identity guidance](https://yaleidentity.yale.edu/frequently-asked-questions) before adding institutional marks. Include an institutional logo or seal only when the applicable dissertation formatting rules require or recommend it. Use the specified mark and placement. When those rules are silent, omit institutional marks.
