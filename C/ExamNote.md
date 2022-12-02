[toc]



## 运算
乘除模加减，移位大小等，位算按逻辑，条件赋逗号
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
- `if(x=0)` 返回0
- `int a=1,b=2,c=3,d=4`, `a<b?a:c<d?c:d = 1`
- `int i=101`, `(i++)/2 = 50`
- `char c ='w'`, `c+='A'-'a'=='W' ` 值为`'w'`，而非1
- `int x=-1`, `printf("%d",(unsigned int)x )` 输出为-1而非255，因为%d
- 取模只能用于整数






## 函数
- 函数的命名规则和变量一样（都支持`a$b_c`）
- 函数里不能定义另一个函数，但是允许函数里声明函数
- C语言中,通过函数调用只能获得一个返回值。是错的
```C
int _(int x, int y){}           //correct
func(int x,int y){return x;}    //incorrect, but can run
func(int x,y){return x;}        //false
```

## 字符
- 数字为48-57
- 大写字母为65-90
- 小写字母为97-122
- `'\017'or'\17' = 15; '\x3a' = 58`
- `("01/24/2019"+5)[4] = '9'`
- `!("01/24/2019"+5)[5] = 1` 因为第十个为空字符
- `printf("%d", !"01-21-2018"[7])` 输出为0，因为第八个为`'0'`，实际值为48
<br>

- `char s[]="123\029\08"`，sizeof(s)为8，strlen(s)为5
- `char s[]="123\0456\0789"`，sizeof(s)为9，strlen(s)为8
- `char s[]="123\0456\0889"`，sizeof(s)为10，strlen(s)为5
- sizeof的值为将所有八进制转义字符转化为一个后，字符串所有字符再加上末尾空字符的个数
- strlen的值为至第一个空字符的字符个数，不包含空字符






## 数组
- 数组的大小一经创建就无法改变
- 下标不可以为浮点数
- `int a[3][13]`, `a[-1][15]` 为第二个数字
- 假设有定义如下： int array[10]; 则该语句定义了一个数组array。其中array的类型是整型指针（即： int * ）。是错的？
```C
a[2][2] = {{1,2},{3,4},{5,6}};  //warning: excess elements in array initializer
a[2][] = {{0,1},{2,3}}; //error: array type has incomplete element type 'int[]'
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





## 指针
- 指针相减得到的是相隔元素数，而非字节数
- 不同类型的指针变量是可以直接相互赋值的。F
- 两个任意类型的指针可以使用关系运算符比较大小。F
- `char s[2][3]={"ab", "cd"}, *p=(char *)s;`，则`*++p+2 = 'd'`

```C
For the function declaration void f(char ** p)，the definition __ of var makes the function call f(var) incorrect。
A. char var[10][10];
B. char *var[10];
C. void *var = NULL;    //if change 'void' to 'char', it will report warning
D. char *v=NULL, **var=&v;

Answer: A
warning: passing argument 1 of 'f' from incompatible pointer type
     f(var);
       ^~~
note: expected 'char **' but argument is of type 'char (*)[10]'
 void f(char ** p) {}
```






## 文件
```C
fopen("..\\MakeData\\data.txt","r");
fopen("..\\MakeData/data.txt","r");
fopen("../MakeData\\data.txt","r");
fopen("../MakeData/data.txt","r");
```
- FILE是数据类型，但不是关键字






## Warning
- `if(x=0)` or `while(x=0)`
- `for(i=-1;-1<=i<1;i++)`
- 注意for循环内是否对循环数进行了修改！


