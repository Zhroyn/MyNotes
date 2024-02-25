
- [线性图形](#线性图形)
  - [平面方程](#平面方程)
  - [直线方程](#直线方程)
  - [线性图形的位置关系](#线性图形的位置关系)
    - [平面与平面的关系](#平面与平面的关系)
    - [平面与直线的关系（三个平面的关系）](#平面与直线的关系三个平面的关系)
    - [直线与直线的关系（四个平面的关系）](#直线与直线的关系四个平面的关系)
    - [多个平面的关系](#多个平面的关系)
  - [线性图形的度量关系](#线性图形的度量关系)
    - [点到平面的距离](#点到平面的距离)
    - [点到直线的距离](#点到直线的距离)
    - [平面与平面的距离和夹角](#平面与平面的距离和夹角)
    - [直线与直线的距离和夹角](#直线与直线的距离和夹角)
    - [直线与平面的距离和夹角](#直线与平面的距离和夹角)
- [二次曲线](#二次曲线)
  - [二次曲线的一般方程](#二次曲线的一般方程)
  - [二次曲线的不变量](#二次曲线的不变量)
  - [二次曲线的最简方程](#二次曲线的最简方程)
    - [椭圆型和双曲型曲线（有心二次曲线）](#椭圆型和双曲型曲线有心二次曲线)
    - [抛物型曲线（无心二次曲线）](#抛物型曲线无心二次曲线)





## 线性图形
### 平面方程
设向量 $\overrightarrow{P_0P} = (x-x_0, y-y_0, z-z_0) $，平面的法向量 $\bm{n} = (a, b, c) $，
则点 $P$ 在平面 $\pi$ 上当且仅当 $\overrightarrow{P_0P} \cdot \bm{n} = 0 $

- 平面的一般方程：$ax+by+cz+d=0$
- 平面的截距式方程：
  - 当 $a,b,c$ 有一个为0时，平面平行于对应坐标轴
  - 当 $a,b,c$ 有两个为0时，平面平行于对应坐标平面
  - 当 $d = 0$ 时，平面经过原点
  - 当 $abcd\neq 0$ 时，$\displaystyle{\frac{x}{a_1}+\frac{y}{b_1}+\frac{z}{c_1}=1}$

<br>

### 直线方程
- 直线的参数方程：
  $\left\{ \begin{aligned}
    &x = x_0 + lt \\ 
    &y = y_0 + mt \\ 
    &z = z_0 + nt \\ 
    \end{aligned} \right. $
- 直线的标准方程：$\bm{S}=(l, m, n)$ 称为直线的方向向量
  - 当 $l,m,n$ 有一个为0时，直线垂直于对应坐标轴
  - 当 $l,m,n$ 有两个为0时，直线垂直于对应坐标平面
  - 当 $lmn\neq 0$ 时，$\displaystyle{\frac{x-x_0}{l}=\frac{y-y_0}{m}=\frac{z-z_0}{n}}$
- 直线的一般方程：$\bm{S} = \bm{n}_1\times \bm{n}_2 $
  $\left\{ \begin{aligned}
    &a_1x + b_1y + c_1z + d_1 = 0 \\ 
    &a_2x + b_2y + c_2z + d_2 = 0 \\ 
    \end{aligned} \right. $







<br>

### 线性图形的位置关系
#### 平面与平面的关系
$\left\{ \begin{aligned}
&a_{11}x_1 + a_{12}x_2 + a_{13}x_3 = b_1 \\ 
&a_{21}x_1 + a_{22}x_2 + a_{23}x_3 = b_2 \\ 
\end{aligned} \right. $

- 当 $\text{r}(A) = \text{r}(A,b) = 2$ 时，方程组有无穷解，解空间为1维子空间，故两平面相交为一直线
- 当 $\text{r}(A) = \text{r}(A,b) = 1$ 时，方程组有无穷解，解空间为2维子空间，故两平面重合
- 当 $\text{r}(A) = 1, \text{r}(A,b) = 2$ 时，方程组无解，故两平面平行

<br>

#### 平面与直线的关系（三个平面的关系）
$\left\{ \begin{aligned}
&a_{11}x_1 + a_{12}x_2 + a_{13}x_3 = b_1 \\ 
&a_{21}x_1 + a_{22}x_2 + a_{23}x_3 = b_2 \\ 
&a_{31}x_1 + a_{32}x_2 + a_{33}x_3 = b_3 \\ 
\end{aligned} \right. $

- 当 $\text{r}(A) = \text{r}(A,b) = 3$ 时，方程组有唯一解，故直线与平面相交于一点，或三个平面交于一点
- 当 $\text{r}(A) = \text{r}(A,b) = 2$ 时，方程组有无穷解，解空间为1维子空间，故直线位于平面上，或三个平面共线
- 当 $\text{r}(A) = \text{r}(A,b) = 1$ 时，方程组有无穷解，解空间为2维子空间，故三个平面重合
- 当 $\text{r}(A) = 1, \text{r}(A,b) = 2$ 时，方程组无解，三个平面平行且至少有两个不重合
- 当 $\text{r}(A) = 2, \text{r}(A,b) = 3$ 时，方程组无解，直线平行于平面

<br>

#### 直线与直线的关系（四个平面的关系）
$\left\{ \begin{aligned}
&a_{11}x_1 + a_{12}x_2 + a_{13}x_3 = b_1 \\ 
&a_{21}x_1 + a_{22}x_2 + a_{23}x_3 = b_2 \\ 
&a_{31}x_1 + a_{32}x_2 + a_{33}x_3 = b_3 \\ 
&a_{41}x_1 + a_{42}x_2 + a_{43}x_3 = b_4 \\ 
\end{aligned} \right. $

- 当 $\text{r}(A) = \text{r}(A,b) = 3$ 时，方程组有唯一解，故直线与直线相交于一点，或四个平面交于一点
- 当 $\text{r}(A) = \text{r}(A,b) = 2$ 时，方程组有无穷解，解空间为1维子空间，故直线于直线重合，或四个平面共线
- 当 $\text{r}(A) = \text{r}(A,b) = 1$ 时，方程组有无穷解，解空间为2维子空间，故四个平面重合
- 当 $\text{r}(A) = 1, \text{r}(A,b) = 2$ 时，方程组无解，此时四个平面重合
- 当 $\text{r}(A) = 2, \text{r}(A,b) = 3$ 时，方程组无解，此时四个平面的法向量共面，故两直线平行而不相交
- 当 $\text{r}(A) = 3, \text{r}(A,b) = 4$ 时，方程组无解，两直线不平行也不相交

<br>

#### 多个平面的关系
- 当方程组有解时
  - $m$ 个平面交于一点
  - $m$ 个平面交于一条直线
  - $m$ 个平面重合
- 当方程组无解时
  - 有两个平面平行而不重合
  - 平面两两的交线中，有两条交线不相交






<br>

### 线性图形的度量关系
#### 点到平面的距离
$$\displaystyle \bm{n}^0 = \frac{1}{\sqrt{a^2 + b^2 + c^2}}(a, b, c)
\\~\\
\begin{aligned}
  d &= \left| |\overrightarrow{P_0P}| \cdot \cos\theta \right| = |\overrightarrow{P_0P}\cdot \bm{n}^0 | \\
  &= \frac{|a(x_1-x_0) + b(y_1-y_0) + c(z_1-z_0)|}{\sqrt{a^2 + b^2 + c^2}} \\
  &= \frac{|ax_1 + by_1 + cz_1 + d|}{\sqrt{a^2 + b^2 + c^2}} \\
\end{aligned} $$

<br>

#### 点到直线的距离
$$\begin{aligned}
  d &= |\overrightarrow{P_0P}|\cdot \sin\theta \\
  &= |\overrightarrow{P_0P}|\cdot \frac{|\bm{S}\times \overrightarrow{P_0P}|}{|\bm{S}|\cdot|\overrightarrow{P_0P}|} \\
  &= \frac{|\bm{S}\times \overrightarrow{P_0P}|}{|\bm{S}|}
\end{aligned} $$

<br>

#### 平面与平面的距离和夹角
$$
\begin{aligned}
  d &= |\overrightarrow{P_0P_1}\cdot \bm{n}^0| \\
  &= \frac{|d_1 - d_2|}{\sqrt{a^2 + b^2 + c^2}} \\
\end{aligned}
\\~\\
\begin{aligned}
  \cos\theta &= |\bm{n}_1^0 \cdot \bm{n}_2^0| \\
  &= \frac{|a_1a_2 + b_1b_2 + c_1c_2|}{\sqrt{a_1^2 + b_1^2 + c_1^2}\cdot\sqrt{a_2^2 + b_2^2 + c_2^2}}, \theta \le \frac{\pi}{2}
\end{aligned}
$$

<br>

#### 直线与直线的距离和夹角
当两条直线相交时，$d = 0$
当两条直线平行时，$\displaystyle d = \frac{|\bm{S}_1\times \overrightarrow{P_1P_2}|}{|\bm{S}_1|}$
当两条直线既不相交又不平行时，
$$
\bm{S} = \bm{S}_1 \times \bm{S}_2 \\
d = \frac{|\overrightarrow{P_1P_2}\cdot \bm{S}|}{|\bm{S}|} = |\overrightarrow{P_1P_2}\cdot \bm{S}_0|
$$

$$\theta = \arccos(\bm{S}_1^0 \cdot \bm{S}_2^0), 0 \le \theta \le \pi $$

<br>

#### 直线与平面的距离和夹角
当直线与平面相交时，$d = 0$
当直线与平面平行时，$d = |\overrightarrow{P_0P_1}\cdot \bm{n}^0|$

$$\theta = \arcsin\frac{|\bm{n} \cdot \bm{s}|}{|\bm{n}|\cdot|\bm{s}|}, 0 \le \theta \le \frac{\pi}{2} $$








<br>

## 二次曲线
### 二次曲线的一般方程
一般方程：$a_{11}x_1^2 + 2a_{12}x_1x_2 + a_{22}x_2^2 + 2a_1x_1 + 2a_2x_2 + a_0 = 0$
其中，二次项部分为
$$
\begin{aligned}
  f(x_1, x_2) &= a_{11}x_1^2 + 2a_{12}x_1x_2 + a_{22}x_2^2 \\
  &= \begin{pmatrix} x_{1} & x_{2} \end{pmatrix}
  \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}
  \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \\
  &= \bm{X^T}A\bm{X}
\end{aligned}
$$ 代入
$$
\bm{X} = Q\bm{Y} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
\begin{pmatrix} y_{1} \\ y_{2} \end{pmatrix} \\
$$ 即得
$$
\begin{aligned}
  \phi(x_1, x_2) 
  &= (Q\bm{Y})^T A (Q\bm{Y}) \\
  &= \bm{Y}^T (Q^TAQ)\bm{Y} \\
  &= \begin{pmatrix} y_{1} & y_{2} \end{pmatrix}
  \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}
  \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}
  \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
  \begin{pmatrix} y_{1} \\ y_{2} \end{pmatrix} \\
  &= \begin{pmatrix} y_{1} & y_{2} \end{pmatrix}
  \begin{pmatrix} b_{11} & 0 \\ 0 & b_{22} \end{pmatrix}
  \begin{pmatrix} y_{1} \\ y_{2} \end{pmatrix} \\
  &= b_{11}y_1^2 + b_{22}y_2^2 \\
\end{aligned}
$$

于是可得
$$
\left\{
\begin{aligned}
  &b_{11} = a_{11}\cos^2\theta + a_{12}\sin 2\theta + a_{22}\sin^2\theta \\
  &b_{12} = b_{21} = \frac{1}{2}(a_{22} - a_{11}) + a_{12}\cos 2\theta \\
  &b_{11} = a_{11}\cos^2\theta - a_{12}\sin 2\theta + a_{22}\sin^2\theta \\
\end{aligned}
\right.
$$

进而得
$$
\cot 2\theta = \frac{a_{11} - a_{22}}{2a_{12}},
\quad \theta = \frac{1}{2}\text{arccot} \frac{a_{11} - a_{22}}{2a_{12}}, 
\\~\\
b_{11} = a_{11} + a_{12}\tan\theta, \quad b_{22} = a_{22} - a_{12}\tan\theta 
$$

<br>

### 二次曲线的不变量
在直角坐标变换下，以下三个不变量不变：
$$
I_1 = a_{11} + a_{22}, \\~\\
I_2 = \begin{vmatrix} a_{11} & a_{12} \\ a_{12} & a_{22} \end{vmatrix}, \\~\\
I_3 = \begin{vmatrix}
  a_{11} & a_{12} & a_{1} \\
  a_{12} & a_{22} & a_{2} \\
  a_{1} & a_{2} & a_{0} \\
\end{vmatrix}
$$

<br>

### 二次曲线的最简方程
#### 椭圆型和双曲型曲线（有心二次曲线）
最简方程：$b_{11}y_1^2 + b_{22}y_2^2 + b_0 = 0 $
$$
I_1 = b_{11} + b_{22}, \\~\\
I_2 = \begin{vmatrix} b_{11} & 0 \\ 0 & b_{22} \end{vmatrix} = b_{11}b_{22}, \\~\\
I_3 = \begin{vmatrix}
  b_{11} & 0 & 0 \\
  0 & b_{22} & 0 \\
  0 & 0 & b_{0} \\
\end{vmatrix} = b_{11}b_{22}b_{0} = I_2b_0
$$

于是 $b_{11}, b_{22}$ 是 $\lambda^2 - I_1\lambda + I_2 = 0$ 的两个实根，$\displaystyle b_0 = \frac{I_3}{I_2}$，

称 $\lambda^2 - I_1\lambda + I_2 = 0$ 为二次曲线的特征方程，
称 $|\lambda E - A| = \begin{vmatrix} \lambda - a_{11} & -a_{12} \\ -a_{12} & \lambda - a_{22} \end{vmatrix} $ 为二次曲线的特征多项式，
因为
$$
\begin{aligned}
  I_1^2 - 4I_2 &= (a_{11} + a_{22})^2 - 4(a_{11}a_{22} - a_{12}^2) \\
  &= (a_{11} - a_{22})^2 + 4a_{12}^2 \ge 0
\end{aligned}
$$ 所以该方程必有两个不等或相等的实根，称为特征根。

故方程可化为 $\displaystyle \lambda_1y_1^2 + \lambda_2y_2^2 + \frac{I_3}{I_2} = 0. $


- 当 $I_2 = \lambda_1\lambda_2 \gt 0$ 时，曲线为椭圆型
  - 若 $I_3$ 与 $I_1$ 或 $I_2$ 异号，则曲线为椭圆
  - 若 $I_3$ 与 $I_1$ 或 $I_2$ 同号，则曲线为虚椭圆
  - 若 $I_3 = 0$，则曲线为一个点
- 当 $I_2 = \lambda_1\lambda_2 \lt 0$ 时，曲线为双曲型
  - 若 $I_3 \neq 0$，则曲线为双曲线
  - 若 $I_3 = 0$，则曲线为一对相交直线

<br>

#### 抛物型曲线（无心二次曲线）
此时，最简方程为 $b_{22}y_2^2 + 2b_1y_1 = 0$
$$
I_1 = b_{22}, \\~\\
I_2 = \begin{vmatrix} 0 & 0 \\ 0 & b_{22} \end{vmatrix} = 0, \\~\\
I_3 = \begin{vmatrix}
  0 & 0 & b_1 \\
  0 & b_{22} & 0 \\
  b_1 & 0 & 0 \\
\end{vmatrix} = -b_{22}b_1^2 = -I_1b_1^2
$$
于是最简方程可化为 $\displaystyle I_1y_2^2 \pm 2\sqrt{\frac{-I_3}{I_1}}y_1 = 0$

- 若 $I_2 = 0, I_3 \neq 0 $，则 $\displaystyle \frac{a_{11}}{a_{12}} = \frac{a_{12}}{a_{22}} \neq \frac{a_1}{a_2}$，一般二次方程可化为 $\displaystyle I_1y_2^2 \pm 2\sqrt{\frac{-I_3}{I_1}}y_1 = 0$，曲线为抛物线
- 若 $I_2 = 0, I_3 = 0 $，则 $\displaystyle \frac{a_{11}}{a_{12}} = \frac{a_{12}}{a_{22}} = \frac{a_1}{a_2}$，一般二次方程可化为 $\displaystyle I_1y_2^2 + \frac{K_1}{I_1} = 0$
  - 若 $K_1 < 0$，则为一对平行直线
  - 若 $K_1 = 0$，则为一对重合直线
  - 若 $K_1 > 0$，则为一对虚平行线

其中 $K_1 = \begin{vmatrix} a_{11} & a_{1} \\ a_{1} & a_{0} \end{vmatrix} + \begin{vmatrix} a_{22} & a_{2} \\ a_{2} & a_{0} \end{vmatrix} $ 称为二次曲线的半不变量，
它在旋转变换中不变，当 $I_2 = I_3 = 0$ 时，在平移变换中也不变。



