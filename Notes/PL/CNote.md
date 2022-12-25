[toc]






## Date type
#### char
```C
char c1 = 255;
char c2 = 257;
printf("%d\n", c1);
printf("%d\n", c2);
// output:
// 1
// -1
```

**ASCII**
| Dec | Hex | Glyph |
| :-: | :-: | :---: |
| 48  | 30  | 0 |
| 57  | 39  | 9 |
| 65  | 41  | A |
| 90  | 5A  | Z |
| 97  | 61  | a |
| 122 | 7A  | z |
| 32  | 20  | space |

| Dec | Hex | Escape sequence |
| :-: | :-: | :---: |
| 0   | 00  | \0 |
| 8   | 08  | \b |
| 9   | 09  | \t |
| 10  | 0A  | \n |
| 13  | 0D  | \r |


#### int
**bytes**
`short` : 16 (-32768 ~ 32767)
`int` : 32 (-2147483648 ~ 2147483647)
`long` : 32(mycom) or 64(PTA)
`long long` : 64

2^16 = 65536
2^32 = 42,9496,7296
2^64 = 1844,6744,0377,0951,1616

**prefix and suffix**
- `Binary` : 0b or 0B
- `Octal` : 0
- `Hexadecimal` : 0x or 0X
<br>

- `long` : l or L
- `long long` : ll or LL
- `unsigned long long` : ull or LLU or ULL



#### float
**bytes**
- `float` : 32 bits, 6-7 significant figures
  - 1 sign, 8 exponent, 23 mantissa
- `double` : 64 bits, 15-16 significant figures
  - 1 sign, 11 exponent, 52 mantissa
- `long double` : 128 bits, 18-19 significant figures
  - 1 sign, 15 exponent, 112 mantissa

