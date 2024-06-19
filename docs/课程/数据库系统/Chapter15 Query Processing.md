
# 查询处理

## 基本概念

查询处理的基本步骤为：

- 解析和翻译 (Parsing and translation)：先将查询转换为中序形式，再将其转换为关系代数，同时需要检查语法
- 优化 (Optimization)：一句 SQL 查询可能有多个等价的关系代数表达式，需要估计代价，选择代价最小的评估计划
- 评估 (Evaluation)：指定每个操作的算法，以及操作之间如何协调

查询的代价来源有磁盘寻道 (seek)、块读取 (block read)、块写入 (block written)、CPU 等。在这里，我们将块读取和块写入合并为块传输 (block transfer)。

在计算代价时，我们只考虑 block transfer 和 seek，将其次数分别定义为 $b$ 和 $S$，时间分别定义为 $t_T$ 和 $t_S$，则代价为 $b\times t_T + S\times t_S$，通常 $t_T << t_S$。




<br>

## 查询的代价

- A1 (linear search)
    - 假定所有的块都放在一起，因此只需要 seek 一次，最坏代价为 $b_r \times t_T + t_S$，平均代价为 $(b_r / 2) \times t_T + t_S$，其中 $b_r$ 为存储关系 $r$ 的所有记录的块的数目
- A2 (primary B+-tree index, equality on key)
    - 使用 B+ 树搜索一条记录
    - $\text{cost} = (h_i + 1) \times (t_T + t_S)$
- A3 (primary B+-tree index, equality on nonkey)
    - 因为是 nonkey，可能会搜索多条记录，且因为有主索引，想要的结果会存储在连续的块中
    - $\text{cost} = h_i \times (t_T + t_S) + t_S + t_T \times b$，其中 $b$ 为包含匹配记录的块的数目
- A4 (secondary B+-tree index, equality on key)
    - $\text{cost} = (h_i + 1) \times (t_T + t_S)$
- A4’ (secondary B+-tree index, equality on nonkey)
    - 会检索 $n$ 条记录，不一定在同一个块上面，设共分布在 $m$ 个块上
    - $\text{cost} = (h_i + m + n) \times (t_T + t_S)$
- A5 (primary B+-tree index, comparison)
    - 对于大于比较来说，代价为 $ h_i \times (t_T + t_S) + t_S + t_T \times b$，对于小于比较来说，只需要从头扫描即可
- A6 (secondary B+-tree index, comparison)
- A7 (conjunctive selection using one index)
- A8 (conjunctive selection using composite index)
- A9 (conjunctive selection by intersection of identifiers)





<br>

## 外部排序的代价

设内存页的数量为 $M$，在外部排序开始时，我们会依次将 $b_r$ 个块读入内存，进行排序，然后写回磁盘，生成 $\lceil b_r/M \rceil$ 个归并段 (runs)。

如果归并段少于可用内存页 ($N < M$)，则可以一次性将所有归并段的第一个块分别读入到 $N$ 个缓冲页中，将合并结果输出到另一个缓冲页，每当 output buffer 满了就写回磁盘，只需要一次 pass 就可以完成合并。

如果归并段不少于可用内存页 ($N \ge M$)，则需要多次 pass，每次以 $M-1$ 为单位将归并段分组，每组合并为一个新的归并段，这样每次 pass 后归并段的数量都会除以 $M-1$，直到最后只剩下一个归并段。

在这种简单的情况下，merge passes 的次数为 $\lceil \log_{M-1} \lceil b_r/M \rceil \rceil$，整个外部排序的代价为：

- block transfer 的代价
    - 创建归并段所需的 block transfer 为 $2b_r$，每次 pass 的 block transfer 也为 $2b_r$
    - 我们可以不考虑最终的 pass 的输出代价，因为它会输出到父操作而不是磁盘中，因此最终的 pass 的代价为 $b_r$
    - 因此，简单版的外部排序所需的 block transfer 次数为 $2b_r \lceil \log_{M-1} \lceil b_r/M \rceil \rceil + b_r = b_r (2\lceil \log_{M-1} \lceil b_r/M \rceil \rceil + 1)$
- seek 的代价
    - 在创建归并段时，读写归并段都需要一次 seek，因此总代价为 $2 \lceil b_r/M \rceil$
    - 在合并归并段时，每次 pass 的代价都为 $2b_r$，除了最终的 pass
    - 因此，简单版的外部排序所需的 seek 次数为 $2 \lceil b_r/M \rceil + b_r (2\lceil \log_{M-1} \lceil b_r/M \rceil \rceil - 1)$

这个版本的算法的问题是，每个归并段同时只处理一个块，导致在合并时每个块都需要一次 seek。我们考虑每个归并段同时读入 $b_b$ 个块，这样的话，每次 pass 的 seek 次数就会下降到 $2 \lceil b_r/b_b \rceil$，但同时，每次合并参与的段数量也会下降到 $\lfloor M/b_b \rfloor - 1$，导致合并次数上升，最终代价变为：

- block transfer: $b_r (2\lceil \log_{\lfloor M/b_b \rfloor - 1} \lceil b_r/M \rceil \rceil + 1)$
- seek: $2 \lceil b_r/M \rceil + \lceil b_r/b_b \rceil (2\lceil \log_{\lfloor M/b_b \rfloor - 1} \lceil b_r/M \rceil \rceil - 1)$





<br>

## Join 的代价

### Nested-Loop Join

$r \Join_{\theta} s$ 的计算方法是逐一比较 $(t_r, t_s)$ 是否满足条件 $\theta$。在顺序扫描的情况下：

