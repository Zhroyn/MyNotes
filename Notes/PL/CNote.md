[toc]

## ***数据类型***

- 类型的级别从高至低依次是: long double , double , float ,
  unsigned long long , long long , unsigned long , long ,
  unsigned int , int
  - 当 int 和 long 大小相同时，unsigned int 的级别高于 long
- char and short 在表达式中会类型转换（升级）为 int or unsigned int
- 作为函数参数传递时，char and short 会升级为 int，float 会升级为 double
- 赋值表达式结果会转换为被赋值变量的类型

#### 整数

###### 转换说明
十进制: %d or %i
八进制: %o or %#o
十六进制: %x or %#x or %#X

unsigned int: %u
short: %hd  (%ho or %hx or %hu)
long: %ld  (%lo or %lx or %lu)
long long: %lld  (%llo or %llx or %llu)
sizeof or strlen的返回值: %zd

###### 位数
short: 16  (-32768~32767)
int: 32  (-2147483648~2147483647)
long: 32 or 64
long long: 64

2^16 = 65536
2^32 = 42,9496,7296
2^64 = 1844,6744,0377,0951,1616

###### 前缀后缀
二进制前缀为0b or 0B，八进制前缀为0，十六进制前缀为0x or 0X
long: l or L
long long: ll or LL
unsigned long long: ull or LLU or ULL
(两个L须在一起且大小写相同，U和L大小写可不同，相对位置可不同)



#### 字符
- 若传入数据过大则会截取末8位
###### 常用字符ASCII码
```C
' ' = 32
'\0' = 0, '\n' = 10 or `%lf`
'0' = 48, '9' = 57
'A' = 65, 'a' = 97
```


#### 浮点数
###### 转换说明
- float: `%f`
- double: `%lf`
  - scanf()时应使用`%lf`，printf()时应使用`%f` or `%lf`
- long double: `%Lf`
- `%g` or `%G`: 根据值的不同，选择`%f` or `%e` or `%E`
- `%a` or `%A`: 十六进制p计数法

###### 位数
float: 32（8位指数，24位尾数或有效数，至少6位有效数字）
double: 64（至少13位有效数字）
long double: 128位（至少与double相同）

###### 其他
- 使用%.2f会四舍五入，如9.999变为10.00，但9.99仍为9.99
- 上溢时会显示inf，下溢会损失类型全精度
- 浮点型常量示例
  * .2
  * 100.
  * .8E-5 （不可加空格）
  * 0x0.ap4 ((0 + 10/16) * 16 = 10)
  * 浮点型常量默认为double，加后缀f or F可变为float，加后缀l or L可变为long double



#### 复数
float_Complex，double_Complex，long double_Complex
float_Imaginary，double_Imaginary，long double_Imaginary
(若包含complex.h头文件，可用complex、imaginary代替_Complex、_Imaginary)






---
## ***函数***

#### 常见函数
```C
printf()
```
- *修饰符：%\*d可指定字段宽度，%\*.\*f可指定字段宽度和精度
- 浮点数的字段宽度包括小数点
- 返回成功打印的字符数，包括空格和转义字符（比如‘\n’就属于一个字符），但不包括‘\0'。发生错误时，返回负值（-1）
![Graph4-4](../Pictures/Graph4-4.png)
![Graph4-5](../Pictures/Graph4-5.png)

```C
scanf()
```
- 把字符串读入字符数组，不需要&
- `scanf()`只会读取字符串的第一个单词
- `scanf()`会停止在第一个读取错误处（如%d遇到“A”）
- 若格式字符串转换说明后紧跟其他符号（如"%d:%d"），则输出时必须在其后紧跟该符号，否则会出错
- 格式字符串中的空格表示读取所有空白字符
- *修饰符：将\*放在%和转换字符之间，会跳过相应的输出项
- 返回成功读取的项数的个数，当读取到”文件结尾“时，返回-1

```C
getchar()
```
- 返回类型为int

```C
putchar()
```
- 参数类型为int

```C
qsort(array, n, sizeof(int), cmpfunc)

int cmpfunc(const void * a, const void * b)
{
    return (*(int*)a - *(int*)b);
}
```
- 上述为升序排序
- 若cmpfunc返回正值则交换

---
## ***运算符***

###### 优先级
| 名称 | 运算符	| 结合律 |
| ---- | ----- | ----- |
|后缀运算符| []   ()   ·   ->   |从左到右|
|一元运算符| ++   --   !   ~   +   -   *   &   sizeof |**从右到左**|
|类型转换运算符| (*type*)	    |**从右到左**|
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

###### 其他
- /: C99后，负数的整除除法为趋零截断（-5 / 2 = -2）
- %: 负数求模结果的正负性与第一个数相同，趋零截断（-11 % ±5 = -1）
<br>
- 可通过在数据前加 (*type*) 进行强制类型转换
- 若用于数据类型，sizeof 后需加 ()
<br>
- 比较浮点数最好只使用大于小于
- 包含 iso646.h 头文件，便可用 and 代替 &&，or 代替 ||，not 代替 !
- && 和 || 运算符都是序列点
<br>
- 条件运算符：expression1 ? expression2 : expression3。若expression1为真，则表达式的值为expression2，否则为expression3。如 max = (a > b) ? a : b
- 逗号运算符：是一个序列点，左侧项副作用会在执行右侧项之前发生，以最后一个表达式的值作为整个表达式的值




---
## ***C控制语句***

#### continue语句
- 在 while 和 do while 循环中，会跳转到测试表达式
- 在 for 循环中，会跳转到更新表达式，然后进入测试表达式

#### break语句
- 会直接跳转到循环后面第一条语句，更新也跳过

#### switch语句
- switch 的测试表达式必须是整型表达式，case 标签必须是整型常量或整型常量表达式
- 可使用 default 标签，当没有匹配的标签时会跳转到 default : 标签行
```C
switch(expression){
    case constant-expression :
       statement(s);
    case constant-expression :
       statement(s);

    default :
       statement(s);
}
```

#### goto语句
- 把控制无条件转移到同一函数内的被标记的语句



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
- **文件作用域**：变量定义在函数外，也称为全局变量，可见范围是从定义处到文件末尾。只能使用常量表达式初始化文件作用域变量
- 函数作用域：仅用于goto语句的标签，即标签出现在函数的内层块中，它的作用域也延伸至整个函数
- 函数原型作用域：范围是从形参定义处到原型声明结束

#### 链接
- 外部链接：可延伸至其他翻译单元的作用域
- 内部链接：仅限于一个翻译单元
- 无链接：具有块作用域、函数作用域或函数原型作用域的变量

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
- 若声明在所有函数外，则为内部链接的静态变量，具有文件作用域，内部链接
- 若未显式初始化，则会被初始化为0

`extern`: 声明外部变量（外部存储类别）
- 外部变量声明在所有函数外，具有静态存储期、文件作用域和外部链接
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
## 位操作

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
## C预处理器

#### 翻译处理
在预处理之前，编译器会先对程序进行翻译处理，如：
- 将源代码出现的字符映射到源字符集
- 将物理行转换为逻辑行，即删除反斜杠加按下Enter键形成的换行符，使表达式成为一行
- 将文本划分成预处理记号序列、空白序列和注释序列。编译器用一个空格字符替换每一条注释



