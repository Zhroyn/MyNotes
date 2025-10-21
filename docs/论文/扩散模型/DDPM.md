# 变分推断

**变分推断**（Variational Inference, VI）是一种近似贝叶斯推断的方法，用于在**后验分布难以直接计算**时，通过优化来寻找一个简单的、可处理的概率分布，使其尽可能接近真实的后验分布。

在贝叶斯统计中，我们关心的是后验分布：

$$p(z|x) = \frac{p(x|z)p(z)}{p(x)} = \frac{p(x|z)p(z)}{\int p(x|z)p(z) dz}$$

其中，$x$ 是观测数据，$z$ 是隐变量，$p(x)$ 是边缘似然（evidence）。

然而，计算边缘似然通常是不可行的（当真实后验可计算时，可使用 EM 算法），因为它涉及对所有可能的高维隐变量进行积分。这时候，我们需要**近似推断**，而变分推断是其中最主流的**确定性近似方法**。

定义一个简单的变分分布族 $q_{\phi}(z)$，其中 $\phi$ 是变分参数，变分推断要做的是最小化 KL 散度：

$$\phi^* = \arg\min_{\phi} D_{\text{KL}}(q_{\phi}(z) || p(z|x))$$

然而，直接计算 KL 散度需要知道后验分布 $p(z|x)$，这又回到了原来的问题。为了解决这个问题，我们需要引入**证据下界**（Evidence Lower Bound, ELBO），也被称为**变分下界**（Variational Lower Bound, VLB）：

$$
\begin{aligned}
    \log p(x) 
    &= \log \int p(x, z) dz \\
    &= \log \int q_\phi(z) \frac{p(x, z)}{q_\phi(z)} dz \\
    &= \log \mathbb{E}_{q_\phi(z)} \left[ \frac{p(x, z)}{q_\phi(z)} \right] \\
    &\geq \mathbb{E}_{q_\phi(z)} \left[ \log \frac{p(x, z)}{q_\phi(z)} \right] \quad \text{（Jensen 不等式）} \\
    &=: \mathcal{L}(\phi)
\end{aligned}
$$

同时易得：

$$
\begin{aligned}
    \log p(x) 
    &= \int q_\phi(z) \log \frac{p(x, z)}{q_\phi(z)} dz + \int q_\phi(z) \log \frac{q_\phi(z)}{p(z \mid x)} dz \\
    &= \mathcal{L}(\phi) + D_{\text{KL}}(q_\phi(z) \,\|\, p(z \mid x))
\end{aligned}
$$

因此，最小化 KL 散度 $D_{\text{KL}}(q_\phi(z) \,\|\, p(z \mid x))$ 等价于最大化 ELBO $\mathcal{L}(\phi)$。

ELBO 有两种等价形式：

- 期望形式，常用于推导：
   $$\mathcal{L}(\phi) = \mathbb{E}_{q_\phi(\mathbf{z})} \left[ \log p(\mathbf{x}, \mathbf{z}) - \log q_\phi(\mathbf{z}) \right]$$

- KL 形式，常用于解释目标：
   $$\mathcal{L}(\phi) = \log p(\mathbf{x}) - D_{\text{KL}}(q_\phi(\mathbf{z}) \,\|\, p(\mathbf{z} \mid \mathbf{x}))$$


# 自回归

# 条件高斯

# 扩散模型

## 扩散模型的定义

扩散概率模型是一种参数化的马尔可夫链，通过变分推断进行训练，旨在在有限时间步内生成与数据分布相匹配的样本。

扩散模型是一种隐变量模型（latent variable model），其形式为 $p_\theta(x_0) := \int p_\theta(x_{0:T}) dx_{1:T}$，即数据 $x_0$ 的生成分布 $p_\theta(x_0)$ 是通过对一个**联合分布** $p_\theta(x_{0:T})$ **边缘化**（积分掉）所有中间隐变量 $x_1, \dots, x_T$ 得到的，其中 $x_1, \dots, x_T$ 是与数据 $x_0 \sim q(x_0)$ 具有相同维度的隐变量。$x_0$ 是最初的图像样本，对应的真实数据分布为 $x_0 \sim q(x_0)$，而 $x_1, ..., x_T$ 是通过扩散过程逐步添加噪声后得到的中间状态。

