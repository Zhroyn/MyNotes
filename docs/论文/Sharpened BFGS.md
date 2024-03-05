
# Sharpened Quasi-Newton Methods: Faster Superlinear Rate and Larger Local Convergence Neighborhood
## Abstract
- BFGS 方法能使 Hessian 近似矩阵在 Newton 方向上的误差收敛为 0
- Greedy-BFGS 能够直接近似 Hessian 矩阵，不过在一开始的收敛速度比 BFGS 慢，需要经过更多次数的更新，收敛才能实现局部超线性速度。这是因为 Greedy-BFGS 直接近似 Hessian 矩阵，在 Newton 方向上不一定精确
- 本篇论文提出了 Sharpened-BFGS 方法，它利用了 BFGS 和 Greedy-BFGS 的近似思想，同时在 Newton 方向上和 Hessian 矩阵上近似，从而实现了更快的收敛速度，而且只需要更少的更新次数就可以达到二次收敛速度





<br>

## Introduction
- 一阶算法：$O(d)$ 的计算代价，但是在病态问题上收敛速度慢
- 二阶算法：利用 Hessian 矩阵来提高曲率估计，从而实现快速局部收敛速度。具体来说，Newton 方法可以实现局部二次收敛速度，但是计算代价为 $O(d^3)$
- 拟牛顿法 (Quasi-Newton, QN)：介于一阶和二阶方法之间，通过构造一个正定矩阵来近似 Hessian 矩阵，从而将计算代价降低到 $O(d^2)$

### Contributions
- 标准的 BFGS 方法在 Newton 方向上近似 Hessian 矩阵，在一开始能获得较快的收敛速度，但是难以完美地近似 Hessian 矩阵
- Greedy-BFGS 方法直接近似 Hessian 矩阵，一开始的收敛速度比 BFGS 慢，但是一旦 Hessian 近似矩阵足够精确，就能实现更快的收敛速度
- Sharpened-BFGS 方法结合了经典 BFGS 和 Greedy-BFGS 的思想，既通过在 Newton 方向上近似获得了一开始的快速收敛速度，又通过 Greedy-BFGS 的思想逐渐得到一个精确的 Hessian 近似矩阵，从而实现了二次收敛速度





<br>

## Preliminaries
QN 方法的一次更新的通用形式为： $$x_{t+1} = x_t - \eta_t G_t^{-1} \nabla f(x_t)$$

其中 $G_t$ 为 Hessian 矩阵的近似，QN 方法的本质就是更新 $G_t$。$\eta_t$ 为步长，在论文中保持为 1。

### BFGS Operator and Algorithm
设 $A$ 为 $d\times d$ 的正定矩阵，$G$ 为 $A$ 的近似，通过 BFGS 更新得到。$G$ 在方向 $u\in \mathbb{R}^d\backslash\{0\}$ 上的 BFGS 更新为：$$BFGS(A, G, u) = G_+ := G - \frac{Guu^\top G}{u^\top G u} + \frac{Au u^\top A}{u^\top A u}$$

显然 $Au = G_+u$，即 $A$ 和 $G_+$ 在 $u$ 方向上相等。

注：我们实际要更新的是 Hessian 近似矩阵的逆。通过利用 Sherman-Morrison-Woodbury 公式，可以得到 Hessian 逆近似矩阵 $H = G^{−1}$ 的更新形式：$$H_+ = \left( I - \frac{u u^\top A}{u^\top A u} \right) H \left( I - \frac{A u u^\top}{u^\top A u} \right) + \frac{u u^\top}{u^\top A u}$$

因此，BFGS 的计算代价为 $O(d^2)$。

我们选择 $x_{t+1} - x_t$ 作为方向 $u$，并设 $A$ 为从 $x_t$ 到 $x_{t+1}$ 的 Hessian 矩阵的平均，即 $A = J_t := \int_0^1 \nabla^2 f(x_t + \tau(x_{t+1} - x_t)) d\tau$，则可令 $G_{t+1}$ 满足 secant condition： $$G_{t+1}u = J_tu = \nabla f(x_{t+1}) - \nabla f(x_t)$$

由此就可以得到经典 BFGS 的更新形式：

$$
\begin{aligned}
  & \text{Update the variable } x_{t+1} = x_t - G_t^{-1} \nabla f(x_t) \\
  & \text{Compute } s_t = x_{t+1} - x_t \\
  & \text{Compute } y_t = \nabla f(x_{t+1}) - \nabla f(x_t) \\
  & \text{Compute } G_{t+1} = G_t - \frac{G_t s_t s_t^\top G_t}{s_t^\top G_t s_t} + \frac{y_t y_t^\top}{y_t^\top s_t}
\end{aligned}
$$

### Greedy-BFGS Algorithm
定义一个测度用来比较 $A$ 和 $G$ 的距离：$$\sigma(A, G) := Tr(A^{-1}G) - d$$

当且仅当 $A = G$ 时，$\sigma(A, G) = 0$。$\sigma$ 越小，说明收敛越好。

若使用 BFSG 更新 $G$，则有：$$\sigma(A, G) - \sigma(A, G_+) \ge \frac{u^\top Gu}{u^\top Au} - 1$$

右式的值越大，说明收敛越快。可以看到，收敛的速度跟 $u$ 有关，并且无法保证 $\sigma(A, G)$ 能收敛到 0。

