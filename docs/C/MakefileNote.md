
### Build Process
```makefile
# 预处理
gcc -E test.c -o test.i

# 编译
gcc -S test.i [-o test.s]

# 汇编
gcc -c test.s [-o test.o]

# 链接，生成a.exe
gcc test.o
# 生成test.exe
gcc test.o -o test.exe
```
```makefile
# 多源文件的编译
gcc test1.c test2.c -o test.exe

# 编译优化，0为不优化，1-3优化越来越强
gcc -O0 test.c -o text.exe
gcc -O|-O1 test.c -o text.exe
gcc -O2 test.c -o text.exe
gcc -O3 test.c -o text.exe

# 禁止警告信息
gcc -w test.c -o test.exe
# 产生尽可能多的警告信息
gcc -Wall test.c -o test.exe
# 将所有警报当成错误
gcc -Werror test.c -o test.exe
```
```makefile
# 向 gcc 的头文件搜索路径中添加新的目录
gcc -I ./include test.c -o test.exe
# 向 gcc 的库文件搜索路径中添加新的目录
gcc -L ./lib test.c -o test.exe
```


### Makefile

##### 执行步骤
- 读入所有的Makefile
- 读入被include的其它Makefile
- 初始化文件中的变量
- 推导隐晦规则，并分析所有规则
- 为所有的目标文件创建依赖关系链
- 根据依赖关系，决定哪些目标要重新生成
- 执行生成命令

##### 书写规则
```makefile
targets : prerequisites
        command
        ... 


targets : prerequisites ; command
        command
        ...
```


##### 伪目标文件
```makefile
.PHONY : clean          # 表示是个伪目标文件
clean :
        rm $(OBJS)
```
##### 引用
```makefile
include foo.make *.mk $(makefiles)
```
- 若未指定路径，则会先在当前目录寻找，若未找到，那么make还会在下面的几个目录下找：
    - 如果make执行时，有`-I|--include-dir`参数，那么make就会在这个参数所指定的目录下去寻找
    - 如果目录`<prefix>/include`（一般是：`/usr/local/bin`或`/usr/include`）存在的话，make也会去找

##### 文件搜寻
```makefile
VPATH = foo:bar
vpath %.c ../header
vpath %.h foo:bar
```
- 若定义了`VPATH`，那么make就会在当前目录找不到指定文件的情况下，到所指定的目录中去寻找文件
- `vpath <pattern> <directories>` 为符合模式<pattern>的文件指定搜索目录。
- `vpath <pattern>` 清除符合模式<pattern>的文件的搜索目录。
- `vpath` 清除所有已被设置好了的文件搜索目录。
- 目录由冒号分隔

##### 多目标
```makefile
$(OBJS) : defs.h
kbd.o command.o files.o : command.h
display.o insert.o search.o files.o : buffer.h
```

##### 自动化变量
- `$@` 表示规则中的目标文件集。在模式规则中，如果有多个目标，那么，`$@`就是匹配于目标中模式定义的集合。
- `$<` 依赖目标中的第一个目标名字。如果依赖目标是以模式（即%）定义的，那么`$<`将是符合模式的一系列的文件集。注意，其是一个一个取出来的。
- `$?` 所有比目标新的依赖目标的集合。以空格分隔。
- `$^` 所有依赖目标的集合。以空格分隔。如果在依赖目标中有多个重复的，那个这个变量会去除重复的依赖目标，只保留一份。
- `$+` 所有依赖目标的集合，但不去除重复的依赖目标。
- `$%` 仅当目标是函数库文件中，表示规则中的目标成员名。例如，如果一个目标是`foo.a(bar.o)`，那么，`$%`就是`bar.o`，`$@`就是`foo.a`。如果目标不是函数库文件（Unix下是`.a`，Windows下是`.lib`），那么，其值为空

##### 模式规则
```makefile
%.o : %.c
        $(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@
```
- `%` 表示一个或多个字符
- 如果`%`定义在目标中，那么目标中的`%`的值决定了依赖目标中的`%`的值

##### 隐含规则
```makefile
all : foo.o bar.o
        gcc foo.o bar.o -o test

foo.o : foo.h
bar.o : bar.h
```
- 编译C程序的隐含规则：`<n>.o`的目标的依赖目标会自动推导为`<n>.c`，并且其生成命令是`$(CC) –c $(CPPFLAGS) $(CFLAGS)`
- 编译C++程序的隐含规则：`<n>.o`的目标的依赖目标会自动推导为`<n>.cc`或是`<n>.C`，并且其生成命令是`$(CXX) –c $(CPPFLAGS) $(CFLAGS)`（建议使用`.cc`作为C++源文件的后缀，而不是`.C`）

```makefile
# 取消内建隐含规则
%.o :%.c
# 定义隐含规则
%.o : %.c foo.h
        $(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@
```
