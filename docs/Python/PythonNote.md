
- [Python 笔记](#python-笔记)
    - [内建函数](#内建函数)
        - [迭代](#迭代)
        - [转换](#转换)
        - [算术](#算术)
        - [对象](#对象)
        - [输入输出](#输入输出)
    - [内建类型](#内建类型)
        - [数字](#数字)
        - [列表和元组](#列表和元组)
        - [范围和切片](#范围和切片)
        - [字符串](#字符串)
            - [查找和删除](#查找和删除)
            - [分割和合并](#分割和合并)
            - [转换](#转换-1)
            - [判断](#判断)
            - [格式化](#格式化)
        - [字节序列](#字节序列)
        - [集合](#集合)
        - [字典](#字典)
        - [文件](#文件)
    - [命令行选项](#命令行选项)
    - [Expressions](#expressions)
        - [Atoms](#atoms)
            - [Comprehensions and Generator expressions](#comprehensions-and-generator-expressions)
            - [Yields expressions and Generator functions](#yields-expressions-and-generator-functions)
        - [Primaries](#primaries)
        - [Operators](#operators)
        - [Assignment, Conditional and Lambda Expressions](#assignment-conditional-and-lambda-expressions)
    - [Statements](#statements)
        - [Function definitions](#function-definitions)
            - [Decorator](#decorator)







# Python 笔记
## 内建函数
### 迭代
- `all(iterable)` 若对所有项 bool(x) 均为 True 则返回 True
- `any(iterable)` 若存在项使得 bool(x) 为 True 则返回 True
<br>

- `max/min(iterable, *[, default=obj, key=func])`
- `max/min(arg1, arg2, *args, *[, key=func])`
    - 若为一个可迭代对象，则返回其中的最大/最小值；若为多个参数，则返回多个参数中的最大/最小值
    - `key` 单参数函数，返回的值用于排序
    - `default` 当可迭代对象为 None 时返回的值
    - `max(words, key=len)`
    - `max(students, default={}, key=lambda x: x.get('grade'))`
<br>

- `sorted(iterable, /, *, key=None, reverse=False)` 返回一个新的升序排序的列表，不会改变原有可迭代对象
    - `key` 单参数函数，返回的值用于排序
    - `reverse` 若为 True 则变为降序排序
- `reversed(seq)` 返回一个反转迭代器
<br>

- `map(func, *iterables)` 返回一个迭代器，对可迭代对象中的每一项应用指定函数，直至其中一个的可迭代对象被遍历完时停止
    - `func` 参数个数必须与可迭代对象个数一致
    - `map(str.lower, words)`
    - `map(lambda x, y: x + y, [1, 2, 3], [0, 5, 3])`
- `filter(function or None, iterable)` 返回一个迭代器，生成 function(item) 为 True 的对象，若 function 为 None，则生成 item 为 True 的对象
    - `filter(lambda x: x % 2 == 0, numbers)`
<br>

- `enumerate(iterable, start=0)` 返回一个 enumerate 对象，每次生成一个 (count, value)，其中 count 为当前计数，value 为可迭代对象生成的值
- `zip(*iterables, strict=False)` 返回一个 zip 对象，每次生成一个 n 元数组，直至其中一个的可迭代对象被遍历完时停止
    - `strict` 若为 True，则会在可迭代对象长度不等时抛出 ValueError


### 转换
- `bin(number)` 将 number 转换为前缀为 0b 的二进制字符串
- `oct(number)` 将 number 转换为前缀为 0o 的八进制字符串
- `hex(number)` 将 number 转换为前缀为 0x 的十六进制字符串
<br>

- `chr(i)` 返回一个序数为 i 的 Unicode 字符
- `ord(c)` 返回一个单字符字符串的 Unicode 码点
<br>

- `eval(source, globals=None, locals=None)` 将 source 字符串当作 Python 表达式进行求值
    - `globals` 默认为当前的全局命名空间
    - `locals` 默认为当前的局部命名空间
    - `eval("a + b", {"a": 1, "b": 2})`
- `repr(obj)` 返回一个对象的规范字符串表示
    - 在大多数情况下，eval(repr(obj)) == obj，否则返回一个用尖括号括起来的字符串，其中包含类型、名称、地址等信息，或者由 \_\_repr\_\_() 方法指定
- `ascii(obj)` 类似 repr()，但会使用 \\x, \\u 或 \\U 转义序列来表示非 ASCII 字符


### 算术
- `abs(x)` 返回绝对值
- `pow(base, exp, mod=None)` 返回 base**exp % mod
- `divmod(x, y)` 返回一对商和余数，即 (x//y, x%y)，满足 div * y + mod == x
- `round(number, ndigits=None)` 当 ndigits 为 None 时，返回整数，否则返回指定精度的小数
    - `round(10.5)` 返回 10
    - `round(10.5, 0)` 返回 10.0
    - `round(10.5001, 1)` 返回 10.6


### 对象
- `id(obj)` 返回对象的标识，在 CPython 中为对象的内存地址
- `hash(obj)` 返回对象的哈希值，比较起来相等的两个对象哈希值也相等，如不同类型的相等数字
- `type(obj)` 返回对象的类型，不考虑继承关系，若 obj 为一个类则返回 type
<br>

- `issubclass(class, class_or_tuple)` 判断 cls 是否为后一个类或元组包含的多个类中任意类的子类，考虑继承关系，一个类是本身的子类
- `isinstance(obj, class_or_tuple)` 判断 obj 是否为后一个类或元组包含的多个类中任意类的对象，考虑继承关系
<br>

- `hasattr(obj, name)` 若对象包含指定属性则返回 True
- `getattr(obj, name[, default])` 返回对象的指定属性的值，若不存在则返回 default，若 default 未传入则抛出 AttributeError
- `setattr(obj, name, value)` 设置对象的指定属性的值，该属性可以不存在


### 输入输出
- `input(prompt='')` 从标准输入读入一个字符串，会去除末尾的换行符，若用户输入 EOF 则会抛出 EOFError
- `print(*objects, sep=' ', end='\n', file=None, flush=False)`
    - `file` 输出的文件对象，默认为 sys.stdout
    - `flush` 若为 True，则会立即刷新输出缓冲区











<br>

## 内建类型
### 数字
- bool 是 int 的子类
- 虚部末尾需要加上 j 或 J，可使用 z.real 和 z.imag 分别获得实部和虚部

**整数方法**
- `int(x=0)` `int(x, base=10)` 将字符串转换为整数，或者将数字向零取整
<br>

- `bit_count()` 返回二进制形式中 1 的个数
- `bit_length()` 返回二进制形式的长度，不考虑符号
- `to_bytes(length=1, byteorder='big', *, signed=False)` 返回一个表示该整数的 bytes
    - `length` 字节序列的长度，若不足会抛出 OverflowError
    - `byteorder` 若为 `'big'`，则为大端模式，低地址存放高字节；若为 `'little'`，则为小端模式，低地址存放低字节
    - `signed` 若为 True，则会使用补码，否则传入负数会抛出 OverflowError
- `from_bytes(bytes, byteorder='big', *, signed=False)` 返回 bytes 表示的整数

**浮点数方法**
- `float(x=0.0)` 将字符串或数字转换为浮点数
- `is_integer()` 判断浮点数是否为整数
- `hex()` 将浮点数转换为十六进制字符串，字符串开头为 0x，末尾为 p 型指数
- `fromhex(string)` 返回十六进制字符串表示的浮点数，可以不包含 0x 和指数部分

**复数方法**
- `complex(real=0, imag=0)` `complex(string)` 将字符串或两个数字转换为复数
- `conjugate()` 返回复数的共轭




<br>

### 列表和元组
- 列表、元组、字符串等序列都支持 `+` (concatenation) 和 `*` (repetition) 操作符，可实现浅复制
- 列表、元组、字符串等序列都支持 `in` 和 `not in` 操作符，字符串、bytes 和 bytearray 还额外支持子序列包含检查
- 列表是 mutable 序列类型，不可使用 hash() 函数
- 列表切片是浅复制
- 列表可通过给切片赋值 iterable，来插入、删除、修改批量元素，如：
```py
>>> a = [1, 2, 3, 4, 5]
>>> a[4:] = [6]
>>> a
[1, 2, 3, 4, 6]
>>> a[4:4] = [7, 8]
>>> a
[1, 2, 3, 4, 7, 8, 6]
>>> a[2:6] = []
>>> a
[1, 2, 6]
```

**列表方法**
- `index(value, start=0, stop=9223372036854775807)` 返回值的第一个索引，若不存在则抛出 ValueError
- `count(value)` 返回值的出现次数
<br>

- `append(object)` 将一个元素附加到列表的末尾
- `insert(index, object)` 在 index 之前插入元素，超出的索引会被截断
- `extend(iterable)` 将 iterable 中的元素附加到列表末尾
<br>

- `pop(index=-1)` 删除并返回索引处的值，若列表为空或索引超出范围则会抛出 IndexError
- `remove(value)` 删除第一个出现的值，若不存在则抛出 ValueError
- `clear()` 删除列表所有的元素
- `copy()` 返回列表的浅复制
<br>

- `sort(*, key=None, reverse=False)` 升序排序列表，返回 None
    - 稳定排序，即值相同的两个元素的相对位置不变
- `reverse()` 原地反转，返回 None

**元组方法**
- `index(value, start=0, stop=9223372036854775807)` 返回值的第一个索引，若不存在则抛出 ValueError
- `count(value)` 返回值的出现次数



<br>

### 范围和切片
- `range(stop)`
- `range(start, stop, step=1)`
- range 是 immutable 序列类型，表示相同序列的 range 相同
<br>

- `slice(stop)`
- `slice(start, stop, step=1)`
- 切片会创造一个浅复制，即只会构建一个包含原有元素索引的复合对象





<br>

### 字符串
- 三个引号包裹的字符串允许使用单引号和双引号，还允许换行
- r 或 R 开头的字符串被称为生字符串，内部的反斜杠会被当成文本

#### 查找和删除
- `index(sub[, start[, end]])` 返回子字符串的第一个索引，若不存在则抛出 ValueError
- `rindex(sub[, start[, end]])` 返回子字符串的最后一个索引，若不存在则抛出 ValueError
- `find(sub[, start[, end]])` 返回子字符串的第一个索引，若不存在则返回 -1
- `rfind(sub[, start[, end]])` 返回子字符串的最后一个索引，若不存在则返回 -1
- `count(sub[, start[, end]])` 返回子字符串的出现次数，每个子字符串不能重叠
<br>

- `strip(chars=None)` 返回副本，其开头和末尾的指定字符被移除，默认为空白字符
- `lstrip(chars=None)` 返回副本，其开头的指定字符被移除
- `rstrip(chars=None)` 返回副本，其末尾的指定字符被移除
- `removeprefix(prefix)` 返回副本，若开头为 prefix 则删除开头 prefix
- `removesuffix(suffix)` 返回副本，若末尾为 suffix 则删除末尾 suffix

<br>

#### 分割和合并
- `split(sep=None, maxsplit=-1)` 返回一个列表，存放分割后的子字符串
    - `seq` 分隔符，默认为空白字符
    - `maxsplit` 最大分割次数，返回的列表长度最大为 maxsplit + 1
- `rsplit(sep=None, maxsplit=-1)` 从末尾开始分割
- `splitlines(keepends=False)` 返回一个用换行符分割的字符串列表，默认不保留末尾的换行符
<br>

- `partition(sep)` 若找到分隔符，则返回 (前, 分隔符, 后)，否则返回 (源字符串, '', '')
- `rpartition(sep)` 从右边开始查找分隔符
<br>

- `join(iterable)` 以 self 为分隔符，将多个字符串连接起来

<br>

#### 转换
- `capitalize()` 将第一个字母变为大写，其余变为小写
- `title()` 将每个单词的第一个字母变为大写，其余变为小写
- `lower()` 将所有字母变为小写
- `upper()` 将所有字母变为大写
- `swapcase()` 将所有字母转换大小写
- `casefold()` 将所有字母变为小写，但适用于更多语言
<br>

- `center(width, fillchar=' ')` 将字符串原有内容居中，若 width 大于字符串长度则会用 fillchar 填充
- `ljust(width, fillchar=' ')` 将字符串原有内容左对齐
- `rjust(width, fillchar=' ')` 将字符串原有内容右对齐
- `zfill(width)` 将字符串原有内容右对齐，若 width 大于字符串长度则会用零填充
<br>

- `replace(old, new, count=-1)` 替换 old 为 new，最多替换 count 次
- `expandtabs(tabsize=8)` 将所有制表符转换为空格
- `encode(encoding='utf-8', errors='strict')` 将字符串编码为 bytes 对象
    - `error` 若为 `'ignore'` 则会忽略 UnicodeEncodeError

<br>

#### 判断
- `startswith(prefix[, start[, end]])` 若字符串开头为指定 prefix，则返回 True
- `endswith(suffix[, start[, end]])` 若字符串末尾为指定 suffix，则返回 True
    - `prefix` 可为一个字符串或由字符串组成元组
    - `start` 开始检查的索引位置
    - `end` 结束检查的索引位置
<br>

- `isalnum()` 若不为空字符串且所有字符均为字母数字，则返回 True
- `isalpha()` 若不为空字符串且所有字符均为字母，则返回 True
- `isdecimal()` 若不为空字符串且所有字符均为数字，则返回 True，包括 Unicode 数字和双字节全角数字
- `isdigit()` 若不为空字符串且所有字符均为数字，则返回 True，包括 Unicode 数字、单字节数字和双字节全角数字
- `isnumeric()` 若不为空字符串且所有字符均为数字，则返回 True，包括 Unicode 数字、双字节全角数字、罗马数字和汉字数字
- `isspace()` 若不为空字符串且所有字符均为空白字符，则返回 True
<br>

- `islower()` 若不为空字符串且所有字母均小写，则返回 True
- `isupper()` 若不为空字符串且所有字母均大写，则返回 True
- `istitle()` 若不为空字符串且所有单词均只有开头大写，则返回 True
<br>

- `isascii()` 若所有字符均为 ASCII 字符，则返回 True，包括空字符串
- `isprintable()` 若所有字符均为可打印，则返回 True，包括空字符串
- `isidentifier()` 若为 Python 标识符，则返回 True，包括合法的变量名和保留的关键字

<br>

#### 格式化
**格式化运算符**
运算符 `%` 可用于格式化字符串，其前面为字符串，后面为元组，元组长度对应于字符串中的转换说明符
转换说明符的基本格式为 `%[flags][width][.precision][length]type`，以下为几个示例：
- `"%+05d" % (1)` 的结果为 `"+0001"`
- `"%-5d" % (1)` 的结果为 `"1    "`
- `"%#06x" % (1)` 的结果为 `"0x0001"`
- `"%5.2f" % (1.1)` 的结果为 `" 1.10"`
- `"%*.*f" % (5, 2, 1.1)` 的结果为 `" 1.10"`

<br>

**format 方法**
字符串自带的 format() 方法也可用于格式化，以下为几个示例：
- `"{} are {} years old".format(name, age)`
- `"{0} are {1} years old".format(name, age)`
- `"{name} are {year} years old".format(name=name, age=age)`
- `"{person.name} are {person.year} years old".format(person=person)`

替换域中也可以在 `:` 后面使用格式说明符，其基本格式为：
```C
format_spec     ::=  [[fill]align][sign][z][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

- align
    - `<` 左对齐
    - `>` 右对齐
    - `=` 将填充字符放在符号之后
    - `^` 居中对齐
- sign
    - `+` 正负数都应有符号
    - `-` 只有负数有符号，默认
    - ` ` 正数使用空格作符号，负数使用减号作符号
- z, #, 0
    - `z` 在浮点数四舍五入后，强制负的零变为正的零
    - `#` 使用另一种替代形式，整数会加上前缀，浮点数会保留小数点
    - `0` 会填充零并注意符号位置，相当于 `0=`
- grouping_option
    - `,` 使用逗号作为整数或浮点数的千位分隔符
    - `_` 使用下划线作为整数或浮点数的千位分隔符，若整数不是十进制，则每四位用下划线分隔一次
- type
    - `n` 和 `d` 或 `g` 相同，除了在插入分隔符时会使用所在地区的设置
    - `%` 和 `f` 相同，但会乘以一百并加上百分号
<br>

- `"{:^5}".format(1)` 的结果为 `"  1  "`
- `"{:#^5}".format(1)` 的结果为 `"##1##"`
- `"{:,}".format(1234567)` 的结果为 `"1,234,567"`
- `"{:.2%}".format(0.2)` 的结果为 `"20.00%"`

<br>

**格式字符串字面量**
- f 或 F 开头的字符串被称为格式字符串字面量，也被称为 f-string
- f-string 中的 `{}` 内可直接使用表达式，可在表达式后加上 `:` 再加上格式说明符
- 可在表达式后使用 `=` 来得到赋值语句，空白会被保留，如 `f"{ a = :.2f} "` 的结果为 `" a = 1.00 "`




<br>

### 字节序列
**构造函数**
- `bytes(iterable_of_ints)` 返回由可迭代对象决定的 bytes 对象，可迭代对象中的整数应小于 256
- `bytes(string, encoding[, errors])` 返回编码后的 bytes 对象
- `bytes(bytes_or_buffer)` 返回 bytes 或 buffer 对象的**不可变**副本
- `bytes(int)` 返回指定长度的由 null 初始化的 bytes 对象
- `bytes()` 返回空 bytes 对象
<br>

- `bytearray(iterable_of_ints)` 返回由可迭代对象决定的 bytearray 对象，可迭代对象中的整数应小于 256
- `bytearray(string, encoding[, errors])` 返回编码后的 bytearray 对象
- `bytearray(bytes_or_buffer)` 返回 bytes 或 buffer 对象的**可变**副本
- `bytearray(int)` 返回指定长度的由 null 初始化的 bytearray 对象
- `bytearray()` 返回空 bytearray 对象

**方法**
- bytes 对象有着字符串的大多数方法，bytearray 对象有着字符串和列表的大多数方法
- `fromhex(string)` 将字符串转换为对应的字节序列，不可带有前缀 0x，每个字节必须由两个字符组成，其间可以有空白字符
- `hex([sep[, bytes_per_sep]])` 将字节序列转换为对应的十六进制字符串
    - `sep` 分隔符，必须为单个字符或单个字节，默认为无
    - `bytes_per_sep` 分隔符的间隔的字节数，若为正数则从右开始分隔，若为负数则从左开始分隔
- `decode(encoding='utf-8', errors='strict')` 将字节序列解码为字符串
    - `error` 若为 `'ignore'` 则会忽略 UnicodeDecodeError




<br>

### 集合
- 集合内的元素是无序且可哈希的，必须各不相同
- set 和 frozenset 都是集合类型，其中 set 是可变的，不可哈希，frozenset 是不可变的，可哈希
- set 可以使用花括号创建，不过花括号内必须有元素，否则会被当作 dict

**set 方法**
- `add(elem)` 添加元素
- `remove(elem)` 删除元素，若不存在会抛出 KeyError
- `discard(elem)` 删除元素，若不存在不会报错
- `pop()` 弹出任意一个元素，若 set 为空则抛出 KeyError
- `clear()` 删除所有元素
<br>

- `update(*others)` 更新为多个集合的并集
    - 等效于 `set |= other | ...`
- `intersection_update(*others)` `set &= other & ...` 更新为多个集合的交集
    - 等效于 `set &= other & ...`
- `difference_update(*others)` `set -= other | ...` 更新为多个集合的差集
    - 等效于 `set -= other | ...`
- `symmetric_difference_update(other)` `set ^= other` 更新为多个集合的异或
    - 等效于 `set ^= other`

**集合方法**
- `isdisjoint(other)` 若交集为空则返回 True
- `issubset(other)` 若为 other 的子集则返回 True
    - 等效于 `set <= other` 和 `set < other and set != other`
- `issuperset(other)` 若为 other 的超集则返回 True
    - 等效于 `set >= other` 和 `set > other and set != other`
<br>

- `union(*others)` 取多个集合的并集
    - 等效于 `set | other | ...`
- `intersection(*others)` 取多个集合的交集
    - 等效于 `set & other & ...`
- `difference(*others)` 取多个集合的差集
    - 等效于 `set - other - ...`
- `symmetric_difference(other)` 取多个集合的异或
    - 等效于 `set ^ other`





<br>

### 字典
- `list(dict)`, `set(dict)` 和 `iter(dict)` 只能获得字典的键
- 字典可以使用操作符 `|`，当键相同时，后面的字典优先级更高

**字典方法**
- `keys()` 返回字典的键的视图
- `values()` 返回字典的值的视图
- `items()` 返回字典的键值对的视图
<br>

- `clear()` 删除所有键值对
- `copy()` 返回字典的浅复制
<br>

- `fromkeys(iterable, value=None)` 返回一个所有值均为 value 的字典
- `get(key, default=None)` 返回指定键的值，若不存在则返回 default
- `pop(key, default=None)` 弹出指定键的值，若不存在则返回 default
- `popitem()` 弹出一个键值对，顺序为 LIFO，若字典为空则抛出 KeyError




<br>

### 文件
```py
open(
    file,
    mode='r',
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
)
```
- `mode` 指定打开模式，各个字符之间的顺序不重要
    - `r` 只读模式，不可写，若文件不存在会抛出 FileNotFoundError
    - `w` 写入模式，不可读，若文件不存在会新建文件，若文件已存在会清空原有文件
    - `a` 追加模式，不可读，若文件不存在会新建文件，若文件已存在会移至文件末尾
    - `x` 创建模式，不可读，若文件已存在会抛出 FileExistsError
    - `+` 读写模式，与上述模式一起使用
    - `t` 文本模式，与上述模式一起使用，默认
    - `b` 二进制模式，与上述模式一起使用
- `errors` 指定在编解码错误时的处理方式
    - `strict` 默认，会抛出错误，中断程序执行
    - `ignore` 会忽略错误字符
    - `replace` 会替换为 Unicode 替换字符 U+FFFD
    - `xmlcharrefreplace` 会替换为相应的 XML 字符引用
    - `backslashreplace` 会替换为 Python 字符串转义序列
- `newline` 指定换行符的处理方式
    - `None` 默认，在读取和写入时使用当前操作系统的格式
    - `""` 禁用换行转换，保持原有格式
    - `"\n"` 在读取和写入时使用 \\n
    - `"\r\n"` 在读取和写入时使用 \\r\\n

<br>

**文件方法**
- `read(size=-1)` 读取文件，最多读取 size 个字符，默认为读取全部
- `readline(size=-1)` 读取整行，包括末尾的换行符，最多读取 size 个字符
- `readlines(size=-1)` 读取所有行并返回一个列表，最多读取 size 个字符
<br>

- `write(text)` 将文本写入文件，返回写入的字符数
- `writelines(lines)` 将列表里的文本写入文件，不会自动加上换行符
- `flush()` 刷新文件缓冲区，强制将数据写入文件
<br>

- `tell()` 返回文件当前的位置
- `seek(offset, whence=0)` 移动到指定位置
    - `whence` 若为 0，则从文件开头开始偏移；若为 1，则从当前位置开始偏移；若为 2，则从文件末尾开始偏移

<br>

**文件属性**
- `file.name` 文件的名称，可能包括路径
- `file.mode` 文件的打开方式
- `file.closed` 文件是否已被关闭
- `file.encoding` 文件的编码方式，仅用于文本模式
- `file.newline` 文件读取时遇到的换行符列表，仅用于文本模式
- `file.errors` 文件遇到编解码错误时的处理方式，仅用于文本模式
- `file.buffer` 文件的缓冲区对象，仅用于文本模式













<br>

## 命令行选项
```powershell
python [-bBdEhiIOqsSuvVWx?] [-c cmd | -m mod | file | - ] [args]
```
- `-c cmd` 在命令行中直接运行提供的代码
- `-m mod` 将 Python 模块作为脚本运行
- `-` 从标准输入读取代码执行
<br>

- `-b` 在解释脚本之前，将脚本编译成字节码文件，提高脚本的执行速度
- `-B` 禁用字节码生成，不会生成 .pyc 文件
- `-i` 运行脚本后进入交互模式
- `-O` 以优化模式运行脚本
- `-V` 显示 Python 解释器的版本信息

<br>

常用命令行打开的一个模块是 pydoc，其使用如下：
```powershell
 python -m pydoc -b
```
- `-b` 在任意未被使用的端口上打开 HTTP 服务器，并自动打开浏览器
- `-p <port>` 在指定端口打开 HTTP 服务器









<br>

## Expressions

### Atoms
```C
atom      ::=  identifier | literal | enclosure
enclosure ::=  parenth_form | list_display | dict_display | set_display
               | generator_expression | yield_atom

parenth_form ::=  "(" [starred_expression] ")"

list_display ::=  "[" [starred_list | comprehension] "]"
set_display ::=  "{" (starred_list | comprehension) "}"
dict_display       ::=  "{" [key_datum_list | dict_comprehension] "}"
key_datum_list     ::=  key_datum ("," key_datum)* [","]
key_datum          ::=  expression ":" expression | "**" or_expr
dict_comprehension ::=  expression ":" expression comp_for
```
- Atoms are the most basic elements of expressions. The simplest atoms are identifiers or literals. Forms enclosed in parentheses, brackets or braces are also categorized syntactically as atoms.
- A parenthesized form is an optional expression list enclosed in parentheses.
    - An empty pair of parentheses yields an empty tuple object.
    - A parenthesized expression list yields whatever that expression list yields: if the list contains at least one comma, it yields a tuple; otherwise, it yields the single expression that makes up the expression list.
- A list display is a possibly empty series of expressions enclosed in square brackets.
- A set display is denoted by curly braces and distinguishable from dictionary displays by the lack of colons separating keys and values.
- A dictionary display is a possibly empty series of key/datum pairs enclosed in curly braces.
    - A double asterisk `**` denotes dictionary unpacking. Its operand must be a mapping. Each mapping item is added to the new dictionary..
    - An empty pair of braces `{}` constructs an empty dictionary, not a set.


#### Comprehensions and Generator expressions
```C
comprehension ::=  assignment_expression comp_for
comp_for      ::=  ["async"] "for" target_list "in" or_test [comp_iter]
comp_iter     ::=  comp_for | comp_if
comp_if       ::=  "if" or_test [comp_iter]

generator_expression ::=  "(" expression comp_for ")"
```
- The comprehension consists of a single expression followed by at least one `for` clause and zero or more `for` or `if` clauses.
- In this case, the elements of the new container are those that would be produced by considering each of the `for` or `if` clauses a block, nesting from left to right, and evaluating the expression to produce an element each time the innermost block is reached.
- The iterable expression in the leftmost `for` clause is evaluated directly in the enclosing scope and then passed as an argument to the implicitly nested scope. Subsequent `for` clauses and any filter condition in the leftmost `for` clause cannot be evaluated in the enclosing scope as they may depend on the values obtained from the leftmost iterable.
<br>

- A generator expression is a compact generator notation in parentheses, which will yield a new generator object. Its syntax is the same as for comprehensions, except that it is enclosed in parentheses instead of brackets or curly braces.
- Variables used in the generator expression are evaluated lazily when the `__next__()` method is called for the generator object. However, the iterable expression in the leftmost `for` clause is immediately evaluated.
- The parentheses can be omitted on calls with only one argument.

#### Yields expressions and Generator functions
```C
yield_atom       ::=  "(" yield_expression ")"
yield_expression ::=  "yield" [expression_list | "from" expression]
```
- The yield expression is used when defining a generator function or an asynchronous generator function and thus can only be used in the body of a function definition. Using a yield expression in a function’s body causes that function to be a generator function, and using it in an `async def` function’s body causes that coroutine function to be an asynchronous generator function.
- Due to their side effects on the containing scope, yield expressions are not permitted as part of the implicitly defined scopes used to implement comprehensions and generator expressions.
- When a generator function is called, it returns an iterator known as a generator. That generator then controls the execution of the generator function.
- Every time one of the generator’s methods is called, the execution proceeds to the next yield expression, and then it is suspended, returning the value of `expression_list` to the generator’s caller, or None if `expression_list` is omitted.
- When `yield from <expr>` is used, the supplied expression must be an iterable, and the items in the iterable is returned one by one once one of the generator’s methods is called. When the underlying iterator is complete, the `value` attribute of the raised `StopIteration` instance becomes the value of the yield expression.
- The parentheses may be omitted when the yield expression is the sole expression on the right hand side of an assignment statement.

**Generator-iterator methods**
- `generator.__next__()` Starts the execution of a generator function or resume it at the last executed yield expression.
    - When a generator function is resumed with a `__next__()` method, the current yield expression always evaluates to None.
    - The execution then continues to the next yield expression, where the generator is suspended again, and the value of the `expression_list` is returned to `__next__()`’s caller.
    - If the generator exits without yielding another value, a `StopIteration` exception is raised.
    - This method is normally called implicitly, e.g. by a `for` loop, or by the built-in `next()` function.
- `generator.send(value)` Resume the execution and “sends” a value into the generator function. The value argument becomes the result of the current yield expression.
    - The `send()` method returns the next value yielded by the generator, or raises `StopIteration` if the generator exits without yielding another value.
    - When `send()` is called to start the generator, it must be called with None as the argument, because there is no yield expression that could receive the value.
- `generator.throw(value)` or `generator.throw(type[, value[, traceback]])` Raise an exception at the point where the generator was paused, and returns the next value yielded by the generator function.
- `generator.close()` Raise a `GeneratorExit` at the point where the generator function was paused.


### Primaries
```C
primary ::=  atom | attributeref | subscription | slicing | call

attributeref ::=  primary "." identifier
subscription ::=  primary "[" expression_list "]"

slicing      ::=  primary "[" slice_list "]"
slice_list   ::=  slice_item ("," slice_item)* [","]
slice_item   ::=  expression | proper_slice
proper_slice ::=  [lower_bound] ":" [upper_bound] [ ":" [stride] ]
lower_bound  ::=  expression
upper_bound  ::=  expression
stride       ::=  expression
```
- Primaries represent the most tightly bound operations of the language.
- An **attribute reference** is a primary followed by a period and a name. If this attribute is not available, the exception `AttributeError` is raised.
- The **subscription** of an instance of a container class will generally select an element from the container. The subscription of a generic class will generally return a GenericAlias object.
    -  An object may support subscription through defining one or both of `__getitem__()` and `__class_getitem__()`. When the primary is subscripted, the evaluated result of the expression list will be passed to one of these methods.
    -  For built-in objects, there are two types of objects that support subscription via `__getitem__()`: Mappings, the `expression list` must evaluate to an object whose value is one of the keys of the mapping; Sequences, the `expression list` must evaluate to **an int or a slice**.
- A **slicing** selects a range of items in a sequence object. Slicings may be used as expressions or as targets in assignment or `del` statements.
    - There is ambiguity in the formal syntax here: anything that looks like an expression list also looks like a slice list, so any subscription can be interpreted as a slicing. Rather than further complicating the syntax, this is disambiguated by defining that in this case the interpretation as a subscription takes priority over the interpretation as a slicing (this is the case if the slice list contains no proper slice).

**Calls**
```C
call                 ::=  primary "(" [argument_list [","] | comprehension] ")"
argument_list        ::=  positional_arguments ["," starred_and_keywords]
                            ["," keywords_arguments]
                          | starred_and_keywords ["," keywords_arguments]
                          | keywords_arguments
positional_arguments ::=  positional_item ("," positional_item)*
positional_item      ::=  assignment_expression | "*" expression
starred_and_keywords ::=  ("*" expression | keyword_item)
                          ("," "*" expression | "," keyword_item)*
keywords_arguments   ::=  (keyword_item | "**" expression)
                          ("," keyword_item | "," "**" expression)*
keyword_item         ::=  identifier "=" expression
```
- A call calls a callable object (e.g., a function) with a possibly empty series of arguments.
- An optional trailing comma may be present after the positional and keyword arguments but does not affect the semantics.
- All argument expressions are evaluated before the call is attempted.
- If positional argument follows keyword argument, a `SyntaxError` is raised.
- If keyword arguments are present, they are first converted to positional arguments, as follows.
    - First, a list of unfilled slots is created for the formal parameters. If there are N positional arguments, they are placed in the first N slots.
    - Next, for each keyword argument, the identifier is used to determine the corresponding slot. If the slot is already filled, a `TypeError` exception is raised.
    - When all arguments have been processed, the slots that are still unfilled are filled with the corresponding default value from the function definition. If there are any unfilled slots for which no default value is specified, a `TypeError` exception is raised.
    - Otherwise, the list of filled slots is used as the argument list for the call.
<br>

- If there are more positional arguments than there are formal parameter slots, a `TypeError` exception is raised, unless a formal parameter using the syntax `*identifier` is present; in this case, that formal parameter receives a tuple containing the excess positional arguments (or an empty tuple if there were no excess positional arguments).
    - The arguments after `*` argument is keyword-only.
- If any keyword argument does not correspond to a formal parameter name, a `TypeError` exception is raised, unless a formal parameter using the syntax `**identifier` is present; in this case, that formal parameter receives a dictionary containing the excess keyword arguments, or a empty dictionary if there were no excess keyword arguments.
<br>

- If the syntax `*expression` appears in the function call, `expression` must evaluate to an iterable. Elements from these iterables are treated as if they were additional positional arguments.
    - Although the `*expression` syntax may appear after explicit keyword arguments, it is processed before the keyword arguments, so `f(b=1, *(2,))` is similar to `f(2, b=1)`.
- When `**expression` is used, each key in this mapping must be a string. Each value from the mapping is assigned to the first formal parameter whose name is equal to the key. If there is no match to a formal parameter, the key-value pair is collected by the `**` parameter if there is one, otherwise a `TypeError` exception is raised.
- Formal parameters using the syntax `*identifier` or `**identifier` cannot be used as positional argument slots or as keyword argument names.


### Operators
**Operator Precedence**
| Description | Operator |
| --- | --- |
| Binding or parenthesized expression, list display, dictionary display, set display | `(expressions...)`, `[expressions...]`, `{key: value...}`, `{expressions...}` |
| Subscription, slicing, call, attribute reference | `x[index]`, `x[index:index]`, `x(arguments...)`, `x.attribute` |
| Await expression | `await x` |
| Exponentiation | `**` |
| Positive, negative, bitwise NOT | `+x`, `-x`, `~x` |
| Multiplication, matrix multiplication, division, floor division, remainder | `*`, `@`, `/`, `//`, `%` |
| Addition and subtraction | `+`, `-` |
| Shifts | `<<`, `>>` |
| Bitwise AND | `&` |
| Bitwise XOR | `^` |
| Bitwise OR | `|` |
| Comparisons, including membership tests and identity tests | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` |
| Boolean NOT | `not x` |
| Boolean AND | `and` |
| Boolean OR | `or` |
| Conditional expression | `if – else` |
| Lambda expression | `lambda` |
| Assignment expression | `:=` |

**Arithmetic Operations**
- The power operator `**` binds more tightly than unary operators on its left; it binds less tightly than unary operators on its right, i.e. `1**-2` is `1.0`, `-1**2` is `-1`.
    - For int operands, the result has the same type as the operands unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered.
    - Raising a negative number to a fractional power results in a complex number.
    - Raising `0` or `0.0` to a negative power results in a `ZeroDivisionError`, but to a positive power results in `0` or `0.0`, while to zero power results in `1` or `1.0`.
- The unary invert operator `~` only applies to integral numbers or to custom objects that override the `__invert__()` special method.
- Bitwise operations only make sense for integers. The result of bitwise operations is calculated as though carried out in two’s complement with an infinite number of sign bits.
- The `*` (multiplication) operator's arguments must either both be numbers, or one argument must be an integer and the other must be a sequence.
    - In the former case, the numbers are converted to a common type and then multiplied together.
    - In the latter case, sequence repetition is performed; a zero or negative repetition factor yields an empty sequence.
- The `//` (floor division) operator's result is always rounded towards minus infinity, e.g. `1//2` equals `0`, `-1//2` equals `-1`, `1//-2` equals `-1`, `-1//-2` equals `0`
- The `%` (modulo) operator's arguments may be floating point numbers, e.g., `3.14%0.7` equals `0.34`.
    - The modulo operator always yields a result with the same sign as its second operand, e.g. `1.4%-0.7` equals `-0.0`
    - The absolute value of the result is strictly smaller than the absolute value of the second operand

**Conparisons**
```py
<, <=, >, >=
==, !=
is, is not
in, not in
```
- Objects of different types, except different numeric types, never compare equal, e.g. `1 == 1.0 and 1 == complex(1)` is True, but `1 == '1'` is False.
- Comparisons can be chained arbitrarily, e.g., `x < y <= z` is equivalent to `x < y and y <= z`. Formally, `a op1 b op2 c ... y opN z` is equivalent to `a op1 b and b op2 c and ... y opN z`, except that each expression is evaluated at most once.
- The operators `is` and `is not` test for an object’s identity. `x is y` is true if and only if x and y are the same object. An Object’s identity is determined using the `id()` function. They cannot be customized.
- The operators `in` and `not in` test for membership. `x in s` evaluates to True if x is a member of s, and False otherwise. All built-in sequences and set types support this as well as dictionary, for which in tests whether the dictionary has a given key. They are supported by types that are iterable or implement the `__contains__()` method.
- The operators `is` and `is not` test for an object’s identity: `x is y` is true if and only if x and y are the same object. An Object’s identity is determined using the `id()` function. x is not y yields the inverse truth value.

### Assignment, Conditional and Lambda Expressions
```py
assignment_expression ::=  [identifier ":="] expression

conditional_expression ::=  or_test ["if" or_test "else" expression]
expression             ::=  conditional_expression | lambda_expr

lambda_expr ::=  "lambda" [parameter_list] ":" expression
def <lambda>(parameter_list):
    return expression
```
- An assignment expression (`:=`) assigns an expression to an identifier, while also returning the value of the expression.
- The expression `x if C else y` first evaluates the condition `C`. If `C` is true, `x` is evaluated and its value is returned; otherwise, `y` is evaluated and its value is returned.
- Lambda expressions are used to create anonymous functions. The expression `lambda parameters: expression` yields a function object. Note that functions created with lambda expressions cannot contain statements or annotations.









## Statements
### Function definitions
```C
funcdef                   ::=  [decorators] "def" funcname "(" [parameter_list] ")"
                               ["->" expression] ":" suite
decorators                ::=  decorator+
decorator                 ::=  "@" assignment_expression NEWLINE
parameter_list            ::=  defparameter ("," defparameter)* "," "/" ["," [parameter_list_no_posonly]]
                                 | parameter_list_no_posonly
parameter_list_no_posonly ::=  defparameter ("," defparameter)* ["," [parameter_list_starargs]]
                               | parameter_list_starargs
parameter_list_starargs   ::=  "*" [parameter] ("," defparameter)* ["," ["**" parameter [","]]]
                               | "**" parameter [","]
parameter                 ::=  identifier [":" expression]
defparameter              ::=  parameter ["=" expression]
funcname                  ::=  identifier
```
- A function definition defines a user-defined function object.
- A function definition is an executable statement. Its execution binds the function name in the current local namespace to a function object.
- If a parameter has a default value, all following parameters up until the `*` must also have a default value. This is a syntactic restriction that is not expressed by the grammar.
- Default parameter values are evaluated from left to right when the function definition is executed. This means that the expression is evaluated once, when the function is defined, and that the same "pre-computed" value is used for each call.
<br>

- A function call always assigns values to all parameters mentioned in the parameter list, either from positional arguments, from keyword arguments, or from default values.
- If the form `*identifier` is present, it is initialized to a tuple receiving any excess positional arguments.
- If the form `**identifier` is present, it is initialized to a new ordered mapping receiving any excess keyword arguments.
- Parameters after `*` or `*identifier` are keyword-only parameters and may only be passed by keyword arguments.
- Parameters before `/` are positional-only parameters and may only be passed by positional arguments.
<br>

- Parameters may have an annotation of the form `: expression` following the parameter name. Any parameter may have an annotation, even those of the form `*identifier` or `**identifier`.
- Functions may have "return" annotation of the form `-> expression` after the parameter list.
- These annotations can be any valid Python expression.
- The presence of annotations does not change the semantics of a function.
- The annotation values are available as values of a dictionary keyed by the parameters’ names in the `__annotations__` attribute of the function object.


#### Decorator
- A function definition may be wrapped by one or more decorator expressions.
- Decorator expressions are evaluated when the function is defined, in the scope that contains the function definition.
- The result must be a callable, which is invoked with the function object as the only argument.
- The returned value is bound to the function name instead of the function object.
- Even if the parametrized decorator has default values for its arguments, the parentheses after its name is required to call the out wapper.

**Builtin decorators**
- `@classmethod` Transform a method into a class method.
    - A class method receives the class as an implicit first argument, just like an instance method receives the instance.
    - A class method can be called either on the class or on an instance. The instance is ignored except for its class.
    - If a class method is called for a derived class, the derived class object is passed as the implied first argument.
- `@staticmethod` Transform a method into a static method.
    - A static method does not receive an implicit first argument.
    - A static method can be called either on the class or on an instance. Moreover, they can be called as regular functions.

**Examples**
```py
from functools import wraps

def mydecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs): 
        # do some stuff before the original function gets called
        result = func(*args, **kwargs)
        # do some stuff after function call and return the result
        return result
    # return wrapper as a decorated function
    return wrapper

def mydecorator(parameters):
    def outwrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs): 
            # do some stuff with the parameters
            result = func(*args, **kwargs)
            # do some stuff with the parameters
            return result
        # return wrapper as a decorated function
        return wrapper
    return outwrapper

class DecoratorAsClass:
    # return an instance of the class as a decorated function
    def __init__(self, func):
        self.func = func
    
    @wraps(func)
    def __call__(self, *args, **kwargs):
        # do some stuff before the original function gets called
        result = self.func(*args, **kwargs)
        # do some stuff after function call and return the result
        return result
```



