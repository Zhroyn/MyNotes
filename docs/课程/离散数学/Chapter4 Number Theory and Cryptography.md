
## Number Theory and Cryptography
### 4.1 Divisibility and Modular Arithmetic
**The Division Algorithm**
Let $a$ be an integer and $d$ a positive integer. Then there are unique integers $q$ and $r$, with $0 ≤ r < d$, such that $a = dq + r$.

$d$ is called the **divisor**, $a$ is called the **dividend**,
$q$ is called the **quotient**, $r$ is called the **remainder**.

**Arithmetic Modulo m**
The operation $+_m$ is defined as $a +_m b = (a + b) \textbf{ mod } m$, which is called *addition modulo m*.
The operation $\cdot_m$ is defined as $a \cdot_m b = (a \cdot b) \textbf{ mod } m$, which is called *multiplication modulo m*.







<br>

### 4.2 Integer Representations and Algorithms
#### Representations of Integers
$
\textbf{procedure } \textit{base b expansion } (n, b: \text{positive integers with } b > 1) \\
q := n \\
k := 0 \\
\text{while } q ≠ 0 \\
\qquad a_k := q \textbf{ mod } b \\
\qquad q := q \textbf{ div } b \\
\qquad k := k + 1 \\
\text{return } (a_{k−1},… , a_1, a_0) \{(a_{k−1} … a_1a_0)_b \text{ is the base } b \text{ expansion of } n\}
$

<br>

#### Modular Exponentiation
$
\textbf{procedure } \textit{modular exponentiation } (b: \text{integer}, n = (a_{k−1}a_{k−2} … a_1a_0)_2, \\
\qquad \qquad m: \text{positive integers}) \\
x := 1 \\
power := b \textbf{ mod } m \\
\text{for } i := 0 \text{ to } k − 1 \\
\qquad \text{if } a_i = 1 \text{ then } x := (x ⋅ power) \textbf{ mod } m \\
\qquad power := (power ⋅ power) \textbf{ mod } m \\
\text{return } x \; \{x \text{ equals } b^n \textbf{ mod } m\}
$







<br>

### 4.3 Primes and Greatest Common Divisors
#### Greatest Common Divisors and Least Common Multiples
Let $a$ and $b$ be integers, not both zero. The largest integer $d$ such that $d ∣ a$ and $d ∣ b$ is called the **greatest common divisor** of $a$ and $b$, which is denoted by $\gcd(a, b)$.
$$
\gcd(a, b) = p_1^{\text{min}(a_1, b_1)} p_2^{\text{min}(a_2, b_2)} \cdots p_n^{\text{min}(a_n, b_n)}
$$

The integers $a$ and $b$ are **relatively prime** if their greatest common divisor is 1.

The **least common multiple** of the positive integers $a$ and $b$ is the smallest positive integer that is divisible by both $a$ and $b$, which is denoted by $\text{lcm}(a, b)$.
$$
\text{lcm}(a, b) = p_1^{\text{max}(a_1, b_1)} p_2^{\text{max}(a_2, b_2)} \cdots p_n^{\text{max}(a_n, b_n)}
$$

**Theorem**
Let $a$ and $b$ be positive integers. Then $$ab = \gcd(a, b) \cdot \text{lcm}(a, b)$$

<br>

#### Euclidean Algorithm
**Lemma 1**
Let $a = bq + r$, where $a$, $b$, $q$, and $r$ are integers. Then $\gcd(a, b) = \gcd(b, r)$.

$
\textbf{procedure } \textit{gcd } (a, b: \text{positive integers}) \\
x := a \\
y := b \\
\text{while } y ≠ 0 \\
\qquad r := x \textbf{ mod } y \\
\qquad x := y \\
\qquad y := r \\
\text{return } x \; \{\gcd(a, b) \text{ is } x\}
$

<br>

#### Bezout’s Theorem
If $a$ and $b$ are positive integers, then there exist integers $s$ and $t$ such that $$\gcd(a, b) = sa + tb$$

