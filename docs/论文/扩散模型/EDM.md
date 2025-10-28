# Elucidating the Design Space of Diffusion-Based Generative Models

## 引言

作者认为当前扩散模型的研究**过于理论化且设计选择耦合紧密**，导致难以清晰理解各组件的作用。因此，他们提出一个**模块化、解耦的设计空间框架**，将扩散模型拆解为几个独立可调的组成部分：

- 采样过程（Sampling）
- 网络结构与预处理（Network & Preconditioning）
- 训练策略（Training）

通过这种解耦，他们系统地改进了每个部分，最终在多个基准上取得了新的 SOTA 结果，同时显著提升了采样效率。

论文的主要贡献为：

- 统一框架重构扩散模型，将多种扩散模型（如 DDPM、NCSN、iDDPM、DDIM 等）纳入一个统一的 ODE（常微分方程）框架中
- 改进采样过程，确定了采样中表现最佳的时间离散化方法，将高阶 Runge–Kutta 方法应用于采样过程，评估了不同的采样器调度策略，并分析了采样过程中随机性的有用性
- 对网络输入、输出和损失函数的预处理（preconditioning） 进行了系统性分析，并推导出改善训练动态的最佳实践
- 优化训练策略，包括噪声分布、损失权重和数据增强
- 提出一种“噪声搅动 + ODE 步”的混合策略，在特定噪声区间内注入额外噪声，并补偿 L2 训练导致的“去噪过度”问题



<br>

## 统一框架的建模

### ODE 公式

让我们定义：

- $p_{\text{data}}(x)$: 数据分布
- $\sigma_{\text{data}}$: 数据分布的标准差
- $p(x; \sigma)$: 通过对数据添加独立同分布的高斯噪声（标准差为 $\sigma$）得到的平滑分布
- $\sigma_{\max}$: 当 $\sigma_{\max} \gg \sigma_{\text{data}}$ 时，$p(x; \sigma_{\max})$ 视为纯高斯噪声

扩散模型的思想是：首先随机采样一个噪声图像 $x_0 \sim \mathcal{N}(0, \sigma_{\max}^2 I)$，然后逐步将其去噪为一系列图像 $x_i$，对应的噪声水平满足 $\sigma_0 = \sigma_{\max} > \sigma_1 > \cdots > \sigma_N = 0$，使得在每个噪声水平下都有 $x_i \sim p(x_i; \sigma_i)$。该过程的终点 $x_N$ 因此服从真实数据分布。

我们可以用一个常微分方程（ODE）来描述这一连续过程，令其在时间正向推进时连续增加图像噪声水平，反向推进时则降低噪声水平。具体而言，该概率流 ODE 的特性是：若从时间 $t_a$ 开始，将样本 $x_a \sim p(x_a; \sigma(t_a))$ 演化到时间 $t_b$（无论正向或反向），所得样本 $x_b$ 将服从 $p(x_b; \sigma(t_b))$。这一要求可通过以下方程满足：

$$
dx = -\dot{\sigma}(t)\sigma(t) \nabla_x \log p(x; \sigma(t)) \, dt \tag{1}
$$

其中:

- $\sigma(t)$: 噪声调度函数
- $\dot{\sigma}(t)$: $\sigma(t)$ 对时间的导数
- $\nabla_x \log p(x; \sigma)$: 得分函数（score function），指向给定噪声水平下数据密度更高的方向

一些方法会引入额外的缩放调度 $s(t)$，并将 $x = s(t) \hat{x}$ 视为原始变量 $\hat{x}$ 的缩放版本。这样得到的概率流 ODE 的一般形式为:

$$dx = \left[ \frac{\dot{s}(t)}{s(t)} x - s(t)^2 \dot{\sigma}(t)\sigma(t) \nabla_x \log p\left(\frac{x}{s(t)}; \sigma(t)\right) \right] dt$$

### 去噪得分匹配

得分函数与去噪器 $D(x; \sigma)$ 的关系:

$$\nabla_x \log p(x; \sigma) = \frac{D(x; \sigma) - x}{\sigma^2}$$

其中 $D(x; \sigma)$ 会最小化去噪误差:

$$\mathbb{E}_{y \sim p_{\text{data}}} \mathbb{E}_{n \sim \mathcal{N}(0, \sigma^2 I)} \|D(y + n; \sigma) - y\|_2^2$$

### 离散化求解

将上式代入 ODE 得到最终求解的形式:

