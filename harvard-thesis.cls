% -------------------------------------------------------------------
%  @LaTeX-class-file{
%     filename        = "harvard-thesis.cls",
%     version         = "0.1",
%     date            = "5 April 2011",
%     createdby       = "Jordan Suchow",
%     address         = "10 Akron St. 309, Cambridge, MA 02138"
%     telephone       = "+1 914 582 2646",
%     email           = "suchow at fas.harvard.edu",
%     codetable       = "ISO/ASCII",
%     keywords        = "LaTeX, harvard-thesis",
%     supported       = "send email to suchow@fas.harvard.edu",
%     docstring       = "A thesis class for a Harvard dissertation."
% --------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{harvard-thesis}[2011/04/09 v0.1 Harvard University Thesis Class]
\LoadClass[11pt, oneside, letterpaper]{book}


%these should be inpreamble of .tex file, not .cls
\RequirePackage{graphicx}
\RequirePackage{hyperref}
\usepackage[centertags]{amsmath}
\RequirePackage{amssymb}
\RequirePackage[numbers, comma, sort&compress]{natbib}
\RequirePackage[small, bf, sc]{titlesec}
\RequirePackage[tight,nice]{units}
\RequirePackage{verbatim}
\RequirePackage{url}
\usepackage{pdfsync} %do pdf synchronization [andy]
\synctex=1 % turn synctex on automatically to sync between pdf viewer [andy]


%these can stay here
\RequirePackage{lettrine}%big letter at start of chapter
\RequirePackage[width=5in, letterpaper]{geometry}


\RequirePackage{fancyhdr} % This should be set AFTER setting up the page geometry
\pagestyle{plain} % options: empty , plain , fancy
\RequirePackage[palatino]{quotchap}
\RequirePackage{titling}
\RequirePackage{setspace} 
\RequirePackage{booktabs} % for much better looking tables
\RequirePackage[labelfont={sf,bf,small},textfont={sf,small},justification=RaggedRight,margin=0pt, figurewithin=section, tablewithin=section]{caption}
\onehalfspacing
%\raggedright

\parindent 12pt
\RequirePackage{mathspec}
\setmathsfont(Digits,Latin,Greek)[Numbers={OldStyle,Proportional}]{Chaparral Pro}

\RequirePackage{fontspec,xltxtra,xunicode}
\defaultfontfeatures{Mapping=tex-text, Numbers=OldStyle}
\setromanfont[Mapping=tex-text, Numbers=OldStyle, Ligatures={{Historic,Contextual,Rare}}]{Chaparral Pro} % Contextuals=Swash, Ligatures={{Historic,Contextual,Rare}}

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
	\thispagestyle{empty}\vspace*{\fill} 
	\begin{center}
	\huge \thetitle \normalsize \\ \vspace{100pt}
	A dissertation presented \\ by\\
	\theauthor\\ to\\ The \@department\\ 
	in partial fulfillment of the requirements\\ 
	for the degree of\\ \@degree\\ 
	in the subject of\\ \@field\\
	\vspace{24pt}
	\@university\\ \@universitycity, \@universitystate\\ 
	\@degreemonth\ \@degreeyear
	\end{center} \vspace*{\fill}
} 

\newcommand{\copyrightpage}{
	\newpage \thispagestyle{empty} \vspace*{\fill}
	\noindent \copyright \degreeyear, \theauthor \\
	All rights reserved.
	\vspace*{\fill} \newpage \rm
}

\newcommand{\abstractpage}{
	\newpage
	\pagenumbering{roman}
	\setcounter{page}{3}
	\pagestyle{fancy}
	\lhead{\@advisor} \rhead{\@author}
	\renewcommand{\headrulewidth}{0.0pt} 
	\begin{center}
	\Large \@title \normalsize \\
	\vspace{20pt}
	\sc Abstract \\ \rm
	\end{center}
	\input{frontmatter/abstract}
	\newpage \lhead{} \rhead{}
	\cfoot{\thepage}
}

\newcommand{\dedicationpage}{
	\pagestyle{fancy}
	\newpage \thispagestyle{fancy} \vspace*{\fill}
	\sc \noindent \input{frontmatter/dedication}
	\vspace*{\fill} \newpage \rm
}

\newcommand{\acknowledgments}{
	\newpage \vspace*{\fill}
	\section*{Acknowledgments}
	\noindent
	\input{frontmatter/thanks}
	\vspace*{\fill} \newpage
	\setcounter{page}{1}
	\pagenumbering{arabic}}
	
% An environment for paragraph-style section

\providecommand\newthought[1]{%
   \addvspace{1.0\baselineskip plus 0.5ex minus 0.2ex}%
   \noindent\textsc{#1}%
}
	