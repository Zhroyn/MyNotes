
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
```makefile
all : test.o
        gcc test.o -o test

test.o : test.c
        gcc -c test.c

clean :
        rm test.exe

```