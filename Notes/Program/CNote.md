<!-- TOC -->

- [Date type](#date-type)
        - [char](#char)
        - [int](#int)
        - [float](#float)
        - [Implicit type conversion](#implicit-type-conversion)
- [Operators and Expressions](#operators-and-expressions)
        - [Operator precedence](#operator-precedence)
        - [Side effects](#side-effects)
        - [Sequence points](#sequence-points)
- [Statements](#statements)
- [String](#string)
        - [string.h](#stringh)
        - [stdio.h, stdlib.h](#stdioh-stdlibh)
        - [ctype.h](#ctypeh)
- [Array and Pointer](#array-and-pointer)
        - [declaration](#declaration)
        - [initialization](#initialization)
        - [Function Pointer](#function-pointer)
- [Storage, Linkage and Memory](#storage-linkage-and-memory)
        - [storage class](#storage-class)
        - [storage-class specifier](#storage-class-specifier)
        - [Dynamic memory management](#dynamic-memory-management)
        - [Type Qualifier](#type-qualifier)
- [File Input/Output](#file-inputoutput)
        - [File access](#file-access)
        - [Input/Output](#inputoutput)
        - [File positioning](#file-positioning)
        - [Others](#others)
- [***结构和其他数据形式***](#结构和其他数据形式)
        - [结构类型](#结构类型)
                - [定义结构变量](#定义结构变量)
                - [初始化结构](#初始化结构)
                - [伸缩型数组成员](#伸缩型数组成员)
                - [匿名结构](#匿名结构)
        - [联合类型](#联合类型)
                - [匿名联合](#匿名联合)
        - [枚举类型](#枚举类型)
        - [typedef关键字](#typedef关键字)
- [Bit manipulation](#bit-manipulation)
        - [Bitwise operator](#bitwise-operator)
        - [Bit field](#bit-field)
        - [Align](#align)
- [***C预处理器***](#c预处理器)
    - [翻译处理](#翻译处理)
    - [预处理器指令](#预处理器指令)
        - [#define](#define)
                - [类函数宏](#类函数宏)
                - [##运算符](#运算符)
                - [变参宏](#变参宏)
                - [预定义宏和预定义标识符](#预定义宏和预定义标识符)
        - [#include](#include)
        - [其他指令](#其他指令)
- [C functions](#c-functions)
        - [printf()](#printf)
        - [scanf()](#scanf)
        - [memcpy(), memmove()](#memcpy-memmove)
        - [qsort(), bsearch()](#qsort-bsearch)
        - [rand(), srand()](#rand-srand)
- [C libaries](#c-libaries)
        - [time.h](#timeh)
        - [windows.h](#windowsh)
        - [sys/time.h](#systimeh)

<!-- /TOC -->





## Date type
#### char
```C
char c1 = 255;
char c2 = 257;
printf("%d\n", c1);
printf("%d\n", c2);
// output:
// -1
// 1
```

**ASCII**
| Dec | Hex | Glyph |
| :-: | :-: | :---: |
| 32  | 20  | space |
| 48  | 30  | 0 |
| 57  | 39  | 9 |
| 65  | 41  | A |
| 90  | 5A  | Z |
| 97  | 61  | a |
| 122 | 7A  | z |

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
do {
  statement;
} while (test);
```

**goto statement**
- Unconditionally jump to the place of a specified label in the same function
- Label names do not interfere with other identifier names

**break statement**
- If the break statement is inside of a loop or switch statement which itself is inside of a loop or switch statement, the break only terminates the innermost loop or switch statement.

**continue statemnet**
- Used in loops to unconditionally jump to test
- If the a continue statement is inside a loop which itself is inside a loop, then it affects only the innermost loop.





---
##  String

#### string.h
```C
// Returns the length of the givenstring, not including the first NULL
size_t strlen( const char *str )

// Compares two null-terminated byte strings
// Return negative value if lhs appears before rhs in lexicographical order
int strcmp( const char *lhs, const char *rhs )
// Compares at most count characters of two possibly null-terminated arrays
int strncmp( const char *lhs, const char *rhs, size_t count )

// Finds the first occurrence of ch
// The terminating null character can also be found
// Return pointer to the found character in str, or NULL if not found
char *strchr( const char *str, int ch )
// Finds the last occurrence of ch
char *strrchr( const char *str, int ch )
```
```C
// Returns a copy of dest
// The behavior is undefined if the destination array is not large enough.
// The behavior is undefined if the strings overlap.
// The behavior is undefined if either dest or src is not null-terminated.
char *strcat( char *restrict dest, const char *restrict src )
// Appends at most count characters from the src, stopping if NULL is found
char *strncat( char *restrict dest, const char *restrict src, size_t count )

// The undefined behavior is the same as upper.
char *strcpy( char *restrict dest, const char *restrict src )
// Copies at most count characters, including the terminating null character
// If count is reached before entirely copied, the result is not null-terminated.
char *strncpy( char *restrict dest, const char *restrict src, size_t count )
```

#### stdio.h, stdlib.h
```C
// Writes the results to a character string buffer.
int sprintf( char *restrict buffer, const char *restrict format, ... )
// At most bufsz - 1 characters are written, unless bufsz is zero.
int snprintf( char *restrict buffer, size_t bufsz,
              const char *restrict format, ... )

// Reads the data from null-terminated character string buffer.
int sscanf( const char *restrict buffer, const char *restrict format, ... )

```
```C
// Converts an int to a null-terminated string using the specified base
// Return a pointer to the resulting null-terminated string
char *itoa( int value, char* str, int base)
char *ltoa( int value, char* str, int base)


// Interprets an integer value in a byte string pointed to by str.
// The implied radix is always 10.
// Discards any whitespace characters until the first non-whitespace character.
// Takes as many characters as possible to form a valid integer number.
// It is undefined if the value of the result cannot be represented in the corresponding type.
// If no conversion can be performed, ​0​ is returned.
int atoi( const char *str )
long atol( const char *str )

// The set of valid values for base is {0,2,3,...,36}
// If the value of base is ​0​, the numeric base is auto-detected:
    //if the prefix is 0, the base is octal
    //if the prefix is 0x or 0X, the base is hexadecimal
    //otherwise the base is decimal.
// str_end will be set to point to the character past the last numeric character.
// If str_end is a null pointer, it is ignored.
long strtol( const char *restrict str, char **restrict str_end, int base )


// Interprets a floating-point value in a byte string pointed to by str.
double atof( const char* str )
float strtof( const char *restrict str, char **restrict str_end );
double strtod( const char *restrict str, char **restrict str_end );
```

#### ctype.h
```C
int isalnum( int ch )
int isalpha( int ch )
int isdigit( int ch )
int isxdigit( int ch ) //checks if a character is a hexadecimal character

int islower( int ch )
int isupper( int ch )

int isblank( int ch )  //only space and horizontal tab in the default C locale
int isspace( int ch )  //' ', '\n', '\r', '\t', '\v', '\f'

int ispunct( int ch )  //!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
int iscntrl( int ch )  //i.e. codes 0x00-0x1F and 0x7F

// Checks if the given character has a graphical representation
// number, letter, punctuation
int isgraph( int ch )
// Checks if the given character can be printed
// number, letter, punctuation, space
int isprint( int ch )


int tolower( int ch )
int toupper( int ch )
```




---
## Array and Pointer

#### declaration
```C
// [] and () precede *

int * p[2]      //an array of 2 pointers-to-int
int (* p)[2]    //a pointer points to an array of 2 ints
int * p[3][4]   //a 2-dimensional array of 12 pointers-to-int
int (* p)[3][4] //a pointer points to an 2-dimensional array
int (* p[3])[4] //an array of 3 pointers-to-array
int (* pf[3])(char) //an array of 3 pointers-to-function
```

```C
// Generate a copy of the string
char s[] = "string constant"
// Point directly to static memory
char *s = "string constant"
```

```C
// Declare the pointed-to value is a const
const int * p
int const * p
// Declare the pointer is a const
int * const p
// Not only can't modify the value to which p points, but also where it points to
const int * const p
// Protect the data in array a
void f(const int a[])


// regular pointer can't point to const value:
const int * p;
int * t = p;
// warning: assignment discards 'const' qualifier from pointer target type
int * const p;
int * t = p;
// No waring
```


#### initialization
```C
a[5] = {};              //0 0 0 0 0
a[] = {1, 2, 3};        //sizeof(a) == 12
a[] = {};               //sizeof(a) == 0
a[5] = {1, 2, 3, 4, 5, 6};
//warning: excess elements in designated initializer
a[10] = {1, 2, [4] = 3, 4, 5, [1] = 6, 7};
//1 6 7 0 3 4 5 0 0 0  
```
```C
a[][] = {{1, 2, 3}, {4, 5, 6}};
//error: array type has incomplete element type 'int[]'
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
```C
int n = 3, m = 4;
int (* p)[m] = (int (*)[m]) malloc(n * m * sizeof(int));
```
 
#### Function Pointer
```C
void f(char *);
...
void (*pf)(char *) = &f     //The & is optional
char * str = "hello word";
pf(str)
(*pf)(str);                 //The * is optional
```










---
## Storage, Linkage and Memory

#### storage class
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

#### storage-class specifier
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

#### Dynamic memory management
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

#### Type Qualifier
- `const` : to share const data across files, can define global varibles with `static` in header
- `volatile` : tells the compiler that a variable can have its value altered by agencies other than the program, which facilitates compiler optimization.
  - A value can be both `const` and `volatile`.
- `restrict` : can be applied only to pointers, and it indicates that a pointer is the sole initial means of accessing a data object.
  - the compiler can’t check whether you obey this restriction.
- `_Atomic` : While a thread performs an atomic operation on an object of atomic type, other threads won’t access that object.







---
## File Input/Output

#### File access
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



#### Input/Output
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

#### File positioning
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

#### Others
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
## Bit manipulation

#### Bitwise operator
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

#### Bit field
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

#### Align
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

#### scanf()
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

#### rand(), srand()
```C
// Returns a pseudo-random integer value between ​0​ and RAND_MAX
// If rand() is used before any calls to srand(), rand() behaves as if it was seeded with srand(1).
int rand();

// Seeds the pseudo-random number generator used by rand() with the value seed.
void srand( unsigned seed );
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