现令目标函数的 Hessian 矩阵 $A$ 固定，且满足 $A \preceq G$ 和 $\mu I \preceq A \preceq LI$，则可得到使得右式最大的 $u$ 的取值：$$\bar u(A, G) := \argmax_{u\in \{e_i\}_{i=0}^d} \frac{u^\top Gu}{u^\top Au}$$

其中 $e_i$ 是第 $i$ 个元素为一，其余元素全为零的单位向量。我们可以通过确定第几个对角元之比最大来确定 $\bar{u}(A, G)$ 是第几个单位向量。

在 Greedy-BFGS 中，我们贪婪地选择 $\bar u(A, G)$ 来更新 $G$，如此就有：$$\sigma(A, \bar G_+) \le \left( 1 - \frac{\mu}{dL} \right) \sigma(A, G)$$

可以看到，Greedy-BFGS 算法能保证 $\sigma$ 可以线性收敛到 0，$G$ 可以收敛到真实的 Hessain 矩阵。

算法简记为：

$$
\begin{aligned}
  & \text{Update the variable } x_{t+1} = x_t - G_t^{-1} \nabla f(x_t) \\
  & \text{Compute } \bar u = \bar u(A, G_t) \\
  & \text{Compute } G_{t+1} = BFSG(A, G_t, \bar u)
\end{aligned}
$$

### Sharpened-BFSG
在 $A$ 固定的情况下，Sharpened-BFSG 的算法可以表述为：

$$
\begin{aligned}
  & \text{Update the variable } x_{t+1} = x_t - G_t^{-1} \nabla f(x_t) \\
  & \text{Compute } s_t = x_{t+1} - x_t \\
  & \text{Compute } \bar G_t = BFSG(A, G_t, s_t) \\
  & \text{Compute } \bar u = \bar u(A, \bar G_t) \\
  & \text{Compute } G_{t+1} = BFSG(A, \bar G_t, \bar u) \\
\end{aligned}
$$

大体就是先用经典 BFGS 更新一次，然后用 Greedy-BFGS 更新一次。

然而，对于更普遍的凸优化问题，$A$ 并不是固定的。为了建立算法的超线性收敛速率，我们需要如下的两个假设：
- 目标函数 $f$ 二阶可微，是强凸函数，强凸参数为 $\mu > 0$，且其梯度是 Lipschitz 连续的，Lipschitz 参数为 $L > 0$
- 目标函数 $f$ 是具有参数 $M$ 的强自和谐函数，即对于任意 $x, z, w \in \mathbb{R}^n$, 我们有：$$\nabla^2 f(y) - \nabla^2 f(x) \preceq M\| y - x \|_{z} \nabla^2 f(x)$$ 其中 $\| y - x \|_{z} = \sqrt{(y - x)^\top \nabla^2 f(z) (y - x)}$

这样以后，我们来给出 Sharpened-BFSG 的算法：
$$
\begin{aligned}
  & \text{Update the variable } x_{t+1} = x_t - G_t^{-1} \nabla f(x_t) \\
  & \text{Compute } s_t = x_{t+1} - x_t \\
  & \text{Set } J_t = \int_0^1 \nabla^2 f(x_t + \tau s_t) d\tau \\
  & \text{Compute } \bar G_t = BFSG(J_t, G_t, s_t) \\
  & \text{Compute } r_t = \left\| x_{t+1} - x_t \right\|_{x_t} \\
  & \text{Compute } \hat G_t = (1 + Mr_t/2)^2 \bar G_t \\
  & \text{Compute } \bar u = \bar u(\nabla^2 f(x_{t+1}), \hat G_t) \\
  & \text{Compute } G_{t+1} = BFSG(\nabla^2 f(x_{t+1}), \hat G_t, \bar u) 
\end{aligned}
$$

我们并不能保证 $\nabla^2 f(x) \preceq G$ 始终成立，而只有当 $\nabla^2 f(x) \preceq G$ 时，$\sigma(\nabla^2 f(x), G)$ 才是良定义的。因此我们需要添加修正项，来确保新的点和新的 Hessian 近似矩阵满足 $\nabla^2 f(x_{t+1}) \preceq \bar{G}_t$。然而，在实践中发现，对于混合方法和贪心方法，不矫正 Hessian 近似矩阵效果会更好，即在算法中令 $\hat{G}_t = \bar{G}_t$，因此我们可以将 $M$ 设置为 0。

此章节大量篇幅用于证明 Sharpened-BFSG 的收敛性以及收敛速度，其中用到了牛顿减量： $$\lambda_f(x) = \sqrt{\nabla f(x)^{\top} \nabla^2 f(x)^{-1} \nabla f(x)}$$

它可以利用二阶信息预测当前点到最优解的下降量。要得到它，我们可以将 $x^* = x_0 - \nabla^2 f(x_0)^{-1} \nabla f(x_0)$ 带入到 $f(x)$ 的二阶展开式中：

$$
\begin{aligned}
  f(x^*) &= f(x_0) + \nabla f(x_0)^\top (x^* - x_0) + \frac{1}{2} (x^* - x_0)^\top \nabla^2 f(x_0) (x^* - x_0) \\
  &= f(x_0) - \frac{1}{2} \nabla f(x_0)^\top \nabla^2 f(x_0)^{-1} \nabla f(x_0)
\end{aligned}
$$

所以到 $f(x^*)$ 的下降量约为： $$f(x_0) - f(x^*) = \frac{1}{2} \nabla f(x_0)^\top \nabla^2 f(x_0)^{-1} \nabla f(x_0) = \frac{1}{2} \lambda_f(x_0)^2$$
