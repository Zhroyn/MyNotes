
# Homework

## Homework 1

**2-1** If the depth of an AVL tree is 6 (the depth of an empty tree is defined to be -1), then the minimum possible number of nodes in this tree is:

- A. 13

- B. 17

- C. 20

- D. 33

??? tip "Answer"
    
    D. 要么使用 $n_h = n_{h-1} + n_{h-2} + 1$，要么使用 $n_h = F_{h+3} - 1$

**2-2** Insert 2, 1, 4, 5, 9, 3, 6, 7 into an initially empty AVL tree.  Which one of the following statements is FALSE?

- A. 4 is the root

- B. 3 and 7 are siblings

- C. 2 and 6 are siblings

- D. 9 is the parent of 7

??? tip "Answer"
    
    B. 3 和 7 不是兄弟节点

    ```mermaid
    graph TD
    classDef null fill:#999,stroke:#333;
        4((4))-->2((2))
        4-->6((6))
        2-->1((1))
        2-->3((3))
        6-->5((5))
        6-->9((9))
        9-->7((7))
        9-->a((n)):::null
    ```

**2-3** For the result of accessing the keys 3, 9, 1, 5 in order in the splay tree in the following figure, which one of the following statements is FALSE?

<div align="center"><img src="https://images.ptausercontent.com/128" width=50% /></div>

- A. 5 is the root

- B. 1 and 9 are siblings

- C. 6 and 10 are siblings

- D. 3 is the parent of 4

??? tip "Answer"
    
    D. 4 才是 3 的父节点

    ```mermaid
    graph TD
    classDef null fill:#999,stroke:#333;
        5((5))-->1((1))
        5-->9((9))
        1-->a((n)):::null
        1-->2((2))
        2-->b((n)):::null
        2-->4((4))
        4-->3((3))
        4-->c((n)):::null
        9-->6((6))
        9-->10((10))
        6-->d((n)):::null
        6-->8((8))
        8-->7((7))
        8-->e((n)):::null
        10-->f((n)):::null
        10-->11((11))
        11-->g((n)):::null
        11-->12((12))
        12-->h((n)):::null
        12-->13((13))
    ```

**2-4** When doing amortized analysis, which one of the following statements is FALSE?

- A. Aggregate analysis shows that for all $n$, a sequence of $n$ operations takes worst-case time $T(n)$ in total.  Then the amortized cost per operation is therefore $T(n)/n$

- B. For potential method, a good potential function should always assume its maximum at the start of the sequence

- C. For accounting method, when an operation's amortized cost exceeds its actual cost, we save the difference as credit to pay for later operations whose amortized cost is less than their actual cost

- D. The difference between aggregate analysis and accounting method is that the later one assumes that the amortized costs of the operations may differ from each other

??? tip "Answer"
    
    B. 势能函数应该在一开始最小

**2-5** Consider the following buffer management problem. Initially the buffer size (the number of blocks) is one. Each block can accommodate exactly one item. As soon as a new item arrives, check if there is an available block. If yes, put the item into the block, induced a cost of one. Otherwise, the buffer size is doubled, and then the item is able to put into. Moreover, the old items have to  be moved into the new buffer so it costs $k+1$ to make this insertion, where $k$ is the number of old items. Clearly, if there are $N$ items, the worst-case cost for one insertion can be $\Omega (N)$.  To show that the average cost is $O(1)$, let us turn to the amortized analysis. To simplify the problem, assume that the buffer is full after all the $N$ items are placed. Which of the following potential functions works?

- A. The number of items currently in the buffer

- B. The opposite number of items currently in the buffer

- C. The number of available blocks currently in the buffer

- D. The opposite number of available blocks in the buffer

??? tip "Answer"
    
    D. 为了证明，先设 $\text{size}_i$ 为第 $i$ 次插入前缓冲区的大小，则易得实际代价 $c_i$ 在缓冲区未满时等于 $1$，已满时等于 $\text{size}_i + 1$，接下来来看各个选项。

    A: 若缓冲区未满，则 $\hat{c}_i = c_i + \phi_i - \phi_{i-1} = 1 + 1 = 2$；若缓冲区已满，则 $\hat{c}_i = \text{size}_i + 1 + 1 = \text{size}_i + 2$。无法表现出均摊复杂度为 $O(1)$，错误。

    B: 若缓冲区未满，则 $\hat{c}_i = 1 - 1 = 0$；若缓冲区已满，则 $\hat{c}_i = \text{size}_i + 1 - 1 = \text{size}_i$。无法表现出均摊复杂度为 $O(1)$，错误。

    C: 若缓冲区未满，则 $\hat{c}_i = 1 - 1 = 0$；若缓冲区已满，则 $\hat{c}_i = \text{size}_i + 1 + \text{size}_i - 1 = \text{size}_i$。无法表现出均摊复杂度为 $O(1)$，错误。

    D: 若缓冲区未满，则 $\hat{c}_i = 1 + 1 = 2$；若缓冲区已满，则 $\hat{c}_i = \text{size}_i + 1 - \text{size}_i + 1 = 2$。由此可见均摊复杂度为 $O(1)$，正确。需要注意的是，这里的势能函数在最开始并不是最小值，但是由于题目强调了最后缓冲区是满的，所以 $\phi_N - \phi_0 \ge 0$，$\sum_{i=1}^N \hat{c}_i \ge \sum_{i=1}^N c_i$ 仍能成立。


