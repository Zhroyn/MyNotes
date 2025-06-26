
# C++ 笔记

## 命名空间和别名

C++ 标准库有两类头文件，其中以 `.h` 为后缀的头文件中的符号是全局范围的，而不包含 `.h` 的头文件的符号则包含在命名空间之中，需要通过作用域解析运算符 `::` 访问，例如 `std::cout`。

若要自定义命名空间，可以使用 `namespace` 关键字，如 `namespace A{ ... }`。一个命名空间的定义可以分散在不同文件，或者同一文件的不同位置中。命名空间还可以嵌套定义，此时可以通过叠加使用 `::` 操作符来访问内层命名空间的符号。

可以使用 `using` 关键字，在编译期导入命名空间、导入单个符号、定义别名：

- `using namespace ns` 导入命名空间内的所有符号，使其在当前作用域可用
- `using ns::symbol` 导入命名空间内的单个符号，使其在当前作用域可用。若两个命名空间有相同的符号，还都引入到了当前作用域，则会在使用该符号时产生冲突并报错，此时可以通过在当前作用域、该符号使用之前，使用 `using` 来消除歧义
- `using IntVector = std::vector<int>` 定义类型别名，与 `typedef` 几乎等价
- `using MyVector = std::vector<T>` 定义模板类型别名，用作类型时需要加上模板参数，如 `MyVector<int>`

可以使用 `namespace ns = name` 来定义命名空间的别名，这样以后，就可以通过 `ns::symbol` 来更简洁地访问其中的符号。

C++ 中最常见的命名空间是 `std`，它包含了大量的标准库函数和对象，例如 `cout`、`cin`、`endl`、`string`、`vector` 等。




<br>

## 字符串

### 构造函数

- `string()` 返回一个空字符串
- `string(const string& str)` 返回一个与 str 相同的字符串
- `string(const string& str, size_t pos, size_t len = npos)` 返回 str 中从 pos 开始的 len 个字符
    - pos 的取值范围为 [0, str.size()]，若超出范围则会报错
    - len 可以取任意值，若超出范围，则会返回从 pos 开始的所有字符
    - `string::npos` 的值为 -1，在 len 参数中代表着到字符串末尾
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

### 搜索比较

`compare` 方法可以用于比较两个字符串，返回值为 0 时表示相等，大于 0 时表示当前字符串大于参数字符串，小于 0 时表示当前字符串小于参数字符串。大于的定义是第一个不匹配的字符在当前字符串中更大，或者全都匹配但当前字符串更长，小于同理。`compare` 方法的形式有：

- `compare(str)` 比较当前字符串和 str
- `compare(pos, len, str)` 比较当前字符串的子字符串和 str

`find` 方法可以用于搜索字符串，返回值为第一个匹配的位置，若没有匹配则返回 `string::npos`。`find` 方法的形式有：

- `find(str, pos = 0)` 在当前字符串中搜索 str，从 pos 开始
- `find(char, pos = 0)` 在当前字符串中搜索字符 char，从 pos 开始

### 字符串字面量

字符串字面量被存储在常量区，应该使用 `const char*` 类型的指针来指向它，其值不可修改。若要修改字符串的值，可以使用 `char[]` 类型的数组，将字符串字面量拷贝到数组中，例如 `char s[] = "111"`，这会自动推断类型为 `char[4]`。

字符串字面量可以使用 `sizeof` 运算符来获取长度，返回的长度包括结尾的空字符。





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

`new` 运算符会先为对象分配内存，然后调用构造函数初始化对象，最后返回对象的地址，其语法为 `new type new-initializer`。对于内置数据类型，如果不使用初始化器，程序便不会进行初始化，而对于类类型，则会调用默认构造函数。

若 type 是非数组类型，则可以使用 `(...)` 作为初始化器；若 type 是数组类型，则可以使用 `{...}` 初始化器列表，它会按照从前往后逐一初始化对象，剩余对象会调用默认构造函数来初始化，示例如下：

- `new int` 创建一个未初始化的整数
- `new int(2)` 创建一个被初始化为 2 的整数
- `new int[10]` 创建一个未初始化的整数数组
- `new int[10]{}` 创建一个被初始化为 0 的整数数组
- `new int[10]{1, 2, 3}` 创建一个前三位被初始化为 1、2、3，后七位被初始化为 0 的整数数组

`delete` 运算符会先调用对象的析构函数，然后释放对象的内存，有两种形式：

- `delete ptr` 用于非数组对象，只会对指向的第一个对象起作用
- `delete [] ptr` 用于数组对象，会对每个对象依次调用析构函数并释放内存

需要注意的是，`new` 运算符在分配失败时会抛出 `std::bad_alloc` 异常，而 `delete` 一般不会，还可以用于空指针。





<br>

## 指针

### 指针的定义

在指针的定义中，`[]` 和 `()` 的优先级高于 `*`，下列指针定义的含义依次为：

- `int * p[3]` 元素为整数指针的数组
- `int (* p)[3]` 指向整数数组的指针，每一步跨度为 12 字节
- `int (* p[3])(int, int)` 元素为指向函数的指针的数组，函数形如 `int func(int, int)`

此外，const 和指针的位置关系也很重要：

- `const type * p` `type const * p` 表示指向的值为常量，但是可通过其他指针修改
- `type * const p` 表示指针为常量，不可指向其他值
- `const type * const p` 表示指针和指向的值皆为常量，均不可修改

当函数的返回值是指针时，可以为其加上 const 修饰符，这样函数的返回值就必须赋值给常量指针，起到保护作用。如果返回值只是基本数据类型，将其声明为 const 通常没有实际意义，因为返回值是一个临时对象，其生存期仅限于表达式的求值期间。

