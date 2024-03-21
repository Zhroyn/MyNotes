
# SQL 介绍

SQL 是 Structured Query Language 的缩写，可以分为两个部分：数据操作语言 (DML) 和 数据定义语言 (DDL)。SQL 有多种标准，其中最经典的是 SQL92 和 SQL99。

在各平台，不同数据库软件的关键字和函数名都不区分大小写，但具体的语法会有区别，本笔记以 MySQL 为主。




## 数据类型

**字符串类型**

- `char(n)`  定长字符串，默认为 1
- `varchar(n)` 不定长字符串
- `tinytext` `text` `mediumtext` `longtext` 文本数据，分别最多存放 255、65536、16MB、4GB 个字符
- `tinyblob` `blob` `mediumblob` `longblob` 二进制数据，分别最多存放 255、65536、16MB、4GB 个字节

**数值类型**

- `bool` 布尔值
- `tinyint` `smallint` `int` `bigint` 整数，分别占 1、2、4、8 个字节，在 MySQL 中可加上 `(n)` 限制最大显示长度，默认为 255
- `float(p)` 浮点数
    - 在 MySQL 中，`float` 和 `double` 分别占 4 和 8 个字节，`float` 可以使用 p 指定精度，当 p 为从 0 到 23 时，会占 4 个字节，当 p 为从 24 到 53 时，会占 8 个字节
    - 在 SQL Server 中，`float` 和 `real` 分别占 8 和 4 个字节，`float` 可以使用 p 指定精度，当 p 为从 0 到 24 时，会占 4 个字节，当 p 为从 25 到 53 时，会占 8 个字节
- `decimal(p, d)` `numeric(p, d)` 定点数，p 为总位数，默认为 10，d 为小数位数，默认为 0，不会丢失精度

**时间类型**

- `date` 日期，格式为 `YYYY-MM-DD`
- `time` 时间，格式为 `hh:mm:ss`
- `timestamp` 时间戳，格式为 `YYYY-MM-DD hh:mm:ss`
- `interval` date/time/timestamp 相减可以得到 interval，interval 可以加上 date/time/timestamp
- `year` 年份，格式为 `YYYY`，有一个字节大小，可以接受以下值：
    - 从 `'1901'` 到 `'2155'` 的字符串
    - 从 1901 到 2155 的四位整数
    - 从 `'0'` 到 `'69'` 的字符串，会被解释为 2000 到 2069，从 `'70'` 到 `'99'` 的字符串，会被解释为 1970 到 1999
    - 从 0 到 69 的整数，会被解释为 2000 到 2069，从 70 到 99 的整数，会被解释为 1970 到 1999
    - 时间函数返回的结果





## 数据定义

### 创建数据库和表

可以使用 `create` 语句创建数据库或表：

- `create database database_name` 创建数据库
- `create table table_name (column_name datatype, ...)` 创建表
- `create table table_name as <select_statement>` 通过已存在的表创建新表，`as` 关键字可以忽略。新表的列名和数据类型会与原表一致，但不会保留原表的约束和索引

### 查看数据库和表

在 MySQL 中，先使用 `use database_name` 语句切换到指定数据库，然后使用以下命令查看数据库或表的信息：

- `show databases` 查看所有数据库
- `show tables [from database_name]` 查看所有表的名称
- `show table status [from database_name]` 查看所有表的详细信息
- `show create table table_name` 查看表的创建语句
- `desc table_name` 查看表的结构

### 删除数据库和表

可以使用 `drop` 语句删除数据库或表：

- `drop database database_name` 删除数据库
- `drop table table_name` 完全删除表
- `truncate table table_name` 保留表的结构，只是删除其中的内容

### 修改列

可以使用 `alter table` 语句修改表的列：

- `ALTER TABLE table_name ADD column_name datatype` 添加列
- `ALTER TABLE table_name DROP COLUMN column_name` 删除列
- `ALTER TABLE table_name RENAME COLUMN old_name TO new_name` 重命名列
- 修改列的数据类型有三种形式：
    - `ALTER TABLE table_name ALTER COLUMN column_name datatype` SQL Server / MS Access
    - `ALTER TABLE table_name MODIFY COLUMN column_name datatype` My SQL / Oracle prior version
    - `ALTER TABLE table_name MODIFY column_name datatype` Oracle 10G and later





