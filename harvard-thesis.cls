% -------------------------------------------------------------------
%  @LaTeX-class-file{
%     filename        = "harvard-thesis.cls",
%     version         = "0.1.1",
%     date            = "5 April 2011",
%     createdby       = "Jordan Suchow, modified by Andrew Leifer",
%     address         = "10 Akron St. 309, Cambridge, MA 02138"
%     telephone       = "+1 914 582 2646",
%     email           = "suchow at fas.harvard.edu",
%     codetable       = "ISO/ASCII",
%     keywords        = "LaTeX, harvard-thesis",
%     supported       = "send email to suchow@fas.harvard.edu",
%     docstring       = "A thesis class for a Harvard dissertation."
% --------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{harvard-thesis}[2011/09/09 v0.1.1 Harvard University Thesis Class]
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


%Begin Andy's package additions
\usepackage{pdfsync} %do pdf synchronization [andy]
\usepackage[closeFloats, noSeparatorLine]{packages/fltpage} %use the custom modified fltpage package
\RequirePackage{afterpage} 





 


\synctex=1 % turn synctex on automatically to sync between pdf viewer [andy]

%   list an entire bibliography entry inline. Useful for acknowledging when my paper was previously published
\usepackage{bibentry} 
\nobibliography*        
%End Andy's package additions

\RequirePackage{lettrine}%big letter at start of chapter
\RequirePackage[width=5in, letterpaper]{geometry}


\RequirePackage{fancyhdr} 
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


% Instead of using default latex for math fonts, we can be fancy and try to adapt Chaparral Pro.. --ANDY
\setmathsfont(Digits,Latin,Greek)[Numbers={OldStyle,Proportional}]{Chaparral Pro}
\setmathrm{Chaparral Pro}  %I added this to handle \mathbf

%Use this if you want math fonts that are slightly better than default Latex
%\setmathfont{Cambria Math}

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
	\noindent \copyright~\textit{\@degreeyear ~-\theauthor}  \\
	All rights reserved.
	\vspace*{\fill} \newpage \rm
}


%Andy's Alternative Creative Commons Licensing (NOTE this is non-traditional, but a good idea)
% See: http://creativecommons.org/weblog/entry/12824 for other PhD students who release their work under creative commons

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
	\begin{doublespace} %Harvard registrar requests that abstract is double spaced
	\input{frontmatter/abstract}
	\end{doublespace}
	\newpage \lhead{} \rhead{}
	\cfoot{\thepage}
}

\newcommand{\dedicationpage}{
	\pagestyle{fancy}
	\newpage \thispagestyle{fancy} \vspace*{\fill}
	\sc \noindent \input{frontmatter/dedication}
	\vspace*{\fill} \newpage \rm
	}

	\newcommand{\authorlist}{
		\pagestyle{fancy}
\thispagestyle{fancy} 
		\section*{Author List}
		\noindent \input{frontmatter/authorlist}
		\newpage \rm
		}


\newcommand{\acknowledgments}{
%	\vspace*{\fill} %This has to be removed, otherwise you get an additional empty page
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
	
	
%Andys Spacing 
%Be more forgiving, and stretch word spacing out more so that wormds don't run out into the margins..
\emergencystretch=1.5em
%End Andy Spacing


%Andy's Numbering Fixf
%Fix the figure counting so that it isn't affected by sections so as to be complient with harvard's annoying rule that says Figure 4.2.x cannot be followed by Figure 4.5.1.
\usepackage{chngcntr}

%The way it will now work is that figures will have two numbers and the first number will increment by chapter and the second number will increment within a chapter irrespective of section
\counterwithout{figure}{part}
\counterwithout{figure}{section}
\counterwithin{figure}{chapter}

%Repeat for Tables
\counterwithout{table}{part}
\counterwithout{table}{section}
\counterwithin{table}{chapter}