### 智能指针

智能指针是封装了原生指针的类模板，用于自动管理对象的生命周期，主要有 `unique_ptr`、`shared_ptr` 和 `weak_ptr` 三种。

`unique_ptr` 是独占指针，只能有一个指针指向对象，当指针被销毁时，对象也会被销毁，常见方法有：

- `get()` 返回指向的原生指针，不改变所有权
- `release()` 返回指向的原生指针，放弃所有权，不再管理对象
- `reset(pointer p = pointer())` 释放原有对象，接管新对象，默认为空指针
- `swap(unique_ptr& x)` 交换两个指针的所有权

`shared_ptr` 是共享指针，可以有多个指针指向对象，当最后一个指针被销毁时，对象也会被销毁，常见方法有：

- `get()` 返回指向的原生指针，不改变所有权
- `reset(pointer p = pointer())` 释放原有对象，接管新对象，初始计数为 1
- `swap(shared_ptr& x)` 交换两个指针的所有权
- `use_count()` 返回引用计数，即有多少个 shared_ptr 实例共享同一对象，若为空指针则返回 0
- `unique()` 判断所有权是否唯一，即引用计数是否为 1

`weak_ptr` 是弱指针，它不会增加对象的引用计数，可以用来打破 shared_ptr 之间的循环引用，常见方法有：

- `expired()` 检查所指向的对象是否已被销毁
- `lock()` 返回一个指向对象的 shared_ptr，若对象已被销毁则返回空指针
- `use_count()` 返回引用计数，即有多少个 shared_ptr 实例共享同一对象，若为空指针则返回 0

关于智能指针的使用，有以下几点需要注意：

- 最好使用 `std::make_shared` 或 `std::make_unique` 函数来创建 unique_ptr 和 shared_ptr，如 `std::unique_ptr<int> ptr = std::make_unique<int>(10)`
- unique_ptr 不能直接赋值给 unique_ptr 和 shared_ptr，但可以通过 `std::move` 函数转移所有权，如 `ptr2 = std::move(ptr1)`
- shared_ptr 可以直接赋值给新的 shared_ptr，这会增加引用计数，如果使用 `std::move` 只会转移所有权，引用计数不会增加
- shared_ptr 可以直接赋值给 weak_ptr，但 weak_ptr 不能直接赋值给 shared_ptr，需要通过 `lock` 方法转换






<br>

## 引用

与指针不同的是，引用并不是一个对象，而是一个别名，它必须在定义时初始化，并且一旦初始化完成，它就会一直引用同一个对象，无法重新绑定到其他对象。

在 C++ 的表达式中，有左值和右值之分：

- 左值 (lvalue) 是指表达式结束后依然存在的持久对象，可以取地址，可以被赋值，如 `x`
- 右值 (rvalue) 是指表达式结束后就消失的临时对象或字面量，不能取地址，不能被赋值，如 `x + y` 和 `10`

由此，引用也可以分为左值引用和右值引用。

### 左值引用

左值引用是对左值的引用，定义形式为 `type & name = object`，其中 type 是引用的类型，name 是引用的名字，object 是要引用的对象，下面是一些例子：

- `int (&refArr)[5] = arr` 引用整个数组
- `int& refElem = arr[2]` 引用数组的第三个元素
- `int& ref2 = ref1` 引用另一个引用，相当于同一个对象的另一个别名

左值引用通常用于函数参数传递和返回类型，前者可以避免对象的拷贝，后者可以实现将函数调用放在赋值语句的左侧的效果。

常量左值引用的定义形式为 `const type & name = object`，有以下特性：

- 不能通过常量左值引用来修改对象的值，但可以通过非 const 的原始变量来修改
- 常量左值引用可以绑定右值，从而实现在函数调用时传递右值的效果

### 右值引用

右值引用是对右值的引用，不能引用左值，使用 `&&` 符号定义，主要用于移动语义和完美转发。

移动语义是指通过移动资源而不是拷贝资源来传递对象，从而提高性能。通过 `std::move` 函数，我们可以将任意值转换为右值引用，示例如下：

```cpp
int a = std::move(10);
int b = std::move(a);
```

完美转发是指在模板函数中，完整地转发参数，而不改变其类型和值类别。在模板中，`T&&` 可以是左值引用或右值引用，这取决于传递给模板的参数类型。这被称为引用折叠，规则如下：

- 如果 `T` 是一个左值或左值引用类型，那么 `T&&` 会折叠为 `T&`
- 如果 `T` 是一个右值或右值引用类型，那么 `T&&` 仍然是 `T&&`

然后 `std::forward` 就可以根据模板参数类型的推导结果，选择将参数完美转发为左值或右值，示例如下：

```cpp
void overloaded(int& x) {
    std::cout << "Lvalue reference overload" << std::endl;
}
void overloaded(int&& x) {
    std::cout << "Rvalue reference overload" << std::endl;
}

template <typename T>
void forwarding(T&& arg) {
    overloaded(std::forward<T>(arg));
}

int main() {
    int a = 5;
    forwarding(a);             // T 被推导为 int&，T&& 折叠为 int&，std::forward<int&>(a) 传递左值引用
    forwarding(5);             // T 被推导为 int，T&& 折叠为 int&&，std::forward<int>(5) 传递右值引用
    forwarding(std::move(a));  // T 被推导为 int，T&& 折叠为 int&&，std::forward<int>(std::move(a)) 传递右值引用
}
```





<br>

## 面向对象

### 类与对象

