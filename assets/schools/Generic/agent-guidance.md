# Guidance for working with this dissertation

This generic template is a starting point. Identify the institution, degree program, and submission requirements before changing the format. Consult the institution's current official dissertation instructions and any department-specific rules. Do not treat the sample layout as proof of compliance.

Edit `frontmatter/personalize.tex` for the author's details. The main document is `dissertation.tex`; chapters are in `chapters/`. Preserve the author's content and verify requested changes in the compiled PDF. The template uses XeLaTeX and BibTeX.

For one adviser, set `\advisor{...}`. For two co-advisers, comment out the `\advisor` line and set both `\coadvisorOne{...}` and `\coadvisorTwo{...}`. The abstract header lists the configured adviser or co-advisers.

Include an institutional logo or seal only when the applicable dissertation formatting rules require or recommend it. Use the specified mark and placement. When those rules are silent, omit institutional marks.

## Design choices

Generic preserves the house design: Garamond text, gray oversized chapter numerals, right-aligned titles, small caps, Lato captions, and the optional illustrated colophon. The chapter numeral uses the bundled Garamond bold face. Generic makes no claim to satisfy a particular institution’s formatting rules.
