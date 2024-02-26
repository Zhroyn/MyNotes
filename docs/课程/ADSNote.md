



# 高级数据结构与算法分析笔记

## AVL Tree

定义空树的深度为 -1，同时定义平衡因子 $BF = h_L - h_R$，则在平衡树中，每个节点的平衡因子 (Balance Factor) 只能是 -1, 0, 1

Tree Rotation 是一种不会改变元素顺序的对二叉树的操作，是 AVL Tree 的核心操作，分为四种情况：

- 当不平衡节点发现插入节点在左子树的左子树时，进行 LL Rotation 调整，具体操作是将不平衡节点的左子树提升为新的根节点，原根节点成为新根节点的右子树，即右旋：

```C
AVLTree LLRotation(AVLTree A) {
    AVLTree B = A->left;
    A->left = B->right;
    B->right = A;
    A->height = GetHeight(A);
    B->height = GetHeight(B);
    return B;
}
```

- 当不平衡节点发现插入节点在右子树的右子树时，进行 RR Rotation 调整，具体操作是将不平衡节点的右子树提升为新的根节点，原根节点成为新根节点的左子树，即左旋：

```C
AVLTree RRRotation(AVLTree A) {
    AVLTree B = A->right;
    A->right = B->left;
    B->left = A;
    A->height = GetHeight(A);
    B->height = GetHeight(B);
    return B;
}
```

- 当不平衡节点发现插入节点在左子树的右子树时，进行 LR Rotation 调整，具体操作是先对不平衡节点的左子树进行 RR Rotation，然后对不平衡节点进行 LL Rotation，即将左节点的右节点提上来：

```C
AVLTree LRRotation(AVLTree A) {
    A->left = RRRotation(A->left);
    return LLRotation(A);
}
```

- 当不平衡节点发现插入节点在右子树的左子树时，进行 RL Rotation 调整，具体操作是先对不平衡节点的右子树进行 LL Rotation，然后对不平衡节点进行 RR Rotation，即将右节点的左节点提上来：

```C
AVLTree RLRotation(AVLTree A) {
    A->right = LLRotation(A->right);
    return RRRotation(A);
}
```

---

现欲构造一棵高度为 $h$ 的树，定义 $n_h$ 为所需的最少节点数，$n_h = n_{h-1} + n_{h-2} + 1$，其中 $n_0 = 1, n_1 = 2$，则有：

$$n_h = F_{h+3} - 1$$

其中 $F_0 = 0, F_1 = 1, F_i \approx \frac{1}{\sqrt{5}} \left( \frac{1 + \sqrt{5}}{2} \right)^i$。

所以 $n_h \approx \frac{1}{\sqrt{5}} \left( \frac{1 + \sqrt{5}}{2} \right)^{h+3} - 1$，AVL Tree 的高度为 $O(\log n)$。


<br>

## Splay Tree

Splay Tree 是一种自调整的二叉搜索树，通过旋转操作将被访问的节点提升到根节点，以提高后续访问的效率。虽然其单步操作复杂度可能超过 $log(N)$，但其在执行了 $M$ 个操作后，均摊时间复杂度为 $O(M\log N)$。

具体来说，对任意节点 $X$，定义其父节点为 $P$，祖父节点为 $G$，则有以下三种情况：

- Zig/Zag: 当 $P$ 是根节点时，对 $X$ 进行单旋转
- Zig-Zig: 当 $P$ 和 $G$ 在同一侧时，先对 $P$ 进行单旋转，再对 $X$ 进行单旋转
- Zig-Zag: 当 $P$ 和 $G$ 在不同侧时，先对 $X$ 进行单旋转，再对 $X$ 进行单旋转

每次 Splay 操作都会将被访问的节点提升到根节点，大致会将高度砍半。

若要删除 $X$ 节点，可以先将 $X$ 旋转到根节点，删除 $X$ 得到 $T_L$ 和 $T_R$，然后找到 $T_L$ 中最大的元素，使其成为根节点，$T_R$ 接在根节点的右侧。



<br>

## Amortized Analysis

均摊上界考虑的是最坏的情况，而平均上界则会考虑数据分布的影响。

聚合分析是一种分析数据结构的均摊复杂度的方法，通过执行 $N$ 个最坏时间的操作，然后将其分摊到每个操作上，得到均摊复杂度，比如 MultiPop 的均摊复杂度是 $O(n) / n = O(1)$。
