<!-- TOC -->

- [Preamble](#preamble)
- [Document structure](#document-structure)
    - [Abstract](#abstract)
    - [Paragraph and new lines](#paragraph-and-new-lines)
    - [Chapters and sections](#chapters-and-sections)
    - [Adding a Table of Contents](#adding-a-table-of-contents)
- [Font](#font)
- [Math](#math)
    - [Basic](#basic)
    - [Superscript and Subscript](#superscript-and-subscript)
    - [Functions](#functions)
    - [Operations](#operations)
    - [Symbols](#symbols)
    - [Style](#style)
    - [Greek Alphabet](#greek-alphabet)
    - [Matrix](#matrix)
- [Image](#image)
- [List](#list)
- [Table](#table)
- [Package](#package)

<!-- /TOC -->



## Preamble

```latex
\documentclass[12pt, letterpaper]{article}  %the default size is 10pt
\documentclass[a4paper, total={6in, 8in}]{geometry}

\title{One test LaTeX document}

\author{Zheng Haoren\thanks{Learn from Overleaf.}}

\date{August 2022}
\data{today}

\begin{document}
\maketitle %used within the body and could only function when first used
\end{document}
```



## Document structure

#### Abstract
```latex
\begin{document}
\begin{abstract}
This is a simple paragraph at the beginning of the 
document. A brief introduction about the main subject.
\end{abstract}
\end{document}
```
#### Paragraph and new lines
- blank lines will automatically intent paragraph
- `\\` or `\newline` can be used to create new lines
- `~\\` can add blank lines anyway

#### Chapters and sections
```latex
\part{part}
\section{section}
\subsection{subsection}
\subsubsection{subsubsection}
\paragraph{paragraph}
\subparagraph{subparagraph}
```

#### Adding a Table of Contents
```latex
\begin{document}
\tableofcontents
\end{document}
```


## Font

[Overleaf](https://cn.overleaf.com/learn/latex/Font_sizes%2C_families%2C_and_styles)
```latex
\documentclass{article}
\begin{document}

% Font sizes
{\tiny this will show different font sizes}
{\footnotesize Foot note size also}
{\small}    {\normalsize}
{\large}    {\Large}    {\LARGE}
{\huge}     {\Huge}

% Default font families
\textrm{serif(roman)}	            \rmfamily
\textsf{sans serif}	            \sffamily
\texttt{typewriter(monospace)}	    \ttfamily

% Font styles
\textmd{medium}	              \mdseries
\textbf{bold}	              \bfseries
\textup{upright}	      \upshape
\textit{italic}	              \itshape
\textsl{slanted}	      \slshape
\textsc{small caps}	      \scshape


% Change sans font as a default by using the command:
\renewcommand{\familydefault}{\sfdefault}
\renewcommand{\familydefault}{\rmdefault}

% Use other font typefaces like TEX Gyre Bonum by:
\usepackage{tgbonum}
% Change default font typeface like TEX gyre cursor, whose fontcode is qcr by:
{\fontfamily{qcr}\selectfont
This text uses a different font typeface
}

\end{document}
```


## Math
#### Basic
To typeset inline-mode math you can use one of these delimiter pairs: `\( ... \)`, `$ ... $` or `\begin{math} ... \end{math}`
To typeset display-mode math you can use one of these delimiter pairs: `\[ ... \]`, `$$ ... $$`, `\begin{displaymath} ... \end{displaymath}` or `\begin{equation} ... \end{equation}`
```latex
% Inline-mode
$E=mc^2$
\(E=mc^2\)

\begin{math}
E=mc^2
\end{math}

% Display-mode
\[E=mc^2\]        % unnumbered

$$
E=mc^2            % unnumbered
$$

\begin{displaymath}
E=mc^2            % unnumbered
\end{displaymath}

\begin{equation}
E=mc^2            % numbered
\end{equation}
```

#### Superscript and Subscript
$$a_i^2, a_{j-1,j}^{n+1}$$

#### Functions
$$
\sin x \\
\cos x \\
\ln x  \\
\log_{2}{x}   \\
\lim_{x\to 0} x^2
$$

#### Operations
$$
\sum_{i=0}^\infty i^2 \\
\prod_{k=1}^n k = n!  \\
\int_0^1 x^2 = \frac{1}{3}
$$

#### Symbols
$$\times, \div, \pm, \mp, \cdot, \oplus, \circ, \bullet$$
$$\lt, \le, \leq, \leqq, \leqslant, \not\lt$$
$$\gt, \ge, \geq, \geqq, \geqslant, \not\gt$$
$$\neq, \approx, \approxeq, \sim, \simeq, \cong, \equiv$$
$$\cap, \cup, \setminus, \subset, \subseteq, \subsetneq, \supset, \in, \notin$$
$$\to, \rightarrow, \leftarrow, \Rightarrow, \Leftarrow, \iff$$
$$\forall, \exists, \mapsto, \because, \therefore$$

#### Style
$
\lim\limits_{n\to\infty} \sqrt[n]{n},
\underset{n\to\infty}{\lim} \sqrt[n]{n},
\sum\limits_{i=1}^n a_n \\~\\
\\
\displaystyle{\sum_{i=1}^n a_n, \frac{1}{\sqrt[n]{n}}} \\~\\
\\
\begin{aligned}
f(x) &= 2x+1 \\
     &= 2+1 \\
     &= 3
\end{aligned}
$


#### Greek Alphabet
|form|letter|form|letter|
|---|---|---|---|
|\alpha	|α |\Alpha	|A|
|\beta	|β |\Beta	  |B|
|\gamma	|γ |\Gamma	|Γ|
|\delta	|δ |\Delta	|Δ|
|\epsilon|ϵ|\Epsilon|E|
|\zeta	|ζ |\Zeta	  |Z|
|\eta	  |η |\Eta	  |H|
|\theta	|θ |\Theta  |Θ|
|\iota	|ι |\Iota   |I|
|\kappa	|κ |\Kappa  |K|
|\lambda|λ |\Lambda |Λ|
|\mu	  |μ |\Mu     |M|
|\nu	  |ν |\Nu     |N|
|\xi	  |ξ |\Xi     |Ξ|
|\omicron|ο|\Omicron|O|
|\pi	  |π |\Pi     |Π|
|\rho	  |ρ |\Rho    |P|
|\sigma	|σ |\Sigma  |Σ|
|\tau	  |τ |\Tau    |T|
|\upsilon|υ|\Upsilon|Υ|
|\varphi|φ |\Phi    |Φ|
|\psi	  |ψ |\Psi    |Ψ|
|\omega	|ω |\Omega  |Ω|

#### Matrix
```latex
$$
% without brackets
\begin{array}{ccc}
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & 1\\
\end{array}

% with brackets
\left(
\left[
  \begin{array}{ccc}
      1 & 0 & 0\\
      0 & 1 & 0\\
      0 & 0 & 1\\
  \end{array}
\right]
\right)


\begin{pmatrix}   % matrix with []
\begin{bmatrix}   % matrix with ()
\begin{vmatrix}   % determinant
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & 1\\
\end{pmatrix}

A = \frac{1}{3} \times
  \begin{pmatrix}
      a_{11} & a_{12} & \cdots & a_{1n}\\
      a_{21} & a_{22} & \cdots & a_{2n}\\
      \vdots & \vdots & \ddots & \vdots\\
      a_{n1} & a_{n2} & \cdots & a_{nn}\\
  \end{pmatrix}
$$
```






## Image
```latex
\documentclass{article}
\usepackage{graphicx}
\graphicspath{{C:/Users/壬/Pictures/head profile/Pokemon}}
%the path cannot use '\'


\begin{document}

\includegraphics[height=10cm,width=10cm]{Eevee}
\includegraphics{C:/Users/壬/Pictures/head profile/Pokemon/Eevee}

\begin{figure}
    \centering
    \includegraphics[width=0.75\textwidth]{Eevee}
    \caption{A cute creature.}
    \label{fig:Eevee}
\end{figure}
 
The figure \ref{fig:Eevee} is on page \pageref{fig:Eevee}.
\end{document}
```



## List

```latex
% Unordered List
\begin{itemize}
  \item The individual entries are indicated with a black dot, a so-called bullet.
  \item The text in the entries may be of any length.
\end{itemize}

% Ordered List
\begin{enumerate}
  \item This is the first entry in our list.
  \item The list numbers increase with each entry we add.
\end{enumerate}
```


## Table

```latex
\begin{center}
\begin{tabular}{||c c c c||} 
% c-center, l-left, r-right
  \hline
  Col1 & Col2 & Col2 & Col3 \\ [0.5ex] 
  % 1 em is 10.06667 pixels, and 1 ex is 6 pixels
  \hline\hline
  1 & 6 & 87837 & 787 \\ 
  \hline
  2 & 7 & 78 & 5415 \\
  \hline
  3 & 545 & 778 & 7507 \\ [1ex] 
  \hline
\end{tabular}
\end{center}
```
or
```latex
Table \ref{table:data} shows how to add a table caption and reference a table.

\begin{table}[h!]

\centering
\begin{tabular}{||c c c c||} 
  \hline
  Col1 & Col2 & Col2 & Col3 \\ [0.5ex] 
  \hline\hline
  1 & 6 & 87837 & 787 \\ 
  2 & 7 & 78 & 5415 \\
  3 & 545 & 778 & 7507 \\
  4 & 545 & 18744 & 7560 \\
  5 & 88 & 788 & 6344 \\ [1ex] 
  \hline
\end{tabular}
\caption{Table to test captions and labels.}
\label{table:data}

\end{table}
```



## Package
```latex
\usepackage[options]{somepackage}
```