## 扩散模型的反向过程

联合分布 $p_\theta(x_{0:T})$ 被称为**反向过程**，它被定义为一个马尔可夫链，其转移分布是可学习的高斯转移（每一步的去噪操作被建模为一个高斯分布，其均值或方差由神经网络 $\theta$ 预测），并以 $p(x_T) = \mathcal{N}(x_T; 0, I)$ 作为起始分布：

$$p_\theta(x_{0:T}) := p(x_T) \prod_{t=1}^T p_\theta(x_{t-1}|x_t), \quad p_\theta(x_{t-1}|x_t) := \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$$

## 扩散模型的前向过程

扩散模型与其他隐变量模型的区别在于，其近似后验分布 $q(x_{1:T}|x_0)$ （被称为**前向过程**或**扩散过程**）被固定为一个马尔可夫链，该链按照预设的方差调度（variance schedule）$\beta_1, ..., \beta_T$ 逐步向数据中添加高斯噪声，$\beta_t$ 可以是可学习参数也可以是超参数：

$$q(x_{1:T}|x_0) := \prod_{t=1}^T q(x_t|x_{t-1}), \quad q(x_t|x_{t-1}) := \mathcal{N}(x_t; \sqrt{1-\beta_t}x_{t-1}, \beta_t I)$$

设 $\alpha_t = 1 - \beta_t, \bar{\alpha}_t = \prod_{s=1}^t \alpha_s$，则可以得到前向过程任意时间步 $t$ 的闭式表达式：

$$
\begin{aligned}
    x_t
    &= \sqrt{\alpha_t} x_{t-1} + \sqrt{1 - \alpha_t} \epsilon_{t-1} \\
    &= \sqrt{\alpha_t} (\sqrt{\alpha_{t-1}} x_{t-2} + \sqrt{1 - \alpha_{t-1}} \epsilon_{t-2}) + \sqrt{1 - \alpha_t} \epsilon_{t-1} \\
    &= \sqrt{\alpha_t \alpha_{t-1}} x_{t-2} + \sqrt{1 - \alpha_t \alpha_{t-1}} \bar{\epsilon}_{t-2} \\
    &\dots \\
    &= \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon, \quad \epsilon, \epsilon_{t-1}, \epsilon_{t-2}, \dots, \epsilon_0 \sim \mathcal{N}(0, I)
\end{aligned}
$$

或者写为：

$$q(x_t|x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t}x_0, (1-\bar{\alpha}_t)I)$$

在给定了起始数据 $x_0$ 和最终噪声 $x_T$ 的情况下，前向过程的每一步后验分布 $q(x_{t-1}|x_t, x_0)$ 也都是高斯分布，且有闭式表达式：

$$
\begin{aligned}
    q(x_{t-1}|x_t, x_0)
    &= \frac{q(x_t, x_{t-1}, x_0)}{q(x_t, x_0)} \\
    &= \frac{q(x_0) q(x_{t-1}|x_0) q(x_t|x_{t-1}, x_0)}{q(x_0) q(x_t|x_0)} \\
    &= \frac{q(x_{t-1}|x_0) q(x_t|x_{t-1}, x_0)}{q(x_t|x_0)} \\
    &= \exp \left( -\frac{1}{2} \left[\frac{\|x_{t-1} - \sqrt{\bar{\alpha}_{t-1}} x_0\|^2}{1 - \bar{\alpha}_{t-1}} + \frac{\|x_t - \sqrt{\alpha_t} x_{t-1}\|^2}{\beta_t} - \frac{\|x_t - \sqrt{\bar{\alpha}_t} x_0\|^2}{1 - \bar{\alpha}_t} \right] \right) \\
    &= \mathcal{N}\left(x_{t-1}; \tilde{\mu}_t(x_t, x_0), \tilde{\beta}_t I\right) \\
\end{aligned}
$$