**format and suffix**
- `.2`
- `100.`
- `.8E-5` (can't exist space)
- `0x0.1ap8` (this is (0 + 1/16 + 10/256) * (2^8) = 26)
<br>

- `3.666` : double
- `3.666f` or `3.666F` : float
- `3.666l` or `3.666L` : long double

**others**
- `%.2f` can be used to round off. For example, 9.999 becomes 10.00, but 9.99 is still 9.99
- `NAN(Not A Number)` or `IDN(Indeterminate Number)` : `0.0/0.0`
- `INF(Infinity)` : `1.0/0.0` or `-1.0/0.0`
- `DEN(Denomarlized)` : `0.01E-305`


#### Implicit type conversion
- automatic type conversion will take place when more than one data type is present in an expression
- `char` and `short` will be promoted to `int` or `unsigned int` before operation
- `float` will be promoted to `double` before float operation
- when signed and unsigned int are both involved, signed int will be converted to unsigned int
- smaller to larger: `bool -> char -> short -> int -> `
  `unsigned int -> long -> unsigned long -> `
  `long long -> float -> double -> long double`
```C
int main() {
    int a = -10;
    unsigned int b = 5;
    if (a + b > 0) {
        if ((-a) + b > 0) {
            printf("%d\n", a + b);
        }
    }
}
// output:
// -5
```





---
## Operators and Expressions
- `/` : Signed integer division truncates towards zero, i.e. `5/-2 = -2`
- `%` : The sign of the result is the same as the left-hand operand, i.e. `-11 % ±5 = -1`
- `-` : If the operand of negative operator `-` is an unsigned data type, the result will be the maximum value of the unsigned data type, minus the value of the operand.
- `sizeof` : Return the bytes of the data type of its operand. It must be enclosed in parentheses when the operand is a type name.
- `,` : Return the value of the last expression. It must be enclosed in parentheses when used in function call.

#### Operator precedence
|Description|Operator|Associativity|
| :---: | :---: | :---: |
| Suffix | ++ -- []   ()   ·   -> |Left-to-right|
| Prefix | ++ -- ! ~ + - * & sizeof (*type*) _Alignof |**Right-to-left**|
| Multiple and divide | * / % |Left-to-right|
| Plus and Minus | +    -	        |Left-to-right|
| Bitwise shift | <<    >>	        |Left-to-right|
| Relational | <  <=   >  >=      |Left-to-right|
| Renational | ==    !=	        |Left-to-right|
| Bitwise AND | &	            |Left-to-right|
| Bitwise XOR | ^	            |Left-to-right|
| Bitwise OR | &#124;	        |Left-to-right|
| Logical AND | &&	            |Left-to-right|
| Logical OR | &#124;&#124;	|Left-to-right|
| Ternary conditional | ? :	            |**Right-to-left**|
| Assignment | =  +=  -=  *=  /= %= &=  ^= &#124;= <<= >>=	|**Right-to-left**|
| Comma | ,	                |Left-to-right|


#### Side effects
- Accessing a `volatile` object
- Modifying an object
- Modifying a file
- A call to a function which performs any of the above side effects


#### Sequence points
All the side effects of previous expression evaluations must be complete at a sequence point.

- A call to a function (after argument evaluation is complete)
- The end of the left-hand operand of the `&&`
- The end of the left-hand operand of `||`
- The end of the left-hand operand of `,`
- The end of the first operand of `a ? b : c`
- The end of an initialisation expression
- The end of an expression statement (i.e. an expression followed by `;`)
- The end of the controlling expression of an `if` or `switch` statement
- The end of the controlling expression of a `while` or `do` or `for` statement
- The end of the expression in a return statement
- Immediately before the return of a library function
- After the actions associated with an item of formatted I/O
- Immediately before and after a call to a comparison function (as called for example by `qsort`)






---
## Statements

**switch statement**
- All of the expressions compared must be of a constant integer type (e.g., a literal integer or an expression built of literal integers).
```C
switch(test){
    case constant-expression :
       statement;
    case constant-expression :
       statement;
    ...
    default :
       statement;
}
```

**do statement**
```C
do
  statement
while (test);
```

**goto statement**
- Unconditionally jump to the place of a specified label in the same function
- Label names do not interfere with other identifier names

**break statement**
- If the break statement is inside of a loop or switch statement which itself is inside of a loop or switch statement, the break only terminates the innermost loop or switch statement.

**continue statemnet**
- Used in loops to jump to test
- If the a continue statement is inside a loop which itself is inside a loop, then it affects only the innermost loop.





---
##  ***字符串及字符串函数***

- 字符串最后一个字符为NULL，最大strlen比size小1
- `char s[]` 不可改变s指向的地址，且会将静态存储区中的字符串拷贝到数组中，产生一个副本
- `char *s` 直接指向静态存储区的字符串，可以改变指向地址，但修改指向地址的值的行为是未定义的，最好使用`const`限定符

#### 字符串函数
```C
gets(char*)     //读取整行输入，并丢弃换行符。可能导致缓冲区溢出
                //若读到文件末尾返回空指针NULL
puts(char*)     //只显示字符串，并加上换行符

fgets(str, n, stdin)    //str必须被分配内存
                        //读入n-1个字符，遇到换行符停止，会读入换行符
                        //若读到文件末尾返回空指针NULL
fputs(str, stdout)      //不会附加换行符

scanf()     //遇到空白字符停止，不会读入空白字符
            //若数组大小为6，则应使用%5s最多读入5个字符
```
```C
strlen()

strcat(s1, s2)      //s1附加s2的备份，s2不变
strncat(s1, s2, n)  //防止数组溢出，n最大为sizeof(s1)-strlen(s1)-1

strcmp(s1, s2)      //(mingw)看第一个不同的字符，若s1在前则返回-1，若s1在后则返回1
strncmp(s1, s2, n)  //比较前n个字符

strcpy(s1, s2)      //将源字符串(s2)拷贝到目标字符串(s1)，返回第一个参数的值
strncpy(s1, s2, n)  //n为可拷贝的最大字符数，若s2第n个不是空字符，则副本不会包含空字符

strchr(str, c)      //若包含c字符，则返回str字符串首位置指针，否则返回空指针
strrchr(str, c)     //返回c字符最后出现的位置（末尾的空字符也属于字符串）
```
```C
sprintf(str,"...",...)  //在stdio.h中，将格式字符串储存到str

atoi(str)   //在stdlib.h中，将str开头数字部分转化为整型返回，若开头无数字则返回0
itoa(num, str, n)   //在stdio.h中，将整型转化为n进制字符串后储存到str

strtol(str, char ** end, n) //在stdlib.h中，转化为long，n最大为36
                            //end指向最后一位有效位数后一个字符
strtoul(str, char ** end, n)    //在stdlib.h中，转化为unsigned long
strtod(str, char ** end)    //在stdlib.h中，转化为double
```

#### ctype.h

###### 字符测试函数
```C
isalpha()
isdigit()
isxdigit()
isalnum()

islower()
isupper()

isblank()  //空格或制表符
isspace()  //所有空白字符：空格，水平制表符，换行符，垂直制表符'\v'，提要'\f'，回车'\r'

isgraph()  //除空格之外的可打印字符
ispunct()  //除空格和字母数字之外的可打印字符

iscntrl()  //控制字符，Ascii码为0-31
```
###### 字符映射函数
```C
tolower()
toupper()
```




---
## ***数组与指针***

- 数组名表示的是“常量”，不是可修改的左值
- 左值为指向对象的表达式

#### 初始化数组
```C
a[5] = {1, 2, 3};       //1 2 3 0 0
a[5] = {1};             //1 0 0 0 0
a[5] = {0};             //0 0 0 0 0
a[5] = {};              //0 0 0 0 0
a[5];                   //8 0 41 0 10359760
a[] = {1, 2, 3};        //1 2 3 3 12391344

a[5] = {1, 2, 3, 4, 5, 6};
//warning: excess elements in array initializer
a[10] = {1, 2, [4] = 3, 4, 5, [1] = 6, 7};
//1 6 7 0 3 4 5 0 0 0  
```
```C
a[][2] = {1,2,3,4,5};
//1 2
//3 4
//5 0
a[5][5] = 
{
    {1, 2, 3, 4, 5}, 
    {1, 2, 3, 4},
    {1, 2, 3},
    [1] = {1, 2},
    {1}
};
//1 2 3 4 5 
//1 2 0 0 0
//1 0 0 0 0
//0 0 0 0 0
//0 0 0 0 0
```
 
#### 指针运算
- `a == &a[0]`
- `a + 2 == &a[2]`
- `*(a + 2) == a[2]`
- 指针求差得元素距离,可得负数
- 相同类型指针可比较

#### const指针
- 可用`const`关键字声明数组为只读数组，但若const数组名作为实参传递给函数，导致const数据被修改，这样的结果是未定义的
- 可在函数定义中用`const`关键字避免数组被修改
- 不能通过const指针改变其指向地址的值，但可以改变const指针的指向地址
- 可用普通指针改变const指针指向地址的值
- const指针可指向const数据或非const数据的地址
- 普通指针只能指向非const数据的地址
- `int * const p` 可修改指针指向地址的值，但不可修改指针的值
- `const int * const p` 既不可修改指针指向地址的值，又不可修改指针的指向地址

#### 函数指针
```C
void ToUpper(char *);
void (*pf)(char *);
pf = ToUpper;  //函数名代表函数的地址（代码起始处）

char * str = "hello word";
*pf(str);
pf(str);    //两种语法皆可用
```
- 函数指针指向函数代码起始处
- 声明函数指针时，要指明函数签名，即函数的返回类型和形参类型

#### 复杂的声明
```C
[]和()优先级相同，从左往右结合，优先级高于*，先与[]结合表明是数组，先与*结合表明是指针

int * p[10]     //声明一个指针数组
int (* p)[10]   //声明一个指向数组的指针
int * p[3][4]   //声明一个二维指针数组
int (* p)[3][4] //声明一个指向二维数组的指针
int (* p[3])[4] //声明一个内含三个指针元素数组，每个指针指向int数组
int (* pf[3])(char) //声明一个指针数组，每个指针指向返回值为int的函数
```








---
## ***内存***

#### 作用域
- **块作用域**：为用花括号括起来的区域，变量的可见范围是从定义处到包含该定义的块的末尾。内层块会隐藏外层块的含义
- **文件作用域**：变量定义在函数外，也称为全局变量，可见范围是从定义处到文件末尾。只能使用常量表达式初始化文件作用域变量，不能用之前声明的全局变量来初始化，除非其有`const`限定符
- 函数作用域：仅用于goto语句的标签，即标签出现在函数的内层块中，它的作用域也延伸至整个函数
- 函数原型作用域：范围是从形参定义处到原型声明结束

#### 链接
- 外部链接：可延伸至其他翻译单元的作用域
- 内部链接：仅限于一个翻译单元
- 无链接：具有**块作用域**、**函数作用域**或**函数原型作用域**的变量

#### 存储期
- **自动存储期**：进入块时分配内存，退出块时释放内存
- **静态存储期**：在程序执行期间一直存在
- 线程存储期：从声明时到线程结束一直存在。关键字_Thread_local使每个线程获得声明变量的私有备份
- 动态分配存储期

#### 存储类别说明符
`auto`: 声明自动变量（自动存储类别）
- 具有自动存储期、块作用域和无链接
- 主要用于明确表达要使用与外部变量同名的局部变量
- 不会初始化，除非显式初始化，可使用非常量表达式

`register`: 声明寄存器变量（寄存器存储类别）
- 具有自动存储期、块作用域和无链接
- 可请求储存在CPU的寄存器中
- 不能获取寄存器变量的地址，无论是否请求成功

`static`: 声明静态变量（静态存储类别）
- 无论在何处声明，都会在程序被载入内存时执行完毕，不会在运行时执行
- 声明在块内，则为块作用域的静态变量，即局部静态变量（内部静态存储类别），无链接
- 若声明在所有函数外，则为内部链接的静态变量，具有文件作用域，**内部链接**
- 若未显式初始化，则会被初始化为0，即使是局部变量

`extern`: 声明外部变量（外部存储类别）
- 外部变量声明在所有函数外，具有静态存储期、文件作用域和**外部链接**
- 是**引用式声明**，而非定义式声明，指示编译器去别处查找其定义，不会分配存储空间。因此，若定义外部变量，则不可使用extern
- 可在函数中使用extern关键字，重复声明文件作用域变量，但不会改变其链接属性
- 若未显式初始化，则会被初始化为0。只有定义式声明才能初始化

#### 存储类别和函数
函数可分为外部函数和静态函数，一般默认为外部函数
- `static`: 用于说明该函数归特定模块，可避免名称冲突，使其他文件可使用同名函数
- `extern`: 用于声明定义在其他文件的函数，表明该函数被定义在别处

#### 动态分配内存
`malloc(n * sizeof(int))`: 返回动态分配内存块的首字节地址，类型为 void *（指向void的指针），通常要进行强制类型转换；若分配内存失败，会返回空指针

`calloc(n, sizeof(int))`: 还会初始化内存块中所有位为0

`free()`: 用于释放之前`malloc()`和`calloc()`分配的内存

```C
int (* p)[m] = (int (*)[m]) malloc(n * m * sizeof(int));
//声明n×m数组
```

#### 类型限定符
`const`: 若使用头文件共享全局数据且禁止修改，应使用`static const`，以防止每个包含该头文件的文件拥有一个相同标识符的定义式声明

`restrict`: 限定声明的指针是访问内存唯一且初始的方式，方便编译器优化

`volatile`: 告知计算机代理可以修改该变量的值，使编译器假定两条语句之间声明的变量发生了变化

`_Atomic`







---
## ***文件***

#### 文件结束信号
- Windows: Ctrl + Z + Enter
- Unix, Linux: Ctrl + D + Enter

#### 重定向
- 重定向运算符: `<` and `>`
- 不能读取多个文件的输入，也不能将输出定向至多个文件

### 标准文件
标准输入文件通常为键盘，文件指针为stdin
标准输出文件通常为显示器，文件指针为stdout
标准错误文件通常为显示器，文件指针为stderr

#### 退出文件
`exit()`函数关闭所有打开的文件并结束程序
- 可在其他函数调用
- 在最初调用的`main()`函数中与return语句效果相同
- 退出失败为`exit(EXIT_FAILURE)`

#### 打开文件和关闭文件
```C
fopen(filename, "r")    //只读模式，不存在则打开失败
fopen(filename, "w")    //写入模式，文件存在截为0，若不存在则新建
fopen(filename, "a")    //追加模式，文件存在追加末尾，若不存在则新建

fopen(filename, "r+")   //更新模式，可读可写，不存在则打开失败
fopen(filename, "w+")   //写入更新模式，文件存在截为0，若不存在则新建
fopen(filename, "a+")   //追加更新模式，文件存在追加末尾，若不存在则新建

//以文本模式打开（默认）
fopen(filename, "..t")
fopen(filename, "..t+")
fopen(filename, "..+t")

//以二进制模式打开
fopen(filename, "..b")
fopen(filename, "..b+")
fopen(filename, "..+b")

fclose(fp)  //成功关闭放回0，否则返回EOF
```
`fopen()`返回文件指针（FILE *），不指向实际文件，指向一个包含文件信息的数据对象

#### 处理文件
###### 输入输出
```C
ch = getc(fp)       //从fp指定的文件获取一个字符
putc(ch, fp)        //将字符放入FILE指针指定的文件

fprintf(fp, "...", ...)
fscanf(fp, "...", ...)

fgets(str, n, fp)   //在读到换行符，或读到文件末尾，或读完n-1个字符后停止
                    //读到换行符时，会保留换行符并给str加上空字符
                    //遇到EOF时，会返回Null值
                    //读完n-1个字符后，会给str末尾加上空字符
fputs(str, fp)  //不会加上换行符
```
- 所有的标准I/O输入函数使用相同的缓冲区，调用任何一个函数都将从上次函数停止调用的位置开始
- 读完缓冲区所有字符后，会请求拷贝下一个缓冲大小的数据块到缓冲区

###### 定位
```C
rewind(fp)      //让程序回到文件开始处

fseek(fp, 2L, SEEK_SET)     //从文件开始处前进2个字节
fseek(fp, 0L, SEEK_CUR)     //定位至文件当前位置
fseek(fp, -5L, SEEK_END)    //从文件结尾处回退5个字节
若一切正常则返回0，若发生超出文件范围等错误则返回-1

n = ftell(fp)   //返回当前的位置，类型为long
```

###### 其他标准I/O函数
```C
ungetc(ch, fp)  //将一个字符放回输入流

fflush(fp)      //刷新缓存区，将缓存区所有未写入的数据发送到fp指定的输出文件
setvbuf(fp, buf, mode, size)    //创建缓冲区

fwrite(void *ptr, size_t size, int nmemb, FILE *fp)
//把二进制数据从ptr指向的数据块写进文件，size为元素大小，nmemb为元素个数
fread(void *ptr, size_t size, int nmemb, FILE *fp)
//把二进制数据从文件读进ptr指向的数据块，并返回成功读取的项的个数

feof(fp)    //当上一次输入调用检测到文件结尾时，返回非零值，否则返回0
ferror(fp)  //当读写出现错误时，返回非零值，否则返回0
```





---
## ***结构和其他数据形式***

#### 结构类型
- 结构可以赋值给另一个结构，数组不可以赋值给另一个数组
- 结构可以所谓参数传递，也可以作为返回值返回
- 复合字面量即可用于数组，又可用于结构，可以在复合字面量中使用指定初始化器

###### 定义结构变量
```C
//带标记的结构模板
struct book {
    char title[N];
    char author [N];
    int value;
};

//将结构变量定义和声明结构结合，因无结构标记，后面不能再次声明
struct {
    char title[N];
    char author [N];
    int value;
} bookA, bookB;
```
###### 初始化结构
```C
struct Graph G = {
    4, 2,
    {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
    },
}
struct Graph G = {  //指定初始化器
    .col = 4,
    .G = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
    },
    .row = 2,
}
```
###### 伸缩型数组成员
```C
struct List {
    int n;
    int data[];
};

struct List *L = malloc( sizeof(struct List) + n*sizeof(int) );
```
- 伸缩数组必须是结构最后一个成员
- 方括号是中空的
- 带伸缩型数组成员的结构不可赋值、拷贝、传递
- 带伸缩型数组成员的结构不可作为数组成员或另一个结构成员

###### 匿名结构
```C
struct person {
    int id;
    struct { char *first; char *last;};
};
struct person personA = {8483, { "Alan", "Turing"}};
```

#### 联合类型
```C
//带标记的联合模板
union hold {
    int digit;
    double biglf;
    char letter;
};

union hold valB = valA;     //初始化联合为另一个联合变量
union hold valC = {88};     //初始化联合的第一个元素
union hold valC = {.biglf = 118.2}; //使用指定初始化器初始化
```
- 联合一次只能存储一个值
- 联合和结构的指针都能使用间接成员运算符
###### 匿名联合
```C
struct car {
    char make[15];
    int status;
    union {
        struct owner owncar;
        struct leasecompany leasecar;
    }
}
```

#### 枚举类型
```C
//默认每个枚举常量依次为0-6
enum color {red, orange, yellow, green, cyan, blue, violet};
enum levels {low = 100, medium = 500, high = 2000};
enum feline {cat, lynx = 10, puma, tiger};
//cat值为0，puma为11，tiger为11
enum
{
      MON=1, TUE, WED, THU, FRI, SAT, SUN
} day;
```
- 用于定义符号常量
- 在C语言中，结构标记、联合标记、枚举标记与普通变量使用的名称空间不同，不会引起名称冲突

#### typedef关键字
```C
//定义结构
typedef struct {
    char title[N];
    char author [N];
    int value;
} book;

//定义函数指针
typedef void (*FUNC)(char*)
FUNC funcs[4];
```
- 定义的作用域取决于定义所在的位置



---
## ***位操作***

#### 二进制有符号整数
- 符号位表示法
  - 高阶位存储符号，剩下7位表示数字
- 二进制补码
  - 若高阶位为1，则实际值为当前值减去256，如-1为11111111，-128为10000000
  - 取得相反数的操作为反转每一位
- 二进制反码
  - 若高阶位为1，则负值为反转每一位后得到的值

#### 按位运算符
- 按位取反：`~`
- 按位与：`&` `&=`
- 按位或：`|` `|=`
- 按位异或：`^` `^=`
<br>
- 掩码：`& mask`，1的位置被显示，0的位置被掩蔽
- 切换位：`^ mask`，1的位置被切换，0的位置不变
- 打开位（设置位）：`| mask`，1的位置被打开，0的位置不变
- 关闭位（清空位）：`& ~maks`，1的位置被关闭，0的位置不变
- 检查位的值：`(flag & mask) == mask` 1的位置被比较

#### 移位运算符
- 左移：`<< n` `<<= n`
  - 空出的位置由0填充
- 右移：`>> n` `>>= n`
  - 对于无符号类型，空出的位置由0填充；对于有符号类型，其结果取决于机器

#### 位字段
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

#### 对齐
_Alignas
_Alignof




---
## ***C预处理器***

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

#### #define
###### 类函数宏
```C
#define SQUARE(X) ((X)*(X))
#define PSQR(X) printf("the square of " #X " is %d\n", ((X)*(X)))
```
- 分为宏标识符（如`SQUARE`），宏参数（如`X`）和替换列表（如`((X)*(X))`）
- 双引号中的宏不会被替换，但可用预处理运算符`#`将记号转换为字符串

###### ##运算符
```C
#define XNAME(n) x ## n
#define PRINT_XN(n) printf("x" #n " = %d\n", x ## n)
```
- 可用于类函数宏和对象宏，起记号粘合剂的作用

###### 变参宏
```C
#define PR(X, ...) printf("Message " #X ": " __VA_ARGS__)

PR(1, "x = %.2f, y = %.4f\n", x, y);
```
- 省略号只能代替最后的宏参数

###### 预定义宏和预定义标识符
```C
__FILE__    //当前文件名
__DATE__    //预处理的日期
__TIME__    //翻译代码时的时间
__LINE__    //当前所处行号
__func__    //当前所处函数
__STDC_VERSION__  //支持C99标准，设置为199901L；支持C11标准，设置为201112L
```


#### #include
```C
#include <stdio.h>          //查找系统目录
#include "hot.h"            //查找当前工作目录
#include "usr/biff/p.h"     //查找指定目录
```

#### 其他指令
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

---
## C functions

#### printf()
```C
int printf(const char *format, ...)
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
```

#### scanf()
```C
int scanf(const char *format, ...)

// Format placeholder syntax
%[*][width][modifiers]type

[*] indicates the data read from the stream will be omitted
[width] specifies the maximum chars read from the stream
```

#### memcpy(), memmove()
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

#### qsort(), bsearch()
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




---
## C libaries

#### time.h
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

#### windows.h
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

#### sys/time.h
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
