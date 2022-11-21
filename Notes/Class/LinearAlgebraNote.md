[toc]


## 集合 关系 运算 结构
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
DeMorgan律：\bar{A\cup B} = \bar{A}\cap \bar{B}\\
\qquad \qquad \qquad \quad \bar{A\cup B} = \bar{A}\cap \bar{B}\\
~\\
A\setminus B = A\cap \bar{B}\\
(A\cap B)\setminus C = A\cup(B\setminus C)\\
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
- 外积（叉积，向量积）：$a \times b = |a||b|sin\left<a,b \right>，方向为右手伸开由a转到b$
- 混合积：$a\cdot(b\times c)=b\cdot(c\times a)=c\cdot(a\times b)$
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
- 齐次线性方程组总是有解的，当$r=n$时有唯一解，当$r<n$时有无穷多个解
#### 代数结构
- $\left<G:\circ\right>$称为群，如果：满足结合律；存在单位元；存在逆元
  - 半群：满足结合律
  - 含幺半群：满足结合律；存在单位元
  - 交换群：满足结合律；存在单位元；存在逆元；满足交换律
- $\left<R:+,\circ\right>$称为环，如果：
  - $\left<R:+\right>$是交换群（加法群）
  - $\left<R:\circ\right>$是半群，即不一定有单位元和逆元
  - $“+”$对$“\circ”$满足左、右分配律
  - 若乘法满足结合律，则称其为交换环
  - 若乘法存在单位元，则称其为含幺环
- $\left<F:+,\circ\right>$称为域，如果：
  - 是至少含有两个元的交换环
  - $F\setminus \left\{0\right\}$关于乘法运算是交换群





