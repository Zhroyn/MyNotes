
# C 语言笔记

## 基本数据类型

### 字符

char 分为 signed char 和 unsigned char，其中 gcc 默认是 signed char。二者当字符用时并无差别，但是当整数用时，会因符号扩展的不同产生差别。因此若有代码移植需求，最好使用 `stdint.h` 中的 `int8_t` 和 `uint8_t`。

!!! Example

    ```C
    char c = 0xff;
    printf("%s", c == 0xff ? "True" : "False");
    ```

    这样在 gcc 中打印的是 False，因为这里的 char 是有符号的，又会在参与运算前被提升为 int，变为 -1，而 0xff 是 255，所以不相等。

常见的字符的 ASCII 码如下：

- 数字为 48~57 (0x30~0x39)
- 大写字母为 65~90 (0x41~0x5A)
- 小写字母为 97~122 (0x61~0x7A)
- 空格为 32 (0x20)
- `\0`, `\b`, `\t`, `\n`, `\r` 依次为 0x00, 0x08, 0x09, 0x0A, 0x0D


<br>

### 整数

常见长度的整数类型有：

- short 为短整型，至少 16 位，转换说明符为 hd/hu
- int 为整型，至少 16 位，通常为 32 位，转换说明符为 d/u
- long 为长整型，至少 32 位，后缀为 l/L，转换说明符为 ld/lu
- long long 为长长整型，至少 64 位，后缀为 ll/LL，转换说明符为 lld/llu

上述整型默认是有符号的，若要表示无符号整数，可在后缀加上 u/U。此外还有进制的区别：

- 二进制整数前缀为 0b/0B
- 八进制整数前缀为 0，转换说明符为 o
- 十六进制整数前缀为 0x/0X，转换说明符为 x/X


<br>

### 浮点数

- float 为单精度浮点数，长 32 位，有 6-7 个有效数字，后缀为 f/F
    - 1 个符号位，8 个指数位，23 个尾数位
- double 为双精度浮点数，长 64 位，有 15-16 个有效数字，为默认类型
    - 1 个符号位，11 个指数位，52 个尾数位
- long double 为长双精度浮点数，至少长 128 位，后缀为 l/L
<br>

- 对于 scanf() 函数，float 使用 %f，double 使用 %lf，long double 使用 %Lf
- 对于 printf() 函数，float 和 double 使用 f/F/e/E/g/G，long double 还要额外加上 L 长度修饰符，l 会被忽略
    - e/E 表示使用指数形式，g/G 表示使用合适的形式，大写则表示使用指数形式时会使用大写字母
    - 当使用精度修饰符时，会自动四舍五入

浮点数的合法的写法有： .2, 100., .8E-5 (不能有空格出现), 0x0.1ap8 (等于 (0 + 1/16 + 10/256) * (2^8) = 26) 等


<br>

### 隐式类型转换

- char 和 short 在参与运算前，必须先转换为 int 或 unsigned int
- float 在参与运算前，必须先转换为 double
- 当有符号整数和无符号整数同时存在时，有符号整数会转换为无符号整数，具体做法是取模，如以下程序，其输出为 `-5 4294967291`：

```C
int a = -10;
unsigned int b = 5;
if (a + b > 0) {
    if ((-a) + b > 0) {
        printf("%d %u", a + b, a + b);
    }
}
```







<br>

## 运算符与表达式

- `/` 有符号数的除法的结果向零取整
- `%` 结果的符号取决于左操作数，例如 `-11 % ±5 = -1`
- `,` 返回最后一个表达式的值，若在函数调用中使用则必须在括号中
- `=` 左操作数必须为可修改的左值，返回右操作数的值
- `sizeof` 返回占用的字节数，类型名必须在括号中

<br>

### 运算符优先级

| 名称 | 运算符	| 结合律 |
| ---- | ----- | ----- |
|后缀运算符| []   ()   .   ->   |从左到右|
|一元运算符| ++ -- ! ~ + - * & sizeof (*type*)|**从右到左**|
|乘除法运算符| *    /    %	    |从左到右|
|加减法运算符| +    -	        |从左到右|
|移位运算符| <<    >>	        |从左到右|
|关系运算符| <  <=   >  >=      |从左到右|
|相等运算符| ==    !=	        |从左到右|
|位运算符 AND| &	            |从左到右|
|位运算符 XOR| ^	            |从左到右|
|位运算符 OR| &#124;	        |从左到右|
|逻辑运算符 AND| &&	            |从左到右|
|逻辑运算符 OR| &#124;&#124;	|从左到右|
|条件运算符| ? :	            |**从右到左**|
|赋值运算符| =  +=  -=  *=  /= %= &=  ^= &#124;= <<= >>=	|**从右到左**|
|逗号运算符| ,	                |从左到右|

