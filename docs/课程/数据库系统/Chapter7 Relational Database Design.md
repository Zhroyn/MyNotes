
# 关系数据库设计

## 分解

坏的关系模式设计会导致：

- 数据冗余 (Information repetition)
- 插入异常 (Insertion anomalies)
- 更新困难 (Update difficulty)

为此，常常需要将结合在一起的表分解为多个表。

设一个关系模式为 $R$，一个分解就是 $R = R_1 \cup R_2$，分解可以分为两种情况：

- 有损分解 (lossy decomposition): $r \subset \prod_{R_1}(r) \Join \prod_{R_2}(r)$
- 无损分解 (lossless decomposition): $r = \prod_{R_1}(r) \Join \prod_{R_2}(r)$

有损分解会增加不确定性，损失信息，无法从分解后的表重建原来的表。

无损分解要求分解所使用的公共属性是超键，即至少满足下列条件之一：

- $R_1 \cap R_2 \rightarrow R_1$
- $R_1 \cap R_2 \rightarrow R_2$

在本章节中，我们将学会判断一个关系是否是一个好的范式，若不好则对其进行无损分解，变成相应的规范范式 (Normal Form, NF)。规范范式有：1NF -> 2NF -> 3NF -> BCNF -> 4NF。




<br>

## 函数依赖

函数依赖 (Functional Dependency) 是键的更广泛的概念。

设 $\alpha \subseteq R, \beta \subseteq R$，若对任意元组 $t_1, t_2 \in r(R)$，有 $t_1[\alpha] = t_2[\alpha] \Rightarrow t_1[\beta] = t_2[\beta]$，则称 $\beta$ 函数依赖于 $\alpha$，即 $\alpha \rightarrow \beta$。

有了函数依赖以后，可以很快得到以下定义：

- 若 $K \rightarrow R$，则称 $K$ 为超键 (superkey)。
- 若 $K \rightarrow R$ 且不存在 $\alpha \subset K$ 使得 $\alpha \rightarrow R$，则称 $K$ 为候选键 (candidate key)。
- 若 $\beta \subseteq \alpha$，则称 $\alpha \rightarrow \beta$ 是频繁的 (trivial)，通常需要排除。



<br>

## 闭包

函数依赖集 $F$ 的闭包 (Closure) 是指可以从 $F$ 推导出来的所有函数依赖的集合，记为 $F^+$。

