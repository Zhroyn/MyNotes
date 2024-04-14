
# 分治法

## 介绍

分治法分为三步：

1. 将问题分解为子问题
2. 递归地解决子问题
3. 将子问题的解合并为原问题的解（关键）

相应的递推式为：

$$ T(N) = aT(N/b) + f(N) $$

当 $f(N) = cN$ 时，

$$
\begin{aligned}
    T(N) &= 2T(N/2) + cN \\
    &= 2^k T(N / 2^k) + kcN \\
    &= N + cN \log N \\
    &= O(N \log N)
\end{aligned}
$$

当 $f(N) = cN^2$ 时，

$$
\begin{aligned}
    T(N) &= 2T(N/2) + cN^2 \\
    &= 2^k T(N / 2^k) + cN^2(1 + 1/2 + \cdots + 1/2^{k-1}) \\
    &= O(N + N^2) \\
    &= O(N^2)
\end{aligned}
$$

常见的可由分治法解决的问题有：

- 最大子序列和：每次合并时，把以左子序列的开头为开头、右子序列的结尾为结尾的序列之和，与左子序列的最大和与右子序列的最大和做比较，取最大值。此时 $a = b = 2, f(N) = N$，所以 $T(N) = O(N\log N)$。
- 树的遍历：若树的度为 $m$，则 $a = b = m, f(N) = 1$，所以 $T(N) = O(N)$
- 合并排序与快速排序：$O(N\log N)$




<br>

## 最近点问题

最近点问题的分治法解法如下：

1. 将点按照 $x$ 坐标排序，分为左右两堆
2. 解出左右两堆点的最近点对，取更小的那个作为 $\delta$
3. 仅考虑与分界线距离小于 $\delta$ 的点，对每个点，只需考虑其下方 $\delta$ 范围内的点，此时该范围内最多有 7 个点，逐一枚举即可




<br>

## 递归式的求解

### 代入法

先猜测上界，然后使用数学归纳法证明。需要注意的是，在代入递推式后得到的上界必须严格小于等于假设的上界，例如假设 $T(N) = O(N)$ 就不能推出 $\le cN + N$

### 递归树法

递归树法就是通过画出递归树，求解递归树的高度和每层的代价之和，来得到递归式的解。

例如，对于 $T(N) = 3T(N / 4) + \Theta(N^2)$，有：

$$
\begin{aligned}
    T(N) &= cN^2 + c \cdot 3\cdot (\frac{N}{4})^2 + \cdots + c\cdot 3^k \cdot (\frac{N}{4^k})^2 + \cdots \\
    &= cN^2 + c (\frac{3}{16}) N^2 + \cdots + c (\frac{3}{16})^k N^2 + \cdots \\
\end{aligned}
$$

因为树的高度为 $\log_4 N$，所以叶子节点的个数为 $3^{\log_4 N} = N^{\log_4 3}$，所以：

$$ T(N) = c \sum_{i=0}^{\log_4 N - 1} (\frac{3}{16})^i N^2 + \Theta(N^{\log_4 3}) = \Theta(N^2) $$


### 主方法

主定理：对于形式为 $T(N) = a T(N / b) + f(N)$ 的递推式，有下面三种情况：

1. 若 $\exist \epsilon>0, f(N) = O(N^{\log_b a - \epsilon})$，则 $T(N) = \Theta(N^{\log_b a})$
2. 若 $f(N) = \Theta(N^{\log_b a})$，则 $T(N) = \Theta(N^{\log_b a} \log N)$
3. 若 $\exist \epsilon>0, f(N) = \Omega(N^{\log_b a + \epsilon})$，且对于充分大的 $N$ 有 $\exist c < 1, a f(N / b) \le c f(N)$，则 $T(N) = \Theta(f(N))$

主定理的另一种形式为：

1. 若存在 $\kappa < 1$ 使得 $a f(N / b) = \kappa f(N)$，则 $T(N) = \Theta(f(N))$
2. 若存在 $K > 1$ 使得 $a f(N / b) = K f(N)$，则 $T(N) = \Theta(N^{\log_b a})$
3. 若 $a f(N / b) = f(N)$，则 $T(N) = \Theta(f(N) \log_b N)$

#### 主定理的用例

很多递推式都可以使用主定理快速求解：

- $a > 1, f(N) = 1$ 对应于第一种情况，$T(N) = \Theta(N^{\log_b a})$
- $a = b = k, f(N) = N$ 对应于第二种情况，$T(N) = \Theta(N \log N)$
- $k > \log_b a, a \le b^k, f(N) = N^k$ 对应于第三种情况，$T(N) = \Theta(N^k)$

需要注意的是，$a = b = k, f(N) = N\log N$ 不对应于主定理的任何一种情况，不能使用主方法求解。

对于形式为 $T(N) = a T(N / b) + \Theta(N^k \log^p N)$ 的递推式，有：

$$
T(N) = \begin{cases}
    O(N^{\log_b a}) \quad & \text{if } \log_b a > k \\
    O(N^k \log^{p+1} N) \quad & \text{if } \log_b a = k \\
    O(N^k) \quad & \text{if } \log_b a < k
\end{cases}
$$

因此，若 $a = b = k, f(N) = N\log N$，则 $T(N) = N\log^2 N$。

#### 主定理的证明

主定理可以使用递归树法证明。首先，递归展开 $T(N)$，得到：

$$ T(N) = \Theta(N^{\log_b a}) + \sum_{i=0}^{\log_b N - 1} a^i f(N / b^i) $$

对于情况一，有：

$$\sum_{i=0}^{\log_b N - 1} a^i f(N / b^i) \le \sum_{i=0}^{\log_b N - 1} a^i c (N / b^i)^{\log_b a - \epsilon} = O(N^{\log_b a})$$

所以 $T(N) = \Theta(N^{\log_b a})$。

对于情况二，有：

$$
\begin{aligned}
    \sum_{i=0}^{\log_b N - 1} a^i f(N / b^i) &= \Theta \left( \sum_{i=0}^{\log_b N - 1} a^i \left( \frac{N}{b^i} \right)^{\log_b a} \right) \\
    &= \Theta \left( N^{\log_b a} \sum_{i=0}^{\log_b N - 1} 1 \right) \\
    &= \Theta(N^{\log_b a} \log N)
\end{aligned}
$$

所以 $T(N) = \Theta(N^{\log_b a} \log N)$。

对于情况三，有：

$$ \sum_{i=0}^{\log_b N - 1} a^i f(N / b^i) \le \sum_{i=0}^{\infty} c^i f(N) + O(1) = O(f(N)) $$

因为 $c$ 是一个常数，所以 $T(N) = \Theta(f(N))$。