类的定义为：

```cpp
class T {
public:          // 访问修饰符
    void func(); // 成员函数
    int var;     // 成员变量
};               // 注意分号
```

上面的 `class` 也可以用 `struct` 来代替，两者基本上是可以互换的。

对象的定义为：

```cpp
T obj;       // 调用默认构造函数
T obj(args); // 调用带参构造函数
T obj();     // 函数声明，不是对象的定义
```

对象可以使用 `.` 运算符来访问成员，对象的指针可以使用 `->` 运算符来访问成员。

### 访问修饰符

关键字 `public` `private` `protected` 都是访问修饰符，区别如下：

- `public` 成员可以被任何函数访问
- `private` 成员只能被类的成员函数访问
- `protected` 成员可以被类的成员函数和派生类的成员函数访问

`struct` 的成员的默认访问权限是 `public`，而 `class` 的成员的默认访问权限是 `private`。


### 成员函数

类的成员函数可以在类的内部定义，也可以在类的外部定义，外部定义时需要使用作用域解析运算符 `::` 来指明所属的类，例如 `void T::func() { ... }`。

成员函数可以直接访问类所有的成员，也可以通过 `this` 指针来访问。`this` 指针指向当前对象，可以用于区分同名的成员变量和局部变量。

#### 显式默认化和显式删除

可以在成员函数后加上显式默认化函数声明 `= default`，显式要求编译器生成默认实现，适用于构造函数、析构函数、拷贝构造函数、拷贝赋值运算符、移动构造函数和移动赋值运算符，例如 `MyClass(const MyClass&) = default`。

类似地，可以使用显式删除函数声明 `= delete`，显式禁用特定成员函数，防止不希望的操作被执行，例如 `MyClass(const MyClass&) = delete`。

#### 构造函数

构造函数 (constructor) 是一类特殊的成员函数，它没有返回值，函数名为 `T`，可以有多个重载版本。构造函数在对象创建时被调用，用于初始化对象的成员变量。没有参数的构造函数被称为默认构造函数，只有一个参数的构造函数被称为转换构造函数，可以用于隐式类型转换。

构造顺序遵循这样两条规则：基类先于派生类构造，成员变量的构造先于自己构造函数的调用。这样一来，对于类类型成员变量，如果在构造函数主体中赋值，就会先调用成员变量的默认构造函数，然后再调用赋值运算符，导致效率低下；同时，这也无法做到为常量成员和引用成员赋值。因此，我们最好使用**初始化列表**来完成成员变量的初始化，其语法为 `: member(args), ...`，示例如下：

```cpp
MyClass(int a, int b): var1(a), var2(b) { ... }
```

需要注意的是，在使用初始化列表时，成员变量的初始化顺序并不是由初始化列表中出现的顺序决定的，而是由成员变量在类中声明的顺序决定的。如果某些成员变量不在初始化列表中，它们仍将按默认规则进行初始化，即基本数据类型保持未定义的值，类类型成员变量调用默认构造函数。

如果一个类没有定义任何构造函数，或者显式地使用了 `= default`，编译器就会自动生成一个默认构造函数，它基本等价于一个函数体为空且初始化列表为空的构造函数，会按照默认规则初始化成员变量，此时如果无法访问类类型的默认构造函数，就会导致编译错误。

#### 析构函数

析构函数 (destructor) 与构造函数相对应，它没有参数，没有返回值，函数名为 `~T`，只有一个版本，不能重载，但可以被继承。析构函数在对象销毁时被调用，用于释放对象的资源。

如果一个类没有定义析构函数且没有将其删除，编译器就会自动生成一个默认析构函数，它基本等价于一个空函数体。

析构顺序与构造相反，派生类先于基类析构，自己析构函数的调用先于成员变量的析构，且成员变量的析构与它们在类中声明的顺序相反，示例如下：

```cpp
struct X {
    ~X() { std::cout << "X::~X()" << std::endl; }
};
struct Y : public X {
    ~Y() { std::cout << "Y::~Y()" << std::endl; }
};
struct Parent {
    ~Parent() { std::cout << "Parent::~Parent()" << std::endl; }
    X x;
};
struct Child : public Parent {
    ~Child() { std::cout << "Child::~Child()" << std::endl; }
    Y y;
};

// Child::~Child()
// Y::~Y()
// X::~X()
// Parent::~Parent()
// X::~X()
```

#### 拷贝构造函数

拷贝构造函数 (copy constructor) 只有一个参数，且参数为类的引用。拷贝构造函数在对象拷贝时被调用，用于初始化新对象的成员变量。

拷贝构造函数会在以下几种情况下被调用：

- 使用一个对象初始化另一个对象，例如 `T a = b` 和 `T a(b)`，其中前者是隐式的，后者是显式的
- 函数参数传递，例如 `f(a)`，其中 `f` 的参数类型不是引用
- 函数返回，例如 `return a`，其中 `a` 的类型没有移动构造函数

如果一个类没有定义拷贝构造函数、移动构造函数、移动赋值运算符，编译器就会自动生成一个默认拷贝构造函数，对对象的直接基类子对象和成员子对象逐个进行拷贝。这样的拷贝是浅拷贝，拷贝后指针成员会指向同一个地址，可能并非预期行为，此时可以通过定义自己的拷贝构造函数来解决这个问题，例如：

```cpp
MyClass(const MyClass& obj) {
    var = obj.var;
    ptr = new int(*obj.ptr);
}
```

可以通过在构造函数和转换运算符的定义前方加上 `explicit` 修饰符，来禁止隐式调用拷贝构造函数，以及不同类型的隐式转换，这样一来，`T a = b` 就会报错，对对象进行值传递也会报错。

