<!-- TOC -->

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

<!-- /TOC -->





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

The **degree of a vertex in an undirected graph** is the number of edges incident with it, except that a loop at a vertex contributes twice to the degree of that vertex, which is denoted by $\text{deg}(v)$.
If $\text{deg}(v) = 0$, $v$ is called **isolated**.
If $\text{deg}(v) = 1$, $v$ is called **pendant**.

**Theorem 1**
Let $G = (V, E)$ be an undirected graph with $m$ edges. Then
$$2m = \sum_{v\in V}\text{deg}(v)$$

**Theorem 2**
An undirected graph has an even number of vertices of odd degree.

<br>

#### Terminology for Directed Graph
If $(u, v)\in V$, $u$ is said to be **adjacent to** $v$ and $v$ is said to be **adjacent from** $u$. The vertex $u$ is called the **initial vertex** of $(u, v)$, and $v$ is called the **terminal** or **end vertex** of $(u, v)$.

The **in-degree of a vertex $v$** is the number of edges which terminate at $v$, which is denoted by $\text{deg}^-(v)$.
The **out-degree of a vertex $v$** is the number of edges which initiate at $v$, which is denoted by $\text{deg}^+(v)$.

**Theorem 3**
$$\sum_{v\in V} \text{deg}^-(v) = \sum_{v\in V} \text{deg}^+(v) = |E|$$

<br>

#### Some Special Simple Graphs
**Complete Graph** - $K_n$: A simple graph with $n$ vertices and exactly one edge between every pair of distinct vertices

**Cycle** - $C_n(n \ge 3)$: A simple graph consists of $n$ vertices $v_1, v_2, … , v_n$ and edges $\{v_1, v_2\}, \{v_2, v_3\}, … ,\{v_n, v_1\}$

**Wheel** - $W_n(n \ge 3)$: Add one additional vertex to the $C_n$ and connect this new vertex to each vertex in $C_n$

**$n$-Cube** - $Q_n$: A simple graph that has vertices representing the $2^n$ bit strings of length $n$. Two vertices are adjacent if and only if the bit strings that they represent differ in exactly one bit position.

<br>

#### Bipartite Graphs
A simple graph $G$ is called **bipartite** if $V$ can be partitioned into two disjoint sets $V_1$ and $V_2$ such that every edge connects a vertex in $V_1$ and a vertex in $V_2$ (so that no edge in $G$ connects either two vertices in $V_1$ or two vertices in $V_2$).
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

The **union** of two simple graphs $G_1 = (V_1, E1)$ and $G_2 = (V_2, E2)$ is the simple graph with vertex set $V_1 ∪ V_2$ and edge set $E1 ∪ E2$, which is denoted by $G_1 ∪ G_2$.

> How many subgraphs with at least one vertex does $W_3$ have?
> $= C(4,1) + C(4,2)\times 2 + C(4,3)\times 2^3 + C(4,4)\times 2^6 \\ = 128 $





