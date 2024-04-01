
# 中级 SQL

## 自定义数据类型

可以使用 `create type` 语句自定义数据类型，其形式为：

```sql
create type type_name as datatype
```

SQL-92 又提出了 `create domain` 语句，其形式为：

```sql
create domain domain_name [as] datatype [constrant [...]]
```

type 与 domain 类似，但是 domain 包含了约束。需要注意的是，这两种语法 MySQL 都不支持。



## 完整性约束

可以在表的定义中添加完整性约束，以保证数据的完整性。完整性约束有以下几种：

- `not null` 保证列的值不为空
- `unique` 保证列的值都是唯一的，一个表可以有多个
- `default value` 保证列的值有默认值，当插入新行时若没有指定该列的值则使用默认值
- `check(condition)` 保证列的值满足某种条件
- `primary key` 保证列的值唯一且不为空，一个表只能有一个
- `foreign key` 保证列的值是另一张表的主键

这些约束可以是列的定义的一部分，位于数据类型之后，可以叠加使用。在其中 `check` `primary key` `foreign key` 还可以定义在表中，与列的定义用逗号分隔，这时它们可以使用多个列，形式变为：

- `check(condition)` 保证表的每一行满足某种条件
- `primary key (column1, column2, ...)` 保证列的值的组合唯一，且任意一列都不能为 NULL
- `foreign key (column1, column2, ...) references table_name (column1, column2, ...)`

这时还可以在约束前面加上 `CONSTRAINT constraint_name` 来命名约束。

外键可以后接动作，加上 `on delete/update action_name`，这样之后，一旦被引用属性的值被修改，就会对引用属性进行相应的更改，以保持参照完整性。动作有四种：

- `restrict` 不允许修改被引用条目，在 MySQL 中默认为此
- `cascade` 对引用条目进行同样修改
- `set null` 将引用条目设为空
- `set default` 将引用条目设为默认值

SQL-92 规定了另一种更强大的 scheme 水平的约束，称为 assertion，可以通过 `create assertion` 语句创建，其形式为：

```sql
create assertion assertion_name check (condition)
```

但是主流的数据库都不支持这种语法。


## 视图

在 SQL 中，视图 (View) 是一个虚拟的表，其中的行和列都是从定义该视图的查询中获取的。可以通过 `create view` 语句创建视图，其形式为：

```sql
create view view_name as <select_statement>
```

实际上，视图的创建并不会导致对查询表达式的计算，其存储的其实是查询表达式。当查询语句引用视图时，会自动将视图替换为对应的查询表达式。

若要更新视图，可以使用 `create or replace view` 语句，形式与上相同。

若要删除视图，可以使用 `drop view view_name`。

在视图创建后，可以通过对视图使用 `insert` `delete` `update` 等语句来修改原来的表，但是这要求在该视图的定义下该操作意义明确。常见的要求的有：

- `from` 子句只能引用一个表
- `select` 子句中不能有表达式、聚集函数、`distinct` 等
- 未在 `select` 中列出的列可以被设置为 `null` 或默认值
- 不能有 `group by` 或 `having` 子句

