# Guidance for working with this UC Berkeley dissertation

Check the current [Berkeley dissertation writing and filing guidance](https://grad.berkeley.edu/academics/degree-progress/dissertation/) and the student's department instructions before changing the layout. Check the required page order, margins, pagination, font sizes, and PDF accessibility. Berkeley's guidance states that dissertations submitted from April 2026 must meet WCAG 2.1 Level AA. A successful LaTeX build alone does not establish accessibility or submission compliance.

Use US Letter paper, black 12-point body text, and single spacing throughout the manuscript. Keep text at least 1 inch from each paper edge and page numbers at least 0.75 inch from the edge. Match the official title and abstract samples. The title and copyright pages are uncounted and unnumbered. Number the abstract separately with Arabic numerals starting at 1. Number subsequent preliminary pages with lowercase Roman numerals starting at i. Begin body pagination at Arabic 1.

Consult [Berkeley's logo guidance](https://brand.berkeley.edu/visual-identity/logos/) before adding or changing an institutional mark.

Edit `frontmatter/personalize.tex` for the author's details. The main document is `dissertation.tex`; chapters are in `chapters/`. Keep the author's text intact when adjusting layout or metadata. Follow current university and department rules where the template differs, and verify changes in the compiled PDF. The template uses XeLaTeX and BibTeX.

Include an institutional logo or seal only when the applicable dissertation formatting rules require or recommend it. Use the specified mark and placement. When those rules are silent, omit institutional marks.
