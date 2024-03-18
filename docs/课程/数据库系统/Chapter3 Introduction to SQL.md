
# SQL 介绍

SQL 是 Structured Query Language 的缩写，可以分为两个部分：数据操作语言 (DML) 和 数据定义语言 (DDL)。SQL 有多种标准，其中最经典的是 SQL92 和 SQL99。

在各平台，不同数据库软件的关键字和函数名都不区分大小写，但具体的语法会有区别，本笔记以 MySQL 为主。



## 数据类型

**字符串类型**

- `char(n)`  定长字符串，默认为 1
- `varchar(n)` 不定长字符串
- `tinytext` `text` `mediumtext` `longtext` 分别最多存放 255、65536、16MB、4GB 个字符
- `tinyblob` `blob` `mediumblob` `longblob` 分别最多存放 255、65536、16MB、4GB 个字节的二进制数据

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



## 数据库操作

- `create database database_name` 创建数据库
- `drop database database_name` 删除数据库



## 表操作

### 创建表

SQL 可以使用 `create table` 语句创建表，其基本形式为：

```sql
create table table_name (
    column1 datatype,
    column2 datatype,
    ...
)
```

或

```sql
create table table_name as select ...
```

后一种形式可用已存在的表创建新表，其中 `as` 关键字可以忽略。新表的列名和数据类型会与原表一致，但不会保留原表的约束和索引。

### 删除表

- `drop table table_name` 完全删除表
- `truncate table table_name` 保留表的结构，只是删除其中的内容

### 修改表

对列的修改可以使用 `alter table` 语句，其命令形式有：

- `ALTER TABLE table_name ADD column_name datatype` 添加列
- `ALTER TABLE table_name DROP COLUMN column_name` 删除列
- `ALTER TABLE table_name RENAME COLUMN old_name to new_name` 重命名列
- `ALTER TABLE table_name ALTER COLUMN column_name datatype` 修改列的数据类型 (SQL Server / MS Access)
- `ALTER TABLE table_name MODIFY COLUMN column_name datatype` 修改列的数据类型 (My SQL / Oracle prior version)
- `ALTER TABLE table_name MODIFY column_name datatype` 修改列的数据类型 (Oracle 10G and later)





## 主键与外键

若主键只由一个属性组成，也可以将主键的声明和属性的定义放在一起，例如 `::sql course_id varchar(8) primary key`

外键可以后接动作，使得被引用属性的值更改后对引用属性进行更改，以保持完整性，有四种动作：

- `cascade` 对引用条目进行同样修改
- `restrict` 不允许修改被引用条目
- `set null` 将引用条目设为空
- `set default` 将引用条目设为默认值






## 数据更新

`insert` 命令可用于向表插入行，其形式为：

```sql
insert into table_name (column1, column2, ...)
values
(value1, value2, ...),
(value1, value2, ...),
...
```

当没有指定列名时，需要按照列的顺序指定值；若指定了列名，则可以忽略那些有默认值的列，并且可以不按照列的顺序插入。`values` 子句可以被 `select` 子句替代，此时需要保证列的数目与类型一致。

`delete` 命令可用于删除满足条件的记录，若未指定条件则会删除所有记录，其形式为：

```sql
delete from table_name
where condition
```

`update` 命令可用于修改已有的记录，其形式为：

```sql
update table_name
set column1 = value1, column2 = value2, ...
where condition
```

`update` 命令还可以与 `case` 语句结合使用，以实现条件修改。`case` 语句还可以用于 `select` `order by` 等各种子句，实现更强大的功能，其形式为：

```sql
case
    when condition1 then result1
    when condition2 then result2
    when conditionN then resultN
    else result
end
```



## 数据查询

数据查询需要用到 `select` 语句，其最基本的形式为：

```sql
select column1, column2, ... from table1, table2, ...
```

`from` 之后除了可以是表名，也可以是子查询返回的表，此时必须为表起别名。当从多个表查询数据时，那些重名的列前必须加上表名，形式变为 `table.column`，此时若选中此列且不加别名，显示的列名也是该形式。

若想选择所有列，可用 `*` 语句代替所有列名，更加方便。此时若有多张表，重复的列名前会自动加上表名。

若想返回的行不重复，可用 `select distinct` 语句代替 `select`，与之相反的是 `select all`。需要注意的是，这样只会去除结果中完全相同的行，因此每一列都有可能出现重复的值。

### 别名

SQL 可以使用 `as` 关键字为表或列起别名。为表起的别名可用于别的子句，为列起的别名只能用于显示。示例如下：

```sql
select c.customer_id as ID
from customers as c
```

若列的别名内有空格，需要用引号括起来，表的别名则不能有空格。此外，在 MySQL 等众多数据库系统中，`as` 关键字是可选的，可以直接忽略，隔一个空格即可。

