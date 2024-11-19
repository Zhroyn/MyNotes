
# 查询优化

## 等价规则

如果两个关系代数表达式会产生相同的元组集，则称它们是等价的。一条等价规则 (Equivalence Rule) 是一个将一个关系代数表达式转换为另一个等价的表达式的规则。

常见的等价规则有：

- 合取选择和选两次等价：$\sigma_{\theta_1 \land \theta_2}(E) = \sigma_{\theta_1}(\sigma_{\theta_2}(E))$
- 选择两次的顺序可以交换：$\sigma_{\theta_1}(\sigma_{\theta_2}(\cdots(E))) = \sigma_{\theta_2}(\sigma_{\theta_1}(E))$
- 嵌套的投影只需要看最外层的：$\Pi_{L_1}(\Pi_{L_2}(E)) = \Pi_{L_1}(E)$
- 选择和笛卡尔积可以变成 Theta-Join：$\sigma_{\theta}(E_1 \times E_2) = E_1 \Join_{\theta} E_2$
- Theta-Join 可以和选择合并：$\sigma_{\theta_1}(E_1 \Join_{\theta_2} E_2) = E_1 \Join_{\theta_1 \land \theta_2} E_2$
- Theta-­Join 和自然连接是可交换的：$E_1 \Join_{\theta} E_2 = E_2 \Join_{\theta} E_1$
- 自然连接的结合律：$(E_1 \Join E_2) \Join E_3 = E_1 \Join (E_2 \Join E_3)$
- Theta-Join 的结合律：$(E_1 \Join_{\theta_1} E_2) \Join_{\theta_2 \land \theta_3} E_3 = E_1 \Join_{\theta_1 \land \theta_3} (E_2 \Join_{\theta_2} E_3)$
    - $\theta_2$ 只涉及 $E_2$ 和 $E_3$ 的属性
- Theta-Join 关于选择的分配律：
    - $\sigma_{\theta_0} (E_1 \Join_{\theta} E_2) = \sigma_{\theta_0}(E_1) \Join_{\theta} E_2$
        - $\theta_0$ 只涉及 $E_1$ 的属性
    - $\sigma_{\theta_1 \land \theta_2} (E_1 \Join_{\theta} E_2) = \sigma_{\theta_1}(E_1) \Join_{\theta} \sigma_{\theta_2}(E_2)$
        - $\theta_1$ 只涉及 $E_1$ 的属性，$\theta_2$ 只涉及 $E_2$ 的属性
- Theta-Join 关于投影的分配律：
    - $\prod_{L_1 \cup L_2} (E_1 \Join_{\theta} E_2) = \prod_{L_1}(E_1) \Join_{\theta} \prod_{L_2}(E_2)$
        - $L_1$ 只涉及 $E_1$ 的属性，$L_2$ 只涉及 $E_2$ 的属性，$\theta$ 只涉及 $L_1$ 和 $L_2$
    - $\prod_{L_1 \cup L_2} (E_1 \Join_{\theta} E_2) = \prod_{L_1 \cup L_2} (\prod_{L_1 \cup L_3}(E_1) \Join_{\theta} \prod_{L_2 \cup L_4}(E_2))$
        - $L_3$ 是 $E_1$ 中除了 $L_1$ 之外的属性，$L_4$ 是 $E_2$ 中除了 $L_2$ 之外的属性，这个形式更加通用
- 全外连接是可交换的：$E_1 ⟗ E_2 = E_2 ⟗ E_1$
- 左外连接可以交换为右外连接：$E_1 ⟕ E_2 = E_2 ⟖ E_1$



<br>

## 代价估计

定义 $V(A, r)$ 为关系 $r$ 的属性 $A$ 上的不同值的数目，则 $\sigma_{A=v}(r)$ 选择出的元组数目的期望为 $n_r / V(A, r)$。