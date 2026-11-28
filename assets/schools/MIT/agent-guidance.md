# Guidance for working with this dissertation

This template covers a single-author, single-degree MIT Ph.D. thesis. It does not implement joint authorship, dual degrees, co-supervisors, joint-institution programs, or a change of supervisor. Consult the current [MIT Libraries specifications](https://libraries.mit.edu/distinctive-collections/thesis-specs/) and your department before submission. Departmental rules may be stricter.

The title page counts as 1 without a printed number. Arabic numbering continues through the abstract, preliminaries, body, appendices, and references. Do not reset the body to 1. The abstract immediately follows the title page and is single-spaced, generally no more than 500 words. Acknowledgments, a biography if included, notes, and references are single-spaced. The template retains double-spaced body text unless `dsingle` is selected. US Letter paper, the configured margins, bottom-centered page numbers, and EB Garamond body text are template defaults. MIT suggests a sans serif font but explicitly does not require one. Mathematics retains the base class math fonts; review the PDF for consistent and embedded fonts.

In `frontmatter/personalize.tex`, set the title as submitted to the registrar, preferred author name, department, supervisor, and degree-conferral month and year. MIT conferral months are February, May or June, and September. Add these school fields after the existing personal details:

```tex
\mitpreviousdegrees{[Previous degrees, institutions, and years]}
\mitsubmissiondate{[Date presented to the department]}
\mitsupervisordepartment{[Supervisor department from MIT catalog]}
\mitsupervisortitle{[Supervisor title from MIT catalog]}
\mitacceptedby{[Current department or program officer]}
\mitacceptedtitle{[Current officer title]}
```

Use `\mitpreviousdegrees{}` if no previous degree information applies. Verify every officer name and title with the department; replace all placeholders before submission. The title page must fit on one page. The abstract includes the submission date, supervisor name, and supervisor title. No signed page is included in the final thesis PDF; obtain separate signature-page instructions from the department if required.

The title page includes the author’s copyright with the degree-award year and the current mandatory MIT permission legend. The default rights notice is “All rights reserved.” To select a Creative Commons license, replace it through `\mitrightsstatement{...}` with the chosen license name and URL after reviewing MIT's licensing guidance. Preserve the permission legend. The current written copyright rule governs the year, even when a sample uses a different year.

The main document is `dissertation.tex`. Edit the abstract in `frontmatter/abstract.tex`, acknowledgments in `frontmatter/thanks.tex`, and chapters in `chapters/`. The `\frontmatter` definition in the distributed `Dissertate.cls` includes both figure and table lists; remove a list only if the thesis contains none of that type. For a biography, create `resources/biography.tex` and enable its commented input. For supplemental materials, create `resources/supplemental-material.tex`, describe each file and the software needed to read it, and enable its commented input. Appendices and references remain within the consecutive page count.

The template uses XeLaTeX and BibTeX. Compiling with XeLaTeX does not validate PDF/A. The main specifications require PDF/A-1 and validation before submission, while the [PDF/A FAQ](https://libguides.mit.edu/mit-thesis-faq/pdfa) says regular PDF is accepted and PDF/A-1 is preferred. Follow the main specifications and confirm the current submission rule with the department. Convert from the source files through an appropriate PDF/A-1 workflow, then validate the resulting file separately with a PDF/A validator. No conversion or archival validation is provided by this template. Inspect embedded fonts, metadata, hyperlinks, figures, and equations after conversion, and retain the validation report. Do not encrypt the submitted PDF or embed multimedia. Follow MIT's file-naming scheme and submit matching thesis metadata to the Libraries.

Consult the [MIT Brand Guide](https://brand.mit.edu/logos-marks) before adding institutional branding. Include an institutional logo or seal only when the applicable dissertation formatting rules require or recommend it. Use the specified mark and placement. When those rules are silent, omit institutional marks.

The template retains the Harvard/Generic typography: EB Garamond body and smallcaps, Lato captions, oversized chapter numerals, and the original chapter-epigraph composition. MIT Red `#750014` supplies title, chapter-number, citation, and URL accents ([current palette](https://brand.mit.edu/color)). These are discretionary design choices. The Institute-wide rules do not prescribe heading size, heading composition, or black text throughout. Departmental requirements can narrow these choices. The school overrides preserve required title and abstract fields, alignment, consecutive pagination, and single spacing for the sections named above. Lists retain the base compressed spacing.

The body retains the house text width of 5.75 inches, centered horizontally on US Letter paper. The wider side margins preserve the school constraints described above.

The optional colophon follows the references and appendices. No inspected rule explicitly requires the bibliography to be the final page in this edition.
