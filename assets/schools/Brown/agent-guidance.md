# Guidance for working with this dissertation

This template is for a Brown Graduate School Ph.D. dissertation. Check the current [dissertation guidelines](https://graduateschool.brown.edu/academics/rules-regulations/dissertation-guidelines) and linked [signature](https://graduateschool.brown.edu/sites/default/files/pdfs/Sample%20-%20Dissertation%20Signature%20Page.pdf), [copyright](https://graduateschool.brown.edu/sites/default/files/pdfs/Sample%20-%20Dissertation%20Copyright%20Notice.pdf), and [abstract](https://graduateschool.brown.edu/sites/default/files/pdfs/Sample%20-%20Dissertation%20Abstract%20-%20updated.pdf) samples before changing the layout. The samples show a 1.5-inch left margin and 1-inch remaining margins. US Letter is the template’s paper choice. Its bottom margin is 1.1 inches to keep footnote text inside the sample’s one-inch boundary.

Use double-spaced text and a standard 10-, 11-, or 12-point font. Block quotations, captions, long headings, and footnotes may be single-spaced, with blank lines between items. The title page counts as i and the copyright page as ii; neither has a printed number. The signature page is iii, followed by the curriculum vitae at iv, preface and acknowledgments, contents, tables, and illustrations. Longer sections continue the count. Center Roman preliminary numbers 0.75 inch above the bottom edge; the body starts at Arabic 1. Omit running headers. Major-section headings are centered, uppercase, and two inches from the top.

Set the author, title, department, and actual degree-conferral month and year in `frontmatter/personalize.tex`. The main file is `dissertation.tex`; chapters are in `chapters/`. Use `resources/biography.tex` for the CV. Exclude birth details and phone numbers. The template omits a dedication from the prescribed preliminary sequence. The title-page composition is a template choice; the linked samples cover the other three pages.

Configure `\brownsignatures{...}` in `frontmatter/personalize.tex`. Include the director, every reader, and dean approval in the order shown in the signature sample. Each `\brownsignatureentry{Typed Name}{Role}` prints blank date and signature lines. Insert “Recommended to the Graduate Council” before the readers and “Approved by the Graduate Council” before the dean. Confirm the current dean's name before submission. Submit a signed signature page separately; the ETD copy is unsigned. This template does not generate signatures.

The included `abstract.tex` is beside `dissertation.tex`. Compile it as a separate document. Its contents are:

```tex
\documentclass{Dissertate}
\begin{document}
\input{frontmatter/personalize}
\brownabstractpage
\end{document}
```

Compile it with XeLaTeX. The abstract is excluded from the dissertation PDF and contents. Keep it double-spaced. Limit it to 350 words and 2,450 characters, counting spaces and punctuation toward the character limit. The template does not enforce these limits. The header uses the configured conferral month, including February or October when applicable.

Preserve the author's text and inspect the compiled PDF after changes. Use XeLaTeX and BibTeX for the main document. Consult Brown's [visual identity policy](https://policy.brown.edu/policy/visual-identity) and [identity standards](https://ouc.brown.edu/logos-identity/visual-identity-policy-and-standards) before adding institutional branding. Include an institutional logo or seal only when the applicable dissertation formatting rules require or recommend it. Use the specified mark and placement. When those rules are silent, omit institutional marks.

## Design choices

The [Graduate School guide](https://graduateschool.brown.edu/academics/rules-regulations/dissertation-guidelines) requires centered uppercase major headings two inches from the top. The template preserves that layout and uses 12-point headings and chapter labels. Oversized numbers remain unresolved under the guide’s broad size wording. Contents entries retain house small caps; their page heading remains uppercase. Accents use [Brown #4E3629](https://policy.brown.edu/sites/default/files/policy/related/Brown_Visual_Identity_Policy_2016-07-22.pdf). The dissertation guide does not prohibit color.

The [signature sample](https://graduateschool.brown.edu/sites/default/files/pdfs/Sample%20-%20Dissertation%20Signature%20Page.pdf) labels the margins. Applying those margins throughout is a conservative template choice. The optional colophon requires review against the broad size wording, particularly its drop cap.

The optional colophon follows the references and appendices. No inspected rule explicitly requires the bibliography to be the final page in this edition.
