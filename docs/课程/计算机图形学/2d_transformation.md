# 2D变换
## 2D线性变换

线性变换是能够用矩阵直接表示的变换，包括缩放、反射、剪切、旋转等，平移不是线性变换。

2D线性变换的基本形式是：

$$
\begin{pmatrix} x' \\ y' \end{pmatrix}
= \begin{pmatrix}
    a & b \\
    c & d
\end{pmatrix}
\begin{pmatrix} x \\ y \end{pmatrix}
$$

### 缩放
- 均匀缩放：

$$
\begin{pmatrix} x' \\ y' \end{pmatrix}
= \begin{pmatrix}
    s & 0 \\
    0 & s
\end{pmatrix}
\begin{pmatrix} x \\ y \end{pmatrix}
$$

- 非均匀缩放：

$$
\begin{pmatrix} x' \\ y' \end{pmatrix}
= \begin{pmatrix}
    s_x & 0 \\
    0 & s_y
\end{pmatrix}
\begin{pmatrix} x \\ y \end{pmatrix}
$$

### 反射
- 水平反射矩阵：

$$
\begin{pmatrix}
    -1 & 0 \\
    0 & 1
\end{pmatrix}
$$

### 剪切
- 水平剪切矩阵：

$$
\begin{pmatrix}
    1 & a \\
    0 & 1
\end{pmatrix}
$$

- 当 $y=0$ 时水平偏移为 $0$，$y=1$ 时水平偏移为 $a$。

### 旋转
- 绕原点逆时针旋转 $\theta$ 的矩阵：

$$
R(\theta) =
\begin{pmatrix}
    \cos\theta & -\sin\theta \\
    \sin\theta & \cos\theta
\end{pmatrix}
$$




<div style="margin-top: 60pt"></div>

## 齐次坐标与仿射变换
### 齐次坐标的引入

为了能够用矩阵乘法表示平移，引入齐次坐标，为普通2D点和2D向量添加一个新的维度：

- **2D点**：$(x, y, 1)^T$
- **2D向量**：$(x, y, 0)^T$
- **操作规则**：
    - 向量 + 向量 = 向量
    - 点 - 点 = 向量
    - 点 + 向量 = 点
    - 点 + 点 = 点（需归一化）

### 仿射变换的矩阵表示

仿射变换就是线性变换和平移的组合，可以用 $3 \times 3$ 矩阵表示：

$$
\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix}
= \begin{pmatrix}
    a & b & t_x \\
    c & d & t_y \\
    0 & 0 & 1
\end{pmatrix}
\begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$
