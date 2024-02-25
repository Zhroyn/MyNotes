
- [线性方程组](#线性方程组)
    - [齐次线性方程组](#齐次线性方程组)
    - [非齐次线性方程组](#非齐次线性方程组)




### 线性方程组
#### 齐次线性方程组
**定理：解空间的维数**
设 $A\in M_{m\times n}(F)$，$\text{r}(A) = r$，
则齐次线性方程组的解空间 $N(A)$ 的维数 $\dim N(A) = \dim(\text{null}A) = n-r$

记解空间的基 $X_1,X_2,\cdots,X_{n-r}$ 为线性方程组 $AX=b$ 的基础解系

记 $R(A)$ 为 $n$ 个列向量张成的列空间，$R(A^T)$ 为 $m$ 个行向量张成的行空间，
则由 $\dim R(A^T) + \dim N(A) = n$ 可得，$N(A) = (R(A^T))^{\perp}$

**例题**
设 $A$ 是 $m\times n$ 实矩阵，证明：$r(A^TA)=r(A)$

$\text{Proof :}$
显然 $\text{r}(A^TA) \le \text{r}(A) $，故只需证 $\text{r}(A^TA) \ge \text{r}(A) $，即证 $N(A^TA) \subseteq N(A)$，
$(A^TA)\bm{X} = 0 \\
\Rightarrow \bm{X}^T(A^TA)\bm{X} = 0 \\
\Rightarrow (\bm{X}^TA^T)(A\bm{X}) = 0 \\
\Rightarrow |A\bm{X}|^2 = 0 \\
\Rightarrow A\bm{X} = 0 $

#### 非齐次线性方程组
非齐次线性方程组 $A\bm{X} = \bm{b}$ 的一般解为 $\bm{X} = \bm{X_0 + \overline X}$，
其中 $X_0$ 为 $A\bm{X} = \bm{b}$ 的一个特解，$\overline{X}$ 为 $A\bm{X} = 0$ 的一般解。

对于非齐次线性方程组，下列命题等价：
$\pod 1\; A\bm{X} = \bm{b}$有解
$\pod 2\; b\in R(A)$
$\pod 3\; \text{r}(A, \bm{b}) = \text{r}(A)$