## 线性空间
#### 定义与定理
$
如果\left<V:+\right>是一个交换群（加法群），\\
且\forall \alpha,\beta\in V,\forall \lambda,\mu\in F，以及域F的乘法单位元1，有：\\
1\alpha=\alpha\\
\lambda(\mu\alpha)=(\lambda\mu)\alpha\\
(\lambda+\mu)\alpha=\lambda\alpha+\mu\alpha\\
\lambda(\alpha+\beta)=\lambda\alpha+\lambda\beta\\
则称V为域F上的线性空间，记作V(F)
$
$~\\
定理2.1：V(F)的\bm{非空}子集W为V的子空间\\
\iff W对于V(F)的线性运算封闭\\
定理2.2：V(F)的非空子集S的线性扩张L(S)是V中包含S的最小子空间\\
~\\
定理2.3：V(F)中的向量组\alpha_1,\alpha_2,\dots,\alpha_m(m\ge 2)线性相关\\
\iff \alpha_1,\alpha_2,\dots,\alpha_m中存在向量可由其余向量在域F上线性表示\\
定理2.3等价命题：\alpha_1,\alpha_2,\dots,\alpha_m(m\ge 2)线性无关\\
\iff 任何一个向量都不能由其余向量线性表示\\
~\\
定理2.4：若\left\{\alpha_1,\alpha_2,\dots,\alpha_n\right\}线性无关，\left\{\beta,\alpha_1,\alpha_2,\dots,\alpha_n\right\}线性相关，\\
则\beta可由\alpha_1,\alpha_2,\dots,\alpha_n线性表示，且表示法唯一\\
推论：若\left\{\alpha_1,\alpha_2,\dots,\alpha_n\right\}是R^n中线性无关的n个向量，\\
则R^n中任一向量可由\left\{\alpha_1,\alpha_2,\dots,\alpha_n\right\}线性表示\\
~\\
定理2.5：设\left\{\beta_1,\beta_2,\dots,\beta_s\right\}中的每个向量可由\left\{\alpha_1,\alpha_2,\dots,\alpha_r\right\}线性表示，\\
若s>r，则\left\{\beta_1,\beta_2,\dots,\beta_s\right\}线性相关\\
定理2.5等价命题：若\left\{\beta_1,\beta_2,\dots,\beta_s\right\}线性无关，则s\le r\\
~\\
若S中每个向量可由T线性表示，则r(S)\le r(T)
$
#### 交、和与直和
$
dimW_1+dimW_2=dim(W_1+W_2)+dim(W_1\cap W_2)\\
~\\
定理2.7：对V的子空间W_1,W_2，下列命题等价：\\
(1)W_1+W_2是直和，即W_1\cap W_2=\left\{0\right\}\\
(2)W_1+W_2中的每个向量\alpha的分解式\alpha=\alpha_1+\alpha_2唯一\\
(3)零向量\bm{0}的分解式0=\alpha_1+\alpha_2，仅当\alpha_1=\alpha_2=0时成立\\
(4)dim(W_1+W_2)=dimW_1+dimW_2\\
~\\
若V=W_1\oplus +W_2，则称W_1为W_2的补空间，W_2为W_1的补空间\\
求线性空间的基：如给方程，则求解空间；如给向量组，则高斯消元\\
求子空间的和的基：求子空间的基，然后高斯消元\\
求子空间的交的基：如给方程，则交为方程组的解空间，否则先求和\\
求补空间的基（扩充基）：用观察法或行列式找出不能线性表示的向量\\
~\\
若W_1\perp W_2且W_1+W_2=V，则称W_2是W_1的正交补，记作W_1^{\perp}\\
求正交补的基（扩充单位正交基）：与已有正交基联立，求解空间的基
$
#### 内积空间
$
若\forall \alpha,\beta\in V,\lambda\in R，满足下列条件，则称实数(\alpha,\beta)为向量\alpha,\beta的内积：\\
交换律：(\alpha,\beta)=(\beta,\alpha) \\
分配律：(\alpha+\beta,\gamma)=(\alpha,\gamma)+(\beta+\gamma) \\
数乘性：(\lambda\alpha,\beta)=\lambda(\alpha,\beta) \\
正定性：(\alpha,\alpha)\geqslant 0, 当且仅当\alpha=0时等号成立\\
~\\
有限维实内积空间称为欧氏(Euclid)空间\\
~\\
设自然基\left\{e_1,e_2,\dots,e_n\right\}下的标准内积为\alpha\cdot\beta，\\经变换矩阵A变换后，基变为\left\{\epsilon_1,\epsilon_2,\dots,\epsilon_n \right\}，\\
设\alpha=\sum_{i=1}^n a_i'\epsilon_i，\beta=\sum_{i=1}^n b_i'\epsilon_i，则(\alpha,\beta)=\sum_{i=1}^n\sum_{j=1}^n
a_i' b_j'(\epsilon_i,\epsilon_j)\\
~\\
柯西-施瓦兹不等式：|(\alpha,\beta)|\le |\alpha||\beta|\\
三角不等式：|\alpha+\beta|\le |\alpha|+|\beta| \\
$

#### 施密特(Schmidt)正交化
$$
\beta_n = \alpha_n
-\frac{(\alpha_n,\beta_{n-1})}{(\beta_{n-1},\beta_{n-1})}\beta_{n-1}
-\cdots-\frac{(\alpha_n,\beta_2)}{(\beta_2,\beta_2)}\beta_2
-\frac{(\alpha_n,\beta_1)}{(\beta_1,\beta_1)}\beta_1 \\~\\
单位化：\epsilon_m=\frac{\beta_m}{|\beta_m|}
$$