例如，对于仅从一个没有约束的表选择了某几列的视图，插入一行就会自动在被选择的列插入对应的值，而在未被选择的的列插入 NULL。具体的要求可以参考[微软的这篇文档](https://learn.microsoft.com/zh-cn/sql/t-sql/statements/create-view-transact-sql?view=sql-server-ver16#conditions-for-modifying-data-in-partitioned-views)。

此外，还可以将 `view` 替换为 `materialized view`，来创建具体化视图。具体化视图会计算查询表达式，并在表中的数据更改时自动更新。但是这种语法并不是 SQL 标准的一部分，不同的数据库支持的程度也不同。




## 索引

索引 (Index) 是一种用于加快查询速度的数据结构，从表中创建，也会随表而更新，对使用者来说是不可见的。通过使用索引，数据库系统可以更快地定位到满足查询条件的数据行，而无需逐行扫描整个表。

可以通过 `create index` 语句创建索引，其形式为：

```sql
create [unique] index index_name
on table_name (column1 [asc|desc], column2 [asc|desc], ...)
```

若使用 `unique` 关键字，则索引中的值是唯一的。`asc` 与 `desc` 分别表示升序与降序，默认为升序。

其他命令还有：

- `drop index index_name on table_name` 删除索引
- `alter table table_name drop index index_name` 删除索引
- `show index from table_name` 查看索引




## 事务

一个事务 (Transaction) 是一个不可分割的工作单元，是数据库管理系统执行的一个操作序列。

在 MySQL 中，事务默认是隐式的，每句 SQL 语句都会在开头自动开启一个事务，在结尾自动提交，不能显式使用 `rollback` 语句回滚，但是会在出错时自动回滚。

若想在执行某一系列语句时取消自动提交模式，可以在前面使用 `start transaction` 或 `begin` 语句显式地开启事务，在后面使用 `commit` 或 `rollback` 语句显式地结束事务，在结束以后提交模式就会回到之前的状态。

若想全局地取消自动提交模式，可以在会话开头使用 `set autocommit = 0`，此时必须使用 `commit` 来保存更改，或使用 `rollback` 来取消更改。

??? Example "示例"

    ```sql
    SET autocommit = 0;
    UPDATE account SET balance=balance -100 WHERE ano='1001';
    UPDATE account SET balance=balance+100 WHERE ano='1002';
    COMMIT;

    UPDATE account SET balance=balance -200 WHERE ano='1003';
    UPDATE account SET balance=balance+200 WHERE ano='1004';
    COMMIT;

    UPDATE account SET balance=balance+balance*2.5%;
    COMMIT;
    ```

事务的 ACID 特性是指：

- 原子性 (Atomicity)，事务要么全部执行，要么全部不执行
- 一致性 (Consistency)，事务执行前后数据库的完整性约束没有被破坏
- 隔离性 (Isolation)，事务的执行不受其他事务的干扰
- 持久性 (Durability)，事务一旦提交就是永久性的，即使系统崩溃也不会丢失




## 权限管理

### 授予权限

可以使用 `grant` 语句授予用户权限，其形式为：

```sql
grant privilege1, privilege2, ...
on object_name
to user_or_role1, user_or_role2, ...
```

在 MySQL 中，常见的权限有：

- `all` 所有权限
- `create` 创建数据库和表的权限
- `create role` 创建角色等权限
- `create user` 创建、删除、重命名用户，以及撤销权限的权限
- `create view` 创建、修改视图的权限
- `drop` 删除数据库、表、视图的权限
- `drop role` 删除角色的权限
- `select` 使用 `select` 命令的权限
- `insert` 使用 `insert` 命令的权限
- `delete` 使用 `delete` 命令的权限
- `update` 使用 `update` 命令的权限
- `alter` 使用 `alter table` 命令的权限
- `usage` 无权限

权限的水平也主要分为四种：

- global: 全局权限，需要使用 `on *.*` 来指定对象
- database: 数据库权限，需要使用 `on database_name.*` 来指定对象
- table: 表权限，需要使用 `on [database_name.]table_name` 来指定对象
- column: 列权限，可以在表名后加上 `(column1, column2, ...)` 来表示只有这些列的权限

许多权限可以拥有多种水平，如 `select` `insert` `update` 等就同时包含上述四种水平。


### 撤销权限

可以使用 `revoke` 语句撤销之前授予用户的权限，其形式为：

```sql
revoke [if exists] privilege1, privilege2, ...
on object_name
from user_or_role1, user_or_role2, ...
```

### 账户管理

MySQL 的账户名由用户名和主机名组成，因此可以使用相同的用户名创建不同的账户。账户名的形式为 `username@hostname`，其中 `@hostname` 是可选的，在必要时需要给用户名和主机名加上单引号或双引号。

与用户相关命令有：

- `CREATE USER [IF NOT EXISTS] user IDENTIFIED BY password` 创建用户，常用的主机名为 `'localhost'`
- `DROP USER [IF EXISTS] user [, user] ...` 删除用户
- `RENAME USER old_user TO new_user [, old_user TO new_user] ...` 重命名用户

可以给一个账户授予多个角色，从而给账户授予角色所有的权限。角色的命名规则与账户基本一致。与角色相关的命令有：

- `CREATE ROLE [IF NOT EXISTS] role [, role ] ...` 创建角色
- `DROP ROLE [IF EXISTS] role [, role ] ...` 删除角色
- `GRANT role [, role] ... TO user_or_role [, user_or_role] ...` 授予角色
- `REVOKE role [, role ] ... FROM user_or_role [, user_or_role ] ...` 撤销角色

若要显示账户权限可以使用 `SHOW GRANTS FOR user_or_role` 命令。
