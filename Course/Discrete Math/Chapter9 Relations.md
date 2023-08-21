
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Relations](#relations)
  - [9.1 Relations and Their Properties](#91-relations-and-their-properties)
    - [Properties of Binary Relations](#properties-of-binary-relations)
    - [Combining Relations](#combining-relations)
    - [Inverse and Complementary Relations](#inverse-and-complementary-relations)
  - [9.3 Representing Relations](#93-representing-relations)
    - [Representing Relations Using Matrices](#representing-relations-using-matrices)
    - [Representing Relations Using Digraphs](#representing-relations-using-digraphs)
  - [9.4 Closures of Relations](#94-closures-of-relations)
    - [Different Types of Closures](#different-types-of-closures)
    - [Paths in Directed Graphs](#paths-in-directed-graphs)
    - [Transitive Closures](#transitive-closures)
    - [Warshall’s Algorithm](#warshalls-algorithm)
  - [9.5 Equivalence Relations](#95-equivalence-relations)
    - [Equivalence Relations](#equivalence-relations)
    - [Equivalence Classes](#equivalence-classes)
    - [Equivalence Classes and Partitions](#equivalence-classes-and-partitions)
  - [9.6 Partial Orderings](#96-partial-orderings)
    - [Terminology for Partial Ordering](#terminology-for-partial-ordering)
    - [Lexicographic Order](#lexicographic-order)
    - [Hasse Diagrams](#hasse-diagrams)
    - [Maximal and Minimal Elements](#maximal-and-minimal-elements)
    - [Lattice](#lattice)
    - [Topological Sorting](#topological-sorting)

<!-- /code_chunk_output -->








## Relations
### 9.1 Relations and Their Properties
**Definition**
A **binary relation** from $A$ to $B$ is a subset of $A × B$, in other words, is a set $R$ of ordered pairs. When $(a, b)$ belongs to $R$, $a$ is said to be **related to** $b$ by $R$.
A **relation on a set $A$** is a relation from $A$ to $A$.

$(a, b) ∈ R$ is denoted by $aRb$, $(a, b) ∉ R$ is denoted by $a \cancel{R} b$.

> There are $2^{n^2}$ relations on a set with $n$ elements.

<br>

#### Properties of Binary Relations
A relation $R$ on a set $A$ is called **reflexive** if $$\forall a\in A, aRa$$

A relation $R$ on a set $A$ is called **symmetric** if $$\forall a, b\in A, aRb \rightarrow bRa$$

A relation $R$ on a set $A$ is called **asymmetric** if $$\forall a, b\in A, aRb \rightarrow b \cancel R a$$

A relation $R$ on a set $A$ is called **antisymmetric** if $$\forall a, b\in A, aRb \land bRa \rightarrow a = b$$

A relation $R$ on a set $A$ is called **transitive** if $$\forall a, b, c\in A, aRb \wedge bRc \rightarrow aRc$$


> There are $2^{n(n-1)}$ relations on a set with $n$ elements that are reflecxive.
> There are $2^{n(n-1)}$ relations on a set with $n$ elements that are irreflecxive.
> There are $2^{\frac{n(n+1)}{2}}$ relations on a set with $n$ elements that are symmetric.
> There are $3^{\frac{n(n-1)}{2}}$ relations on a set with $n$ elements that are asymmetric.
> There are $2^{n}3^{\frac{n(n-1)}{2}}$ relations on a set with $n$ elements that are antisymmetric.

<br>

#### Combining Relations
Let $R$ be a relation from $A$ to $B$, and $S$ a relation from $B$ to $C$, then the **composite** of $R$ and $S$ is
$$S \circ R = \{ (a, c) | (a, b) \in R, (b, c) \in S \}$$

The powers $R^n, n = 1, 2, 3, …$ , are defined recursively by 
$$R^1 = R, \quad R^{n+1} = R^n \circ R $$

**Theorem 1**
A relation $R$ on a set $A$ is transitive if and only if $R^n \subseteq R$ for $n = 1, 2, 3, …$

<br>

#### Inverse and Complementary Relations
Let $R$ be a relation from $A$ to $B$, then the **inverse relation** of $R$ is
$$R^{-1} = \{ (b, a) | (a, b)\in R\}$$

and the complementary relation of $R$ is
$$\overline{R} = \{ (a, b) | (a, b)\notin R\}$$

- $\overline{R} = A\times B - R $
- $(\overline{R})^{-1} = \overline{R^{-1}} $
- $(R \cup S)^{-1} = R^{-1} \cup S^{-1} $
- $(R \cap S)^{-1} = R^{-1} \cap S^{-1} $
- $(R - S)^{-1} = R^{-1} - S^{-1} $
- $(A\times B)^{-1} = B\times A $
- $(S \circ T)^{-1} = T^{-1} \circ S^{-1} $









<br>

### 9.3 Representing Relations
#### Representing Relations Using Matrices
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

$R$ is reflexive if and only if all elements on the main diagonal of $M_R$ are equal to 1.
$R$ is symmetric if and only if $M_R = (M_R)^T$.
$R$ is antisymmetric if and only if $M_R$ has the property that if $m_{ij} = 1$ with $i ≠ j$, then $m_{ji} = 0$.
<br>

- $M_{R_1 \cup R_2} = [c_{ij} \vee d_{ij}] = M_{R_1} \vee M_{R_2} $
- $M_{R_1 \cap R_2} = [c_{ij} \wedge d_{ij}] = M_{R_1} \wedge M_{R_2} $
- $M_{\overline{R}_1} = [\overline{c}_{ij}] $
- $M_{R_1 - R_2} = [c_{ij} \wedge \overline{d}_{ij}] = M_{R_1 \cap \overline{R}_2} $
- $M_{R_2 \circ R_1} = [\bigvee_{k=1}^n (c_{ik} \wedge d_{kj})] = M_{R_1} \odot M_{R_2} $
- $M_{R^{-1}} = M_{R}^T $

<br>

#### Representing Relations Using Digraphs
A **directed graph**, or **digraph**, consists of a set $V$ of *vertices* (or *nodes*) together with a set $E$ of ordered pairs of elements of $V$ called *edges* (or *arcs*). The vertex $a$ is called the *initial vertex* of the edge $(a, b)$, and the vertex $b$ is called the *terminal vertex* of this edge.

An edge of the form $(a, a)$ is called a **loop**.









<br>

### 9.4 Closures of Relations
#### Different Types of Closures
If $R$ is a relation on a set $A$, then the **closure** of $R$ with respect to $P$, if it exists, is the relation $S$ on $A$ with property $P$ that contains $R$ and is a subset of every subset of $A × A$ containing $R$ with property $P$.
The closure of a relation $R$ with respect to property $P$ is the smallest relation with property $P$ containing $R$.

- The reflexive closure of $R$ is $r(R) = R \cup I_A $.
- The symmetric closure of $R$ is $s(R) = R \cup R^{-1} $.

<br>

#### Paths in Directed Graphs
A **path** from $a$ to $b$ in the directed graph $G$ is a sequence of edges $(x_0, x_1), (x_1, x_2), (x_2, x_3), … , (x_{n−1}, x_n)$ in $G$, where $n$ is a nonnegative integer, and $x_0 = a$ and $x_n = b$. The path is denoted by $x_0, x_1, x_2, … , x_{n−1}, x_n$ and has **length** $n$.
We view the empty set of edges as a path of length zero from $a$ to $a$.

A path of length $n ≥ 1$ that begins and ends at the same vertex is called a **circuit** or **cycle**.

**Theorem 1**
There is a path of length $n$, where $n$ is a positive integer, from $a$ to $b$ if and only if $(a, b) ∈ R^n$.

<br>

#### Transitive Closures
Let $R$ be a relation on a set $A$, then the **connectivity relation** $R^*$ is
$$R^* = \bigcup_{n=0}^{\infty} R^n $$

**Theorem 2**
The transitive closure of $R$ is $t(R) = R^∗$.
If $|A| = n$, then any path of length $> n$ must contain a cycle.
If $|A| = n$, then $t(R) = R^* = R \cup R^2 \cup \cdots \cup R^n $.

**Theorem 3**
Let $M_R$ be the zero–one matrix of the relation $R$ on a set with $n$ elements, then $$M_{R^∗} = M_R ∨ M^{[2]}_R ∨ M^{[3]}_R ∨ ⋯ ∨ M^{[n]}_R$$

$
\textbf{procedure } \textit{transitive closure } (M_R : \text{zero–one } n × n \text{ matrix}) \\
A := M_R \\
B := A \\
\text{for } i := 2 \text{ to } n \\
\qquad A := A ⊙ M_R \\
\qquad B := B ∨ A \\
\text{return } B \; \{B \text{ is the zero–one matrix for } R^∗\}$

This algorithm uses $n^2(2n−1)(n−1) + (n−1)n^2 = 2n^3(n−1)$, which is $O(n^4)$ bit operations

<br>

#### Warshall’s Algorithm
Warshall’s algorithm is an efficient method for computing the transitive closure of a relation, using only $2n^3$ bit operations.

$
\textbf{procedure } \textit{Warshall’s Algorithm } (M_R : \text{zero–one } n × n \text{ matrix}) \\
k := 0 \\
W_0 := M_R \\
\text{for } k := 1 \text{ to } n \\
\qquad \text{for } i := 1 \text{ to } n \\
\qquad \qquad \text{for } j := 1 \text{ to } n \\
\qquad \qquad \qquad w^{[k]}_{ij} = w^{[k−1]}_{ij} ∨ (w^{[k−1]}_{ik} ∧ w^{[k−1]}_{kj} ) \\
\text{return } W_n \; \{W_n \text{ is the zero–one matrix for } R^∗\}$

> $W_0 = \begin{bmatrix}
  0 & 1 & 1 & 0 & 1 \\
  1 & 0 & 1 & 0 & 0 \\
  1 & 1 & 0 & 0 & 0 \\
  1 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 1 & 0 \\
\end{bmatrix}, W_1 = \begin{bmatrix}
  0 & 1 & 1 & 0 & 1 \\
  1 & 1 & 1 & 0 & 1 \\
  1 & 1 & 1 & 0 & 1 \\
  1 & 1 & 1 & 0 & 1 \\
  0 & 0 & 0 & 1 & 0 \\
\end{bmatrix},$
> 
> $W_2 = \begin{bmatrix}
  1 & 1 & 1 & 0 & 1 \\
  1 & 1 & 1 & 0 & 1 \\
  1 & 1 & 1 & 0 & 1 \\
  1 & 1 & 1 & 0 & 1 \\
  0 & 0 & 0 & 1 & 0 \\
\end{bmatrix} = W_3, W_4 = \begin{bmatrix}
  1 & 1 & 1 & 0 & 1 \\
  1 & 1 & 1 & 0 & 1 \\
  1 & 1 & 1 & 0 & 1 \\
  1 & 1 & 1 & 0 & 1 \\
  1 & 1 & 1 & 1 & 1 \\
\end{bmatrix},$
> 
> $W_5 = \begin{bmatrix}
  1 & 1 & 1 & 1 & 1 \\
  1 & 1 & 1 & 1 & 1 \\
  1 & 1 & 1 & 1 & 1 \\
  1 & 1 & 1 & 1 & 1 \\
  1 & 1 & 1 & 1 & 1 \\
\end{bmatrix}$







<br>

### 9.5 Equivalence Relations
#### Equivalence Relations
A relation on a set $A$ is called an **equivalence relation** if it is *reflexive*, *symmetric*, and *transitive*.

Two elements $a$ and $b$ that are related by an equivalence relation are called **equivalent**, which is noted by $a ∼ b$.

<br>

#### Equivalence Classes
**Definition**
Let $R$ be an equivalence relation on a set $A$, then the **equivalence class** of $a$ with respect to $R$ is $$[a]_R = \{s ∣ (a, s) ∈ R\}$$

If $b ∈ [a]_R$, then $b$ is called a **representative** of this equivalence class.

<br>

#### Equivalence Classes and Partitions
**Theorem 1**
Let $R$ be an equivalence relation on a set $A$, then these statements for $a, b \in A$ are equivalent:
$\pod{1}$ $aRb$
$\pod{2}$ $[a] = [b]$
$\pod{3}$ $[a] \cap [b] \neq \emptyset$

<br>

**Definition**
A **partition** of a set $S$ is a collection of disjoint nonempty subsets of $S$ that have $S$ as their union.

$\{A_i | i ∈ I\}$ forms a partition of $S$ if and only if
$\pod{1}$ $\forall i\in I, A_i \neq \emptyset$
$\pod{2}$ $\forall i \neq j, A_i \cap A_j \neq \emptyset$
$\pod{3}$ $\bigcup_{i\in I} A_i = S$

<br>

**Theorem 2**
Let $R$ be an equivalence relation on a set $S$. Then the equivalence classes of $R$ form a partition of $S$.

Conversely, given a partition $\{A_i ∣ i ∈ I\}$ of the set $S$, there is an equivalence relation $R$ that has the sets $A_i, i ∈ I$, as its equivalence classes.









<br>

### 9.6 Partial Orderings
#### Terminology for Partial Ordering
**Definition 1**
A relation $R$ on a set $S$ is called a **partial ordering** or **partial order** if it is *reflexive*, *antisymmetric*, and *transitive*.

A set $S$ together with a partial ordering $R$ is called a **partially ordered set**, or **poset**, which is denoted by $(S, R)$.

> $(Z, \le)$ is a poset.
> $(Z^+, |)$ is a poset.
> $(P(S), \subseteq)$ is a poset.

<br>

**Definition 2**
When $a$ and $b$ are elements of a poset $(S, \preccurlyeq )$ such that either $a \preccurlyeq b$ or $b \preccurlyeq a$, $a$ and $b$ are called **comparable**.
When $a$ and $b$ are elements of $(S, \preccurlyeq )$ such that neither $a \preccurlyeq b$ nor $b \preccurlyeq a$, $a$ and $b$ are called **incomparable**.

<br>

**Definition 3**
If $(S, \preccurlyeq )$ is a poset and every two elements of $S$ are comparable, $S$ is called a **totally ordered** or **linearly ordered set**, and $\preccurlyeq$ is called a **total order** or a **linear order**.

A subset of a poset such that every two elements of this subset are comparable is called a **chain**.
A subset of a poset such that every two elements of this subset are incomparable is called an **antichain**.

<br>

**Definition 4**
$(S, \preccurlyeq )$ is a **well-ordered set** if it is a poset such that $\preccurlyeq$ is a total ordering and every nonempty subset of $S$ has a least element.

<br>

**Theorem 1 : The Principle of Well-ordered Induction**
Suppose that $S$ is a well-ordered set, then $P(x)$ is true for all $x ∈ S$, if
*Inductive Step*: For every $y ∈ S$, if $P(x)$ is true for all $x ∈ S$ with $x ≺ y$, then $P(y)$ is true.

$\texttt{Proof:}$
Suppose it is not the case that $P(x)$ is true for all $x ∈ S$, then there is an element $y ∈ S$ such that $P(y)$ is false. Consequently, the set $A = \{x ∈ S ∣ P(x) \text{ is false}\}$ is nonempty.

Because $S$ is well-ordered, $A$ has a least element $a$. By the choice of $a$ as a least element of $A$, we know that $P(x)$ is true for all $x ∈ S$ with $x \prec a$. This implies by the inductive step $P(a)$ is true.

This contradiction shows that $P(x)$ must be true for all $x ∈ S$.

<br>

#### Lexicographic Order
A **lexicographic ordering** can be defined on the Cartesian product of $n$ posets $(A_1, \preccurlyeq_{1}), (A_2, \preccurlyeq_{2}), … , (A_n, \preccurlyeq_{n})$.
Define the partial ordering $\preccurlyeq$ on $A_1 × A_2 × ⋯ × A_n$ by $$(a_1, a_2, … , a_n) ≺ (b_1, b_2, … , b_n)$$ if $a_1 \prec_{1} b_1$, or if there is an integer $i > 0$ such that $a_1 = b_1, … , a_i = b_i$ and $a_{i+1} \prec_{i+1} b_{i+1}$

<br>

#### Hasse Diagrams
Hasse Diagrams is a method used to represent a partial ordering. The procedure of constructing a Hasse diagram of $(S, \preccurlyeq)$ is:
1. Construct a digraph representation of the poset $(S, \preccurlyeq)$ so that all arcs are pointed upward (except the loops).
2. Eliminate all loops.
3. Eliminate all arcs that are redundant because of transitivity.
4. Eliminate the arrows at the ends of arcs since everything points up.

<br>

#### Maximal and Minimal Elements
$a$ is **maximal** in the poset $(S, \preccurlyeq )$ if there is no $b ∈ S$ such that $a \prec b$.
$a$ is **minimal** in the poset $(S, \preccurlyeq )$ if there is no $b ∈ S$ such that $b \prec a$.

$a$ is the **greatest element** of $(S, \preccurlyeq )$ if $b \preccurlyeq a$ for all $b ∈ S$.
$a$ is the **least element** of $(S, \preccurlyeq )$ if $a \preccurlyeq b$ for all $b ∈ S$.
The greatest and least elements are unique.

<br>

#### Lattice
Let $A$ be a subset of $S$ in the poset $(S, \preccurlyeq)$. If there exists an element $a$ in $S$ such that $b\preccurlyeq a$ for all $b$ in $A$, then $a$ is called an **upper bound** of $A$. 
Similar definition for **lower bounds**.

The element $a$ is called the **least upper bound** of the subset $A$ if $a$ is an upper bound that is less than every other upper bound of $A$, which is denoted by $\text{lub}(A)$.
Similar definition for **greatest lower bounds**, which is denoted by $\text{glb}(A)$.

A poset is called a **lattice** if every pair of elements has a least upper bound and a greatest lower bound.

> $(Z, \le)$ is a lattice.
> $(Z^+, |)$ is a lattice.
> $(P(S), \subseteq)$ is a lattice.

<br>

#### Topological Sorting
A total ordering $\preccurlyeq$ is said to be **compatible** with the partial ordering $R$ if $a \preccurlyeq b$ whenever $aRb$.
Constructing a compatible total ordering from a partial ordering is called **topological sorting**.

**Lemma 1**
Every finite nonempty poset $(S, \preccurlyeq )$ has at least one minimal element.

**Algorithm**
$
\textbf{procedure } \textit{topological sort } ((S, \preccurlyeq )\text{: finite poset}) \\
k := 1 \\
\text{while } S ≠ ∅ \\
\quad a_k := \text{ a minimal element of S \{such an element exists by Lemma 1\}} \\
\quad S := S − {a_k} \\
\quad k := k + 1 \\
\text{return } a_1, a_2,… , a_n \{a_1, a_2,… , a_n \text{ is a compatible total ordering of } S\} \\
$