### 过滤

可以使用 `where` 子句会对每一行进行判断，过滤出满足条件的记录，其常用的运算符有：

- `=` 等于
- `<>` 不等于
- `>` 大于
- `<` 小于
- `>=` 大于等于
- `<=` 小于等于
- `between A and B` 指定范围，是闭区间
- `like PATTERN` 搜索模式，`%` 可以匹配任意字符串，`_` 可以匹配任意字符
- `is null` `is not null` 判断是否为空值 
- `in` `not in` 判断左值是否在右值中，其中右值可以是手动指定的元组，也可以是子查询返回的表，但要保证列的数目与左值相同，例如 `:::sql (id, name) IN (SELECT customer_id, customer_name FROM customers)`
- `not` `and` `or` 逻辑运算
- `exists()` `not exists()` 判断子查询是否为空
- `unique()` 判断子查询返回的结果是否唯一
- `all()` `any()` 要与别的运算符一起使用，all 要求子查询的所有结果都满足条件，any 要求子查询至少有一个结果满足条件

!!! Example

    找到年龄最大的学生：

    ```sql
    select name, age
    from students
    where age >= all (select age from students);
    ```

需要注意的是，当 null 参与运算时，可能会返回 unknown 真值，结果为 unknown 的记录不会被选择。不过 unkown 可以通过与、或运算转换为 false 和 true。

### 聚合

可以使用 `group by` 子句，将所有过滤出来的记录按照指定列分组。因为每组会聚合为一条记录，因此指定列之外的列必须使用聚合函数，如 `COUNT()` `MAX()` `MIN()` `AVG()` `SUM()`。

`COUNT()` 函数会返回满足条件的行数，若输入 `*` 则会返回所有行数，若输入某一列名则会排除此列值为空的行，若输入 `DISTINCT column_name` 则会忽略重复的行。

`SUM()` 和 `AVG()` 函数分别会返回类型为数值的指定列的和与平均值，除了单个列以外，还都可以输入表达式，如 `sum(price * quantity)`。`MAX()` 和 `MIN()` 函数则会分别返回指定列的最大值和最小值，列的类型也不仅限于数值，还可以是日期、字符串等。这些聚合函数会忽略 null，在全为 null 时会返回 null。

可以在 `group by` 子句之后使用 `having` 子句，用于过滤分组后的结果，其用法与 `where` 子句类似，但是可以使用聚合函数。

!!! Example

    查询每家银行在不同城市的储户数，过滤掉不足 1000 的，并从高到低排列：

    ```sql
    select bank_name, city, count(*)
    from depositor
    group by bank_name, city
    having count(*) >= 1000
    order by count(*) desc;
    ```

### 排序

可以使用 `order by` 子句对结果进行排序，其默认是升序排列，若要降序排列则需要在列名后加上 `desc` 关键字。若要对多列进行排序，则需要按照优先级从前往后声明列名，形式为 `ORDER BY column1, column2, ... ASC|DESC`。

若只要显示前 N 条，可以在最后加上 `limit N` 子句。或者使用 `limit M, N`，显示从第 M 条开始的 N 条记录。

### 临时表

可以使用 `with as` 子句建立临时表，方便后续使用，其用法为：

```sql
with
    table1 as (...),
    table2 as (...)
select ...
```


### 表运算

SQL 的连接子句如下，可以链式调用：

- `r CROSS JOIN s` 交叉连接，返回笛卡尔积的结果
- `r NATURAL JOIN s` 自然连接，会自动找到两个表中相同的列名，然后将这些列匹配的行连接起来并返回
- `r [INNER] JOIN s ON condition` 内连接，会先将两个表的笛卡尔积求出，然后再根据条件进行筛选
- `r LEFT [OUTER] JOIN s ON condition` 左外连接，在内连接的基础上，返回左表中没有匹配的行，用 null 填充多余的列
- `r RIGHT [OUTER] JOIN s ON condition` 右外连接，在内连接的基础上，返回右表中没有匹配的行，用 null 填充多余的列
- `r FULL [OUTER] JOIN s ON condition` 全外连接，在内连接的基础上，返回左表和右表中没有匹配的行，用 null 填充多余的列

表之间还可以使用集合运算符进行操作，需要其列数相同、类型相似：

- `r UNION s` 返回两个表的并集，会自动去重
- `r INTERSECT s` 返回两个表的交集
- `r EXCEPT s` 返回 r 中有而 s 中没有的记录
- `r UNION ALL s` 重复行会出现 $m + n$ 次
- `r INTERSECT ALL s` 重复行会出现 $\min(m, n)$ 次
- `r EXCEPT ALL s` 重复行会出现 $\max(0, m - n)$ 次