#### 拷贝赋值运算符

拷贝赋值运算符 (copy assignment operator) 重载了赋值运算符 `=`，定义形式通常为 `T& operator=(const T& obj)`。

如果是同类对象间进行赋值，会先调用自己的拷贝赋值运算符，再调用基类的拷贝赋值运算符，编译器可以自动生成该运算符；如果是不同类型的对象赋值，会优先调用相关类型的拷贝赋值运算符，若不存在则会先调用相关类型的构造函数进行类型转换，再进行同类对象的拷贝赋值，若都不存在则会报错。

#### 移动构造函数

移动构造函数 (move constructor) 与拷贝构造函数类似，只是参数为右值引用，定义形式为 `T(T&& other)`。移动构造函数在对象移动时被调用，其内部逻辑应当是移动资源而不是复制资源。

移动构造函数会在以下几种情况下被调用：

- 使用右值初始化另一个对象，例如 `T a = std::move(b)` 和 `T a(std::move(b))`
- 函数参数传递，例如 `f(std::move(a))`，其中 `f` 的参数类型不是引用
- 函数返回，例如 `return a`，其中 `a` 的类型有移动构造函数

如果一个类没有定义拷贝构造函数、拷贝赋值运算符、拷贝构造函数、移动赋值运算符、析构函数，编译器就会自动生成一个签名为 `T::T(T&&)` 的默认移动构造函数。如果没有移动构造函数，编译器就会调用拷贝构造函数来代替。

#### 移动赋值运算符

移动赋值运算符 (move assignment operator) 重载了赋值运算符 `=`，定义形式通常为 `T& operator=(T&& obj)`。

如果一个类没有定义拷贝构造函数、拷贝赋值运算符、拷贝构造函数、移动赋值运算符、析构函数，编译器就会自动生成一个签名为 `T& T::operator=(T&&)` 的默认移动赋值运算符。如果没有移动赋值运算符，编译器就会调用拷贝赋值运算符来代替。


### 友元函数

友元函数 (friend function) 不是类的成员函数，但可以访问类的私有成员和保护成员。若要声明函数为一个类的友元函数，需要在该类的定义中使用 `friend` 关键字，示例如下：

```cpp
class B;
class A {
    int var;
    friend void func(A& a, B& b);
};
class B {
    int var;
    friend void func(A& a, B& b);
};

void func(A& a, B& b) {
    cout << a.var << endl;
    cout << b.var << endl;
}
```

友元类 (friend class) 与友元函数类似，不过它是一个类而不是一个函数，可以通过 `friend class T` 来声明。友元类的所有成员函数都是友元函数。


### 静态成员

可以通过在成员定义的前面加上 `static` 关键字来定义静态成员，静态成员属于类而不属于对象，可以通过 `T::member` 来访问。

静态成员变量只有一份拷贝，所有对象共享，但如果静态成员变量是被定义在模板类中，那么每个模板实例都会有一份独立的拷贝。

静态成员变量必须在类的外部进行初始化，即使是初始化为默认值，常量静态成员变量除外，它们可以在类的内部进行初始化，示例如下：

```cpp
class MyClass {
public:
    static int var1;
    static const int var2 = 10;
    static constexpr int var3 = 20;
};
int MyClass::var1;
```

静态成员函数不属于任何对象，不需要通过对象来调用。它们只能访问静态成员变量和静态成员函数，不能访问对象的 this 指针和普通成员。


### 重载

重载 (overload) 是指在同一个作用域内，可以定义多个同名的函数，只要它们的参数列表不同。在编译期，编译器就会根据调用的参数类型来选择合适的函数。

#### 重载解析

重载解析有以下特性：

- 重载的函数可以有不同的返回类型，但不能只有返回类型不同，否则无法区分函数
- 值传递参数是否有 const 修饰符是无关紧要的，`int` 和 `const int` 会被认为是相同的参数
- 指针参数是否有 const 修饰符是重要的，`int*` 和 `const int*` 会被认为是不同的参数，因为这影响了指针的操作权限
- 在函数参数列表中，数组会退化为指向其第一个元素的指针，`int arr[5]` 和 `int* arr`、`const int arr[5]` 和 `const int* arr` 会被认为是相同的参数

引用的重载解析与指针类似，`int&` 和 `const int&` 会被认为是不同的参数，示例如下：

```cpp
// 左值引用参数
void func(int& a) {
    std::cout << "int& a" << std::endl;
}
// 右值引用参数
void func(int&& a) {
    std::cout << "int&& a" << std::endl;
}
// const 左值引用参数
void func(const int& a) {
    std::cout << "const int& a" << std::endl;
}
// const 右值引用参数
void func(const int&& a) {
    std::cout << "const int&& a" << std::endl;
}

int main() {
    int x = 10;
    const int cx = 20;
    int& lr = x;           // 左值引用
    int&& rr = 30;         // 右值引用
    const int& clr = cx;   // const 左值引用
    const int&& crr = 40;  // const 右值引用

    func(x);    // 调用 func(int& a)
    func(cx);   // 调用 func(const int& a)
    func(lr);   // 调用 func(int& a)
    func(rr);   // 调用 func(int& a)
    func(clr);  // 调用 func(const int& a)
    func(crr);  // 调用 func(const int& a)
    func(50);   // 调用 func(int&& a)
}
```

