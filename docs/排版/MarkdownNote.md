
# Markdown 笔记

## 文档结构

Markdown 的段落之间需要用空行隔开，否则可能被认为是同一个段落。不过 Markdown 支持内联 HTML 语法，因此可以使用 `<p> ... </p>` 来标记段落，使用 `<br>` 来换行。

需要注意的是，即使 HTML 标签加上了 `markdown="1"` 属性，此时标签内的 Markdown 语法也无法被解析，若要在 HTML 标签内使用 Markdown 语法，需要使用 `md_in_html` 扩展。

标题使用 `#` 标记，并用数量表示层级，如 `## heading` 为二级标题。可以给标题添加自定义编号，具体格式为 `## heading {#custom-id}`。这样以后，就可以使用 `#custom-id` 作为链接进行访问。该语法来自扩展 `attr_list`，其更完整的用法为 `{: #someid .someclass somekey='some value' }`。

此外，我们还可以使用 `[TOC]` 或者 `[toc]` 来自动生成目录，该语法来自扩展 `toc`，其常用选项有：

- `toc_depth` 会被生成的章节层次，`N` 代表第一层到第 N 层，`N-M` 代表第 N 层到第 M 层，默认为 `6`
- `permalink` 若为 True 或者字符串，则会自动在每个标题后加上一个永久链接，前者的连接文本是 `&para;`
- `anchorlink` 若为 True 则会将标题变成指向自己的链接
- `marker` 生成目录的标记，默认为 `[TOC]`




<br>

## 常见样式

Markdown 可以使用 `*` 或 `_` 来格式化文字：

- 被单个 `*` 或 `_` 包围会变成*斜体*
- 被两个 `*` 或 `_` 包围会变成**粗体**
- 被三个 `*` 或 `_` 包围会变成***斜粗体***

除此以外，常见的标记有：

| 描述 | 标记 |
| :---: | :---: |
| 分割线 | `---` `***` `___` |
| 删除线 | `~~text~~` |
| 下划线 | `<u>text</u>` `^^text^^` |
| 高亮 | `==text==` |
| 下标 | `a~n+1~` |
| 上标 | `a^n+1^` |

其中删除线和下标由扩展 `pymdownx.tilde` 支持，下划线与上标由扩展 `pymdownx.caret` 支持，高亮由扩展 `pymdownx.mark` 支持。




<br>

## 列表

无序列表以 `-` `*` `+` 打头，有序列表以 `1.` 等打头，两者支持嵌套使用。不过需要注意的是，有序列表的序号只由第一项决定，后续所有序号均在第一项序号的基础上递增，与手动指定的数字无关。

扩展 `def_list` 提供了定义列表，该列表以 `:` 打头，需要前面一行非空，使用示例如下：

```markdown
First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.
```

此外，扩展 `pymdownx.tasklist` 还提供了任务列表，使用示例如下：

```markdown
- [x] Done task
- [ ] Undone task
```



<br>

## 引用块

Markdown 可以在一个段落前使用 `>` 来使其变成引用块，`>` 可以叠加使用来进行嵌套，区块内可以正常使用各种元素，示例如下：

```markdown
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.
```



<br>

## 代码块

行内代码可以使用单个反引号 `` ` `` 包裹，若要在行内代码中使用 `` ` ``，可以将其用双反引号包裹。

代码块可以通过缩进四个空格来创建，或者使用三个 `` ` `` 或 `~` 包裹，后者为扩展 `fenced_code` 的语法。若要在代码块中使用三个反引号，可以将代码块用四个反引号包裹。

若要实现行内代码高亮，可以使用扩展 `pymdownx.inlinehilite`，此时行内代码的语法为 `` :::language mycode `` 或 `` #!language mycode ``。

若要实现代码块高亮，可以使用扩展 `pymdownx.superfences`，此时可以在 `` ``` `` 或 `~~~` 后面加上语言名称，例如 `` ```python ``。

除此以外，SuperFences 还支持在区块中嵌入代码块，保留 Tab 字符，像属性列表一样注入 ID、类和属性等信息，并允许使用各种自定义代码块。

### 自定义样式

通过注入属性，可以为每个代码块单独定义样式，常见的有：

- `linenums` 设置行号
    - `linenums="2"` 从 2 开始编号
    - `linenums="1 2"` 从 1 开始编号，每遇到 2 的倍数才显示行号
    - `linenums="1 1 2"` 从 1 开始编号，每行都显示，每遇到 2 的倍数则为行号加一个 `special` 类
- `hl_lines` 设置行高亮
    - `ht_lines="1 3"` 将第一行和第三行高亮
    - `hl_lines="1-2 5 7-8"` 将第一到二行、第五行、第七到八行高亮
- `title` 设置标题

`` ```{.python linenums="2" hl_lines="1-2 5 7-8" title="Example"} `` 的效果如下：

