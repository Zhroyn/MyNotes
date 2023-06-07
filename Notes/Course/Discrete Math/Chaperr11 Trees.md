<!-- TOC -->

- [Trees](#trees)
  - [11.1 Introduction to Trees](#111-introduction-to-trees)
    - [Terminologies of Trees](#terminologies-of-trees)
    - [Properties of Trees](#properties-of-trees)
  - [11.2 Applications of Trees](#112-applications-of-trees)
    - [Binary Search Trees](#binary-search-trees)
    - [Decision Trees](#decision-trees)
    - [Prefix Codes](#prefix-codes)
  - [11.3 Tree Traversal](#113-tree-traversal)
    - [Traversal Algorithms](#traversal-algorithms)
    - [Infix, Prefix, and Postfix Notation](#infix-prefix-and-postfix-notation)

<!-- /TOC -->







## Trees
### 11.1 Introduction to Trees
#### Terminologies of Trees
**Definition 1**
A **tree** is a connected undirected graph with no simple circuits.

**Forest** is an undirected graph with no simple circuits. Each connected components of forest is a tree. 

<br>

**Theorem 1**
An undirected graph is a tree if and only if there is a **unique** simple path between any two of its vertices.

<br>

**Definition 2**
A **rooted tree** is a tree in which one vertex has been designated as the root and every edge is directed away from the root.

Vertices with the same parent are called **siblings**

The **ancestors of a non-root vertex** are all the vertices in the path from root to this vertex.
The **descendants of vertex $v$** are all the vertices that have $v$ as an ancestor.

A vertex is called a **leaf** if it has no children.
A vertex is called an **internal vertex** if it has children.

The **subtree at vertex $v$** is the subgraph of the tree consisting of vertex $v$ and its descendants and all edges incident to these descendants. 

<br>

**Definition 3**
A rooted tree is called an **m-ary tree** if every internal vertex has no more than $m$ children.
The tree is called a **full m-ary tree** if every internal vertex has exactly $m$ children.
An $m$-ary tree with $m = 2$ is called a **binary tree**.

<br>

#### Properties of Trees
**Theorem 2**
A tree with $n$ vertices has $n − 1$ edges.

**Theorem 3**
A full m-ary tree with $i$ internal vertices contains $n=mi+1$ vertices.

**Theorem 4**
A full m-ary tree with
- $n$ vertices has $i=(n-1)/m$ internal vertices and $l=[(m-1)n+1]/m$ leaves
- $i$ internal vertices has $n=mi+1$ vertices and $l=(m-1)i+1$ leaves
- $l$ leaves has $n=(ml-1)/(m-1)$ vertices and $i=(l-1)/(m-1)$ internal vertices


The **level** of vertex $v$ in a rooted tree is the length of the unique path from the root to $v$. 
The **height** of a rooted tree is the maximum of the levels of its vertices. 
A rooted m-ary tree of height $h$ is called **balanced** if all its leaves are at levels $h$ or $h-1$.

**Theorem 5**
There are at most $m^h$ leaves in an m-ary tree of height $h$.

**Corollary 1**
If an m-ary tree of height $h$ has $l$ leaves, then $h \ge \lceil \log_ml \rceil$. If the m-ary tree is full and balanced, then $h = \lceil \log_m l \rceil$.










<br>

### 11.2 Applications of Trees
#### Binary Search Trees
Vertices are assigned keys so that the key of a vertex is both larger than the keys of all vertices in its left subtree and smaller than the keys of all vertices in its right subtree.

If $U$ has $n$ internal vertices, the height of $U$ is greater than or equal to $h = \lceil \log_2(n+1) \rceil$.

<br>

#### Decision Trees
Rooted trees can be used to model problems in which a series of decisions leads to a solution.

A rooted tree in which each internal vertex corresponds to a decision, with a subtree at these vertices for each possible outcome of the decision, is called a decision tree.

<br>

#### Prefix Codes
To ensure that no bit string corresponds to more than one sequence of letters, the bit string for a letter must never occur as the first part of the bit string for another letter. Codes with this property are called **prefix codes**.

$
\textbf{procedure } Huffman (C: \text{ symbols } a_i \text{ with frequencies } w_i, i = 1, … , n) \\
F := \text{forest of } n \text{ rooted trees, each consisting of the single vertex and } a_i \\
\qquad \text{assigned weight } w_i \\
\textbf{while } F \text{ is not a tree} \\
\qquad \text{Replace the rooted trees } T \text{ and } T' \text{ of least weights from } F \text{ with } w(T) \\
\qquad ≥ w(T') \text{ with a tree having a new root that has } T \text{ as its left subtree} \\
\qquad \text{and } T' \text{ as its right subtree. Label the new edge to } T \text{ with } 0 \text{ and the new} \\
\qquad \text{edge to } T' \text{ with } 1. \\
\qquad \text{Assign } w(T) + w(T') \text{ as the weight of the new tree.} \\
\{\text{the Huffman coding for the symbol } a_i \text{ is the concatenation of he labels of} \\
\text{the edges in the unique path from the root to the vertex } a_i\}
$










<br>

### 11.3 Tree Traversal
#### Traversal Algorithms
Suppose that $T_1, T_2, … , T_n$ are the subtrees at $r$ from left to right, then:
**Preorder Traversal**: $r, T_1, T_2, \cdots, T_n$
**Inorder Traversal**: $T_1, r, T_2, \cdots, T_n$
**Postorder Traversal**: $T_1, T_2, \cdots, T_n, r$

Start at the root and traverse counterclockwise around the tree, while imagining each vertex has $m$ children, then:
In preorder traversal, list a vertex when encounter it at the first time;
In inorder traversal, list a vertex when encounter it at the second time;
In postorder traversal, list a vertex when encounter it at the last time;

<br>

####  Infix, Prefix, and Postfix Notation
A binary expression tree is a special kind of binary tree in which:
1. Each leaf node contains a single operand;
2. Each nonleaf node contains a single operator;
3. The left and right subtrees of an operator node represent subexpressions that must be evaluated before applying the operator at the root of the subtree.

We obtain the **infix form** of an expression when we traverse the binary expression tree in inorder, **prefix form** (Polish notation) when in preorder, **postfix form** (reverse Polish notation) when in postorder.

To evaluate a prefix expression, the steps is to start at the right, and then push when encounter operand, pop when encounter operator.
To evaluate a postfix expression, the steps is to start at the left, and then push when encounter operand, pop when encounter operator.

> For $((x + y) \uparrow 2) + ((x − 4)/3)$,
> The prefix form is $ \uparrow +\; x\; y\; 2\; / − x\; 4\; 3$
> The postfix form is $x\;y + 2 \uparrow x\; 4 − 3\; /\; +$