可以看到，在正常情况下，只有直接传递右值时，才会调用右值引用参数的函数，其他情况下都会调用左值引用参数的函数，即使是右值引用的变量也会被当作左值引用来处理。若要调用 const 右值引用参数的函数，可以使用 `std::move` 函数来将参数转换为右值，此时原本为常量的参数就会被当作 const 右值引用来处理。需要注意的是，此时不能再定义一个 `int` 或 `const int` 的值传递函数，这样会导致二义性错误。

#### 重载运算符

除了函数重载以外，运算符也可以重载，下面将列出一些常见的运算符重载形式：

- 一元运算符重载
    - `T& operator++()` 前置自增，`T operator++(int)` 后置自增
    - `T& operator--()` 前置自减，`T operator--(int)` 后置自减
    - `T operator+()` 正号，`T operator-()` 负号
    - `T& operator*()` 解引用，`T* operator&()` 取地址
    - `bool operator!()` 逻辑非，`T operator~()` 按位非
- 二元运算符重载
    - `T operator+(const T&)` `T operator%(const T&)` `T operator&(const T&)` 等
    - `T& operator|=(const T&)` `T& operator<<=(const T&)` 等
    - `bool operator==(const T&)` `bool operator<(const T&)` 等
- 赋值运算符重载
    - `T& operator=(const T&)` 拷贝赋值运算符
    - `T& operator=(T&&)` 移动赋值运算符
- 类型转换运算符重载
    - `operator T()`
    - `operator const char&()` 转换为常量左值引用
- 输入/输出运算符重载
    - `std::ostream& operator<<(std::ostream&, const T&)`
    - `std::istream& operator>>(std::istream&, T&)`
    - 需要注意的是，输入/输出运算符并不能重载为 `T` 的成员函数，因为左侧的操作数必须是流对象，一般都是重载为 `T` 的友元函数
- 下标运算符重载
    - `T& operator[](int)`
    - `const T& operator[](int) const`
- 函数调用运算符重载
    - `ReturnType operator()(args)`
- 成员访问运算符重载
    - `PointerType operator->()`
    - `p->member` 相当于 `(p.operator->()).member`

可以看到，大多数运算符是可以重载的，但仍有一些运算符不可以重载，例如 `::` `.` `.*` `?:` `sizeof` `typeid`。

大多数运算符既可以重载为友元函数，也可以重载为成员函数，但 `=` `[]` `()` `->` `->*` 以及类型转换运算符只能重载为成员函数。


### 继承

继承 (inheritance) 是面向对象编程的一个重要特性，它允许一个派生类继承另一个基类的成员。继承的语法为 `class DerivedClass: public BaseClass {...}`，其中 `public` 是继承方式，可以是 `public` `protected` `private`，区别如下：

- `public` 基类的公有成员仍是公有成员，保护成员仍是保护成员
- `protected` 基类的公有成员变为保护成员，保护成员仍是保护成员
- `private` 基类的公有成员和保护成员变为私有成员

`struct` 的默认继承方式是 `public`，而 `class` 的默认继承方式是 `private`。

可以在类名后加上 `final` 关键字来阻止类被继承，例如 `class T final { ... }`；还可以在成员函数后加上 `final` 关键字来阻止函数被重写，例如 `void func() final { ... }`。

派生类会继承基类的所有成员，除了构造函数、析构函数、拷贝构造函数、友元函数和重载运算符。派生类可以继承多个基类，多个基类之间用逗号分隔，每个基类前需要指定继承方式。如果这些基类中有相同名称的成员，可以使用作用域解析运算符来指定要访问的成员属于哪个基类，如 `Base1::func()`。

派生类在初始化时，一定会调用基类的构造函数，如果没有在初始化列表中指定基类的构造函数，编译器会隐式地调用基类的默认构造函数。派生类在销毁时，也会调用基类的析构函数。由于派生类无法访问基类的私有成员，因此基类的构造函数和析构函数不能是私有的。


### 多态

多态 (polymorphism) 是面向对象编程的一个重要特性，它允许对象以多种形式存在，并通过相同的接口调用不同类的对象。C++ 中的多态主要通过继承和虚函数实现。

虚函数 (virtual function) 可以通过在基类的成员函数的前面加上 `virtual` 关键字来定义，这会让编译器在运行时动态绑定该函数的地址，此后即使通过基类指针或引用调用该函数，也会调用派生类重写的函数。如果派生类没有重写基类的虚函数，则会绑定基类的虚函数。派生类重写的虚函数前面也可以加上 `virtual` 关键字作为提示，但这不是必须的。

如果不想在基类中给出虚函数的实现，可以将虚函数定义为纯虚函数 (pure virtual function)，形式为 `virtual type func(args) = 0`。这会让基类变为抽象类，无法实例化，只能作为接口使用。

为了确认派生类成功重写了基类的虚函数，可以在派生类重写的虚函数后面加上 `override` 关键字，例如 `void func() override { ... }`。这样的话，如果派生类没有成功重写基类的虚函数，编译器便会报错。`override` 关键字可以和 `final` 关键字一起使用，以防止派生类的派生类再次重写该函数，例如 `void func() final override { ... }`，顺序并不要紧。

### 常量对象与常量成员函数

常量对象可以通过在对象的类型前面加上 `const` 关键字来定义，例如 `const T obj`，有以下特性：

- 只能调用常量成员函数
- 不能修改对象的成员变量

常量成员函数可以通过在函数后添加 `const` 关键字来定义，例如 `void func() const { ... }`，有以下特性：

- 只能修改静态成员变量的值
- 只能调用常量成员函数
- 可以与另一个名称相同、参数列表相同、但没有 `const` 关键字的非常量成员函数构成重载

