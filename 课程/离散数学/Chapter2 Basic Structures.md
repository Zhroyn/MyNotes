
- [Basic Structures](#basic-structures)
  - [2.1 Sets](#21-sets)
  - [2.2 Set Operations](#22-set-operations)
  - [2.3 Functions](#23-functions)
  - [2.5 Cardinality of Sets](#25-cardinality-of-sets)
  - [2.6 Matrices](#26-matrices)








## Basic Structures
### 2.1 Sets
- **elements** or **members** : $a ∈ A$ or $a ∉ A$
- describe a set : use **roster method** or **set builder** notation
- **equal** if and only if have the same elements
- **subject** : $A ⊆ B$ or $A ⊈ B$
- **superset** : $B ⊇ A$
- **proper subset** : $A ⊂ B$
<br>

- If there are exactly $n$ distinct elements in $S$ where $n$ is a nonnegative integer, we say that $S$ is a **finite set** and that $n$ is the **cardinality** of $S$. The cardinality of $S$ is denoted by $|S|$
- A set is said to be **infinite** if it is not finite
- The **power set** of $S$ is the set of all subsets of the set $S$, which is denoted by $P(S)$
<br>

- **ordered n-tuple** : $(a_1, a_2, … , a_n)$
- **ordered pairs** : $(a_1, a_2)$
- **Cartesian product** : $A1 × A2 × ⋯ × An = \{(a_1, a_2, … , a_n) ∣ a_i ∈ A_i \; for \; i = 1, 2, … , n\}$
- A subset $R$ of the Cartesian product $A × B$ is called a **relation** from the set $A$ to the set $B$
<br>

- $∀x ∈ S(P(x))$ is shorthand for $∀x(x ∈ S → P(x))$
- $∃x ∈ S(P(x))$ is shorthand for $∃x(x ∈ S ∧ P(x))$
- We define the **truth set** of $P$ to be the set of elements $x$ in $D$ for which $P(x)$ is true, which is denoted by $\{x ∈ D ∣ P(x)\}$







<br>

### 2.2 Set Operations
- **union** : $A ∪ B$
- **intersection** : $A ∩ B$
  - Two sets are called **disjoint** if their intersection is the empty set
- **difference of A and B** or **complement of B with respect to A** : $A − B$
- **complement** : $\bar{A}$

|Identity|Name|
|--|--|
|$A ∩ U = A$ <br> $A ∪∅= A$ | Identity laws |
|$A ∪ U = U$ <br> $A ∩∅=∅$ | Domination laws  |
|$A ∪ A = A$ <br> $A ∩ A = A$ | Idempotent laws  |
|$\overline{(\bar A)} = A$ | Complementation law |
|$A ∪ B = B ∪ A$ <br> $A ∩ B = B ∩ A$ | Commutative laws |
|$A ∪ (B ∪ C) = (A ∪ B) ∪ C$ <br> $A ∩ (B ∩ C) = (A ∩ B) ∩ C$ | Associative laws |
|$A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)$ <br> $A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)$ | Distributive laws |
|$\overline{(A ∩ B)} = \bar A ∪ \bar B$ <br> $\overline{(A ∪ B)} = \bar A ∩ \bar B$ | De Morgan's laws |
|$A ∪ (A ∩ B) = A$ <br> $A ∩ (A ∪ B) = A$ | Absorption laws |
|$A ∪ \bar A = U$ <br> $A ∩ \bar A = ∅$ | Complement laws |

- A **multiset** (short for multiple-membership set) $\{m_1 ⋅ a_1, m_2 ⋅ a_2, … , m_r ⋅ a_r\}$ is an unordered collection of elements where an element can occur as a member more than once. The numbers $m_i , i = 1, 2, … , r$, are called the **multiplicities** of the elements $a_i , i = 1, 2, … , r$
- In the **union** of the multisets P and Q, the multiplicity is the maximum
- In the **intersection** of the multisets P and Q, the multiplicity is the minimum
- In the **difference** of P and Q, the multiplicity is the difference of P less Q unless this difference is negative
- In the **sum** of P and Q, the multiplicity is the sum of multiplicities in P and Q






<br>

### 2.3 Functions
- A **function** $f$ from $A$ to $B$ is an assignment of exactly one element of $B$ to each element of $A$.
- We write $f(a) = b$ if $b$ is the unique element of $B$ assigned by the function $f$ to the element $a$ of $A$, and we say that $b$ is the **image** of $a$ and $a$ is a **preimage** of $b$. The **range**, or **image** of $f$, is the set of all images of elements of $A$
- If $f$ is a function from $A$ to $B$, we write $f : A → B$ and we say that $A$ is the **domain** of $f$ and $B$ is the **codomain** of $f$.
- Let $f_1$ and $f_2$ be functions from $A$ to $R$. Then $f_1 + f_2$ and $f_1 f_2$ are also functions from $A$ to $R$ defined for all $x ∈ A$ by
  - $(f_1 + f_2)(x) = f_1(x) + f_2(x)$
  - $(f_1f_2)(x) = f_1(x)f_2(x)$
- The **image** of $S$ : $f(S) = \{t ∣ ∃s∈S (t = f(s))\}$ or $\{f(s) ∣ s ∈ S\}$
<br>

- A function $f$ is said to be **one-to-one**, or an **injection**, if and only if $f(a) = f(b)$ implies that $a = b$ for all $a$ and $b$ in the domain of $f$. A function is said to be **injective** if it is one-to-one
- A function f from A to B is called **onto**, or a **surjection**, if and only if for every element $b ∈ B$ there is an element $a ∈ A$ with $f(a) = b$. A function is called **surjective** if it is onto
- The function f is a **one-to-one correspondence**, or a **bijection**, if it is both one-to-one and onto. We also say that such a function is **bijective**
<br>

- The **inverse function** of $f$ is denoted by $f^{−1}$
- Let $g$ be a function from the set $A$ to the set $B$ and let $f$ be a function from the set $B$ to the set $C$, then the **composition** of the functions $f$ and $g$ is denoted by $f \circ g$
- The value of the **floor function** at $x$ is denoted by $⌊x⌋$
- The value of the **ceiling function** at $x$ is denoted by $⌈x⌉$
- A **partial function** $f$ from $A$ to $B$ is an assignment to each element $a$ in a subject of $A$, called the domain of definition of $f$ , of a unique element $b$ in $B$. We say that $f$ is undefined for elements in $A$ that are not in the domain of definition of $f$. When the domain of definition of $f$ equals $A$, we say that $f$ is a **total function**






<br>

### 2.5 Cardinality of Sets
- The sets $A$ and $B$ have the same cardinality if and only if there is a one-to-one correspondence from $A$ to $B$, and this is denoted by $|A| = |B|$
- If there is a one-to-one function from $A$ to $B$, we write $|A| ≤ |B|$
- A set that is either finite or has the same cardinality as the set of positive integers is called **countable**, and we denote the cardinality of this set by $ℵ_0$. We write $|S| = ℵ_0$ and say that $S$ has cardinality "aleph null"

- If $A$ and $B$ are countable sets, then $A ∪ B$ is also countable
-  **Schröder-Bernstein theorem** :  If $A$ and $B$ are sets with $|A| ≤ |B|$ and $|B| ≤ |A|$, then $|A| = |B|$. In other words, if there are one-to-one functions $f$ from $A$ to $B$ and $g$ from $B$ to $A$, then there is a one-to-one correspondence between $A$ and $B$






<br>

### 2.6 Matrices
**Zero-One Matrices**
- Let $A = [a_{ij}]$ and $B = [b_{ij}]$ be $m × n$ zero–one matrices, then:
- The **join** of $A$ and $B$ is the zero–one matrix with $(i, j)$th entry $a_{ij} ∨ b_{ij}$. The join of $A$ and $B$ is denoted by $A ∨ B$.
- The **meet** of $A$ and $B$ is the zero–one matrix with $(i, j)$th entry $a_{ij} ∧ b_{ij}$. The meet of $A$ and $B$ is denoted by $A ∧ B$.
- Let $A = [a_{ij}]$ be an $m × k$ zero–one matrix and $B = [b_{ij}]$ be a $k × n$ zero–one matrix. Then the Boolean product of $A$ and $B$, denoted by $A \odot B$, is the $m × n$ matrix with $(i, j)$th entry $cij$ where
$$ c_{ij} = (a_{i1} ∧ b_{1j}) ∨ (a_{i2} ∧ b_{2j})
∨ ⋯ ∨ (a_{ik} ∧ b_{kj})
$$
- The $r$th **Boolean power** of $A$ is the Boolean product of $r$ factors of $A$. The $r$th Boolean product of $A$ is denoted by $A^{[r]}$.
- We also define $A^{[0]}$ to be $I_n$.