```{.python linenums="2" hl_lines="1-2 5 7-8" title="Example"}
"""Some file."""
import foo
import boo.baz
import foo.bar.baz

class Foo:
   def __init__(self):
       self.foo = None
       self.bar = None
       self.baz = None
```

---

InlineHilite 和 SuperFences 都支持通过 `pymdownx.highlight` 全局配置样式，其常用选项有：

- `linenums` 默认为 None，若为 True 则会使所有代码块显示行号
- `linenums_special` 默认为 1，设置每 n 行为 `special` 类
- `anchor_linenums` 若为 True，则会将行号包裹进 `<a>` 中。若未配置 `line_anchors`，则每一行的链接为 `#__codelineno-<code_block_number>-<line_number>`
- `line_anchors` 修改行号链接的开头
- `auto_title` 默认为 None，若为 True 则会直接由 Pygments 提供标题
- `auto_title_map` 修改 `auto_title` 默认的语言名称，例如：

    ```json
    "auto_title_map": {
        "Python Console Session": "Python",
        "Text Only": "Text",
    }
    ```

### 自定义代码块

可以通过 SuperFences 的 `custom_fences` 属性来自定义代码块，`custom_fences` 需要一个列表，列表内每个元素是一个字典，字典内需要包含的键有：

- `name` 使用代码块时的名称
- `class` 被转换为 HTML 后的类名
- `format` 格式化输出的 HTML 的函数
    - `superfences.fence_code_format` 将代码块置于 `<pre><code>` 块内
    - `superfences.fence_div_format` 将代码块置于 `<div>` 块内

一个配置示例为：

```json
"custom_fences": [
    {
        'name': 'mermaid',
        'class': 'mermaid',
        'format': pymdownx.superfences.fence_div_format
    }
]
```

