
## BFGS
BFGS 是拟牛顿法，用于弥补牛顿法 Hessian 矩阵计算代价大、可能非正定的缺陷，同时通过近似 Hessian 矩阵来获得比一阶梯度下降更快的收敛速度。

对于一般的优化问题，若使用正定矩阵 $G$ 来近似 $A$，且迭代公式为

$$
G_{t+1} = G_t - \frac{G_tuu^TG_t}{u^TG_tu} + \frac{Auu^TA}{u^TAu}
$$

则有 $G_{t+1}u = Au$，且 $G_{t+1}$ 也为正定矩阵。



现设 $s_t = x_{t+1} - x_t$，$y_t = \nabla f_{t+1} - \nabla f_t$，优化目标为 $A = J_t = \int_0^1 \nabla^2 f(x_t + \tau s_t) \mathrm{d}\tau$，则有