- 每进入一次外层循环的循环体，就会顺序读入内层关系的所有块，block transfer 的开销为 $b_s$ 除以每次读入的块数目，seek 的开销为 1，最后的总开销会乘以外层循环的次数
- 每当外层关系在内存中的块都已处理完毕，就会重新读入一次外层关系的块，block transfer 的总开销为 $b_r$ 除以每次读入的块数目，seek 的开销与之相同
- 因此，block transfer 的代价为 *外层循环次数 X 内层关系传输次数 + 外层关系传输次数*，seek 的代价为 *外层循环次数 + 外层关系传输次数*。

具体的公式是：

- Nested-Loop Join: 对于 $r$ 中的每个元组 $t_r$，都要扫描一遍 $s$
    - 在最坏的情况下，内存只能存下每个关系的一个块，此时因为需要频繁地切换 $s$ 的块，block transfer 的代价为 $n_r \times b_s + b_r$，seek 的代价为 $n_r + b_r$
    - 在最好的情况下，内存可以存下 $s$ 的所有块，此时 block transfer 的代价为 $b_s + b_r$，seek 的代价为 $2$
- Block Nested-Loop Join: 最外两层循环是遍历 $r$ 的块和 $s$ 的块，最内两层循环是遍历块中 $r$ 的元组和 $s$ 的元组
    - 在最坏的情况下，$n_r$ 被优化为了 $b_r$，block transfer 的代价变为 $b_r \times b_s + b_r$，seek 的代价变为 $2 \times b_r$
    - 在最好的情况下，block transfer 的代价为 $b_r + b_s$，seek 的代价为 $2$
    - 在优化的算法中，每次外层关系可以读入 $M-2$ 个块，内层关系可以读入 1 个块，内存剩下一个块用作输出缓冲，此时 block transfer 的代价为 $\lceil b_r/(M-2) \rceil \times b_s + b_r$，seek 的代价为 $2 \lceil b_r/(M-2) \rceil$

Indexed Nested-Loop Join: 当连接条件是相等时，或者连接是自然连接时，我们可以使用索引扫描来加速连接操作。此时连接操作的代价为 $b_r(t_T + t_S) + n_r\times c$，其中 $c$ 是查询索引并返回匹配元组的代价，一般是树的高度加一。

### Merge-Join

Merge-Join: 适用于等值连接和自然连接，具体做法就是先让两个关系在连接属性上排序，然后逐一比较合并。这样的话，block transfer 的代价为 $b_r + b_s$，seek 的代价为 $\lceil b_r/b_b \rceil + \lceil b_s/b_b \rceil$ 或 $\lceil b_r/x_r \rceil + \lceil b_s/x_s \rceil$，其中 $b_b$、$x_r$、$x_s$ 都是内存能够一次性读入的块数目，$x_r + x_s = M$。

Hybrid Merge-Join: 当一个关系有序，另一个关系在连接属性上拥有 secondary index (B+树索引) 时，可以先把排序关系和未排序关系 B+ 树的叶子做 merge，再按照未排序关系指针指向的地址排序（这样之后就可以顺序扫描），最后再将指针替换为记录，拼接成结果。

### Hash-Join

在 Hash-Join 中，我们可以把要 join 的属性按近似程度分类，这样只用比较同一类的属性就可以了，大大减少了比较的次数。

哈希函数 $h$ 会对两个关系中具有共同连接属性 (JoinAttrs) 的元组进行分区 (partition)，将连接属性的值映射到 $\{0, 1, \cdots, n\}$，$r_i$ 中的元组只需要和 $s_i$ 中的元组比较即可。

我们设小的关系为 $s$，称作 build input，大的关系为 $r$，称作 probe input。

一般最后一级的哈希函数是 $n_h = \lceil b_s/M \rceil ∗ f$，$f$为修正因子。

如果不需要递归分区，哈希连接的代价是：

- block transfers: $3(b_r + b_s) + 4n_h$
    - 对 $r$ 和 $s$ 的分区要求完全读取这两个关系，并随后将它们写回，此操作需要 $2(b_r + b_s)$ 次块传输。构建和探测阶段各自读取每个分区一次，需要进一步进行 $b_r + b_s$ 次块传输。由于部分填充的块，分区占用的块数可能会稍多于 $b_r + b_s$。访问这样的部分填充的块可能会为每个关系增加最多$2n_h$ 的开销，因为每个 $n_h$ 分区都可能有一个必须写入和读回的部分填充的块
- seek: $2(\lceil b_r/b_b \rceil + \lceil b_s/b_b \rceil) + 2n_h$
    - 假设为每个输入缓冲区和每个输出缓冲区分配 $b_b$ 个块，分区总共需要 $2(\lceil b_r/b_b \rceil + \lceil b_s/b_b \rceil)$ 次查找。构建和探测阶段只需要对每个关系的 $n_h$ 个分区进行一次查找，因为每个分区都可以按顺序读取

如果需要递归分区，哈希连接的代价是：

- 对构建关系 $s$ 进行分区，以便每个分区少于 $M$ 个块所需的传递次数是 $\log_{\lfloor M/b_b \rfloor - 1} \lceil b_s/M \rceil \rceil$，因此最好选择较小的关系作为构建关系
- block transfer: $2(b_r + b_s)\log_{\lfloor M/b_b \rfloor - 1} \lceil b_s/M \rceil \rceil + b_r + b_s$
- seek: $2(\lceil b_r/b_b \rceil + \lceil b_s/b_b \rceil) \log_{\lfloor M/b_b \rfloor - 1} \lceil b_s/M \rceil \rceil$

如果所有东西都能放进主存里且不需要 partition，则 $n_h = 0$，代价降低为 $b_r + b_s$。