- `int a=1,b=2,c=3,d=4`, `a<b?a:c<d?c:d = 1`
- `int i=101`, `(i++)/2 = 50`
- `char c ='w'`, `c+='A'-'a'=='W' ` 值为`'w'`，而非1
- `0xFFFFFFFD & 0xF == 13` 值为0，而非1
- `int x=-1`, `printf("%d",(unsigned int)x )` 输出为-1而非255，因为%d
- 取模只能用于整数

<br>

### 副作用与序列点

访问 volatile 对象、修改对象、修改文件或调用执行上述操作的函数，都会产生**副作用** (Side Effects)，即改变了执行环境的状态。

在执行序列中某些特定的点称为**序列点** (Sequence Points)，在此点之前的所有副作用都应已完成，后续求值的副作用还未发生。序列点会在 `&&`, `||`, `?`, `,` 的左侧产生。








<br>

##  字符串

- 使用字符串字面量初始化字符数组时，会复制该字符串字面量到数组中
- 使用字符串字面量初始化字符指针时，字符指针会指向该字符串字面量，该字符串字面量存在常量数据段中，不可修改

### string.h

```C
size_t strlen( const char *str )

int strcmp( const char *lhs, const char *rhs )
int strncmp( const char *lhs, const char *rhs, size_t count )

char *strchr( const char *str, int ch )
char *strrchr( const char *str, int ch )

char *strcat( char *restrict dest, const char *restrict src )
char *strncat( char *restrict dest, const char *restrict src, size_t count )

char *strcpy( char *restrict dest, const char *restrict src )
char *strncpy( char *restrict dest, const char *restrict src, size_t count )
```

- `strlen(str)` 返回字符串长度，不包括空字符
<br>

- `strcmp(lhs, rhs)` 以字典顺序比较两个字符串，若 lhs 小于 rhs 则返回负整数，大于则返回正整数，等于则返回零，具体值由编译器决定
- `strncmp(lhs, rhs, count)` 最多比较 count 个字符，若始终相等则返回零
<br>

- `strchr(str, ch)` 返回指向第一个 ch 的指针，若找不到则返回 NULL，ch 可为末尾空字符
- `strrchr(str, ch)` 返回指向最后一个 ch 的指针
<br>

- `strcat(dest, src)` 将 src 附加到 dest 末尾，并返回 dest 的副本，当目标数组不够长、两个字符串重叠、字符串无末尾空字符时，行为是未定义的
- `strncat(dest, src, count)` 最多复制 count 个字符，遇到空字符则会在复制完后停止，否则在复制完后还会额外复制一个空字符
<br>

- `strcpy(dest, src)` 将 src 复制到 dest，并返回 dest 的副本，当目标数组不够长、两个字符串重叠、字符串无末尾空字符时，行为是未定义的
- `strncpy(dest, src, count)` 最多复制 count 个字符，不会额外复制一个空字符

<br>

### stdio.h

```C
int sprintf( char *restrict buffer, const char *restrict format, ... )
int snprintf( char *restrict buffer, size_t bufsz,
              const char *restrict format, ... )

int sscanf( const char *restrict buffer, const char *restrict format, ... )
```

- `sprintf(buffer, format, ...)` 将格式化结果写入字符串 buffer，并额外附加一个空字符
- `snprintf(buffer, bufsz, format, ...)` 最多写入 bufsz - 1 个字符，并额外附加一个空字符
- `sscanf(buffer, format, ...)` 从字符串 buffer 格式化读取数据，并返回成功赋值的参数数量

<br>

### stdlib.h

```C
char *itoa( int value, char* str, int base)
char *ltoa( long value, char* str, int base)
char *ltoa( long long value, char* str, int base)

int atoi( const char *str )
long atol( const char *str )
long long atoll( const char *str )
double atof( const char* str )

long strtol( const char *restrict str, char **restrict str_end, int base )
long long strtoll( const char *restrict str, char **restrict str_end, int base )

float strtof( const char *restrict str, char **restrict str_end );
double strtod( const char *restrict str, char **restrict str_end );
long double strtod( const char *restrict str, char **restrict str_end );
```

- `itoa/ltoa/lltoa(value, str, base)` 将整数转换为指定进制的字符串
- `atoi/atol/atoll(str)` 将 str 转换为整数或浮点数，会抛弃所有前面的空白字符，然后取尽可能多的字符来表示一个有效结果，若转换失败则返回零
<br>

