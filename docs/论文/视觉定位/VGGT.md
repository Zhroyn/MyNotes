# VGGT: Visual Geometry Grounded Transformer
## Abstract
- VGGT 是一个前馈神经网络，能够直接从一张、几张或数百张图像推断场景的所有关键 3D 属性，包括相机参数、点云地图、深度图和 3D 点轨迹
- 该方法在 3D 计算机视觉领域是一个重要进步，传统方法通常受限于特定任务的专门化设计
- VGGT 简单高效，在不到一秒内完成重建，且无需后处理即可超越需要几何优化技术的替代方法
- 在多个 3D 任务中实现 SOTA 性能，包括相机参数估计、多视图深度估计、密集点云重建和 3D 点追踪
- 预训练的 VGGT 作为特征主干可显著增强下游任务，如非刚性点追踪和前馈新视图合成

<br>

## Related Work
### Structure from Motion
- **传统 SfM 管道**：COLMAP 等基于特征匹配、三角化和束调整的多阶段方法
- **深度学习改进**：
  - **关键点检测**：Superpoint、D2-Net、Disk、LIFT
  - **图像匹配**：SGMNet、Lightglue、Superglue、ClusterGNN
  - **端到端可微 SfM**：VGGSfM 等方法实现端到端可微 SfM，在挑战性场景中超越传统算法

### 多视图立体视觉
- **传统方法**：基于手工特征的立体匹配算法
- **全局优化方法**：Geo-neus、Nerfingmvs
- **基于学习的方法**：MVSNet、CasMVSNet、GeoMVSNet、CER-MVS、UniMVSNet
- **统一深度估计**：DUSt3R、MASt3R 直接从图像对估计对齐的密集点云，无需已知相机参数

### 点追踪
- **传统方法**：Particle Video 首次提出 **Tracking-Any-Point** 概念（2008）
- **深度学习时代**：
  - **PIPs 系列**：开创性的深度点追踪方法
  - **TAP-Vid**：提出三种 benchmark 以及一个简单的基线方法，后被 TAPIR 改进
  - **CoTracker**：利用点间相关性进行追踪
  - **TAPTR**：端到端 Transformer 架构
  - **LocoTrack**：将常用的点特征扩展为局部特征

### 大型视觉 Transformer
- **基础模型**：ViT、DINO、DINOv2 等在视觉任务中的成功应用
- **多模态模型**：CLIP 等展示了大规模预训练的威力
- **3D 视觉中的应用**：
  - **单任务模型**：DepthAnything (深度估计)、MoGe (几何估计)
  - **多任务学习**：少数工作尝试统一多个 3D 任务

### 快速 3D 重建
- **表示进化**：NeRF → InstantNGP → 3D Gaussian Splatting
- **前馈方法**：
  - **单图像重建**：pixelNeRF、SRN 等从单视图重建场景
  - **多视图方法**：IBRNet、MVSNeRF 等需要已知相机参数
- **实时应用需求**：VR、游戏等应用对速度的严格要求

VGGT 首次提出统一的大型 Transformer 架构，通过最小的 3D 归纳偏置直接预测所有关键 3D 属性，实现真正的端到端 3D 理解。

<br>

## Introduction
VGGT 探索是否可以通过神经网络直接解决 3D 任务，几乎完全摆脱几何后处理的需要。

### 关键特点
- **直接预测**：单次前向传播预测完整的 3D 属性集合，包括相机参数、深度图、点云地图和 3D 点轨迹
- **高效快速**：在数秒内完成，通常无需进一步处理即可超越基于优化的替代方法
- **架构简单**：基于标准的大型 Transformer，没有特殊的 3D 或其他归纳偏置（除了帧间和全局注意力的交替）
- **大规模训练**：在大量公开的 3D 标注数据集上训练，类似于 GPT、CLIP、DINO 等大型模型的构建模式

### 贡献
1. 提出 VGGT，一个大型前馈 Transformer，给定一张、几张或数百张场景图像，能在数秒内预测所有关键 3D 场景属性
2. 证明 VGGT 的预测可直接使用，具有高度竞争力且通常优于使用缓慢后处理优化技术的 SOTA 方法
3. 当进一步结合 BA 后处理时，VGGT 在各项任务中实现 SOTA 结果，即使与专门化方法相比也能大幅提升质量

<br>

## Method
### 问题定义
输入：$N$ 张 RGB 图像序列 $(I_i)_{i=1}^N$  
输出：对应的 3D 标注集合 $(g_i, D_i, P_i, T_i)_{i=1}^N$

$$ f((I_i)_{i=1}^N) = (g_i, D_i, P_i, T_i)_{i=1}^N $$

