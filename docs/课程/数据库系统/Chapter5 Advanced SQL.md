
# 高级 SQL

## JDBC

JDBC (Java Database Connectivity) 是 Java 语言访问数据库的标准接口，提供了一种访问数据库管理系统的标准方法。开发人员可以编写 Java 应用程序，通过 JDBC API 访问数据库。

### 常见 API

连接对象可以通过 `Connection conn = DriverManager.getConnection(username, userid, password)` 来创建，用于连接数据库，其方法有：

- `conn.close()` 关闭数据库连接
- `conn.setAutoCommit(false)` 关闭自动提交
- `conn.commit()` 提交事务
- `conn.rollback()` 回滚事务

表达式对象可以通过 `Statement stmt = conn.createStatement()` 来创建，用于执行 SQL 语句，其方法有：

- `stmt.close()` 关闭表达式对象
- `stmt.executeUpdate(sql)` 执行更新数据库的 SQL 语句
- `ResultSet rs_= stmt.executeQuery(sql)` 执行查询数据库的 SQL 语句

结果集 `ResultSet` 是 SQL 语句的返回类型，用于存储查询结果，其方法有：

- `rs.next()` 移动到下一行，若有数据则返回 true。初始时指向第一行之前
- `rs.getString(i)` 获取当前行第 i 个字段（为字符串类型）的值
- `rs.getString(name)` 获取当前行名为 name 的字段的值

预处理表达式对象可以通过 `PreparedStatement pStmt = conn.prepareStatement(sql)` 来创建。它对语句进行预编译，可以提高执行效率。而且，由于不是直接拼接 SQL 语句，预处理表达式可以有效防御 SQL 注入攻击。其方法有：

- `pStmt.setInt(1, 100)` 设置第一个参数的值为 100
- `pStmt.executeUpdate()` 执行预处理表达式对象
- `ResultSet rs_= pStmt.executeQuery()` 执行查询预处理表达式对象

### SQL 注入

在使用如下语句时：

```java
String sql = "SELECT * FROM book WHERE title = '" + title + "'";
```

如果用户输入的 `title` 是 `'; DROP TABLE book; --`，那么最终的 SQL 语句就会变成：

```sql
SELECT * FROM book WHERE title = ''; DROP TABLE book; --'
```

显然该语句不是我们想要的，如果成功执行会造成巨大的损失，这种攻击方式就是 SQL 注入。为了防止 SQL 注入，需要尽量只使用预处理表达式。它会根据参数预设的类型，自动转义特殊字符，从而避免 SQL 注入。

### 元数据

数据库元数据可以通过 `DatabaseMetaData dbmd = conn.getMetaData()` 来获得，其方法有：

- `ResultSet rs = dbmd.getColumns(null, null, tableName, null)` 获取表的列信息。在该方法中，第一个参数是目录名称，第二个参数是模式名称，第三个参数是表名称，第四个参数是列名称

结果集元数据对象可以通过 `ResultSetMetaData rsmd = rs.getMetaData()` 来获得，其方法有：

- `rsmd.getColumnCount()` 获取结果集的列数
- `rsmd.getColumnName(i)` 获取第 i 个列的名称
- `rsmd.getColumnTypeName(i)` 获取第 i 个列的类型名称




<br>

## SQLJ

SQLJ 是 embeded SQL 的 Java 版本，与 JDBC 相比，SQLJ 是静态的，在编译时就会检查 SQL 语句的正确性。

SQLJ 语句以 `#sql` 开头，以 `;` 结尾，有声明语句和可执行语句两种类型。声明语句宣布连接环境和迭代器，其中连接环境被用于建立数据库连接，而迭代器被用于保存 SQL 查询的结果集。可执行语句则执行嵌入的 SQL 语句，通过 Java 变量在 Java 程序和数据库之间交换信息。

示例如下：

```sql
#sql iterator deptInfoIter (String dept name, int avgSal);
deptInfoIter iter = null;
#sql iter = { select dept_name, avg(salary) as_avgSal from instructor group by dept name };
while (iter.next()) {
    String deptName = iter.dept_name();
    int avgSal = iter.avgSal();
    System.out.println(deptName + " " + avgSal);
}
iter.close();
```




<br>

## ODBC

ODBC (Open Database Connectivity) 是微软公司提出的数据库连接标准，可以让应用程序通过 SQL 语句访问数据库，主要用于 C, C++, C# 等语言。

连接数据库的 API 如下：

- `SQLAllocEnv(&env)` 分配环境句柄，存储到 `HENV env` 中
- `SQLAllocConnect(env, &conn)` 分配连接句柄，存储到 `HDBC conn` 中
- `SQLConnect(conn, DSN, SQL_NTS, username, SQL_NTS, password, SQL_NTS)` 连接数据库，其中 DSN 是数据源名称，SQL_NTS 是字符串终止符
- `SQLDisconnect(conn)` 断开数据库连接
- `SQLFreeConnect(conn)` 释放连接句柄
- `SQLFreeEnv(env)` 释放环境句柄

