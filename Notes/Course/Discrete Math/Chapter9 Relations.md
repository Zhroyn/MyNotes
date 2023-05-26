<!-- TOC -->

- [Relations](#relations)
  - [9.1 Relations and Their Properties](#91-relations-and-their-properties)
    - [Properties of Binary Relations](#properties-of-binary-relations)
    - [Combining Relations](#combining-relations)
  - [9.2 n-ary Relations and Their Applications](#92-n-ary-relations-and-their-applications)
  - [9.3 Representing Relations](#93-representing-relations)
  - [9.4 Closures of Relations](#94-closures-of-relations)
    - [Transitive Closures](#transitive-closures)
    - [Warshall’s Algorithm](#warshalls-algorithm)
  - [9.5 Equivalence Relations](#95-equivalence-relations)
    - [Equivalence Relations](#equivalence-relations)
    - [Equivalence Classes](#equivalence-classes)
    - [Equivalence Classes and Partitions](#equivalence-classes-and-partitions)
    - [The Operations of Equivalence Class](#the-operations-of-equivalence-class)
  - [9.6 Partial Orderings](#96-partial-orderings)
    - [Definitions about Partial Ordering](#definitions-about-partial-ordering)
    - [Lexicographic Order](#lexicographic-order)
    - [Hasse Diagrams](#hasse-diagrams)
    - [Maximal and Minimal Elements](#maximal-and-minimal-elements)
    - [Lattice](#lattice)
    - [Topological Sorting](#topological-sorting)

<!-- /TOC -->






## Relations
### 9.1 Relations and Their Properties
- Let $A$ and $B$ be sets. A **binary relation from $A$ to $B$** is a subset of $A × B$.
- We use the notation $aRb$ to denote that $(a, b) ∈ R$ and $a \cancel{R} b$ to denote that $(a, b) ∉ R$.
- Moreover, when $(a, b)$ belongs to $R$, $a$ is said to be **related to** $b$ by $R$.
- A **relation on a set $A$** is a relation from $A$ to $A$.

<br>

#### Properties of Binary Relations
- A relation $R$ on a set $A$ is called **reflexive** if $(a, a) ∈ R$ for every element $a ∈ A$.
- A relation $R$ on a set $A$ is called **symmetric** if for all $a, b ∈ A$, $(b, a) ∈ R$ whenever $(a, b) ∈ R$.
- A relation $R$ on a set $A$ is called **antisymmetric** if for all $a, b ∈ A$, if $(a, b) ∈ R$ and $(b, a) ∈ R$, then $a = b$.
- A relation $R$ on a set $A$ is called **transitive** if for all $a, b ∈ A$, if $(a, b) ∈ R$ and $(b, c) ∈ R$, then $ (a, c) ∈ R$.

<br>

#### Combining Relations
- Two relations from $A$ to $B$ can be combined in any way two sets can be combined, such as $R_1 ∪ R_2, R_1 ∩ R_2, R_1 ⊕ R_2, R_1 − R_2, R_2 − R_1$.
- Let $R$ be a relation from $A$ to $B$, and $S$ a relation from $B$ to $C$. The **composite** of $R$ and $S$ is the relation consisting of ordered pairs $(a, c)$, where $a ∈ A, c ∈ C$, and $\exists b ∈ B, (a, b) ∈ R, (b, c) ∈ S$. We denote the composite of $R$ and $S$ by $S \circ R$.
- Let $R$ be a relation on the set $A$. The powers $R^n, n = 1, 2, 3, …$ , are defined recursively by $$R^1 = R, R^{n+1} = R^n \circ R $$
- **THEOREM :** A relation $R$ on a set $A$ is transitive if and only if $R^n \subseteq R$ for $n = 1, 2, 3, …$
<br>

- $\bar{R} = A\times B - R $
- $(R\circ T)\circ P = R\circ (T\circ P) $
- $(R \cup S) \circ T = R\circ T \cup S\circ T $

**Inverse Relation**
If $R = \left\{ (a, b) | a\in A, b\in B, aRb \right\}$, then define $$R^{-1} = \left\{ (b, a) | (a, b)\in R, a\in A, b\in B \right\}$$

- $(R \cup S)^{-1} = R^{-1} \cup S^{-1} $
- $(R \cap S)^{-1} = R^{-1} \cap S^{-1} $
- $(\bar{R})^{-1} = \overline{R^{-1}} $
- $(R - S)^{-1} = R^{-1} - S^{-1} $
- $(A\times B)^{-1} = B\times A $
- $(S \circ T)^{-1} = T^{-1} \circ S^{-1} $







<br>

### 9.2 n-ary Relations and Their Applications
- Let $A_1, A_2, … , A_n$ be sets. An **n-ary relation** on these sets is a subset of $A_1 × A_2 × ⋯ × A_n$.
- The sets $A_1, A_2, … , A_n$ are called the **domains** of the relation, and $n$ is called its **degree**.
<br>

- Let $R$ be an n-ary relation and $C$ a condition that elements in $R$ may satisfy. Then the **selection operator** $s_C$ maps the n-ary relation R to the n-ary relation of all n-tuples from $R$ that satisfy the condition $C$.
- The **projection** $P_{i_1i_2,…,i_m}$ where $i_1 < i_2 < ⋯ < i_m$, maps the n-tuple $(a_1, a_2, … , a_n)$ to the m-tuple $(a_{i1}, a_{i2}, … , a_{im} )$, where $m ≤ n$.
- Let $R$ be a relation of degree $m$ and $S$ a relation of degree $n$. The **join** $J_p(R, S)$, where $p ≤ m$ and $p ≤ n$, is a relation of degree $m + n − p$ that consists of all (m + n − p)-tuples $(a_1, a_2, … , a_{m−p}, c_1, c_2, … , c_p, b_1, b_2, … , b_{n−p})$, where the m-tuple $(a_1, a_2, … , a_{m−p}, c_1, c_2, … , c_p)$ belongs to $R$ and the n-tuple $(c_1, c_2, … , c_p, b_1, b_2, … , b_{n−p})$ belongs to $S$.






<br>

### 9.3 Representing Relations
The relation $R$ can be represented by the matrix $M_R = [m_{ij}]$, where
$$
m_{ij} =
\left\{
\begin{aligned}
  1 \text{ if } (a_i, b_j) \in R \\
  0 \text{ if } (a_i, b_j) \notin R \\
\end{aligned}
\right.
$$

- $R$ is reflexive if and only if all elements on the main diagonal of $M_R$ are equal to 1.
- $R$ is symmetric if and only if $M_R = (M_R)^T$.
- $R$ is antisymmetric if and only if $M_R$ has the property that if $m_{ij} = 1$ with $i ≠ j$, then $m_{ji} = 0$.
<br>

- $M_{R_1 \cup R_2} = [c_{ij} \vee d_{ij}] = M_{R_1} \vee M_{R_2} $
- $M_{R_1 \cap R_2} = [c_{ij} \wedge d_{ij}] = M_{R_1} \wedge M_{R_2} $
- $M_{\bar{R}_1} = [\bar{c}_{ij}] $
- $M_{R_1 - R_2} = [c_{ij} \wedge \bar{d}_{ij}] = M_{R_1 \wedge \bar{R}_2} $
- $M_{R_2 \circ R_1} = [\bigvee_{k=1}^n (c_{ik} \wedge d_{kj})] = M_{R_1} \odot M_{R_2} $
- $M_{R^{-1}} = M_{R}^T $
<br>

- A **directed graph**, or **digraph**, consists of a set $V$ of *vertices* (or *nodes*) together with a set $E$ of ordered pairs of elements of $V$ called *edges* (or *arcs*). The vertex $a$ is called the *initial vertex* of the edge $(a, b)$, and the vertex $b$ is called the *terminal vertex* of this edge.
- An edge of the form $(a, a)$ is called a **loop**.







<br>

### 9.4 Closures of Relations
- If $R$ is a relation on a set $A$, then the closure of $R$ with respect to $P$, if it exists, is the relation $S$ on $A$ with property $P$ that contains $R$ and is a subset of every subset of $A × A$ containing $R$ with property $P$.
- The closure of a relation $R$ with respect to property $P$ is the smallest relation with property $P$ containing $R$.
<br>

- The reflexive closure of $R$ is $r(R) = R \cup I_A $.
- The symmetric closure of $R$ is $s(R) = R \cup R^{-1} $.
<br>

- A **path** from $a$ to $b$ in the directed graph $G$ is a sequence of edges $(x_0, x_1), (x_1, x_2), (x_2, x_3), … , (x_{n−1}, x_n)$ in $G$, where $n$ is a nonnegative integer, and $x_0 = a$ and $x_n = b$,
- The path denoted by $x_0, x_1, x_2, … , x_{n−1}, x_n$ has length $n$.
- We view the empty set of edges as a path of length zero from $a$ to $a$. 
- A path of length $n ≥ 1$ that begins and ends at the same vertex is called a **circuit** or **cycle**.
- There is a path of length $n$, where $n$ is a positive integer, from $a$ to $b$ if and only if $(a, b) ∈ R^n$.

<br>

#### Transitive Closures
- The **connectivity relation** $R^∗$ consists of the pairs $(a, b)$ such that there is a path of length at least one from $a$ to $b$ in $R$, that is $$R^* = \bigcup_{n=0}^{\infty} R^n $$
<br>

- The transitive closure of $R$ is $t(R) = R^∗$.
- When $a ≠ b$, if there is a path of length at least one in $R$ from $a$ to $b$, then there is such a path with length not exceeding $n − 1$.
- If $|A| = n$, then any path of length $> n$ must contain a cycle.
- If $|A| = n$, then $t(R) = R^* = R \cup R^2 \cup \cdots \cup R^n $.
- Let $M_R$ be the zero–one matrix of the relation $R$ on a set with $n$ elements, then $$M_{R^∗} = M_R ∨ M^{[2]}_R ∨ M^{[3]}_R ∨ ⋯ ∨ M^{[n]}_R$$

$\text{procedure } \textit{transitive closure } (M_R : \text{zero–one } n × n \text{ matrix}) \\
A := M_R \\
B := A \\
\text{for } i := 2 \text{ to } n \\
\quad A := A ⊙ M_R \\
\quad B := B ∨ A \\
\text{return } B\{B \text{ is the zero–one matrix for } R^∗\}$

This algorithm uses $n^2(2n−1)(n−1) + (n−1)n^2 = 2n^3(n−1)$, which is $O(n^4)$ bit operations

<br>

#### Warshall’s Algorithm
- Warshall’s algorithm is an efficient method for computing the transitive closure of a relation, using only $2n^3$ bit operations.
<br>

- If $a, x_1, x_2, … , x_{m−1}, b$ is a path, then its **interior vertices** are $x_1, x_2, … , x_{m−1}$
- $W_0 = M_R, W_n = M_{R^∗}$, and $W_k =[w^{(k)}_{ij}]$, where $w^{(k)}_{ij} = 1$ if there is a path from $v_i$ to $v_j$ such that all the interior vertices of this path are in the set $\{v_1, v_2, … , v_k\}$ and is $0$ otherwise.
- There is a path from $v_i$ to $v_j$ with no vertices other than $v_1, v_2, … , v_k$ as interior vertices if and only if either there is a path from $v_i$ to $v_j$ with its interior vertices among the first $k − 1$ vertices in the list, or there are paths from $v_i$ to $v_k$ and from $v_k$ to $v_j$ that have interior vertices only among the first $k − 1$ vertices in the list. So $$w^{[k]}_{ij} = w^{[k−1]}_{ij} ∨ (w^{[k−1]}_{ik} ∧ w^{[k−1]}_{kj} )$$







<br>

### 9.5 Equivalence Relations
#### Equivalence Relations
**Definition of Equivalence Relation**
A relation on a set $A$ is called an **equivalence relation** if it is *reflexive*, *symmetric*, and *transitive*.

**Definition of Equivalent**
Two elements $a$ and $b$ that are related by an equivalence relation are called **equivalent**, which is noted by $a ∼ b$.


#### Equivalence Classes
**Definition of Equivalence Class**
If $R$ is an equivalence relation on a set $A$, **the equivalence class of the $a$ with respect to $R$** is $$[a]_R = \{s ∣ (a, s) ∈ R\}$$
- When only one relation is under consideration, we can delete the subscript $R$ and write $[a]$ for this equivalence class.
- If $b ∈ [a]_R$, then $b$ is called a representative of this equivalence class.

**Theorem 1**
Let $R$ be an equivalence relation on a set $A$. These statements for elements $a$ and $b$ of $A$ are equivalent:
$\pod{1}\; aRb$
$\pod{2}\; [a] = [b]$
$\pod{3}\; [a] \cap [b] \neq \emptyset$
 
$(2)\Rightarrow (3) : $
$$
\left.
\begin{aligned}
  [a] = [b] \\
  R \text{ is reflexive} \Rightarrow [a] \text{ is nonempty} \\
\end{aligned}
\right\}
\Rightarrow [a] \cap [b] \neq \emptyset
$$

<br>

#### Equivalence Classes and Partitions
**Definition of Partition**
A **partition** of a set $S$ is a collection of disjoint nonempty subsets of $S$ that have $S$ as their union.
$\{A_i | i ∈ I\}$ (where $I$ is an index set) forms a partition of $S$ if and only if
$$
A_i \neq \emptyset \text{ for } i \in I \\
A_i \cap A_j \neq \emptyset \text{ when } i \neq j \\
\bigcup_{i\in I} A_i = S
$$

**Theorem 2**
Let $R$ be an equivalence relation on a set $S$. Then the equivalence classes of $R$ form a partition of $S$.
Conversely, given a partition $\{A_i ∣ i ∈ I\}$ of the set $S$, there is an equivalence relation $R$ that has the sets $A_i, i ∈ I$, as its equivalence classes.

<br>

#### The Operations of Equivalence Class
**Theorem 3**
If $R_1, R_2$ are equivalence relations on $A$, then $R_1 \cap R_2$ is equivalence relations on $A$.

**Theorem 4**
If $R_1, R_2$ are equivalence relations on $A$, then $R_1 \cup R_2$ is reflexive and symmetric relations on $A$.








<br>

### 9.6 Partial Orderings
#### Definitions about Partial Ordering
**Definition 1**
A relation $R$ on a set $S$ is called a **partial ordering** or **partial order** if it is *reflexive*, *antisymmetric*, and *transitive*.
A set $S$ together with a partial ordering $R$ is called a **partially ordered set**, or **poset**, which is denoted by $(S, R)$.
Members of $S$ are called **elements** of the poset.

**Definition 2**
When $a$ and $b$ are elements of a poset $(S, \preccurlyeq )$ such that either $a \preccurlyeq b$ or $b \preccurlyeq a$, $a$ and $b$ are called **comparable**.
When $a$ and $b$ are elements of $(S, \preccurlyeq )$ such that neither $a \preccurlyeq b$ nor $b \preccurlyeq a$, $a$ and $b$ are called **incomparable**.

**Definition 3**
If $(S, \preccurlyeq )$ is a poset and every two elements of $S$ are comparable, $S$ is called a **totally ordered or linearly ordered set**, and $\preccurlyeq$ is called a **total order** or a **linear order**.
A subset of a poset such that every two elements of this subset are comparable is called a **chain**.
A subset of a poset such that every two elements of this subset are incomparable is called an **antichain**.

**Definition 4**
$(S, \preccurlyeq )$ is a **well-ordered set** if it is a poset such that $\preccurlyeq$ is a total ordering and every nonempty subset of $S$ has a least element.

**Theorem 1 : The Principle of Well-ordered Induction**
Suppose that $S$ is a well-ordered set, then $P(x)$ is true for all $x ∈ S$, if
**Inductive Step**: For every $y ∈ S$, if $P(x)$ is true for all $x ∈ S$ with $x ≺ y$, then $P(y)$ is
true.
$\text{Proof :}$ Suppose it is not the case that $P(x)$ is true for all $x ∈ S$, then there is an element $y ∈ S$ such that $P(y)$ is false. Consequently, the set $A = \{x ∈ S ∣ P(x) \text{ is false}\}$ is nonempty.
Because $S$ is well-ordered, $A$ has a least element $a$. By the choice of $a$ as a least element of $A$, we know that $P(x)$ is true for all $x ∈ S$ with $x \prec a$. This implies by the inductive step $P(a)$ is true.
This contradiction shows that $P(x)$ must be true for all $x ∈ S$.

<br>

#### Lexicographic Order
A **lexicographic ordering** can be defined on the Cartesian product of $n$ posets $(A_1, \preccurlyeq_{1}), (A_2, \preccurlyeq_{2}), … , (A_n, \preccurlyeq_{n})$. Define the partial ordering $\preccurlyeq$ on $A_1 × A_2 × ⋯ × A_n$ by $$(a_1, a_2, … , a_n) ≺ (b_1, b_2, … , b_n)$$ if $a_1 \prec_{1} b_1$, or if there is an integer $i > 0$ such that $a_1 = b_1, … , a_i = b_i$ and $a_{i+1} \prec_{i+1} b_{i+1}$

<br>

#### Hasse Diagrams
The procedure of constructing a Hasse diagram of $(S, \preccurlyeq)$ is:
1. Construct a digraph representation of the poset $(S, \preccurlyeq)$ so that all arcs are pointed upward (except the loops).
2. Eliminate all loops.
3. Eliminate all arcs that are redundant because of transitivity.
4. Eliminate the arrows at the ends of arcs since everything points up.

<br>

#### Maximal and Minimal Elements
$a$ is **maximal** in the poset $(S, \preccurlyeq )$ if there is no $b ∈ S$ such that $a \prec b$.
$a$ is **minimal** in the poset $(S, \preccurlyeq )$ if there is no $b ∈ S$ such that $b \prec a$.

$a$ is the **greatest element** of the poset $(S, \preccurlyeq )$ if $b \preccurlyeq a$ for all $b ∈ S$.
$a$ is the **least element** of the poset $(S, \preccurlyeq )$ if $a \preccurlyeq b$ for all $b ∈ S$.
The greatest and least elements are unique.

<br>

#### Lattice
A partially ordered set in which every pair of elements has both a least upper bound and a greatest lower bound is called a **lattice**.

<br>

#### Topological Sorting
A total ordering $\preccurlyeq$ is said to be compatible with the partial ordering $R$ if $a \preccurlyeq b$ whenever $aRb$.
Constructing a compatible total ordering from a partial ordering is called **topological sorting**.

**Lemma 1**
Every finite nonempty poset $(S, \preccurlyeq )$ has at least one minimal element.

**Algorithm**
$
\text{procedure } \textit{topological sort } ((S, \preccurlyeq )\text{: finite poset}) \\
k := 1 \\
\text{while } S ≠ ∅ \\
\quad a_k := \text{ a minimal element of S \{such an element exists by Lemma 1\}} \\
\quad S := S − {a_k} \\
\quad k := k + 1 \\
\text{return } a_1, a_2,… , a_n \{a_1, a_2,… , a_n \text{ is a compatible total ordering of } S\} \\
$






