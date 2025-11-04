# 模型架构

## 2D UNet

以 Hugging Face Diffusers 库中的 UNet2DConditionModel 为例，它是一个带文本条件输入的 2D UNet，由以下几个关键组件组成：

- 下采样模块：下采样路径，提取多尺度特征
- 中间模块：最深层的特征处理
- 上采样模块：上采样路径，逐步重建图像
- 跳跃连接（Skip Connections）：将编码器对应层的特征拼接到解码器，保留细节
- 条件注入（Conditioning）：通过 Cross-Attention 和 Time Embedding 融合文本/时间信息

输入为：

- `sample`: 带噪声的 latent 图像，形状为 `(B, C, H, W)`，其中 `C` 为通道数，需要等于 UNet2DConditionModel 的 `in_channels` 参数，默认值为 4
- `timestep`: 时间步，形状为 `(B,)`
- `encoder_hidden_states`: 条件信号（如文本嵌入），形状为 `(B, L, D)`，其中 `L` 为序列长度，`D` 为 embedding 特征维度，需要等于 UNet2DConditionModel 的 `cross_attention_dim` 参数，默认值为 1280

下面来依次讲解输入经过默认的 UNet 的各个部分时会发生什么。

首先是时间步嵌入（Time Embedding），`timestep` 会通过正弦位置编码被编码为高维向量，然后经过一个由全连接层、SiLU 激活函数和另一个全连接层组成的 MLP，得到最终的时间步嵌入向量，形状为 `(B, 1280)`。

潜变量 `sample` 会首先经过一个卷积层，通道数从 4 变成 320，然后依次经过由 3 个 CrossAttnDownBlock2D 和 1 个 DownBlock2D 组成的**下采样模块**（由 `down_block_types` 列表决定）。

**CrossAttnDownBlock2D** 由 ResNetBlock2D、Transformer2DModel 和 Downsample2D 组成：

- ResNetBlock2D 和 Transformer2DModel 一起组成一层，默认会重复两次，由 `layers_per_block = 2` 参数控制
- **ResNetBlock2D** 包含 GroupNorm、Dropout、SiLU 激活函数和两个 Conv2d 卷积层（不改变通道数），**时间步嵌入向量**会通过线性层投影到对应尺度后，加到两个卷积层之间的中间特征上
- **Transformer2DModel** 包含 GroupNorm、两个 Conv2d 和一个 BasicTransformerBlock，BasicTransformerBlock 会先进行一次自注意力（因为 `only_cross_attention` 默认为 False），再通过交叉注意力融合**条件信息**，最后经过 FeedForward 层处理。
- **Downsample2D** 仅包含一个步幅为 2 的卷积层，用于将**高和宽减半**
- 后两个 CrossAttnDownBlock2D 中的第一个 ResNetBlock2D 中的第一个卷积层会**将潜变量通道数翻倍**，从 320 变成 640 再变成 1280
- 在 Transformer2DModel 中，潜变量会先经过不会改变通道数的卷积层，再被展平成 `(B, H*W, C)` 形状进行注意力计算，计算完成后再恢复成 `(B, C, H, W)` 形状以通过第二个卷积层
- 在 Transformer2DModel 中，head 的数量为 8，head 的维度为潜变量通道数除以 8

DownBlock2D 仅有两个 ResnetBlock2D 组成，不会改变通道数和宽高，潜变量会保持 `(B, 1280, H/8, W/8)` 的形状。

在了解了下采样模块后，中间模块和上采样模块也就很好理解了：

- **中间模块**依次由 ResNetBlock2D、Transformer2DModel 和 ResNetBlock2D 组成，处理后的潜变量形状仍为 `(B, 1280, H/8, W/8)`
- **上采样模块**由 1 个 UpBlock2D 和 3 个 CrossAttnUpBlock2D 组成（由 `up_block_types` 列表决定）
    - **UpBlock2D** 仅包含三个 ResNetBlock2D 和一个 Upsample2D，其中 ResNetBlock2D 不会改变通道数，Upsample2D 会通过插值再卷积的方法将**高和宽翻倍**
    - **CrossAttnUpBlock2D** 结构与 CrossAttnDownBlock2D 类似，由 Resnet + Transformer 结构和 Upsample2D 组成，但是 Resnet + Transformer 结构会比 CrossAttnDownBlock2D 多一个，多的一个是为了拼接 Downsample2D 输出的残差特征
    - 由于 UpBlock2D 中已经有了一个 Upsample2D，所以最后一个 CrossAttnUpBlock2D 不会再进行上采样
    - 后两个 CrossAttnUpBlock2D 中的第一个 ResNetBlock2D 中的第一个卷积层会**将潜变量通道数减半**，从 1280 变成 640 再变成 320

