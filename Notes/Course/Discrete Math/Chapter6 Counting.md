<!-- TOC -->

- [Counting](#counting)
  - [6.1 The Basics of Counting](#61-the-basics-of-counting)
  - [6.2 The Pigeonhole Principle](#62-the-pigeonhole-principle)
  - [6.3 Permutations and Combinations](#63-permutations-and-combinations)
  - [6.4 Binomial Coefficients and Identities](#64-binomial-coefficients-and-identities)
  - [6.5 Generalized Permutations and Combinations](#65-generalized-permutations-and-combinations)
  - [6.6 Generating Permutations and Combinations](#66-generating-permutations-and-combinations)

<!-- /TOC -->





## Counting
### 6.1 The Basics of Counting
- **THE PRODUCT RULE** : Suppose that a procedure can be broken down into a sequence of two tasks. If there are $n_1$ ways to do the first task, and for each of these ways of doing the first task, there are $n_2$ ways to do the second task, then there are $n_1n_2$ ways to do the procedure
- **THE SUM RULE** : If a task can be done either in one of $n_1$ ways or in one of $n_2$ ways, where none of the set of $n_1$ ways is the same as any of the set of $n_2$ ways, then there are $n_1 + n_2$ ways to do the task
- **THE SUBTRACTION RULE** : If a task can be done in either $n_1$ ways or $n_2$ ways, then the number of ways to do the task is $n_1 + n_2$ minus the number of ways to do the task that are common to the two different ways. The subtraction rule is also known as the **principle of inclusion–exclusion**
- **THE DIVISION RULE** : There are $n∕d$ ways to do a task if it can be done using a procedure that can be carried out in $n$ ways, and for every way $w$, exactly $d$ of the $n$ ways correspond to way $w$


### 6.2 The Pigeonhole Principle
- **THE PIGEONHOLE PRINCIPLE** : If $k$ is a positive integer and $k + 1$ or more objects are placed into $k$ boxes, then there is at least one box containing two or more of the objects
- The pigeonhole principle is also called the **Dirichlet drawer principle**
- **THE GENERALIZED PIGEONHOLE PRINCIPLE** If $N$ objects are placed into $k$ boxes, then there is at least one box containing at least $⌈N∕k⌉$ objects. Proof:
  - Suppose that none of the boxes contains more than $⌈N∕k⌉ − 1$ objects. Then, the total number of objects is at most $k(⌈N/k⌉ − 1) < k ((N/k + 1) − 1) = N$
  - Thus, the total number of objects is less than $N$. This completes the proof by contraposition


### 6.3 Permutations and Combinations
- An ordered arrangement of $r$ elements of a set is called an **r-permutation**. If $n$ is a positive integer and $r$ is an integer with $1 ≤ r ≤ n$, then there are $\displaystyle P(n, r) = n(n − 1)(n − 2) ⋯ (n − r + 1) = \frac{n!}{(n-r)!}$
- An **r-combination** of elements of a set is an unordered selection of r elements from the set. Thus, $\displaystyle C(n, r) = \frac{n!}{r!(n-r)!}$. $C(n, r)$ is also denoted by $\begin{pmatrix} n \\ r \end{pmatrix}$ and is called a **binomial coefficient**
<br>

- A **combinatorial proof** of an identity is a proof that uses counting arguments to prove that both sides of the identity count the same objects but in different ways or a proof that is based on showing that there is a bijection between the sets of objects counted by the two sides of the identity. These two types of proofs are called **double counting proofs** and **bijective proofs**, respectively


### 6.4 Binomial Coefficients and Identities
- $\displaystyle (x+y)^n = \sum_{j=0}^n \begin{pmatrix} n \\ j \end{pmatrix}x^{n-j}y^j $
- $\displaystyle \sum_{k=0}^n \begin{pmatrix} n \\ k \end{pmatrix} = 2^n $
- $\displaystyle \sum_{k=0}^n (-1)^k\begin{pmatrix} n \\ k \end{pmatrix} = 0 $
- $\displaystyle \sum_{k=0}^n 2^k\begin{pmatrix} n \\ k \end{pmatrix} = 3^n $
- Pascal’s Identity : $\displaystyle \begin{pmatrix} n+1 \\ k \end{pmatrix} = \begin{pmatrix} n \\ k-1 \end{pmatrix} + \begin{pmatrix} n \\ k \end{pmatrix}$
- Vandermonde’s Identity : $\displaystyle \begin{pmatrix} m+n \\ r \end{pmatrix} = \sum_{k=0}^r \begin{pmatrix} m \\ r-k \end{pmatrix} \begin{pmatrix} n \\ k \end{pmatrix}$
  - $\displaystyle \begin{pmatrix} 2n \\ n \end{pmatrix} = \sum_{k=0}^n \begin{pmatrix} n \\ k \end{pmatrix}^2$
- $\displaystyle \begin{pmatrix} n+1 \\ r+1 \end{pmatrix} = \sum_{j=r}^n \begin{pmatrix} j \\ r \end{pmatrix}$


### 6.5 Generalized Permutations and Combinations
- **Permutations with Repetition** : The number of r-permutations of a set of $n$ objects with repetition allowed is $n^r$
- **Combinations with Repetition** : There are $C(n + r − 1, r) = C(n + r − 1, n − 1)$ r-combinations from a set with $n$ elements when repetition of elements is allowed.
- **Permutations with Indistinguishable Objects** : The number of different permutations of $n$ objects, where there are $n_1$ indistinguishable objects of type 1, $n_2$ indistinguishable objects of type 2, … , and $n_k$ indistinguishable objects of
type k, is $\displaystyle \frac{n!}{n_1! n_2! ⋯ n_k!}$
- **Distributing Objects into Boxes**
  - **Distinguishable Objects and Distinguishable Boxes** : The number of ways to distribute $n$ distinguishable objects into $k$ distinguishable boxes so that $n_i$ objects are placed into box $i$, $i = 1, 2, … , k$, equals $\displaystyle \frac{n!}{n_1! n_2! ⋯ n_k!}$
  - **Indistinguishable Objects and Distinguishable Boxes** : There are $C(n + r − 1, n − 1)$ ways to place $r$ indistinguishable objects into $n$ distinguishable boxes
  - **Distinguishable Objects and Indistinguishable Boxes**
    - Let $S(n, j)$ denote the number of ways to distribute $n$ distinguishable objects into $j$ indistinguishable boxes so that no box is empty. The numbers $S(n, j)$ are called **Stirling numbers of the second kind**.
    - It can be shown that $\displaystyle S(n, j) = \frac{1}{j!}\sum_{i=0}^{j-1} (-1)^i\begin{pmatrix} j \\ i \end{pmatrix} (j-i)^n $
    - So the number of ways to distribute $n$ distinguishable objects into $k$ indistinguishable boxes equals $\displaystyle \sum_{j=1}^k S(n, j) = \sum_{j=1}^k\frac{1}{j!}\sum_{i=0}^{j-1} (-1)^i\begin{pmatrix} j \\ i \end{pmatrix} (j-i)^n $
  - **Indistinguishable Objects and Indistinguishable Boxes** : No simple closed formula exists for this number.



### 6.6 Generating Permutations and Combinations
- A general method can be described for producing the next larger permutation in increasing order following a given permutation $a_1a_2 ⋯ a_n$:
  - First, find the integers $a_j$ and $a_{j+1}$ with $a_{j} < a_{j+1}$ and $a_{j+1} > a_{j+2} > ⋯ > a_{n}$, that is, the last pair of adjacent integers in the permutation where the first integer in the pair is smaller than the second.
  - Then, the next larger permutation in lexicographic order is obtained by putting in the $j$th position the least integer among $a_{j+1}, a_{j+2}, ⋯, a_{n}$ that is greater than $a_j$, and then listing in increasing order the rest of the integers $a_j, a_{j+1}, ⋯, a_{n}$ in positions $j + 1$ to $n$.
-  The next r-combination after $a_1a_2 ⋯ a_r$ can be obtained in the following way:
   - First, locate the last element $a_i$ in the sequence such that $a_i ≠ n − r + i$.
   - Then, replace $a_i$ with $a_i + 1$ and $a_j$ with $a_i + j − i + 1$, for $j = i + 1, i + 2, … , r$.