其中：

- $g_i \in \mathbb{R}^9$：相机参数（内参和外参），包括四元数 $\mathbf{q} \in \mathbb{R}^4$，平移向量 $\mathbf{t} \in \mathbb{R}^3$，FoV $\mathbf{f} \in \mathbb{R}^2$
- $D_i \in \mathbb{R}^{H \times W}$：深度图
- $P_i \in \mathbb{R}^{3 \times H \times W}$：点云地图（视点不变，在第一个相机坐标系中定义）
- $T_i \in \mathbb{R}^{C \times H \times W}$：用于点追踪的 $C$ 维特征

### 架构设计
#### 特征主干（Feature Backbone）
- **图像标记化**：使用 DINO 将每张输入图像分解为 $K$ 个 token $t_I \in \mathbb{R}^{K \times C}$
- **交替注意力（Alternating-Attention）**：
  - **帧内自注意力**：在每帧内部的 token 之间单独进行注意力计算
  - **全局自注意力**：在所有帧的 token 之间进行注意力计算
  - 默认使用 L=24 层全局和帧内注意力层
  - 不使用交叉注意力层

#### 预测头（Prediction Heads）

- 为每张输入图像增加相机 token $t_i^g \in \mathbb{R}^{1\times C'}$ 和 4 个寄存器 token $t_i^R \in \mathbb{R}^{4\times C'}$，将 $(t_i^I, t_i^g, t_i^R)_{i=1}^N$ 传入 AA，得到 $(\hat{t}_i^I, \hat{t}_i^g, \hat{t}_i^R)_{i=1}^N$
- 第一帧的相机 token 和寄存器 token 要与其他帧区分开来，以便模型区分第一帧
- $\hat{t}_i^R$ 被抛弃，$\hat{t}_i^I$ 和 $\hat{t}_i^g$ 用于后续预测


1. **坐标系**：
    - 预测的相机、点云地图、深度图都基于第一个相机 $g_1$
    - $\mathbf{q}_1$ 被设为 $[0,0,0,1]$，$\mathbf{t}_1$ 被设为 $[0,0,0]$

2. **相机预测**：
    - 相机头由 4 个额外的自注意力层 + 线性层组成
    - 输入为 $(\hat{t}_i^g)_{i=1}^N$

3. **密集预测**：
    - 使用 DPT 头将输出图像 token $\hat{t}_i^I$ 转换为密集特征图 $F_i \in \mathbb{R}^{C'' \times H \times W}$
    - 通过 3×3 卷积层映射到深度图、点图以及对应的置信度 $\Sigma_i^D$ 和 $\Sigma_i^P$

4. **点追踪**：
    - 使用另一个 DPT 头得到特征图 $T_i \in \mathbb{R}^{C \times H \times W}$
    - 使用 CoTracker2 架构处理密集追踪特征 $T_i$，即给定查询图像 $I_q$ 中的查询点 $\mathbf{y}_j$（固定取 $q=1$），通过追踪头 $\mathcal{T}$ 预测所有图像中该点对应的 2D 点
    - 具体做法是，查询点通过双线性采样从 $T_q$ 中得到对应特征，然后与其他特征图 $T_i$ （$i \neq q$）进行相关性计算得到相关性图，最后通过自注意力层处理预测最终的 2D 点 $\hat{\mathbf{y}}_i$
    $$\mathcal{T} ((\mathbf{y}_j)_{j=1}^M, (T_i)_{i=1}^N) = ((\hat{\mathbf{y}}_{j, i})_{i=1}^N)_{j=1}^M$$

### 训练策略
#### 多任务损失
$$L = \mathcal{L}_{\text{camera}} + \mathcal{L}_{\text{depth}} + \mathcal{L}_{\text{pmap}} + \lambda \mathcal{L}_{\text{track}}$$

- **相机损失**：$\mathcal{L}_{\text{camera}} = \sum_{i=1}^N \|\hat{g}_i - g_i\|_\epsilon$（Huber 损失）
- **深度损失**：$\mathcal{L}_{\text{depth}} = \sum_{i=1}^N \|\Sigma_i^D \odot (\hat{D}_i - D_i)\| + \sum_{i=1}^N \|\Sigma_i^D \odot (\nabla \hat{D}_i - \nabla D_i)\| - \alpha \log \Sigma_i^D$
- **点图损失**：$\mathcal{L}_{\text{pmap}} = \sum_{i=1}^N \|\Sigma_i^P \odot (\hat{P}_i - P_i)\| + \sum_{i=1}^N \|\Sigma_i^P \odot (\nabla \hat{P}_i - \nabla P_i)\| - \alpha \log \Sigma_i^P$
- **追踪损失**：$\mathcal{L}_{\text{track}} = \sum_{j=1}^M \sum_{i=1}^N \|\mathbf{y}_{j, i} - \hat{\mathbf{y}}_{j, i}\|$

