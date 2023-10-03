
- [基本使用](#基本使用)
  - [定义文档类](#定义文档类)
  - [加载宏包](#加载宏包)
  - [特殊字符](#特殊字符)
  - [空白换行](#空白换行)
- [文档结构](#文档结构)
  - [标题摘要](#标题摘要)
  - [章节目录](#章节目录)
  - [参考文献](#参考文献)
- [插入元素](#插入元素)
  - [列表](#列表)
  - [表格](#表格)
  - [图像](#图像)
- [字体](#字体)
- [数学](#数学)
  - [Additional Component](#additional-component)
  - [Operators](#operators)
  - [Symbols](#symbols)
  - [Equations and Alignment](#equations-and-alignment)
  - [Matrix](#matrix)
  - [Greek Alphabet](#greek-alphabet)







## 基本使用
### 定义文档类
在导言区 (Preamble) 中可以使用 `\documentclass[options]{class}` 命令定义文档类，其选项如下：
- `10pt|11pt|...` 指定字体大小，默认为 10pt
- `letterpaper|a4paper|a5paper|b5paper|...` 指定页面大小，默认为 letterpaper
- `titlepage|notitlepage` 指定是否生成标题页，article 默认为 notitlepage，report 和 book 默认为 titlepage
- `oneside|twoside` 指定是单面还是双面，article 和 report 默认为 onepage，report 默认为 twopage
- `onecolumn|twocolumn` 指定是单栏排版还是双栏排版，默认为 onecolumn
- `fleqn` 指定行间公式为左对齐，默认为居中对齐
- `leqno` 指定公式编号为左对齐，默认为右对齐
- `landscape` 指定排版方向为横向，默认为纵向

<br>

### 加载宏包
可用 `\usepackage[options]{pkg}` 命令加载宏包，若要加载多个宏包可以使用多次命令，或用逗号分隔多个宏包。

多个选项要用逗号分隔，某些选项可以传递参数，如 `spacing=1.5`。

所有 `\documentclass` 命令中指定文档类不认识的选项，会传递给 `\usepackage` 加载的宏包。

<br>

### 特殊字符
$\#$ $\$$ $\%$ $\&$ $\{$ $\}$ $\_$ $\^{}$ $\~{}$ 等特殊字符分别可以使用 \\#, \\$, \\%, \\&, \\{, \\}, \\_, \\^{}, \\~{} 表示。

- `` ` `` 表示左单引号
- `'` 表示右单引号
- ` `` ` 表示左双引号
- `''` 和 `"` 表示右双引号
<br>

- `-` 表示用于连接单词的连字号
- `--` 表示用于数字范围的起止号
- `---` 表示破折号。
<br>

- `\textasciiacute` 表示尖音符号 $\acute{}$
- `\textasciigrave` 表示重音符号 $\grave{}$
- `\textasciitilde` 表示波浪号 $\tilde{}$

<br>

### 空白换行
- `~` 等效于标准空格，长度为 1/3em，且不会被压缩或断行
- `\ ` 等效于标准空格，长度为 1/3em，且不会被压缩
- `\;` 等效于 `\thickspace`，长度为 5/18em
- `\:` 等效于 `\medspace`，长度为 4/18em
- `\,` 等效于 `\thinspace`，长度为 3/18em
- `\!` 等效于 `\negthinspace`，长度为 -3/18em
- `\quad` 长度为 1em
- `\qquad` 长度为 2em
- `\hspace{length}` 自定义长度，可为负数
<br>

- 空行或 `\par` 会换行并开始新的段落，有首行缩进
- `\\` 或 `\newline` 会换行，但没有首行缩进
- `\\[morespace]` 换行并指定行间距
- `\newpage` 换页
- `\noindent` 用于段首，取消缩进
<br>

- `\setlength{\parindent}{amount}` 设置首行缩进长度
- `\setlength{\parskip}{amount}` 设置段间距
- `\setlength{\baselineskip}{amount}` 设置行间距
<br>

使用 setspace 宏包可以更方便地设置行间距：
- `\singlespacing` 设置单倍行距
- `\onehalfspacing` 设置 1.5 倍行距
- `\doublespacing` 设置双倍行距
- `\setstretch{factor}` 自定义行间距

setspace 宏包还支持使用 `\begin{singlespace}...` `\begin{onehalfspace}...` `\begin{doublespace}...` `\begin{spacing}{factor}...` 等命令来设置局部行间距。

setspace 宏包还支持传入 `singlespacing` `onehalfspacing` `doublespacing` 等选项来改变全局行间距。










<br>

## 文档结构
### 标题摘要
`\title{}`, `\author{}`, `\date{}` 命令分别用来设置标题、作者和日期，可在导言区或正文区使用。

`\maketitle` 用于显示标题，在正文区使用。若 `\date{}` 的参数为空，则不显示日期信息；若未出现 `\date{}` 命令，则默认显示当前日期。

`\begin{abstract}...\end{abstract}` 用于插入摘要，一般在 `\maketitle` 命令之后使用。若要自定义摘要标题，可使用 `\renewcommand{\abstractname}{define}` 命令。

<br>

### 章节目录
章节命令的级别依次如下：
- `\part{}` -1 (book, report), 0 (article)
- `\chapter{}` 0，article 不可用
- `\section{}` 1
- `\subsection{}` 2
- `\subsubsection{}` 3
- `\paragraph{}` 4
- `\subparagraph{}` 5

以上各命令可在花括号前加上 * 号，这样便不会被自动编号，也不会出现在目录中。

`\tableofcontents` 可用于插入目录。若要自定义目录标题，可使用 `\renewcommand{\contentsname}{define}` 命令。

`\setcounter{secnumdepth}{level}` 可用于设置编号深度，级别小于等于 secnumdepth 的章节将会被编号，article 默认为 3，book 和 report 默认为 2
`\setcounter{tocdepth}{level}` 可用于设置目录深度，级别小于等于 tocdepth 的章节将会被列入目录，article 默认为 3，book 和 report 默认为 2

载入 hyperref 宏包可让目录自动生成跳转链接。

<br>

### 参考文献
参考文献编写如下：
```latex
\begin{thebibliography}{99}
  \bibitem{ref1} Author A, Author B. Title of the Article. Journal Name, 2022, 10(2): 100-120.
  \bibitem{ref2} Author C, Author D. Title of the Book. Publisher, 2022.
\end{thebibliography}
```
- `\begin{thebibliography}{widestlabel}...` 设置标签的最大宽度，以便正确对齐
- `\bibitem[label]{citekey}` lable 默认为自动数字编号，citykey 用于在引用时指定参考文献

若要在正文中引用文献，可使用 `\cite{keylist}`。若要引用多个参考文献，可用逗号分隔。








<br>

## 插入元素
### 列表
无序列表、有序列表和描述列表的环境依次为 `itemize` `enumerate` 和 `discription`，写法基本如下：
```latex
\begin{itemize}
  \item[optional label of first item] text of first item
  \item[optional label of second item] text of second item
  ...
\end{itemize}
```
无序列表和有序列表各级别的默认标签依次如下：
| 级别 | 无序列表 | 有序列表 |
|:---:|--------|--------|
| 1 | $\bullet$ \textbullet | 阿拉伯数字加点号 |
| 2 | $\bf{-}$ \normalfont\bfseries\textendash | 小写字母加括号 |
| 3 | $*$ \textasteriskcentered | 小写罗马数字加点号 |
| 4 | $\cdot$ \textperiodcentered | 大写字母加点号 |

---
若要改变列表的标签样式，可以使用 `\renewcommand` 命令：

对于无序列表，若要修改默认标签，则各级别对应的命令依次为 `\labelitemi` `\labelitemii` `\labelitemiii` `\labelitemiv`，比较好看的有 $\diamond$, $\diamonds$, $\circ$, $\triangledown$, $\triangle$, $\blacktriangledown$, $\blacktriangle$, $\square$, $\blacksquare$, $\star$ 等。

对于有序列表，若要修改默认标签，则各级别对应的命令依次为 `\labelenumi` `\labelenumii` `\labelenumiii` `\labelenumiv`，每个级别对应的计数器依次为 `enumi` `enumii` `enumiii` `enumiv`，使用范例为：`\renewcommand{\labelenumi}{(\textbf{\Alph{enumi}})}`。比较常用的计数命令有：
- `\arabic{counter}` `\arabic*` 阿拉伯数字
- `\alph{counter}` `\alph*` 小写字母
- `\Alph{counter}` `\Alph*` 大写字母
- `\roman{counter}` `\roman*` 小写罗马数字
- `\Roman{counter}` `\Roman*` 大写罗马数字

---
使用 enumitem 宏包可以更方便地修改列表的样式。单独修改列表样式的方法如下：
```latex
\begin{enumerate}[label=step \arabic*, itemsep=5pt]
  \item first item
  \item second item
\end{enumerate}
```

全局修改列表样式可使用 `\setitemize` `\setenumerate` `\setdiscription` 命令。以下命令分别修改了所有级别和第一个级别：
```latex
\setenumerate{itemsep=0pt, labelsep=0pt}
\setenumerate[1]{leftmargin=10pt}
```

常见的各间距的含义为：
- `itemsep` 条目之间的垂直距离
- `labelsep` 标签与文本之间的水平距离
- `parsep` 条目内的段间距
- `topsep` 列表上下两侧的额外距离
- `leftmargin` 列表左侧的空白距离
- `rightmargin` 列表右侧的空白距离




<br>

### 表格
使用 `\begin{tabular}[pos]{cols}` 环境可以写出基本的表格：
```latex
\begin{tabular}{||cc|c||} 
  Col1 & Col2 & Col3 \\
  \hline\hline
  2 & 7 & 78 \\
\end{tabular}
```
- `c` 代表居中对齐，`l` 代表左对齐，`r` 代表右对齐
- `|` 代表竖线，`\hline` 代表横线，可叠加使用
- cols 参数还可以使用 `@{}` 说明符，如 `@{\hspace{2em}}`。若两个说明符之间没有 @ 表达式，则每列的两侧都会放上 `\tabcolsep` 长度的空格，否则会放上 @ 表达式中的内容

若要跨列合并单元格，可以使用 `\multicolumn{numcols}{cols}{text}` 命令。cols 参数会覆盖原有参数，故若要保持竖线，则必须使用 `|`。

若要跨行合并单元格，可以使用 multirow 宏包中的 `\multirow{numrows}{width}{text}` 命令。width 参数代表表格宽度，一般填 * 代表自动宽度。

若要改变行间距，可以使用 `\renewcommand{\arraystretch}{factor}` 命令。
若要改变列间距，可以使用 `\setlength{\tabcolsep}{length}` 命令，或使用 `@{}`。

---
使用 `\begin{table}[placement]` 环境可以更方便地使表格居中，并添加标题、标签：
```latex
\begin{table}
  \centering
  \begin{tabular}{c|ccc}
    \multirow{2}{*}{Method} & \multicolumn{3}{|c}{PSNR} \\
                            & Room & Fern & Leaves \\ \hline
    SRN & 27.29 & 21.37 & 18.24 \\
    LLFF & 28.42 & 22.85 & 19.52 \\
    Ours & 32.70 & 25.17 & 20.92 
  \end{tabular}
  \caption{Per-scene quantitative results from real image dataset}
  \label{tab:psnr}
\end{table}
```

表格标题会自动编号并显示。可以使用 `\ref{key}` 来引用表格，引用处会显示编号。

placement 选项默认为 `tbp`，各选项含义如下：
- `h` 将表格尽可能地放置在当前位置，若空间不足则会自动添加 `t` 选项
- `t` 将表格放置在页面顶部
- `b` 将表格放置在页面底部
- `p` 将表格作为单独的浮动页面放置，而不是嵌入到正文中
- `!` 忽略 LaTeX 默认的表格放置限制
- 各选项的顺序不重要，未出现的选项不会被尝试，也就是说，Latex 默认不会将表格放置在当前位置




<br>

### 图像
可以使用 graphicx 宏包中的 `\includegraphic[options]{filename}` 命令来导入图片，常见的选项有：
- `width` 图像宽度，如 `0.5\textwidth`，代表页面宽度的一半
- `height` 图像高度，如 `0.5\paperheight`，代表纸张高度的一半
- `scale` 缩放因数

此外，还可以使用 graphicx 宏包中的 `\graphicspath{list of directories}` 命令来添加搜索路径，其中的每个路径都要包裹在花括号中。

与表格类似，图像也有浮动环境 figure，其使用示例如下：
```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.5\textwidth]{CTANlion.png}
  \caption{The CTAN lion, by Duane Bibby}
  \label{fig:lion}
\end{figure}
```










<br>

## 字体
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

## 数学
### Additional Component
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

### Operators
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


### Symbols
$$\lt, \le, \leq, \leqq, \leqslant, \not\lt$$
$$\gt, \ge, \geq, \geqq, \geqslant, \not\gt$$
$$\prec, \preceq, \preccurlyeq, \precapprox, \precnapprox, \precsim, \precnsim $$
$$\neq, \approx, \approxeq, \sim, \simeq, \cong, \equiv$$
$$\subset, \subseteq, \subsetneq, \supset, \in, \notin$$
$$\to, \rightarrow, \leftarrow, \Rightarrow, \Leftarrow, \iff$$
$$\forall, \exists, \mapsto, \because, \therefore$$


### Equations and Alignment
$$
y =
\begin{cases}
  \sin(x)       & x<0 \\
  x^2 + 2x +4   & 0 \leq x < 1 \\
  x^3           & x \geq 1 \\
\end{cases}
$$

$$
\begin{cases}\tag{1}
  a + b - c = 2 \\
  a - b = 4 \\
\end{cases}
$$

$$
\left\{\tag{2}
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


### Matrix
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

### Greek Alphabet
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





