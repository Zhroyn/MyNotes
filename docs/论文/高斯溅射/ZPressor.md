# ZPressor: Bottleneck-Aware Compression for Scalable Feed-Forward 3DGS
## Abstract
- 前馈 3D 高斯溅射（Feed-forward 3DGS）模型可以在无需逐场景优化的情况下实现单次推理，但受编码器容量限制，随着输入视图数量增加会导致性能下降或内存消耗过度
- 本文通过信息瓶颈（Information Bottleneck）原理分析前馈 3DGS 框架，提出了 ZPressor——一个轻量级的、架构无关的模块
- ZPressor 能够将多视图输入高效压缩为紧凑的潜在状态 Z，保留重要的场景信息同时去除冗余
- 通过将视图分为锚点集和支持集，使用交叉注意力将支持视图信息压缩到锚点视图中，使得现有前馈 3DGS 模型能够在 80GB GPU 上处理超过 100 个 480P 分辨率的输入视图

<br>

## Related Work
### 信息瓶颈及其应用

- **信息瓶颈（IB）原则**：
    - 旨在从输入 $X$ 中提取压缩表示 $Z$，使得 $Z$ 对目标 $Y$ 信息最大化。
    - 被扩展到深度学习领域，如：
        - 深度变分信息瓶颈（Deep Variational Information Bottleneck）：提出IB目标的可行下界，连接理论与实际应用。
- **在多视图输入中的应用**：
    - 多项研究尝试利用IB从多视图中提取共享信息、丢弃冗余和视角特有信息。
- **在3D场景重建领域的信息论方法**：
    - StreamGS：通过跨帧特征聚合合并冗余的高斯，压缩图像流中的冗余。
    - 其他工作：集中于压缩已学习的3D高斯。
    - 尚未在前馈3DGS中引入IB进行信息压缩 —— 本文旨在填补这一空白。

### 基于优化的NeRF与3DGS

- **传统的新视图合成方法**：
    - 多使用图像混合技术实现。
- **神经渲染方法**：
    - NeRF：利用MLP映射3D位置与观察方向至颜色和密度。
    - 多项研究提高其效率与重建质量，但由于体积渲染较慢，影响实际应用。
- **3D Gaussian Splatting（3DGS）及其变种**：
    - 使用显式表示和基于光栅化的快速渲染，效率超过NeRF。
    - 尽管高效，但仍需慢速的逐场景优化，限制了其实际部署。

### 前馈式NeRF与3DGS（Feed-forward NeRF and 3DGS）

- **PixelNeRF**：首次引入编码器以实现前馈式NeRF，可以一次性推理出场景表示。
- **前馈式3DGS研究进展**：
    - pixelSplat：结合双视图的 epipolar transformer 与深度预测来生成高斯。
    - MVSplat：使用成本体积融合策略改善多视图重建。
    - DepthSplat：利用单目深度特征从稀疏输入中恢复细粒度结构。
- **局限性**：
    - 多采用像素对齐设计，预测的3D高斯数随输入视图线性增长，导致内存和计算开销剧增。
    - 如FreeSplat和GGN尝试通过跨视图合并减少高斯数量，但缺乏理论支撑。
- **本文贡献**：
    - 引入信息瓶颈理论视角，分析信息过载问题。
    - 提出架构无关的压缩模块——ZPressor，用于提升前馈式3DGS在密集视图输入下的表现。

<br>

## Introduction
前馈 3DGS 模型通过引入编码器从输入图像中提取场景相关特征，避免了传统 3DGS 方法需要逐场景优化的限制，但仍受限于少量输入视图。

### 贡献
- 通过信息瓶颈原理分析为什么现有前馈 3DGS 模型在密集输入视图下表现不佳，识别出**编码器容量有限**是根本原因
- 受 IB 启发，提出 ZPressor——一个**架构无关**的模块，可集成到现有前馈 3DGS 模型的编码器中来压缩输入视图信息
- 大量实验表明，ZPressor 在中等输入视图数量下持续改善基线模型性能，在密集输入设置下增强鲁棒性

<br>

## Methodology
### Information Bottleneck 原理
前馈 3DGS 网络在输入视图信息增长时遭受性能急剧下降和计算成本指数增长，主要由于信息冗余和缺乏自适应信息压缩机制。

信息瓶颈（IB）原理通过最小化 IB 分数来建模：

$$\min_\mathcal{Z} IB = \beta I(\mathcal{X},\mathcal{Z}) - I(\mathcal{Z},\mathcal{Y})$$

其中：

