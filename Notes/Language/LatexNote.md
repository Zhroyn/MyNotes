<!-- TOC -->

- [Preamble](#preamble)
- [Document structure](#document-structure)
  - [Abstract](#abstract)
  - [Paragraph and new lines](#paragraph-and-new-lines)
  - [Chapters and sections](#chapters-and-sections)
  - [Adding a Table of Contents](#adding-a-table-of-contents)
- [Font](#font)
- [Math](#math)
  - [Additional Component](#additional-component)
  - [Operators](#operators)
  - [Symbols](#symbols)
  - [Equations and Alignment](#equations-and-alignment)
  - [Matrix](#matrix)
  - [Greek Alphabet](#greek-alphabet)
- [Image](#image)
- [List](#list)
- [Table](#table)
- [Package](#package)

<!-- /TOC -->



### Preamble

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



### Document structure

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


### Font
$$
text \\
\textit{text} \\
\text{text} \\
\textrm{text} \\
\textup{text} \\
\textbf{text} \\
\textsf{text} \\
\texttt{text} \\
$$

$$
math \\
\mathrm{math} \\
\mathbf{math} \\
\mathsf{math} \\
\mathtt{math} \\
\mathbb{R}, \mathcal{R}, \mathscr{R} \\ 
\mathbb{P}, \mathcal{P}, \mathscr{P} \\ 
\mathbb{L}, \mathcal{L}, \mathscr{L} \\
$$

### Math
#### Additional Component
**Subscript and Supscript**
$$
a_i^2, a_{j-1,j}^{n+1} \\~\\
$$

$a_i^n, \mathop{a}\limits_i^n $
$\sum_{i=1}^n, \sum\limits_{i=1}^n $
$\lim_{n\to\infty}, \lim\limits_{n\to\infty} $

**Additional Symbols**
$$
\hat{a}, \widehat{a}, \check{a}, \widecheck{a}, \tilde{a}, \widetilde{a} \\~\\
\bar{a}, \vec{a} \\~\\
\acute{a}, \grave{a} \\~\\
\dot{a}, \ddot{a} \\~\\
\not\in, \cancel\in \\
$$

**Over and Under**
$$
\overleftarrow{abc}, \underleftarrow{abc} \\~\\
\overrightarrow{abc}, \underrightarrow{abc} \\~\\
\overleftrightarrow{abc}, \underleftrightarrow{abc} \\~\\
\overline{\text{overline}}, \underline{\text{underline}} \\~\\
\underbar{\text{underbar}}, \underbrace{\text{underbrace}} \\~\\
\overset{a}{\text{overset}}, \underset{a}{\text{underset}} \\~\\
$$

#### Operators
**Binary Operators**
$$
\pm, \mp, \oplus, \setminus \\~\\
\times, \div \\~\\
\cdot, \odot, \circ, \bullet \\~\\
\cap, \cup, \bigcap, \bigcup \\~\\
\wedge, \vee, \bigwedge,\bigvee \\~\\
$$

**Large Operators**
$$
\lim, \sum, \prod, \int, \sqrt[n]{n},
$$

$$
\frac{\mathrm{d} y}{\mathrm{d} x}, 
\frac{\partial f}{\partial x}, 
f^{'}, 
\nabla f
$$


#### Symbols
$$\lt, \le, \leq, \leqq, \leqslant, \not\lt$$
$$\gt, \ge, \geq, \geqq, \geqslant, \not\gt$$
$$\prec, \preceq, \preccurlyeq, \precapprox, \precnapprox, \precsim, \precnsim $$
$$\neq, \approx, \approxeq, \sim, \simeq, \cong, \equiv$$
$$\subset, \subseteq, \subsetneq, \supset, \in, \notin$$
$$\to, \rightarrow, \leftarrow, \Rightarrow, \Leftarrow, \iff$$
$$\forall, \exists, \mapsto, \because, \therefore$$


#### Equations and Alignment
$$
y =
\begin{cases}
  \sin(x)       & x<0 \\
  x^2 + 2x +4   & 0 \leq x < 1 \\
  x^3           & x \geq 1 \\
\end{cases}
$$

$$
\begin{cases}
  a + b - c = 2 \\
  a - b = 4 \\
\end{cases}
\\~\\
\left\{
  \begin{aligned}
    & a + b - c = 2 \\
    & a - b = 4 \\
  \end{aligned}
\right.
$$

$$
\begin{aligned}
f(x) &= 2x+1 \\
     &= 2+1 \\
     &= 3
\end{aligned}
$$


#### Matrix
$$
\left(
\left[
  \begin{array}{ccc}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    a_{21} & a_{22} & \cdots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn} \\
  \end{array}
\right]
\right)
$$

$$
\begin{matrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 1 \\
\end{matrix}, 
\begin{pmatrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 1 \\
\end{pmatrix}, 
\begin{bmatrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 1 \\
\end{bmatrix}, 
\begin{vmatrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 1 \\
\end{vmatrix}, 
$$

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







### Image
```latex
\documentclass{article}
\usepackage{graphicx}
\graphicspath{{C:/Users/hrzhe/Pictures/head profile/Pokemon}}
%the path cannot use '\'


\begin{document}

\includegraphics[height=10cm,width=10cm]{Eevee}
\includegraphics{C:/Users/hrzhe/Pictures/head profile/Pokemon/Eevee}

\begin{figure}
    \centering
    \includegraphics[width=0.75\textwidth]{Eevee}
    \caption{A cute creature.}
    \label{fig:Eevee}
\end{figure}
 
The figure \ref{fig:Eevee} is on page \pageref{fig:Eevee}.
\end{document}
```



### List

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


### Table

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



### Package
```latex
\usepackage[options]{somepackage}
```