- `strtol/strtoll(str, str_end, base)` 将 str 转换为整数
    - `str_end` 指向字符指针，存储转换结束的位置，若为 NULL 则被忽略
    - `base` 可为 0 或 2~36，若为 0，则由整数的前缀决定相应进制
- `strtof/strtod/strtold(str, str_end)` 将 str 转换为浮点数

<br>

### ctype.h

```C
int isalnum( int ch )
int isalpha( int ch )
int isdigit( int ch )
int isxdigit( int ch )

int islower( int ch )
int isupper( int ch )

int isblank( int ch ) // ' ', '\t'
int isspace( int ch ) // ' ', '\n', '\r', '\t', '\v', '\f'

int ispunct( int ch ) // !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
int iscntrl( int ch ) // i.e. codes 0x00-0x1F and 0x7F

int isgraph( int ch ) // 检查给定字符是否具有图形表示
int isprint( int ch ) // 检查给定字符是否可以打印

int tolower( int ch )
int toupper( int ch )
```







<br>

## 数组与指针

### 定义

[] 和 () 的优先级高于 *，故下列定义依次为：

- `int * p[2]` 一个存储整数指针的数组
- `int (* p)[2]` 一个指向整数数组的指针
- `int * p[3][4]` 一个存储了 12 个整数指针的二维数组
- `int (* p)[3][4]` 一个指向二维数组的指针
- `int (* p[3])[4]` 一个数组，存储了 3 个指向长度为 4 的整数数组的指针
- `int (* pf[3])(char)` 一个数组，存储了三个指向函数的指针
<br>

- `const int * p` `int const * p` 指针指向的值为常量，但是可通过其他指针修改
- `int * const p` 指针为常量，不可指向其他值
- `const int * const p` 指针和指向的值皆为常量，不可修改
- 将带有 const 限定符的变量的地址，或指向常量的指针赋值给普通指针时，编译器会警告
<br>

- `int a[5][5][5]` 在类型转换中可写为 `int (*)[5][5]`，在函数原型中可写为 `int a[][5][5]` 或 `int (*a)[5][5]`

<br>

### 初始化

- `int a[5]` 不做初始化
- `int a[5] = {}` 全部初始化为 0
- `int a[5] = {1}` 部分初始化为指定值，剩余部分初始化为 0，超出部分无效且会报错
- `int a[] = {1, 2, 3, 4, 5}` 数组长度等于指定的元素个数
- `int a[] = {1, [3] = 1, 1}` 使用指定初始化器，该示例会被初始化为 `1 0 0 1 1`
- 多维数组初始化时，若元素被大括号包裹，则会自动扩充为对应长度的数组
<br>

- 数组在初始化后不可以被赋值，指针在初始化后还可以被赋值
- 在将函数赋值给函数指针时，& 是可选的
- 在通过函数指针调用函数时，* 是可选的
 








<br>

## 结构、联合与枚举
### 结构

- 结构体可作为参数传递，可作为返回值返回，还可赋值给另一个结构体，当结构体较大时最好使用结构体指针

#### 定义与初始化

```C
struct tag {
    member-list
} variable-list;

typedef struct LNode {
  int data;
  struct LNode *next;
} *List;
```

- 结构体的定义包括标签、成员列表和变量列表
- 结构体的定义可以在 typedef 中进行，但在使用自身作为成员时不能使用新别名作为类型名

结构也可以像数组一样，使用复合字面量进行初始化，复合字面量中也一样可以使用指定初始化器：

```C
struct Graph G = {
    4, 2,
    {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
    },
}
struct Graph G = {
    .col = 4, .row = 2,
    .G = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
    },
}
```

#### 伸缩型数组成员

```C
struct List {
    int length;
    int data[];
};

struct List *L = malloc(sizeof(struct List) + n * sizeof(int));
```

- 伸缩型数组成员必须是结构的最后一个成员，且不能为唯一的成员
- 伸缩型数组成员不占内存，使用前需要调用 malloc() 为结构体指针分配内存
- 有伸缩型数组成员的结构体最好不要用于传值、作为数组成员和作为结构体成员

#### 匿名结构

```C
struct Person  
{  
    int age;
    int weight;
    struct {  
      char firstName[20];
      char lastName[20];
    }; 
};  
```

- 可以像访问结构中的其他成员一样，直接访问匿名结构中的成员


<br>

### 联合

#### 定义与初始化

```C
union tag {
    member-list
} variable-list;
```
- 联合只能存储一个值
- 联合占用的内存足以存储联合中最大的成员
- 联合需要使用 `.` 来访问成员，成员的数据类型决定了怎样写入或读取
<br>

- `union Data a = {5}` 初始化联合的第一个元素
- `union Data a = {.num = 5}` 使用指定初始化器进行初始化

#### 匿名联合

