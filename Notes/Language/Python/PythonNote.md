<!-- TOC -->

- [Command line and environment](#command-line-and-environment)
- [Expressions](#expressions)
    - [Arithmetic Operator](#arithmetic-operator)
    - [Conparisons](#conparisons)
- [Built-in Functions](#built-in-functions)
  - [Construct](#construct)
  - [Calculate](#calculate)
  - [Convert](#convert)
  - [Get](#get)
  - [Iterator](#iterator)
  - [Test](#test)
  - [I/O](#io)
- [Built-in Types](#built-in-types)
  - [Numeric Types (int, float, complex)](#numeric-types-int-float-complex)
  - [Iterator Types](#iterator-types)
  - [Sequence Types](#sequence-types)
- [Python3 基础语法](#python3-基础语法)
    - [保留字](#保留字)
    - [注释](#注释)
    - [多行语句](#多行语句)
- [Python3 基本数据类型](#python3-基本数据类型)
    - [Number（数字）](#number数字)
    - [String（字符串）](#string字符串)
        - [字符串长度](#字符串长度)
        - [转义符](#转义符)
        - [转义符的打印](#转义符的打印)
        - [raw字符串](#raw字符串)
        - [多行字符串](#多行字符串)
        - [字符串截取](#字符串截取)
        - [格式字符串](#格式字符串)
        - [字符串方法](#字符串方法)
    - [List（列表）](#list列表)
        - [列表连接](#列表连接)
        - [改变连续元素](#改变连续元素)
        - [列表方法](#列表方法)
- [Python3 内置函数](#python3-内置函数)
- [Python 文件](#python-文件)
        - [文件路径](#文件路径)

<!-- /TOC -->







## Command line and environment
```py
python [-bBdEhiIOqsSuvVWx?] [-c cmd | -m mod | script | - ] [args]
```
- `-b` Issue warnings when comparing `bytes` or `bytearray` with str or `bytes` with int. Issue an error when the option is given twice (`-bb`).
- `-B` Don't write `.pyc` files on the import of source modules; also `PYTHONDONTWRITEBYTECODE=x`
- `-d` Turn on parser debugging output (for experts only, only works on debug builds); also `PYTHONDEBUG=x`
- `-E` Ignore `PYTHON*` environment variables, that might be set.
- `-h` Print help message and exit (also `-?` or `--help`)
- `-i` Inspect interactively after running script; forces a prompt even if stdin does not appear to be a terminal; also PYTHONINSPECT=x
- `-I` Isolate Python from the user's environment (implies `-E` and `-s`)
- `-O` Remove assert statements and any code conditional on the value of `__debug__`; add `.opt-1` before `.pyc` extension; also `PYTHONOPTIMIZE=x`
- `-OO` Do `-O` changes and also discard docstrings; add `.opt-2` before `.pyc` extension
- `-P` Don't prepend a potentially unsafe path to sys.path
- `-q` Don't print version and copyright messages on interactive startup
- `-s` Don't add user site directory to sys.path; also `PYTHONNOUSERSITE`
- `-S` Don't imply `import site` on initialization
- `-u` Force the stdout and stderr streams to be unbuffered; this option has no effect on stdin; also `PYTHONUNBUFFERED=x`
- `-v` Verbose (trace import statements). Print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. When given twice (`-vv`), print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit; also `PYTHONVERBOSE=x` can be supplied multiple times to increase verbosity
- `-V` Print the Python version number and exit (also `--version`); when given twice, print more information about the build
- `-W arg` Warning control; arg is `action:message:category:module:lineno`; also `PYTHONWARNINGS=arg`
- `-x` Skip first line of source, allowing use of non-Unix forms of #!cmd
- `-X opt` Set implementation-specific option
- `--check-hash-based-pycs always|default|never` Control how Python invalidates hash-based `.pyc` files
- `--help-env` Print help about Python environment variables and exit
- `--help-xoptions` Print help about implementation-specific `-X` options and exit
- `--help-all` Print complete help information and exit
<br>

- `-c cmd` Program passed in as string (terminates option list)
- `-m mod` Run library module as a script (terminates option list)
- `script` program read from script file
- `-` program read from stdin (default; interactive mode if a tty)
- `arg ...` arguments passed to program in `sys.argv[1:]`






## Expressions
#### Arithmetic Operator
- For integer division `//`, the resultant value is a whole integer, though the result’s type is not necessarily int. The result is always rounded towards minus infinity and the same sign as the latter number, e.g. `1//2` is 0, `(-1)//2` is -1, `1//(-2)` is -1, and `(-1)//(-2)` is 0.
- Python defines `0 ** 0` and `pow(0, 0)` to be 1, as is common for programming languages.
- Bitwise operations only make sense for integers. The result of bitwise operations is calculated as though carried out in two’s complement with an infinite number of sign bits.


#### Conparisons
```py
< <= > >=
== !=
is  is not
in  not in
```
- Objects of different types, except different numeric types, never compare equal, e.g. `1 == 1.0 and 1 == complex(1)` is True, but `1 == '1'` is False.
- Comparisons can be chained arbitrarily, e.g., `x < y <= z` is equivalent to `x < y and y <= z`. Formally, `a op1 b op2 c ... y opN z` is equivalent to `a op1 b and b op2 c and ... y opN z`, except that each expression is evaluated at most once.
- The operators `is` and `is not` test for an object’s identity. `x is y` is true if and only if x and y are the same object. An Object’s identity is determined using the `id()` function. They cannot be customized.
- The operators `in` and `not in` test for membership. `x in s` evaluates to True if x is a member of s, and False otherwise. All built-in sequences and set types support this as well as dictionary, for which in tests whether the dictionary has a given key. They are supported by types that are iterable or implement the `__contains__()` method.








## Built-in Functions
### Construct
- `bool(x=False)` Return a Boolean value. x is converted using the standard truth testing procedure. If x is false or omitted, this returns False; otherwise, it returns True.
- `int(x=0)` or `int(x, base=10)` Return an integer object constructed from a number or string x, or return 0 if no arguments are given.
  - For floating point numbers, this truncates towards zero.
  - If base is given, then x must be a string, bytes, or bytearray instance representing an integer in radix base. Optionally, the string can be preceded by `+` or `-` (with no space in between), have leading zeros, be surrounded by whitespace, and have single underscores interspersed between digits.
  - The allowed bases are 0 and 2–36. For base 0, the string is interpreted in a similar way to an integer literal in code, in that the actual base is 2, 8, 10, or 16 as determined by the prefix.
- `float(x=0.0)` Return a floating point number constructed from a number or string x.
- `complex(real=0, imag=0)` or `complex(string)` Return a complex number with the value `real` + `imag`*1j or convert a string or number to a complex number. If both arguments are omitted, returns `0j`.
<br>

- `bytearray(source=b'')`
- `bytearray(source, encoding)`
- `bytearray(source, encoding, errors)`
- Return a new array of bytes which is a mutable sequence of integers in the range `0 <= x < 256`. The optional source parameter can be used to initialize the array in a few different ways:
  - If it is a string, you must also give the encoding (and optionally, errors) parameters; `bytearray()` then converts the string to bytes using `str.encode()`.
  - If it is an integer, the array will have that size and will be initialized with null bytes.
  - If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.
  - If it is an iterable, it must be an iterable of integers in the range `0 <= x < 256`, which are used as the initial contents of the array.
  - Without an argument, an array of size 0 is created.
- `bytes(source=b'')`
- `bytes(source, encoding)`
- `bytes(source, encoding, errors)`
- Return a new `bytes` object which is an immutable sequence of integers in the range `0 <= x < 256`. bytes is an immutable version of bytearray. Accordingly, constructor arguments are interpreted as for `bytearray()`.
<br>

- `list(iterable)` Rather than being a function, list is actually a mutable sequence type.
- `tuple(iterable)` Rather than being a function, tuple is actually an immutable sequence type.
- `set(iterable)` Return a new set object, optionally with elements taken from iterable.
- `enumerate(iterable, start=0)` Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The `__next__()` method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
- `dict(**kwarg)`
- `dict(mapping, **kwarg)`
- `dict(iterable, **kwarg)`
- Create a new dictionary. The dict object is the dictionary class.
<br>

- `range(stop)`
- `range(start, stop, step=1)`
- Rather than being a function, range is actually an immutable sequence type.
- `slice(stop)`
- `slice(start, stop, step=1)`
- Return a slice object representing the set of indices specified by `range(start, stop, step)`. Slice objects are also generated when extended indexing syntax is used, e.g. `a[start:stop:step]` or `a[start:stop, i]`.
<br>

- `str(object='')`
- `str(object=b'', encoding='utf-8', errors='strict')`
- Return a string version of object. If object is not provided, returns the empty string. Otherwise, the behavior of `str()` depends on whether encoding or errors is given, as follows.
- If neither encoding nor errors is given, `str(object)` returns `type(object).__str__(object)`, which is the informal or nicely printable string representation of object. For string objects, this is the string itself. If object does not have a `__str__()` method, then `str()` falls back to returning `repr(object)`.
- If at least one of encoding or errors is given, object should be a bytes-like object. In this case, if object is a `bytes` or `bytearray` object, then `str(bytes, encoding, errors)` is equivalent to `bytes.decode(encoding, errors)`.
<br>

- `super(type, object_or_type=None)` Return a proxy object that delegates method calls to a parent or sibling class of type. The `object_or_type` determines the method resolution order to be searched. The search starts from the class right after the type.
- `type(object)`
- `type(name, bases, dict, **kwds)`
- With one argument, return the type of an object. The return value is a type object and generally the same object as returned by `object.__class__`.
- With three arguments, return a new type object.
  - The name `string` is the class name and becomes the `__name__` attribute.
  - The `bases` tuple contains the base classes and becomes the `__bases__` attribute; if empty, `object`, the ultimate base of all classes, is added.
  - The `dict` dictionary contains attribute and method definitions for the class body; it may be copied or wrapped before becoming the `__dict__` attribute.


### Calculate
- `abs(x)` Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing `__abs__()`. If the argument is a complex number, its magnitude is returned.
- `divmod(a, b)` Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.
  - With mixed operand types, the rules for binary arithmetic operators apply.
  - For integers, the result is the same as `(a // b, a % b)`.
  - For floating point numbers the result is `(q, a % b)`, where q is usually math.floor`(a / b)` but may be 1 less than that.
  - If `a % b` is non-zero, it has the same sign as b.
- `eval(expression, globals=None, locals=None)` The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.
- `pow(base, exp, mod=None)` Return base to the power exp; if mod is present, return base to the power exp, modulo mod. If mod is present and exp is negative, base must be relatively prime to mod. In that case, `pow(inv_base, -exp, mod)` is returned, where `inv_base` is an inverse to `base` modulo `mod`.
- `round(number, ndigits=None)` Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.
- `sum(iterable, /, start=0)` Sums start and the items of an iterable from left to right and returns the total.

### Convert
- `bin(x)` Convert an integer number to a binary string prefixed with "0b". If x is not a Python int object, it has to define an `__index__()` method that returns an integer.
- `hex(x)` Convert an integer number to a lowercase hexadecimal string prefixed with "0x". If x is not a Python int object, it has to define an `__index__()` method that returns an integer.
- `oct(x)` Convert an integer number to an octal string prefixed with "0o". The result is a valid Python expression. If x is not a Python int object, it has to define an `__index__()` method that returns an integer.
- `format(value, format_spec='')` Convert a value to a “formatted” representation, as controlled by format_spec. The interpretation of format_spec will depend on the type of the value argument
<br>

- `chr(i)` Return the string representing a character whose Unicode code point is the integer i.
- `ord(c)` Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.


### Get
- `dir()` or `dir(object)` Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object. If the object has a method named `__dir__()`, this method will be called and must return the list of attributes.
- `getattr(object, name)` or `getattr(object, name, default)` Return the value of the named attribute of object. name must be a string. If the named attribute does not exist, default is returned if provided, otherwise `AttributeError` is raised. name need not be a Python identifier.
- `setattr(object, name, value)` The arguments are an object, a string, and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it.
- `globals()` Return the dictionary implementing the current module namespace.
- `hash(object)` Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).
- `help()` or `help(request)` Invoke the built-in help system. If no argument is given, the interactive help system starts on the interpreter console.
- `id(object)` Return the "identity" of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. In CPython, this is the address of the object in memory.
- `len(s)` Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set). In CPython, it will raises `OverflowError` on lengths larger than `sys.maxsize`.
- `locals()` Update and return a dictionary representing the current local symbol table.
- `open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)` Open file and return a corresponding file object. If the file cannot be opened, an `OSError` is raised.
- `sorted(iterable, /, *, key=None, reverse=False)` Return a new sorted list from the items in iterable.
  - `key` specifies a function of one argument that is used to extract a comparison key from each element in iterable, e.g. `key=str.lower`. The default value is None (compare the elements directly).
  - `reverse` is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
- `vars()` or `vars(object)` Return the `__dict__` attribute for a module, class, instance, or any other object with a `__dict__` attribute. Without an argument, `vars()` acts like `locals()`.
<br>

- `max(iterable, *, key=None)`
- `max(iterable, *, default, key=None)`
- `max(arg1, arg2, *args, key=None)`
- Return the largest item in an iterable or the largest of two or more arguments.
- The `key` argument specifies a one-argument ordering function where comparison of iterable is performed based on its return value.
- The `default` argument specifies an object to return if the provided iterable is empty.
- `min(iterable, *, key=None)`
- `min(iterable, *, default, key=None)`
- `min(arg1, arg2, *args, key=None)`
- Return the smallest item in an iterable or the smallest of two or more arguments.

### Iterator
- `iter(object)`
- `iter(object, sentinel)`
- Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument.
  - Without a second argument, object must be a collection object which supports the iterable protocol (the `__iter__()` method), or it must support the sequence protocol (the `__getitem__()` method with integer arguments starting at 0). If it does not support either of those protocols, `TypeError` is raised.
  - If the second argument is given, then object must be a callable object. The iterator created in this case will call object with no arguments for each call to its `__next__()` method; if the value returned is equal to sentinel, `StopIteration` will be raised, otherwise the value will be returned.
- `next(iterator)`
- `next(iterator, default)`
- Retrieve the next item from the iterator by calling its `__next__()` method. If default is given, it is returned if the iterator is exhausted, otherwise `StopIteration` is raised.
<br>

- `filter(function, iterable)` Construct an iterator from those elements of iterable for which function returns true. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
- `map(function, iterable, *iterables)` Return an iterator that applies function to every item of iterable, yielding the results.
  - If additional iterables arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.
  - With multiple iterables, the iterator stops when the shortest iterable is exhausted.
  - For example : `map(lambda x, y : x + y, [1, 2, 3], [0, 5, 3])`
- `reversed(seq)` Return a reverse iterator. seq must be an object which has a `__reversed__()` method or supports the sequence protocol
- `zip(*iterables, strict=False)` Iterate over several iterables in parallel, producing tuples with an item from each one.
  - By default, `zip()` stops when the shortest iterable is exhausted. It will ignore the remaining items in the longer iterables.
  - If `strict` is True, `zip()` will raise a `ValueError` if one iterable is exhausted before the others.
  - With a single iterable argument, zip() returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.


### Test
- `all(iterable)` Return True if all elements of the iterable are true (or if the iterable is empty).
- `any(iterable)` Return True if any element of the iterable is true. If the iterable is empty, return False.
- `callable(object)` Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed. Note that classes are callable; instances are callable if their class has a `__call__()` method.
- `hasattr(object, name)` The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not.
- `isinstance(object, classinfo)` Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect, or virtual) subclass thereof. If object is not an object of the given type, the function always returns False. If classinfo is a tuple of type objects (or recursively, other such tuples) or a Union Type of multiple types, return True if object is an instance of any of the types.
- `issubclass(class, classinfo)` Return True if class is a subclass (direct, indirect, or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects (or recursively, other such tuples) or a Union Type, in which case return True if class is a subclass of any entry in classinfo.

### I/O
- `input()` or `input(prompt)` If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised.
- `print(*objects, sep=' ', end='\n', file=None, flush=False)` Print objects to the text stream `file`, separated by `sep` and followed by `end`.
  - All non-keyword arguments are converted to strings and written to the stream, separated by `sep` and followed by `end`.
  - The `file` argument must be an object with a `write(string)` method; if it is not present or None, `sys.stdout` will be used. Since printed arguments are converted to text strings, `print()` cannot be used with binary mode file objects.
  - Whether the output is buffered is usually determined by file, but if the `flush` keyword argument is true, the stream is forcibly flushed.








## Built-in Types
### Numeric Types (int, float, complex)
- Appending 'j' or 'J' to a numeric literal yields an imaginary number. The real and imaginary part of the complex number are each a floating point number. To extract these parts from a complex number z, use `z.real` and `z.imag`.

**int methods**
- `bit_count()` Return the number of ones in the binary representation of the absolute value of the integer.
- `bit_length()` Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros, e.g. `(-3).bit_length` is 2.
- `to_bytes(length=1, byteorder='big', *, signed=False)` Return an array of bytes representing an integer.
  - The integer is represented using `length` bytes. An `OverflowError` is raised if the integer is not representable with the given number of bytes.
  - The `byteorder` argument determines the byte order used to represent the integer. If byteorder is `"big"`, the most significant byte is at the beginning of the byte array. If byteorder is `"little"`, the most significant byte is at the end of the byte array.
  - The `signed` argument determines whether two’s complement is used to represent the integer. If `signed` is False and a negative integer is given, an `OverflowError` is raised.
- `from_bytes(bytes, byteorder='big', *, signed=False)` Return the integer represented by the given array of bytes.
- `as_integer_ratio()` Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

**float methods**
- `as_integer_ratio()` Return a pair of integers, whose ratio is exactly equal to the original float and with a positive denominator.
- `is_integer()` Return True if the float instance is finite with integral value, and False otherwise
- `hex()` Return a hexadecimal representation of a floating-point number. For finite floating-point numbers, this representation will always include a leading 0x and a trailing p and exponent.
- `fromhex(string)` Create a floating-point number from a hexadecimal string.

**complex metheds**
- `conjugate()` Return the complex conjugate of its argument.


### Iterator Types
- Python supports a concept of iteration over containers. This is implemented using two distinct methods. Sequences always support the iteration methods.
- One method needs to be defined for container objects to provide iterable support `container.__iter__()`, which return an iterator object. The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:
  - `iterator.__iter__()` Return the iterator object itself. This is required to allow both containers and iterators to be used with the `for` and `in` statements.
  - `iterator.__next__()` Return the next item from the iterator. If there are no further items, raise the `StopIteration` exception.
- Python’s generators provide a convenient way to implement the iterator protocol. If a container object’s `__iter__()` method is implemented as a generator, it will automatically return an iterator object (technically, a generator object) supplying the `__iter__()` and `__next__()` methods.

### Sequence Types
- `a + b` the concatenation of a and b
- `a * n` or `n * a` equivalent to adding a to itself n times. Replicating a list with `*` doesn’t create copies, it only creates references to the existing objects, i.e. after `a = [[0]] * 3; a[0][0] = 1`, a will be `[[1], [1], [1]]`.
- Some sequence types (such as `range`) only support item sequences that follow specific patterns, and hence don’t support sequence concatenation or repetition.
- While the `in` and `not in` operations are used only for simple containment testing in the general case, some specialised sequences (such as `str`, `bytes` and `bytearray`) also use them for subsequence testing, e.g. `"gg" in "eggs"` is True.
- The only operation that immutable sequence types generally implement that is not also implemented by mutable sequence types is support for the `hash()` built-in.






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