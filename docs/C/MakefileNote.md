
# Makefile 笔记

## 编译选项

```shell
# 预处理
gcc -E main.c -o main.i
# 编译
gcc -S main.i [-o main.s]
# 汇编
gcc -c main.s [-o main.o]
# 链接
gcc main.o
```

- `-E` 只进行预处理，默认输出到终端
- `-S` 只进行预处理和编译，默认输出同名 `.s` 文件
- `-c` 只进行预处理、编译和汇编，不进行链接，默认输出同名 `.o` 文件
- `-o` 指定输出文件的名称。若在生成可执行文件不使用该选项，则会使用默认名称 `a`
- `-std=cXX` 指定 C 语言标准
- `-I` 添加头文件搜索路径，如 `-Iinclude`
- `-L` 添加库文件搜索路径，如 `-Llib`
- `-D` 在编译过程中定义预处理器宏，如 `-DDEBUG` `-DVERSION=1`
- `-I` `-L` `-D` 参数可以有空格也可以没有

优化选项有：

- `-O0` 默认选项，不执行任何优化
- `-O/O1` 执行基本的优化
- `-O2` 执行更高级的优化
- `-O3` 执行最高级别的优化
- `-Os` 用于生成尽可能小的代码
- `-Og` 在优化代码的同时，尽可能地保留调试信息

警告选项有：

- `-w` 禁止所有警告
- `-Wall` 打开大部分警告
- `-Wextra` 除了 `-Wall` 之外的额外警告
- `-Werror` 将所有警告视为错误，会导致编译失败

调试选项有：

- `-g` 在编译时包含调试信息，以便使用调试器进行调试
- `-fsanitize=address` 开启 AddressSanitizer，在运行时检测诸如数组越界、堆溢出、栈溢出、全局变量溢出、使用已释放的内存等问题
- `-fsanitize=leak` 开启 LeakSanitizer，会在程序结束时检查哪些内存块仍然被分配但未被释放，并报告这些泄漏
- `-fsanitize=undefined` 开启 UndefinedBehaviorSanitizer，可以检测未定义行为，如除以零、空指针解引用、整数溢出等





<br>

## 规则

一个 Makefile 通常包含一系列的规则，每个规则描述了如何生成一个或多个目标文件。每个规则的基本结构如下：

```makefile
target: dependencies
    command
```

- `target` 目标文件，可以是最终的可执行文件、中间目标文件或伪目标。伪目标是不会生成实际文件的目标，常见的有 `all` `clean` 等。伪目标通常使用 .PHONY 来声明，如 `.PHONY: all clean`，这样就不会把它们当作文件名来处理
- `dependencies` 依赖文件或目标，它们是生成目标文件所需的文件。当依赖文件比目标新时，就会执行规则中的命令；当依赖是目标时，就先会执行这个目标
- `command` 生成目标文件的命令，这些命令必须以 TAB 字符开头

使用 Makefile 构建项目时，通常在终端中运行 `make` 命令。`make` 将自动查找名为 `Makefile` 或 `makefile` 的文件，然后执行第一个目标，也可以通过 `make target` 来指定执行的目标。

### 模式规则

模式规则使用通配符来匹配一类文件，从而为这些文件定义共同的构建方式。下面是模式规则的一个示例：

```makefile
%.o: %.c
    $(CC) -c $(CFLAGS) $< -o $@

%.o: %.cpp
    $(CXX) -c $(CXXFLAGS) $< -o $@
```

模式规则必须在目标中使用模式字符 `%`，它可以匹配任何非空字符串。当 `%` 在依赖中出现时，它代表与目标中的 `%` 匹配到的字符串相同的字符串。





<br>

## 变量

Makefile 中的变量可以用于存储命令中的重复部分，也可以用于存储编译选项、搜索路径等。变量的定义格式为 `VAR = value`，使用时用 `$(VAR)` 或 `${VAR}` 来引用。

Makefile 中有几种不同类型的变量赋值方式：

- `=` 延时赋值，在解析到该变量时再进行赋值
- `:=` 即时赋值，在定义变量时立即赋值
- `?=` 条件赋值，仅在变量未被定义过时赋值
- `+=` 追加赋值，在现有变量值后追加内容

### 自动变量

自动变量用于在规则的命令部分自动获取目标文件和依赖文件的名称，可以减少重复代码。常用的自动变量有：

- `$@` 规则的目标文件集
- `$<` 规则的第一个依赖文件名
- `$^` 规则的所有依赖文件名，包含重复项
- `$+` 规则的所有依赖文件名，不包含重复项
- `$?` 所有比目标文件新的依赖文件名




<br>

## 函数

Makefile 函数的使用语法 `$(function arguments)`，常用的函数有：

- `$(wildcard pattern)` 扩展通配符，例如 `$(wildcard *.c)`
- `$(subst from,to,text)` 字符串替换，例如 `$(subst .c,.o,$(SRC))`
- `$(patsubst pattern,replacement,text)` 模式替换，例如 `$(patsubst %.c,%.o,$(SRC))`
- `$(addprefix prefix,names)` 为每个名字添加前缀
- `$(addsufix prefix,names)` 为每个名字添加后缀
- `$(dir names)` 返回文件名中的目录部分，如 `src/`
- `$(notdir names)` 返回文件名中的非目录部分，如 `main.c`
- `$(basename names)` 返回去掉后缀的文件名，如 `src/main`
- `$(suffix names)` 返回文件名中的后缀部分，如 `.c`
- `$(filter pattern,text)` 返回符合模式的字符串
- `$(filter-out pattern,text)` 返回不符合模式的字符串
- `$(shell command)` 执行 shell 命令并返回结果





<br>

## 搜索路径

当构建一个项目时，有时源文件、头文件和目标文件会分布在不同的目录中。`VPATH` 和 `vpath` 可以帮助 make 在指定的目录中查找文件。

`VPATH` 是一个全局变量，用于为所有文件类型指定搜索路径，不同搜索路径之间用 `:` 分割，例如 `VPATH = src:include`。

`vpath` 是一种更灵活的方法，允许为特定类型的文件指定搜索路径，语法为 `vpath pattern directories`，示例如下：

```makefile
vpath %.c src
vpath %.h include
```



<br>

## 命令

make 会将执行的命令输出到屏幕上，我们可以通过在命令最前面加上 `@` 来禁止输出这个命令。例如：

```makefile
all:
    @echo "Building project..."
    gcc -o main main.c
```

如果要忽略命令的出错，可以在命令前面加上 `-` 符号。例如：

```makefile
clean:
    -rm -f *.o
```
