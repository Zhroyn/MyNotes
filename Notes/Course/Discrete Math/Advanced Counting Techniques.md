<!-- TOC -->

- [Advanced Counting Techniques](#advanced-counting-techniques)
  - [8.1 Applications of Recurrence Relations](#81-applications-of-recurrence-relations)
  - [8.2 Solving Linear Recurrence Relations](#82-solving-linear-recurrence-relations)
  - [8.4 Generating Functions](#84-generating-functions)
    - [Useful Generating Functions](#useful-generating-functions)
    - [Solving Counting Problems by Generating Functions](#solving-counting-problems-by-generating-functions)
    - [Solving Recurrence Relations by Generating Functions](#solving-recurrence-relations-by-generating-functions)
    - [Proving Identities by Generating Functions](#proving-identities-by-generating-functions)

<!-- /TOC -->





## Advanced Counting Techniques

### 8.1 Applications of Recurrence Relations
- A rule for determining subsequent terms from those that precede them, is called a **recurrence relation**



### 8.2 Solving Linear Recurrence Relations
**Linear Homogeneous Recurrence Relations**
- A **linear homogeneous recurrence relation of degree k with constant coefficients** is a recurrence relation of the form $a_n = c_1a_{n−1} + c_2a_{n−2} + ⋯ + c_ka_{n−k}$.
- $r^k − c_1r^{k−1} − c_2r^{k−2} − ⋯ − c_{k−1}r − c_k = 0$ is called the **characteristic equation** of the recurrence relation.
<br>

**THEOREM 1** : 
Let $c_1$ and $c_2$ be real numbers. Suppose that $r_2 − c_1r − c_2 = 0$ has only one root $r_0$. 
Then the sequence $\{a_n\}$ is a solution of the recurrence relation $a_n = c_1a_{n−1} + c_2a_{n−2}$ if and only if $a_n = \alpha_1r_1^n + \alpha_2r_n^2$ for $n = 0, 1, 2, …$ , where $\alpha_1$ and $\alpha_2$ are constants.

**THEOREM 2** : 
Let $c_1$ and $c_2$ be real numbers with $c_2 ≠ 0$. Suppose that $r_2 − c_1r − c_2 = 0$ has two distinct roots $r_1$ and $r_2$. 
Then the sequence $\{a_n\}$ is a solution of the recurrence relation $a_n = c_1a_{n−1} + c_2a_{n−2}$ if and only if $a_n = \alpha_1r_0^n + \alpha_2nr_0^2$ for $n = 0, 1, 2, …$ , where $\alpha_1$ and $\alpha_2$ are constants.
<br>

**THEOREM 3** : 
Suppose that the characteristic equation $r^k − c_1r^{k−1} − ⋯ − c_k = 0$ has $k$ distinct roots $r_1, r_2, … , r_k$. 
Then a sequence $\{a_n\}$ is a solution of the recurrence relation $a_n = c_1a_{n−1} + c_2a_{n−2} + ⋯ + c_ka_{n−k}$ if and only if $a_n = \alpha_1r_1^n + \alpha_2r_2^n + ⋯ + \alpha_kr_k^n$ for $n = 0, 1, 2, …$

**THEOREM 4** : 
Suppose that the characteristic equation $r^k − c_1r^{k−1} − ⋯ − c_k = 0$ has $t$ distinct roots $r_1, r_2, … , r_t$ with multiplicities $m_1, m_2, … , m_t$, respectively, so that $m_1 + m_2 + ⋯ + m_t = k$. Then a sequence $\{a_n\}$ is a solution of the recurrence relation $a_n = c_1a_{n−1} + c_2a_{n−2} + ⋯ + c_ka_{n−k}$ if and only if 
  $\begin{aligned} a_n = &(\alpha_{1,0} + \alpha_{1,1}n + ⋯ + \alpha_{1,m_1-1}n^{m_1-1})r_1^n \\
  &+ (\alpha_{2,0} + \alpha_{2,1}n + ⋯ + \alpha_{2,m_2-1}n^{m_2-1})r_2^n \\
  &+ ⋯ + (\alpha_{t,0} + \alpha_{t,1}n + ⋯ + \alpha_{t,m_t-1}n^{m_t-1})r_t^n \end{aligned}$ 
  for $n = 0, 1, 2, …$


**Linear Nonhomogeneous Recurrence Relations**
- A **linear nonhomogeneous recurrence relation with constant coefficients** is a recurrence relation of the form $a_n = c_1a_{n−1} + c_2a_{n−2} + ⋯ + c_ka_{n−k} + F(n)$.
- The recurrence relation $a_n = c_1a_{n−1} + c_2a_{n−2} + ⋯ + c_ka_{n−k}$ is called the **associated homogeneous recurrence relation**.

**THEOREM 5** : 
If $\{a^{(p)}_n\}$ is a particular solution of the nonhomogeneous linear recurrence relation with constant coefficients, then every solution is of the form $\{a^{(p)}_n + a^{(h)}_n \}$, where $\{a^{(h)}_n\}$ is a solution of the associated homogeneous recurrence relation.
<br>

**THEOREM 6** :
Suppose that $\{a^n\}$ satisfies the linear nonhomogeneous recurrence relation $a_n = c_1a_{n−1} + c_2a_{n−2} + ⋯ + c_ka_{n−k} + F(n)$, where
  $\qquad F(n) = (b_tn^t + b_{t−1}n^{t−1} + ⋯ + b_1n + b_0)s^n$.
When $s$ is not a root of the characteristic equation of the associated linear homogeneous recurrence relation, there is a particular solution of the form
  $\qquad (p_tn^t + p_{t−1}n^{t−1} + ⋯ + p_1n + p_0)s^n$.
When s is a root of this characteristic equation and its multiplicity is $m$, there is a particular solution of the form
  $\qquad n^m(p_tn^t + p_{t−1}n^{t−1} + ⋯ + p_1n + p_0)s^n$.





### 8.4 Generating Functions
- The **generating function** for the sequence $a_0, a_1, … , a_k, …$ of real numbers is the infinite series $\displaystyle G(x) = a_0 + a_1x + ⋯ + a_kx_k + ⋯ = \sum^∞_{k = 0} a_kx_k$.

**THEOREM 1** : 
- $\displaystyle f(x) + g(x) = \sum^∞_{k = 0} (a_k + b_k)x^k$
- $\displaystyle x\cdot f'(x) = \sum^∞_{k = 0} k\cdot a_kx^k$
- $\displaystyle f(x)g(x) = \sum^∞_{k = 0} ( \sum^k_{j=0}a_jb_{k−j})x^k$
<br>

$\displaystyle \begin{aligned}
\begin{pmatrix} -n \\ r \end{pmatrix}
&= \frac{(-n)(-n-1)\cdots (-n-r+1)}{r!} \\
&= \frac{(-1)^r n(n+1)\cdots (n+r-1)}{r!} \\
&= \frac{(-1)^r (n+r-1)(n+r-2)\cdots (n)}{r!} \\
&= \frac{(-1)^r (n+r-1)!}{r!(n-1)!} \\
&= (-1)^r \begin{pmatrix} n+r-1 \\ r \end{pmatrix} \\
&= (-1)^r C(n+r-1, r)
\end{aligned} $

**THEOREM 2 (THE EXTENDED BINOMIAL THEOREM)** : 
$\displaystyle (1 + x)^u = \sum^∞_{k = 0}\begin{pmatrix} u \\ k \end{pmatrix}x^k$

#### Useful Generating Functions
| $a_k$ | $G(x)$ |
|:---:|:---:|
| $C(n, k) $ | $(1 + x)^n $ |
| $C(n, k)A^k $ | $(1 + Ax)^n $ |
| $C(n, k/r) \text{ if } r\vert k \text{ else 0} $ | $(1 + x^r)^n $ |
| $1 $ | $\displaystyle \frac{1}{1 - x} $ |
| $a^k $ | $\displaystyle \frac{1}{1 - ax} $ |
| $1 \text{ if } r\vert k \text{ else 0} $ | $\displaystyle \frac{1}{1 - x^r} $ |
| $k + 1 $ | $\displaystyle \frac{1}{(1 - x)^2} $ |
| $k $ | $\displaystyle \frac{x}{(1 - x)^2} $ |
| $C(n + k - 1, k) $ | $\displaystyle \frac{1}{(1 - x)^n} $ |
| $(-1)^kC(n + k - 1, k) $ | $\displaystyle \frac{1}{(1 + x)^n} $ |
| $C(n + k - 1, k)A^k $ | $\displaystyle \frac{1}{(1 - Ax)^n} $ |
| $\displaystyle \frac{1}{k!} $ | $e^x $ |
| $\displaystyle \frac{(-1)^{k+1}}{k} $ | $\ln x $ |

#### Solving Counting Problems by Generating Functions
> Determine the number of ways to insert tokens worth \$1, \$2 and \$5 into a vending machine to pay for an item that costs r dollars in both the cases when the order in which the tokens are inserted does not matter and when the order does matter
> 
>  When the order does not matter, $G(x) = (1 + x + x^2 + x^3 + \cdots)(1 + x^2 + x^4 + x^6 + \cdots)(1 + x^5 + x^{10} + x^{15} + \cdots) $
>  When the order does matter, $G(x) = (x + x^2 + x^5)^n $

#### Solving Recurrence Relations by Generating Functions
> Use generating functions to solve the recurrence relation $a_n = 2a_{n-1} + 3a_{n-2} + 4^n + 5n + 6 $ with initial conditions $a_0 = 20, a_1 = 60. $
>
> $\displaystyle \Rightarrow a_nx^n = 2a_{n-1}x^n + 3a_{n-2}x^n + 4^nx^n + 5nx^n + 6x^n $
> $\displaystyle \Rightarrow \sum_{n=2}^{\infty}a_nx^n = 2\sum_{n=2}^{\infty}a_{n-1}x^n + 3\sum_{n=2}^{\infty}a_{n-2}x^n + \sum_{n=2}^{\infty}4^nx^n + 5\sum_{n=2}^{\infty}nx^n + 6\sum_{n=2}^{\infty}x^n $
> $\displaystyle \Rightarrow G(x) - a_0 - a_1x = 2x(G(x) - a_0) + 3x^2G(x) + \frac{1}{1-4x} - 1 - 4x + 5\left[\frac{x}{(1-x)^2} - x\right] + 6\left(\frac{1}{1-x} - 1 - x\right) $
> &nbsp;

#### Proving Identities by Generating Functions
> Prove $\displaystyle C(n, r) = C(n-1, r) + C(n-1, r-1) $ by $(1 + x)^n = (1 + x)^{n-1} + x(1 + x)^{n-1} $
> Prove $\displaystyle \sum_{k=0}^n C(n, k)^2 = C(2n, n) $ by $(1 + x)^{2n} = (1 + x)^n(1 + x)^n $
> Prove $\displaystyle \sum_{k=0}^r C(m , r-k)C(n, k) = C(m + n, r) $ by $(1 + x)^{m + n} = (1 + x)^m(1 + x)^n $