#### 数据标准化
- **坐标系统一**：在第一个相机 $g_1$ 的坐标系中表达所有量
- **尺度标准化**：计算点云地图中所有 3D 点到原点的平均欧氏距离作为场景尺度 $s$，用此尺度标准化相机平移、点云地图和深度图
- **端到端学习**：不对 Transformer 输出的预测结果应用标准化处理；相反，强制模型从训练数据中学习我们选择的标准化方式，使输出可直接使用

#### 实现细节
- 模型约 12 亿参数
- AdamW 优化器，160K 次迭代
- 余弦学习率调度器，峰值学习率 0.0002，8K 次迭代预热
- 每批随机采样 2-24 帧，输入图像最大维度 518 像素
- 64 张 A100 GPU 训练 9 天
- **数据增强**：高宽比在 0.33 - 1 之间随机、颜色抖动、高斯模糊、灰度增强
- **内存优化**：使用梯度检查点和混合精度训练
- **多尺度训练**：在不同分辨率下训练以提高泛化性


<br>

## Experiments
### 相机位姿估计
- 在 **CO3Dv2** 和 **RealEstate10K** 数据集上评估
- VGGT 仅前馈模式就足以超过那些使用计算代价高昂的后期优化步骤的方法（如 DUSt3R 和 MASt3R 的全局对齐）
- 运行速度极快，前馈模式仅需 0.2 秒
- 将 VGGT 与 Bundle Adjustment 结合使用时，其性能还能再上一个台阶，且由于良好的初始化，速度仍然很快

### 多视图深度估计
- 在 **DTU** 数据集上评估
- 与不知道 GT camera 的方法（如 DUSt3R）相比大幅提升
- 与知道 GT camera 方法（如 GeoMVSNet）相比略有不如
- 性能提升主要得益于 VGGT 的多图像联合训练机制，使其具备天然的多视图三角化推理能力

### 点云地图估计
- 在 **ETH3D** 数据集上，将我们所预测的点云与 DUSt3R 和 MASt3R 进行比较。每个场景随机采样 10 张图像帧，将预测的点云通过 Umeyama 算法与真实点云进行配准，并使用官方掩码过滤无效点。
- 前馈模式下显著超越 DUSt3R 和 MASt3R，且速度快几十倍
- 使用深度+相机头组合比直接点云地图预测效果更好，可能是因为推理阶段的任务分解更易于学习与泛化

### 图像匹配
使用 ScanNet 数据集，具体流程如下：

- 使用 ALIKED 检测关键点，将其作为查询点传递给追踪分支，得到第二张图像中的对应点；
- 使用匹配点估计基本矩阵（Essential Matrix）；
- 再将基本矩阵分解为相对相机位姿（Relative Camera Pose）；
- 得到最终评估指标**相对位姿准确率**（AUC）。

尽管 VGGT 并未专门为两视图匹配训练，但其性能仍然超过了专门为此任务设计的 SOTA 方法（Roma）。

### 消融研究

- 特征骨干：交替注意力强于全局自注意力强于交叉注意力
- 多任务学习：丢弃任一损失项都会导致性能显著下降

### 下游任务微调
#### 前馈新视图合成
- 修改 VGGT 直接输出目标图像，无需已知输入相机参数
- 在 GSO 数据集上：PSNR 30.41，SSIM 0.949，LPIPS 0.033
- 与 LVSM 相当（后者需要已知相机参数且使用更多训练数据）

#### 动态点追踪
- 用 VGGT 预训练权重替换 CoTracker 主干
- TAP-Vid 基准测试显著提升

<br>

## Discussion
### 优势
- **简单高效**：无需复杂的几何后处理，单次前向传播完成重建
- **通用性强**：统一框架处理多个 3D 任务，易于适应新场景
- **性能卓越**：在多个基准测试中达到或超越 SOTA
- **可扩展性**：支持从单张到数百张图像的输入

### 局限性
- 不支持鱼眼或全景图像
- 极端输入旋转下重建性能下降
- 无法处理大幅非刚性变形场景
- 全局自注意力的内存消耗随 token 数量增长较快

### 未来方向
- 通过特定数据集微调解决上述局限性
- 采用大语言模型部署技术（如张量并行）加速推理
- 探索可微分 BA 在大规模训练中的应用
