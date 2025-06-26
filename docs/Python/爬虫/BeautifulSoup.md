# BeautifulSoup 笔记

BeautifulSoup 是一个用于解析 HTML 和 XML 文档的 Python 库。它能够从这些文档中提取数据，并提供了简单易用的 API 来遍历和搜索文档树。BeautifulSoup 通常与 lxml 或 html.parser 等解析器一起使用，以便处理不规范的 HTML 文档。

与 lxml 相比，BeautifulSoup 提供了更高层次的 API，适合快速提取数据，尤其是对初学者非常友好。


## 安装与导入

在使用 BeautifulSoup 之前，需要先安装它。可以通过以下命令安装：

```bash
pip install beautifulsoup4
```

安装完成后，可以通过以下方式导入：

```python
from bs4 import BeautifulSoup
```


## 解析与序列化

`BeautifulSoup` 可以通过以下方式解析 HTML/XML 文档：

- `BeautifulSoup(doc, 'html.parser')` 使用 Python 内置的 `html.parser` 解析器解析 HTML 文档
- `BeautifulSoup(doc, 'lxml')` 使用 `lxml` 解析器解析 HTML 文档
- `BeautifulSoup(doc, 'xml')` 使用 `lxml` 解析器解析 XML 文档

解析后的结果是一个 `BeautifulSoup` 对象，可以通过以下方式序列化：

- `soup.prettify()` 将文档格式化为字符串，会自动添加缩进和换行，适合打印或保存
- `str(soup)` 或 `soup.encode()` 将文档转换为字符串或字节串



## 元素操作

`BeautifulSoup` 对象和元素对象（如 `Tag` 对象）有以下属性和方法：

### 属性

- `tag.name` 元素的标签名
- `tag.string` 元素的文本内容。如果元素包含多个子元素，返回 `None`
- `tag.text` 元素及其所有子元素的文本内容
- `tag.attrs` 元素的属性字典
- `tag.contents` 元素的子节点列表
- `tag.parent` 元素的父节点
- `tag.children` 元素的子节点迭代器
- `tag.descendants` 元素的所有后代节点迭代器
- `tag.next_sibling` 元素的下一个兄弟节点
- `tag.next_siblings` 元素之后的所有兄弟节点迭代器
- `tag.previous_sibling` 元素的上一个兄弟节点
- `tag.previous_siblings` 元素之前的所有兄弟节点迭代器

### 方法

- `tag.get(key, default=None)` 获取指定属性的值
- `tag[key]` 获取指定属性的值（与 `get` 方法类似）
- `tag.has_attr(key)` 检查元素是否具有指定属性
- `tag.find(name=None, attrs={}, recursive=True, string=None, **kwargs)` 查找第一个匹配的子元素
- `tag.find_all(name=None, attrs={}, recursive=True, string=None, limit=None, **kwargs)` 查找所有匹配的子元素
    - `name` 标签名
    - `attrs` 属性字典，用于过滤元素
    - `recursive` 是否递归查找子元素
    - `string` 文本内容
    - `limit` 返回结果的最大数量
- `tag.select(selector)` 使用 CSS 选择器查找元素



## CSS 选择器

CSS 选择器规定了 CSS 规则会被应用到哪些元素上。BeautifulSoup 提供了 `select` 方法，可以使用 CSS 选择器查找元素。

### 基本选择器

- `*` 通用选择器，匹配所有元素
- `tag` 标签选择器，根据给定的节点名称选择元素
- `.class` 类选择器，根据给定的类名选择元素
- `#id` ID 选择器，根据给定的 ID 选择元素，在每个文档中 ID 必须是唯一的
- `[attr]` 属性选择器
    - `[attr=value]` 属性值完全匹配
    - `[attr^=value]` 属性值以指定值开头
    - `[attr$=value]` 属性值以指定值结尾
    - `[attr*=value]` 属性值包含指定值
    - `[attr~=value]` 属性值包含指定值的一个或多个空格分隔的词

### 分组选择器

可以使用逗号 `,` 将多个选择器组合在一起，选择所有能被列表中的任意一个选择器选中的节点。

### 组合器

- `A B` 后代选择器，选择 A 元素的后代 B 元素
- `A > B` 子元素选择器，选择 A 元素的直接子元素 B
- `A + B` 相邻兄弟选择器，选择 A 元素的下一个兄弟元素 B
- `A ~ B` 通用兄弟选择器，选择 A 元素之后的所有兄弟元素 B

### 伪选择器

BeautifulSoup 仅支持伪类选择器，而不支持伪元素选择器。

BeautifulSoup 中常用的伪类选择器有：

- `:first-child` 选择父元素的第一个子元素
- `:last-child` 选择父元素的最后一个子元素
- `:nth-child(n)` 选择父元素的第 n 个子元素
- `:nth-last-child(n)` 选择父元素的倒数第 n 个子元素
- `:only-child` 选择父元素的唯一子元素
- `:empty` 选择没有子元素的元素
- `:not(selector)` 选择不匹配指定选择器的元素
- `:has(selector)` 选择包含指定选择器的元素
- `:contains(text)` 选择包含指定文本的元素
