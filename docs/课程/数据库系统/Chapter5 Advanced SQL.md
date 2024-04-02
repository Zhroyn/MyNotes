
# 高级 SQL

- ODBC (Open Database Connectivity): C, C++, C#

## JDBC

JDBC (Java Database Connectivity) 是 Java 语言访问数据库的标准接口，提供了一种访问数据库管理系统的标准方法。开发人员可以编写 Java 应用程序，通过 JDBC API 访问数据库。

连接对象 `Connection` 用于连接数据库，其方法有：

- `Connection conn = DriverManager.getConnection(username, userid, password)` 连接数据库
- `conn.close()` 关闭数据库连接
- `conn.setAutoCommit(false)` 关闭自动提交
- `conn.commit()` 提交事务
- `conn.rollback()` 回滚事务
- `DatabaseMetaData dbmd = conn.getMetaData()` 获取数据库的元数据
- `dbmd.getColumns(null, null, tableName, null)` 获取表的列信息


表达式对象 `Statement` 用于执行 SQL 语句，其方法有：

- `Statement stmt = conn.createStatement()` 创建表达式对象
- `stmt.close()` 关闭表达式对象
- `stmt.executeUpdate(sql)` 执行更新数据库的 SQL 语句
- `ResultSet rset = stmt.executeQuery(sql)` 执行查询数据库的 SQL 语句

结果集对象 `ResultSet` 用于存储查询结果，其方法有：

- `rset.next()` 移动到下一行，若有数据则返回 true
- `rest.getString(1)` 获取当前行第一个字段的值
- `ResultSetMetaData rsmd = rset.getMetaData()` 获取结果集的元数据
- `rsmd.getColumnCount()` 获取结果集的列数
- `rsmd.getColumnName(n)` 获取第 n 个列的名称
- `rsmd.getColumnTypeName(n)` 获取第 n 个列的类型名称

预处理表达式对象可以对语句进行预编译，因此可以提高执行效率。而且，由于预处理表达式可以防止 SQL 语句与参数混合在一起，因此可以避免 SQL 注入攻击。

- `PreparedStatement pStmt = conn.prepareStatement(sql)` 创建预处理表达式对象，SQL 字符串中的参数用 `?` 代替
- `pStmt.setInt(1, 100)` 设置第一个参数的值为 100
- `pStmt.executeUpdate()` 执行预处理表达式对象


### SQLJ

SQLJ 是 embeded SQL 的 Java 版本，可以在 Java 程序中嵌入 SQL 语句。SQLJ 通过预处理器将 SQLJ 文件转换为 Java 文件，然后编译 Java 文件。


## ODBC

ODBC (Open Database Connectivity) 是微软公司提出的数据库连接标准，可以让应用程序通过 SQL 语句访问数据库，主要用于 C, C++, C# 等语言。

- `SQLAllocEnv(&env)` 分配环境句柄
- `SQLAllocConnect(env, &conn)` 分配连接句柄
- `SQLConnect(conn, "DSN", "username", "password")` 连接数据库
- `SQLDisconnect(conn)` 断开数据库连接
- `SQLFreeConnect(conn)` 释放连接句柄
- `SQLFreeEnv(env)` 释放环境句柄
- `SQLAllocStmt(conn, &stmt)` 分配语句句柄
- `SQLExecDirect(stmt, sql, SQL_NTS)` 执行 SQL 语句
- `SQLBindCol(stmt, 1, SQL_C_CHAR, buf, 100, &len)` 绑定结果集的第一个列到 buf
- `SQLFetch(stmt)` 获取结果集的下一行
- `SQLFreeStmt(stmt, SQL_DROP)` 释放语句句柄
- `SQLPrepare(stmt, sql, SQL_NTS)` 准备 SQL 语句
- `SQLBindParameter(stmt, 1, SQL_PARAM_INPUT, SQL_C_CHAR, SQL_CHAR, 100, 0, buf, 100, &len)` 绑定参数
- `SQLExecute(stmt)` 执行预处理语句
- `SQLSetConnectAttr(conn, SQL_ATTR_AUTOCOMMIT, SQL_AUTOCOMMIT_OFF, 0)` 关闭自动提交
- `SQLCommit(conn)` 提交事务
- `SQLRollback(conn)` 回滚事务



## Embedded SQL

连接数据库：

```C
EXEC SQL INCLUDE SQLCA;
EXEC SQL BEGIN DECLARE SECTION;
char name[20];
int age;
EXEC SQL END DECLARE SECTION;
EXEC SQL CONNECT TO database USER username USING password;
```


## 函数与过程

可以通过 `create function` 创建 SQL 函数，通过 `drop function` 删除 SQL 函数。

```sql
create function func_name (param1 type1, param2 type2, ...)
returns type
begin
    ...
end
```

```sql
drop function func_name
```



## 触发器

触发器 (Trigger) 是一个表达式，可以作为数据库被修改后的副作用。
