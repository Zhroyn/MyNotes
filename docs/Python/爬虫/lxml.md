# lxml 笔记

`lxml` 是一个功能强大的 Python 库，用于处理 XML 和 HTML 文档。它结合了 `libxml2` 和 `libxslt` 库的高性能，并兼容  ElementTree API。`lxml` 支持 XPath、XSLT、XML Schema 验证等高级功能，是处理 XML 和 HTML 文档的首选工具之一。

`lxml` 有 `etree` 和 `html` 两个模块，分别用于处理 XML 和 HTML 文档。`etree` 模块严格遵循 XML 规范，要求文档格式良好；`html` 模块对 HTML 文档的容错性更强，能够处理不规范（malformed）的 HTML。



## 解析与序列化

`etree` 和 `html` 模块可以通过以下函数解析 XML/HTML 文档，结果是一个 `Element` 对象：

- `parse(source)` 从文件路径、URL 或文件对象解析文档，得到的 `ElementTree` 再通过 `getroot()` 方法获取根元素
- `fromstring(string)` 从字符串解析文档

`etree` 和 `html` 模块可以通过以下函数序列化元素：

- `tostring(element)` 将元素转换为字符串

`ElementTree` 对象还可以使用 `write(file)` 方法将文档保存到文件，`file` 可以是文件路径或文件对象。



## 元素操作

元素的属性有：

- `tag` 元素的标签名
- `text` 元素的文本内容
- `attrib` 元素的属性字典

元素对象支持以下方法：

- `get(key)` 获取属性字典中指定属性的值
- `set(key, value)` 设置属性字典中指定属性的值
- `append(element)` 添加子元素
- `remove(element)` 删除子元素
- `find(path)` 查找第一个匹配的子元素，仅支持简单的路径查询，无法处理复杂的 XPath 表达式，例如不支持绝对路径和属性查询
- `findall(path)` 查找所有匹配的子元素，同上
- `xpath(path)` 查找所有匹配的子元素，支持完整的 XPath 语法



## XPath

XPath 是一种用于选择 XML 文档中节点的语言，它提供了一种在 XML 文档中定位节点的方法。以 `/` 开头的路径为绝对路径，不以 `/` 开头的路径为相对路径。

### 轴

在 XPath 中，轴（Axis） 是一种用于定义节点之间关系的机制。轴允许你从当前节点出发，沿着特定的方向或关系选择其他节点，语法为 `轴名称::节点测试`。

常用的轴有：

- `child::` 选择当前节点的子节点，等价于直接使用节点测试
- `self::` 选择当前节点，缩写为 `.`
- `parent::` 选择当前节点的父节点，缩写为 `..`
- `ancestor::` 选择当前节点的所有祖先节点
- `descendant::` 选择当前节点的所有后代节点
- `following-sibling::` 选择当前节点之后的所有同级节点
- `preceding-sibling::` 选择当前节点之前的所有同级节点
- `following::` 选择当前节点之后的所有节点（不限于同级节点）
- `preceding::` 选择当前节点之前的所有节点（不限于同级节点）
- `attribute::` 选择当前节点的属性节点，缩写为 `@`
- `namespace::` 选择当前节点的命名空间节点
- `descendant-or-self::` 选择当前节点的所有后代节点及当前节点本身，缩写为 `//`，如果在路径表达式的开头使用，则表示从根节点开始
- `ancestor-or-self::` 选择当前节点的所有祖先节点以及当前节点本身

### 节点测试

在 XPath 中，节点测试（Node Test） 是用于指定要选择的节点类型或名称的机制。节点测试可以分为以下几类：

- 名称测试：选择具有指定名称的节点，例如 `div`、`p` 等
- 通配符：选择所有节点，例如 `*` 匹配所有元素节点，`@*` 匹配所有属性节点
- 类型测试：选择特定类型的节点
    - `node()` 选择所有类型的节点（元素、文本、注释等）
    - `text()` 选择文本节点
    - `comment()` 选择注释节点
    - `processing-instruction()` 选择处理指令节点

### 谓语

谓语是 XPath 中用于过滤节点的条件表达式，通常放在方括号 [] 中。谓语可以是布尔表达式、位置索引、函数调用等。

谓语使用示例如下：

- `div[1]` 选取第一个 `div` 元素
- `div[last()]` 选取最后一个 `div` 元素
- `div[last()-1]` 选取倒数第二个 `div` 元素
- `div[position()<3]` 选取前两个 `div` 元素
- `div[@class]` 选取所有具有 `class` 属性的 `div` 元素
- `div[@class='test']` 选取所有 `class` 属性为 `test` 的 `div` 元素
- `div[@class='test' and not(@id='test')]` 选取所有 `class` 属性为 `test` 且 `id` 属性不为 `test` 的 `div` 元素
- `div[contains(@class, 'test')]` 选取所有 `class` 属性包含 `test` 的 `div` 元素
- `p[text()]` 选取所有具有文本内容的 `p` 元素
- `p[contains(text(), 'Hello')]` 选取所有文本内容包含 `Hello` 的 `p` 元素

以下是一些常用的操作符和函数：

- 比较操作符：`=`、`!=`、`<`、`<=`、`>`、`>=`
- 逻辑操作符：`and`、`or`、`not()`
- 字符串函数：
    - `contains(string, substring)` 检查字符串是否包含指定字符串
    - `starts-with(string, prefix)` 检查字符串是否以指定字符串开头
    - `ends-with(string, suffix)` 检查字符串是否以指定字符串结尾
    - `string-length(string)` 返回字符串的长度
    - `substring(string, start, length)` 返回字符串的子串
    - `substring-before(string, separator)` 返回分隔符之前的子串
    - `substring-after(string, separator)` 返回分隔符之后的子串
    - `translate(string, from, to)` 替换字符串中的字符
    - `normalize-space(string)` 去除字符串两端的空白字符，并将内部连续空白字符替换为单个空格
- 数值函数：
    - `number()` 将参数转换为数字
    - `floor()` 将参数向下取整
    - `ceiling()` 将参数向上取整
    - `round()` 将参数四舍五入
    - `count()` 返回节点集合中节点的数量
    - `sum()` 返回节点集合中所有节点的数字之和
- 节点集函数：
    - `last()` 返回节点集中的最后一个节点的位置
    - `position()` 返回当前节点在节点集中的位置
- 名称函数：
    - `name()` 返回当前节点的名称

