
- [数据结构基础笔记](#数据结构基础笔记)
    - [Algorithm Analysis](#algorithm-analysis)
    - [List](#list)
    - [Tree](#tree)
        - [Binary Search Tree](#binary-search-tree)
        - [Heap](#heap)
        - [Union-Find Set](#union-find-set)
    - [Graph](#graph)
    - [Sorting](#sorting)
    - [Hashing](#hashing)




# 数据结构基础笔记

## Algorithm Analysis

All algorithms must satisfy the following criteria:

- **Input**: Zero or more quantities are externally supplied
- **Output**: One or more quantities is produced
- **Definiteness**: Each instruction is clear and unambiguous
- **Finiteness**: If we trace out the instructions of an algorithm, then for all cases, the algorithm terminates after finite number of steps. On the contrary, A **program** does not have to be finite
- **Effectiveness**: Every instruction must be basic enough to be carried out, in principle, by a person using only pencil and paper. It is not enough that each operation be definite, it also must be feasible

---

- $T(N) = o(p(N))$ if $T(N) = O(N)$ and $T(N) \neq \Theta(p(N))$
- $\log N = O(N^a)$, $\log^k N = O(N)$

---

- The time complexity of the function which calculates the Fibonacci number $F_N$ recursively is $O(2^n)$
- The space complexity of the function which calculates the Fibonacci number $F_N$ recursively is $O(n)$
- In fact, $\left( \dfrac{3}{2} \right)^N \le \text{Fib}(N) \le \left( \dfrac{5}{3} \right)^N$








<br>

## List

- For a sequentially stored **linear list** of length $N$, the time complexities for deleting the first element and inserting the last element are $O(N)$ and $O(1)$, respectively.







<br>

## Tree

- Level(root) = 1, Depth(root) = 0, Height(leaf) = 0
- There exists a binary tree with 2016 nodes in total, and with 16 nodes having only one child. (False)
- Given a tree of degree 3. Suppose that there are 3 nodes of degree 2 and 2 nodes of degree 3. Then the number of leaf nodes must be \____. (8)
    - The number of leaf nodes is $\sum_{k = 2}^{\text{degree}} (k - 1) n_k$
- If a general tree $T$ is converted into a binary tree $BT$, then which of the following $BT$ traversals gives the same sequence as that of the post-order traversal of $T$? (In-order traversal, first visit the FirstChild, then itself, then the NextSibling)
    - Rotate the FirstChild-NextSibling tree clockwise by $45\degree$, then it can look like a binary tree.
- In the threaded binary trees, all lchilds in the empty pointer domain will be changed to point to their predecessor nodes, all rchilds in the empty pointer domain will be changed to point to their successor nodes.


<br>

### Binary Search Tree

- A skewed binary tree is a binary tree in which all nodes have only one child with the same direction.
- In a binary search tree which contains several integer keys including 4, 5, and 6, if 4 and 6 are on the same level, then 5 must be their parent. (False, can be their farther ancestor).
- If a binary search tree is complete, the minimum key must be at a leaf node, but the maximum key may not be at a leaf node.
- The decision tree for binary search is a binary search tree. Its root is (left + right) / 2, meaning the first index to be checked. To determine whether a binary tree is such a valid decision tree, we can firstly fill in the tree with the index from 1 to n, then determine whether all decisions are rounded up or down equally.
- Given a pre-order traversal sequence {1, 2, 3, 4}, and a post-order traversal sequence {3, 2, 4, 1}, the in-order traversal sequence cannot be determined.


<br>

### Heap

- A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
- The number of nodes in a complete binary tree of height $h$ is between $2^h$ and $2^{h+1} - 1$. The number of nodes in the last level is between $1$ and $2^h$.
- In a complete binary tree with 1238 nodes, there must be \____ leaf nodes. (215 + 404 = 619)
- If root at 1, then the left child of node $i$ is $2i$, and the right child of node $i$ is $2i + 1$, and the parent of node $i$ is $\lfloor i / 2 \rfloor$.
- If root at 0, then the left child of node $i$ is $2i + 1$, and the right child of node $i$ is $2i + 2$, and the parent of node $i$ is $\lfloor (i - 1) / 2 \rfloor$.
- Use the linear algorithm to adjust max-heap into a min-heap, is to adjust the array from the last non-leaf node to the root node by percolaing down. The time complexity is $O(N)$.


<br>

### Union-Find Set

- Let $T$ be a tree created by union-by-size with $N$ nodes, then $\text{height}(T) \le \lfloor \log_2 N \rfloor + 1$. So the time complexity of $N$ Union and $M$ Find operations is now $O(N + M \log_2 N)$.



- $T(M, N)$ is $\log^* N$, $\log^* N$ is the times the logarithm is applied to $N$ until the result is no greater than 1.






<br>

## Graph

- Length of a path is number of edges on the path.
- Simple path is a path with no repeated vertices.
- Connected component of an undirected $G$ is the maximal connected subgraph.
- A directed acyclic gragh (DAG) must be a tree. (False, one node can have multiple parents)
- A graph with 90 vertices and 20 edges must have at least __ connected component(s). (70, note that it's least)

---

- AOV (Activity On Vertex) Network is a digraph $G$ in which $V(G)$ represents activities and $E(G)$ represents precedence relations.
- $i$ is a predecessor of $j$ if there is a path from $i$ to $j$.
- $i$ is a immediate predecessor of $j$ if $\left\langle i, j \right\rangle \in E(G)$.
- A topological order is a linear ordering of the vertices of a graph such that, for any two vertices $i$ and $j$, if $i$ is a predecessor of $j$ in the network then $i$ precedes $j$ in the linear ordering.
- Partial order is a precedence relation which is both transitive and irreflexive. (True, in the context of topological sorting)
- Topological sorting method can be used to check if there is a cycle in a given directed graph. (True)
- There must be no topological order in a directed graph with a cycle. (True)
- Apply DFS to a directed acyclic graph, and output the vertex before the end of each recursion. The output sequence will be \____. (reversely topologically sorted)

---

- AOE (Activity On Edge) Network is a digraph $G$ in which $E(G)$ represents activities and $V(G)$ represents signals of the completion of activities.
- Earliest completion time: $EC[w] = \max_{(v, w) \in E} \{ EC[v] + C_{v, w} \}$
- Latest completion time: $LC[v] = \min_{(v, w) \in E} \{ LC[w] - C_{v, w} \}$
- Slack time: $S_{v, w} = LC[w] - EC[v] - C_{v, w}$
- Critical path is a path consisting entirely of zero-slack edges.

---

- Dijkstra algorithm does not work for a graph with negative edges. If simply scan the table to find the smallest distance, the time complexity is $O(V^2 + E)$, which is good if the graph is dense. If using a priority queue, the time complexity is $O((V + E) \log V) = O(E\log V)$, which is good if the graph is sparse.
- SPFA algorithm can work for a graph with negative edges, but not for a graph with negative cycles. The time complexity is $O(VE)$.

---

- Prim's algorithm: grow a tree by selecting the minimum weight edge that is connected to $T$ and does not form a loop after adding it. The time complexity is $O(E \log V)$.
- Kruskal's algorithm: grow a tree by selecting the minimum weight edge that does not form a loop after adding it. The time complexity is $O(E \log E) = O(E \log V)$.
- The minimum spanning tree of any weighted graph may not exist.








<br>

## Sorting

- Any algorithm that sorts by exchanging adjacent elements requires $O(N^2)$ time on average.
- The time comlexity of Selection Sort will be the same no matter we store the elements in an array or a linked list. (True)
- Shellsort is a very simple algorithm, yet with an extremely complex analysis.  It is good for sorting up to moderately large input (tens of thousands).
    - Hibbard’s increment sequence is $h_k = 2^k - 1$. The worst-case running time of Shellsort, using Hibbard’s increments, is $\Theta(N^{3/2})$. $T_{\text{avg}} (N) = O (N^{5/4})$ and $T_{\text{worst}} (N) = O (N^{3/2})$.
    - Sedgewick’s best sequence is {1, 5, 19, 41, 109, ... } in which the terms are either of the form $9\times 4^i – 9\times 2^i + 1$ or $4^i – 3\times 2^i + 1$. $T_{\text{avg}} (N) = O (N^{7/6})$ and $T_{\text{worst}} (N) = O (N^{4/3})$.

---

- The average number of comparisons used to heapsort a random permutation of $N$ distinct items is $2N\log N - O(N\log\log N)$. Although Heapsort gives the best average time, in practice it is slower than a version of Shellsort that uses Sedgewick’s increment sequence.
- To sort $N$ elements by heap sort, the extra space complexity is $O(1)$.
- Mergesort requires linear extra memory, and copying an array is slow.  It is hardly ever used for internal sorting, but is quite useful for external sorting.

---

- Quicksort is the fastest known sorting algorithm in practice.
- Quicksort is slower than insertion sort for small $N(\le 20)$.
- During the sorting, processing every element which is not yet at its final position is called a "run". To sort a list of integers using quick sort, it may reduce the total number of recursions by processing the small partion first in each run. (False)

---

- LSD Sort: Radix sort according to the Least Significant Digit first
- MSD Sort: Radix sort according to the Most Significant Digit first

---

- Stable Sorting: Insertion Sort, Bubble Sort, Merge Sort, Radix Sort
- Unstable Sorting: Selection Sort, Shell Sort, Heap Sort, Quick Sort
- For small $N$, Insertion sort is better; For large $N$, Quick sort is better, Shell sort is good and better than Heap sort in practice.








<br>

## Hashing

- The expected number of probes for insertions is greater than that for successful searches in linear probing method. (True)
- If the table size is prime and the table is at least half empty, a new element can always be inserted with quadratic probing. (True)
- In separate chaining method, if duplicate elements are allowed in the list, insertions are generally quicker than deletions. (True)

