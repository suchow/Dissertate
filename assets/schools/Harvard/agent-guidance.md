# Guidance for working with this Harvard dissertation

Check the current [Harvard Griffin GSAS dissertation formatting guidance](https://gsas.harvard.edu/resource/dissertation-formatting-guidance) and the student's department instructions before changing the layout. The guidance links to the GSAS formatting policy and includes recommendations. Check the table of contents, preliminary pages, pagination, margins, and embedded fonts in the PDF.

Harvard requires the signed Thesis Acceptance Certificate as the first page of the submitted PDF. The certificate has no printed page number and is excluded from the preliminary-page count. For submission, add `\harvardacceptancecertificate{certificate.pdf}` after `\documentclass{Dissertate}` in `dissertation.tex`. Replace `certificate.pdf` with the path to the completed certificate. You may omit the certificate while writing. The title page remains i, the copyright page ii, and the abstract page iii.

For Harvard names and marks, consult the [Harvard name and insignia policies](https://trademark.harvard.edu/pages/policies-forms).

Edit `frontmatter/personalize.tex` for the author's details. The main document is `dissertation.tex`; chapters are in `chapters/`. Keep the author's text intact when adjusting layout or metadata. Follow current university and department rules where the template differs, and verify changes in the compiled PDF. The template uses XeLaTeX and BibTeX.

Include an institutional logo or seal only when the applicable dissertation formatting rules require or recommend it. Use the specified mark and placement. When those rules are silent, omit institutional marks.