需要注意的是，UNet2DConditionModel 通过拼接的方式，将下采样模块中每个 Block 输出的特征与上采样模块中对应的 Block 输入的特征进行 concat，从而实现**跳跃连接**（Skip Connections）。具体来说：

- 每经过一层 Resnet + Transformer 或者 Downsample2D，都会将该层输出保存下来作为后续跳跃连接的残差
- 最开始通道数为 320 的输入也会被保存下来，作为最后一个残差
- 三个 CrossAttnDownBlock2D 输出的残差的通道数依次为 320、320、320；640、640、640；1280、1280、1280
- DownBlock2D 输出的残差的通道数依次为 1280、1280
- UpBlock2D 拼接的残差通道数依次为 1280、1280、1280
- CrossAttnUpBlock2D 拼接的残差通道数依次为 1280、1280、640；640、640、320；320、320、320

最后输出会依次经过 GroupNorm、SiLU 激活函数和一个 Conv2d 卷积层，将通道数从 320 变回 4，得到最终的去噪潜变量，形状为 `(B, 4, H, W)`。





## 3D UNet

以 Hugging Face Diffusers 库中的 UNet3DConditionModel 为例，它与 2D UNet 类似，但适用于处理视频等数据。它的输入为：

- `sample`: 带噪声的 3D latent 图像，形状为 `(B, C, F, H, W)`，其中 `F` 为帧数
- `timestep`: 时间步，形状为 `(B,)`
- `encoder_hidden_states`: 条件信号（如文本嵌入），形状为 `(B, L, D)`

在 3D UNet 中，时间步嵌入的处理与 2D UNet 相同，而输入的预处理则不同。`sample` 会先变换成 `(B*F, C, H, W)` 形状再经过卷积层，通道数从 4 变成 320 然后再经过 **TransformerTemporalModel** 处理：

- 先变换成 `(B, C, F, H, W)` 形状做归一化
- 再变换成 `(B*H*W, F, C)` 形状在帧间进行一次自注意力计算
- 再变换回 `(B*F, C, H, W)` 形状加上残差返回

**下采样模块**由 3 个 CrossAttnDownBlock3D 和 1 个 DownBlock3D 组成：

- **CrossAttnDownBlock3D** 由两层 ResNetBlock2D + TemporalConvLayer + Transformer2DModel + TransformerTemporalModel 结构和一层 Downsample2D 组成
    - **ResNetBlock2D**、**Transformer2DModel**、**Downsample2D** 与 2D UNet 中相同，只是输入变成了 `(B*F, C, H, W)` 形状
    - **TemporalConvLayer** 会将输入变换为 `(B, C, F, H, W)` 形状，经过 4 个 Conv3d 层后加上残差，再变回 `(B*F, C, H, W)` 形状输出
    - **TransformerTemporalModel** 会如上所述在帧间进行一次自注意力计算
    - Transformer2DModel 和 TransformerTemporalModel 默认有 `out_channels / 64` 个 head，每个 head 的维度为 64
- **DownBlock3D** 由两层 ResNetBlock2D + TemporalConvLayer 结构组成

**中间模块**由一层 ResNetBlock2D + TemporalConvLayer 结构，和一层 ResNetBlock2D + TemporalConvLayer + Transformer2DModel + TransformerTemporalModel 结构组成。

**上采样模块**由 1 个 UpBlock3D 和 3 个 CrossAttnUpBlock3D 组成：

- **UpBlock3D** 由三层 ResNetBlock2D + TemporalConvLayer 结构和一层 Upsample2D 组成
- **CrossAttnUpBlock3D** 由三层 ResNetBlock2D + TemporalConvLayer + Transformer2DModel + TransformerTemporalModel 结构和一层 Upsample2D 组成
- 和 CrossAttnDownBlock2D 一样，由于 UpBlock3D 中已经有了一个 Upsample2D，所以最后一个 CrossAttnUpBlock3D 不会再进行上采样
