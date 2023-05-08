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

<!-- /TOC -->






## Relations
### 9.1 Relations and Their Properties
- Let A and B be sets. A **binary relation from $A$ to $B$** is a subset of $A × B$.
- We use the notation $aRb$ to denote that $(a, b) ∈ R$ and $a \cancel{R} b$ to denote that $(a, b) ∉ R$.
- Moreover, when $(a, b)$ belongs to $R$, $a$ is said to be **related to** $b$ by $R$.
- A **relation on a set $A$** is a relation from $A$ to $A$.

#### Properties of Binary Relations
- A relation $R$ on a set $A$ is called **reflexive** if $(a, a) ∈ R$ for every element $a ∈ A$.
- A relation $R$ on a set $A$ is called **symmetric** if for all $a, b ∈ A$, $(b, a) ∈ R$ whenever $(a, b) ∈ R$.
- A relation $R$ on a set $A$ is called **antisymmetric** if for all $a, b ∈ A$, if $(a, b) ∈ R$ and $(b, a) ∈ R$, then $a = b$.
- A relation $R$ on a set $A$ is called **transitive** if for all $a, b ∈ A$, if $(a, b) ∈ R$ and $(b, c) ∈ R$, then $ (a, c) ∈ R$.
<br>

#### Combining Relations
- Two relations from A to B can be combined in any way two sets can be combined, such as $R_1 ∪ R_2, R_1 ∩ R_2, R_1 ⊕ R_2, R_1 − R_2, R_2 − R_1$.
- Let $R$ be a relation from $A$ to $B$, and $S$ a relation from $B$ to $C$. The **composite** of $R$ and $S$ is the relation consisting of ordered pairs $(a, c)$, where $a ∈ A, c ∈ C$, and $\exists b ∈ B, (a, b) ∈ R, (b, c) ∈ S$. We denote the composite of $R$ and $S$ by $S \circ R$.
- Let $R$ be a relation on the set $A$. The powers $R^n, n = 1, 2, 3, …$ , are defined recursively by $$R^1 = R, R^{n+1} = R^n \circ R $$
  - A relation $R$ on a set $A$ is transitive if and only if $R^n \subseteq R$ for $n = 1, 2, 3, …$
<br>

- $M_{R_1 \cup R_2} = [c_{ij} \vee d_{ij}] = M_{R_1} \vee M_{R_2} $
- $M_{R_1 \cap R_2} = [c_{ij} \land d_{ij}] = M_{R_1} \land M_{R_2} $
- $M_{\bar{R}_1} = [\bar{c}_{ij}] $
- $M_{R_1 - R_2} = [c_{ij} \land \bar{d}_{ij}] = M_{R_1 \land \bar{R}_2} $
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






### 9.2 n-ary Relations and Their Applications
- Let $A_1, A_2, … , A_n$ be sets. An **n-ary relation** on these sets is a subset of $A1 × A2 × ⋯ × An$.
- The sets $A_1, A_2, … , A_n$ are called the **domains** of the relation, and $n$ is called its **degree**.
<br>

- Let $R$ be an n-ary relation and $C$ a condition that elements in $R$ may satisfy. Then the **selection operator** $s_C$ maps the n-ary relation R to the n-ary relation of all n-tuples from $R$ that satisfy the condition $C$.
- The **projection** $P_{i_1i_2,…,i_m}$ where $i_1 < i_2 < ⋯ < i_m$, maps the n-tuple $(a_1, a_2, … , a_n)$ to the m-tuple $(a_{i1}, a_{i2}, … , a_{im} )$, where $m ≤ n$.
- Let $R$ be a relation of degree $m$ and $S$ a relation of degree $n$. The **join** $J_p(R, S)$, where $p ≤ m$ and $p ≤ n$, is a relation of degree $m + n − p$ that consists of all (m + n − p)-tuples $(a_1, a_2, … , a_{m−p}, c_1, c_2, … , c_p, b_1, b_2, … , b_{n−p})$, where the m-tuple $(a_1, a_2, … , a_{m−p}, c_1, c_2, … , c_p)$ belongs to $R$ and the n-tuple $(c_1, c_2, … , c_p, b_1, b_2, … , b_{n−p})$ belongs to $S$.






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

- A **directed graph**, or **digraph**, consists of a set $V$ of *vertices* (or *nodes*) together with a set $E$ of ordered pairs of elements of $V$ called *edges* (or *arcs*). The vertex $a$ is called the *initial vertex* of the edge $(a, b)$, and the vertex $b$ is called the *terminal vertex* of this edge.
- An edge of the form $(a, a)$ is called a **loop**.







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

#### Transitive Closures
- The **connectivity relation** $R^∗$ consists of the pairs $(a, b)$ such that there is a path of length at least one from $a$ to $b$ in $R$, that is $$R^* = \bigcup_{n=0}^{\infty} R^n $$
<br>

- The transitive closure of $R$ is $t(R) = R^∗$.
- When $a ≠ b$, if there is a path of length at least one in $R$ from $a$ to $b$, then there is such a path with length not exceeding $n − 1$.
- If $|A| = n$, then any path of length $> n$ must contain a cycle.
- If $|A| = n$, then $t(R) = R^* = R \cup R^2 \cup \cdots \cup R^n $.
- Let $M_R$ be the zero–one matrix of the relation $R$ on a set with $n$ elements, then $$M_{R^∗} = M_R ∨ M^{[2]}_R ∨ M^{[3]}_R ∨ ⋯ ∨ M^{[n]}_R$$

$\text{procedure } transitive \; closure (M_R : \text{zero–one } n × n \text{ matrix}) \\
A := M_R \\
B := A \\
\text{for } i := 2 \text{ to } n \\
\quad A := A ⊙ M_R \\
\quad B := B ∨ A \\
\text{return } B\{B \text{ is the zero–one matrix for } R^∗\}$

This algorithm uses $n^2(2n−1)(n−1) + (n−1)n^2 = 2n^3(n−1)$, which is $O(n^4)$ bit operations

#### Warshall’s Algorithm
- Warshall’s algorithm is an efficient method for computing the transitive closure of a relation, using only $2n^3$ bit operations.
<br>

- If $a, x_1, x_2, … , x_{m−1}, b$ is a path, then its **interior vertices** are $x_1, x_2, … , x_{m−1}$
- $W_0 = M_R, W_n = M_{R^∗}$, and $W_k =[w^{(k)}_{ij}]$, where $w^{(k)}_{ij} = 1$ if there is a path from $v_i$ to $v_j$ such that all the interior vertices of this path are in the set $\{v_1, v_2, … , v_k\}$ and is $0$ otherwise.
- There is a path from $v_i$ to $v_j$ with no vertices other than $v_1, v_2, … , v_k$ as interior vertices if and only if either there is a path from $v_i$ to $v_j$ with its interior vertices among the first $k − 1$ vertices in the list, or there are paths from $v_i$ to $v_k$ and from $v_k$ to $v_j$ that have interior vertices only among the first $k − 1$ vertices in the list. So $$w^{[k]}_{ij} = w^{[k−1]}_{ij} ∨ (w^{[k−1]}_{ik} ∧ w^{[k−1]}_{kj} )$$



