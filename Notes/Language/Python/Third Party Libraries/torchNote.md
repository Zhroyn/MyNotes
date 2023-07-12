<!-- TOC -->

- [模型](#模型)
  - [保存和加载模型](#保存和加载模型)
  - [使用模型](#使用模型)
- [数据集](#数据集)
  - [下载数据集](#下载数据集)
    - [CIFAR10](#cifar10)
    - [ImageNet](#imagenet)
  - [加载数据集](#加载数据集)
- [神经网络](#神经网络)
  - [卷积层](#卷积层)
  - [池化层](#池化层)
  - [BN 层](#bn-层)

<!-- /TOC -->




## 模型
### 保存和加载模型
```py
# 保存整个模型网络结构和参数
torch.save(model, path)

model = torch.load(path)
model.eval()
```

```py
# 仅保存参数
model = nn.Model()
torch.save(model.state_dict(), path)

model = nn.Model()
model.load_state_dict(torch.load(path))
model.eval()
```





<br>

### 使用模型
```py
# 加载模型
model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
model.eval()

# 图像预处理
norm_mean = [0.485, 0.456, 0.406]
norm_std = [0.229, 0.224, 0.225]

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(norm_mean, norm_std),
])

img = Image.open(img_path)
img_tensor = preprocess(img)
img_input = img_tensor.unsqueeze(0)

# 获取标签
output = model(img_input)
predicted_index = torch.max(output, 1)[1]
predicted_label = labels[predicted_index.item()]
```






<br>

## 数据集
### 下载数据集
#### CIFAR10
```py
torchvision.datasets.CIFAR10(
    root: str,
    train: bool = True,
    transform: Optional[Callable] = None,
    target_transform: Optional[Callable] = None,
    download: bool = False,
) -> None
```
- `root` 若根目录下没有 ``cifar-10-batches-py`` 且 `download` 设为 True，下载并保存于此
- `train` 若为 True，则创建训练集，否则为测试集
- `transform` 将 PIL 图像转换的函数
- `target_transform` 将目标转换的函数
- `download` 若为 True 且数据集不存在，则从 Internet 下载

<br>

#### ImageNet
```py
torchvision.datasets.ImageNet(
    root: str,
    split: str = 'train',
    **kwargs: Any,
) -> None
```
- `split` 支持 `train` 和 `val`
- `transform` 将 PIL 图像转换的函数
- `target_transform` 将目标转换的函数
- `loader` 加载图像的函数，以图像路径为参数






<br>

### 加载数据集
```py
torch.utils.data.DataLoader(
    dataset: torch.utils.data.dataset.Dataset[+T_co],
    batch_size: Optional[int] = 1,
    shuffle: Optional[bool] = None,
    sampler: Union[torch.utils.data.sampler.Sampler, Iterable, NoneType] = None,
    batch_sampler: Union[torch.utils.data.sampler.Sampler[Sequence], Iterable[Sequence], NoneType] = None,
    num_workers: int = 0,
    collate_fn: Optional[Callable[[List[~T]], Any]] = None,
    pin_memory: bool = False,
    drop_last: bool = False,
    timeout: float = 0,
    worker_init_fn: Optional[Callable[[int], NoneType]] = None,
    multiprocessing_context=None,
    generator=None,
    *,
    prefetch_factor: int = 2,
    persistent_workers: bool = False,
    pin_memory_device: str = '',
)
```
- `dataset` 加载数据的数据集
- `batch-size` 每个批次加载的样本数
- `shuffle` 若为 True，则在每个 epoch 后重新排列数据
- `num_workers` 用于加载数据的子进程数

<br>

```py
def imshow(img):
    img = img / 2 + 0.5
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

for step, data in enumerate(trainloader, 0):
    if step < 3:
        images, labels = data
        imshow(torchvision.utils.make_grid(images))
```






<br>

## 神经网络
### 卷积层
```py
nn.Conv2d(
    in_channels: int,
    out_channels: int,
    kernel_size: Union[int, Tuple[int, int]],
    stride: Union[int, Tuple[int, int]] = 1,
    padding: Union[str, int, Tuple[int, int]] = 0,
    dilation: Union[int, Tuple[int, int]] = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = 'zeros',
    device=None,
    dtype=None,
) -> None
```
- `kernel_size` 若卷积核的宽和高相同，则可以用 int，否则必须用 tuple

<br>

### 池化层
```py
nn.MaxPool2d(
    kernel_size: Union[int, Tuple[int, ...]],
    stride: Union[int, Tuple[int, ...], NoneType] = None,
    padding: Union[int, Tuple[int, ...]] = 0,
    dilation: Union[int, Tuple[int, ...]] = 1,
    return_indices: bool = False,
    ceil_mode: bool = False,
) -> None
```
- `stride` 默认值为 `kernel_size`

<br>

### BN 层
```py
nn.BatchNorm2d(
    num_features: int,
    eps: float = 1e-05,
    momentum: float = 0.1,
    affine: bool = True,
    track_running_stats: bool = True,
    device=None,
    dtype=None,
) -> None
```
- `num_features` 特征的通道数
- `eps` 用来防止归一化时除零