类中的常量成员变量必须在构造函数的初始化列表中初始化，不能在构造函数的函数体中初始化。





<br>

## 内联函数

内联函数 (inline function) 通常用于定义简单的函数，它的定义为 `inline type func(args) { ... }`。当调用内联函数时，编译器会将函数的代码插入到调用的地方，而不是跳转到函数的地址，这样可以减少函数调用的开销。

一般来说，内联函数的定义会放在头文件中，它并不会编译成一个独立的函数。

需要注意的是，类内定义的成员函数通常被隐式地视为内联函数。显式使用 `inline` 关键字可以建议编译器将函数内联，但最终是否内联由编译器决定。






<br>

## 类型转换

C++ 有以下四种类型转换：

- `static_cast` 用于相关类型之间的转换，在编译时进行，如果遇到不相关的类型转换会导致编译报错。相关类型包括：
    - 基本数据类型之间的转换
    - 从派生类指针到基类指针
    - 从 `void*` 到其他指针
- `dynamic_cast` 只能用于类的指针或引用，在运行时进行类型检查，指针转换失败会返回空指针，引用转换失败会抛出异常 `std::bad_cast`。常见用法是将基类指针/引用转换为派生类指针/引用，当且仅当基类指针/引用的对象实际上是派生类对象时，转换才会成功
- `const_cast` 用于添加或移除 const 或 volatile 限定符，作用对象只能是指针或引用
- `reinterpret_cast` 用于进行低级别的、位级别的转换，不执行类型检查，常见用法是将一个指针转换为另一个不相关类型的指针、将指针转换为整数、将浮点数转换为整数等

这四种类型转换的语法为 `type_cast<type>(expr)`，其中 `type_cast` 是类型转换的名称，`type` 是转换的目标类型，`expr` 是要转换的表达式。






<br>

## 模板

模板 (template) 是 C++ 的一个重要特性，它允许定义通用的类或函数，可以用于不同的数据类型。

函数模板和类模板的定义形式都是在最前面加上 `template` 关键字，后面跟上模板参数列表，例如 `template <typename T, ...>`，需要注意的有：

- 模板参数可以有默认值，例如 `template <typename T = int>`
- 模板参数列表中的 `typename` 可以用 `class` 替代，两者几乎没有区别
- 当模板中用到模板类型参数的类型成员时，需要在它前面加上 `typename` 关键字，以声明该成员是一个类型，例如 `typename T::value_type func() { ... }`

在调用函数模板和定义类模板对象时，编译器会尝试使用函数参数或者模板参数默认值来推断模板参数的类型，如果无法推断则需要显式指定模板参数，如 `func<int>(args)` 和 `T<int> obj`。

### 非类型模板参数

模板还可以使用非类型参数，非类型参数是一个常量表达式，可以是整数、枚举、指针、引用、数组等，但不能是类类型。

非类型参数可以用于模板的类型、函数参数、函数返回值等，例如：

```cpp
template <typename T, int size>
class Array {
private:
    T arr[size];
public:
    T& operator[](int index) {
        return arr[index];
    }
};
```

### 模板特化

模板特化 (template specialization) 是指为特定的模板参数提供特定的实现，例如：

```cpp
template <typename T, typename U>
class MyPair {
public:
    void print() {
        std::cout << "Generic template" << std::endl;
    }
};

// 偏特化
template <typename T>
class MyPair<T, int> {
public:
    void print() {
        std::cout << "Partial specialization for second int" << std::endl;
    }
};

// 全特化
template <>
class MyPair<int, int> {
public:
    void print() {
        std::cout << "Full specialization for both int" << std::endl;
    }
};
```

### 显式实例化

如果将模板的实现单独放在源文件中，编译器会因为不知道模板参数而无法实例化模板，生成的目标文件也不会包含模板的实现。此时如果在别的源文件中使用了该模板，链接器会因为找不到模板的实现而报错。

因此，模板的定义和声明通常都放在头文件中，以使编译器在编译使用该模板的源文件时能够正确实例化模板。但是，这可能会导致相同的模板代码在每个包含它的翻译单元中都会实例化一次，增加了编译时间和目标文件的大小。

为了避免这个问题，可以在模板的实现文件中进行显式实例化 (explicit instantiation)，例如：

```cpp
template class MyClass<int, int>;
template void func<int>(int, int);
```

这样编译器就会在编译时实例化模板，生成目标文件。需要注意的是，显式实例化只能在模板的实现文件中进行，不能在头文件中进行。







<br>

## 迭代器

C++ 的 STL (Standard Template Library) 中提供了许多容器，为了统一访问方式，这些容器都提供了迭代器 (iterator) 来访问容器中的元素。通过迭代器，可以将容器和算法分离，使得算法可以独立于容器而存在。

迭代器的定义形式为 `container::iterator it`，其中 `container` 是容器的类型，`iterator` 是迭代器的类型。迭代器有以下几种类型：

- 输入迭代器 (InputIterator) 只能支持自增、拷贝、相等判断、解引访问
- 输出迭代器 (OutputIterator) 只能支持自增、拷贝、相等判断、解引赋值
- 前向迭代器 (ForwardIterator) 同时具有输入迭代器和输出迭代器的功能
- 双向迭代器 (BidirectionalIterator) 在前向迭代器的基础上增加了自减操作
- 随机访问迭代器 (RandomAccessIterator) 在双向迭代器的基础上增加了随机存取和前后比较操作，及 `+` `-` `[]` `<` `>` `<=` `>=` 等

### 常见容器的迭代器

常见容器的迭代器类型如下：