```C
struct Person {
    char name[30];
    int age;
    union {
        char gender;
        int id;
    }
};
```

- 可以像访问联合中的其他成员一样，直接访问匿名联合中的成员


<br>

### 枚举

枚举类型用于定义一组具有整数值的常量，如下：

```C
enum {
    MON=1, TUE, WED, THU, FRI, SAT, SUN
} day;
// 1 2 3 4 5 6 7

enum color {red, orange, yellow=-2, green, blue, violet};
// 0 1 -2 -1 0 1
```

- 可以直接使用枚举中定义的标识符，如 `MON` `red`，这些都是常量，不可赋值
- 枚举值默认从 0 开始，后一枚举值为前面加一，可指定枚举值









<br>

## Storage, Linkage and Memory

### storage class

**scope**

- `block scope` : visible from the point it is defined until the end of the block containing the definition.
- `file scope` :  visible from the point it is defined to the end of the file containing the definition. File scope variables are also called global variables .
- `function scope` : applies just to labels used with goto statements. Even if a label first appears inside an inner block in a function, its scope extends to the whole function.
- `function prototype scope` : applies to variable names used in function prototypes, e.g. `void f(int n, int a[n]);`

**linkage**

- Variables with block scope, function scope, or function prototype scope have no linkage.
- `external linkage` : can be used anywhere in a multifile program.
- `internal linkage` : can be used anywhere in a single translation unit.

**storage duration**

- Scope and linkage describe the visibility of identifiers. Storage duration describes the persistence of the objects accessed by these identifiers.
- `automatic storage duration` : have memory allocated for them when the program enters the block in which they are defined, and the memory is freed when the block is exited.
    - Variable-length arrays provide a slight exception in that they exist from the point of declaration to the end of the block rather than from the beginning of the block to the end.
- `static storage duration` : exists throughout program execution.
    - For a variable to have block scope but static storage duration, exists from the time the program is loaded until the program terminates.
- `thread storage duration` : exists from when it’s declared until the thread terminates.
    - Such an object is created when a declaration that would otherwise create a file scope object is modified with the keyword `_Thread_local`.
    - When a variable is declared with this specifier, each thread gets its own private copy of that variable.
- `allocated storage duration` : exists from when the memory is allocated until it's freed, stored in **heap**.

### storage-class specifier

- `auto` : declare a varible belonging to automatic storage class(i.e. automatic varible) which has automatic storage duration, block scope, and no linkage.
    - automatic variables are not initialized unless you do so explicitly.
    - automatic varibles are stored in **stack**.

- `register`: declare a varible belonging to register storage class(i.e. register varible) which has automatic storage duration, block scope, and no linkage.
    - register variables are stored in the CPU registers or, more generally, in the fastest memory available, where they can be accessed and manipulated more rapidly than regular variables.
    - you can’t take the address of a register variable whether or not your request is approved.

- `static`: declare a varible belonging to static storage class(i.e. static varible) which has static storage duration. It has block scope and no linkage if declared in a block, or has file scope and internal linkage if declared outside of any function.
    - static variables and external variables are already in place after a program is loaded into memory and is initialized just once. It’s initialization statement won't execute during runtime.
    - can’t use `static` for function parameters
    - static variables are initialized to zero if you don’t explicitly initialize them to some other value.
    - static local varible can also hide global varible.
    - static varibles are stored in static memory.
    - define static function

- `extern`: declare a varible belonging to external storage class(i.e. external varible) which has static storage duration, file scope, and external linkage.
    - an external variable is created by placing a defining declaration outside of any function.
    - If a particular external variable is defined in one source code file and is used in a second source code file, declaring the variable in the second file with `extern` is mandatory.
    - an external variable can additionally be declared inside a function with `extern` to document your intention of using the static variable created previously instead of creating a new automatic varible.
    - declaration with `extern` does not cause space to be allocated, so don’t use the keyword to create an external definition
    - define external function which is default

- `_Thread_local` : may be used together with static and extern.
- `typedef` : doesn’t say anything about memory storage, but it is thrown in for syntax reasons.

### Dynamic memory management

```C
// Allocate size bytes of uninitialized storage.
void *malloc( size_t size );

// Allocate memory for a num * size array and initializes all bytes to zero.
void *calloc( size_t num, size_t size );

// Reallocates the given area of memory.
// It must be previously allocated by malloc(), calloc() or realloc().
// If ptr is NULL, the behavior is the same as calling malloc(new_size).
// If possible, the contents of the area remain unchanged.
// If the area is expanded, the contents of the new part are undefined.
void *realloc( void *ptr, size_t new_size );

// Deallocates the space previously allocated by malloc(), calloc() or realloc().
void free( void *ptr );
```