## 线性映射
#### 像与核
$
Im\sigma 是V_2的一个子空间，Ker\sigma 是V_1的一个子空间\\
线性空间在线性映射下的的像与完全原像仍为线性空间\\
定理3.1：线性映射\sigma是单射\iff \sigma^{-1}(0_2)=\left\{0_1\right\}
$
#### 线性映射的秩
$
r(\sigma)=dim(Im\sigma)=r(\sigma(B))\\
定理3.2：dim(Im\sigma)+dim(Ker\sigma)=dimV_1=n\\
定理3.3：如果V_1和V_2都是n维线性空间，则下列命题等价：\\
(1)r(\sigma)=n，即\sigma满秩；(2)\sigma是单射；\\
(3)\sigma是满射；(4)\sigma是可逆线性映射 \\
~\\
定理3.4：设V_1,V_2,V_3分别为m,n,s维线性空间，\\
则r(\sigma)+r(\tau)-n\le r(\tau\sigma)\le min(r(\sigma),r(\tau)) \\
Proof：令V_2=\sigma(V_1)\oplus W，\\
则r(\tau(V_2))=r(\tau(\sigma(V_1)+W))=r(\tau\sigma(V_1)+\tau(W))\le r(\tau\sigma)+r(\tau(W))， \\
且r(\tau(W))\le r(W)=r(V_2)+r(\sigma(V_1)\cap W)-r(\sigma(V_1))\le n-r(\sigma(V_1))， \\
故r(\tau)\le r(\tau\sigma)+n-r(\sigma)，即r(\sigma)+r(\tau)-n\le r(\tau\sigma) \\
~\\
定理3.5：r(\sigma+\tau)\le r(\sigma)+r(\tau) \\
定理3.6：设B=\left\{\alpha_1,\alpha_2,\dots,\alpha_n\right\}是V_1的一组基，S=\left\{\beta_1,\beta_2,\dots,\beta_n\right\}是V_2的一组基， \\
则存在唯一的\sigma\in L(V_1,V_2)，使得\sigma(\alpha_i)=\beta_i，i=1,2,\dots,n \\
定理3.8：线性空间L(V_1,V_2)的维数是nm \\
$
#### 线性空间的同构
$
若由线性空间V_1到V_2存在一个线性双射\sigma，则称V_1和V_2是同构的\\
定理3.9：两个有限维线性空间V_1和V_2同构的充要条件是它们的维数相同
$





## 矩阵
#### 坐标变换与基的变换
$$
A:\epsilon \rightarrow e, \sigma(\epsilon) = (e)A \\
B:e \rightarrow \eta, \tau(e) = (\eta)B \\
\tau\sigma(\epsilon) = \tau((e)A) 
= \tau(\sum a_{i1}e_i,\sum a_{i2}e_i,\cdots,\sum a_{in}e_i) \\
= (\tau(e_1),\tau(e_2),\cdots,\tau(e_n))A = \tau(e)A = (\eta)BA \\
~\\
\sigma((\epsilon) X) = \sum x_i\sigma(\epsilon_i)
= \sigma(\epsilon)X = (e)AX， \\
故Y = AX \\
\tau\sigma(\epsilon X) = \tau((e)Y) = (\eta)BY = (\eta)BAX， \\
故Z = BAX \\
~\\
若基B_1到B_2的变换矩阵为A，基B_2到基B_3的变换矩阵为B，\\
不妨设(\eta)=(e)B，(e)=(\epsilon)A， \\
则基B_1到基B_3的变换矩阵为AB
$$

#### 矩阵的秩
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

#### 矩阵的高阶幂
##### 三角形式
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
##### 指数形式（矩阵秩为1）
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
##### 阶梯形式
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
##### 例题
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

#### 矩阵求逆
##### 零化多项式
$$
令f(x) = \sum_{k=0}^n a_kx^k且f(A)=O, 
g(x) = \sum_{k=1}^n a_kx^{k-1} \\~\\
(1) 若a_0\neq0，则A可逆，且A^{-1} = -\frac{1}{a_0}g(A) \\
(2) 若a_0=0，且g(A)\neq O，则A不可逆
$$
##### 三角块方阵
$$
\begin{pmatrix}A & C \\ O & B\end{pmatrix}^{-1} = 
\begin{pmatrix}A^{-1} & -A^{-1}CB^{-1} \\ O & B^{-1}\end{pmatrix}
$$
##### 加边法
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
##### 伴随矩阵法
$$
A^{-1} = \frac{A^*}{|A|}
$$
##### 例题
$$
设X=(x_1,x_2,\cdots,x_n)，Y=(y_1,y_2,\cdots,y_n)，且XY^T=2\\
若A = E + X^TY，请证明A可逆，并求其逆矩阵
$$
$A^2 = E+2X^TY+(X^TY)^2 = E+4X^TY，\\
故4A-A^2 = 3E，即A\times \frac{4E-A}{3} = E，故逆矩阵为\frac{4E-A}{3}$

