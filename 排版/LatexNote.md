
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
  - [伪代码](#伪代码)
  - [代码块](#代码块)
  - [图表](#图表)
- [格式调整](#格式调整)
  - [字体样式](#字体样式)
  - [页面布局](#页面布局)
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
- `10pt|11pt|...` 设置字体大小，默认为 10pt
- `letterpaper|a4paper|a5paper|b5paper|...` 设置纸张大小，默认为 letterpaper
- `titlepage|notitlepage` 设置是否生成标题页，article 默认为 notitlepage，report 和 book 默认为 titlepage
- `oneside|twoside` 设置是单面还是双面，article 和 report 默认为 onepage，report 默认为 twopage
- `onecolumn|twocolumn` 设置页面布局为单栏/双栏排版，默认为 onecolumn
- `fleqn` 设置行间公式为左对齐，默认为居中对齐
- `leqno` 设置公式编号为左对齐，默认为右对齐
- `landscape` 设置纸张方向为横向，默认为纵向

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
- `c` 代表居中对齐，`l` 代表左对齐，`r` 代表右对齐，`|` 代表竖线
- `\hline` 代表水平线，宽度与表格相同
- `\cline{i-j}` 代表水平线，从第 i 个单元格画至第 j 个单元格
- cols 参数还可以使用 `@{}` 说明符，如 `@{\hspace{2em}}`。若两个说明符之间没有 @ 表达式，则每列的两侧都会放上 `\tabcolsep` 长度的空格，否则会放上 @ 表达式中的内容

若要跨列合并单元格，可以使用 `\multicolumn{numcols}{cols}{text}` 命令。cols 参数会覆盖原有参数，故若要保持竖线，则必须使用 `|`。

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

---
multirow 宏包可用于跨行合并单元格，命令为 `\multirow{numrows}{width}{text}`，其中 width 参数用于指定表格宽度，一般填 * 代表自动宽度。

makecell 宏包可用于表格内换行，命令为 `\makecell[alignment]{text}`，可通过在 text 中使用 `\\` 换行，对齐方式默认为居中。

diagbox 宏包可用于制作斜线表头，命令为 `\diagbox[options]{text}{text}...`，常见选项有：
- `dir=NW|NE|SW|SE` 指定斜线方向
- `width|height=<length>` 指定框的宽高
- `innerwidth=<length>` 左右文本之间的距离
- `innerleftsep|innerrighttsep=<length>` 文本与框之间的距离
- `font=<style>` 指定字体样式，如 `\footnotesize\itshape`

tabularx 宏包可用于自动调整列宽以及自动换行，命令为 `\begin{tabularx}{width}[pos]{preamble}`，其基本使用如下：
```latex
\newcolumntype{Y}{>{\centering\arraybackslash}X}
\begin{tabularx}{\textwidth}{|c|c|Y|Y|Y|}
    ...
\end{tabularx}
```
- `\arraybackslash` 常用于 `\raggedleft` `\raggedright` `\centering` 之后，恢复 `\\` 的定义
- `\newcolumntype{name}{definition}` 定义新的列类型




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

### 伪代码
可以使用 algorithm2e 宏包来编写伪代码，其基本使用如下：
```latex
\begin{algorithm}
  \KwIn{A array $A$ of size $N$}
  \KwOut{how to write algorithm with \LaTeX2e}
  \SetKwData{Sum}{sum}
  \BlankLine
  \Sum $\leftarrow$ 0\;
  \For{$i\leftarrow 1$ \KwTo $N$}{
    \Sum $\leftarrow$ \Sum $+ A[i]$\;
  }
  \Return{\Sum}
  \caption{How to write algorithms}
\end{algorithm}
```

algorithm2e 宏包常见的导入选项有：
- 环境设置
  - `plain` 默认
  - `boxed` 用方框包围算法
  - `ruled` 在算法的顶部和底部绘制水平线，并让标题从底部中央到左上方
- 块设置
  - `noline` 默认，不在块内打印竖线
  - `lined` 在块内打印竖线
  - `vlined` 在块内打印竖线，并在末尾有一小段横线，形如 $\lfloor$
- 注释
  - `scright` 默认，右对齐注释
  - `scleft` 左对齐注释
  - `fillcomment` 默认，注释的结束标志会右对齐
  - `nofillcomment` 注释的结束标志紧跟注释之后
- 行号
  - `linesnumbered` 为每行代码添加行号
- end 关键字
  - `noend` 不打印 end 关键字
  - `shortend` 默认，每个宏的 end 关键字都只是 end
  - `longend` 每个宏的 end 关键字都更长且不同

---
以下为一些常用关键字：
- 基本关键字
  - `\KwIn{input}`
  - `\KwOut{output}`
  - `\KwData{input}`
  - `\KwResult{output}`
  - `\KwTo`
  - `\KwRet{[value]}` `\Return{[value]}`
- 注释
  - `\tcp{comments}` 为一行添加注释，紧跟在代码后，默认样式为 `//`
  - `\tcp*{comments}` 为一行添加注释，注释靠右侧对齐
  - `\tcc{comments}` 为多行添加注释，默认样式为 `/* */`
  - `\tcc*{comments}` 为多行添加注释，注释靠右侧对齐
  - `\tcp|\tcc*[alignment]{comments}` 对齐标志有：
    - `r` 默认，右对齐且有换行
    - `l` 左对齐且有换行
    - `f` 右对齐且无换行
    - `h` 左对齐且无换行
- 判断语句
  - `\If(comment){condition}{then block}`
  - `\ElseIf(comment){condition}{then block}`
  - `\Else(comment){else block}`
  - 以上命令，若加上前缀 `u` 则不会打印 end 语句，若加上前缀 `l` 则不会换行也不会有 end 语句
  - `\eIf(then comment){condition}{then block}(else comment){else block}`
  - `\leIf(comment){condition}{then block}{else block}` 所有块都在一行内
- 循环语句
  - `\For(comment){condition}{do block}`
  - `\While(comment){condition}{do block}`
  - `\ForEach(comment){condition}{do block}`
  - `\ForAll(comment){condition}{do block}`
  - 以上命令，若加上前缀 `l` 则不会换行也不会有 end 语句

---
可以使用以下命令自定义宏，这样在使用自定义宏时，会以命令对应的样式打印文本：
- `\SetKwInput{csname}{text}` 定义输入输出宏，可接收一个参数
- `\SetKwInOut{csname}{text}` 定义冒号会对齐的输入输出宏，可接收一个参数
- `\SetKw{csname}{text}` 定义一个关键字宏，可接收一个参数
- `\SetKwData{csname}{text}` 定义一个变量宏
- `\SetKwFunction{csname}{text}` 定义一个函数宏，可接收一个参数
<br>

- `\SetKwComment{csname}{begin text}{end text}` 定义一个注释宏，用法同 \tcp 和 \tcc 命令
- `\SetKwIF{if csname}{elseif csname}{else csname}{if text}{then text}{elseif text}{else text}{endif text}` 定义一个判断语句宏，可以加上前缀
- `\SetKwFor{csname}{for text}{do text}{endfor text}` 定义一个循环语句宏，可以加上前缀
- `\SetKwProg{csname}{title text}{begin text}{end text}` 定义一个程序宏，可用于定义函数。该宏可接收两个参数，分别为函数原型和函数体，打印时，函数原型前后分别为 title text 和 begin text，函数体后为 end text

Python 风格：
```latex
\SetStartEndCondition{ }{}{}
\SetKwProg{Fn}{def}{:}{}
\SetKwFunction{Range}{range}
\SetKw{KwTo}{in}
\SetKwIF{If}{ElseIf}{Else}{if}{:}{elif}{else:}{}
\SetKwFor{For}{for}{\string:}{}
\SetKwFor{While}{while}{:}{}
\AlgoDontDisplayBlockMarkers\SetAlgoNoEnd\SetAlgoNoLine
```
C 风格：
```latex
\SetStartEndCondition{ (}{)}{)}
\SetAlgoBlockMarkers{}{\}}
\SetKwProg{Fn}{}{ \{}{}
\SetKwFunction{FRecurs}{void FnRecursive}
\SetKwFor{For}{for}{ \{}{}
\SetKwIF{If}{ElseIf}{Else}{if}{ \{}{elif}{else \{}{}
\SetKwFor{While}{while}{ \{}{}
\SetKwRepeat{Repeat}{repeat\{}{until}
\AlgoDisplayBlockMarkers\SetAlgoNoLine
```



<br>

### 代码块
可以使用 minted 宏包来编写代码块。在使用 minted 宏包前，需要先给 Python 安装 Pygments 库，还需要在编译时添加 `-shell-escape` 选项。

代码块的基本写法如下：
```latex
\begin{minted}[options]{language}
<code>
\end{minted}
```
若要插入单行代码块，可以使用缩写 `\mint{language}|code|`。还可以使用 `\mintinline[options]{language}|code|` 命令插入行内代码。

另一种插入代码块的方法是导入外部文件，需要使用命令 `\inputminted[options]{language}{file}`，其中 file 参数支持相对路径。

常用的选项有：
- `bgcolor=<string>` 设置代码块背景颜色，常用的有 black, gray, lightgray, white 等。此外，还可以使用 `\definecolor{name}{model}{color}` 命令自定义颜色，如 `\definecolor{bg}{RGB}{242, 242, 242}` 和 `\definecolor{bg}{rgb}{0.9, 0.9, 0.9}`
- `style=<string>` 设置配色风格，常用的有 bw, sas, staroffice, xcode, default, monokai, lightbulb, github-dark, rrt 等。此外，还可以在导言区使用 `\usemintedstyle[language]{pygments style}` 命令设置全局配色
- `fontsize=<font size>` 设置字体大小，常用的有 \small 和 \footnotesize
- `baselinestretch=<factor>` 设置块内行间距
- `linenos[=true]` 显示行号
- `numbersep=<length>` 设置行号和代码块之间的距离
- `frame=<none|leftline|topline|bottomline|lines|single>` 设置边框，`lines` 为上下边框，`single` 为所有边框
- `framerule=<length>` 设置边框宽度
- `framesep=<length>` 设置边框与文本的距离

若要修改字体类别，可以先导入 fontspec 宏包，再使用 `\setmonofont{}` 命令，如 `\setmonofont{FiraCode-Regular.ttf}`。

若要修改行号样式，可以使用 `\renewcommand{\theFancyVerbLine}{define}` 命令，一个示例为 `\renewcommand{\theFancyVerbLine}{\sffamily\textcolor{gray}{\scriptsize\arabic{FancyVerbLine}}}`

若要修改全局设置，可以在导言区使用 `\setminted[language]{options}` 命令。若要单独修改行内代码的全局设置，可以使用命令 `\setmintedinline[language]{options}`。若省略了 language 选项，则会对所有语言应用设置。




<br>

### 图表
可以使用 pgfplots 宏包绘制多种图表，其基本使用如下：
```latex
\begin{tikzpicture}
    \begin{axis}[
        title=Inv. cum. normal,
        xlabel={$x$},
        ylabel={$f(x)$},
    ]
        \addplot[
            blue,
            mark=*,
        ]
        coordinates {
            (1, 2) (2, 4) (5, 6)
            (7, 5) (9, 10)
        };
    \end{axis}
\end{tikzpicture}
```

- 若要绘制散点图，应该添加选项 `scatter, only marks`
- 若要绘制柱状图，应该添加选项 `ybar/xbar`；若要添加符号坐标，可以添加选项 `symbolic x coords={A, B, C, D, E}`
- 若要添加图例，应该在 `\addplot` 语句后使用 `\addlegendentry{}`
- 若要从外部文件导入数据，应将 `coordinates {}` 换为 `table {*.dat}`，文件格式为每行一个数据点，每个数据点的不同分量用空格分隔。
- 若要坐标轴取对数，可以使用 loglogaxis, semilogx/yaxis 环境，或者在 axis 环境中使用 `y/xmode=log`
- 若要添加全局设置，可以使用 `\pgfplotsset{every axis/.append style={options}}` 命令

常用选项有：
- `smooth` 使折线图平滑
- `mark` 设置记号的形状，常用的有 `*` `x` `+` 等
- `xmin/xmax/ymin/ymax=<coord>` 改变坐标轴的最小/大值
- `xtick/ytick=<coord list>/data` 设置坐标轴上的刻度线，若为 `data`，则会使用数据的值作为刻度线的位置
- `xticklabels/yticklabels={label list}` 为每个刻度线添加标签
- `xticklabel style={style}` 改变刻度线标签的样式
- `legend style={font=\small, cells={anchor=west}, inner ysep=0.5em}` 改变图例样式
- `legend pos==south west|south east|north west|north east|outer north east` 改变图例位置，默认为 north east










<br>

## 格式调整
### 字体样式
文本字体样式命令有两种格式，分别为 `\text..{}` 和 `\..family|series|shape`。前者接收一个参数，后者改变整个所在环境的字体样式。文本字体样式是可叠加的，不同类别的命令可以嵌套生效，相同类别的命令最内层的会生效。
- 字体族
  - `\textrm` `\rmfamily` 罗马字体 (Roman)，又称衬线字体，默认
  - `\textsf` `\sffamily` 无衬线字体 (San Serif)，又称等线字体
  - `\texttt` `\ttfamily` 打印机字体 (Typewriter)，又称等宽字体
  - 若要修改默认字体族，可使用 `\renewcommand{\familydefault}{\rmdefault|\sfdefault|\ttdefault}` 命令
- 字体系列
  - `\textmd` `\mdseries` 正常 (Medium)
  - `\textbf` `\bfseries` 粗体 (Boldface)
- 字体形状
  - `\textup` `\upshape` 正体 (Upright)
  - `\textit` `\itshape` 斜体 (Italic)，字形可能会发生变化
  - `\textsl` `\slshape` 倾斜体 (Slanted)
  - `\textsc` `\scshape` 小型大写体 (Small Caps)
- `\textnomal` `\nomalfont` 默认字体样式

数学字体样式不可叠加，只有最内层的命令会生效。除了上述命令以外，数学字体还有以下样式：
- `\mathbb` 黑板粗体字母 - $\mathbb{R}$
- `\mathcal` 书法体字母 - $\mathcal{R}$
- `\mathscr` 手写体字母 - $\mathscr{R}$
- `\mathfrak` 哥特体字母 - $\mathfrak{R}$

字体大小从小到大依次为：`\tiny` `\scriptsize` `\footnotesize` `\small` `\normalsize` `\large` `\Large` `\LARGE` `\huge` `\Huge`。这些命令会改变整个环境的字体大小。

此外，还可以通过 `\textcolor[model]{color}{text}` 命令设置字体颜色。其中 color 参数可为自带的颜色，如 `\textcolor{red}{text}`；可为 RGB 值，如 `\textcolor[RGB]{255, 0, 0}{text}` 或 `\textcolor[rgb]{1, 0, 0}{text}`；还可为使用 `\definecolor` 命令自定义的颜色。

---
使用 fontspec 宏包可以方便地设置字体族，以下为其常用命令：
- `\setmainfont{font}[font features]` 设置默认衬线字体
- `\setsansfont{font}[font features]` 设置默认无衬线字体
- `\setmonofont{font}[font features]` 设置默认等宽字体
- `\setfontfamily{cmd}{font}[font features]` 设置自定义字体族，如在使用过 `\setfontfamily{\siyuan}{思源黑体 CN}` 命令后，就可用 `\siyuan` 改变整个环境的字体族

字体可以通过名称或文件名指定，搜索路径为 C:\Windows\Fonts 和 TEXMF 树，若指定文件名，还可以在用户文件夹的 Windows\Fonts 中搜索。

常见的字体特征有：
- `Color=<color>` 设置字体默认颜色，参数可为 xcolor 定义的颜色或十六进制码
- `Scale=<number>|MatchLowercase|MatchUppercase` 设置字体默认大小，若为 MatchLowercase 则将匹配其他字体的小写字母高度，若为 MatchUppercase 则将匹配其他字体的大写字母高度




<br>

### 页面布局
可以使用 geometry 宏包调整页面布局，其选项如下：
- `letterpaper|a4paper|a5paper|b5paper|...` 设置纸张大小
- `landscape|portrait` 设置纸张方向
- `scale|hscale|vscale=<number>` 设置正文区域与纸张的尺寸比例
- `width|height=<length>` 设置正文区域的宽高
- `text|body={<width>, <height>}` 设置正文区域的宽高
- `left|right|top|bottom|lmargin|rmargin|tmargin|bmargin=<length>` 设置页边距
- `centering` 设置正文区域居中
- `onecolumn|twocolumn` 设置页面布局为单栏/双栏排版











<br>

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