执行 SQL 语句并处理结果的 API 如下：

- `SQLAllocStmt(conn, &stmt)` 分配语句句柄，存储到 `HSTMT stmt` 中
- `SQLExecDirect(stmt, sql, SQL_NTS)` 执行 SQL 语句
- `SQLBindCol(stmt, 1, SQL_C_CHAR, department, 100, &len)` 绑定结果集到某个变量，其中第一个参数为表达式句柄，第二个参数为列号，第三个参数为数据类型，第四个参数为指向数据缓冲区的指针，第五个参数为数据缓冲区的长度，第六个参数为数据的实际长度
- `SQLFetch(stmt)` 获取结果集的下一行
- `SQLFreeStmt(stmt, SQL_DROP)` 释放语句句柄

执行预处理语句的 API 如下：

- `SQLPrepare(stmt, sql, SQL_NTS)` 准备 SQL 语句
- `SQLBindParameter(stmt, 1, SQL_PARAM_INPUT, SQL_C_CHAR, SQL_CHAR, 100, 0, buf, 100, &len)` 绑定参数
- `SQLExecute(stmt)` 执行预处理语句





<br>

## 函数

函数是一种封装了 SQL 语句的可重用代码块，可以接受参数并返回结果。函数可以分为标量函数和表值函数，不过 MySQL 不支持表值函数。创建函数的命令为 `CREATE FUNCTION`，删除函数的命令为 `DROP FUNCTION`。

标量函数示例如下：

```sql
CREATE FUNCTION dept_count(dept_name VARCHAR(20))
RETURNS INTEGER
BEGIN
    DECLARE d_count INTEGER;
    SELECT COUNT(*) INTO d_count
    FROM instructor
    WHERE instructor.dept_name = dept_name;
    RETURN d_count;
END;
```

表值函数示例如下：

```sql
CREATE FUNCTION instructors_of(dept_name VARCHAR(20))
RETURNS TABLE
BEGIN
    RETURN
    SELECT ID, name, dept_name, salary
    FROM instructor
    WHERE instructor.dept_name = dept_name;
END;
```

调用函数的示例如下：

```sql
-- 标量函数
SELECT dept_count('Biology') AS 'Biology Count';
SELECT * FROM instructor WHERE dept_count(dept_name) > 3;

-- 表值函数
SELECT * FROM TABLE(instructors_of('Biology'));
```

MySQL 可能会出于安全原因禁用函数，可以通过 `SET GLOBAL log_bin_trust_function_creators = 1` 来解决。




<br>

## 过程

过程和函数类似，但是过程可以不返回结果。创建过程的命令为 `CREATE PROCEDURE`，删除过程的命令为 `DROP PROCEDURE`。

下面将给出一个选课的过程示例，该过程接受学生 ID、课程 ID、课程号、学期和年份作为参数，如果课程没有满员，则将学生注册到该课程中，否则返回错误信息。

```sql
DELIMITER //

CREATE PROCEDURE take_course(
    IN student_id char(8),
    IN course_id char(8),
    IN course_year YEAR,
    IN semester VARCHAR(10),
    OUT errorMsg VARCHAR(100)
)
BEGIN
    IF NOT EXISTS (SELECT * FROM student WHERE student.student_id = student_id) THEN
        SET errorMsg = 'Student not found.';
    ELSEIF NOT EXISTS (SELECT * FROM course WHERE course.course_id = course_id) THEN
        SET errorMsg = 'Course not found.';
    ELSEIF EXISTS (SELECT * FROM takes WHERE takes.student_id = student_id AND takes.course_id = course_id AND takes.course_year = course_year AND takes.semester = semester) THEN
        SET errorMsg = 'Course already taken.';
    ELSE
        INSERT INTO takes VALUES (student_id, course_id, course_year, semester);
        SET errorMsg = 'Course taken successfully.';
    END IF;
END //

DELIMITER ;
```

调用过程的示例如下：

```sql
CALL take_course('S1000001', 'C1000001', 2021, 'Fall', @errorMsg);
SELECT @errorMsg;
```




<br>

## 触发器

触发器 (Trigger) 是一种特殊的存储过程，它会在数据库中的某个表上执行特定的操作时自动触发。触发器可以在 `INSERT`、`UPDATE` 或 `DELETE` 时执行，触发时机可以是 `BEFORE` 或 `AFTER`。

创建触发器的命令为 `CREATE TRIGGER`，删除触发器的命令为 `DROP TRIGGER`，一个示例如下：

```sql
DELIMITER //

CREATE TRIGGER depositor_insert AFTER INSERT ON depositor
REFERENCING NEW ROW AS nrow
FOR EACH ROW
BEGIN
    INSERT INTO branch_cust
        SELECT branch_name, nrow.customer_name
        FROM account
        WHERE account.account_number = nrow.account_number;
END //

CREATE TRIGGER on_delete_cascade AFTER DELETE ON s
REFERENCING OLD ROW AS orow
FOR EACH ROW
BEGIN
    DELETE FROM r
    WHERE r.B = orow.A;
END //

DELIMITER ;
```