**Extended Euclidean Algorithm**
$
\textbf{procedure } \textit{exgcd } (a, b: \text{positive integers}) \\
s_{j-2} := 1 \\
s_{j-1} := 0 \\
t_{j-2} := 0 \\
t_{j-1} := 1 \\
\text{while } y ≠ 0 \\
\qquad q := x \textbf{ div } y \\
\qquad r := x \textbf{ mod } y \\
\qquad s_{j} := s_{j-2} - qs_{j-1};
\quad s_{j-2} = s_{j-1};
\quad s_{j-1} = s_{j} \\
\qquad t_{j} := t_{j-2} - qt_{j-1};
\quad t_{j-2} = t_{j-1};
\quad t_{j-1} = t_{j} \\
\qquad x := y \\
\qquad y := r \\
\text{return } x, s_j, t_j \; \{\gcd(a, b) = x = s_ja + t_jb \}
$

> Express $\gcd(252, 198) = 18$ as a linear combination of $252$ and $198$.
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

<br>

#### Uniqueness of Prime Factorization
**Lemma 2**
If $a, b, c$ are positive integers such that $\gcd(a, b) = 1$ and $a ∣ bc$, then $a ∣ c$.
$\texttt{Proof:}$
By Bezout's Theorem, $$sa + tb = 1 \\ \Rightarrow sac + tbc = c$$

Because $a | sac$ and $a | tbc$, we can conclude that $a|c$.

**Lemma 3**
If $p$ is a prime and $p ∣ a_1a_2 ⋯ a_n$, where each $a_i$ is an integer, then $p ∣ a_i$ for some $i$.

$\texttt{Proof (of the uniqueness of prime factorization):}$
Suppose that the positive integer $n$ can be written as the product of primes in two different ways, say, $$n = p_1p_2 ⋯ p_s = q_1q_2 ⋯ q_t$$

where each $p_i$ and $q_j$ is prime such that $$p_1 ≤ p_2 ≤ ⋯ ≤ p_s, q_1 ≤ q_2 ≤ ⋯ ≤ q_t$$

After we remove all common primes from the two factorizations, we have
$$p_{i_1}p_{i_2} ⋯ p_{i_u} = q_{j_1}q_{j_2} ⋯ q_{j_v}$$

where no prime occurs on both sides of this equation and $u$ and $v$ are positive integers.

By Lemma 3, it follows that $p_{i_1}$ divides $q_{j_k}$ for some $k$. Because no prime divides another prime, this is impossible.
Consequently, there can be at most one factorization of $n$ into primes in nondecreasing order.

**Theorem**
Let $m$ be a positive integer and let $a$, $b$, and $c$ be integers. If $ac ≡ bc (\text{mod } m)$ and $\gcd(c, m) = 1$, then $a ≡ b (\text{mod } m)$.









<br>

### 4.4 Solving Congruences
#### Linear Congruences
**Definition**
A congruence of the form $$ax ≡ b (\text{mod } m)$$ where $m$ is a positive integer, $a$ and $b$ are integers, and $x$ is a variable, is called a **linear congruence**.

An integer $\bar{a}$ such that $\bar{a}a ≡ 1 (\text{mod } m)$ is said to be an **inverse** of $a$ modulo $m$.

**Theorem 1**
If $a$ and $m$ are relatively prime integers and $m > 1$, then there is a unique positive integer $\bar a$ less than $m$ that is an inverse of $a$ modulo $m$, and every other inverse of $a$ modulo $m$ is congruent to $\bar a$ modulo $m$.

<br>

#### Solving Linear Congruences
When $\gcd(a, m) = 1$, the procedures to get the solution of $ax \equiv b (\text{mod } m)$ are:
1. Use the Euclidean algorithm to find that $\gcd(a, m) = 1$
2. Find the Bezout coefficients for $a$ and $m$ by working backwards through these step, say, $sa + tm = 1$, then we can get $\bar a = s$
3. Multiply both sides by $\bar a$, then we can get $x \equiv \bar ab(\text{mod } m)$
4. Determine whether every $x$ with $x \equiv \bar ab(\text{mod } m)$ is a solution

