# Beautiful Word and LaTeX dissertation templates
[![Build Status](https://travis-ci.org/asm-products/Dissertate.svg?branch=master)](https://travis-ci.org/asm-products/Dissertate)
[![Code Climate](https://codeclimate.com/github/asm-products/dissertate/badges/gpa.svg)](https://codeclimate.com/github/asm-products/dissertate)
<a href="https://assembly.com/dissertate/bounties?utm_campaign=assemblage&utm_source=dissertate&utm_medium=repo_badge"><img src="http://badger.asm.co/dissertate/badges/tasks.svg" height="24px" alt="Open Tasks" /></a>

Dissertate is a set of beautiful Word and LaTeX templates for a thesis or dissertation. 

One of the biggest hurdles in submitting a thesis or dissertation is getting the formatting right — the rules are arcane, and the registrar is pedantic. Few students have the background needed to design and typeset clean and stylish documents. Enter Dissertate. Dissertate is a set of beautiful Word and LaTeX templates for a thesis or dissertation. To date, the software provides everything needed to support the production and typesetting of a PhD dissertation at Harvard, Princeton, and NYU, though it will be adapted to meet the requirements of other schools — eventually all of them. The format and styling are based closely on the requirements published by each university's registrar. Eventually, Dissertate can provide a web app that automatically arranges for the document to be printed and mailed to the student. This is a product being built by the Assembly community. You can help push this idea forward by visiting [https://assembly.com/dissertate](https://assembly.com/dissertate).

### How Assembly Works
Assembly products are like open-source and made with contributions from the community. Assembly handles the boring stuff like hosting, support, financing, legal, etc. Once the product launches we collect the revenue and split the profits amongst the contributors.

Visit [https://assembly.com](https://assembly.com) to learn more.

## Getting started
1. Install LaTeX. For Mac OS X, we recommend MacTex (http://tug.org/mactex/); for Windows, MiKTeX (http://miktex.org/); and for Ubuntu, Tex Live (`sudo apt-get install texlive-full`)
2. Install the default fonts: EB Garamond, Lato, and Source Code Pro. The files are provided in `fonts/EB Garamond`, `fonts/Lato`, and `fonts/Source Code Pro`.
3. Pick your school by editing line 6 of `dissertation.tex` to use the option `Harvard`, `Princeton`, or `NYU`, depending on your school.
4. Personalize the document by filling out your name and all the other info in `frontmatter/personalize.md`.
5. Build your dissertation with `build.command`, located in the `scripts` directory (e.g., you can `cd` into the main directory and then run `./scripts/build.command`).

## FAQ

### How do I make the text justified instead of ragged right?
Remove or comment out the line `\RaggedRight` from the .cls file.

## Acknowledgments
Thanks to Andrew Leifer for many code and README contributions and to Clemens Eppner for the Ubuntu instructions.
