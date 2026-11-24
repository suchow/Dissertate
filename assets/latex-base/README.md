# Dissertate

## Getting started
1. Install LaTeX. For Mac OS X, we recommend MacTex (https://tug.org/mactex/); for Windows, MiKTeX (https://miktex.org/); and for Ubuntu, Tex Live (`sudo apt-get install texlive-full`)
2. Install the default fonts: EB Garamond, Lato, and Source Code Pro. The files are provided in `fonts/EB Garamond`, `fonts/Lato`, and `fonts/Source Code Pro`.
3. Edit `frontmatter/personalize.tex` with your details.
4. Compile `dissertation.tex` with XeLaTeX and BibTeX. On macOS or Linux, you can run `sh scripts/build` from the template folder.

## FAQ

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