When $\gcd(a, m) \neq 1$ and $\gcd(a, m) \not| \; b$, the linear congruence $ax \equiv b (\text{mod } m)$ has no solution.

When $\gcd(a, m) \neq 1$ and $\gcd(a, m) \; | \; b$, then the solution of $ax \equiv b (\text{mod } m)$ is equal to $a'x \equiv b' (\text{mod } m')$, where $a' = \frac{a}{\gcd(a, m)}, b' = \frac{b}{\gcd(a, m)}, m' = \frac{m}{\gcd(a, m)}$.

<br>

#### The Chinese Remainder Theorem
Let $m_1, m_2, … , m_n$ be pairwise relatively prime positive integers greater than one and $a_1, a_2, … , a_n$ arbitrary integers. Then the system
$$
x \equiv a_1 (\text{mod } m_1) \\
x \equiv a_2 (\text{mod } m_2) \\
\cdots \\
x \equiv a_n (\text{mod } m_n) \\
$$ 

has a unique solution modulo $m = m_1m_2 ⋯ m_n$.
Let $M_k = m/m_k$, and $M^{-1}_k$ an inverse of $M_k$ modulo $m_k$, then one solution of the system of linear congruences is $\sum_{i=1}^{n} a_iM_iM^{-1}_i$.

<br>

#### Back Substitution
> Use the method of back substitution to find all integers $x$ such that $x\equiv 1(\text{mod } 5)$, $x\equiv 2(\text{mod } 6)$ and $x\equiv 3(\text{mod } 7)$.
>
> By the first congruence, get $x= 5t + 1$, where $t$ is an integer. 
> Substituting $x = 5t + 1$ into the second congruence, get $5t + 1 \equiv 2 (\text{mod } 6)$.
> $\Rightarrow 5t + 1 + 4= 2 + 4(\text{mod } 6) \Rightarrow 5(t + 1) = 0 (\text{mod } 6)$. 
> 
> So that $t \equiv 5 (\text{mod } 6)$, get $t= 6u + 5$, where $u$ is an integer. 
> Substituting this back into $x = 5t + 1$, get $x = 30u+26$.
> 
> Substituting $x = 30u + 26$ into the third congruence, get $30u + 26 \equiv 3 (\text{mod } 7)$.
> $\Rightarrow 30u + 26 + 4 \equiv 3 + 4(\text{mod } 7) \Rightarrow 30(u + 1) \equiv 0(\text{mod } 7)$
> 
> So that $u \equiv 6(\text{mod } 7)$, get $u = 7v + 6$, where $v$ is an integer. 
> Substituting this back into $x = 30u + 26$, get $x = 210v + 206$.
>
> So the solution is $x$ with $x \equiv 206 (\text{mod } 210)$

<br>

#### Fermat’s Little Theorem
If $p$ is prime and $a$ is an integer not divisible by $p$, then $a^{p−1} ≡ 1 (\text{mod } p)$.
Furthermore, for every integer $a$ we have $a^{p} ≡ a (\text{mod } p)$

<br>

#### Pseudoprimes
**Definition 1**
Let $b$ be a positive integer. If $n$ is a composite positive integer, and $b^{n−1} ≡ 1 (\text{mod } n)$, then $n$ is called a **pseudoprime to the base $b$**.

**Definition 2**
A composite integer $n$ that satisfies the congruence $b^{n−1} ≡ 1 (\text{mod } n)$ for all positive integers $b$ with $\gcd(b, n) = 1$ is called a **Carmichael number**.

<br>

#### Primitive Roots and Discrete Logarithms
**Definition 3**
A **primitive root** modulo a prime $p$ is an integer $r$ in $Z_p$ such that every nonzero element of $Z_p$ is a power of $r$.
There is a primitive root modulo $p$ for every prime $p$.

**Definition 4**
Suppose that $p$ is a prime, $r$ is a primitive root modulo $p$, and $a$ is an integer between $1$ and $p − 1$ inclusive. If $r^e \textbf{ mod } p = a$ and $0 ≤ e ≤ p − 1$, we say that $e$ is the **discrete logarithm** of a modulo $p$ to the base $r$ and we write $\log_r a = e$.