## 数据更新

### 插入行

可以使用 `insert` 语句向指定表插入行，其形式为：

```sql
insert into table_name (column1, column2, ...)
values (value1, value2, ...)
```

当没有指定列名时，需要按照列的顺序指定值；若指定了列名，则可以忽略那些有默认值的列并按照自定义顺序插入。

若想同时插入多行，可以在 `values` 子句后加上多个括号，每个括号内为一行的值，括号之间用逗号分隔。

此外，还可以使用 `select` 子句替换 `values` 子句，从已有的表中提取数据并插入，但需要保证列的数目与类型一致。`select` 语句的写法可见[数据查询](#数据查询)一节。

### 删除行

可以使用 `delete` 语句删除满足条件的记录，其形式为：

```sql
delete from table_name
where condition
```

若未指定条件则会删除所有记录，此时更应该使用 `truncate table` 语句。条件的写法具体可见[过滤](#过滤)一节。

### 修改行

可以使用 `update` 语句修改已有的记录，其形式为：

```sql
update table_name
set column1 = value1, column2 = value2, ...
where condition
```

??? Note "Case 语句的使用"

    `case` 语句可以用于 `select` `order by` `update` 等各种语句，以实现条件选择，其形式为：

    ```sql
    case
        when condition1 then result1
        when condition2 then result2
        when conditionN then resultN
        else result
    end
    ```

    一个与 `update` 语句结合的例子如下：

    ```sql
    update employees
    set salary = case
        when salary < 1000 then salary * 1.1
        when salary < 2000 then salary * 1.2
        else salary * 1.3
    end
    ```



## 数据查询

数据查询需要用到 `select` 语句，其最基本的形式为：

```sql
select column1, column2, ... from table1, table2, ...
```

`from` 之后除了可以是表名，也可以是子查询返回的表。当从多个表查询数据并使用到那些重名的列时，必须在前面加上表名以区分，变为 `table.column`。

若想选择所有列，可用 `*` 代替所有列名。此时若有多张表，在显示列名时，重复的列名前会自动加上表名。

若想返回的行不重复，可用 `select distinct` 语句代替 `select`，与之相反的是 `select all`。需要注意的是，这样只会去除结果中完全相同的行，因此每一列都有可能出现重复的值。

### 别名

可以使用 `as` 关键字为表或列起别名。为表起的别名可用于别的子句，为列起的别名会在显示表时起效。示例如下：

```sql
select C.customer_id as ID
from customers as C
```

若列的别名内有空格，需要用引号括起来，表的别名则不能有空格。此外，`as` 关键字通常是可选的，可以直接忽略，隔一个空格即可。

### 过滤

可以使用 `where` 子句会对每一行进行判断，过滤出满足条件的记录，其常用的运算符有：

- `=` `<>` 等于、不等于
- `>` `<` `>=` `<=` 大于、小于、大于等于、小于等于
- `not` `and` `or` 逻辑运算
- `between A and B` 指定范围，是闭区间
- `like PATTERN` 搜索模式，`%` 可以匹配任意字符串，`_` 可以匹配任意字符
- `is null` `is not null` 判断是否为空值 
- `in` `not in` 判断左值是否在右值中，其中右值可以是手动指定的元组，也可以是子查询返回的表，但都要保证列的数目与左值相同
- `exists()` `not exists()` 判断子查询是否为空
- `unique()` 判断子查询返回的结果是否唯一
- `all()` `any()` 要与别的运算符一起使用，会将子查询的结果逐一放进条件中计算，all 要求所有结果都满足条件，any 要求至少有一个结果满足条件

!!! Example "示例"

    找到年龄最大的学生：

    ```sql
    select name, age
    from students
    where age >= all (select age from students);
    ```

需要注意的是，当 null 参与运算时，可能会返回 unknown 真值，结果为 unknown 的记录不会被选择。不过 unkown 可以通过与、或运算转换为 false 或 true。

### 聚合

可以使用 `group by` 子句，将所有过滤出来的记录按照指定列分组。因为每组会聚合为一条记录，因此除指定列之外的列必须使用聚合函数，如 `count()` `max()` `min()` `avg()` `sum()`，以聚合为一个值。

`count()` 函数会返回满足条件的行数，若输入 `*` 则会返回所有行数，若输入某一列名则会排除此列值为空的行，若输入 `DISTINCT column_name` 则会忽略重复的行。

`sum()` 和 `avg()` 函数分别会返回类型为数值的指定列的和与平均值，除了单个列以外，还都可以输入表达式，如 `sum(price * quantity)`。`max()` 和 `min()` 函数则会分别返回指定列的最大值和最小值，列的类型不仅限于数值，还可以是日期、字符串等。这些聚合函数会忽略 null，在全为 null 时会返回 null。

若不使用 `group by` 子句，那么在 `select` 之后的表达式要么不使用聚合函数，要么全都使用聚合函数，否则会报错。

可以在 `group by` 子句之后使用 `having` 子句，以过滤分组后的结果，其用法与 `where` 子句类似，但是可以使用聚合函数。

!!! Example "示例"

    查询每家银行在不同城市的储户数，过滤掉不足 1000 的，并从高到低排列：

    ```sql
    select bank_name, city, count(*)
    from depositor
    group by bank_name, city
    having count(*) >= 1000
    order by count(*) desc;
    ```

### 排序

可以使用 `order by` 子句对结果进行排序，其形式为：

```sql
select ...
order by column1, column2, ... asc|desc
```

`order by` 默认为升序，因此若要降序排列则必须需要加上 `desc` 关键字。

若声明了多列，则会从前往后赋予优先级，即先根据前面的列排序，若无法分清排名则接着根据后面的列排序。

若只要显示前 N 条排序结果，则可以在最后加上 `limit N` 子句，显示前 N 条记录，或者使用 `limit M, N`，显示从第 M 条开始的 N 条记录。

### 临时表

可以使用 `with as` 子句建立临时表，方便后续使用，其形式为：

```sql
with
    table1 as (...),
    table2 as (...)
select ...
```

### 连接

可以使用 `join` 子句连接多个表，简化后续的条件判断，其形式为：

- `r CROSS JOIN s` 交叉连接，返回笛卡尔积的结果
- `r NATURAL JOIN s` 自然连接，会自动找到两个表中相同的列名，然后将这些列匹配的行连接起来并返回
- `r [INNER] JOIN s ON condition` 内连接，会先将两个表的笛卡尔积求出，然后再根据条件进行筛选
- `r LEFT [OUTER] JOIN s ON condition` 左外连接，在内连接的基础上，返回左表中没有匹配的行，用 null 填充多余的列
- `r RIGHT [OUTER] JOIN s ON condition` 右外连接，在内连接的基础上，返回右表中没有匹配的行，用 null 填充多余的列
- `r FULL [OUTER] JOIN s ON condition` 全外连接，在内连接的基础上，返回左表和右表中没有匹配的行，用 null 填充多余的列

当上述语句中的 `on` 子句是对相同名称、相同类型的列进行等值查询时，可以使用 `using` 子句代替 `on` 子句来简化查询，其形式为 `using (column1, column2, ...)`，此时会和自然连接一样去除重复的列。

### 集合运算

可以使用 `union` `intersect` `except` 等集合运算符对多个 `select` 语句返回的结果进行运算：

- `r UNION s` 返回两个表的并集，会自动去重
- `r INTERSECT s` 返回两个表的交集
- `r EXCEPT s` 返回 r 中有而 s 中没有的记录
- `r UNION ALL s` 重复行会出现 $m + n$ 次
- `r INTERSECT ALL s` 重复行会出现 $\min(m, n)$ 次
- `r EXCEPT ALL s` 重复行会出现 $\max(0, m - n)$ 次
