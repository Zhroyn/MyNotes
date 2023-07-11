
- [Optimization](#optimization)
  - [Model Fitting](#model-fitting)
  - [Numerical Methods](#numerical-methods)
    - [Steepest Descent Method](#steepest-descent-method)
    - [Newton Method](#newton-method)
    - [Gauss-Newton Method](#gauss-newton-method)
    - [Levenberg-Marquardt Method](#levenberg-marquardt-method)
  - [Robust Estimation](#robust-estimation)
    - [Random Sample Concensus (RANSAC)](#random-sample-concensus-ransac)
  - [Graphcut and MRF](#graphcut-and-mrf)
    - [Graph Cut](#graph-cut)
    - [Segmentation by MRF](#segmentation-by-mrf)








## Optimization
### Model Fitting
A typical approach of model fitting is to minimize the **mean square error (MSE)**
$$
\hat{x} = \argmin\sum_i (b_i - a_i^Tx)^2
$$

That's because we assume the data is with Gaussian noise
$$
b_i = a_i^Tx + n, n \sim G(0, \sigma)
$$

If the data points are independent, we can get
$$
\begin{aligned}
  P[(a_1, b_1)(a_2, b_2\cdots | x)]
  &= \prod_i P[(a_i, b_i) | x] \\
  &= \prod_i P[b_i - a_i^Tx] \\
  &\sim \exp -\frac{\sum_i(b_i - a_i^Tx)^2}{2\sigma^2} \\
  &= \exp -\frac{\left\| Ax - b \right\|^2}{2\sigma^2}
\end{aligned}
$$

**Maximum likelihood estimation (MLE)** is to maximize the likelihood to find the best $x$, so MSE = MLE with Gaussian noise assumption.









<br>

### Numerical Methods
#### Steepest Descent Method
Do first-order expansion at $x_k$
$$
F(x_k + \Delta x) \approx F(x_k) + J_F\Delta x
$$

When direction of $\Delta x$ is same as $-J_F^T$, the objective function descend steepest.

To find an appropriate step size, we can use backtracking algorithm. That is, initialize $\alpha$ with a big value, and then decrease $\alpha$ until
$$
\phi(x_k + \alpha) \le \phi(x_k) + \gamma\phi'(x_k)\alpha
$$

where $0 < \gamma < 1$.

<br>

#### Newton Method
Do second-order expansion at $x_k$
$$
F(x_k + \Delta x) \approx F(x_k) + J_F\Delta x + \frac{1}{2}\Delta x^T H_F \Delta x
$$

To minimize $F(x_k + \Delta x)$, we take the derivative of $\Delta x$
$$
H_F\Delta x + J_F^T = 0
$$

So the optimal direction is
$$
\Delta x = -H_F^{-1}J_F^T
$$

<br>

#### Gauss-Newton Method
This is useful for solving nonlinear least squares. Define
$$
R(x) = \begin{bmatrix} b_1 - f_x(a_1) \\ \cdots \\ b_n - f_x(a_n) \end{bmatrix}
$$

$R(x)$ is called the **residual vector**. Then
$$
\begin{aligned}
  \hat{x} &= \argmin F(x) \\
  &= \argmin \left\| R(x) \right\|^2
\end{aligned}
$$

Instead of expanding $F(x)$, we expand $R(x)$
$$
\begin{aligned}
  \left\| R(x_k + \Delta x) \right\|^2
  &\approx \left\| R(x_k) + J_R\Delta x \right\|^2 \\
  &= \left\| R(x_k) \right\|^2 + 2R(x_k)^TJ_R\Delta x + \Delta x^T J_R^T J_R \Delta x
\end{aligned}
$$

The optimal $\Delta x$ satisfies
$$
J_R^TJ_R\Delta x + J_R^TR(x_k) = 0
$$

So the optimal direction is
$$
\Delta x = -(J_R^T J_R)^{-1}J_R^TR(x_k)
$$

<br>

#### Levenberg-Marquardt Method
When $J_R^TJ_R$ is singular, Gauss-Newton algorithm becomes unstable. LM employ regularization to overcome this
$$
\Delta x = -(J_R^T J_R + \lambda I)^{-1} J_R^T R(x_k)
$$

When $\lambda > 0$, $J_R^T J_R + \lambda I$ must be positive-definite.

If $\lambda \rightarrow \infty$, it's like gradient descent.
If $\lambda \rightarrow 0$, it's like Gauss-Newton step.









<br>

### Robust Estimation
Inlier obeys the model assumption.
Outlier differs significantly from the assumption.
MSE is proportional to residual square, so it's affected a lot by outliers.

<br>

#### Random Sample Concensus (RANSAC)
RANSAC is the most powerful method to handle outliers, the procedures are
1. Choose some samples randomly to do model fitting.
2. Count the number of samples that do not deviate significantly from the model.
3. Determine the samples with the largest number as inliers.









<br>

### Graphcut and MRF
#### Graph Cut
Define pixel dissimilarity as
$$
S(\bm{f}_i, \bm{f}_j) = \sqrt{\sum_k (f_{ik} - f_{jk})^2}
$$

Define pixel affinity as
$$
w(i, j) = A(\bm{f}_i, \bm{f}_j) = e^{-\frac{1}{2\sigma^2}S(\bm{f}_i, \bm{f}_j)}
$$

Suppose cut $C = (V_A, V_B)$ is a partition of vertices $V$ of a graph $G$ into two disjoint subsets $V_A$ and $V_B$, then the cost of cut is
$$
\text{cut}(V_A, V_B) = \sum_{u\in V_A, v\in V_B} w(u, v)
$$

The graph cut is to minimize the cost of cut. Moreover, we can normalize the cut
$$
\text{NCut}(V_A, V_B) = \frac{\text{cut}(V_A, V_B)}{\text{assoc}(V_A, V)} + \frac{\text{cut}(V_A, V_B)}{\text{assoc}(V_B, V)} \\~\\
\text{assoc}(V_A, V) = \sum_{u\in V_A, v\in V} w(u, v)
$$

This is a NP-Complete problem, but has approximate solution by eigenvalue decomposition.

<br>

#### Segmentation by MRF
Define joint probability as
$$
P(x, y) = \frac{1}{Z}\prod_i \Phi(x_i, y_i) \prod_{i, j} \Psi(y_i, y_j)
$$

Then we can define the energy function
$$
E(x, y) = \sum_i \varphi(x_i, y_i) + \sum_{i, j} \psi(y_i, y_j)
$$

where $\varphi(x_i, y_i)$ is called unary term, representing the likelihood for each pixel, $\psi(y_i, y_j)$ is called pairwise term, representing the consistency between neighboring pixels.


