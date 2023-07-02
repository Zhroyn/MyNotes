
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Graphs](#graphs)
  - [10.1 Graphs and Graph Models](#101-graphs-and-graph-models)
    - [Undirected Graph](#undirected-graph)
    - [Directed Graph](#directed-graph)
  - [10.2 Graph Terminology and Special Types of Graphs](#102-graph-terminology-and-special-types-of-graphs)
    - [Terminology for Undirected Graph](#terminology-for-undirected-graph)
    - [Terminology for Directed Graph](#terminology-for-directed-graph)
    - [Some Special Simple Graphs](#some-special-simple-graphs)
    - [Bipartite Graphs](#bipartite-graphs)
    - [New Graphs from Old](#new-graphs-from-old)
  - [10.3 Representing Graphs and Graph Isomorphism](#103-representing-graphs-and-graph-isomorphism)
    - [Representing Graphs](#representing-graphs)
    - [Isomorphism of Graphs](#isomorphism-of-graphs)
  - [10.4 Connectivity](#104-connectivity)
    - [Paths](#paths)
    - [Connectedness in Undirected Graphs](#connectedness-in-undirected-graphs)
    - [Connectedness in Directed Graphs](#connectedness-in-directed-graphs)
  - [10.5 Euler and Hamilton Paths](#105-euler-and-hamilton-paths)
    - [Euler Paths and Circuits](#euler-paths-and-circuits)
    - [Hamilton Paths and Circuits](#hamilton-paths-and-circuits)
  - [10.6 Shortest-Path Problems](#106-shortest-path-problems)
  - [10.7 Planar Graphs](#107-planar-graphs)
    - [Euler's Formula](#eulers-formula)
    - [Kuratowski’s Theorem](#kuratowskis-theorem)
  - [10.8 Graph Coloring](#108-graph-coloring)
  - [Network Flow](#network-flow)
    - [Max Flow Problem](#max-flow-problem)
    - [Max-Flow Min-cut Theorem](#max-flow-min-cut-theorem)
    - [Residual Graph](#residual-graph)
    - [Augmenting Path Algorithm](#augmenting-path-algorithm)
    - [Ford-Fulkerson Algorithm](#ford-fulkerson-algorithm)

<!-- /code_chunk_output -->









## Graphs
### 10.1 Graphs and Graph Models
#### Undirected Graph
**Definition 1**
A graph $G = (V, E)$ consists of $V$, a nonempty set of **vertices** (or **nodes**) and $E$, a set of **edges**.
Each edge has either one or two vertices associated with it, called its **endpoints**. An edge is said to **connect** its endpoints.

**Simple graph**: Undirected, No Multiple Edges, No Loops.
**Multigraph**: Undirected, Multiple Edges Allowed, No Loops.
**Pseudograph**: Undirected, Multiple Edges Allowed, Loops Allowed.

<br>

#### Directed Graph
**Definition 2**
A **directed graph** (or **digraph**) $(V, E)$ consists of a nonempty set of vertices $V$ and a set of **directed edges** (or **arcs**) $E$.
The directed edge associated with the ordered pair $(u, v)$ is said to **start** at $u$ and **end** at $v$.

**Simple directed graph**: Directed, No Multiple Edges, No Loops.
**Directed graph**: Directed, No Multiple Edges, Loops Allowed.
**Directed multigraph**: Directed, Multiple Edges Allowed, Loops Allowed.
**Mixed graph**: Directed and undirected, Multiple Edges Allowed, Loops Allowed.








<br>

### 10.2 Graph Terminology and Special Types of Graphs
#### Terminology for Undirected Graph
If $(u, v)\in V$, $u$ and $v$ called **adjacent** (or **neighbors**).
An edge $e$ connecting $u$ and $v$ is called **incident with the vertices $u$ and $v$**.

The set of all neighbors of a vertex $v$ is called the **neighborhood** of $v$, which is denoted by $N(v)$,.
$N(A) = \bigcup_{v\in A}N(v)$, where $A$ is a subset of $V$.

The **degree of a vertex in an undirected graph** is the number of edges incident with it, except that a loop at a vertex contributes twice to the degree of that vertex, which is denoted by $\deg(v)$.
If $\deg(v) = 0$, $v$ is called **isolated**.
If $\deg(v) = 1$, $v$ is called **pendant**.

**Theorem 1**
Let $G = (V, E)$ be an undirected graph with $m$ edges. Then
$$2m = \sum_{v\in V}\deg(v)$$

**Theorem 2**
An undirected graph has an even number of vertices of odd degree.

<br>

#### Terminology for Directed Graph
If $(u, v)\in V$, $u$ is said to be **adjacent to** $v$ and $v$ is said to be **adjacent from** $u$. The vertex $u$ is called the **initial vertex** of $(u, v)$, and $v$ is called the **terminal** or **end vertex** of $(u, v)$.

The **in-degree of a vertex $v$** is the number of edges which terminate at $v$, which is denoted by $\deg^-(v)$.
The **out-degree of a vertex $v$** is the number of edges which initiate at $v$, which is denoted by $\deg^+(v)$.

**Theorem 3**
$$\sum_{v\in V} \deg^-(v) = \sum_{v\in V} \deg^+(v) = |E|$$

<br>

#### Some Special Simple Graphs
**Complete Graph** - $K_n$: A simple graph with $n$ vertices and exactly one edge between every pair of distinct vertices

**Cycle** - $C_n(n \ge 3)$: A simple graph consists of $n$ vertices $v_1, v_2, … , v_n$ and edges $\{v_1, v_2\}, \{v_2, v_3\}, … ,\{v_n, v_1\}$

**Wheel** - $W_n(n \ge 3)$: Add one additional vertex to the $C_n$ and connect this new vertex to each vertex in $C_n$

**$n$-Cube** - $Q_n$: A simple graph that has vertices representing the $2^n$ bit strings of length $n$. Two vertices are adjacent if and only if the bit strings that they represent differ in exactly one bit position.

<br>

#### Bipartite Graphs
A simple graph $G$ is called **bipartite** if $V$ can be partitioned into two disjoint sets $V_1$ and $V_2$ such that every edge connects a vertex in $V_1$ and a vertex in $V_2$ (so that no edge connects either two vertices in $V_1$ or two vertices in $V_2$).
When this condition holds, we call the pair $(V_1, V_2)$ a **bipartition**.

A **complete bipartite graph** is a bipartite graph that every vertex in $V_1$ is connected to every vertex in $V_2$, which is denoted by $K_{m,n}$, where $m = |V_1|, n = |V_2|$.

A **regular graph** is a simple graph that every vertex of this graph has the same degree.
A regular graph is called **$n$-regular** if the degree for every vertex is $n$.

<br>

#### New Graphs from Old
For $G = (V, E)$, $H = (W, F)$,
$H$ is a **subgraph** of $G$ if $W \subseteq V, F \subseteq E$.
$H$ is a **proper subgraph** of $G$ if $H \neq G$.
$H$ is a **spanning subgraph** of $G$ if $W = V, F \subseteq E$.

The **union** of two simple graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ is the simple graph with vertex set $V_1 ∪ V_2$ and edge set $E_1 ∪ E_2$, which is denoted by $G_1 ∪ G_2$.

> How many subgraphs with at least one vertex does $W_3$ have?
> $= C(4,1) + C(4,2)\times 2 + C(4,3)\times 2^3 + C(4,4)\times 2^6 \\ = 128 $








<br>

### 10.3 Representing Graphs and Graph Isomorphism
#### Representing Graphs
**Adjacency Lists**
For undirected graph, firstly, list a column for all verteices as *Vertex*, and then write down their corresponding neighbors as *Adjacent Vertices*.
For directed graph, firstly, list a column for all verteices as *Inital Vertex*, and then write down their corresponding end vertices as *Terminal Vertex*.

**Adjacency Matrices**
$$
A = [a_{ij}], \quad
a_{ij} = \begin{cases}
  1 & \text{if } (v_i, v_j) \in V \\
  0 & \text{otherwise}
\end{cases}
$$

To represent multiple edges, we can use matrices of nonnegative integers.
For a undirected graph, the sum of $n$th row or column is the number of edges incident to the $n$th vertex, which is the same as degree minus the number of loops.
For a directed graph, the sum of $n$th row is the out-degree of the $n$th vertex.
For a directed graph, the sum of $n$th column is the in-degree of the $n$th vertex.

**Incidence Matrices**
$$
M = [m_{ij}], \quad
m_{ij} = \begin{cases}
  1 & \text{if edge } e_j \text{ is incident with } v_i \\
  0 & \text{otherwise}
\end{cases}
$$

<br>

#### Isomorphism of Graphs
The simple graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are **isomorphic** if there exists a one-to-one and onto function $f$ from $V_1$ to $V_2$ with the property that $a$ and $b$ are adjacent in $G_1$ if and only if $f(a)$ and $f(b)$ are adjacent in $G_2$, for all $a$ and $b$ in $V_1$.
Such a function f is called an **isomorphism**.
Two simple graphs that are not isomorphic are called **nonisomorphic**.

To proof $G$ and $H$ are isomorphic:
1. Find a one-to-one and onto function $f$
2. Show that $A_G = A_H$ with the rows and columns of the adjacency matrix of $H$ labeled by the images of the corresponding vertices in $G$








<br>

### 10.4 Connectivity
#### Paths
A **path of length $n(n\ge 0)$** in a *undirected graph* is a sequence of vertices $v_0, v_1, . . . , v_n$ such that $\{v_0, v_1\} , \{v_1, v_2\} , ..., \{v_{n-1}, v_n\}$ are $n$ edges in the graph.
The path is a **circuit** if it begins and ends at the same vertex with length greater than zero.
A path is **simple** if it does not contain the same edge more than once.

A **path of length $n(n\ge 0)$** in a *directed graph* is a sequence of vertices $v_0, v_1, . . . , v_n$ such that $(v_0, v_1) , (v_1, v_2) , ..., (v_{n-1}, v_n)$ are $n$ directed edges in the graph.
The path is a **circuit** or **cycle** if it begins and ends at the same vertex with length greater than zero.

**Theorem 2**
The number of different paths of length $r$ from $v_i$ to $v_j$ is equal to the $(i, j)$th entry of $A^r$, where $A$ is the adjacency matrix representing the graph consisting of vertices $v_1, v_2,\cdots, v_n$.

To proof a graph is connected, show that in one matrix of $A, \cdots, A^{n-1}$, every off-diagonal entry is nonzero.
To proof a graph is disconnected, show that in $A + \cdots + A^{n-1}$, there exists at least one zero off-diagonal entry.

<br>

#### Connectedness in Undirected Graphs
An undirected graph is called **connected** if there is a path between every pair of distinct vertices of the graph.

**Theorem 1**
There is a simple path between every pair of distinct vertices of a connected undirected graph.

The maximal connected subgraphs of $G$ are called the **connected components** or just the **components**. A graph $G$ that is not connected has two or more connected components that are disjoint and have $G$ as their union.
A vertex is called a **cut vertex** or **articulation point**, if removing it and all edges incident with it results in more connected components than in the original graph.
Similarly, an edge is called a **cut edge** or **bridge** if removing it results in more components.

<br>

#### Connectedness in Directed Graphs
A directed graph is **strongly connected** if there is a path from $a$ to $b$ and from $b$ to $a$ for all vertices $a$ and $b$ in the graph.  
A directed graph is **weakly connected** if the underlying undirected graph is connected.

For directed graph, the maximal strongly connected subgraphs are called the **strongly connected components** or just the **strong components**.









<br>

### 10.5 Euler and Hamilton Paths
#### Euler Paths and Circuits
An **Euler path** is a simple path containing every edge of $G$.
An **Euler circuit** is a simple circuit containing every edge of $G$.
An **Euler graph** is a graph contains an Euler circuit.

**Theorem 1**
A connected multigraph has an Euler circuit if and only if each of its vertices has even degree.
- Necessary Condition: The circuit contributes one to $\deg(a)$ when it begins at $a$, another one when it ends at $a$. And each time the circuit passes through a vertex, it contributes two to its degree. So for every vertex $v$, $\deg(v)$ must be even.
- Sufficient Condition: 
  First, we arbitrarily choose an edge incident with $a$ which is possible because $G$ is connected. Thus, we can build a simple path $x_0=a, x_1, … , x_n$ by successively adding edges one by one to the path, until we cannot add any more.
  Where we terminate must be $a$, because we can leave every vertex other than $a$ due to their even degree.
  Continue this process until all edges have been used, and then splice all the circuits we constuct.

**Theorem 2**
A connected multigraph has an Euler path but not an Euler circuit if and only if it has exactly two vertices of odd degree. (Consider the larger graph made up of the original graph with an additional edge $\{a, b\}$)

**Theorem for Directed Graph**
A directed multigraph has an Euler circuit if and only if 
  -  the graph is weakly connected 
  -  the in-degree and out-degree of each vertex are equal.

A directed multigraph has an Euler path but not an Euler circuit if and only if 
  -  the graph is weakly connected 
  -  the in-degree and out-degree of each vertex are equal for all but two vertices, one that has in-degree 1 larger than its out-degree and the other that has out-degree 1 larger than its in-degree. 

<br>

#### Hamilton Paths and Circuits
A **Hamilton path** is a simple path that passes through every vertex in $G$ exactly once.
A **Hamilton circuit** is a simple circuit that passes through every vertex in $G$ exactly once except for the first vertex.
A **Hamilton graph** is a graph contains an Hamilton circuit.

**Theorem 3: Dirac's Theorem**
If $G$ is a simple graph with $n$ vertices with $n\ge 3$ such that the degree of every vertex in $G$ is at least $n/2$, then $G$ has a Hamilton circuit. 

**Theorem 4: Ore's Theorem**
If $G$ is a simple graph with $n$ vertices with $n\ge 3$ such that
$\deg(u) + \deg(v) \ge n$ for every pair of nonadjacent vertices 
$u$ and $v$ in $G$, then $G$ has a Hamilton circuit.









<br>

### 10.6 Shortest-Path Problems
$
\textbf{procedure } Dijkstra (G: \text{weighted connected simple graph, with} \\
\qquad \text{all weights positive}) \\
\{G \text{ has vertices } a = v_0, v_1,… , v_n = z \text{ and lengths } w(v_i, v_j) \\
\qquad\text{where } w(v_i, v_j) = ∞ \text{ if } {v_i, v_j} \text{ is not an edge in } G\} \\
\text{for } i := 1 \text{ to } n \\
\qquad L(v_i) := ∞ \\
L(a) := 0 \\
S := ∅ \\
\text{while } z ∉ S \\
\qquad u := \text{a vertex not in } S \text{ with } L(u) \text{ minimal} \\
\qquad S := S ∪ {u} \\
\qquad \text{for all vertices } v \text{ not in } S \\
\qquad \qquad \text{if } L(u) + w(u, v) < L(v) \text{ then } L(v) := L(u) + w(u, v) \\
\text{return } L(z) \; \{L(z) = \text{length of a shortest path from } a \text{ to } z\}
$

**Theorem 1**
Dijkstra’s algorithm finds the length of a shortest path between two vertices in a connected simple undirected weighted graph.

**Theorem 2**
Dijkstra’s algorithm uses $O(n^2)$ operations (additions and comparisons) to find the length of a shortest path between two vertices in a connected simple undirected weighted graph with $n$ vertices.









<br>

### 10.7 Planar Graphs
A graph is called **planar** if it can be drawn in the plane without any edges crossing.
Such a drawing is called a **planar representation** of the graph.

<br>

#### Euler's Formula
**Theorem 1**
Let $G$ be a connected planar simple graph with $e$ edges and $v$ vertices. Let $r$ be the number of regions in a planar epresentation of $G$. Then $r = e − v + 2$.

$\texttt{Proof:}$ Use induction.

<br>

**Corollary 1**
If $G$ is a connected planar simple graph with $e$ edges and $v$ vertices, where $v ≥ 3$, then $e ≤ 3v − 6$.

$\texttt{Proof:}$
$$
2e = \sum_i \deg(R_i) \ge 3r = 3e - 3v + 6 \\~\\
\Rightarrow e \le 3v - 6
$$

<br>

**Corollary 2**
If $G$ is a connected planar simple graph, then $G$ has a vertex of degree not exceeding five.

$\texttt{Proof:}$
If the degree of every vertex were at least six, then $$2e = \sum_i \deg(v_i) \ge 6v$$

This contradicts the inequality $2e ≤ 6v − 12$. So there must be a vertex with degree no greater than five.

<br>

**Corollary 3**
If a connected planar simple graph has $e$ edges and $v$ vertices with $v ≥ 3$ and no circuits of length three, then $e ≤ 2v − 4$.

$\texttt{Proof:}$ The same as Corollary 1.

<br>

#### Kuratowski’s Theorem
**Theorem 2**
A graph is nonplanar if and only if it contains a subgraph homeomorphic to $K_{3,3}$ or $K_5$.









<br>

### 10.8 Graph Coloring
**Definition 1**
A **coloring** of a simple graph is the assignment of a color to each vertex of the graph so that no two adjacent vertices are assigned the same color.

**Definition 2**
The **chromatic number** of a graph is the least number of colors needed for a coloring of this graph, which is denoted by $\chi(G)$.

$$
\begin{cases}
  \chi(C_n) = 2 & \text{if } n \text{ is even} \\
  \chi(C_n) = 3 & \text{if } n \text{ is odd} \\
\end{cases} 
\\~\\
\chi(K_n) = n
\\~\\
\chi(K_{m,n}) = 2
$$

**The Four Color Theorem**
The chromatic number of a planar graph is no greater than four.

<br>

The general procedures to find the chromatic number are:
1. Let the vertices of a graph represent the element, and then draw an edge between two vertices if the two elements cannot be connected.
2. Compute the complementary graph.
3. Align a color to a vertex if it is connected to all vertices with this color in the complementary graph.











<br>

### Network Flow
#### Max Flow Problem
A s-t flow is a function that satisfies
$$
\forall e\in E, 0 \le f(e) \le c(e) \\~\\
\forall v\in V, \underset{e \text{ in to } v}{\sum}f(e) = \underset{e \text{ out of } v}{\sum}f(e) \\~\\
$$

The value of the flow $f$ is $$v(f) = \underset{e \text{ out of } s}{\sum}f(e)$$

The max flow problem is to find the s-t flow of maximum value.

<br>

#### Max-Flow Min-cut Theorem
A s-t cut is a partition $(S, T)$ of $V$ with $s\in S$ and $t\in T$. Define the capacity of a cut $(S, T)$ as $$\text{cap}(S, T) = \underset{e \text{ out of } S}{\sum} c(e)$$

We can easily get
$$
v(f) = \underset{e \text{ out of } S}{\sum} f(e) - \underset{e \text{ in to } S}{\sum} f(e) \\~\\
v(f) \le \text{cap}(S, T)
$$

**Max-Flow Min-cut Theorem**
Let $f$ be any flow, and let $(S, T)$ be any cut. If $v(f) = \text{cap}(A, B)$, then $f$ is a max flow and $(S, T)$ is a min cut.

<br>

#### Residual Graph
Given a flow graph $G$, then we can get the residual graph $G_R$ by for every $e \in E$ from $u$ to $v$,
adding edge $e'$ from $u$ to $v$ with capacity $c - f$
adding edge $e''$ from $v$ to $u$ with capacity $f$

Set residual capacity as 
$$
c_f(e) = \begin{cases}
  c(e) - f(e) & \text{if } e \in E \\
  f(e) & \text{if } e^R \in E \\
\end{cases}
$$

Then set $G_f = (V, E_f)$ as a residual graph with residual edges having positive residual capacity, that is, $E_f = \{e : f(e) < c(e)\} \cup \{e_R : f(e) > 0\}$.

<br>

#### Augmenting Path Algorithm
An augmenting path is a path with $v_1 = s,  v_k = t$, and for each edge $e$ in the path, there are $c_f(e) > 0$.

$
\textbf{procedure } Augement \; (f : \text{flow}, P : \text{augment path}) \\
b = \underset{e\in P}{\min}\; c_f(e) \\
\text{for each } e \in P \\
\qquad \text{if } e \in E \text{ then } f(e) = f(e) + b \\
\qquad \text{else } f(e^R) = f(e^R) - b \\
\text{return } f \; \{f \text{ is the flow with the path } P \text{ augmented}\}
$

**Augmenting Path Theorem**
Flow $f$ is a max flow iff there are no augmenting paths.

<br>

#### Ford-Fulkerson Algorithm
$
\textbf{procedure } Ford-Fulkerson \; (G : \text{flow graph}) \\
\text{for each } e \in P \\
\qquad f(e) = 0 \\
G_f = \text{the residual graph of } G \\
\text{while there exists augmenting path } P \\
\qquad f = Augment(f, P) \\
\qquad \text{update } G_f \\
\text{return } f \; \{f \text{ is the flow with max flow}\}
$

