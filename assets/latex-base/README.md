# Dissertate

## Getting started
1. Install LaTeX. For Mac OS X, we recommend MacTex (https://tug.org/mactex/); for Windows, MiKTeX (https://miktex.org/); and for Ubuntu, Tex Live (`sudo apt-get install texlive-full`)
2. Edit `frontmatter/personalize.tex` with your details.
3. Compile `dissertation.tex` with XeLaTeX and BibTeX. On macOS or Linux, you can run `sh scripts/build` from the template folder.

The template loads its bundled EB Garamond, Lato, and Source Code Pro fonts automatically.

## FAQ

### How do I set the title and author?

Edit `\title{...}` and `\author{...}` in `frontmatter/personalize.tex`. The school style uses these values on the title page and in headers.

### How do I compile selected chapters?

Add `\includeonly{chapters/chapter1}` after `\documentclass{Dissertate}` in `dissertation.tex` (separate multiple chapter paths with commas). Compile the complete dissertation first to preserve references and numbering from omitted chapters. Front matter and any active bibliography commands are still included; remove `\includeonly` to compile all chapters again.

### How do I adjust line spacing?

The default body spacing is set by `\dnormalspacing`. To change it, add `\renewcommand{\dnormalspacing}{1.5}` after `\documentclass{Dissertate}` in `dissertation.tex`. Replace `1.5` with the spacing factor required by your program. Check the compiled PDF against your school’s current formatting rules.

### How do I make the text justified instead of ragged right?
Remove or comment out the line `\RaggedRight` from the .cls file.


### How do I add subfigures?

Load the [`subcaption`](https://ctan.org/pkg/subcaption) package in `dissertation.tex` after `\documentclass{Dissertate}`:

```latex
\usepackage{subcaption}
```

Each `subfigure` environment takes a width argument:

```latex
\begin{figure}[htbp]
  \centering
  \begin{subfigure}[b]{0.45\textwidth}
    \includegraphics[width=\linewidth]{figures/fig1}
    \caption{First panel.}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.45\textwidth}
    \includegraphics[width=\linewidth]{figures/fig2}
    \caption{Second panel.}
  \end{subfigure}
  \caption{A figure with two panels.}
\end{figure}
```

### How do I add a table?

Place a `table` environment in a chapter. This example puts the caption above a two-column table:

```latex
\begin{table}[htbp]
  \centering
  \caption{Example measurements.}
  \label{tab:example}
  \begin{tabular}{lr}
    \hline
    Measurement & Value \\
    \hline
    First & 12 \\
    Second & 34 \\
    \hline
  \end{tabular}
\end{table}
```

Refer to the table with `Table~\ref{tab:example}`. LaTeX may move the table to a nearby page.

### How do I use author–year citations?

Add `\setcitestyle{authoryear,round,semicolon,aysep={,},yysep={,}}` after `\documentclass{Dissertate}` in `dissertation.tex`. Use `\citet{key}` for a textual citation, `\citep{key}` for a parenthetical citation, and `\citeauthor{key}` for the author’s name. Enable `\bibliographystyle{apalike2}` and `\bibliography{references}` near the end of `dissertation.tex`, and rebuild with XeLaTeX, BibTeX, XeLaTeX, and XeLaTeX. This produces APA-like author–year citations; `apalike2` does not implement current APA requirements.
