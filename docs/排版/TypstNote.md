
# Typst 笔记

## 基本标记

Typst 基本的标记及其对应的函数有：

| 描述 | 标记 | 函数 |
| :---: | :---: | :---: |
| 段落 | 空行 | `parbreak()` |
| 粗体 | `*` | `strong()` |
| 斜体 | `_` | `emph()` |
| 链接 | `https://typst.app/` | `link()` |
| 标签 | `<intro>` | `label()` |
| 引用 | `@intro` | `ref()` |
| 标题 | `=` | `heading()` |
| 纯文本 | ``` `print(1)` ``` | `raw()` |
| 无序列表 | `-` | `list()` |
| 有序列表 | `+` | `enum()` |
| 术语列表 | `/` | `terms()` |
| 换行 | `\` | `linebreak()` |




<br>

## 格式化

Typst 可以使用 `set` 关键字设置规则，自定义元素的展示效果，具体方法就是在 `#set` 后接一个对元素函数的调用，例如 `#set heading(numbering: "I.")`。需要注意的是，这里只接受可选参数。

在顶层设置的规则会一直应用到文件末尾，若想限定规则在一定范围内生效，则可将规则设置在 `#[ ... ]` 块中。

此外，若想选择性地应用规则，还可在函数后使用 `if` 关键字，比如：

```typst
#let task(body, critical: false) = {
  set text(red) if critical
  [- #body]
}

#task(critical: true)[Food today?]
#task(critical: false)[Work deadline]
```

---

若想更自由地定义规则，还可以使用 `show` 关键字，其基本使用格式为 `show selector: set-rule/function`，其中选择器可以是：

- 空，表示之后的所有元素，如 `show: rest => ..`
- 文本，如 `show "Text": ..`
- 正则表达式，如 `show regex("\w+"): ..`
- 元素函数，如 `show "heading": ..`
- 带字段的函数，如 `show heading.where(level: 1): ..`
- 标签，如 `show <intro>: ..`

冒号后面可以是 set rule，也可以是任意一个函数，比如：

```typst
#set heading(numbering: "(I)")
#show heading: it => [
  #set align(center)
  #set text(font: "Inria Serif")
  \~ #emph(it.body)
     #counter(heading).display() \~
]
```







<br>

## 数学模式

- 行内公式：`$x^2$`
- 行间公式：`$ x^2 $`
