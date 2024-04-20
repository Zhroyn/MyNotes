
# 动态规划

动态规划的核心思想就是记住已经解决过的子问题的解，用其来解决更大的问题，避免重复计算。动态规划的关键就是要有最优子结构，且能找到重复的子问题。

## 顺序矩阵乘法

现给定多个不同大小的矩阵 $M_1, M_2, \cdots, M_n$，令 $b_n$ 为计算 $M_1 \cdot M_2 \cdot \cdots \cdot M_n$ 可能的顺序数量。现设 $M_{ij} = M_i \cdots M_j$，则原式等价于 $M_{1n}$，每次计算 $M_{ij}$ 的问题可以拆分为计算 $M_{i, k} \cdot M_{k+1, j}$，从而变成更小的子问题。由此可得 $b_n$ 的递推式为：

$$ b_n = \sum_{i=1}^{n-1} b_i b_{n-i} $$

这是一个卡特兰数，近似为 $O( \frac{4^n}{n\sqrt n} )$。

现设 $M_i$ 是一个 $r_{i-1} \times r_i$ 的矩阵，$m_{ij}$ 为 $M_{ij}$ 根据上面分解的方式计算的最小代价，则易得递推式为：

$$
m_{ij} =
\begin{cases}
    0 & i = j \\
    \min\limits_{i \le l < j} \{ m_{i,l} + m_{l+1,j} + r_{i-1} r_l r_j \} & j > i
\end{cases}
$$

这样从规模为 1 的问题开始迭代计算，就可以得到计算 $M_{1n}$ 的最小代价，时间复杂度为 $O(N^3)$。


## 最优搜索树

给定 $N$ 个按照字典序排序的单词 $w_1 < w_2 < \cdots < w_N$，以及它们出现的概率 $p_i$，现在要构造一棵二叉搜索树，使得搜索的期望代价最小，即最小化：

$$ T(N) = \sum_{i=1}^N p_i \cdot (1 + d_i) $$

设 $c_{ij}$ 为构造 $w_i, \cdots, w_j$ 的最小代价，$w_{ij}$ 为 $w_i, \cdots, w_j$ 的权重和，则有递推式：

$$ c_{ij} = \min\limits_{i < l \le j} \{ w_{ij} + c_{i,l-1} + c_{l+1,j} \} $$

这样从规模为 1 的问题开始迭代计算，就可以构造出一颗 OBST，时间复杂度为 $O(N^3)$。


## 多源最短路径

定义

$$
D^k[i][j] = 
\begin{cases}
    \text{Cost}[i][j] & k = -1 \\
    \min \{ \text{length of path } i \rightarrow \{l \le k\} \rightarrow j \} & k \ge 0
\end{cases}
$$

则有递推式：

$$ D^k[i][j] = \min \{ D^{k-1}[i][j], D^{k-1}[i][k] + D^{k-1}[k][j] \} $$

显然，对于任意一对 $i, j$，$D^{N-1}[i][j]$ 即为 $i \rightarrow j$ 的最短路径。时间复杂度为 $O(N^3)$。这个算法在有负权边的情况下也是适用的，但是不能有负权回路。
