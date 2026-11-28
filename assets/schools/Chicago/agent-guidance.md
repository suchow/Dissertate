# Guidance for the University of Chicago Psychology Ph.D. template

The title-page model covers the ordinary Psychology Ph.D. in the Division of the Social Sciences. Other departments, divisions, and dual or joint programs require separate title-page verification. Check the current [Library formatting requirements](https://www.lib.uchicago.edu/research/scholar/phd/dissertation-requirements/format/), the [official title-page models](https://www.lib.uchicago.edu/research/scholar/phd/students/sample-title-pages/), and departmental instructions before submission.

The title wording and blank-line groups follow the official Psychology Word model. Title text is uppercase, regular weight, and 12 point. It uses the same EB Garamond font as the body. The model's Times New Roman is an example; the Library requires the title font to match the dissertation text.

Text stays within one-inch boundaries on all sides, with extra bottom clearance for descenders. Body text is double-spaced. Preliminary pages count consecutively in lowercase Roman numerals. Title, copyright, abstract, and dedication pages have no printed page numbers. Body pagination starts at Arabic 1. The supplied order is title, copyright, abstract, dedication, contents, figure and table lists, acknowledgments, body, appendix, references, and colophon.

Edit `frontmatter/personalize.tex` for the author's diploma name and other metadata. The sample uses December 2024. Replace this with the degree's quarter-end month and year: March, June, August, or December. The title page includes no honors-thesis wording or advisor header.

The supplied backmatter contains one appendix with an `Appendix: Title` heading and contents entry. Multiple appendices need numbered or lettered headings and corresponding contents entries; update the backmatter before adding them. References use single-spaced entries with space between entries. Omit an empty list of tables or figures when it does not apply.

The main document is `dissertation.tex`; chapters are in `chapters/`. The template uses XeLaTeX and BibTeX. Review every page after changing the metadata or layout, including wrapped titles, preliminary pages, quotations, figures, appendix headings, references, and the colophon. Formatting checks do not establish institutional acceptance or accessibility compliance.

Include an institutional logo or seal only when the applicable dissertation formatting rules require or recommend it. Use the specified mark and placement. When those rules are silent, omit institutional marks. Consult [UChicago's brand resources](https://creative.uchicago.edu/faqs/) before changing a mark.

The body keeps the house EB Garamond family, right-aligned chapter headings, and small-cap chapter titles. The Library’s general 12-point guidance limits the chapter number and title size; oversized house numerals are not enabled. Black text follows the Library’s explicit color rule. The title-page model governs the title page, not body heading alignment. Contents and figure/table lists retain the house title treatment and chapter-entry spacing. Chapter epigraphs remain in normal flow beneath the compact headings. These are design choices within the documented constraints, not a claim of submission acceptance.

The Library says to set one-inch margins on all sides, with no minimum-only qualification. The geometry override therefore remains: the shared 5.75-inch body width would change those specified margins. The additional bottom clearance protects descenders.
