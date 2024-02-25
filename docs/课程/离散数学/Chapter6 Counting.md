
- [Counting](#counting)
    - [6.2 The Pigeonhole Principle](#62-the-pigeonhole-principle)
        - [The Pigeonhole Principle](#the-pigeonhole-principle)
        - [The Generalized Pigeonhole Principle](#the-generalized-pigeonhole-principle)
        - [Examples](#examples)
    - [6.3 Permutations and Combinations](#63-permutations-and-combinations)
        - [Permutations](#permutations)
        - [Combinations](#combinations)
        - [Combinatorial Proofs](#combinatorial-proofs)
    - [6.4 Binomial Coefficients and Identities](#64-binomial-coefficients-and-identities)
    - [6.5 Generalized Permutations and Combinations](#65-generalized-permutations-and-combinations)
        - [Permutations with Repetition](#permutations-with-repetition)
        - [Combinations with Repetition](#combinations-with-repetition)
        - [Permutations with Indistinguishable Objects](#permutations-with-indistinguishable-objects)
        - [Distributing Objects into Boxes](#distributing-objects-into-boxes)
    - [6.6 Generating Permutations and Combinations](#66-generating-permutations-and-combinations)
        - [Generating Permutations](#generating-permutations)
        - [Generating Combinations](#generating-combinations)









## Counting
### 6.2 The Pigeonhole Principle
#### The Pigeonhole Principle
If $k$ is a positive integer and $k + 1$ or more objects are placed into $k$ boxes, then there is at least one box containing two or more of the objects.
It is also called the **Dirichlet Drawer Principle**.

<br>

#### The Generalized Pigeonhole Principle
If $N$ objects are placed into $k$ boxes, then there is at least one box containing at least $⌈N/k⌉$ objects.

$\texttt{Proof:}$
Suppose that none of the boxes contains more than $⌈N/k⌉ − 1$ objects. Then, the total number of objects is at most $k(⌈N/k⌉ − 1) < k (N/k + 1 − 1) = N$
Thus, the total number of objects is less than $N$. This completes the proof by contraposition

<br>

#### Examples
> Show that in a party of 2 or more people, there are 2 people with the same number of friends in the party. (Assuming you can’t be your own friend and that friendship is mutual.)

> Show that among any $n+1$ positive integers not exceeding $2n$, there must be an integer that divides one of the other integers.

> During 11 weeks football games will be held at least 1 game a day, but at most 12 games be arranged each week. Show that there must be a period of some number of consecutive days during which exactly 21 games must be played.
> 
> $\texttt{Proof:}$
> Let $x_i$ be the number of football games held on the $i$th day, and set $a_i = \sum_{k=1}^i x_i, b_i = a_i + 21$.
> Then we can get $$1\le a_1 \lt \cdots \lt a_{77} \le 12\times 11 = 132 \\ 22\le b_1 \lt \cdots \lt b_{77} \le 132 + 21 = 153 $$
>
> So $$22\le a_{22} \lt \cdots \lt a_{77} \le 132 \\ 22\le b_1 \lt \cdots \lt b_{56} \le 132 $$
> 
> Set $A = \{a_{22},\cdots, a_{77},c_1,\cdots, b_{56}\}, B = \{22, 23, \cdots, 132 \} $.
> Because $|A| = 112 > 111 = |B|$, by the pigeonhole principle, we can get $\exists i\neq j, a_i = c_j$, and thus $x_{j+1} + x_{j+2} + \cdots + x_i = 21 $.
>
> Moreover, set $c_i = a_i + n$, then $|A| = 154 - 2n, |B| = 132 - n$. So when $n \le 21$, there must be a period of some number of consecutive days during which exactly $n$ games must be played.

> Assume that in a group of six people, each pair of individuals are either friends or enemies. Show that there are either three mutual friends or three mutual enemies in the group.
> 
> $\texttt{Proof:}$
> Let the six people be $a_1, a_2, a_3, a_4, a_5, a_6$, then take $a_1$ into consideration.
> By the generalized pigeonhole principle, $a_1$ has either at least three friends or at least three enemies. Let's suppose it's the former case, that is, suppose that $a_i, a_j, a_k$ are friends of $a_1$.
> Then if $a_i, a_j, a_k$ are three mutual enemies, the proof is completed; if two of them are friends, then these two people with $a_1$ are three mutual friends. This completes the proof.
>
> The Ramsey number $R(m,n)$, where $m \ge 2$ and $n \ge 2$, denotes the minimum number of people at a party so that there are either $m$ mutual friends or $n$ mutual enemies.
> As this example demonstrates, $R(3, 3) = 6$.








<br>

### 6.3 Permutations and Combinations
#### Permutations
$$
P(n, r) = n(n − 1)(n − 2) ⋯ (n − r + 1) = \frac{n!}{(n-r)!} \\~\\
P(n, 0) = 1, \quad
P(n, n) = P(n, n-1) = n!
$$

<br>

#### Combinations
$$C(n, r) = \begin{pmatrix} n \\ r \end{pmatrix} = \frac{n(n − 1)(n − 2) ⋯ (n − r + 1)}{r!} = \frac{n!}{r!(n-r)!}$$

By definition, there are
$$
\begin{aligned}
  \begin{pmatrix} -n \\ r \end{pmatrix}
  &= \frac{(-n)(-n-1)\cdots (-n-r+1)}{r!} \\
  &= \frac{(-1)^r n(n+1)\cdots (n+r-1)}{r!} \\
  &= \frac{(-1)^r (n+r-1)!}{r!(n-1)!} \\
  &= (-1)^r \begin{pmatrix} n+r-1 \\ r \end{pmatrix} \\
\end{aligned}
$$

<br>

#### Combinatorial Proofs
A **combinatorial proof** of an identity is a proof that  uses one of double counting proof or bijective proofs.

- A **double counting proof** uses counting arguments to prove that both sides of an identity count the same objects, but in different ways.
- A **bijective proof** shows that there is a bijection between the sets of objects counted by the two sides of the identity.








<br>

### 6.4 Binomial Coefficients and Identities
**Theorem 1: The Binomial Theorem**
$$(x+y)^n = \sum_{j=0}^n \begin{pmatrix} n \\ j \end{pmatrix}x^{n-j}y^j $$

**Theorem 2: Pascal’s Identity**
$$\begin{pmatrix} n+1 \\ k \end{pmatrix} = \begin{pmatrix} n \\ k-1 \end{pmatrix} + \begin{pmatrix} n \\ k \end{pmatrix}$$

**Theorem 3: Vandermonde’s Identity**
$$\begin{pmatrix} m+n \\ r \end{pmatrix} = \sum_{k=0}^r \begin{pmatrix} m \\ r-k \end{pmatrix} \begin{pmatrix} n \\ k \end{pmatrix}$$

$\texttt{Double Counting Proof:}$
Let $A$ and $B$ be two disjoint sets with $|A|=m, |B|=n$, then $C(m + n，r)$ is the number of ways to pick $r$ elements from $A \cup B$.
Another way to pick $r$ elements from $A \cup B$ is to firstly pick $r-k$ elements from $A$, and then $k$ elements from $B$, where $0\le k\le r$, which can be done in $C(m，r-k) C(n，r)$ ways.
So both sides of the equation count the same objects.

**Corollary**
$$\begin{pmatrix} 2n \\ n \end{pmatrix} = \sum_{k=0}^n \begin{pmatrix} n \\ k \end{pmatrix}^2$$

**Other Identities**
$$\begin{pmatrix} n+1 \\ r+1 \end{pmatrix} = \sum_{j=r}^n \begin{pmatrix} j \\ r \end{pmatrix}$$








<br>

### 6.5 Generalized Permutations and Combinations
#### Permutations with Repetition
The number of r-permutations of a set of $n$ objects with repetition allowed is $n^r$.

<br>

#### Combinations with Repetition
The number of r-combinations from a set with $n$ elements with repetition allowed is 
$$C(n + r − 1, r) = C(n + r − 1, n − 1)$$

$\texttt{Proof:}$
Just think about choosing $r$ stars or $n - 1$ bars from $n + r - 1$ cells. The bars will split stars into $n$ parts.

<br>

#### Permutations with Indistinguishable Objects
The number of different permutations of $n$ objects, where there are $n_1$ indistinguishable objects of type $1$, $n_2$ indistinguishable objects of type $2$, … , and $n_k$ indistinguishable objects of type $k$, is 
$$\frac{n!}{n_1! n_2! ⋯ n_k!}$$

<br>

#### Distributing Objects into Boxes
**Distinguishable Objects and Distinguishable Boxes**
The number of ways to distribute $n$ distinguishable objects into $k$ distinguishable boxes, so that $n_i$ objects are placed into box $i$, $i = 1, 2, … , k$, is equal to
$$\frac{n!}{n_1! n_2! ⋯ n_k!}$$

<br>

**Indistinguishable Objects and Distinguishable Boxes**
The number of ways to distribute $r$ indistinguishable objects into $n$ distinguishable boxes is equal to
$$C(n + r − 1, r) = C(n + r − 1, n − 1)$$

<br>

**Distinguishable Objects and Indistinguishable Boxes**
Let $S(n, j)$ denote the number of ways to distribute $n$ distinguishable objects into $j$ indistinguishable boxes so that no box is empty. The numbers $S(n, j)$ are called **Stirling numbers of the second kind**.
It can be shown that
$$
S(n, j) = \frac{1}{j!}
\sum_{i=0}^{j-1} (-1)^i
\begin{pmatrix} j \\ i \end{pmatrix}
(j-i)^n
$$

So the number of ways to distribute $n$ distinguishable objects into $k$ indistinguishable boxes equals
$$
\sum_{j=1}^k S(n, j) = \sum_{j=1}^k\frac{1}{j!}
\sum_{i=0}^{j-1} (-1)^i
\begin{pmatrix} j \\ i \end{pmatrix}
(j-i)^n 
$$

<br>

**Indistinguishable Objects and Indistinguishable Boxes**
No simple closed formula exists for this number.








<br>

### 6.6 Generating Permutations and Combinations
#### Generating Permutations
In the **lexicographic** (or **dictionary**) **ordering** of the set of permutations of $\{1, 2, 3, … , n\}$, the permutation $a_1a_2 ⋯ a_n$ precedes the permutation of $b_1b_2 ⋯ b_n$, if for some $k$, with $1 ≤ k ≤ n, a_1 = 1, a_2 = b_2, … , a_{k−1} = b_{k−1}$, and $a_k < b_k$.

The procedures to generate the next permutation in lexicographic order after $a_1a_2 ⋯ a_n$ are:
1. Find $j$ such that $a_{j} < a_{j+1}$ and $a_{j+1} > a_{j+2} > ⋯ > a_{n}$
2. Put in the $j$th position the least integer among $a_{j+1}, a_{j+2}, ⋯, a_{n}$ that is greater than $a_j$
3. List in increasing order the rest of the integers $a_j, a_{j+1}, ⋯, a_{n}$ in positions $j + 1$ to $n$.

> The next larger permutation in lexicographic order after $124653$ is $125346$.

<br>

#### Generating Combinations
We can represent a combination by a bit string, and the procedure to generate the next larger bit string is simply adding by 1.

For all r-combinations of the set $\{1, 2, \cdots, n \}$, the procedures to generate the next r-combination in lexicographic order after $\{a_1, a_2, \cdots, a_r\}$ are:
1. Locate the last element $a_i$ in the sequence such that $a_i ≠ n − r + i$
2. Replace $a_i$ with $a_i + 1$ and $a_j$ with $a_i + j − i + 1$, for $j = i + 1, i + 2, … , r$.

> The next larger 4-combination of the set $\{1,2,3,4,5,6\}$ after $\{1,2,5,6\}$ is $\{1,3,4,5\}$.
> 
> The next larger 6-combination of the set $\{1,2,3,4,5,6,7,8,9,10\}$ after $\{2,3,5,6,9,10\}$ is $\{2,3,5,7,8,9\}$.






