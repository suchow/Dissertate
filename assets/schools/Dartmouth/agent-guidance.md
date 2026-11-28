# Guidance for working with this dissertation

This template is for a Guarini School of Graduate and Advanced Studies Doctor of Philosophy thesis at Dartmouth College, using the general title-page sample. Engineering Sciences and MALS have separate title-page samples and are outside this template’s scope. Consult the [Guarini thesis guidelines, updated March 5, 2026](https://graduate.dartmouth.edu/sites/graduate_studies.prod/files/graduate_studies/wysiwyg/thesis_guidelines_5.pdf), and the current [graduation forms and submission instructions](https://graduate.dartmouth.edu/academics/graduate-school-forms/thesis-and-dissertation-forms) before editing.

Use US Letter paper, a 1.5-inch left margin, and top, bottom, and right margins between 0.5 and 1 inch. The template sets the latter three to 1 inch. Text must be at least 11 points, with line spacing of at least 18 points. Footnotes and long quotations may use closer spacing. The template uses 12-point text and one-and-a-half spacing. Keep figures, tables, and appendices within the margins.

The title page counts as Roman i without a printed number. The second page is blank, uncounted, and unnumbered. To place a copyright notice on that page, add `\toggletrue{DartmouthCopyright}` to `frontmatter/personalize.tex`. The abstract begins at ii and must not exceed 350 words. A preface with acknowledgments, table of contents, list of tables, and list of illustrations follow. The main text begins at Arabic 1; numbering continues through the appendices and references. Page numbers are centered at the bottom. Leave space between reference entries.

In `frontmatter/personalize.tex`, set the title and author. Set `\department` to the approved major. Set `\degreemonth` and `\degreeyear` to the month and year of defense. Set the examining committee with `\dartmouthcommittee{(chair) Name\\Name\\Name\\Name}`. Set the dean’s name with `\dartmouthdean{...}` after checking the current official sample. The dean field contains a placeholder. Verify the current dean and replace every dean and committee placeholder before submission. Submit an unsigned thesis to Dartmouth Digital Commons and the separately signed title page to Guarini, following the current administrative instructions.

Previously published or submitted articles require separate attention. The guide permits reproducing their submitted or published layout within its specified margins. For work with multiple authors, include the required introductory account of author roles and copyright compliance. The template does not add that account automatically.

Edit `frontmatter/abstract.tex` and `frontmatter/thanks.tex` for the abstract and preface. The main document is `dissertation.tex`; chapters are in `chapters/`. To omit unused lists, edit the `\frontmatter` definition in the distributed `Dissertate.cls`. Preserve the author’s text and inspect the compiled PDF, including long titles and committee lists. The template uses XeLaTeX and BibTeX.

Consult Dartmouth’s [design guidelines](https://communications.dartmouth.edu/design-guidelines) before adding institutional branding. Include an institutional logo or seal only when the applicable dissertation formatting rules require or recommend it. Use the specified mark and placement. When those rules are silent, omit institutional marks.

## Design choices

The [Guarini guide](https://graduate.dartmouth.edu/sites/graduate_studies.prod/files/graduate_studies/wysiwyg/thesis_guidelines_5.pdf) sets text size, leading, margins, preliminary pages, and pagination. It does not specify chapter-number size or prohibit color. The template retains the house chapter numbers, heading spacing, epigraph placement, and contents styling. Its accents use [Dartmouth Green #00693E](https://alumni.dartmouth.edu/communicating-your-class). The colophon is optional; the guide does not address it.

The optional colophon follows the references and appendices. No inspected rule explicitly requires the bibliography to be the final page in this edition.