### Type Qualifier
- `const` : to share const data across files, can define global varibles with `static` in header
- `volatile` : tells the compiler that a variable can have its value altered by agencies other than the program, which facilitates compiler optimization.
    - A value can be both `const` and `volatile`.
- `restrict` : can be applied only to pointers, and it indicates that a pointer is the sole initial means of accessing a data object.
    - the compiler can’t check whether you obey this restriction.
- `_Atomic` : While a thread performs an atomic operation on an object of atomic type, other threads won’t access that object.








<br>

## File Input/Output

### File access
```C
// Opens a file indicated by filename and returns a pointer to the file stream.
// On error, returns a null pointer.
FILE *fopen( const char *restrict filename, const char *restrict mode );

// First, attempts to close the file associated with stream, ignoring any errors.
// Then, attempts to open the file specified by filename using mode,
// and associates that file with the file stream pointed to by stream.
// can be used to redirect files in program
FILE *freopen( const char *restrict filename, const char *restrict mode,
               FILE *restrict stream );

// Any unwritten buffered data are flushed to the OS.
// Any unread buffered data are discarded.
// ​0​ on success, EOF otherwise.
int fclose( FILE *stream );

// For output streams, writes any unwritten data from the stream's buffer to the associated output device.
// For input streams, the behavior is undefined.
// If stream is a null pointer, all open output streams are flushed.
// ​0​ on success, EOF otherwise.
int fflush( FILE *stream );

// Set the buffer for a file stream.
// If buffer is null, equivalent to setvbuf(stream, NULL, _IONBF, 0), which turns off buffering.
void setbuf( FILE *restrict stream, char *restrict buffer );

// Changes the buffering mode of the given file stream stream.
// _IOFBF	full buffering
// _IOLBF	line buffering
// _IONBF	no buffering
int setvbuf( FILE *restrict stream, char *restrict buffer,
             int mode, size_t size );
```

**File access flags**

|Mode string| Meaning | Explanation | If file already exists | If file does not exist |
|:--:| :---: | :---: | :---: | :---: |
|r | read	  |Open a file for reading  |	read from start	|failure to open|
|w | write  |Create a file for writing|	destroy contents|create new|
|a | append |Append to a file         |	write to end    |create new|
|r+| read extended  |Open a file for read/write   |	read from start| failure to open|
|w+| write extended |Create a file for read/write | destroy contents|create new|
|a+| append extended|Open a file for read/write   |	write to end|create new|

- File access mode flag `b` can optionally be specified to open a file in binary mode. This flag has no effect on POSIX systems, but on Windows it disables special handling of `\n` and `\x1A`.
- File access mode flag `x` can optionally be appended to `w` or `w+` specifiers. This flag forces the function to fail if the file exists, instead of overwriting it. (C11)
- In update mode (`+`), both input and output may be performed, but output cannot be followed by input without an intervening call to `fflush`, `fseek`, `fsetpos` or `rewind`, and input cannot be followed by output without an intervening call to `fseek`, `fsetpos` or `rewind`, unless the input operation encountered end of file. In update mode, implementations are permitted to use binary mode even when text mode is specified.



### Input/Output

**Direct input/output**

```C
// In Windows, need to open file in binary mode

// Read count objects into the array buffer from the given input stream stream.
// Return the number of objects read successfully.
size_t fread( void *restrict buffer, size_t size, size_t count,
              FILE *restrict stream );

// Write count of objects from the array buffer to the output stream stream.
// Return the number of objects write successfully.
size_t fwrite( const void *restrict buffer, size_t size, size_t count,
               FILE *restrict stream );


double old[1] = {3.6};
double new[1] = {};
FILE * fo = fopen("aaa.txt", "wb");
fwrite(old, 8, 1, fp);
rewind(fp);
fread(new, 8, 1, fp);
printf("%lf\n", new[0]);
```

**Unformatted input/output**