在这里，代码块会被包裹进一个类为 `mermaid` 的块，从而被识别渲染。Mermaid 的语法请见前端 [Mermaid 笔记](https://zhroyn.github.io/MyNotes/%E5%89%8D%E7%AB%AF/MermaidNote/)。




<br>

## 链接

链接的基本格式为 `<link>` 或者 `[text](link 'title')`。其中 `link` 可以是 URL，可以是本地文件，也可以是 `#custom_id` 这样的标题编号；`title` 是鼠标悬停时出现的文字，是可选的。

若要自动识别并形成链接，可以使用扩展 `pymdownx.magiclink`。

另一种类型的链接是引用样式链接，可以将具体的链接写在文件的其他位置，而此处用简称代替，使用示例如下：

```markdown
This is the [official tutorial][link].

[link]: markdown.com.cn 'Markdown'
```

此外，还可以使用扩展 `footnotes` 支持脚注语法，使用示例如下：

```markdown
Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.
```

另一种与脚注类似的语法是缩略语，由扩展 `abbr` 提供。当鼠标悬停在缩略语上时会显示全称，效果等同 `<abbr>` 标签，使用示例如下：

```markdown
The HTML specification
is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium
```



<br>

## 图片

Markdown 支持插入图片，其使用示例如下：

```markdown
![text](src)
![text](src 'title')
[![text](src 'title')](link)
```

若要使图片居中，可以将图片嵌入 `<center>` 或 `<div align="center">` 标签中。

若要调整图片大小，只能转而使用 `<img>` 标签，例如 `<img src="..." width = 60%/>`。




<br>

## 表格

Markdown 支持插入表格，其使用示例如下：

```markdown
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
```

可以通过在标题行中的连字符的左侧、右侧或两侧添加冒号，将列中的文本对齐到左侧，右侧或中央：

```markdown
| Left | Center | Right|
|:---- | :----: | ----:|
| Cell |  Cell  | Cell |
| Cell |  Cell  | Cell |
```

若不添加冒号，则默认为标题行居中，其他行左侧对齐。




<br>

## 公式

Markdown 可以使用 Katex 或 MathJax 来渲染数学公式，分为：

- 行内公式：`$ ... $` `\( ... \)`
- 行间公式：`$$ ... $$` `\[ ... \]`

如果要支持更多的数学公式，需要使用扩展 `pymdownx.arithmatex`，效果如下：

$f(x) = \sin(x)$

$$
\begin{matrix}
   a & b \\
   c & d
\end{matrix}
$$

$$
\begin{CD}
    A @>a>> B \\
    @VbVV @AAcA \\
    C @= D
\end{CD}
$$

!!! warning

    Arithmatex 有选项 `generic`，若为 True 则会输出适用于非 MathJax 库的格式。在 mkdocs 中必须要启用这个选项。



<br>

## 告示

扩展 `admonition` 以更加丰富多彩的样式显示文本，其基本格式为：

```markdown
!!! type summary
```

若不想显示标题，可以将 summary 置为 `""`，否则会以此告示类型为标题。

如果想要告示被折叠，可以使用扩展 `pymdownx.details`，只需将 `!!!` 替换为 `???` 即可，若想默认展开，则替换为 `???+`。

mkdocs 支持的告示有 `note` `abstract` `info` `tip` `success` `question` `warning` `failure` `danger` `bug` `example` `quote` 等，其效果如下：

!!! note

    This is note

!!! abstract

    This is abstract

!!! info

    This is info

!!! tip

    This is tip

!!! success

    This is success

!!! question

    This is question

!!! warning

    This is warning

!!! failure

    This is failure

!!! danger

    This is danger

!!! bug

    This is bug

!!! example

    This is example

!!! quote

    This is quote


<br>

## 标签页

扩展 `pymdownx.tabbed` 可以实现标签页，其标志为 `===`，一个使用示例如下：

```markdown
=== "Tab 1"
    Markdown **content**.

    Multiple paragraphs.

=== "Tab 2"
    More Markdown **content**.

    - list item a
    - list item b
```

若想将多个连续标签页分成两个部分，可以在一个 `===` 后面加上 `!` 变成 `===!`。

若想默认选择另一个标签页，可以在一个 `===` 后面加上 `+` 变成 `===+`。

!!! warning

    Tabbed 有选项 `alternate_style`，若为 True 则会启用实验性的候选样式。在 mkdocs 中必须要启用这个选项。



<br>

## 批注

扩展 `pymdownx.critic` 可以支持批注标记，包括：

- 新增：`{++ ++}`
- 删除：`{-- --}`
- 替换：`{~~ ~> ~~}`
- 注释：`{>> <<}`
- 高亮：`{== ==}{>> <<}`

通过这个扩展，可以实现类似 Github 展示代码差异的效果。



<br>

## 特殊字符

|   描述  |  符号  | 效果 |
|  :---: | :---: | :---: |
| 全角空格 | `&emsp;` `&#8195;` | 空&emsp;格 |
| 半角空格 | `&ensp;` `&#8194;` | 空&ensp;格 |
| 不换行空格 | `&nbsp;` `&#160;` | 空&nbsp;格 |
| 窄空格 | `&thinsp;` `&#8201;` | 空&thinsp;格 |
| 竖线 | `&#124;` | &#124; |
| 勾 | `&#10003;` `&#10004;` | &#10003; &#10004; |
| 叉 | `&#10005;` `&#10006;` `&#10007;` `&#10008;` | &#10005; &#10006; &#10007; &#10008; |



<br>

## Emoji 表情

扩展 `pymdownx.emoji` 提供了 Emoji 支持，使用格式为 `:emoji:`，例如 :white_check_mark: :negative_squared_cross_mark:。

完整的 Emoji 列表可见 https://gist.github.com/rxaviers/7360908。

