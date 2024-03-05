
## 数据库介绍

数据库由 DBMS (Database Management System) 管理，分为关系型数据库和非关系型数据库。

每个数据库系统需要做到以下几点：

- 定义存储结构
- 信息操作
- 安全性
- 并发控制

数据库系统解决的问题是：

- 数据冗余与不一致 (Data Redundancy and Inconsistency)，类似的数据存储在不同地方
- 数据孤立、数据孤岛 (Data isolation)，没有形成有机的结构
- 存取数据困难 (Accessing Data)，每个任务都要写个程序
- 完整性问题 (Integrity Problems)
    - 完整性指防止数据库中存在不符合语义规则的数据，避免错误的输入和输出
- 原子性问题 (Atomicity Problems)
    - 原子性指要么全部成功，要么全部失败
    - 可能中途掉电导致操作未完成，无法保证原子性
- 并发访问异常 (Concurrent Access Anomalies)
- 安全性问题 (Security Problems)
    - 认证 (Authentication)
    - 权限 (Privilege)
    - 审计 (Audit)

由此，数据库对应的特点是：

- 数据持久性 (Data Persistence)
- 数据访问便利性 (Convenience in Accessing Data)
- 数据完整性 (Data Integrity)
- 多用户并发控制 (Concurrency Control for multiple users)
- 故障恢复 (Failure Recovery)
- 安全控制 (Security Control)


<br>

## 数据模型

- 关系模型 (Relation Model)
- 基于对象的数据模型 (Object-based Data Model)
    - 面向对象数据模型 (Object-oriented)
    - 对象-关系数据模型 (Object-relational)
- 半结构化数据数据 (Semi-structured Data Model)
    - XML 数据模型
    - JSON 数据模型
- 其他老模型
    - 网状模型 (Network Model)
    - 层次模型 (Hierarchical Model)
- 实体-联系模型 (Entity-Relationship Model)，主要用于数据库设计



<br>

## 数据视图

数据视图有三种，可以隐藏复杂性，并增强适应变化的能力：

- 视图模式 (View Schema)，描述了用户所见到的数据
- 逻辑模式 (Logical Schema)，描述了数据的逻辑结构
- 物理模式 (Physical Schema)，描述了数据的物理存储结构

逻辑数据独立性指的是改变逻辑模式而不改变用户视图模式的能力，物理数据独立性指的是改变物理模式而不改变逻辑模式的能力。




<br>

## 数据语言

### 数据定义语言

DDL (Data Definition Language) 用于定义数据库的结构，包括表的创建、删除、修改等。

DDL 编译器会生成一个数据字典，用于存储数据库的元数据，其中包含：

- 数据库模式
- 完整性约束
    - 主键
    - 参照完整性
- 权限

### 数据操作语言

DML (Data Manipulation Language) 是一种用于操作数据库中数据的语言，也被称为查询语言，如 SQL Query Language。

分为**过程式 (Procedural)** 和**陈述式 (Declarative)**，其中 SQL 是使用最广泛的语言，属于陈述式。

SQL 并不强大，某些计算和行为必须通过宿主语言 (host language) 来实现，如 Python、Java、C 等。




<br>

## 数据库使用者

- Native User: 通过图形化界面使用
- Application Programmer: 使用 API 制作数据库应用
- Sophisticated User: 使用 DML 和系统交互
- Database Administrator: 协调数据库系统的所有活动，要对信息资源有深入的了解



<br>

## 数据库历史

历届图灵奖获得者有：

- Charles W. Bachman，网状数据库之父，任职美国通用电气，获得 1973 年图灵奖
- Edgar F. Codd，在 IBM 任职期间开创关系模型，获得 1981 年图灵奖
- Jim Gray 因为他对数据库和事务处理研究的开创性贡献获得 1998 年图灵奖
- Michael Stonebraker 因为他对现代数据库系统的概念和实践做出的贡献获得 2014 年图灵奖