```C
// Reads the next character from the given input stream.
// On success, returns the obtained character as an int. On failure, returns EOF.
int fgetc( FILE *stream );

// Writes a character ch to the given output stream stream.
// On success, returns the written character. On failure, returns EOF.
int fputc( int ch, FILE *stream );

// Read at most count - 1 characters from the given file stream.
// Stop if '\n' is found, in which case str will contain '\n', or if EOF occurs.
// Write a null character immediately after the last character written to str.
// Return str on success, null pointer on failure.
char *fgets( char *restrict str, int count, FILE *restrict stream );

// Writes every character from the null-terminated string str to the stream.
// The terminating null character from str is not written.
// On success, returns a non-negative value. On failure, returns EOF.
int fputs( const char *restrict str, FILE *restrict stream );

// If ch is not EOF, push ch into the input buffer associated with the stream.
// On success ch is returned. On failure EOF is returned.
int ungetc( int ch, FILE *stream );
```
```C
// Reads stdin into the character array pointed to by str.
// Stop if a newline character is found or end-of-file occurs.
// Write a null character immediately after the last character written to str.
// The newline character is discarded but not stored in the buffer.
char *gets( char *str );

// Reads characters from stdin until a newline is found or end-of-file occurs.
// Writes only at most n-1 characters into the array.
// The newline character, if found, is discarded.
// Return str on success, a null pointer on failure.
char *gets_s( char *str, rsize_t n );

// Writes every character from str and one additional '\n' to the stdout.
// The terminating null character from str is not written.
// On success, returns a non-negative value. On failure, returns EOF.
int puts( const char *str );
```

**Formatted input/output**
```C
int fscanf( FILE *restrict stream, const char *restrict format, ... );
int fprintf( FILE *restrict stream, const char *restrict format, ... );
```

### File positioning

```C
// Returns the file position indicator for the file stream stream.
// In binary mode, return the number of bytes from the beginning of the file.
// In text mode, what return is unspecified and only meaningful in fseek().
long ftell( FILE *stream );

// Sets the file position indicator to the value pointed to by offset.
// origin can have one of the following values: SEEK_SET, SEEK_CUR, SEEK_END.
// offset can be negative value, e.g. -5L
int fseek( FILE *stream, long offset, int origin );

// Moves the file position indicator to the beginning of the given file stream.
void rewind( FILE *stream );
```

### Others
```C
// Checks if the end of the given file stream has been reached.
// nonzero value if the end of the stream has been reached, otherwise ​0​.
int feof( FILE *stream );
// Checks the given stream for errors.
// Nonzero value if the file stream has errors occurred, ​0​ otherwise.
int ferror( FILE *stream );
// Prints a textual description of the error code stored in errno to stderr.
void perror( const char *s );

// Deletes the file identified by character string pointed to by fname.
int remove( const char *fname );
// Changes the filename of a file.
int rename( const char *old_filename, const char *new_filename );
```









<br>

## Bit manipulation

### Bitwise operator

- Bitwise Negation: `~`
- Bitwise AND: `&`
    - Mask, `a & MASK`
    - Reset bits, `a & ~MASK`
    - Check bits, `a & MASK == MASK`
- Bitwise OR: `|`
    - Set bits, `a | MASK`
- Bitwise EXCLUSIVE OR: `^`
    - Toggle bits, `a ^ MASK`
- Bitwise Left Shift Operator: `<<`
    - operand must have integral type
    - for type smaller than int, shift as int and return int
    - fill 0 on the right
- Bitwise Right Shift Operator: `>>`
    - operand must have integral type
    - for type smaller than int, shift as int and return int
    - for unsigned type, fill 0 on the left
    - for signed type, fill sign on the left

### Bit field

```C
struct {
    unsigned field1 : 1;
    unsigned        : 2;
    unsigned field2 : 1;
    unsigned        : 0;
    unsigned field3 : 1;    //field3存储在下一个unsigned int中
} bit, *pbit;

bit.field1 = 1;
pbit->filed3 = 0;
```

- 字段不允许跨越两个unsigned int 之间的边界，编译器会自动移动跨界的字段
- 可用未命名字段填充未命名的“洞”
- 可用宽度为0的未命名字段迫使下一个字段与下一个整数对齐

### Align

_Alignas
_Alignof







<br>

## C预处理器

### 翻译处理

在预处理之前，编译器会先对程序进行翻译处理：

- 首先，将源代码出现的字符映射到源字符集，该过程处理多字节字符和三字符序列
- 第二，定位每个反斜杠后面出现换行符的实例，并将其删除，将物理行转换为逻辑行，使表达式成为一行
- 将文本划分成预处理记号序列、空白序列和注释序列。编译器用一个空格字符替换每一条注释，预处理指令中的注释将会被替换

### 预处理器指令

- 定义从定义处至文件末尾有效
- 从`#`开始，到第一个换行符为止
- 分为对象宏、类函数宏和空宏
- 由三部分组成：
    - 预处理指令，如`#define`
    - 宏：不允许有空格，只能使用字母、数字和下划线，首字符不能是数字。分为类对象宏和类函数宏
    - 替换列表/替换体
<br>

### #define
#### 类函数宏

```C
#define SQUARE(X) ((X)*(X))
#define PSQR(X) printf("the square of " #X " is %d\n", ((X)*(X)))
```

