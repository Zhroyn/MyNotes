
# Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting

## 摘要

隐式神经模型的不足：

- 6D 全光函数 (6D plenoptic function) 难以拟合动态场景的空间和时间结构
- 显式地建模场景元素的变形在复杂动态场景中会变得非常困难

为了解决这个问题，我们：

- 将时空作为一个整体进行考虑
- 优化一组 4D 基本体，而不是直接优化 6D 全光函数
    - 各向异性椭圆参数化的 4D 高斯函数
    - 4D 球面谐波
  
论文技术的优点是：

- 高效的实时渲染
- 高质量的重建结果
- 提供了对可变长度视频的灵活性、端到端的训练
- 既可以通过多视角场景训练，也可以通过单目场景


## 介绍

物体运动使重建变得复杂，时间场景动态增加了显著的复杂性。此外，实际应用中通常以单目视频形式捕捉动态场景，这使得为每一帧训练单独的静态场景表示并将其组合成动态场景模型变得不切实际。核心挑战在于在不同时间步骤之间保持内在相关性和共享相关信息，同时尽量减少不相关时空位置之间的干扰。

动态新视图合成方法可以分为两类。第一类使用如 MLP 或网格等结构，包括它们的低秩分解，来学习 6D 全光函数，而是不显式地建模场景运动。这些方法在捕捉不同时空位置之间的相关性方面的有效性，取决于所选择的数据结构的固有特性。然而，它们在适应基础场景运动方面缺乏灵活性。因此，这些方法要么因时空位置之间的参数共享而遭受潜在的干扰，要么运行得过于独立，难以利用由物体运动产生的固有相关性。

相反，另一类方法认为场景动态是由一致的基础表示的运动或变形引起的。这些方法显式地学习场景运动，提供了更好利用空间和时间相关性的潜力。然而，与第一类方法相比，它们在复杂的现实场景中表现出较低的灵活性和可扩展性。

为克服这些限制，本研究通过一组 4D 高斯函数来近似场景的潜在时空 4D 体积，从而重新构建任务。值得注意的是，4D 旋转使得高斯函数能够适应 4D 流形并捕捉场景的内在运动。此外，我们引入了球圆柱谐波（Spherindrical Harmonics），作为球谐波（Spherical Harmonics）在动态场景中的推广，用于建模动态场景中外观的时间演变。这种方法标志着第一个支持端到端训练和实时渲染的模型，能够在复杂动态场景中以体积效果和变化光照条件下生成高分辨率、逼真的新视图。此外，我们提出的表示方法在空间和时间维度上都是可解释的、高度可扩展的和适应性的。

我们的贡献如下：

- 我们提出了通过无偏 4D 高斯基本体和专门的基于 splattling 的渲染管道，实现动态场景的空间和时间维度的连贯集成建模
- 我们方法中的 4D 球圆柱谐波对建模动态场景中视图依赖的颜色时间演变非常有用且易于解释
- 在各种数据集上的广泛实验（包括合成和真实、单目和多视角数据集）表明，我们的方法在视觉质量和效率方面优于所有先前的方法。值得注意的是，我们的方法能够以远超实时的速度生成逼真、高分辨率的视频

感想：建模越简单，灵活性越高，但学习更困难；建模越复杂，灵活性越低，但易于学习和渲染；建模地巧妙，才能又快又好


## 相关工作

### 静态场景的新视图合成
1. **Mildenhall et al. (2020)**: NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis
2. Chen et al. (2022): PlenOctrees for Real-time Rendering and Fast Training of Neural Radiance Fields
3. Sun et al. (2022): DirectVoxGO: Fast Optimization of Radiance Fields using Direct Voxel Grid Optimization
4. Hu et al. (2022): EfficientNeRF: Efficient Neural Radiance Fields
5. Chen et al. (2023): TensorRF: Tensorial Radiance Fields
6. Fridovich-Keil et al. (2022): Plenoxels: Radiance Fields without Neural Networks
7. Müller et al. (2022): Instant Neural Graphics Primitives with a Multiresolution Hash Encoding
8. Zhang et al. (2020): NeRF++: Analyzing and Improving Neural Radiance Fields
9. Verbin et al. (2022): Ref-NeRF: Structured View-Dependent Appearance for Neural Radiance Fields
10. Barron et al. (2021; 2022; 2023): mip-NeRF, mip-NeRF 360, SNeRG
11. **Kerbl et al. (2023)**: 3D Gaussian Splatting for Real-Time Radiance Field Rendering

### 动态场景的新视图合成
1. Li et al. (2022b): Neural Volumes: Learning Dynamic Scene Representations for Free-Viewpoint Video
2. Fridovich-Keil et al. (2023): Dynamically Dense Neural Implicit Representations
3. Cao & Johnson (2023): Dynamic Neural Representations with Implicit Deformations
4. Wang et al. (2023): Learning Neural Implicit Representations for Dynamic Scenes
5. Attal et al. (2023): Dynamic Neural Radiance Fields for View Synthesis
6. Pumarola et al. (2020): D-NeRF: Neural Radiance Fields for Dynamic Scenes
7. Song et al. (2023): Neural Scene Flow Fields for Space-Time View Synthesis of Dynamic Scenes
8. Abou-Chakra et al. (2022): Dynamic Neural Representations using Continuous Deformations
9. **Luiten et al. (2024)**: Dynamic 3d gaussians: Tracking by persistent dynamic view synthesis