$$\tilde{\mu}_t(x_t, x_0) = \frac{\sqrt{\bar{\alpha}_{t-1}} \beta_t}{1 - \bar{\alpha}_t} x_0 + \frac{\sqrt{\alpha_t} (1 - \bar{\alpha}_{t-1})}{1 - \bar{\alpha}_t} x_t, \quad \tilde{\beta}_t = \frac{(1 - \bar{\alpha}_{t-1}) \beta_t}{1 - \bar{\alpha}_t}$$

## 扩散模型的训练目标

扩散模型的训练目标是最大化边缘似然 $\log p_\theta(x_0)$，这可以通过变分推断来实现。令 $x_0$ 为观测数据，$x_{1:T}$ 为隐变量，$q(x_{1:T}|x_0)$ 这个前向过程为变分分布，则可以通过优化负对数似然的变分下界（ELBO）来训练模型：

$$\mathbb{E}[-\log p_\theta(x_0)] \leq \mathbb{E}_q\left[-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right] =: L$$

$L$ 可以重写为：

$$
\begin{aligned}
    \mathbb{E}_q \left[ \log \frac{q(x_{1:T}|x_0)}{p_\theta(x_{0:T})} \right]
    &= \mathbb{E}_q \left[ \log \frac{\prod_{t\ge 1} q(x_t|x_{t-1})}{p(x_T) \prod_{t\ge 1} p_\theta(x_{t-1}|x_t)} \right] \\
    &= \mathbb{E}_q \left[ \log \frac{1}{p(x_T)} + \sum_{t>1} \log \frac{q(x_t|x_{t-1})}{p_\theta(x_{t-1}|x_t)} + \log \frac{q(x_0|x_1)}{p_\theta(x_0|x_1)} \right] \\
    &= \mathbb{E}_q \left[ \log \frac{1}{p(x_T)} + \sum_{t>1} \log \frac{q(x_{t-1}|x_t, x_0)}{p_\theta(x_{t-1}|x_t)} \cdot \frac{q(x_t|x_0)}{q(x_{t-1}|x_0)} + \log \frac{q(x_0|x_1)}{p_\theta(x_0|x_1)} \right] \\
    &= \mathbb{E}_q \left[ \log \frac{q(x_T|x_0)}{p(x_T)} + \sum_{t>1} \log \frac{q(x_{t-1}|x_t, x_0)}{p_\theta(x_{t-1}|x_t)} - \log p_\theta(x_0|x_1) \right] \\
    &= \mathbb{E}_q \left[ D_{KL}(q(x_T|x_0) \| p(x_T)) + \sum_{t>1} D_{KL}(q(x_{t-1}|x_t, x_0) \| p_\theta(x_{t-1}|x_t)) - \log p_\theta(x_0|x_1) \right] \\
    &=: L_T + \sum_{t>1} L_{t-1} - L_0
\end{aligned}
$$

可以看到，损失函数中的所有 KL 散度项都是高斯分布之间的对比，有解析解。

其中，$L_T$ 意味着要让加噪后的真实数据尽可能地接近标准高斯分布，$L_{t-1}$ 意味着要让反向过程的每一步转移分布 $p_\theta(x_{t-1}|x_t)$ 尽可能地接近真实数据的去噪效果，$L_0$ 意味着要让最终生成的样本尽可能地接近真实数据。




# DDPM

## 训练

DDPM（Denoising Diffusion Probabilistic Models）在前向过程中使用固定的 $\beta_t$，在反向过程中，方差 $\Sigma_\theta(x_t, t) = \sigma_t^2 I$ 也是仅依赖于时间的固定常数。作者尝试了两种固定的方差设定，实验效果差不多：

- 第一种：$\sigma_t^2 = \beta_t$
    - 这个选择在数据初始分布为标准高斯（$x_0 \sim N(0, I)$）时是最优的
    - $x_0$ 完全随机，反向过程的不确定性最大
- 第二种：$\sigma_t^2 = \tilde{\beta}_t = \frac{1 - \bar{\alpha}_{t-1}}{1 - \bar{\alpha}_t} \beta_t$
    - 这个选择在初始数据是固定为某个具体值时是最优的
    - $x_0$ 完全确定，反向过程的不确定性最小