- 分为宏标识符（如`SQUARE`），宏参数（如`X`）和替换列表（如`((X)*(X))`）
- 双引号中的宏不会被替换，但可用预处理运算符`#`将记号转换为字符串

#### ##运算符

```C
#define XNAME(n) x ## n
#define PRINT_XN(n) printf("x" #n " = %d\n", x ## n)
```

- 可用于类函数宏和对象宏，起记号粘合剂的作用

#### 变参宏

```C
#define PR(X, ...) printf("Message " #X ": " __VA_ARGS__)

PR(1, "x = %.2f, y = %.4f\n", x, y);
```

- 省略号只能代替最后的宏参数

#### 预定义宏和预定义标识符

```C
__FILE__    //当前文件名
__DATE__    //预处理的日期
__TIME__    //翻译代码时的时间
__LINE__    //当前所处行号
__func__    //当前所处函数
__STDC_VERSION__  //支持C99标准，设置为199901L；支持C11标准，设置为201112L
```


### #include

```C
#include <stdio.h>          //查找系统目录
#include "hot.h"            //查找当前工作目录
#include "usr/biff/p.h"     //查找指定目录
```

### 其他指令

**取消定义**

```C
//取消定义。即使原来没有定义过LIMIT，取消LIMIT的定义仍然有效
#undef LIMIT
```

**条件编译**

```C
#ifdef MAVIS
    #include "horse.h"
    #define STABLES 5
#else
    #include "cow.h"
    #define STABLES 15
#endif
```

```C
//可用于防止包含头文件导致重复定义
#ifndef SIZE
  #define SIZE 100
#endif
```

```C
#if SYS == 1
    #include "ibmpc.h"
#elif SYS == 2
    #include "vax.h"
#elif SYS == 3
    #include "mac.h"
#else
    #include "general.h"
#endif
```

**#line 和 #error**

```C
//重置__LINE__和__FILE__
#line 1000
#line 10 "cool.h"

#if __STDC_VERSION__ != 201112L
  #error Not C11
#endif
```

**#pragma**

```C
//编译指示
#pragma nonstandardtreatmenttypeB on

//_Pragma运算符
#define PRAGMA(X) _Pragma(#X)
#define LIMRG(X) PRAGMA(STDC CX_LIMITED_RANGE X)
```

**泛型**

```C
//第一个项的类型匹配哪个标签，整个表达式的值就是该标签后面的值
#define MTYPE(X) _Generic((X),\
    int: "int",\
    float: "float",\
    double: "double",\
    default: "other"\
)
```








<br>

## C functions

### printf()

```C
int printf(const char *format, ...)
// Return number of characters transmitted to the output stream.
// Or return negative value if an output error or an encoding error occurred.
// float arguments are always promoted to double when used in a varargs call.

// Format placeholder syntax
%[flags][width][.precision][length]type

// flags field
-   Left-align the output of this placeholder.
+   Prepends a plus for positive signed-numeric types.
space   Prepends a space for positive signed-numeric types.
0   When the 'width' option is specified, prepends zeros for numeric types.
''  The integer or exponent of a decimal has the thousands grouping separator 
    applied.
#   For g and G types, trailing zeros are not removed.
    For f, F, e, E, g, G types, the output always contains a decimal point.
    For o, x, X types, the text 0, 0x, 0X, respectively, is prepended to non-
    zero numbers.

// width field
Specify a minimum number of characters to output
// precision field
specify a maximum limit on the output.
For floating-point types, it specifies the number of digits of mantissa.
For the string type, it limits the number of characters.
The precision field can be a dynamic value with '*'.
For example, printf("%.*s", 3, "abcdef") will result in "abc".

// length field
hh	For integer types, expect an int-sized integer promoted from a char.
h	For integer types, expect an int-sized integer promoted from a short.
l	For integer types, expect a long-sized integer argument.
        For floating-point types, this is ignored.
ll	For integer types, expect a long long-sized integer argument.
L	For floating-point types, expect a long double argument.
z	For integer types, expect a size_t-sized integer argument.
j	For integer types, expect a intmax_t-sized integer argument.
t	For integer types, expect a ptrdiff_t-sized integer argument.

// type field
d, i	int as a signed integer. %i will interpret a number as hexadecimal if 
        it's preceded by 0x, and octal if it's preceded by 0.
u	Print decimal unsigned int.
f, F	double in normal (fixed-point) notation.
        inf, infinity and nan for f
        INF, INFINITY and NAN for F.
e, E	double value in standard form (d.dde±dd or d.ddE±dd).
g, G	double in either normal or exponential notation, whichever is more 
        appropriate for its magnitude.
a, A	double in hexadecimal notation, starting with 0x or 0X.
x, X	unsigned int as a hexadecimal number.
o	unsigned int in octal.
s	null-terminated string.
c	char (character).
p	void* (pointer to void) in an implementation-defined format.
n	Print nothing, but writes the number of characters written so far into 
        an integer pointer parameter.
```

