<!-- TOC -->

- [正交变换与正交矩阵](#正交变换与正交矩阵)
  - [定义及性质](#定义及性质)
  - [Q-R 分解](#q-r-分解)
  - [哈达马（Hadamard）定理](#哈达马hadamard定理)
- [特征值和特征向量](#特征值和特征向量)
  - [定义](#定义)
  - [求特征值和特征向量](#求特征值和特征向量)
  - [其他性质](#其他性质)

<!-- /TOC -->





##  正交变换与正交矩阵
### 定义及性质
**定义（正交变换）**
设 $\sigma \in V(\mathbf{R})$，若 $\forall \alpha, \beta \in V$，都有
$$(\sigma(\alpha), \sigma(\beta)) = (\alpha, \beta) $$ 则称 $\sigma$ 为一个正交变换。

**正交变换的性质：角度不变等价于长度不变**
$\forall \alpha, \beta \in V, (\sigma(\alpha), \sigma(\beta)) = (\alpha, \beta) \iff \forall \alpha \in V, |\sigma(\alpha)| = |\alpha| $
$\text{Proof :} $ 
必要性：取 $\alpha = \beta$，则由 $(\sigma(\alpha), \sigma(\alpha)) = (\alpha, \alpha) $，可得 $|\sigma(\alpha)|^2 = |\alpha|^2$
充分性：设 $|\sigma(\alpha + \beta)| = |\alpha + \beta| $，则由
$$|\sigma(\alpha + \beta)|^2 = |\sigma(\alpha)|^2 + |\sigma(\beta)|^2 + 2(\sigma(\alpha), \sigma(\beta)) \\
|\alpha + \beta|^2 = |\alpha|^2 + |\beta|^2 + 2(\alpha, \beta) $$ 可得 $(\sigma(\alpha), \sigma(\beta)) = (\alpha, \beta)$。

**定义（正交矩阵）**
欧氏空间 $V(\mathbf{R})$ 的正交变换 $\sigma$ 在 $V$ 的单位正交基所对应的矩阵 $A$ 称为正交矩阵。




**定理：判断是否为单位正交基的充要条件**
$n$ 阶实矩阵的列向量组是 $\mathbf{R}^n$ 的一组单位正交基的充要条件是 $A^TA = E $

**定理：正交矩阵的性质**
若 $A$ 是正交变换 $\sigma$ 是关于单位正交基 $\{\epsilon_1, \epsilon_2, \cdots, \epsilon_n\}$ 的正交矩阵，则 $A$ 的列向量组是一组单位正交基。
$$\text{Proof :} \hspace{11cm} \\ 
\displaystyle
\begin{aligned}
    (\epsilon_i, \epsilon_j) &= (\sigma(\epsilon_i), \sigma(\epsilon_j)) = (\sum_{k=1}^n a_{ki}\epsilon_k, \sum_{l=1}^n a_{li}\epsilon_l) \\
    &= \sum_{k=1}^n a_{ki}a_{kj} = (\alpha_i, \alpha_j) = \delta_{ij}
\end{aligned} $$

若 $A$ 的列向量组 $\alpha_1, \alpha_2, \cdots, \alpha_n $ 是 $\mathbf{R}^n$ 的一组单位正交基，则 $A$ 在 $V$ 的单位正交基 $\{\epsilon_1, \epsilon_2, \cdots, \epsilon_n\}$ 下所对应的线性变换 $\sigma$ 是正交变换。
$$\text{Proof :} \hspace{11cm} \\ 
\displaystyle
\begin{aligned}
    (\sigma(\epsilon_i), \sigma(\epsilon_j)) &= (\sum_{k=1}^n a_{ki}\epsilon_k, \sum_{l=1}^n a_{li}\epsilon_l) \\
    &= \sum_{k=1}^n a_{ki}a_{kj} = (\alpha_i, \alpha_j) = \delta_{ij}
\end{aligned} \\
\begin{aligned}
    (\sigma(\alpha), \sigma(\beta)) &= (\sum_{i=1}^n a_{i}\sigma(\epsilon_i), \sum_{j=1}^n b_{j}\sigma(\epsilon_j)) \\
    &= \sum_{i=1}^n a_{i}b_{i} = (\alpha, \beta)
\end{aligned} $$

综上，若 $n$ 阶实矩阵的列向量组是 $\mathbf{R}^n$ 的一组单位正交基或 $A^TA = E $，则称 $A$ 为正交矩阵。
正交矩阵有如下性质：
1. 若 $A$ 为正交矩阵，则 $A^{-1} = A^T $ 也为正交矩阵
2. 若 $A$ 为正交矩阵，则 $|A| = \pm 1 $
   - 行列式为 $+1$ 的正交矩阵所对应的正交变换称为第一类正交变换，如旋转变换
   - 行列式为 $-1$ 的正交矩阵所对应的正交变换称为第二类正交变换，如镜像变换
3. 若 $A, B$ 为正交矩阵，则 $AB $ 也为正交矩阵


### Q-R 分解
若 $A$ 为可逆实矩阵，则存在正交矩阵 $Q$ 和主对角元为正数的上三角阵 $R$，使得
$$A=QR $$

$$
\text{Proof :} \hspace{11cm} \\
\left\{
\begin{aligned}
  &\alpha_1 = \beta_1 \\
  &\alpha_2 = \beta_2 - k_{12}\beta_1 \\
  &\cdots \\
  &\alpha_n = \beta_n - k_{1n}\beta_1 - k_{2n}\beta_2 - \cdots - k_{n-1,n}\beta_{n-1} \\
\end{aligned}
\right.
\\~\\
A = (\beta_1, \beta_2, \cdots, \beta_n)
\begin{pmatrix}
  1 & -k_{12} & \cdots & -k_{1n} \\
  0 & 1 & \cdots & -k_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  0 & 0 & \cdots & 1 \\
\end{pmatrix}
\\~\\
= (\frac{\beta_1}{|\beta_1|}, \frac{\beta_2}{|\beta_2|}, \cdots, \frac{\beta_n}{|\beta_n|})
\begin{pmatrix}
  |\beta_1| & -t_{12} & \cdots & -t_{1n} \\
  0 & |\beta_2| & \cdots & -t_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  0 & 0 & \cdots & |\beta_n| \\
\end{pmatrix}
\\~\\
= QR
$$

### 哈达马（Hadamard）定理
若 $A$ 为 $n$ 阶实矩阵，则
$$|\text{det} A| \le \prod_{i=1}^{n}|\alpha_i| $$ 等号成立当且仅当 $\alpha_1, \alpha_2, \cdots, \alpha_n $ 为正交向量组。
几何意义：欧氏空间中多面体体积小于等于所有邻边之积。

$\text{Proof :}$
若 $A$ 不可逆，则定理成立；
若 $A$ 可逆，则 $A = QR$，所以 $\displaystyle \det A= \det R = \prod_{i=1}^{n}|\beta_i| $，
由勾股定理得，$|\beta_i| \le |\alpha_i| $，
故 $\displaystyle |\text{det} A| \le \prod_{i=1}^{n}|\alpha_i|$






## 特征值和特征向量
### 定义
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

### 求特征值和特征向量

$|\lambda E - A| = 0$ 在 $F$ 上的根 $\lambda_j$ 就是 $\sigma$ 的特征值，
$(\lambda_j E - A)X = 0 $ 的非零解就是 $\sigma$ 关于 $\lambda_j$ 的特征向量，
$(\lambda_j E - A)X = 0 $ 的解空间就是 $\sigma$ 关于 $\lambda_j$ 的特征子空间。

通常把方程 $|\lambda E - A| = 0$ 叫做矩阵 $A$ 的特征方程，
把 $\lambda$ 的 $n$ 次多项式 $f(\lambda) = |\lambda E - A| $ 叫做矩阵 $A$ 的特征多项式。
$n$ 阶复矩阵的特征多项式在复数域上的 $n$ 个根都是矩阵的特征值，其 $k$ 重根叫做 $k$ 重特征值。

$\Rightarrow$ $n$ 阶对角矩阵、上（下）三角矩阵的特征值就是其 $n$ 个主对角元。

### 其他性质
**定理：** $n$ 阶矩阵 $A$ 的特征多项式为
$$f(\lambda) = \lambda^n + b_1\lambda^{n-1} + \cdots + b_{n-1}\lambda + b_n $$ 其中 $b_k = (-1)^k S_k $，$S_k$ 为 $A$ 的全体 $k$ 阶主子式之和。
$\Rightarrow \displaystyle \sum_{i=1}^n \lambda_i = \sum_{i=1}^n a_{ii},\; \prod_{i=1}^n \lambda_i = |A| $

**定理：** 若矩阵 $A$ 与 $B$ 相似，则其特征多项式相等，即 $|\lambda E - A| = |\lambda E - B| $
$\Rightarrow $ 同一线性映射在不同基下的矩阵的特征值相同。




