% -------------------------------------------------------------------
%  @LaTeX-class-file{
%     filename        = "harvard-thesis.cls",
%     version         = "0.4",
%     date            = "4 April 2012",
%     codetable       = "ISO/ASCII",
%     keywords        = "LaTeX, harvard-thesis",
%     supported       = "send email to suchow@fas.harvard.edu",
%     docstring       = "A thesis class for a Harvard dissertation."
% --------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{harvard-thesis}[2012/04/05 v0.4 Harvard University Thesis Class]
\LoadClass[12pt, oneside, letterpaper]{book}


% Required packages
\RequirePackage{graphicx}
\RequirePackage{hyperref}
\hypersetup{
	linktocpage,
    colorlinks,
    citecolor=Crimson,
    filecolor=black,
    linkcolor=black,
    urlcolor=Crimson,
}

\RequirePackage[centertags]{amsmath}
\RequirePackage{amssymb}
\RequirePackage[numbers, comma, sort&compress]{natbib}
\RequirePackage[small, md, sc]{titlesec}
\RequirePackage[tight,nice]{units}
\RequirePackage{verbatim}

% colors
\RequirePackage{color}
\definecolor{Crimson}{rgb}{0.6471, 0.1098, 0.1882}

\RequirePackage{url}
\RequirePackage[titles]{tocloft}
\setcounter{tocdepth}{1}
\renewcommand{\cftchapfont}{\normalsize \scshape}

\renewcommand\bibname{References}
\renewcommand\listfigurename{Listing of figures}
\raggedright

\RequirePackage{pdfsync} %do pdf synchronization [andy]

%\usepackage[closeFloats, noSeparatorLine]{fltpage} %use the custom modified fltpage package
\RequirePackage{afterpage}








\synctex=1 % turn synctex on automatically to sync between pdf viewer [andy]

%   list an entire bibliography entry inline. Useful for acknowledging when my paper was previously published
\RequirePackage{bibentry}
\nobibliography*

\RequirePackage{lettrine} % big letter at start of chapter
\RequirePackage[width=5in, letterpaper]{geometry}

\RequirePackage{fancyhdr}
\pagestyle{plain} % options: empty , plain , fancy
\RequirePackage[palatino]{quotchap}
\definecolor{chaptergrey}{rgb}{0.6,0,0}
\RequirePackage{titling}
\RequirePackage{setspace}
\RequirePackage{booktabs} % for much better looking tables
\RequirePackage[labelfont={sf,bf,small},textfont={sf,small},justification=RaggedRight,margin=0pt, figurewithin=section, tablewithin=section]{caption}
\onehalfspacing
\addtolength{\footnotesep}{\footnotesep}

%\raggedright

\parindent 12pt
\RequirePackage{mathspec}

% use Arno Pro instead of standard LaTeX fonts
\setmathsfont(Digits,Latin,Greek)[Numbers={OldStyle,Proportional}]{Arno Pro}
\setmathrm{Arno Pro}

\RequirePackage{fontspec,xltxtra,xunicode}
\defaultfontfeatures{Mapping=tex-text, Numbers=OldStyle}
\setromanfont[Mapping=tex-text,
			  Numbers=OldStyle,
			  Ligatures={Common},
			  SizeFeatures={%
		          {Size={-10}, Font=* Caption},
		          {Size={10-13.0}, Font=*},
		          {Size={13.01-19.9}, Font=* Subhead, Ligatures=Rare, Contextuals={Swash,Alternate}},
		       {Size={19.91-},Font=* Display, Ligatures=Rare, Contextuals={Swash,Alternate}}}]
			  {Arno Pro} %

%Set fonts for Mac Specific (Comment out on Windows XP)
%\setsansfont[Scale=MatchLowercase,Mapping=tex-text]{Helvetica Neue}
%\setmonofont[Scale=MatchLowercase]{Consolas}

% some definitions
\def\degreeyear#1{\gdef\@degreeyear{#1}}
\def\degreemonth#1{\gdef\@degreemonth{#1}}
\def\degree#1{\gdef\@degree{#1}}
\def\advisor#1{\gdef\@advisor{#1}}
\def\department#1{\gdef\@department{#1}}
\def\field#1{\gdef\@field{#1}}
\def\university#1{\gdef\@university{#1}}
\def\universitycity#1{\gdef\@universitycity{#1}}
\def\universitystate#1{\gdef\@universitystate{#1}}


\renewcommand{\maketitle}{
	\singlespacing
	\thispagestyle{empty}
	\vspace*{\fill} \vspace{150pt} \begin{center}
	\Huge \textcolor{Crimson}{\textit{\thetitle}} \normalsize \\ \sc \vspace{100pt}
	a dissertation presented \\ by\\
	\theauthor\\ to\\ The \@department\\
	\vspace{12pt}
	in partial fulfillment of the requirements\\
	for the degree of\\ \@degree\\
	in the subject of\\ \@field\\
	\vspace{12pt}
	\@university\\ \@universitycity, \@universitystate\\
	\@degreemonth\ \@degreeyear
	\end{center} \vspace*{\fill}
}

% You might also consider licensing your work under Creative Commons). See: http://creativecommons.org/weblog/entry/12824 for other PhD students who have released their work under creative commons.

\newcommand{\copyrightpage}{
	\newpage \thispagestyle{empty} \vspace*{\fill}
	\sc \noindent \copyright~\textit{\@degreeyear \hspace{3pt}~- \theauthor} \\
	\noindent All rights reserved.
	\vspace*{\fill} \newpage \rm
}

\newcommand{\abstractpage}{
	\newpage
	\pagenumbering{roman}
	\setcounter{page}{3}
	\pagestyle{fancy}
	\lhead{Thesis advisor: \@advisor} \rhead{\@author}
	\renewcommand{\headrulewidth}{0.0pt}
	\begin{center}
	\vspace*{1pt}
	\Large \textcolor{Crimson}{\textit{\@title}} \normalsize\\
	\vspace*{15pt}
	\sc Abstract \\ \rm
	\end{center}
	\doublespace %Harvard registrar requests that abstract is double spaced
	\input{frontmatter/abstract}
	\doublespace %Harvard registrar requests that abstract is double spaced
	\newpage \lhead{} \rhead{}
	\cfoot{\thepage}
	\onehalfspacing
}

\newcommand{\dedicationpage}{
	\pagestyle{fancy}
	\newpage \thispagestyle{fancy} \vspace*{\fill}
	\sc \noindent \input{frontmatter/dedication}
	\vspace*{\fill} \newpage \rm
	}

% the list of authors
\newcommand{\authorlist}{
	\pagestyle{fancy}
	\newpage
	\thispagestyle{fancy}
	\chapter*{Author List}
	\noindent \input{frontmatter/authorlist}
	\newpage \rm
	}

% the acknowledgments page
\newcommand{\acknowledgments}{
	\chapter*{Acknowledgments}
	\noindent
	\input{frontmatter/thanks}
	\vspace*{\fill}
	\newpage
	\setcounter{page}{1}
	\pagenumbering{arabic}}

% An environment for paragraph-style section
\providecommand\newthought[1]{%
   \addvspace{1.0\baselineskip plus 0.5ex minus 0.2ex}%
   \noindent\textsc{#1}}
