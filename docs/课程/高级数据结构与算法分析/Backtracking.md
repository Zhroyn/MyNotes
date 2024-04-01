
# 回溯算法

设我们已经有一个部分解 $(x_1, \dots, x_i)$，满足 $\forall 1 \le k \le i < n, x_k \in S_k$，然后我们添加 $x_{i+1} \in S_{i+1}$，并检查 $(x_1, \dots, x_i, x_{i+1})$ 是否满足约束条件。若满足，则继续添加下一个 $x$，否则删除当前 $x_{i+1}$ 并尝试下一个 $x_{i+1}$。若所有的 $x_{i+1} \in S_{i+1}$ 均不满足条件，则删除 $x_i$ 并回溯到上一个部分解 $(x_1, \dots, x_{i-1})$。

回溯算法的伪代码为：

```C
bool Backtracking(int i) {
    Found = false;
    if (i > N)
        return true;  /* solved with (x1, …, xN) */
    for (each xi in Si) { 
        /* check if satisfies the restriction R */
        OK = Check((x1, …, xi) , R);  /* pruning */
        if (OK) {
            Count xi in;
            Found = Backtracking(i + 1);
            if (!Found) Undo(i);  /* recover to (x1, …, xi-1) */
        }
        if (Found) break; 
    }
    return Found;
}

```