- 有随机访问迭代器的容器包括 `vector` `deque` `array`
- 有双向迭代迭代器的容器包括 `list` `set` `map` `multiset` `multimap`
- 有前向迭代迭代器的容器包括 `forward_list` `unordered_set` `unordered_map` `unordered_multiset` `unordered_multimap`
- 不支持迭代器的容器包括 `stack` `queue` `priority_queue`

除了常见的 `iterator` 类型以外，STL 容器还提供了 `const_iterator` 类型，它只能访问容器中的常量元素，不能修改元素的值。而对于支持双向迭代器的容器，STL 容器还提供了 `reverse_iterator` 和 `const_reverse_iterator` 类型，它们可以逆序访问容器中的元素。

支持迭代器的容器一般都有以下方法：

- `begin()` 返回指向容器第一个元素的迭代器
- `end()` 返回指向容器最后一个元素的下一个位置的迭代器
- `cbegin()` 返回指向容器第一个元素的常量迭代器
- `cend()` 返回指向容器最后一个元素的下一个位置的常量迭代器
- `rbegin()` 返回指向容器最后一个元素的反向迭代器
- `rend()` 返回指向容器第一个元素的前一个位置的反向迭代器

### 特性萃取

在算法中使用迭代器时，我们可能需要用到迭代器的一些特性，例如迭代器的值类型、引用类型、指针类型等。为此，STL 提供了 `iterator_traits` 类模板，它可以通过迭代器的类型来获取迭代器的特性，这种技术被称为特性萃取 (traits)。

具体来说，迭代器的特性包括：

- `value_type` 迭代器所指向的值的类型
- `reference` 迭代器所指向的值的引用类型
- `pointer` 指向迭代器所指向的值的指针类型
- `difference_type` 用于表示两个迭代器之间的距离的类型
- `iterator_category` 迭代器的类型，包括输入迭代器、输出迭代器、前向迭代器、双向迭代器、随机访问迭代器

`iterator_traits` 的一个使用示例如下：

```cpp
template <typename Iterator>
void print_elements(Iterator first, Iterator last) {
    // 获取迭代器的类别
    typedef typename std::iterator_traits<Iterator>::iterator_category category;
    // 根据迭代器的类别调用不同的实现
    print_elements_impl(first, last, category());
}

// 输入迭代器版本的实现
template <typename Iterator>
void print_elements_impl(Iterator first, Iterator last, std::input_iterator_tag) {
    std::cout << "Input Iterator: ";
    while (first != last) {
        std::cout << *first << " ";
        ++first;
    }
    std::cout << std::endl;
}
```

`iterator_traits` 是通过偏特化来实现的。例如，如果迭代器是原生指针类型，它就返回指针的特性，否则会返回迭代器本身的特性。一个简单的示例如下：

```cpp
// 默认版本
template <typename T>
struct iterator_traits {
    typedef typename T::value_type value_type;
    typedef typename T::reference reference;
    typedef typename T::pointer pointer;
    typedef typename T::difference_type difference_type;
    typedef typename T::iterator_category iterator_category;
};

// 原生指针版本
template <typename T>
struct iterator_traits<T*> {
    typedef T value_type;
    typedef T& reference;
    typedef T* pointer;
    typedef ptrdiff_t difference_type;
    typedef random_access_iterator_tag iterator_category;
};
```






<br>

## 常见算法

STL 在 `algorithm` 头文件中提供了许多常见的算法，这些算法都是函数模板，可以通过迭代器来对容器进行操作。

### 范围检测

```cpp
template <class InputIterator, class UnaryPredicate>
bool all_of (
    InputIterator first, InputIterator last,
    UnaryPredicate pred
);

template <class InputIterator, class UnaryPredicate>
bool any_of (
    InputIterator first, InputIterator last,
    UnaryPredicate pred
);

template <class ForwardIterator, class T[, class Compare]>
bool binary_search (
    ForwardIterator first, ForwardIterator last,
    const T& val[, Compare comp]
);

template <class InputIterator1, class InputIterator2[, class BinaryPredicate]>
bool equal (
    InputIterator1 first1, InputIterator1 last1,
    InputIterator2 first2[, BinaryPredicate pred]
);
```

- `all_of` 检测区间 `[first, last)` 中的所有元素是否都满足谓词 `pred`
- `any_of` 检测区间 `[first, last)` 中的所有元素是否有一个满足谓词 `pred`
- `binary_search` 在有序区间 `[first, last)` 中查找是否存在等于 `val` 的元素，可以指定比较函数 `comp`
- `equal` 检测区间 `[first1, last1)` 和 `[first2, ...)` 是否相等，可以指定比较函数 `pred`
- `UnaryPredicate` 是输入为一个迭代器指向的元素，返回值为 `bool` 类型的函数
- `BinaryPredicate` 是输入为两个迭代器指向的元素，返回值为 `bool` 类型的函数

### 拷贝

```cpp
template <class InputIterator, class OutputIterator>
OutputIterator copy (
    InputIterator first, InputIterator last,
    OutputIterator result
);

template <class InputIterator, class OutputIterator, class UnaryPredicate>
OutputIterator copy_if (
    InputIterator first, InputIterator last,
    OutputIterator result, UnaryPredicate pred
);

template <class InputIterator, class Size, class OutputIterator>
OutputIterator copy_n (
    InputIterator first, Size n,
    OutputIterator result
);

template <class BidirectionalIterator1, class BidirectionalIterator2>
BidirectionalIterator2 copy_backward (
    BidirectionalIterator1 first, BidirectionalIterator1 last,
    BidirectionalIterator2 result
);
```

