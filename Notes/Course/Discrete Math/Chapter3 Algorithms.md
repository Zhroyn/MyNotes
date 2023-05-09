<!-- TOC -->

- [Algorithms](#algorithms)
  - [3.1 Algorithms](#31-algorithms)
  - [3.2 The Growth of Functions](#32-the-growth-of-functions)
  - [3.3 Complexity of Algorithms](#33-complexity-of-algorithms)

<!-- /TOC -->





## Algorithms
### 3.1 Algorithms
- Algorithms that make what seems to be the best choice at each step are called **greedy algorithms**
<br>

- $Input$. An algorithm has input values from a specified set.
- $Output$. From each set of input values an algorithm produces output values from a specified set. The output values are the solution to the problem.
- $Definiteness$. The steps of an algorithm must be defined precisely.
- $Correctness$. An algorithm should produce the correct output values for each set of input values.
- $Finiteness$. An algorithm should produce the desired output after a finite (but perhaps large) number of steps for any input in the set.
- $Effectiveness$. It must be possible to perform each step of an algorithm exactly and in a finite amount of time.
- $Generality$. The procedure should be applicable for all problems of the desired form, not just for a particular set of input values.

### 3.2 The Growth of Functions
- We say that $f(x)$ is $O(g(x))$ if there are constants $C$ and $k$ such that $|f(x)| ≤ C|g(x)|$ whenever $x > k$. This is read as "$f(x)$ is big-oh of $g(x)$." The constants $C$ and $k$ in the definition of big-O notation are called **witnesses** to the relationship $f(x)$ is $O(g(x))$.
- We say that $f(x)$ is $Ω(g(x))$ if there are constants $C$ and $k$ such that $|f(x)| ≥ C|g(x)|$ whenever $x > k$. This is read as "$f(x)$ is big-Omega of $g(x)$."
- We say that $f(x)$ is $Θ(g(x))$ if $f(x)$ is $O(g(x))$ and $f(x)$ is $Ω(g(x))$. When $f(x)$ is $Θ(g(x))$, we say that $f(x)$ is big-Theta of $g(x)$, that $f(x)$ is of order $g(x)$, and that $f(x)$ and $g(x)$ are of the same order.
<br>

- Suppose that $f_1(x)$ is $O(g_1(x))$ and that $f_2(x)$ is $O(g_2(x))$. Then $(f_1 + f_2)(x)$ is $O(g(x))$, where $g(x) = (max(|g_1(x)|, |g_2(x)|)$ for all $x$
- Suppose that $f_1(x)$ is $O(g_1(x))$ and that $f_2(x)$ is $O(g_2(x))$. Then $(f_1f_2)(x)$ is $O(g_1(x)g_2(x))$
- Let $f(x) = a_nx^n + a_{n−1}x^{n−1} + ⋯ + a_1x + a_0$, where $a_0, a_1, … , a_n$ are real numbers with $a_n ≠ 0$. Then $f(x)$ is of order $x_n$

### 3.3 Complexity of Algorithms
- An **algorithmic paradigm** is a general approach based on a particular concept that can be used to construct algorithms for solving a variety of problems
- In a **brute-force algorithm**, a problem is solved in the most straightforward manner based on the statement of the problem and the definitions of terms
<br>

- A problem that is solvable using an algorithm with polynomial (or better) worst-case complexity is called **tractable**
-  Problems for which a solution can be checked in polynomial time are said to belong to the **class NP** (tractable problems are said to belong to **class P**) The abbreviation NP stands for *nondeterministic polynomial* time
-  There is also an important class of problems, called **NP-complete problems**, with the property that if any of these problems can be solved by a polynomial worst-case time algorithm, then all problems in the class NP can be solved by polynomial worst-case time algorithms
-  The **P versus NP problem** asks whether NP, the class of problems for which it is possible to check solutions in polynomial time, equals P, the class of tractable problems




