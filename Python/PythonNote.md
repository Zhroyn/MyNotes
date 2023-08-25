<!-- TOC -->

- [内建函数](#内建函数)
  - [迭代](#迭代)
  - [转换](#转换)
  - [算术](#算术)
  - [对象](#对象)
  - [输入输出](#输入输出)
- [Command line and environment](#command-line-and-environment)
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
- [Built-in Types](#built-in-types)
  - [Numeric Types (int, float, complex)](#numeric-types-int-float-complex)
  - [Sequence Types (list, tuple, range)](#sequence-types-list-tuple-range)
  - [Text Sequence Type (str)](#text-sequence-type-str)
    - [Find and Delete](#find-and-delete)
    - [Split and Join](#split-and-join)
    - [Convert](#convert)
    - [Testing](#testing)
    - [printf-style String Formatting](#printf-style-string-formatting)
    - [Format String Syntax](#format-string-syntax)
    - [Formatted String Literals](#formatted-string-literals)
  - [Byte Sequence Types (bytes, bytearray)](#byte-sequence-types-bytes-bytearray)
  - [Set Types (set, frozenset)](#set-types-set-frozenset)
  - [Mapping Types (dict)](#mapping-types-dict)
  - [Iterator Types](#iterator-types)
  - [Context Manager Types](#context-manager-types)

<!-- /TOC -->






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
- `bin(number)` 将 number 转换为前缀为 0b 的二进制数字符串
- `oct(number)` 将 number 转换为前缀为 0o 的八进制数字符串
- `hex(number)` 将 number 转换为前缀为 0x 的十六进制数字符串
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








<br>

## Built-in Types
### Numeric Types (int, float, complex)
- Appending 'j' or 'J' to a numeric literal yields an imaginary number. The real and imaginary part of the complex number are each a floating point number. To extract these parts from a complex number z, use `z.real` and `z.imag`.

**constructor**
- `bool(x=False)` Return a Boolean value. x is converted using the standard truth testing procedure. If x is false or omitted, this returns False; otherwise, it returns True.
- `int(x=0)` or `int(x, base=10)` Return an integer object constructed from a number or string x, or return 0 if no arguments are given.
  - For floating point numbers, this truncates towards zero.
  - If base is given, then x must be a string, bytes, or bytearray instance representing an integer in radix base. Optionally, the string can be preceded by `+` or `-` (with no space in between), have leading zeros, be surrounded by whitespace, and have single underscores interspersed between digits.
  - The allowed bases are 0 and 2–36. For base 0, the string is interpreted in a similar way to an integer literal in code, in that the actual base is 2, 8, 10, or 16 as determined by the prefix.
- `float(x=0.0)` Return a floating point number constructed from a number or string x.
- `complex(real=0, imag=0)` or `complex(string)` Return a complex number with the value `real` + `imag`*1j or convert a string or number to a complex number. If both arguments are omitted, returns `0j`.

**methods of int**
- `bit_count()` Return the number of ones in the binary representation of the absolute value of the integer.
- `bit_length()` Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros, e.g. `(-3).bit_length` is 2.
- `to_bytes(length=1, byteorder='big', *, signed=False)` Return an array of bytes representing an integer.
  - The integer is represented using `length` bytes. An `OverflowError` is raised if the integer is not representable with the given number of bytes.
  - The `byteorder` argument determines the byte order used to represent the integer. If byteorder is `"big"`, the most significant byte is at the beginning of the byte array. If byteorder is `"little"`, the most significant byte is at the end of the byte array.
  - The `signed` argument determines whether two’s complement is used to represent the integer. If `signed` is False and a negative integer is given, an `OverflowError` is raised.
- `from_bytes(bytes, byteorder='big', *, signed=False)` Return the integer represented by the given array of bytes.
- `as_integer_ratio()` Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

**methods of float**
- `as_integer_ratio()` Return a pair of integers, whose ratio is exactly equal to the original float and with a positive denominator.
- `is_integer()` Return True if the float instance is finite with integral value, and False otherwise
- `hex()` Return a hexadecimal representation of a floating-point number. For finite floating-point numbers, this representation will always include a leading 0x and a trailing p and exponent.
- `fromhex(string)` Create a floating-point number from a hexadecimal string.

**methods of complex**
- `conjugate()` Return the complex conjugate of its argument.


### Sequence Types (list, tuple, range)
**constructor**
- `list(iterable)` Rather than being a function, list is actually a mutable sequence type.
- `tuple(iterable)` Rather than being a function, tuple is actually an immutable sequence type.
- `range(stop)` or `range(start, stop, step=1)` Rather than being a function, range is actually an immutable sequence type. Two range objects are considered equal if they represent the same sequence of values.
- `slice(stop)` or `slice(start, stop, step=1)` Return a slice object representing the set of indices specified by `range(start, stop, step)`. Slice objects are also generated when extended indexing syntax is used, e.g. `a[start:stop:step]` or `a[start:stop, i]`.
<br>

**commom sequence operations**
- `a + b` the concatenation of a and b
- `a * n` or `n * a` equivalent to adding a to itself n times. 
  - Replicating a list with `*` doesn’t create copies, it only creates references to the existing objects, i.e. after `a = [[0]] * 3; a[0][0] = 1`, a will be `[[1], [1], [1]]`.
  - Some sequence types (such as `range`) only support item sequences that follow specific patterns, and hence don’t support sequence concatenation or repetition.
- While the `in` and `not in` operations are used only for simple containment testing in the general case, some specialised sequences (such as `str`, `bytes` and `bytearray`) also use them for subsequence testing, e.g. `"gg" in "eggs"` is True.
- Slicing will create a shallow copy, which constructs a new compound object and then inserts references into it to the objects found in the original.
<br>

- `index(value, start=0, stop=9223372036854775807)` Return first index of value.
- `index(sub[, start[, end]])` Return the lowest index where substring/subsection sub is found.
  - Optional arguments `start` and `end` are interpreted as in slice notation.
  - Raises `ValueError` when the value/substring/subsection is not found.
- `count(value)` Return number of occurrences of value.
- `count(sub[, start[, end]])` Return the number of non-overlapping occurrences of substring sub in `S[start:end]`.
  - Optional arguments start and end are interpreted as in slice notation.
- The only operation that immutable sequence types generally implement that is not also implemented by mutable sequence types is support for the `hash()` built-in.

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

**methods of list**
- `append(object)` Append object to the end of the list.
- `clear()` Remove all items from list.
- `copy()` Return a shallow copy of the list.
- `extend(iterable)` Extend list by appending elements from the iterable.
- `insert(index, object)` Insert object before index. If index is greater than `len(s)`, it's considered `len(s)`; if less than `-len(s)`, it's considered `-len(s)`.
- `pop(index=-1)` Remove and return item at index (default last). Raises `IndexError` if list is empty or index is out of range.
- `remove(value)` Remove first occurrence of value. Raises `ValueError` if the value is not present.
- `reverse()` Reverse in place.
- `sort(*, key=None, reverse=False)` Sort the list in ascending order and return None.
  - The sort is in-place and stable, i.e. the order of two equal elements is maintained.
  - If a `key` function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.
  - The `reverse` flag can be set to sort in descending order.

### Text Sequence Type (str)
- Strings are **immutable** sequences of Unicode code points.
- String literals can be written in a variety of ways. Single quotes allow embedded double quotes, double quotes allow embedded single quotes, triple single quotes and double quotes allow both.
- Triple quoted strings may span multiple lines. All associated whitespace will be included in the string literal.
- String literals that are part of a single expression and have only whitespace between them will be implicitly converted to a single string literal.
- Both string and bytes literals may optionally be prefixed with a letter `r` or `R`; such strings are called raw strings and treat backslashes as literal characters.

**constructor**
- `str(object='')`
- `str(object=b'', encoding='utf-8', errors='strict')`
- Return a string version of object. If object is not provided, returns the empty string. Otherwise, the behavior of `str()` depends on whether encoding or errors is given, as follows.
  - If neither encoding nor errors is given, `str(object)` returns `type(object).__str__(object)`, which is the informal or nicely printable string representation of object. For string objects, this is the string itself. If object does not have a `__str__()` method, then `str()` falls back to returning `repr(object)`.
  - If at least one of encoding or errors is given, object should be a bytes-like object. In this case, if object is a `bytes` or `bytearray` object, then `str(bytes, encoding, errors)` is equivalent to `bytes.decode(encoding, errors)`.
  - Passing a bytes object to `str()` without the `encoding` or `errors` arguments falls under the first case of returning the informal string representation like `"b'abc'"`

#### Find and Delete
- `find(sub[, start[, end]])` Return -1 on failure, others are the same as `index()`.
- `rfind(sub[, start[, end]])` Return the highest index where substring sub is found, and return -1 on failure.
- `rindex(sub[, start[, end]])` Return the highest index where substring sub is found, and raises `ValueError` when the substring is not found.
<br>

- `strip(chars=None)` Return a copy of the string with leading and trailing whitespace removed. If `chars` is given and not None, remove characters in `chars` instead.
- `lstrip(chars=None)` Return a copy of the string with leading whitespace removed.
- `rstrip(chars=None)` Return a copy of the string with trailing whitespace removed.
- `removeprefix(prefix)` Return a str with the given prefix string removed if present. If the string starts with the prefix string, return `string[len(prefix):]`. Otherwise, return a copy of the original string.
- `removesuffix(suffix)` Return a str with the given suffix string removed if present. If the string ends with the suffix string and that suffix is not empty, return `string[:-len(suffix)]`. Otherwise, return a copy of the original string.

#### Split and Join
- `partition(sep)` Partition the string into three parts using the given separator.
  - If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.
  - If the separator is not found, returns a 3-tuple containing the original string and two empty strings.
- `rpartition(sep)` Partition the string into three parts using the given separator. This will search for the separator in the string, starting at the end, others are the same as `partition()`
<br>

- `split(sep=None, maxsplit=-1)` Return a list of the substrings in the string, using sep as the separator string.
  - When `seq` is None (the default value), it will split on any whitespace character (including `\n`, `\r`, `\t`, `\f` and spaces) and will discard empty strings from the result.
  - `maxsplit` is the maximum number of splits (starting from the left), -1 (the default value) means no limit.
- `rsplit(sep=None, maxsplit=-1)` Splitting starts at the end of the string and works to the front, others are the same as `split()`
- `splitlines(keepends=False)` Return a list of the lines in the string, breaking at line boundaries (including `\n`, `\r`, `\r\n` and so on). Line breaks are not included in the resulting list unless `keepends` is true.
<br>

- `join(iterable)` Concatenate any number of strings. The string whose method is called is inserted in between each given string. The result is returned as a new string. Example: `'.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'`

#### Convert
- `capitalize()` Return a capitalized version of the string. More specifically, make the first character have upper case and the rest lower case.
- `casefold()` Return a version of the string suitable for caseless comparisons.
- `title()` Return a version of the string where each word is titlecased.
- `lower()` Return a copy of the string converted to lowercase.
- `upper()` Return a copy of the string converted to uppercase.
- `swapcase()` Convert uppercase characters to lowercase and lowercase characters to uppercase.
<br>

- `center(width, fillchar=' ')` Return a centered string of length `width` with specified `fillcharacter`. The `width` can be less than `len(s)`
- `ljust(width, fillchar=' ')` Return a left-justified string of length `width` with specified `fillcharacter`.
- `rjust(width, fillchar=' ')` Return a right-justified string of length `width` with specified `fillcharacter`.
- `zfill(width)` Pad a numeric string with zeros on the left, to fill a field of the given width. The string is never truncated.
<br>

- `replace(old, new, count=-1)` Return a copy with all occurrences of substring `old` replaced by `new`. `count` is the maximum number of occurrences to replace, -1 (the default value) means replace all occurrences.
- `expandtabs(tabsize=8)` Return a copy where all tab characters are expanded using spaces.
- `format(*args, **kwargs)` Return a formatted version of str, using substitutions from `args` and `kwargs`. The substitutions are identified by braces.
- `format_map(mapping)` Return a formatted version of str, using substitutions from `mapping`. The substitutions are identified by braces.
<br>

- `translate(table)` Replace each character in the string using the given translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None. The table must implement lookup/indexing via `__getitem__()`, typically a mapping or sequence. If this operation raises `LookupError`, the character is left untouched. Characters mapped to None are deleted.
- `maketrans(x[, y[, z])` Return a translation table usable for `str.translate()`. It's a static method.
  - If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals.
  - If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y.
  - If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

#### Testing
- `startswith(prefix[, start[, end]])` Return True if str starts with the specified prefix, False otherwise.
  - With optional `start`, test str beginning at that position.
  - With optional `end`, stop comparing str at that position.
  - `prefix` can also be a tuple of strings to try.
- `endswith(suffix[, start[, end]])` Return True if str ends with the specified suffix, False otherwise.
<br>

- `isalnum()` Return True if the string is an alpha-numeric string, False otherwise. A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.
- `isalpha()` Return True if the string is an alphabetic string, False otherwise.
- `isascii()` Return True if all characters in the string are ASCII, False otherwise. ASCII characters have code points in the range `U+0000-U+007F`. Empty string is ASCII too.
- `isdecimal()` Return True if the string is a decimal string, False otherwise.
- `isdigit()` Return True if the string is a digit string, False otherwise.
- `isidentifier()` Return True if the string is a valid Python identifier, False otherwise. Call `keyword.iskeyword(s)` to test whether string s is a reserved identifier, such as "def" or "class".
- `islower()` Return True if the string is a lowercase string, False otherwise.
- `isnumeric()` Return True if the string is a numeric string, False otherwise.
- `isprintable()` Return True if the string is printable, False otherwise. A string is printable if all of its characters are considered printable in `repr()` or if it is empty.
- `isspace()` Return True if the string is a whitespace string, False otherwise.
- `istitle()` Return True if the string is a title-cased string, False otherwise. In a title-cased string, uppercase characters may only follow uncased characters and lowercase characters only cased ones.
- `isupper()` Return True if the string is an uppercase string, False otherwise.

#### printf-style String Formatting
- String objects have one unique built-in operation: the `%` operator (modulo). This is also known as the string formatting or interpolation operator.
- In `format % values`, if `format` requires a single argument, `values` may be a single non-tuple object. Otherwise, `values` must be a tuple with exactly the number of items specified by the format string, or a single mapping object.
- A conversion specifier contains two or more characters and has the following components, which must occur in this order:
  - The `%` character, which marks the start of the specifier.
  - Mapping key (optional), consisting of a parenthesised sequence of characters (for example, `(somename)`).
  - Conversion flags (optional), which affect the result of some conversion types.
  - Minimum field width (optional). If specified as an `*`, the actual width is read from the next element of the tuple in values, and the object to convert comes after the minimum field width and optional precision.
  - Precision (optional), given as a `.` followed by the precision. If specified as `*`, the actual precision is read from the next element of the tuple in values, and the value to convert comes after the precision.
  - Length modifier (optional).
  - Conversion type.

#### Format String Syntax
```C
replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
arg_name          ::=  [identifier | digit+]
attribute_name    ::=  identifier
element_index     ::=  digit+ | index_string
index_string      ::=  <any source character except "]"> +
conversion        ::=  "r" | "s" | "a"

format_spec     ::=  [[fill]align][sign][z][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```
- The `field_name` begins with an `arg_name` that is either a number or a keyword. If it’s a number, it refers to a positional argument, and if it’s a keyword, it refers to a named keyword argument.
- If the numerical `arg_names` in a format string are 0, 1, 2, … in sequence, they can all be omitted (**not just some**) and the numbers 0, 1, 2, … will be automatically inserted in that order.
- An expression of the form `.name` selects the named attribute using `getattr(),` while an expression of the form `[index]` does an index lookup using `__getitem__().`

**align and fill**
- If a valid `align` value is specified, it can be preceded by a `fill` character that can be any character and defaults to a space if omitted.
- `<` Forces the field to be left-aligned (this is the default for most objects).
- `>` Forces the field to be right-aligned (this is the default for numbers).
- `=` Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form `+000000120`. This alignment option is only valid for numeric types. It becomes the default for numbers when `0` immediately precedes the field `width`.
- `^` Forces the field to be centered within the available space.

**sign**
- `+` Indicates that a sign should be used for both positive as well as negative numbers.
- `-` Indicates that a sign should be used only for negative numbers (this is the default behavior).
- `space` Indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.

**z, #, 0**
- The `z` option forces negative zero floating-point values to positive zero after rounding to the format precision. This option is only valid for floating-point presentation types.
- The `#` option causes the "alternate form" to be used for the conversion. This option is only valid for integer, float and complex types.
  - For integers, when binary, octal, or hexadecimal output is used, this option adds the respective prefix `0b`, `0o`, `0x`, or `0X` to the output value.
  - For float and complex the alternate form causes the result of the conversion to always contain a decimal-point character.
  - In addition, for `g` and `G` conversions, trailing zeros are not removed from the result.
- When no explicit alignment is given, preceding the width field by a `0` character enables sign-aware zero-padding for numeric types. This is equivalent to a fill character of `0` with an alignment type of `=`.

**grouping_option**
- The `,` option signals the use of a comma for a thousands separator. For a locale aware separator, use the `n` integer presentation type instead.
- The `_` option signals the use of an underscore for a thousands separator for floating point presentation types and for integer presentation type `d`. For integer presentation types `b`, `o`, `x`, and `X`, underscores will be inserted every 4 digits. For other presentation types, specifying this option is an error.

**type**
- The available string presentation types are `s` and `None` (The same as `s`).
- The available integer presentation types are `b`, `c`, `d`, `o`, `x`, `X`, `n` and `None` (The same as `d`).
  - `n` Number. This is the same as `d`, except that it uses the current locale setting to insert the appropriate number separator characters.
- The available float presentation types are `e`, `E`, `f`, `F`, `g`, `G`, `n`, `%` and `None` (The same as `g`).
  - `n` Number. This is the same as `g`, except that it uses the current locale setting to insert the appropriate number separator characters.
  - `%` Percentage. Multiplies the number by 100 and displays in fixed (`f`) format, followed by a percent sign.

#### Formatted String Literals
```C
f_string          ::=  (literal_char | "{{" | "}}" | replacement_field)*
replacement_field ::=  "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
f_expression      ::=  (conditional_expression | "*" or_expr)
                         ("," conditional_expression | "," "*" or_expr)* [","]
                       | yield_expression
conversion        ::=  "s" | "r" | "a"
format_spec       ::=  (literal_char | NULL | replacement_field)*
literal_char      ::=  <any code point except "{", "}" or NULL>
```
- A formatted string literal or f-string is a string literal that is prefixed with `f` or `F`. These strings may contain replacement fields, which are expressions delimited by curly braces `{}`.
- `{{` or `}}` are replaced with the corresponding single curly brace.
- Formatted string literals may be concatenated, but replacement fields cannot be split across literals.
- An empty expression is not allowed, and both `lambda` and assignment expressions `:=` must be surrounded by explicit parentheses. Each expression is evaluated in the context where the formatted string literal appears, in order from left to right.
- When the equal sign `=` is provided, the output will have the expression text, the `=` and the evaluated value. Spaces after the opening brace `{`, within the expression and after the `=` are all retained in the output.
- By default, the `=` causes the repr() of the expression to be provided, unless there is a format specified. When a format is specified it defaults to the str() of the expression unless a conversion `!r` is declared.
- The result is then formatted using the `format()` protocol. Top-level format specifiers may include nested replacement fields. These nested fields may include their own conversion fields and format specifiers, but may not include more deeply nested replacement fields.


### Byte Sequence Types (bytes, bytearray)
**constuctor**
- `bytes(source=b''[, encoding[, errors]])` Return a bytes object which is an immutable sequence of integers in the range `0 <= x < 256`.
- `bytearray(source=b''[, encoding[, errors]])` Return a new array of bytes which is a mutable sequence of integers in the range `0 <= x < 256`.
- The optional source parameter can be used to initialize the array in a few different ways:
  - If it is a string, you must also give the encoding (and optionally, errors) parameters; `bytes()` then converts the string to bytes using `str.encode()`.
  - If it is an integer, the array will have that size and will be initialized with null bytes.
  - If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.
  - If it is an iterable, it must be an iterable of integers in the range `0 <= x < 256`.

**bytes literal**
- The syntax for bytes literals is largely the same as that for string literals, except that a `b` prefix is added.
- Only ASCII characters are permitted in bytes literals.
- As with string literals, bytes literals may also use a `r` prefix to disable processing of escape sequences.
- While bytes literals and representations are based on ASCII text, bytes objects actually behave like immutable sequences of integers, with each value in the sequence restricted such that `0 <= x < 256`

**methods**
- `bytes` has most methods of `str` 
- `bytearray` has most methods of `str` and `list` 
- `fromhex(string)` The string must contain two hexadecimal digits per byte, with ASCII whitespace being ignored.
- `hex([sep[, bytes_per_sep]])` Return a string object containing two hexadecimal digits for each byte in the instance.
  - `sep` An optional single character or byte to separate hex bytes.
  - `bytes_per_sep` How many bytes between separators. Positive values count from the right, negative values count from the left. The default is 1.
<br>

- `encode(encoding='utf-8', errors='strict')` Encode the string using the codec registered for encoding. It's the method of `str`.
- `decode(encoding='utf-8', errors='strict')` Decode the bytes/bytearray using the codec registered for encoding. It's the method of `bytes` and `bytearray`.



### Set Types (set, frozenset)
- A set object is an unordered collection of distinct hashable objects.
- The `set` type is mutable, so it has no hash value and cannot be used as either a dictionary key or as an element of another `set`.
- The `frozenset` type is immutable and hashable, so it can therefore be used as a dictionary key or as an element of another `set`.

**constructor**
- `set(iterable)`
- `frozenset(iterable)`
- Return a new `set` or `frozenset` object, optionally with elements taken from `iterable`. The elements must be hashable.
- `set` (not `frozensets`) can also be created by using a comma-separated list of elements within braces, or using a set comprehension, in addition to the set constructor.

**commom set operations**
- `len(set)`, `x in s`, `x not in s`
- `isdisjoint(other)` Return True if the set has no elements in common with other.
- `issubset(other)`
  - `set <= other` Test whether every element in the set is in other.
  - `set < other` Test whether the set is a proper subset of other, that is, `set <= other` and `set != other`.
- `issuperset(other)`
  - `set >= other` Test whether every element in other is in the set.
  - `set > other` Test whether the set is a proper superset of other, that is, `set >= other` and `set != other`.
<br>

- `union(*others)` or `set | other | ...` Return a new set with elements from the set and all others.
- `intersection(*others)` or `set & other & ...` Return a new set with elements common to the set and all others.
- `difference(*others)` or `set - other - ...` Return a new set with elements in the set that are not in the others.
- `symmetric_difference(other)` or `set ^ other` Return a new set with elements in either the set or other but not both.
- `copy()` Return a shallow copy of the set.
<br>

- The non-operator versions of `union()`, `intersection()`, `difference()`, `symmetric_difference()`, `issubset()`, and `issuperset()` methods will accept any iterable as an argument.
- Instances of `set` are compared to instances of `frozenset` based on their members. For example, `set('abc') == frozenset('abc')` returns True and so does `set('abc') in set([frozenset('abc')])`.
- Operations that mix `set` instances with `frozenset` return the type of the first operand.

**operations for set**
- `add(elem)` Add element `elem` to the set.
- `remove(elem)` Remove element `elem` from the set. Raises `KeyError` if `elem` is not contained in the set.
- `discard(elem)` Remove element `elem` from the set if it is present.
- `pop()` Remove and return an arbitrary element from the set. Raises `KeyError` if the set is empty.
- `clear()` Remove all elements from the set.
<br>

- `update(*others)` or `set |= other | ...` Update a set with the union of itself and others.
- `intersection_update(*others)` or `set &= other & ...` Update a set with the intersection of itself and another.
- `difference_update(*others)` or `set -= other | ...` Remove all elements of another set from this set.
- `symmetric_difference_update(other)` or `set ^= other` Update a set with the symmetric difference of itself and another.


### Mapping Types (dict)
- `list(dict)`, `set(dict)` and `iter(dict)` only return the keys of the dictionary.
- The n number in worst-case complexities for copying and iterating the dictionary is the maximum size that the dictionary ever achieved.
- `d | other` or `d |= other` Create a new dictionary with the merged keys and values of `d` and `other`, which must both be dictionaries. The values of `other` take priority when `d` and `other` share keys.
- The objects returned by `dict.keys()`, `dict.values()` and `dict.items()` are view objects. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.
- Keys views are set-like since their entries are unique and hashable. For set-like views, all of the operations defined for the abstract base class `collections.abc.Set` are available, e.g. `==`, `<` and `^`.

**constructor**
- `dict(**kwarg)`
- `dict(mapping, **kwarg)`
- `dict(iterable, **kwarg)`
- Return a new dictionary initialized from an optional positional argument and a possibly empty set of keyword arguments.
  - If no positional argument is given, an empty dictionary is created.
  - If a positional argument is given and it is a mapping object, a dictionary is created with the same key-value pairs as the mapping object.
  - Otherwise, the positional argument must be an iterable object. Each item in the iterable must itself be an iterable with exactly two objects. The first object becomes a key and the second object the corresponding value.
  - If a key occurs more than once, the last value for that key becomes the corresponding value in the new dictionary.
  - If keyword arguments are given, the keyword arguments and their values are added to the dictionary created from the positional argument. If a key being added is already present, the value from the keyword argument replaces the value from the positional argument.
- `dict` can also be created by using a comma-separated list of elements of `key: value` pairs within braces, or using a dict comprehension.

**methods**
- `clear()` Remove all items from the dictionary.
- `copy()` Return a shallow copy of the dictionary.
- `fromkeys(iterable, value=None)` Create a new dictionary with keys from `iterable` and values set to `value`. It is a class method that returns a new dictionary.
- `get(key, default=None)` Return the value for key if key is in the dictionary, else default.
- `pop(key, default=None)` If key is in the dictionary, remove it and return its value, else return default.
- `popitem()` Remove and return a `(key, value)` pair from the dictionary. Pairs are returned in LIFO order. If the dictionary is empty, calling `popitem()` raises a `KeyError`.
- `setdefault(key, default=None)` If key is in the dictionary, return its value. If not, insert key with a value of default and return default.
- `update([other])` Update the dictionary with the key-value pairs from other, overwriting existing keys.
  - `update()` accepts either another dictionary object or an iterable of key-value pairs (as tuples or other iterables of length two).
  - If keyword arguments are specified, the dictionary is then updated with those key-value pairs.
<br>

- `items()` Return a new view of the dictionary’s items (`(key, value)` pairs).
- `keys()` Return a new view of the dictionary’s keys.
- `values()` Return a new view of the dictionary’s values. See the documentation of view objects. An equality comparison between one `dict.values()` view and another will always return False.


### Iterator Types
- Python supports a concept of iteration over containers. This is implemented using two distinct methods. Sequences always support the iteration methods.
- One method needs to be defined for container objects to provide iterable support `container.__iter__()`, which return an iterator object. The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:
  - `iterator.__iter__()` Return the iterator object itself. This is required to allow both containers and iterators to be used with the `for` and `in` statements.
  - `iterator.__next__()` Return the next item from the iterator. If there are no further items, raise the `StopIteration` exception.
- Python’s generators provide a convenient way to implement the iterator protocol. If a container object’s `__iter__()` method is implemented as a generator, it will automatically return an iterator object (technically, a generator object) supplying the `__iter__()` and `__next__()` methods.


### Context Manager Types
- Python’s `with` statement supports the concept of a runtime context defined by a context manager. This is implemented using a pair of methods that allow user-defined classes to define a runtime context that is entered before the statement body is executed and exited when the statement ends:
- `contextmanager.__enter__()` Enter the runtime context and return either this object or another object related to the runtime context.
  - The value returned by this method is bound to the identifier in the `as` clause of `with` statements using this context manager.
- `contextmanager.__exit__(exc_type, exc_val, exc_tb)` Exit the runtime context and return a Boolean flag indicating if any exception that occurred should be suppressed.
  - If an exception occurred while executing the body of the with statement, the arguments contain the exception type, value and traceback information. Otherwise, all three arguments are None.
  - Returning a true value from this method will cause the with statement to suppress the exception and continue execution with the statement immediately following the `with` statement.
  - Otherwise the exception continues propagating after this method has finished executing.
  - Exceptions that occur during execution of this method will replace any exception that occurred in the body of the `with` statement.






