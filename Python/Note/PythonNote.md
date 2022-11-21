[toc]


---
## Python3 基础语法

- 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串
标识符
- 标识符的组成为字母、数字、下划线，开头只能为字母、下划线，在Python3中可以用中文做变量名。
- Python允许同时为多个变量赋值，如a = b = c = 1或者a, b, c = 1, 2, "runoob"
- 可使用del语句删除对象引用，如del a,b或者del b[1]

#### 保留字
保留字即关键字，Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

#### 注释
单行注释用#号开头，多行注释可用多个#号，还有’’’和”””

#### 多行语句
可以用 \ 实现多行语句，已用 []、{}、() 则不需要用 \


---
## Python3 基本数据类型

#### Number（数字）

- Python支持int , bool , float , complex(可表示为a+bj或者complex(a,b)）
- Python3 中，bool 是 int 的子类```issubclass(bool, int) ==> True```
  - ```True == 1，False == 0 ``` 会返回 True，但可以通过 is 来判断类型（1 is True ==> False）

- 二进制整数使用前缀0b，十六进制使用前缀0x
- / 返回一个浮点数，// 表示整除，返回一个整数，% 表示取余，** 表示乘方

#### String（字符串）

###### 字符串长度
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串
字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始

###### 转义符
- 结尾的 \ 可表示换行
- 可表示转义命令: 
  \n 表示换行，\t 表示tab，\r 表示回车，\000 表示空格，\oXX 表示接受八进制命令（如\o12表示换行）、\xXX表示接受十六进制命令（如\x0a表示换行）
- 在字符串最后加 \ 只能用+的方法，即 + ’ \\ ’

###### 转义符的打印
- 字符串只有一个 \ 时，若 \ 后不是合法的转义字符，则会在shell中会出现两个 \\（字符数目不会变多）
- 字符串中有多个 \ 时，则shell中 \ 的数目保持原样
- shell中会直接显示转义字符，如字符串中有 ' 或换行时，在shell中会以 \\' or \n 显示

###### raw字符串
- 若 r'...' 与普通字符串相连，则后者仍会转义
- 可以用 r'''...''' 表示raw多行字符串

###### 多行字符串
- 可用 '''...''' 表示多行字符串，除非字符串内只有单引号，否则在shell中两端会出现’（即使用”...”或”””...”””）
- 多行字符串中每一次换行都会被记录，在在shell中会显示 \n

###### 字符串截取
- str[-1] 表示输出最后一个字符
- str[0:-1] 表示输出第一个到倒数第二个所有字符
- str[1:1] 表示输出空字符串
- str[1:] 表示输出第二个到最后一个所有字符
- str[:] 表示输出所有字符
- str[1:5:3] 表示从第二个到第五个每隔两步截取一个字符（先截取步长数或不足步长数的一段取第一个字符，之后若有剩余字符则不断重复）

###### 格式字符串
```python
print('%s is %d years old' % (name, age))

print('{} is {} years old'.format(name, age))
print('{0} is {1} years old'.format(name, age))
print('{n} is {a} years old'.format(n = name, a = age))

print(f'{name} is {age} years old')
```

###### 字符串方法
- `.count(sub[, start[, end]])` 若start和end超出字符串或颠倒不会报错
- `.find(sub[, start[, end]])` 切片不会改变返回的索引值，若找不到则返回-1；
- `rfind(sub[, start[, end]])` 返回最大的索引值
- `.index(sub[, start[, end]])` 切片不会改变返回的索引值，若找不到则抛出ValueError
- `.rindex(sub[, start[, end]])` 返回最大的索引值
<br>

- `.capitalize()` 第一个字母大写
- `.title()` 首字母大写
- `.upper()` 全字母大写
- `.lower()` 全字母小写
- `.swapcase()` 交换大小写
<br>

- `.lstrip(chars = None)` 删除开头全部空白或指定chars
- `.rstrip(chars = None)` 删除末尾全部空白或指定chars
- `.strip(chars = None)` 删除头尾全部空白或指定chars
<br>

- `.center(width, fillchar=' ')` 可用指定单个字符填充字符串使原内容居中，width可小于len(str)
- `.ljust(width, fillchar=' ')` 为左对齐
- `.rjust(width, fillchar=' ')` 为右对齐
- `.zfill(width)` 填充0且右对齐，width可小于len(str)
<br>

- `.join(iterable)` 若参数为字典则返回值为’key1strkey2str…’
- `.partition(sep)` 若找得到第一个分隔符则返回(前字符串, 分隔符, 后字符串)，若否则返回(字符串, ‘’, ‘’)
- `.rpartition(sep)` 从末尾开始找分隔符
- `.split(sep=None, maxsplit=-1)` 返回[sub1, sub2…]，若无分隔符则以空白字符（空格、\n、\r、\t等）为分隔符且空子字符串被丢弃，maxsplit可小于-1
- `.removeprefix(prefix)` 若以prefix开头则返回[len(prefix):]，若否则返回复制本
- `.removesuffix(suffix)` 若以suffix结尾则返回[:-len(suffix)]，若否则返回复制本
- `.replace(old, new, count=-1)` count表示替换个数，可大于str.find(old)，可小于-1
- `.startswith(suffix[, start[, end]])` `.endswith(suffix[, start[, end]])` 若参数为元组，则任一符合则返回True
- `.splitlines(keepends=False)` 若keepends为True则行末尾保留行分隔符（\n、\r等)
<br>

```python
str.isalnum()
str.isalpha()
str.isdecimal()
str.isdigit()
str.isnumeric()
str.isidentifier()
str.islower()
str.isupper()
str.istitle()
str.isspace()   #以上若符合条件且不为空字符串则返回True
str.isascii()   #若全为ASCII字符或为空字符串则返回True
```



#### List（列表）

###### 列表连接
列表表示索引方式与字符串基本一致。+ 是列表连接运算符，星号 * 是重复操作，如```print (list + tinylist) ==> ['runoob', 123]``` ```print (tinylist * 2) ==> [123, 123]```

###### 改变连续元素
与Python字符串不一样的是，列表中的元素是可以改变的，如：
```python
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

###### 列表方法
.append(object)在末尾添加一个元素，.extend(iterable)在末尾添加一个集合，.insert(index,object)在特定位置前一位插入一个元素
.pop(index=-1)在指定索引删除一个元素并返回值，.remove(value)删除出现的第一个指定元素
.count(value)统计指定元素在列表中的数量，.index(value,start=0,stop=922337......)返回出现的第一个指定元素的索引值



---
## Python3 内置函数

type(object)：返回对象的类型，type(name, bases, dict)返回新的类型对象

isinstance(obj, class_or_tuple, /)：判断一个对象是否是一个已知的类型或一个类型元组中的一个类型，会认为子类是一种父类类型，考虑继承关系

issubclass(cls, class_or_tuple, /)：判断参数class是否是类型参数的子类

range(stop)或range(start,stop[,step])

str(object)：
```python
str(‘abc’) ==> 'abc'
str([1,'a']) ==> "[1, 'a']"
str({'a': 1}) ==> "{'a': 1}"
```

chr()：ASCII码转字符
ord()：字符转ASCII码



---
## Python 文件

###### 文件路径
- …/ 表示当前文件所在的目录的上一级目录
- ./ 表示当前文件所在的目录(可以省略)
- / 表示当前站点的根目录(域名映射的硬盘目录)
```python
path1 = r"C:\windows\temp\readme.txt"
path2 = "C:\\windows\\temp\\readme.txt"
path3 = "c:/windows/temp/readme.txt" #可用正斜杠，且大小写不影响
```