<!-- TOC -->

- [平面方程](#平面方程)
- [直线方程](#直线方程)
- [线性图形的位置关系](#线性图形的位置关系)
  - [平面与平面的关系](#平面与平面的关系)
  - [平面与直线的关系（三个平面的关系）](#平面与直线的关系三个平面的关系)
  - [直线与直线的关系（四个平面的关系）](#直线与直线的关系四个平面的关系)
  - [多个平面的关系](#多个平面的关系)
- [线性图形的度量关系](#线性图形的度量关系)
  - [点到平面的距离](#点到平面的距离)

<!-- /TOC -->






### 平面方程
设向量 $\overrightarrow{P_0P} = (x-x_0, y-y_0, z-z_0) $，平面的法向量 $\bm{n} = (a, b, c) $，
则点 $P$ 在平面 $\pi$ 上当且仅当 $\overrightarrow{P_0P} \cdot \bm{n} = 0 $

- 平面的一般方程：$ax+by+cz+d=0$
- 平面的截距式方程：
  - 当 $a,b,c$ 有一个为0时，平面平行于对应坐标轴
  - 当 $a,b,c$ 有两个为0时，平面平行于对应坐标平面
  - 当 $d = 0$ 时，平面经过原点
  - 当 $abcd\neq 0$ 时，$\displaystyle{\frac{x}{a_1}+\frac{y}{b_1}+\frac{z}{c_1}=1}$


### 直线方程
- 直线的参数方程：
  $\left\{ \begin{aligned}
    &x = x_0 + lt \\ 
    &y = y_0 + mt \\ 
    &z = z_0 + nt \\ 
    \end{aligned} \right. $
- 直线的标准方程：$\bm{S}=(l, m, n)$ 称为直线的方向向量
  - 当 $l,m,n$ 有两个为0时，直线垂直于对应坐标平面
  - 当 $l,m,n$ 有一个为0时，直线垂直于对应坐标轴
  - 当 $lmn\neq 0$ 时，$\displaystyle{\frac{x-x_0}{l}=\frac{y-y_0}{m}=\frac{z-z_0}{n}}$
- 直线的一般方程：$\bm{S} = \bm{n_1\times n_2} $
  $\left\{ \begin{aligned}
    &a_1x + b_1y + c_1z + d_1 = 0 \\ 
    &a_2x + b_2y + c_2z + d_2 = 0 \\ 
    \end{aligned} \right. $

### 线性图形的位置关系
#### 平面与平面的关系
$\left\{ \begin{aligned}
&a_{11}x_1 + a_{12}x_2 + a_{13}x_3 = b_1 \\ 
&a_{21}x_1 + a_{22}x_2 + a_{23}x_3 = b_2 \\ 
\end{aligned} \right. $

- 当 $\text{r}(A) = \text{r}(A,b) = 2$ 时，方程组有无穷解，解空间为1维子空间，故两平面相交为一直线
- 当 $\text{r}(A) = \text{r}(A,b) = 1$ 时，方程组有无穷解，解空间为2维子空间，故两平面重合
- 当 $\text{r}(A) = 1, \text{r}(A,b) = 2$ 时，方程组无解，故两平面平行

#### 平面与直线的关系（三个平面的关系）
$\left\{ \begin{aligned}
&a_{11}x_1 + a_{12}x_2 + a_{13}x_3 = b_1 \\ 
&a_{21}x_1 + a_{22}x_2 + a_{23}x_3 = b_2 \\ 
&a_{31}x_1 + a_{32}x_2 + a_{33}x_3 = b_3 \\ 
\end{aligned} \right. $

- 当 $\text{r}(A) = \text{r}(A,b) = 3$ 时，方程组有唯一解，故直线与平面相交于一点，或三个平面交于一点
- 当 $\text{r}(A) = \text{r}(A,b) = 2$ 时，方程组有无穷解，解空间为1维子空间，故直线位于平面上，或三个平面共线
- 当 $\text{r}(A) = \text{r}(A,b) = 1$ 时，方程组有无穷解，解空间为2维子空间，故三个平面重合
- 当 $\text{r}(A) = 2, \text{r}(A,b) = 3$ 时，方程组无解，故直线平行于平面，或三个平面平行且至少有两个不重合

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
- 当 $\text{r}(A) = 2, \text{r}(A,b) = 3$ 时，方程组无解，此时四个平面的法向量共面，故两直线平行而不相交
- 当 $\text{r}(A) = 3, \text{r}(A,b) = 4$ 时，方程组无解，两直线不平行也不相交

#### 多个平面的关系
- 当方程组有解时
  - $m$ 个平面交于一点
  - $m$ 个平面交于一条直线
  - $m$ 个平面重合
- 当方程组无解时
  - 有两个平面平行而不重合
  - 平面两两的交线中，有两条交线不相交



### 线性图形的度量关系
#### 点到平面的距离