$$dx = \left[ \frac{\dot{s}(t)}{s(t)} x - s(t)^2 \dot{\sigma}(t)\sigma(t) \cdot \frac{D(x/s(t); \sigma(t)) - x/s(t)}{\sigma(t)^2} \right] dt$$

在实际应用中，我们会通过数值积分方法来进行求解。因此，每一种采样方案都需要确定以下信息：

- ODE 求解器（Euler 或二阶 Heun 方法）
- 采样时间步 $\{t_0, t_1, \ldots, t_N\}$
- 噪声调度函数 $\sigma(t)$
- 信息缩放函数 $s(t)$




<br>

## 确定性采样的改进

论文的假设是：与采样过程相关的选择在很大程度上独立于其他组件，例如网络架构和训练细节。换句话说，$D_\theta$ 的训练过程不应强制规定 $\sigma(t)$、$s(t)$ 和 $\{t_i\}$，反之亦然；从采样器的视角来看，$D_\theta$ 仅仅是一个黑盒。

论文使用 Fréchet Inception Distance（FID）来评估生成图像的质量，并通过 FID 达到最优时的 NEF（Neural Function Evaluations）来衡量采样速度的提升。

### 求解器选择

数值求解 ODE 必然是对真实解轨迹的近似。每一步求解器都会引入截断误差，这些误差在 $N$ 步过程中累积。局部误差通常随步长超线性增长，因此增加 $N$ 可提高解的精度。

常用的欧拉（Euler）方法是一阶 ODE 求解器，其局部误差为 $O(h^2)$。更高阶的 Runge–Kutta 方法的误差更小，但每步需要多次调用 $D_\theta$。经过测试，论文发现 Heun 的二阶方法（又称改进欧拉法、梯形法则）在仅需调用两次 $D_\theta$ 的同时，局部误差为 $O(h^3)$，取得了极佳的平衡。

**二阶 Heun 算法确定性采样流程:**

