
- [矩阵](#矩阵)
    - [线性映射的矩阵表示](#线性映射的矩阵表示)
    - [基的变换矩阵与坐标变换](#基的变换矩阵与坐标变换)
    - [矩阵的秩](#矩阵的秩)
    - [矩阵的高阶幂](#矩阵的高阶幂)
        - [三角形式](#三角形式)
        - [指数形式（矩阵秩为1）](#指数形式矩阵秩为1)
        - [阶梯形式](#阶梯形式)
        - [例题](#例题)
    - [矩阵求逆](#矩阵求逆)
        - [零化多项式](#零化多项式)
        - [三角块方阵](#三角块方阵)
        - [加边法](#加边法)
        - [伴随矩阵法](#伴随矩阵法)
        - [例题](#例题-1)
    - [其他](#其他)







## 矩阵
### 线性映射的矩阵表示
设 $B_1 = \left\{ \epsilon_1, \epsilon_2,\cdots ,\epsilon_n \right\} $ 是 $V_1(F)$ 的基，$B_2 = \left\{ e_1, e_2, \cdots , e_m \right\}$ 是 $V_2(F)$ 的基，
设 $\sigma \in L(V_1, V_2)$，$A$ 是 $\sigma$ 关于基 $B_1$ 和 $B_2$ 的矩阵，
则有
$$
\left\{
    \begin{aligned}
  &\sigma(\epsilon_1) = a_{11}e_1 + a_{21}e_2 + \cdots + a_{m1}e_m \\
  &\sigma(\epsilon_1) = a_{12}e_1 + a_{22}e_2 + \cdots + a_{m2}e_m \\
  &\cdots \; \cdots \\
  &\sigma(\epsilon_1) = a_{1n}e_1 + a_{2m}e_2 + \cdots + a_{mn}e_m \\
\end{aligned}
\right. 
\\~\\
(\sigma(\epsilon_1), \sigma(\epsilon_2), \cdots ,\sigma(\epsilon_n)) = (e_1, e_2, \cdots ,e_m) A
\\~\\
\sigma(\epsilon_1, \epsilon_2, \cdots ,\epsilon_n) = (e_1, e_2, \cdots ,e_m) A
$$

设 $\alpha \in V_1, \beta \in V_2$，且 $\alpha = (\epsilon_1, \epsilon_2, \cdots ,\epsilon_n)X, \beta = (e_1, e_2, \cdots, e_m)Y$，
则有
$$
\begin{aligned}
  \sigma\left( (\epsilon_1, \epsilon_2, \cdots, \epsilon_n)X \right) 
  & = \sigma(\epsilon_1, \epsilon_2, \cdots, \epsilon_n)X \\
  & = (e_1, e_2, \cdots, e_m)AX \\
  & = (e_1, e_2, \cdots, e_m)Y
\end{aligned}
\\~\\
\Rightarrow Y = AX
$$

若 $A$ 是 $\sigma$ 关于规范正交基 $\left\{ e_1, \cdots, e_n \right\}$ 的矩阵，则由
$$\sigma(e_1, \cdots, e_n) = (e_1, \cdots, e_n)A = EA = A $$ 可得 $A = (\sigma(e_1), \cdots, \sigma(e_n)) $

故，易得，逆时针旋转 $\theta$ 角关于规范正交基的矩阵 $A = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} $


### 基的变换矩阵与坐标变换
设 $B_1 = \left\{ \alpha_1, \alpha_2, \cdots, \alpha_n \right\} $，$B_2 = \left\{ \beta_1, \beta_2, \cdots, \beta_n \right\}$ 与 $B_3 = \left\{ e_1, e_2, \cdots, e_n \right\}$ 是 $V(F)$ 的三组基，
设 $A$ 是基 $B_1$ 变为基 $B_2$ 的变换矩阵，$B$ 是基 $B_2$ 变为基 $B_3$ 的变换矩阵，则有
$$
(\beta_1, \beta_2, \cdots, \beta_n) = (\alpha_1, \alpha_2, \cdots, \alpha_n) A \\
(e_1, e_2, \cdots, e_n) = (\beta_1, \beta_2, \cdots, \beta_n) B \\
(e_1, e_2, \cdots, e_n) = (\alpha_1, \alpha_2, \cdots, \alpha_n) AB
$$

设对 $\xi \in V$，有
$$\xi = (\alpha_1, \alpha_2, \cdots, \alpha_n)X = (\beta_1, \beta_2, \cdots, \beta_n)Y = (e_1, e_2, \cdots, e_n)Z $$ 则有
$$
\begin{aligned}
  (e_1, e_2, \cdots, e_n)Z
  &= (\beta_1, \beta_2, \cdots, \beta_n)BZ = (\beta_1, \beta_2, \cdots, \beta_n)Y \\
  &= (\alpha_1, \alpha_2, \cdots, \alpha_n)ABZ = (\alpha_1, \alpha_2, \cdots, \alpha_n)X \\
\end{aligned}
\\~\\
\Rightarrow Z = B^{-1}Y = B^{-1}A^{-1}X
$$


### 矩阵的秩
$$
r(A+B) \le r(A) + r(B) \\
r(AB) \le min(r(A), r(B)) \\
~\\
若P，Q分别是m，n阶可逆矩阵，A为m\times n矩阵，则 \\
r(PA) = r(AQ) = r(PAQ) = r(A) \\
~\\
r(A) + r(B) \le r\begin{pmatrix}A & C \\ O & B\end{pmatrix}
\le r(A) + r(B) + r(C)
$$

### 矩阵的高阶幂
#### 三角形式
$$
\begin{pmatrix}
    \cos \phi & -\sin \phi \\
    \sin \phi & \cos \phi
\end{pmatrix}^n =
\begin{pmatrix}
    \cos n\phi & -\sin n\phi \\
    \sin n\phi & \cos n\phi
\end{pmatrix}\\
~\\
\begin{pmatrix}
    \cos \phi & \sin \phi \\
    -\sin \phi & \cos \phi
\end{pmatrix}^n = 
\begin{pmatrix}
    \cos n\phi & \sin n\phi \\
    -\sin n\phi & \cos n\phi
\end{pmatrix}\\
~\\~\\
\Rightarrow
\begin{pmatrix}
    a & b \\
    -b& a
\end{pmatrix}^n = \\
~\\
\begin{pmatrix}
    \sqrt{a^2+b^2} & \\
     & \sqrt{a^2+b^2}
\end{pmatrix}^n
\begin{pmatrix}
    \cos{n\arccos{\frac{a}{\sqrt{a^2+b^2}}}} & \sin{n\arccos{\frac{b}{\sqrt{a^2+b^2}}}} \\
    -\sin{n\arccos{\frac{b}{\sqrt{a^2+b^2}}}} & \cos{n\arccos{\frac{a}{\sqrt{a^2+b^2}}}}
\end{pmatrix}
$$
#### 指数形式（矩阵秩为1）
$$
当ad=bc时，
\begin{pmatrix}
    a & b \\
    c & d
\end{pmatrix}^n =
\begin{pmatrix}
    a(a+d)^{n-1} & b(a+d)^{n-1} \\
    c(a+d)^{n-1} & d(a+d)^{n-1}
\end{pmatrix}
$$
$$
若A = \begin{pmatrix}
    a_1b_1 & a_1b_2 & \cdots & a_1b_n \\
    a_2b_1 & a_2b_2 & \cdots & a_2b_n \\
    \vdots & \vdots & \ddots & \vdots \\
    a_nb_1 & a_nb_2 & \cdots & a_nb_n
\end{pmatrix},
设 \alpha = \begin{pmatrix}a_1\\ a_2\\ \vdots\\ a_n \end{pmatrix}
\beta = \begin{pmatrix}b_1, b_2, \cdots, b_n \end{pmatrix} \\ ~\\
则A^i = (\alpha\beta)^i = \alpha(\beta\alpha)^{i-1}\beta
= (\sum_{j=1}^n a_jb_j)^{i-1}A = (tr(A))^{i-1}A
$$
#### 阶梯形式
$$
\forall i,j(i>j-k):a_{ij}=0 \\ \equiv A^{(k)}\\
\Rightarrow A^{(k)}\times B^{(m)} = C^{(k+m)}
$$
$
Proof:
由A^{(k)}, B^{(m)}得，\\
当i>s-k时，a_{is}=0;\\
当s>j-m时，b_{sj}=0;\\
\therefore 当i>j-k-m时，c_{ij}=\sum_{s=1}^n a_{is}b_{sj} = 0\\
\Rightarrow A^{(k)}\times B^{(m)} = C^{(k+m)}
$
#### 例题
$$求
\begin{pmatrix}
    1 & 2 & 3 \\
    0 & 1 & 2 \\
    0 & 0 & 1
\end{pmatrix}^n
$$
$=
\left[
    E+
    \begin{pmatrix}
    0 & 2 & 3 \\
    0 & 0 & 2 \\
    0 & 0 & 0
    \end{pmatrix}
\right]^n ~\\$
$=E^n + C_n^1E^{n-1}
\begin{pmatrix}
    0 & 2 & 3 \\
    0 & 0 & 2 \\
    0 & 0 & 0
\end{pmatrix} + C_n^2E^{n-2}
\begin{pmatrix}
    0 & 0 & 4 \\
    0 & 0 & 0 \\
    0 & 0 & 0
\end{pmatrix}~\\$
$=\begin{pmatrix}
    1 & 2n & 2n^2+n \\
    0 & 1 & 2n \\
    0 & 0 & 1
\end{pmatrix}$

---
$$设
P=\begin{pmatrix}2&3\\1&2\end{pmatrix}, 
A=\begin{pmatrix}2&0\\0&-1\end{pmatrix}, 
Q=\begin{pmatrix}2&-3\\-1&2\end{pmatrix}\\
~\\求(PAQ)^n
$$

$PAQ=\begin{pmatrix}11&-18\\6&-10\end{pmatrix}
= 2E + \begin{pmatrix}9&-18\\6&-12\end{pmatrix} ~\\$

$\therefore
(PAQ)^n=\sum_{i=0}^nC_n^i
\begin{pmatrix}2&0\\0&2\end{pmatrix}^{n-i}
\begin{pmatrix}9&-18\\6&-12\end{pmatrix}^i ~\\$

$=\begin{pmatrix}2^{n}&0\\0&2^{n}\end{pmatrix}+
\sum_{i=1}^nC_n^i
\begin{pmatrix}2^{n-i}&0\\0&2^{n-i}\end{pmatrix}
\begin{pmatrix}
    -3(-3)^i & 6(-3)^i \\
    -2(-3)^i & 4(-3)^i
\end{pmatrix} ~\\$

$=\begin{pmatrix}2^{n}&0\\0&2^{n}\end{pmatrix}+
\begin{pmatrix}
    -3\cdot2^n\sum_{i=1}^nC_n^i(-\frac{3}{2})^i &
     6\cdot2^n\sum_{i=1}^nC_n^i(-\frac{3}{2})^i \\
    -2\cdot2^n\sum_{i=1}^nC_n^i(-\frac{3}{2})^i &
     4\cdot2^n\sum_{i=1}^nC_n^i(-\frac{3}{2})^i
\end{pmatrix} ~\\$

$=\begin{pmatrix}2^{n}&0\\0&2^{n}\end{pmatrix}+
\begin{pmatrix}
    -3\cdot2^n[(-\frac{1}{2})^n-1] &
     6\cdot2^n[(-\frac{1}{2})^n-1] \\
    -2\cdot2^n[(-\frac{1}{2})^n-1] &
     4\cdot2^n[(-\frac{1}{2})^n-1]
\end{pmatrix} ~\\$

$=\begin{pmatrix}
    2^{n+2}-3(-1)^n & -3\cdot2^{n+1}+6(-1)^n \\
    2^{n+1}-2(-1)^n & -3\cdot2^n+4(-1)^n
\end{pmatrix}$

### 矩阵求逆
#### 零化多项式
$$
令f(x) = \sum_{k=0}^n a_kx^k且f(A)=O, 
g(x) = \sum_{k=1}^n a_kx^{k-1} \\~\\
(1) 若a_0\neq0，则A可逆，且A^{-1} = -\frac{1}{a_0}g(A) \\
(2) 若a_0=0，且g(A)\neq O，则A不可逆
$$
#### 三角块方阵
$$
\begin{pmatrix}A & C \\ O & B\end{pmatrix}^{-1} = 
\begin{pmatrix}A^{-1} & -A^{-1}CB^{-1} \\ O & B^{-1}\end{pmatrix}
$$
#### 加边法
$$
若A=\begin{pmatrix}
    A_1 & B \\
    C & a_{nn}
\end{pmatrix}，
设A^{-1}=\begin{pmatrix}
    D & X \\
    Y & b_{nn}
\end{pmatrix}，k=\frac{1}{a_{nn}-CA_1^{-1}B}\\~\\
则b_{nn}=k，D=A_1^{-1}(E+kBCA_1^{-1})，\\~\\
X=-kA_1^{-1}B，Y=-kCA_1^{-1}
$$
#### 伴随矩阵法
$$
A^{-1} = \frac{A^*}{|A|}，其中\\~\\
A^*=\begin{pmatrix}
    A_{11} & A_{21} & \cdots & A_{n1} \\
    A_{12} & A_{22} & \cdots & A_{n2} \\
    \vdots & \vdots & \ddots & \vdots \\
    A_{1n} & A_{2n} & \cdots & A_{nn} \\
\end{pmatrix}
$$
#### 例题
$$
设X=(x_1,x_2,\cdots,x_n)，Y=(y_1,y_2,\cdots,y_n)，且XY^T=2\\
若A = E + X^TY，请证明A可逆，并求其逆矩阵
$$
$A^2 = E+2X^TY+(X^TY)^2 = E+4X^TY，\\
\displaystyle{故4A-A^2 = 3E，即A\times \frac{4E-A}{3} = E，故逆矩阵为\frac{4E-A}{3}} $

### 其他
$AB与BA的迹相同，故AB-BA\neq E$

$~\\ \begin{pmatrix}a & 0 \\ 0 & a^{-1} \end{pmatrix} 可表示为倍加初等矩阵的乘积 \\
Proof:
\begin{pmatrix}a & 1 \\ 0 & a^{-1} \end{pmatrix} \rightarrow
\begin{pmatrix}0 & 1 \\ -1 & a^{-1} \end{pmatrix} \rightarrow
\begin{pmatrix}0 & 1 \\ -1 & 0 \end{pmatrix} \rightarrow
\begin{pmatrix}1 & 0 \\ 0 & 1 \end{pmatrix}$