### 动态 3D 高斯
1. Luiten et al. (2024): Dynamic 3d gaussians: Tracking by persistent dynamic view synthesis
2. Yang et al. (2023): Joint Optimization of Geometry and Dynamics using Canonical Space and Deformation Fields
3. Wu et al. (2023): Dynamic Scene Modeling with Gaussian Fields
4. Liang et al. (2023): Canonical Space Gaussian Splatting for Dynamic Scenes
5. Kratimenos et al. (2023): Factorized Motion Trajectories for Dynamic Scene Reconstruction
6. Chen & Wang (2024): Extending 3D Gaussian Splatting to Dynamic Scenes

这些动态 3D 高斯工作巧妙地将拓扑不变性的先验知识融入其表示中，使它们非常适合从单目视频中重建动态场景。然而，它们假设动态场景是由一组固定的 3D 高斯函数生成的，并且组成场景的元素始终可见。相比之下，通过制定一种新的 4D 场景基本体，我们摒弃了它们的基本假设，避免了保持模糊和复杂跟踪关系的需求，从而为处理现实应用中的复杂场景提供了一种更加灵活和多功能的方法。


## 方法

### 3D 高斯

#### 3D 高斯的表示

每个 3D 高斯在位置 $x$ 上的影响被定义为一个未归一化的 3D 高斯函数： 

$$
p(x|\mu, \Sigma) = e^{-\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu)}
$$

其中 $\Sigma \in \mathbb{R}^{3\times 3}$ 是一个各向异性协方差矩阵。可以证明对于未归一化的高斯函数而言 $p(u,v,t) = p(t)p(u,v|t)$ 仍然成立。

对于每个 3D 高斯而言，$\mu$ 会被参数化为 $(\mu_x, \mu_y, \mu_z)$，$\Sigma$ 会被分解为 $RSS^TR^T$，其中 $S$ 会被参数化为 $\text{diag}(s_x, s_y, s_z)$，$R$ 会被参数化为一个单位四元数。此外还会包括一系列球谐函数的系数，以及不透明度 $\alpha$。

#### 高斯溅射的可微栅格化

在渲染时，给定一个视角 $\mathcal{I}$ 的外参矩阵 $E$ 和内参矩阵 $K$，可以通过将排过序的 3D 高斯按照深度计算出在 $(u, v)$ 处的颜色：

$$
\mathcal{I}(u, v) = \sum_{i=1}^N p_i(u, v; \mu_i^{2d}, \Sigma_i^{2d}) \alpha_i c_i(d_i) \prod_{j=1}^{i-1} (1 - p_j(u, v; \mu_j^{2d}, \Sigma_j^{2d}) \alpha_j)
$$

（感觉应该错了，后面不该是 $p_j$ 吗？）

其中 

$$
\mu_i^{2d} = \text{Proj} (u_i|E, K)_{1:2}
$$

$$
\Sigma_i^{2d} = (JE\Sigma E^TJ^T)_{1:2,1:2}
$$

## 4D 高斯

### 4D 高斯溅射

加入时间维度后，易得渲染公式变为：

$$
\mathcal{I}(u, v, t) = \sum_{i=1}^N p_i(t)p_i(u, v|t) \alpha_i c_i(d_i) \prod_{j=1}^{i-1} (1 - p_j(t)p_j(u, v|t) \alpha_j)
$$

如果我们认为 $(x, y, z)$ 和 $t$ 是独立的，那么 $p_i(x, y, z|t) = p_i(x, y, z)$，只需要在 3D 高斯的基础上再加一个 1D 高斯 $p_i(t)$ 即可。这种方法可以实现四维流形的合理拟合，但很难捕捉场景的底层运动。

### 4D 高斯的表示

因此，我们需要相同地对待空间和时间，使用各维度相关的 4D 高斯函数来表示场景。此时，$\mu = (\mu_x, \mu_y, \mu_z, \mu_t)$，$S = \text{diag}(s_x, s_y, s_z, s_t)$，$R$ 由两个表示左右各向同性旋转的四元数构成，即，对于 $q_l = (a, b, c, d)$ 和 $q_r = (p, q, r, s)$，有：

$$
R = L(q_l) L(q_r) = 
\begin{pmatrix}
  a & -b & -c & -d \\
  b & a & -d & c \\
  c & d & a & -b \\
  d & -c & b & a \\
\end{pmatrix}
\begin{pmatrix}
  p & -q & -r & -s \\
  q & p & s & -r \\
  r & -s & p & q \\
  s & r & -q & p \\
\end{pmatrix}
$$

有了这个以后，我们就能通过多元高斯函数的性质得出条件高斯函数：