#### 其他
$AB与BA的迹相同，故AB-BA\neq E$

$~\\ \begin{pmatrix}a & 0 \\ 0 & a^{-1} \end{pmatrix} 可表示为倍加初等矩阵的乘积 \\
Proof:\rightarrow
\begin{pmatrix}a & 1 \\ 0 & a^{-1} \end{pmatrix} \rightarrow
\begin{pmatrix}0 & 1 \\ -1 & a^{-1} \end{pmatrix} \rightarrow
\begin{pmatrix}0 & 1 \\ -1 & 0 \end{pmatrix} \rightarrow
\begin{pmatrix}1 & 0 \\ 0 & 1 \end{pmatrix}$




## 行列式
#### 常见计算
$$D_n = \begin{vmatrix}
    a & b & \cdots & b \\
    b & a & \cdots & b \\
    \vdots & \vdots & \ddots & \vdots \\
    b & b & \cdots & a
\end{vmatrix} = [a+(n-1)b](a-b)^{n-1}$$

$$~\\~\\
\begin{vmatrix}
    A & C \\ O & B
\end{vmatrix} = |A||B|$$

###### n阶三对角行列式
$$D_n = \begin{vmatrix}
    a & b & & & & \\
    c & a & b & & & \\
    & c & a & \ddots & & \\
    & & \ddots & \ddots & \ddots & \\
    & & & \ddots & a & b \\
    & & & & c & 
\end{vmatrix} = aD_{n-1} - bcD_{n-2} \\ ~\\
设\alpha+\beta=a, \alpha\beta = bc,
则D_n - \beta D_{n-1} = \alpha(D_{n-1} - \beta D_{n-2}),\\
故D_n - \beta D_{n-1} = \alpha^{n-2}(a^2-bc-\beta a)=\alpha^n, \\$$
$即D_n = \alpha^n + \beta D_{n-1}\\
= \alpha^n+\alpha^{n-1}\beta+\beta^2D_{n-2}\\
= \alpha^n+\alpha^{n-1}\beta+\cdots+\alpha^2\beta^{n-2}+\beta^{n-1}D_1\\
= \alpha^n+\alpha^{n-1}\beta+\cdots+\alpha^2\beta^{n-2}+\alpha\beta^{n-1}+\beta^n \\
= \left\{\begin{matrix}
    \frac{\alpha^{n+1}-\beta^{n+1}}{\alpha-\beta}, \alpha \neq \beta\\
    (n+1)\alpha^n, \alpha = \beta
\end{matrix}\right.$

###### 范德蒙(Vandermonde)行列式
$$V_n = \begin{vmatrix}
    1 & 1 & 1 & \cdots & 1 \\
    x_1 & x_2 & x_3 & \cdots & x_n \\
    x_1^2 & x_2^2 & x_3^2 & \cdots & x_n^2 \\
    \vdots & & & & \vdots \\
    x_1^{n-1} & x_2^{n-1} & x_3^{n-1} & \cdots & x_n^{n-1}
\end{vmatrix} \\~\\
= \begin{vmatrix}
    1 & 1 & 1 & \cdots & 1 \\
    0 & x_2-x_1 & x_3-x_1 & \cdots & x_n-x_1 \\
    0 & x_2(x_2-x_1) & x_3(x_3-x_1) & \cdots & x_n(x_n-x_1) \\
    \vdots & & & & \vdots \\
    0 & x_2^{n-1}(x_2-x_1) & x_3^{n-1}(x_3-x_1) & \cdots & x_n^{n-1}(x_n-x_1)
\end{vmatrix} \\~\\
= (x_2-x_1)(x_3-x_1)\cdots(x_n-x_1) V_{n-1} \\~\\
= \prod_{1\le i\lt j\le n} (x_j-x_i)$$



1
5
2
4
3


