### scanf()

```C
int scanf(const char *format, ...)
// Return number of receiving arguments successfully assigned.
// Or return EOF if input failure occurs before the first argument was assigned.

// Format placeholder syntax
%[*][width][modifiers]type

[*] indicates the data read from the stream will be omitted
[width] specifies the maximum chars read from the stream

// type field
[set]	matches a non-empty sequence of character from set of characters.
        If the first character of the set is ^, then all characters not in the 
        set are matched. If the set begins with ] or ^] then the ] character 
        is also included into the set. It is implementation-defined whether the 
        character - in the non-initial position in the scanset may be indicating 
        a range, as in [0-9]. If width specifier is used, matches only up to 
        width.
n	returns the number of characters read so far.
```

### memcpy(), memmove()

```C
// in string.h

void* memcpy(void *restrict dest, const void *restrict src, size_t count)
// Copy [count] chars from src to dest as unsigned char array.
// the behavior is undefined if the objects overlap. 
// The behavior is undefined if access occurs beyond the end of the dest array.
// The behavior is undefined if either dest or src is an invalid or null pointer.

void* memmove(void* dest, const void* src, size_t count);
// Copy [count] chars from src to dest as unsigned char array.
// The objects may overlap.
// The behavior is undefined if access occurs beyond the end of the dest array.
// The behavior is undefined if either dest or src is an invalid or null pointer.
```

### qsort(), bsearch()

```C
// in stdlib.h

void qsort( void *ptr, size_t count, size_t size,
            int (*comp)(const void *, const void *) )
// Sorts the array pointed to by ptr in ascending order.
// If comp indicates two elements as equivalent, their order is unspecified.

void* bsearch( const void *key, const void *ptr, size_t count, size_t size,
               int (*comp)(const void*, const void*) );
// Finds an element in an ascending array pointed to by ptr.
// Return the pointer to an element equal to *key, or null pointer if not found.


// Example:
int comp(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}

int a[5] = {2, 1, 4, 5, 3};
qsort(a, 5, sizeof(int), comp);

int key = 3;
int *res = bsearch(&key, a, 5, sizeof(int), comp);
```

### rand(), srand()

```C
// Returns a pseudo-random integer value between ​0​ and RAND_MAX
// If rand() is used before any calls to srand(), rand() behaves as if it was seeded with srand(1).
int rand();

// Seeds the pseudo-random number generator used by rand() with the value seed.
void srand( unsigned seed );
```







<br>

## C libaries

### time.h

```C
time_t time(time_t *seconds)
// Returns the seconds since the Epoch (00:00:00 UTC, January 1, 1970).
// If seconds is not NULL, the return value is also stored in variable seconds.

clock_t clock(void)
// Returns the number of clock ticks elapsed since the program was launched
```

```C
//accurate to seconds
time_t start = time(NULL);
Sleep(1000);
time_t end = time(NULL);
printf("time = %lf\n", difftime(end, start));   //in time.h

//accurate to milliseconds
clock_t start = clock();
Sleep(1000);
clock_t end = clock();
printf("time = %lf\n",(double)(end-start)/CLK_TCK);
```

### windows.h

```C
void Sleep(DWORD dwMilliseconds)
// Suspend the current thread for a specific time
// In Windows, the argument is milliseconds

QueryPerformanceFrequency(&num);
// Retrieve the frequency of the performance counter.
QueryPerformanceCounter(&num); 
// Retrieve the current value of the performance counter,
```
```C
//accurate to microseconds
LARGE_INTEGER num;
QueryPerformanceFrequency(&num);
long long freq = num.QuadPart;

QueryPerformanceCounter(&num); 
long long start = num.QuadPart; 
Sleep(1000);
QueryPerformanceCounter(&num); 
long long end = num.QuadPart;

printf("time = %lf\n",(double)(end - start)/freq);
```

### sys/time.h

```C
int gettimeofday(struct timeval*tv, struct timezone *tz)
// Return the number of seconds and microseconds since the Epoch.

struct timeval{
    long int tv_sec;  //seconds
    long int tv_usec; //microseconds
}
```

```C
//accurate to microseconds
struct timeval start, end;

gettimeofday(&start, NULL);
Sleep(200);
gettimeofday(&end, NULL);

long timeuse = 1000000*(end.tv_sec - start.tv_sec) + end.tv_usec - start.tv_usec;
printf("time = %lf\n", timeuse/1000000.0);
```