1. 采样初始噪声: $x_0 \sim \mathcal{N}(0, \sigma^2(t_0) s^2(t_0) I)$
2. 对于每一步 $i = 0, \ldots, N-1$:
    1. 计算导数: $d_i = \left( \frac{\dot{\sigma}(t_i)}{\sigma(t_i)} + \frac{\dot{s}(t_i)}{s(t_i)} \right)x_i - \frac{\dot{\sigma}(t_i) s(t_i)}{\sigma(t_i)} D_{\theta}(\frac{x_i}{s(t_i)}; \sigma(t_i))$
    2. Euler 步: $x_{i+1} = x_i + (t_{i+1} - t_i) d_i$
    3. 如果 $\sigma(i+1) \neq 0$，应用二阶修正:
        1. 计算导数: $d_i' = \left( \frac{\dot{\sigma}(t_{i+1})}{\sigma(t_{i+1})} + \frac{\dot{s}(t_{i+1})}{s(t_{i+1})} \right)x_i - \frac{\dot{\sigma}(t_{i+1}) s(t_{i+1})}{\sigma(t_{i+1})} D_{\theta}(\frac{x_i}{s(t_{i+1})}; \sigma(t_{i+1}))$
        2. 梯形法则: $x_{i+1} = x_i + (t_{i+1} - t_i) \cdot \frac{1}{2}(d_i + d_i')$
3. 返回 $x_N$

相比 Euler 方法，每步多一次网络评估，但总 NFE 可减少 3-7 倍。

### 调度函数选择

EDM 推荐使用最简单的调度（这也是 DDIM 的选择）：

$$\sigma(t) = t, \quad s(t) = 1$$

这使得 ODE 简化为：

$$\frac{dx}{dt} = \frac{x - D(x; t)}{t}$$

此时 $\sigma$ 和 $t$ **可以互换**。

### 时间步离散化

时间步 $\{t_i\}$ 由噪声调度序列 $\{\sigma_i\}$ 定义，其中:

$$\sigma_i = \left( \sigma_{\max}^{1/\rho} + \frac{i}{N-1} \left( \sigma_{\min}^{1/\rho} - \sigma_{\max}^{1/\rho} \right) \right)^\rho, \quad i = 0, 1, \ldots, N-1$$

$$\sigma_N = 0$$

参数设置:

- $\rho = 7$: 控制步长分布，使小噪声处步长更短，$\rho$ 越小，步长分布越均匀
- $\sigma_{\min} = 0.002, \sigma_{\max} = 80$: 噪声范围



<br>

## 随机采样

确定性采样具有诸多优势，例如能够通过反转 ODE 将真实图像映射到其对应的潜在表示。然而，与在每一步都注入新噪声的随机采样相比，它往往导致更差的输出质量。

为了加入随机性，可以给概率流 ODE 添加 Langevin 扰动项:

$$
dx = -\dot{\sigma}(t)\sigma(t) \nabla_x \log p(x; \sigma(t)) dt \pm \beta(t)\sigma(t)^2 \nabla_x \log p(x; \sigma(t)) dt + \sqrt{2 \beta(t)} \sigma(t) dw_t
$$

其中 $dw_t$ 是维纳过程（Wiener process）。Langevin 项可进一步视为一个基于得分的确定性去噪项与一个随机噪声注入项的组合，二者的净噪声水平贡献相互抵消。因此，$\beta(t)$ 实际上表达了现有噪声被新噪声替换的相对速率。当选择 $\beta(t) = \dot{\sigma}(t)/\sigma(t)$ 时，可复现 Song 等人的 SDE，此时正向 SDE 中的得分项消失。

这一视角揭示了随机性为何在实践中有用：隐式的 Langevin 扩散会主动将样本推向给定时刻的目标边缘分布，从而**纠正早期采样步骤中产生的误差**。然而，用离散 SDE 求解器步长近似 Langevin 项本身也会引入误差。

论文通过以下方法，将二阶确定性 ODE 积分器与显式的类 Langevin “搅动”（churn）相结合：

- 添加噪声：根据因子 $\gamma_i \geq 0$ 向样本添加噪声，达到更高的噪声水平 $\hat{t}_i = t_i + \gamma_i t_i$
- ODE 反向求解：从**加噪后的样本** $\hat{x}_i$ 出发，用单步从 $\hat{t}_i$ 反向求解 ODE 至 $t_{i+1}$，得到下一状态 $x_{i+1}$
- 由于过度的类 Langevin 噪声添加与移除会导致生成图像细节逐渐丢失，在极低和极高噪声水平下，还会出现颜色过饱和的漂移，因此仅在 $[S_{t_{\min}}, S_{t_{\max}}]$ 区间内启用随机性
- 将 $S_{\text{noise}}$ 设为略微大于 1，可部分抵消细节丢失，这表明 $D_{\theta}(x; \sigma)$ 会倾向于过度去噪——这很可能是任何基于 L2 训练的去噪器都会出现的“回归均值”效应

**算法流程:**

1. 采样初始噪声: $x_0 \sim \mathcal{N}(0, t_0^2 I)$
2. 对于每一步 $i = 0, \ldots, N-1$:
    1. 确定扰动量:

    $$\gamma_i = \begin{cases}
    \min\left(\frac{S_{\text{churn}}}{N}, \sqrt{2} - 1\right) & \text{if } t_i \in [S_{t_{\min}}, S_{t_{\max}}] \\
    0 & \text{otherwise}
    \end{cases}$$

    2. 添加噪声: 
        1. $\hat{t}_i = t_i + \gamma_i t_i$
        2. $\epsilon_i \sim \mathcal{N}(0, S_{\text{noise}}^2 I)$
        3. $\hat{x}_i = x_i + \sqrt{\hat{t}_i^2 - t_i^2} \cdot \epsilon_i$
    3. 计算导数: $d_i = (\hat{x}_i - D(\hat{x}_i; \hat{t}_i)) / \hat{t}_i$
    4. Euler 步: $x_{i+1} = \hat{x}_i + (t_{i+1} - \hat{t}_i) d_i$
    5. 如果 $t_{i+1} \neq 0$，应用二阶修正:
        1. $d_i' = (x_{i+1} - D(x_{i+1}; t_{i+1})) / t_{i+1}$
        2. $x_{i+1} = \hat{x}_i + (t_{i+1} - \hat{t}_i) \cdot \frac{1}{2}(d_i + d_i')$

3. 返回 $x_N$

其中:

- $S_{\text{churn}}$: 控制整体随机性强度，典型值为 0-40
- $S_{t_{\min}}, S_{t_{\max}}$: 限制随机性作用的噪声范围，$S_{t_{\min}}$ 的典型值为 0.05，$S_{t_{\max}}$ 的典型值为 50
- $S_{\text{noise}}$: 噪声缩放因子，略大于 1 可补偿去噪器的过度去噪，典型值为 1.003-1.007

经过实验发现:

- 简单数据集（如 CIFAR-10）使用确定性采样效果更好
- 复杂数据集（如 ImageNet-64）需要适量随机性



<br>

## 预处理与训练

### 网络预处理

去噪器 $D_\theta(x; \sigma)$ 通过预处理函数与神经网络 $F_\theta$ 关联:

$$D_\theta(x; \sigma) = c_{\text{skip}}(\sigma) x + c_{\text{out}}(\sigma) F_\theta(c_{\text{in}}(\sigma) x; c_{\text{noise}}(\sigma))$$

其中:

- $c_{\text{in}}(\sigma)$: 输入缩放
- $c_{\text{out}}(\sigma)$: 输出缩放
- $c_{\text{skip}}(\sigma)$: 跳跃连接权重
- $c_{\text{noise}}(\sigma)$: 噪声条件化

推荐的预处理函数为：

$$c_{\text{skip}}(\sigma) = \frac{\sigma_{\text{data}}^2}{\sigma^2 + \sigma_{\text{data}}^2}$$

$$c_{\text{out}}(\sigma) = \frac{\sigma \cdot \sigma_{\text{data}}}{\sqrt{\sigma^2 + \sigma_{\text{data}}^2}}$$

$$c_{\text{in}}(\sigma) = \frac{1}{\sqrt{\sigma^2 + \sigma_{\text{data}}^2}}$$

$$c_{\text{noise}}(\sigma) = \frac{1}{4} \ln \sigma$$

**设计原则:**

- $c_{\text{in}}$ 和 $c_{\text{out}}$ 使训练输入和训练目标保持单位方差
- $c_{\text{skip}}$ 最小化 $c_{\text{out}}$，即最小化网络输出误差的放大
- 使网络在所有噪声水平下都面对相似幅度的信号和梯度

### 损失加权

训练损失函数加入损失权重后变为:

$$\mathbb{E}_{\sigma, y, n} \left[ \lambda(\sigma) \|D_\theta(y + n; \sigma) - y\|_2^2 \right]$$

其中:

- $\sigma \sim p_{\text{train}}(\sigma)$: 训练时的噪声水平分布
- $y \sim p_{\text{data}}$: 真实数据
- $n \sim \mathcal{N}(0, \sigma^2 I)$: 添加的噪声
- $\lambda(\sigma)$: 损失权重

展开为对 $F_\theta$ 的损失:

$$\mathbb{E}_{\sigma, y, n} \left[ \lambda(\sigma) c_{\text{out}}(\sigma)^2 \left\| F_\theta(c_{\text{in}}(\sigma) \cdot (y + n); c_{\text{noise}}(\sigma)) - \frac{1}{c_{\text{out}}(\sigma)} (y - c_{\text{skip}}(\sigma) \cdot (y + n)) \right\|_2^2 \right]$$

传统方法使用 $\lambda(\sigma) = 1/\sigma^2$，但论文为平衡不同噪声水平的损失贡献，提出一种与预处理一致的加权策略:

$$\lambda(\sigma) = \frac{1}{c_{\text{out}}(\sigma)^2} = \frac{\sigma^2 + \sigma_{\text{data}}^2}{\sigma^2 \cdot \sigma_{\text{data}}^2}$$

这样之后，不同噪声水平对于损失的贡献仅取决于噪声分布 $p_{\text{train}}(\sigma)$。

### 噪声分布

论文发现，以高斯分布采样 $\log \sigma$ 能更好地匹配真实数据中不同尺度结构的出现频率，即:

$$\ln \sigma \sim \mathcal{N}(P_{\text{mean}}, P_{\text{std}}^2)$$

推荐参数:

- $P_{\text{mean}} = -1.2$
- $P_{\text{std}} = 1.2$

**原理:**

- 经过归一化后，不同噪声水平的初始损失均为 1
- 经过充分训练后，发现较大的损失下降发生在中间噪声水平
- 极小噪声处难以区分噪声，训练意义不大
- 极大噪声处目标接近数据集均值，训练改进有限

### 数据增强

使用非泄漏增强（non-leaky augmentation）防止过拟合:

1. 对训练图像应用几何变换（旋转、平移、缩放等）
2. 将增强参数作为条件输入传递给 $F_\theta$
3. 推理时将增强参数设为零

**效果:**

- 在小数据集上显著提升性能
- CIFAR-10 无条件: FID 2.05 → 1.97
- CIFAR-10 类条件: FID 1.88 → 1.79