我们可以通过不断应用 Armstrong 公理 (Armstrong's Axioms) 来求闭包：

- 自反律 (Reflexivity): 若 $\beta \subseteq \alpha$，则 $\alpha \rightarrow \beta$
- 增广律 (Augmentation): 若 $\alpha \rightarrow \beta$，则 $\gamma\alpha \rightarrow \gamma\beta$
- 传递律 (Transitivity): 若 $\alpha \rightarrow \beta$ 且 $\beta \rightarrow \gamma$，则 $\alpha \rightarrow \gamma$

这些规则是有效 (Sound) 且完备 (Complete) 的，即推出的函数依赖是正确的，且可以推出所有函数依赖。

可以从中推理出来的额外的规则有：

- 合并律 (Union): 若 $\alpha \rightarrow \beta$ 且 $\alpha \rightarrow \gamma$，则 $\alpha \rightarrow \beta\gamma$
- 分解律 (Decomposition): 若 $\alpha \rightarrow \beta\gamma$，则 $\alpha \rightarrow \beta$ 且 $\alpha \rightarrow \gamma$
- 伪传递律 (Pseudo-Transitivity): 若 $\alpha \rightarrow \beta$ 且 $\gamma\beta \rightarrow \delta$，则 $\alpha\gamma \rightarrow \delta$

属性集 $\alpha$ 的闭包是指可以从 $\alpha$ 中的属性和 $F$ 中的函数依赖得到的所有属性的集合，记为 $\alpha^+$。

属性闭包的作用有：

- 判断超键：若 $\alpha^+ = R$，则 $\alpha$ 是超键。
- 判断函数依赖：若 $\beta \subseteq \alpha^+$，则 $\alpha \rightarrow \beta$。
- 计算函数依赖闭包：先求出所有属性组合的闭包，然后将这些闭包变成函数依赖，再对这些函数依赖应用分解律。以 $R(A,B,C), F=\{A\rightarrow B, B\rightarrow C\}$ 为例：
    - 先得到属性闭包：$A^+ = ABC, B^+ = BC, C^+ = C, (AB)^+ = ABC, (AC)^+ = ABC, (BC)^+ = BC, (ABC)^+ = ABC$
    - 再得到函数依赖：$A\rightarrow ABC, B\rightarrow BC, C\rightarrow C, AB\rightarrow ABC, AC\rightarrow ABC, BC\rightarrow BC, ABC\rightarrow ABC$
    - 对每一条函数依赖应用分解律，即可得到最终的 $F^+$




<br>

## 正则覆盖

$F$ 的正则覆盖 (Canonical Cover) 是指一个最小的可以推出 $F$ 的函数依赖集合，是对 $F$ 的化简，记为 $F_c$。

设 $\alpha\rightarrow \beta \in F$，若属性 $A \in \alpha$ 且 $F$ 逻辑蕴含 $(F - \{\alpha\rightarrow \beta\}) \cup \{(\alpha-A)\rightarrow \beta\}$，或者 $A \in \beta$ 且 $F$ 逻辑蕴含 $(F - \{\alpha\rightarrow \beta\}) \cup \{\alpha \rightarrow (\beta - A)\}$，则称 $A$ 为无关属性 (Extraneous Attributes)。

$F_c$ 的性质为：

- $F$ 逻辑蕴涵 $F_c$
- $F_c$ 逻辑蕴涵 $F$
- $F_c$ 中所有的函数依赖都不包含无关属性
- $F_c$ 中的函数依赖的左侧是唯一的

计算正则覆盖就是不断合并左侧以及去除无关属性的过程：

1. 对 $F$ 中的所有函数依赖应用合并律，用 $\alpha_1 \rightarrow \beta_1 \beta_2$ 代替 $\alpha_1 \rightarrow \beta_1$ 和 $\alpha_1 \rightarrow \beta_2$
2. 找到包含无关属性的函数依赖，将无关属性从其中删除
3. 若 $F$ 未被改变，则结束过程，否则重新开始

以 $F = \{ A\rightarrow B, B\rightarrow C, A\rightarrow C \}$ 为例，在第一步过后，$F$ 会变为 $\{ A\rightarrow BC, B\rightarrow C \}$，此时 $A\rightarrow BC$ 中的 $C$ 是无关属性，删去后 $F$ 变为 $\{ A\rightarrow B, B\rightarrow C \}$，此时无法合并也没有无关属性，算法结束。

不过在实际中，与其按照算法一步步执行，不如直接画图表示 $F$，这样效率更高。





<br>

## Boyce-Codd 范式

设 $R$ 是一个关系模式，$F$ 是 $R$ 上的函数依赖集合，若 $R$ 满足 BCNF，则对任意 $\alpha \rightarrow \beta \in F^+$，下面的条件至少有一条成立：

- $\alpha \rightarrow \beta$ 是频繁的
- $\alpha$ 是 $R$ 的超键

BCNF 分解算法就是，若有关系模式 $R_i$ 不符合 BCNF，则找到其中一个非频繁函数依赖 $\alpha \rightarrow \beta$，满足 $\alpha^+ \neq R_i$ 和 $\alpha \cap \beta = \empty$，然后将 $R_i$ 分解为 $R_i - \beta$ 和 $(\alpha, \beta)$。因为 $(R_i - \beta) \cap (\alpha, \beta) = \alpha \rightarrow (\alpha, \beta)$，所以这是一个无损分解。

这样的一个函数依赖是一定可以找到的，首先显然可以找到一个不满足上述两个条件的 $\alpha \rightarrow \beta$，易得 $\alpha^+ \neq R_i$ 成立，此时若 $\alpha \cap \beta = \empty$，则成功找到，若 $\alpha \cap \beta \neq \empty$，则使用 $\alpha \rightarrow (\beta - \alpha)$，然后成功找到。

### 依赖保持

依赖保持 (Dependency Preservation) 指的是在分解后，原来的每一个函数依赖都可以通过单一关系上的函数依赖得到检验或者推导得到。设 $F_i$ 为 $F^+$ 在 $R_i$ 上的函数依赖集合，则一个分解是依赖保持的的条件是：

$$ (F_1, F_2, \cdots, F_n)^+ = F^+ $$

以 $R = \{ A, B, C \}$，$F = \{ A\rightarrow B, B\rightarrow C \}$ 为例，$R_1 = \{A, B\}, R_2 = \{B, C\}$ 就是依赖保持的，而 $R_1 = \{A, B\}, R_2 = \{A, C\}$ 不是依赖保持的。

我们并不能保证 BCNF 分解是依赖保持的，例如 $F = \{ A\rightarrow C, B\rightarrow C \}$，因此需要引入第三范式。




<br>

## 第三范式

设 $R$ 是一个关系模式，$F$ 是 $R$ 上的函数依赖集合，若 $R$ 满足 3NF，则对任意 $\alpha \rightarrow \beta \in F^+$，下面的条件至少有一条成立：

- $\alpha \rightarrow \beta$ 是频繁的
- $\alpha$ 是 $R$ 的超键
- $\beta - \alpha$ 中的每一个属性都属于 $R$ 的一个候选键

以 $R(A, B, C), F = \{ AC\rightarrow B, B\rightarrow C \}$ 为例，$AC\rightarrow B$ 满足第二个条件，$B\rightarrow C$ 满足第三个条件，符合第三范式。需要注意的是，此时 $B$ 和 $C$ 的同时存在会导致 $R$ 会产生冗余。

3NF 分解算法为：

```verilog
Let Fc be a canonical cover for F

i = 0
for each functional dependency a->b in Fc do
begin
    i = i + 1
    Ri = (a, b)
end

if none of the schemas Rj, 1 <= j <= i contains a candidate key for R then
begin
    i = i + 1
    Ri = any candidate key for R
end

/* remove redundant relations */
repeat
    if any schema Rj is contained in another schema Rk then
    begin   /* delete Rj  */
        Rj = Ri
        i = i - 1
    end
until no more Rj s can be deleted

return (R1, R2, ..., Ri)
```

以 $F = \{ A\rightarrow C, B\rightarrow C \}$ 为例，第一个阶段后会得到 $R_1 = AC, R_2 = BC$，第二阶段后又会得到 $R_3 = R_4 = AB$，第三个阶段去掉重复的关系模式后，即可得到 $(AC, BC, AB)$。