因为前向过程是固定的，所以 $L_T$ 是常数，可以被忽略。

因为反向过程中的方差也是固定的，所以 $L_{t-1}$ 可以被简化为：

$$
\begin{aligned}
    L_{t-1}
    &= \mathbb{E}_{q} \left[ \frac{1}{2 \sigma_t^2} \| \tilde{\mu}_t(x_t, x_0) - \mu_{\theta}(x_t, t) \|^2 \right] + C \\
    &= \mathbb{E}_{x_0, \epsilon} \left[ \frac{1}{2 \sigma_t^2} \left\| \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}} \epsilon \right) - \mu_{\theta}(x_t, t) \right\|^2 \right] + C \\
\end{aligned}
$$

为了降低模型预测的难度以及简化训练目标，作者提出了**噪声预测重参数化**，即不再让模型直接预测均值 $\mu_\theta(x_t, t)$，而是先预测从 $x_t$ 到 $x_0$ 的噪声 $\epsilon_{\theta}$，由此重建出 $x_0$，再由前向过程的后验分布公式得到 $x_{t-1}$ 的均值：

$$\mu_\theta(x_t, t) = \tilde{\mu}_t \left( x_t, \frac{1}{\sqrt{\bar{\alpha}_t}} (x_t - \sqrt{1 - \bar{\alpha}_t} \epsilon_{\theta}(x_t)) \right) = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}} \epsilon_\theta(x_t, t) \right)$$

这样之后，训练目标可进一步简化为：

$$
\begin{aligned}
    L_{t-1}
    &= \mathbb{E}_{x_0, \epsilon} \left[ \frac{\beta_t^2}{2 \sigma_t^2 \alpha_t (1 - \bar{\alpha}_t)} \| \epsilon - \epsilon_\theta(x_t, t) \|^2 \right] \\
    &= \mathbb{E}_{x_0, \epsilon} \left[ \frac{\beta_t^2}{2 \sigma_t^2 \alpha_t (1 - \bar{\alpha}_t)} \| \epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon, t) \|^2 \right] \\
\end{aligned}
$$

在实际训练中，会使用更进一步简化的损失函数：

$$L_{\text{simple}}(\theta) := \mathbb{E}_{t, x_0, \epsilon} \left[ \| \epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon, t) \|^2 \right]$$

这种“忽略权重”的做法，实际上等价于使用了一个新的加权变分下界，让模型在训练时更重视较大的 $t$，即让模型把更多容量用于学习如何从强噪声中重建，这对生成高质量样本至关重要。

对于 $L_0$，则使用一个独立的离散解码器，用积分计算预测结果与真实数据之间的对数似然：

$$p_\theta(x_0|x_1) = \prod_{i=1}^{D} \int_{\delta_{-}(x_0^i)}^{\delta_{+}(x_0^i)} \mathcal{N}(x; \mu_{\theta}^i(x_1, 1), \sigma_1^2) \, dx$$

在实际训练中，$L_0$ 会使用高斯概率密度函数乘以区间大小的近似公式。

## 采样

采样时，会从标准高斯分布采样初始噪声 $x_T \sim \mathcal{N}(0, I)$，然后通过反向过程的马尔可夫链逐步去噪，直到得到最终样本 $x_0$。

其中的每一步，都会预测噪声 $\epsilon_\theta(x_t, t)$ 重建出 $x_0$，再根据前向过程的后验分布公式采样 $x_{t-1}$：

$$x_{t-1} = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}} \epsilon_\theta(x_t, t) \right) + \sigma_t z, \quad z \sim \mathcal{N}(0, I)$$

## 消融分析

- 当使用可学习方差时，训练更不稳定，采样效果更差
- 当使用固定方差、原始 ELBO 时，预测目标是均值或噪声差别不大
- 当使用固定方差、简化 ELBO 时，预测目标是均值时非常不稳定，预测目标是噪声时模型效果提升极大