$$
\mu_{xyz|t} = \mu_{1:3} + \Sigma_{1:3,4} \Sigma_{4,4}^{-1} (t - \mu_t)
$$

$$
\Sigma_{xyz|t} = \Sigma_{1:3,1:3} - \Sigma_{1:3,4} \Sigma_{4,4}^{-1} \Sigma_{4,1:3}
$$

有了 $p_i(x, y, z|t)$ 以后，就可以像上述 3D 高斯一样得到 $p_i(u, v|t)$。

另一个边际分布则为 $p(t) = \mathcal{N}(t; \mu_4, \Sigma_{4,4})$。

#### 4D 球谐函数

原本的球谐函数只考虑到了空间维度，没有考虑时间维度，因此，我们可以将原本的球谐函数和傅里叶级数结合起来，得到有四维扩展的球谐函数 4DSH：

$$
Z_{nl}^{m} (t, \theta, \phi) = \cos \left( \frac{2\pi n}{T}t \right) Y_{l}^{m} (\theta, \phi)
$$

其中 $l$ 是阶数，$m \in [-l, l]$ 是球谐函数阶数内的序号，$n$ 是傅里叶级数的序号。

这样一来，$c_i(d)$ 就变成了 $c_i(d, t)$，其中 $d = (\theta, \phi)$。


## 训练

在优化环节，我们仅利用渲染损失作为监督。在大多数场景中，将前面介绍的表示法结合 Kerbl 等人(2023)默认的训练计划，就足以获得令人满意的结果。但是，在一些变化更为剧烈的场景中，我们会遇到诸如时间闪烁和抖动等问题。我们认为这些问题可能是由于采样技术不够理想造成的。相反于采用先验正则化，我们发现简单的时间批量采样实际上表现更佳，能生成更连贯且视觉上更吸引人的动态视觉内容。

在时空中的密度控制方面，仅仅考虑视图空间位置梯度的平均大小不足以评估随时间变化的欠重建和过度重建情况。为了解决这个问题，我们将时间平均梯度 $\mu_t$ 作为额外的密度控制指标纳入考量。此外，在那些容易发生过度重建的区域，我们在进行高斯斑点的分裂时，采用空间和时间位置的联合采样策略。


## 消融分析

- 全相干的、无约束的、不严格区分时空间的 4D 高斯函数优于受约束的基线模型
- 对于每一个高斯分布，我们检验了由其条件分布的期望值 $\mu_{xyz|t}$ 形成的在空间中的轨迹，渲染得到估算的光流。实验显示，通过 4D 高斯分布及其 4D 旋转特性，我们能够捕捉到场景中物体的三维运动趋势。即使没有专门的运动信息指导，仅通过最小化渲染误差，系统就能够自发地识别和呈现场景的基本动态特性
- 有 4DSH 优于无 4DSH
- 允许高斯分布随着时间进行分割，通过使用完整的四维高斯分布作为概率密度函数 (PDF) 来采样新的位置，优于仅能在空间上分裂

## 4D 高斯的时间特征

如果 4D 高斯分布仅在时间上具有局部支持，就像 3D 高斯在空间上的局部支持一样，随着视频长度的增加，所需 4D 高斯的数量可能会变得难以管理。幸运的是，高斯分布的各向异性特征为避免这一困境提供了可能。为了进一步发挥这一特性的潜力，我们将初始时间缩放设置为场景持续时间的一半。

为了更直观地理解拟合的 4D 高斯分布的时间分布，图 8 和图 9 展示了一组关于时间维度均值和方差的可视化，借此可以完全描述 4D 高斯分布关于时间 t 的边际分布。可以观察到，这些统计量自然形成了一种掩模，清晰地区分了动态区域和静态区域，其中背景高斯分布具有较大的时间维度方差，意味着它们能够覆盖较长的时间段。这使得随着视频长度的延长，总高斯数目的增长受到非常严格的限制。

此外，考虑到在剔除视锥体前，我们根据边缘概率 pi(t) 对高斯分布进行过滤，几乎不会消耗时间，参与每帧渲染的实际高斯数目几乎是恒定的。因此，随着视频长度的增加，渲染速度倾向于保持稳定。这种局部性反而使得我们的方法在渲染速度上对长视频更加友好。

在图 10 中，我们直接展示了在不同视频长度下总高斯数目及真正参与给定帧光栅化过程的高斯数目。可以看出，几百帧视频上拟合的 4D 高斯总数实际上并没有比单帧上拟合的 3D 高斯数目大很多，而且每帧真正用于渲染的 4D 高斯平均数目是稳定的。

我们在图 11 中比较了两种变体（No-4DRot 和 Full）切片 3D 高斯分布的情况。很明显，在 No-4DRot 设置下，轮子的边缘未能很好地重建，尽管在这种配置下拟合的高斯总数更大，但在过滤后参与渲染显示帧的高斯分布却更少。这表明，在 No-4DRot 设置下的 4D 高斯在时间上具有较少的变化，这损害了运动拟合能力和连续帧之间信息交换的能力，导致渲染视频中出现更多的闪烁和模糊。
