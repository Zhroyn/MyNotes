<!-- TOC -->

- [Graphs](#graphs)
  - [10.1 Graphs and Graph Models](#101-graphs-and-graph-models)
  - [10.2 Graph Terminology and Special Types of Graphs](#102-graph-terminology-and-special-types-of-graphs)

<!-- /TOC -->





## Graphs
### 10.1 Graphs and Graph Models
**Definition 1**
A graph $G = (V, E)$ consists of $V$, a nonempty set of **vertices** (or **nodes**) and $E$, a set of **edges**.
Each edge has either one or two vertices associated with it, called its **endpoints**. An edge is said to **connect** its endpoints.

**Simple graph**: Undirected, No Multiple Edges, No Loops.
**Multigraph**: Undirected, Multiple Edges Allowed, No Loops.
**Pseudograph**: Undirected, Multiple Edges Allowed, Loops Allowed.

**Definition 2**
A **directed graph** (or **digraph**) $(V, E)$ consists of a nonempty set of vertices $V$ and a set of **directed edges** (or **arcs**) $E$. Each directed edge is associated with an ordered pair of vertices.
The directed edge associated with the ordered pair $(u, v)$ is said to **start** at $u$ and **end** at $v$.

**Simple directed graph**: Directed, No Multiple Edges, No Loops.
**Directed multigraph**: Directed, Multiple Edges Allowed, Loops Allowed.
**Mixed graph**: Directed and undirected, Multiple Edges Allowed, Loops Allowed.





<br>

### 10.2 Graph Terminology and Special Types of Graphs
Two vertices $u$ and $v$ in an undirected graph $G$ are called **adjacent** (or **neighbors**) in $G$ if $u$ and $v$ are endpoints of an edge $e$ of $G$.
An edge $e$ connecting $u$ and $v$ is called **incident with the vertices $u$ and $v$**.

The set of all neighbors of a vertex $v$, denoted by $N(v)$, is called the **neighborhood** of $v$.
$N(A) = \bigcup_{v\in A}N(v)$, where $A$ is a subset of $V$.

The **degree of a vertex in an undirected graph** is the number of edges incident with it, except that a loop at a vertex contributes twice to the degree of that vertex, which is denoted by $\text{deg}(v)$.
If $\text{deg}(v) = 0$, $v$ is called **isolated**.
If $\text{deg}(v) = 1$, $v$ is called **pendant**.

