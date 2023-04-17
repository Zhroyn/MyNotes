








## 特征值和特征向量
### 定义及求解
**定义（不变子空间）**
设 $\sigma \in L(V)$，$U$ 为 $V$ 的子空间，
若 $\forall u \in U, \sigma(u) \in U $，则称 $U$ 是 $V$ 的不变子空间，并称 $V$ 的子空间 $U$ 在 $\sigma $ 下不变。
<br>

**定义（特征值和特征向量）** 
设 $\sigma \in L(V)$，若存在 $\lambda_0 \in F, \xi \in V$ 且 $\xi \neq 0$，使得 $$\sigma(\xi) = \lambda_0\xi $$ 则称 $\lambda_0$ 为 $\sigma$ 的一个特征值，$\xi$ 为 $\sigma $ 关于 $\lambda_0$ 的特征向量。

**定义（特征子空间）**
设 $V_{\lambda_0}$ 为 $\sigma$ 关于 $\lambda_0$ 的特征子空间，则：
$$V_{\lambda_0} = \text{null}(\lambda_0 I - \sigma) $$ 且有 $\text{dim}(\text{null}(\lambda_0I-\sigma)) \ge 1, \text{dim}(\text{range}(\lambda_0I-\sigma)) \le n - 1 $

若 $\sigma$ 关于基 $B$ 的矩阵为 $A$，则 $|\lambda_0E - A| = 0$。

**求特征值和特征向量**

$|\lambda E - A| = 0$ 在 $F$ 上的根 $\lambda_j$ 就是 $\sigma$ 的特征值，
$(\lambda_j E - A)X = 0 $ 的非零解就是 $\sigma$ 关于 $\lambda_j$ 的特征向量，
$(\lambda_j E - A)X = 0 $ 的解空间就是 $\sigma$ 关于 $\lambda_j$ 的特征子空间。

通常把方程 $|\lambda E - A| = 0$ 叫做矩阵 $A$ 的特征方程，
把 $\lambda$ 的 $n$ 次多项式 $f(\lambda) = |\lambda E - A| $ 叫做矩阵 $A$ 的特征多项式。
若域 $F$ 是复数域 $C$，则 $n$ 阶矩阵的特征多项式在复数域上的 $n$ 个根都是矩阵的特征值，其 $k$ 重根叫做 $k$ 重特征值。

$\Rightarrow$ $n$ 阶对角矩阵、上（下）三角矩阵的特征值就是其 $n$ 个主对角元。

### 其他性质
**定理：** $n$ 阶矩阵 $A$ 的特征多项式为
$$f(\lambda) = \lambda^n + b_1\lambda^{n-1} + \cdots + b_{n-1}\lambda + b_n $$ 其中 $b_k = (-1)^k S_k $，$S_k$ 为 $A$ 的全体 $k$ 阶主子式之和。
$\Rightarrow \displaystyle \sum_{i=1}^n \lambda_i = \sum_{i=1}^n a_{ii},\; \prod_{i=1}^n \lambda_i = |A| $

**定理：** 若矩阵 $A$ 与 $B$ 相似，则其特征多项式相等，即 $|\lambda E - A| = |\lambda E - B| $
$\Rightarrow $ 同一线性映射在不同基下的矩阵的特征值相同。




