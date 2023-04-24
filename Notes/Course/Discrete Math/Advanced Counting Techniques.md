<!-- TOC -->

- [Advanced Counting Techniques](#advanced-counting-techniques)
  - [8.1 Applications of Recurrence Relations](#81-applications-of-recurrence-relations)
  - [8.2 Solving Linear Recurrence Relations](#82-solving-linear-recurrence-relations)
    - [Linear Homogeneous Recurrence Relations](#linear-homogeneous-recurrence-relations)
    - [Linear Nonhomogeneous Recurrence Relations](#linear-nonhomogeneous-recurrence-relations)
  - [8.4 Generating Functions](#84-generating-functions)
    - [Useful Generating Functions](#useful-generating-functions)
    - [Solving Counting Problems by Generating Functions](#solving-counting-problems-by-generating-functions)
    - [Solving Recurrence Relations by Generating Functions](#solving-recurrence-relations-by-generating-functions)
    - [Proving Identities by Generating Functions](#proving-identities-by-generating-functions)
  - [8.5 Inclusion-Exclusion](#85-inclusion-exclusion)
    - [An Alternative Form of Inclusion–Exclusion](#an-alternative-form-of-inclusionexclusion)
    - [The Sieve of Eratosthenes](#the-sieve-of-eratosthenes)
    - [The Number of Onto Functions](#the-number-of-onto-functions)
    - [Derangements](#derangements)

<!-- /TOC -->





## Advanced Counting Techniques

### 8.1 Applications of Recurrence Relations
- A rule for determining subsequent terms from those that precede them, is called a **recurrence relation**



### 8.2 Solving Linear Recurrence Relations
#### Linear Homogeneous Recurrence Relations
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


#### Linear Nonhomogeneous Recurrence Relations
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






### 8.5 Inclusion-Exclusion
**THE PRINCIPLE OF INCLUSION–EXCLUSION**
Let $A_1, A_2, … , A_n$ be finite sets, then
$$\begin{aligned}
  |A1 ∪ A2 ∪ ⋯ ∪ An| = &\sum_{1≤i≤n}|A_i| − \sum_{1≤i<j≤n}|A_i ∩ A_j| + \sum_{1≤i<j<k≤n}|A_i ∩ A_j ∩ A_k| \\
  &− ⋯ + (−1)^{n+1}|A_1 ∩ A_2 ∩ ⋯ ∩ A_n| \\
\end{aligned} $$

$ \text{Proof :} $
Suppose that $a$ is a member of exactly $r$ of the sets $A_1, A_2, … , A_n$ where $1 ≤ r ≤ n$.
In general, it is counted $C(r, m)$ times by the summation involving $m$ of the sets $A_i$.
Thus, this element is counted exactly 
$$
C(r, 1) − C(r, 2) + C(r, 3) − ⋯ + (−1)^{r+1}C(r, r) \\ 
= C(r, 0) - (1 - 1)^r = 1
$$


#### An Alternative Form of Inclusion–Exclusion
Let $A_i$ be the subset containing the elements that have property $P_i$.
Then the number of elements with all the properties $P_1, P_2, … , P_k$ is denoted by $N(P_1 P_2 … P_k)$.
The number of elements with none of the properties $P_1, P_2, … , P_k$ is denoted by $N(P'_1 P'_2 … P'_k)$.
The number of elements in the set is denoted by $N$.

From the inclusion-exclusion principle, we see that
$$\begin{aligned}
  N(P'_1 P'_2 … P'_n) = &N − \sum_{1≤i≤n}N(P_i) + \sum_{1≤i<j≤n}N(P_iP_j) \\
  &- ⋯ + (−1)^{n}N(P_1 P_2 … P_n) \\
\end{aligned} $$

> How many solutions does $x_1 + x_2 + x_3 = 11$ have, where $x_1, x_2$, and $x_3$ are nonnegative integers with $x_1 ≤ 3, x_2 ≤ 4$, and $x_3 ≤ 6$?
> Let a solution have property $P_1$ if $x_1 > 3$, property $P_2$ if $x_2 > 4$, and property $P_3$ if $x_3 > 6$. Then:
> $N = C(13, 2) = 78, $
> $N(P_1) = C(9, 2) = 36, $
> $N(P_2) = C(8, 2) = 28, $
> $N(P_3) = C(6, 2) = 15, $
> $N(P_1P_2) = C(4, 2) = 36, $
> $N(P_1P_3) = 1, $
> $N(P_2P_3) = 0, $
> $N(P_1P_2P_3) = 0. $
> So $N(P'_1P'_2P'_3) = 78 − 36 − 28 − 15 + 6 + 1 + 0 − 0 = 6.$

> How many positive integers not exceeding $1000$ that are not divisible by $5, 6, 8$?
> $\displaystyle \begin{aligned}
  N(P'_1P'_2P'_3) = &\; 1000 - \lfloor \frac{1000}{5} \rfloor - \lfloor \frac{1000}{6} \rfloor - \lfloor \frac{1000}{8} \rfloor \\
  & + \lfloor \frac{1000}{5\cdot 6} \rfloor + \lfloor \frac{1000}{5\cdot 8} \rfloor + \lfloor \frac{1000}{3\cdot 8} \rfloor - \lfloor \frac{1000}{5\cdot 3 \cdot 8} \rfloor \\
  = &\; 1000 - 200 - 166 - 125 + 33 + 25 + 41 - 8 \\
  = &\; 600 \\
\end{aligned}$

#### The Sieve of Eratosthenes
> How many primes are there that do not exceed $100$?
> Let $P_1$ be the property that an integer is divisible by $2$, 
> let $P_2$ be the property that an integer is divisible by $3$, 
> let $P_3$ be the property that an integer is divisible by $5$, 
> and let $P_4$ be the property that an integer is divisible by $7$.
> Thus, the number of primes not exceeding $100$ is $4 + N(P'_1P'_2P'_3P'_4)$.
> $\displaystyle \begin{aligned}
  N(P'_1P'_2P'_3P'_4) 
  = &\; 99 - \lfloor \frac{100}{2} \rfloor - \lfloor \frac{100}{3} \rfloor - \lfloor \frac{100}{5} \rfloor - \lfloor \frac{100}{7} \rfloor \\
    & + \lfloor \frac{100}{2\cdot 3} \rfloor + \lfloor \frac{100}{2\cdot 5} \rfloor + \lfloor \frac{100}{2\cdot 7} \rfloor + \lfloor \frac{100}{3\cdot 5} \rfloor + \lfloor \frac{100}{3\cdot 7} \rfloor + \lfloor \frac{100}{5\cdot 7} \rfloor \\
    & - \lfloor \frac{100}{2\cdot 3\cdot 5} \rfloor - \lfloor \frac{100}{2\cdot 3\cdot 7} \rfloor - \lfloor \frac{100}{2\cdot 5\cdot 7} \rfloor - \lfloor \frac{100}{3\cdot 5\cdot 7} \rfloor \\
    & + \lfloor \frac{100}{2\cdot 3\cdot 5\cdot 7} \rfloor \\
  = &\; 99 - 50 - 33 - 20 - 14 + 16 + 10 + 7 + 6 + 4 + 2 \\
    & - 3 - 2 - 1 - 0 + 0 \\
  = &\; 21
\end{aligned} $

#### The Number of Onto Functions
The principle of inclusion–exclusion can also be used to determine the number of onto functions from a set with $m$ elements to a set with $n$ elements.

Let $m$ and $n$ be positive integers with $m ≥ n$. Then, there are
$$n^m − C(n, 1)(n − 1)^m + C(n, 2)(n − 2)^m − ⋯ + (−1)^{n−1}C(n, n − 1) ⋅ 1^m$$ onto functions from a set with $m$ elements to a set with $n$ elements.

$\text{Proof :}$
Let $P_i$ be the propety that $b_1$ is not in the range of the funtion, then 
$$
\begin{aligned}
  N(P'_1P'_2\cdots P'_n) 
  = &N − \sum_{1≤i≤n}N(P_i) + \sum_{1≤i<j≤n}N(P_iP_j) \\
    &- ⋯ + (−1)^{n}N(P_1 P_2 … P_n) \\
  = &n^m − C(n, 1)(n − 1)^m + C(n, 2)(n − 2)^m \\
    &− ⋯ + (−1)^{n-1}C(n, n − 1) ⋅ 1^m  \\
\end{aligned}
$$

#### Derangements
The principle of inclusion–exclusion will be used to count dearangement.
A **derangement** is a permutation of objects that leaves no object in its original position.

The number of derangements of a set with $n$ elements is
$$D_n = n!\left[ 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \cdots + (-1)^n\frac{1}{n!} \right] $$

$\text{Proof :}$
Let $P_i$ be the propety that the object $i$ is in the original position, then
$$
\begin{aligned}
  D_n 
  = &\; N(P'_1P'_2\cdots P'_n) \\
  = &\; N − \sum_{1≤i≤n}N(P_i) + \sum_{1≤i<j≤n}N(P_iP_j) \\
    &- ⋯ + (−1)^{n}N(P_1 P_2 … P_n) \\
  = &\; n! − C(n, 1)(n − 1)! + C(n, 2)(n − 2)! \\
    &− ⋯ + (-1)^nC(n, n)\cdot 0! \\
  = &\; n! - \frac{n!}{1!} + \frac{n!}{2!} - \cdots + (-1)^n\frac{n!}{n!} \\
  = &\; n!\left[ 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \cdots + (-1)^n\frac{1}{n!} \right]
\end{aligned}
$$