- `copy` 将区间 `[first, last)` 中的元素拷贝到从 `result` 开始的区间
- `copy_if` 只拷贝满足谓词 `pred` 的元素
- `copy_n` 只拷贝前 `n` 个元素，不需要指定结束位置
- `copy_backward` 逆序拷贝到以 `result` 结束的区间，即从 `*(result-1) = *(last-1)` 开始，不断向前拷贝
- 返回指向复制结束的位置的迭代器，对于 `copy_backward` 来说，就是指向目标区间开头的迭代器

### 计数

```cpp
template <class InputIterator, class T>
typename iterator_traits<InputIterator>::difference_type count (
    InputIterator first, InputIterator last,
    const T& val
);

template <class InputIterator, class T>
typename iterator_traits<InputIterator>::difference_type count_if (
    InputIterator first, InputIterator last,
    UnaryPredicate pred
);
```

- `count` 计算区间 `[first, last)` 中等于 `val` 的元素的个数
- `count_if` 只计算满足谓词 `pred` 的元素的个数

### 查找

```cpp
template <class InputIterator, class T>
InputIterator find (
    InputIterator first, InputIterator last,
    const T& val
);

template <class ForwardIterator1, class ForwardIterator2[, class BinaryPredicate]>
ForwardIterator1 find_end (
    ForwardIterator1 first1, ForwardIterator1 last1,
    ForwardIterator2 first2, ForwardIterator2 last2
    [, BinaryPredicate pred]
);

template <class InputIterator, class ForwardIterator[, class BinaryPredicate]>
InputIterator find_first_of (
    InputIterator first1, InputIterator last1,
    ForwardIterator first2, ForwardIterator last2
    [, BinaryPredicate pred]
);

template <class InputIterator, class UnaryPredicate>
InputIterator find_if (
    InputIterator first, InputIterator last,
    UnaryPredicate pred
);

template <class InputIterator, class UnaryPredicate>
InputIterator find_if_not (
    InputIterator first, InputIterator last,
    UnaryPredicate pred
);
```
- `find` 在区间 `[first, last)` 中查找第一个等于 `val` 的元素
- `find_end` 在区间 `[first1, last1)` 中查找最后一个与区间 `[first2, last2)` 匹配的子序列，返回子序列的起始位置
- `find_first_of` 在区间 `[first1, last1)` 中查找第一个与区间 `[first2, last2)` 中任意一个元素匹配的元素
- `find_if` 查找第一个满足谓词 `pred` 的元素，
- `find_if_not` 查找第一个不满足谓词 `pred` 的元素
- 如果没有找到，上述函数会返回 `last` 或 `last1`








<br>

## 异常处理

异常处理 (exception handling) 用于处理程序运行时错误，它可以使程序在出现错误时不会立即崩溃，而是能够根据错误类型执行相应的处理逻辑。C++ 中的异常处理机制由 `try` `throw` `catch` 三个关键字组成。

我们可以使用 `throw` 关键字来抛出异常，抛出的异常可以是任意类型，但通常是一个异常类的对象。异常类通常继承自 `std::exception` 类，它有一个虚函数 `what`，用于返回异常的描述。

抛出异常后，我们可以使用 `try` 和 `catch` 关键字来捕获异常。程序会在当前函数中自上而下查找匹配的 `catch` 语句，如果找到则执行 `catch` 语句中的代码，否则会返回到上一层查找。具体来说，匹配的 `catch` 语句是指 `catch` 语句中的异常类型与抛出的异常类型相同，或者是抛出的异常类型的基类。我们可以使用 `catch (...)` 来捕获所有类型的异常。

在捕获到异常之后，我们还可以使用 `throw;` 语句，将其再次抛出，以便让上层调用者处理这个异常。这通常用于在捕获异常后，执行一些清理或记录操作，然后将异常传递给更高层次的异常处理程序。

一个简单的检测不同类型异常的示例如下：

```cpp
try {
    throw 1;
} catch (int e) {
    std::cout << "Catch int: " << e << std::endl;
} catch (double e) {
    std::cout << "Catch double: " << e << std::endl;
} catch (const char * e) {
    std::cout << "Catch const char *: " << e << std::endl;
} catch (std::exception & e) {
    std::cout << "Catch exception: " << e.what() << std::endl;
} catch (...) {
    std::cout << "Catch unknown exception" << std::endl;
}
```

C++ 提供了一些标准异常类，它们都继承自 `std::exception` 类，例如：

- `std::logic_error` 逻辑错误，包括：
    - `std::invalid_argument` 无效参数，表示函数的参数不合法
    - `std::domain_error` 域错误，表示函数的参数超出了定义域
    - `std::length_error` 长度错误，表示容器的长度超出了最大限制
    - `std::out_of_range` 越界错误，表示访问容器时下标超出范围
- `std::runtime_error` 运行时错误，包括：
    - `std::range_error` 范围错误
    - `std::overflow_error` 溢出错误
    - `std::underflow_error` 下溢错误
- `std::bad_alloc` 内存分配错误，当 `new` 失败时会抛出
- `std::bad_cast` 类型转换错误，当 `dynamic_cast` 失败时会抛出
- `std::bad_exception` 未捕获的异常，通常与 `std::unexpected` 一起使用
- `std::bad_typeid` `typeid` 运算符错误，当 `typeid` 作用于空指针时会抛出

我们还可以自定义异常类，只需要继承自 `std::exception` 类，并实现 `what` 函数即可。一个简单的自定义异常类的示例如下：

```cpp
class MyException : public std::exception {
public:
    const char * what() const noexcept override {
        return "My exception";
    }
};
```
