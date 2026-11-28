# Penn standard Ph.D. dissertations

This template covers portrait-only Ph.D. dissertations at the University of Pennsylvania with the standard title page. Francophone, Italian and Germanic Studies, Wharton, and Social Welfare title variants are excluded. Use the current graduate-group instructions for those programs.

The [Provost formatting page](https://provost.upenn.edu/for-students/graduate-and-professional-education/graduate-degrees/phd-students/dissertation-formatting/) identifies the Spring 2023 Ph.D. Dissertation Formatting Guide as its source of requirements. The linked Guide 15 is dated January 18, 2023. The [current title-page examples](https://provost.upenn.edu/for-students/graduate-and-professional-education/graduate-degrees/phd-students/sample-dissertation-title-page/) supply the standard title wording. Verify current requirements before deposit.

## Fields and pages

In `frontmatter/personalize.tex`, set the title and author. Set `\department` to the official graduate group, `\degreeyear` to the deposit year, and `\advisor` to the supervisor’s name. The author name must match Path@Penn. Use the full title consistently on the title, copyright, and abstract pages. Set these additional fields:

```tex
\pennsupervisortitle{[FULL FACULTY TITLE, RANK AND DEPARTMENT]}
\penngraduatechair{[FULL NAME], [FULL FACULTY TITLE, RANK AND DEPARTMENT]}
\penncommittee{[FULL NAME], [FULL FACULTY TITLE, RANK AND DEPARTMENT]\\
  [EXTERNAL MEMBER NAME], [FULL FACULTY TITLE AND AFFILIATION]}
\pennlegalname{[FULL LEGAL NAME INCLUDING FULL MIDDLE NAME]}
```

List every committee member. Include named professorships and external affiliations where applicable. Format academic credentials consistently across all names. The graduate group chair is a separate field from the supervisor. For a co-supervisor, redefine `\penncosupervisor` to the name and `\penncosupervisortitle` to the full faculty title. Replace every placeholder before submission. Signatures are optional; this template supplies an unsigned title page. If signatures are included, both supervisors, if applicable, and the graduate group chair must sign.

The title page counts as Roman i without a printed number. The optional copyright page counts as ii without a printed number. Copyright is enabled by default; `\penncopyrightfalse` omits it, and the following page becomes ii. The copyright page prints the uppercase title, COPYRIGHT, deposit year, and full legal name on four lines. It contains no copyright symbol. Add an optional Creative Commons note only after selecting the appropriate license.

The dedication is italic, has no heading, and has no table-of-contents entry. Acknowledgment, abstract, contents, required lists, and optional preface follow. Disable an unused dedication or acknowledgment with an empty redefinition of `\penndedication` or `\pennacknowledgments`. Redefine `\pennlists` to include only the required lists: tables if the main text has tables, and figures if it has illustrations. A preface may be added with `\renewcommand{\pennpreface}{\pennfrontsection{PREFACE}{frontmatter/preface}}`. Additional preliminary sections are outside this scope; field-specific abbreviation lists belong in appendices.

The abstract is double-spaced, with ABSTRACT, the uppercase dissertation title, author name, and supervisor name. Supervisor names here have no academic titles or degrees. The 350-word maximum includes the title and all names in the header. Body pagination begins at Arabic 1 and continues through appendices, bibliography, and any index. An index is required for Architecture, City and Regional Planning, Earth and Environmental Science, East Asian Languages and Civilizations, and Near Eastern Languages and Civilizations; authors in those groups must add one after the bibliography.

## Layout and submission

US Letter pages have one-inch left, right, and top margins. The body ends 1.4 inches above the bottom edge to leave space for the bottom-centered page number above the required one-inch blank bottom margin. All material, including footnotes, figures, and page numbers, must remain inside the one-inch boundary. Running heads are omitted. Preliminary and chapter headings are uppercase; chapters and appendices have numbers or letters and titles. Guide 15 permits headings up to 36 points without excessive spacing. The table of contents distinguishes appendices from chapters.

The template uses black 12-point body text and double spacing for body text, preliminary pages, ordinary lists, and the bibliography. The guide recommends double spacing; lists of tables and figures may also be single-spaced. Footnotes and long quotations are single-spaced. Footnotes use continuous Arabic numbering across chapters. Do not mix footnotes and chapter endnotes. Use at least 8-point type for footnotes, figures, citations, charts, and graphs. The guide recommends Arial, Calibri, Georgia, or Times New Roman; these are recommendations, not an exclusive list. Inspect the final PDF for embedded fonts and legibility.

Landscape formatting is not implemented. Guide 15 says landscape margins are one inch on all sides, but the [live FAQ](https://provost.upenn.edu/for-students/graduate-and-professional-education/graduate-degrees/grad-degrees-faqs/) specifies a 1.5-inch top margin. This conflict remains unresolved. Obtain current guidance before adding landscape pages.

Submit a PDF through ETD Administrator and inspect every converted page. Formatting checks do not establish acceptance, accessibility, copyright permission, or completion of deposit requirements. For previously published material, obtain committee and graduate group chair approval, secure required permissions, disclose the publication under the chapter title, and describe the individual contribution to joint work. Upload permission letters as the supplemental file specified by the guide.

No logo or seal is included. Consult the [Penn branding rules](https://branding.web-resources.upenn.edu/) for the specified mark. Include an institutional logo or seal only when the applicable dissertation formatting rules require or recommend it. Use the specified mark and placement. When those rules are silent, omit institutional marks.

## Design choices

The house chapter composition is right-aligned, with a 36-point Garamond numeral and an uppercase title. The 36-point ceiling comes from Guide 15; the earlier 12-point centered treatment was unnecessary. The Penn edition follows the guide’s direct recommendation for black text and headings. Its one-inch page boundaries, title wording, preliminary order, uppercase labels, and continuous footnotes remain school-specific. The colophon initial stays within the heading-size ceiling.

The guide recommends double spacing but permits single-spaced bibliography entries. This template retains double body spacing. A department may impose additional requirements. These design choices do not establish institutional acceptance or PDF accessibility.
