
- [关系模型](#关系模型)
    - [基本概念](#基本概念)
    - [键](#键)
    - [关系代数](#关系代数)
        - [附加操作](#附加操作)
        - [扩展操作](#扩展操作)
        - [多重集关系代数](#多重集关系代数)
    - [SQL 和关系代数](#sql-和关系代数)



# 关系模型

## 基本概念

给定集合 $D_1, D_2, \cdots, D_n$，一个关系 $r$ 就是 $D_1 \times D_2 \times \cdots \times D_n$ 的子集，它是一个 $n$ 元组的集合。

$A_1, A_2, \cdots, A_n$ 是**属性 (attribute)**，其可能取到的值的集合称为**域 (domain)**。属性的值需要是**原子的 (atomic)**。每个值域都包含一个特殊的值，称为**空值 (null)**。

$R = (A_1, A_2, \cdots, A_n)$ 是一个**关系模式 (relation schema)**，它定义了一个关系的属性集合，$r(R)$ 则是 $R$ 的一个**关系实例 (relation instance)**。

**数据库模式 (database schema)** 是数据库的逻辑设计，包括所有关系模式的集合。**数据库实例 (database instance)** 是数据库的一个具体的状态，包括所有关系实例的集合。



<br>

## 键

如果 $K\subseteq R$ 足以唯一地标识 $r(R)$ 中的元组，那么称 $K$ 是 $R$ 的一个**超键 (superkey)**，如 \{ID, Name\}。

如果一个超键 $K$ 是最小的，那么称 $K$ 是 $R$ 的一个**候选键 (candidate key)**，如 \{ID\}。候选键之一可以被选为**主键 (primary key)**。

若一个**外键 (foreign key)** 从关系 $r_1$ 的属性 $A$ 指向关系 $r_2$ 的主键 $B$，则该约束规定，在任意数据库实例上，$r_1$ 中每个元组的 $A$ 值也必须是 $r_2$ 中某个元组的 $B$ 值，其中 $r_1$ 是 Referencing relation，$r_2$ 是 Referenced relation。

**参照完整性 (Referential integrity)** 约束要求出现在引用关系 $r_1$ 中的任何元组的指定属性 $A$ 中的值也出现在被引用关系 $r_2$ 中的至少一个元组的指定属性 $B$ 中。

参照完整性约束是一个更广泛的术语，它包括了外键约束，比外键约束更弱，可以不是主键。在符号表示上，外键是单箭头，参照完整性是两个连在一起的箭头。




<br>

## 关系代数

形式化关系查询语言分为以下三种：

- **元组关系演算 (Tuple relational calculus)**
- **域关系演算 (Domain relational calculus)**
- **关系代数 (Relational algebra)** 描述了关系的操作，有六种基本操作：
    - 选择 (Select): $\sigma$
    - 投影 (Project): $\prod$
    - 并 (Union): $\cup$
    - 差 (Set Difference): $-$
    - 笛卡尔积 (Cartesian Product): $\times$
    - 重命名 (Rename): $\rho$

选择操作的定义为 $\sigma_p(r) = \{ t | t\in r \text{ and } p(t) \}$，其中 $p(t)$ 是一个**选择谓词 (selection predicate)**，它是一个关于 $t$ 的布尔表达式。

投影操作的定义为 $\prod_{A_1, A_2, \cdots, A_k}(r) = \{ t[A_1, A_2, \cdots, A_n] | t\in r \}$，其中 $A_1, A_2, \cdots, A_k$ 是 $r$ 的属性。

并操作的定义为 $r \cup s = \{ t | t\in r \text{ or } t\in s \}$，其中 $r$ 和 $s$ 必须有相同的**元数 (arity)**，属性的域也必须相容。

差操作的定义为 $r - s = \{ t | t\in r \text{ and } t\notin s \}$，其中 $r$ 和 $s$ 必须有相同的**元数 (arity)**，属性的域也必须相容。

笛卡尔积操作的定义为 $r \times s = \{ t_1, t_2 | t_1\in r \text{ and } t_2\in s \}$，其中 $r$ 和 $s$ 的属性必须是不相交的，否则必须使用重命名。

重命名操作的定义为 $\rho_x (E)$，会返回被重命名为 $x$ 的表达式 $E$。

!!! note 示例
    找到最多的薪水的查询可以写成 $\prod_{\text{salary}}(\text{instructor}) - \prod_{\text{instructor.salary}}(\sigma_{\text{instructor.salary} < \text{d.salary}}(\text{instructor} \times \rho_d(\text{instructor})))$

### 附加操作

附加操作可以用来简化查询，无法增加表达能力，包括：

- 交 (Set Intersection): $\cap$
- 自然连接 (Natural Join): $\Join$
- 外连接 (Outer Join): $⟕, ⟖, ⟗$
- 半连接 (Semijoin): $\ltimes$
- 赋值 (Assignment): $\leftarrow$
- 除 (Division): $\div$

交操作的定义为 $r \cap s = \{ t | t\in r \text{ and } t\in s \} = r - (r - s)$。

自然连接操作会匹配在相同属性上有相同值的元组，其定义为 $r \Join s = \prod_{r.A, r.B, r.C, r.D, s.E} (\sigma_{r.B=s.B \wedge r.D=s.D(r \times s)} (r \times s))$，其中 $R = (A, B, C, D), S = (B, D, E)$。

外连接操作会保留不匹配的元组，分为左外连接、右外连接和全外连接，其中左外连接可以被写为 $r ⟕ s = (r \Join s) \cup (r - \prod_R (r \Join s)) \times \{ (\text{null}, \cdots, \text{null}) \}$，全外连接可以被写为 $r ⟗ s = (r \Join s) \cup (r - \prod_R (r \Join s)) \times \{ (\text{null}, \cdots, \text{null}) \} \cup \{ (\text{null}, \cdots, \text{null}) \} \times (s - \prod_S (r \Join s))$。

theta 连接操作的定义为 $r \Join_{\theta} s = \sigma_{\theta}(r \times s)$，半连接操作的定义为 $r \ltimes_{\theta} s = \prod_R (r \Join_{\theta} s)$，可用于用外部表的信息进行筛选。

除操作是找到最大 $t(R - S)$，使得 $t \times s \subseteq r$，即 $r \div s =  \prod_{R-S}(r) - \prod_{R-S} (\prod_{R-S}(r) \times s - r)$。

!!! note 示例
    设

    $r(\text{ID}, \text{course\_id}) = \prod_{\text{id}, \text{course\_id}} (\text{takes})$

    $s(\text{course\_id}) = \prod_{\text{course\_id}} (\sigma_{\text{dept\_name="Biology"}} (\text{course}))$

    则 $r \div s$ 代表的就是选择了所有生物课的学生。

### 扩展操作

扩展操作可以增加表达能力，包括：

- **广义投影 (Generalized Projection)**，可以在投影中使用算术表达式
- **聚合函数 (Aggregate Functions)**，可以接受一系列值并返回单个值，包括 $\text{avg}$, $\min$, $\max$, $\text{sum}$, $\text{count}$
- **聚合操作 (Aggregate Operations)**，可以将关系代数表达式按照属性分组，然后根据聚合函数返回值，形式为 $_{G_1, \cdots, G_n} \mathcal{G}_{F_1(A_1), \cdots, F_n(A_n)} (E)$

!!! note 示例

    $_\text{dept\_name} \mathcal{G}_{\text{avg(salary)}} (\text{instructor})$ 会返回每个部门的平均薪水


### 多重集关系代数

**多重集关系代数 (multiset relational algebra)** 允许重复元素，可以提高效率，其操作有一些区别：

- 选择和投影操作不会去重
- 若 $r$ 和 $s$ 中各有 $m$ 和 $n$ 个副本，则叉积会产生 $m \times n$ 个副本
- 并：$m + n$ 个副本
- 交：$\min(m, n)$ 个副本
- 差：$\max(m - n, 0)$ 个副本



<br>

## SQL 和关系代数

在多重集关系代数中，

$\prod_{A_1, \cdots, A_n} \sigma_P (r_1 \times \cdots \times r_m) $ 等价于：

```sql
select A1, A2, ..., An
from r1, r2, ..., rm
where P
```

$_{A_1, A_2} \mathcal{G}_{\text{sum}(A_3)} \sigma_P (r_1 \times \cdots \times r_m) $ 等价于：

```sql
select A1, A2, sum(A3)
from r1, r2, ..., rm
where P
group by A1, A2
```