- $I(\cdot, \cdot)$ 是互信息（mutual information），$\mathcal{X}$ 是输入 ZPressor 的图像和视角特征，$\mathcal{Z}$ 是压缩后的潜在状态，$\mathcal{Y}$ 是输出的 3DGS 参数
- **压缩分数** $\beta I(\mathcal{X},\mathcal{Z})$：鼓励 $\mathcal{Z}$ 成为输入 $\mathcal{X}$ 的简洁表示
- **预测分数** $I(\mathcal{Z},\mathcal{Y})$：确保 $\mathcal{Z}$ 保留关于目标变量 $\mathcal{Y}$ 的足够任务相关信息

### ZPressor 架构
ZPressor 将 $K$ 个输入视图 $\mathcal{X}$ 分为：

- **锚点视图** $\mathcal{X}_{anchor} = \{F_{a_i}\}_{i=1}^N$：捕获场景的基本信息
- **支持视图** $\mathcal{X}_{support} = \{F_{s_j}\}_{j=1}^M$：包含支持上下文但可能有冗余

#### 三个关键设计问题：
1. **如何选择锚点视图**：从相机位置（与视图通过 $f$ 双射） $\mathcal{T} = \{T_{i}\}_{i=1}^K$ 中随机选择一个对应的视图作为初始锚点视图，得到 $S = \{T_{a_1}\}$，然后依次选择距离当前锚点视图集合最远的视图作为下一个锚点视图：

    $$T_{a_{i+1}} = \argmax_{T_j \in T\setminus S} \left( \min_{T_k \in S} d(T_j, T_k) \right)$$

2. **如何分配支持视图**：将每个支持视图分配给最近的锚点视图：

    $$\mathcal{C}_i = \{f(T) \in \mathcal{X}_{support} | \|T - T_{a_i}\| \leq \|T - T_{a_j}\|, \forall j \neq i\}$$

3. **如何融合信息**：通过交叉注意力机制融合信息

    $$\mathcal{Z} = \text{Cross-Attn}(Q, K, V), \quad Q \leftarrow \mathcal{X}_{anchor}, \quad K,V \leftarrow \mathcal{X}_{support}$$

#### 训练策略
- **压缩分数**：通过设置锚点视图数量 $N$ 来约束复杂度
- **预测分数**：根据互信息的定义 $I(\mathcal{Z};\mathcal{Y}) = H(\mathcal{Y}) - H(\mathcal{Y}|\mathcal{Z})$，其中：
    - $H(\mathcal{Y})$ 是**熵函数**，表示 3D 高斯参数 $\mathcal{Y}$ 的不确定性，是一个常数（代表底层 3D 场景建模的固有复杂度）
    - $H(\mathcal{Y}|\mathcal{Z})$ 是**条件熵**，表示给定压缩表示 $\mathcal{Z}$ 后，3D 高斯参数 $\mathcal{Y}$ 的剩余不确定性
    - 因此最大化 $I(\mathcal{Z};\mathcal{Y})$ 等价于最小化 $H(\mathcal{Y}|\mathcal{Z})$，即减少预测的不确定性，使预测的 3D 高斯更接近真实场景
    - 使用变分渲染损失（如 MSE 和 LPIPS）来优化
- 通过自注意力层和多块堆叠（每个块包含交叉注意力和自注意力）来进一步提升性能

<br>

## Experiments
### 实验设置
- **数据集**：DL3DV-10K（51.3M 帧，10,510 个真实场景）和 RealEstate10K（10M 帧，80,000 个视频片段）
- **基线模型**：DepthSplat、MVSplat、pixelSplat
- **评估指标**：PSNR、SSIM、LPIPS，以及运行时间和内存消耗

### 主要结果
1. **性能提升**：在所有输入视图设置和评估指标上一致改善基线模型性能
    - DepthSplat + ZPressor（36视图）：PSNR 提升 4.65dB
    - 输入视图越多，性能提升越显著

2. **模型效率**：随着输入视图数量增加，DepthSplat 的高斯数量、推理时间与内存消耗均呈线性增长，而 DepthSplat + ZPressor 则基本保持不变

3. **瓶颈约束分析**：不同场景覆盖范围（用帧之间的距离表示）需要的锚点视图数量
    - 低信息场景（Context Gap 50）：锚点数量从 7 到 9，表现不断下降
    - 高信息场景（Context Gap 100）：锚点数量从 7 到 9，表现逐渐提升，说明高信息场景有更高的信息瓶颈

4. **信息融合**：没有支持视图的信息融合，或只在锚点视图上进行融合，会导致性能轻微下降

### 消融研究
对堆叠注意力块的效果进行消融研究，发现没有自注意力或者多块堆叠均会导致性能轻微下降。
