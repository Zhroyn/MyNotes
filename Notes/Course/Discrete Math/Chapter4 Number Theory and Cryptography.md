<!-- TOC -->

- [Number Theory and Cryptography](#number-theory-and-cryptography)
  - [4.1 Divisibility and Modular Arithmetic](#41-divisibility-and-modular-arithmetic)
  - [4.2 Integer Representations and Algorithms](#42-integer-representations-and-algorithms)
    - [Representations of Integers](#representations-of-integers)
    - [Modular Exponentiation](#modular-exponentiation)
  - [4.3 Primes and Greatest Common Divisors](#43-primes-and-greatest-common-divisors)
    - [Greatest Common Divisors and Least Common Multiples](#greatest-common-divisors-and-least-common-multiples)
    - [Euclidean Algorithm](#euclidean-algorithm)
    - [Bezout’s Theorem](#bezouts-theorem)
    - [Uniqueness of Prime Factorization](#uniqueness-of-prime-factorization)

<!-- /TOC -->





## Number Theory and Cryptography
### 4.1 Divisibility and Modular Arithmetic
**The Division Algorithm**
Let $a$ be an integer and $d$ a positive integer. Then there are unique integers $q$ and $r$, with $0 ≤ r < d$, such that $a = dq + r$.

$d$ is called the **divisor**, $a$ is called the **dividend**,
$q$ is called the **quotient**, $r$ is called the **remainder**.

**Arithmetic Modulo m**
The operation $+_m$ is defined as $a +_m b = (a + b) \textbf{ mod } m$, which is called *addition modulo m*.
The operation $\cdot_m$ is defined as $a \cdot_m b = (a \cdot b) \textbf{ mod } m$, which is called *multiplication modulo m*.






### 4.2 Integer Representations and Algorithms
#### Representations of Integers
$
\text{procedure } \textit{base b expansion } (n, b: \text{positive integers with } b > 1) \\
q := n \\
k := 0 \\
\text{while } q ≠ 0 \\
\quad a_k := q \textbf{ mod } b \\
\quad q := q \textbf{ div } b \\
\quad k := k + 1 \\
\text{return } (a_{k−1},… , a_1, a_0) \{(a_{k−1} … a_1a_0)_b \text{ is the base } b \text{ expansion of } n\}
$

#### Modular Exponentiation
$
\text{procedure } \textit{modular exponentiation } (b: \text{integer}, n = (a_{k−1}a_{k−2} … a_1a_0)_2, \\
\qquad \qquad m: \text{xpositive integers}) \\
x := 1 \\
power := b \textbf{ mod } m \\
\text{for } i := 0 \text{ to } k − 1 \\
\quad \text{if } a_i = 1 \text{ then } x := (x ⋅ power) \textbf{ mod } m \\
\quad power := (power ⋅ power) \textbf{ mod } m \\
\text{return } x \{x \text{ equals } b^n \textbf{ mod } m\}
$





### 4.3 Primes and Greatest Common Divisors
#### Greatest Common Divisors and Least Common Multiples
Let $a$ and $b$ be integers, not both zero. The largest integer $d$ such that $d ∣ a$ and $d ∣ b$ is called the **greatest common divisor** of $a$ and $b$, which is denoted by $\text{gcd}(a, b)$.
$$
\text{gcd}(a, b) = p_1^{\text{min}(a_1, b_1)} p_2^{\text{min}(a_2, b_2)} \cdots p_n^{\text{min}(a_n, b_n)}
$$

The integers $a$ and $b$ are **relatively prime** if their greatest common divisor is 1

The **least common multiple** of the positive integers $a$ and $b$ is the smallest positive integer that is divisible by both $a$ and $b$, which is denoted by $\text{lcm}(a, b)$.
$$
\text{lcm}(a, b) = p_1^{\text{max}(a_1, b_1)} p_2^{\text{max}(a_2, b_2)} \cdots p_n^{\text{max}(a_n, b_n)}
$$

**Theorem**
Let $a$ and $b$ be positive integers. Then $$ab = \text{gcd}(a, b) \cdot \text{lcm}(a, b)$$


#### Euclidean Algorithm
**Lemma 1**
Let $a = bq + r$, where $a$, $b$, $q$, and $r$ are integers. Then $\text{gcd}(a, b) = \text{gcd}(b, r)$.

$
\text{procedure } \textit{gcd } (a, b: \text{positive integers}) \\
x := a \\
y := b \\
\text{while } y ≠ 0 \\
\quad r := x \textbf{ mod } y \\
\quad x := y \\
\quad y := r \\
\text{return } x \{\text{gcd}(a, b) \text{ is } x\}
$

#### Bezout’s Theorem
If $a$ and $b$ are positive integers, then there exist integers $s$ and $t$ such that $$\text{gcd}(a, b) = sa + tb$$

**Extended Euclidean Algorithm**
$
\text{procedure } \textit{exgcd } (a, b: \text{positive integers}) \\
s_{j-2} := 1 \\
s_{j-1} := 0 \\
t_{j-2} := 0 \\
t_{j-1} := 1 \\
\text{while } y ≠ 0 \\
\quad q := x \textbf{ div } y \\
\quad s_{j} := s_{j-2} - qs_{j-1};
\quad s_{j-2} = s_{j-1};
\quad s_{j-1} = s_{j} \\
\quad t_{j} := t_{j-2} - qt_{j-1};
\quad t_{j-2} = t_{j-1};
\quad t_{j-1} = t_{j} \\
\quad x := y \\
\quad y := r \\
\text{return } x, s_j, t_j \{\text{gcd}(a, b) = x = s_ja + t_jb \}
$

> Express $\text{gcd}(252, 198) = 18$ as a linear combination of $252$ and $198$.
> **Solution1:** Working backwards through the steps of the Euclidean algorithm
> $252 = 198\cdot 1 + 54 \Rightarrow 54 = 252 - 1\cdot 198$
> $198 = 54\cdot 3 + 36 \Rightarrow 36 = 198 - 3\cdot 54$
> $54 = 36\cdot 1 + 18 \Rightarrow 18 = 54 - 1\cdot 36$
> $36 = 18\cdot 2 + 0$
> Therefore, we can get
> $$\begin{aligned} 18 &= 4\cdot 54 - 198 \\ &= 4\cdot 252 - 5\cdot 198 \end{aligned}$$
>
> **Solution2:** Using extended euclidean algorithm
> From above, we know that $q_1 = 1, q_2 = 3, q_3 = 1, q_4 = 2$
> So
> $$s_2 = 1 - 0\cdot 1 = 1, t_2 = 0 - 1\cdot 1 = -1 \\ s_3 = 0 - 1\cdot 3 = -3, t_3 = 1 - (-1)\cdot 3 = 4 \\ s_4 = 1 - (-3)\cdot 1 = 4, t_4 = -1 - 4\cdot 1 = -5 $$

#### Uniqueness of Prime Factorization
**Lemma 2**
If $a$, $b$, and $c$ are positive integers such that $\text{gcd}(a, b) = 1$ and $a ∣ bc$, then $a ∣ c$.
$\text{Proof:}$
By Bezout's Theorem, $$sa + tb = 1 \\ \Rightarrow sac + tbc = c$$

Because $a | sac$ and $a | tbc$, we can conclude that $a|c$.

**Lemma 3**
If $p$ is a prime and $p ∣ a_1a_2 ⋯ a_n$, where each $a_i$ is an integer, then $p ∣ a_i$ for some $i$.

$\text{Proof (of the uniqueness of the prime factorization of a positive integer):}$
Suppose that the positive integer $n$ can be written as the product of primes in two different ways, say, $$n = p_1p_2 ⋯ p_s = q_1q_2 ⋯ q_t$$, where each $p_i$ and $q_j$ is prime such that $$p_1 ≤ p_2 ≤ ⋯ ≤ p_s, q_1 ≤ q_2 ≤ ⋯ ≤ q_t$$

When we remove all common primes from the two factorizations, we have
$$p_{i_1}p_{i_2} ⋯ p_{i_u} = q_{j_1}q_{j_2} ⋯ q_{j_v}$$,where no prime occurs on both sides of this equation and $u$ and $v$ are positive integers. 
By Lemma 3, it follows that $p_{i_1}$ divides $q_{j_k}$ for some $k$. 
Because no prime divides another prime, this is impossible.  Consequently, there can be at most one factorization of $n$ into primes in nondecreasing order.

**Theorem**
Let $m$ be a positive integer and let $a$, $b$, and $c$ be integers. If $ac ≡ bc (\text{mod } m)$ and $\text{gcd}(c, m) = 1$, then $a ≡ b (\text{mod } m)$.


