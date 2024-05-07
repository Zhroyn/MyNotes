
# C++ 笔记

## 命名空间

C++ 中以 `.h` 为后缀的头文件中的符号仍是全局范围的，而不包含 `.h` 的头文件的符号则包含在命名空间之中，需要通过 `::` 操作符访问，例如 `:::Cpp std::cout`。若要自定义命名空间，可以使用 `namespace` 关键字，如 `:::Cpp namespace A{ ... }`。

需要注意的是，一个命名空间的定义可以分散在不同文件，或者同一文件的不同位置中。此外，命名空间还可以嵌套定义，此时可以通过叠加使用 `::` 操作符来访问内层命名空间的符号。

为了避免繁琐地使用 `::` 操作符，可以通过 `using namespace` 指令将指定命名空间的所有符号引入到当前作用域中。若两个命名空间有相同的符号，还都引入到了当前作用域，则会产生冲突并报错。

C++ 中最常见的命名空间是 `std`，它包含了大量的标准库函数和对象，例如 `cout`、`cin`、`endl`、`string`、`vector` 等。




<br>

## 字符串

### 构造函数

- `string()` 返回一个空字符串
- `string(const string& str)` 返回一个与 str 相同的字符串
- `string(const string& str, size_t pos, size_t len = npos)` 返回 str 中从 pos 开始的 len 个字符
    - 若 len 没有被指定或者超出范围，则会返回从 pos 开始的所有字符
    - 需要注意的是，当传入的不是 string 时，第二个参数会被认为是长度
- `string(const char* s)` 返回一个与 s 相同的字符串
- `string(const char* s, size_t n)` 返回 s 中的前 n 个字符
- `string(size_t n, char c)` 返回 n 个字符 c

### 查询长度

- `size()` 返回字符串的长度
- `length()` 返回字符串的长度，与 `size()` 相同，但更推荐使用 `size()`
- `empty()` 判断字符串是否为空

### 修改字符串

- `append(...)` 向原字符串末尾添加字符串，参数与构造函数一致
- `assign(...)` 为字符串赋值新的内容，参数与构造函数一致
- `insert(pos, ...)` 从 pos 开始插入字符串，原 pos 位置的字符向后移，后续参数与构造函数一致
- `erase(pos = 0, len = npos)` 删除从 pos 开始的 len 个字符
- `replace(pos, len, ...)` 替换字符串中的字符，后续参数与构造函数一致

上述方法都会返回一个指向当前字符串的引用，

### 子字符串

- `substr(pos = 0, len = npos)` 返回一个新字符串，包含从 pos 开始的 len 个字符

需要注意的是，这些方法中的 pos 参数不能大于字符串的长度，否则会报错。

### 搜索比较

`compare` 方法可以用于比较两个字符串，返回值为 0 时表示相等，大于 0 时表示当前字符串大于参数字符串，小于 0 时表示当前字符串小于参数字符串。大于的定义是第一个不匹配的字符在当前字符串中更大，或者全都匹配但当前字符串更长，小于同理。`compare` 方法的形式有：

- `compare(str)` 比较当前字符串和 str
- `compare(pos, len, str)` 比较当前字符串的子字符串和 str

`find` 方法可以用于搜索字符串，返回值为第一个匹配的位置，若没有匹配则返回 `string::npos`。`string::npos` 的值为 -1，若用在 len 参数中则意为到字符串末尾。`find` 方法的形式有：

- `find(str, pos = 0)` 在当前字符串中搜索 str，从 pos 开始
- `find(char, pos = 0)` 在当前字符串中搜索字符 char，从 pos 开始





<br>

## 文件 I/O

C++ 中许多对象都定义了读写的方式，可以通过流操作符 `<<` 和 `>>` 来进行输入输出。流操作符的左侧是流对象，右侧是要输入或输出的数据，操作符方向决定了数据的流向，其中 `<<` 是流插入操作符，用于输出，`>>` 是流提取操作符，用于输入。

头文件 `iostream` 定义了三个重要的流对象：

- `cin` 标准输入流，istream 类的对象，对应于 stdin
- `cout` 标准输出流，ostream 类的对象，对应于 stdout
- `cerr` 标准错误流，ostream 类的对象，对应于 stderr

头文件 `fstream` 定义了三个重要的类，其构造函数分别为：

- `ifstream(const char* filename, ios::openmode mode = ios::in)`
- `ofstream(const char* filename, ios::openmode mode = ios::out)`
- `fstream(const char* filename, ios::openmode mode = ios::in | ios::out)`

其中 mode 参数的标志有：

- `ios::in` 以输入模式打开文件，若不存在则创建
- `ios::out` 以输出模式打开文件，若不存在则创建，若存在则清空
- `ios::binary` 以二进制模式而不是文本模式打开文件
- `ios::ate` 打开时将位置切换到文件末尾
- `ios::app` 每次写操作前都将位置切换到文件末尾
- `ios::trunc` 打开时丢弃文件内容

这些标志是位掩码类型，可以使用或运算符组合使用。





<br>

## 内存管理

可以使用 `new` 和 `delete` 运算符来动态分配和释放内存。

`new` 运算符会先为对象分配内存，然后调用构造函数初始化对象，最后返回对象的地址，其语法为 `new type new-initializer`。若 type 为数组类型，则可以使用花括号列表进行初始化，否则需要使用括号列表进行初始化，示例如下：

- `new int` 创建一个未初始化的整数
- `new int(0)` 创建一个被初始化为 0 的整数
- `new int[3]{1, 2, 3}` 创建一个整数数组并初始化
- `new A[3]{{1, 2}, {3, 4}, {5, 6}}` 创建一个类 A 的对象组成的数组并初始化

`delete` 运算符会先调用对象的析构函数，然后释放对象的内存，有两种形式：

- `delete ptr` 用于非数组对象，只会对指向的第一个对象起作用
- `delete [] ptr` 用于数组对象，会对每个对象依次调用析构函数并释放内存

需要注意的是，`new` 运算符在分配失败时会抛出 `std::bad_alloc` 异常，而 `delete` 一般不会，还可以用于空指针。

