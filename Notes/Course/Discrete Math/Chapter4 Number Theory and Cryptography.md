<!-- TOC -->

- [Number Theory and Cryptography](#number-theory-and-cryptography)
  - [4.1 Divisibility and Modular Arithmetic](#41-divisibility-and-modular-arithmetic)
  - [4.2 Integer Representations and Algorithms](#42-integer-representations-and-algorithms)
    - [Representations of Integers](#representations-of-integers)
    - [Modular Exponentiation](#modular-exponentiation)

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




