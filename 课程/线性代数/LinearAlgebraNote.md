<!-- TOC -->

- [集合 关系 运算 结构](#集合-关系-运算-结构)
  - [集合](#集合)
  - [映射](#映射)
  - [向量运算](#向量运算)
  - [高斯消元法](#高斯消元法)
  - [代数结构](#代数结构)
- [线性空间](#线性空间)
  - [定义与定理](#定义与定理)
  - [交、和与直和](#交和与直和)
- [线性映射](#线性映射)
  - [像与核](#像与核)
  - [线性映射的秩](#线性映射的秩)
  - [线性空间的同构](#线性空间的同构)
- [行列式](#行列式)
  - [行列式的性质](#行列式的性质)
  - [常见计算](#常见计算)
      - [n阶三对角行列式](#n阶三对角行列式)
      - [范德蒙(Vandermonde)行列式](#范德蒙vandermonde行列式)

<!-- /TOC -->





### 集合 关系 运算 结构
#### 集合
- 幂集：非空集合A的所有子集组成的集合称为A的幂集，记作$P(A)或2^A$
- 余集：$A\setminus B, A - B, \bar{B}(if B \subset A)$
- 差集：$A-B$
- 等价关系：一个二元关系R称为等价关系，如果R是自反的、对称的和传递的
- 等价类：$\bar{a}=\left\{x|xRa,x\in X \right\}$称为a关于R的等价类
- 商集：X关于R的所有等价类组成的集合称为X关于R的商集，记作$X/R$
$
~\\
分配律：A\cap(B\cup C) = (A\cap B)\cup (A\cap B)\\
\qquad \qquad A\cup(B\cap C) = (A\cup B)\cap (A\cup B)\\
~\\
DeMorgan律：\overline{A\cup B} = \bar{A}\cap \bar{B}\\
\qquad \qquad \qquad \quad \overline{A\cup B} = \bar{A}\cap \bar{B}\\
~\\
A\setminus B = A\cap \bar{B}\\
(A\cap B)\setminus C = A\cap(B\setminus C)\\
(A\cup B)\setminus C = (A\setminus C)\cup(B\setminus C)
$
#### 映射
$
定理1.4：集X到Y的映射\sigma 可逆的充要条件是\sigma是双射\\
Proof（必要性）：\\
对\forall y_0 \in Y，有y_0=I_Y(y_0)=(\sigma\sigma^{-1})(y_0)=\sigma(\sigma^{-1}(y_0)),由于\sigma^{-1}(y_0)\in X，故\sigma是满射\\
若\sigma(x_1)=\sigma(x_2)，则必有x_1=I_X(x_1)=\sigma^{-1}(\sigma(x_1))=\sigma^{-1}(\sigma(x_2))=I_X(x_2)=x_2，故\sigma是单射
$
#### 向量运算
- 加法
- 数乘，单位向量记作$a^0$
- 内积（点积，数量积）：$a\cdot b=|a||b|cos\theta，0\le\theta\le\pi$
- 外积（叉积，向量积）：$a \times b = |a||b|sin\left<a,b \right>，方向为右手伸开由a转到b（可联想空间直角坐标系，e_1e_2=e_3, e_2e_3=e_1, e_3e_1=e_2）$
- 混合积：$a\cdot(b\times c)=b\cdot(c\times a)=c\cdot(a\times b)$
- 抽心公式：$a \times (b \times c) = (a \cdot c) \cdot b - (a \cdot b) \cdot c$
$~\\
自行证明，在空间直角坐标系中：\\
a\times b=\begin{vmatrix}
    \bm{e_1} & \bm{e_2} & \bm{e_3} \\
    a_1 & a_2 & a_3 \\
    b_1 & b_2 & b_3 \\
\end{vmatrix}，
a\cdot(b\times c)=\begin{vmatrix}
    a_1 & a_2 & a_3 \\
    b_1 & b_2 & b_3 \\
    c_1 & c_2 & c_3 \\
\end{vmatrix}，
$

#### 高斯消元法
- 常数项全为0的方程组称为齐次线性方程组
- 齐次线性方程组总是有解的，m个方程，n个未知量，当$r=n$时有唯一解，当$r<n$时有无穷多个解（r为非零行个数，n为未知量个数）


#### 代数结构
- $\left<G:\circ\right>$称为群，如果：满足结合律；存在单位元；存在逆元
  - 半群：满足结合律
  - 含幺半群：满足结合律；存在单位元
  - 交换群：满足结合律；存在单位元；存在逆元；满足交换律
  - $ R(X)_3=\{a_0+a_1x+a_2x^2\}, R(X)$为所有实系数多项式组成的集合
- $\left<R:+,\circ\right>$称为环，如果：
  - $\left<R:+\right>$是交换群（加法群）
  - $\left<R:\circ\right>$是半群，即不一定有单位元和逆元
  - $“+”$对$“\circ”$满足左、右分配律
  - 若乘法满足交换律，则称其为交换环
  - 若乘法存在单位元，则称其为含幺环
- $\left<F:+,\circ\right>$称为域，如果：
  - 是至少含有两个元的交换环
  - $F\setminus \left\{0\right\}$关于乘法运算是交换群





### 线性空间
#### 定义与定理

如果 $\left<V:+\right>$ 是一个交换群（加法群），
且 $\forall \alpha,\beta\in V,\forall \lambda,\mu\in F$，以及域F的乘法单位元1，有：
$
1\alpha=\alpha \\
\lambda(\mu\alpha)=(\lambda\mu)\alpha \\
(\lambda+\mu)\alpha=\lambda\alpha+\mu\alpha \\
\lambda(\alpha+\beta)=\lambda\alpha+\lambda\beta
$
则称V为域F上的线性空间，记作 $V(F)$

V本身称为V的平凡子空间，V的其他子空间称为非平凡子空间 
定理2.1：$V(F)$的\bm{非空}子集W为V的子空间
\iff W对于$V(F)$的线性运算封闭
定理2.2：$V(F)$的非空子集S的线性扩张$L(S)$是V中包含S的最小子空间

定理2.3：$V(F)$中的向量组$\alpha_1,\alpha_2,\dots,\alpha_m(m\ge 2)$线性相关
$\iff \alpha_1,\alpha_2,\dots,\alpha_m$中存在向量可由其余向量在域F上线性表示
定理2.3等价命题：$\alpha_1,\alpha_2,\dots,\alpha_m(m\ge 2)$线性无关
$\iff$ 任何一个向量都不能由其余向量线性表示

定理2.4：若 $\left\{\alpha_1,\alpha_2,\dots,\alpha_n\right\}$ 线性无关，$\left\{\beta,\alpha_1,\alpha_2,\dots,\alpha_n\right\}$线性相关，
则$\beta$可由$\alpha_1,\alpha_2,\dots,\alpha_n$线性表示，且表示法唯一
推论：若$\left\{\alpha_1,\alpha_2,\dots,\alpha_n\right\}$是$R^n$中线性无关的n个向量，
则$R^n$中任一向量可由$\left\{\alpha_1,\alpha_2,\dots,\alpha_n\right\}$线性表示
~
定理2.5：设$\left\{\beta_1,\beta_2,\dots,\beta_s\right\}$中的每个向量可由$\left\{\alpha_1,\alpha_2,\dots,\alpha_r\right\}$线性表示，
若s>r，则$\left\{\beta_1,\beta_2,\dots,\beta_s\right\}$线性相关
定理2.5等价命题：若$\left\{\beta_1,\beta_2,\dots,\beta_s\right\}$线性无关，则$s\le r$
若$S$中每个向量可由$T$线性表示，则$r(S)\le r(T)$

#### 交、和与直和

$dimW_1+dimW_2=dim(W_1+W_2)+dim(W_1\cap W_2)$

定理2.7：对$V$的子空间$W_1,W_2$，下列命题等价：
(1)$W_1+W_2$是直和，即$W_1\cap W_2=\left\{0\right\}$
(2)$W_1+W_2$中的每个向量$\alpha$的分解式$\alpha=\alpha_1+\alpha_2$唯一
(3)零向量$\bm{0}$的分解式$0=\alpha_1+\alpha_2$，仅当$\alpha_1=\alpha_2=0$时成立
(4)$dim(W_1+W_2)=dimW_1+dimW_2$

若$V=W_1\oplus W_2$，则称$W_1$为$W_2$的补空间，$W_2$为$W_1$的补空间
求线性空间的基：如给方程，则求解空间；如给向量组，则高斯消元
求子空间的和的基：求子空间的基，然后高斯消元
求子空间的交的基：如给方程，则交为方程组的解空间，否则先求和的基
求补空间的基（扩充基）：用观察法或行列式找出不能线性表示的向量

若$W_1\perp W_2$且$W_1+W_2=V$，则称$W_2$是$W_1$的正交补，记作$W_1^{\perp}$
求正交补的基（扩充规范正交基）：与已有正交基联立，求解空间的基






### 线性映射
#### 像与核

Im\sigma 是V_2的一个子空间，Ker\sigma 是V_1的一个子空间
线性空间在线性映射下的的像与完全原像仍为线性空间
定理3.1：线性映射\sigma是单射\iff \sigma^{-1}(0_2)=\left\{0_1\right\} 
可逆线性映射的逆映射是线性映射

#### 线性映射的秩

r(\sigma)=dim(Im\sigma)=r(\sigma(B))
定理3.2：dim(Im\sigma)+dim(Ker\sigma)=dimV_1=n
定理3.3：如果V_1和V_2都是n维线性空间，则下列命题等价：
(1)r(\sigma)=n，即\sigma满秩；(2)\sigma是单射；
(3)\sigma是满射；(4)\sigma是可逆线性映射 
~
定理3.4：设V_1,V_2,V_3分别为m,n,s维线性空间，
则r(\sigma)+r(\tau)-n\le r(\tau\sigma)\le min(r(\sigma),r(\tau)) 
Proof：令V_2=\sigma(V_1)\oplus W，
则r(\tau(V_2))=r(\tau(\sigma(V_1)+W))=r(\tau\sigma(V_1)+\tau(W))\le r(\tau\sigma)+r(\tau(W))， 
且r(\tau(W))\le r(W)=r(V_2)+r(\sigma(V_1)\cap W)-r(\sigma(V_1)) = n-r(\sigma(V_1))， 
故r(\tau)\le r(\tau\sigma)+n-r(\sigma)，即r(\sigma)+r(\tau)-n\le r(\tau\sigma) 
~
定理3.5：r(\sigma+\tau)\le r(\sigma)+r(\tau) 
定理3.6：设B=\left\{\alpha_1,\alpha_2,\dots,\alpha_n\right\}是V_1的一组基，S=\left\{\beta_1,\beta_2,\dots,\beta_n\right\}是V_2的一组基， 
则存在唯一的\sigma\in L(V_1,V_2)，使得\sigma(\alpha_i)=\beta_i，i=1,2,\dots,n 
定理3.7：线性空间L(V_1,V_2)的维数是nm 

#### 线性空间的同构

若由线性空间V_1到V_2存在一个线性双射\sigma，则称V_1和V_2是同构的
定理3.8：两个有限维线性空间V_1和V_2同构的充要条件是它们的维数相同







### 行列式
#### 行列式的性质

性质1：若有一列为零向量，则行列式等于0 
性质2：若有两列元素相同，则行列式等于0 
性质3：若有两列元素成比例，则行列式等于0 
性质4：对行列式作倍加列变换，行列式的值不变 
性质5：若行列式列向量线性相关，则行列式等于0 
性质6：|A^T|=|A| 
~
M_{ij}为余子式，A_{ij}为代数余子式 
引理：D=|A|=a_{nn}A_{nn} 
\displaystyle{定理5.1：D=\sum_{k=1}^n a_{kj}A_{kj} = \sum_{k=1}^n a_{ik}A_{ik}} 
\displaystyle{定理5.2：\sum_{k=1}^n a_{kj}A_{ki} = \sum_{k=1}^n a_{jk}A_{ik} = 0， i\neq j} 

\sum_{k=1}^n a_{kj}A_{ki} = \sum_{k=1}^n a_{jk}A_{ik} = \delta_{ij}D,
~
Kronecker符号：\delta_{ij} = \left\{\begin{matrix}
    1，i=j  0，i\neq j
\end{matrix}\right.

~
定理5.3：若A,B\in M_n(F)，则|AB|=|A||B| 
定理5.4：n阶矩阵A可逆的充要条件是|A|\neq 0 
三角块矩阵A=\begin{pmatrix} B & *  O & C\end{pmatrix}可逆的充要条件为|A|=|B||C|\neq 0 
奇数阶反对称矩阵不可逆

~
A的非零子式的最高阶数r称为A的行列式秩
定理5.5：r(A) = r的充要条件是A的行列式秩为r


定理5.6(Cramer法则)：设A=(a_{ij})_{nn}，
若线性方程组AX=b的系数行列式D=|A|\neq 0，则方程组有唯一解x_j=\frac{D_j}{D}，
其中D_j为第j列被b取代的的行列式


定理5.7：齐次线性方程组AX=0有非零解的充要条件为|A|\neq 0 
~
定理5.8：设R^n中m个列向量\alpha_1,\dots,\alpha_m 线性无关，A=(\alpha_1,\dots,\alpha_m)_{n\times m}，
则V_m^2(\alpha_1,\dots,\alpha_m)=|A^TA|


#### 常见计算
$$
D_n = \begin{vmatrix}
    a & b & \cdots & b \\
    b & a & \cdots & b \\
    \vdots & \vdots & \ddots & \vdots \\
    b & b & \cdots & a
\end{vmatrix} = [a+(n-1)b](a-b)^{n-1}
$$

$$
\begin{vmatrix}
    A & O \\ C & B
\end{vmatrix} = |A||B|，
\\~\\
\begin{vmatrix}
    O & A \\ B & C
\end{vmatrix} = (-1)^{km}|A||B|
$$

###### n阶三对角行列式
$$
D_n = \begin{vmatrix}
    a & b & & & & \\
    c & a & b & & & \\
    & c & a & \ddots & & \\
    & & \ddots & \ddots & \ddots & \\
    & & & \ddots & a & b \\
    & & & & c & a
\end{vmatrix} = aD_{n-1} - bcD_{n-2}
$$

设 $\alpha+\beta=a, \alpha\beta = bc$,
则 $D_n - \beta D_{n-1} = \alpha(D_{n-1} - \beta D_{n-2})$,
故 $D_n - \beta D_{n-1} = \alpha^{n-2}(a^2-bc-\beta a)=\alpha^n$, 
即
$$
\begin{aligned}
  D_n &= \alpha^n + \beta D_{n-1} \\
  &= \alpha^n+\alpha^{n-1}\beta+\beta^2D_{n-2} \\
  &= \alpha^n+\alpha^{n-1}\beta+\cdots+\alpha^2\beta^{n-2}+\beta^{n-1}D_1 \\
  &= \alpha^n+\alpha^{n-1}\beta+\cdots+\alpha^2\beta^{n-2}+\alpha\beta^{n-1}+\beta^n \\
  &= \left\{\begin{matrix}
      (n+1)\alpha^n, \alpha = \beta \\
      \displaystyle \frac{\alpha^{n+1}-\beta^{n+1}}{\alpha-\beta}, \alpha \neq \beta
  \end{matrix}\right.
\end{aligned}
$$

###### 范德蒙(Vandermonde)行列式
$$
V_n = \begin{vmatrix}
    1 & 1 & 1 & \cdots & 1 \\
    x_1 & x_2 & x_3 & \cdots & x_n \\
    x_1^2 & x_2^2 & x_3^2 & \cdots & x_n^2 \\
    \vdots & & & & \vdots \\
    x_1^{n-1} & x_2^{n-1} & x_3^{n-1} & \cdots & x_n^{n-1}
\end{vmatrix}
\\~\\
= \begin{vmatrix}
    1 & 1 & 1 & \cdots & 1 \\
    0 & x_2-x_1 & x_3-x_1 & \cdots & x_n-x_1 \\
    0 & x_2(x_2-x_1) & x_3(x_3-x_1) & \cdots & x_n(x_n-x_1) \\
    \vdots & & & & \vdots \\
    0 & x_2^{n-1}(x_2-x_1) & x_3^{n-1}(x_3-x_1) & \cdots & x_n^{n-1}(x_n-x_1)
\end{vmatrix}
\\~\\
= (x_2-x_1)(x_3-x_1)\cdots(x_n-x_1) V_{n-1}
\\~\\
= \prod_{1\le i\lt j\le n} (x_j-x_i)
$$


