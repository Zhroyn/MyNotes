
- [模型](#模型)
  - [保存和加载模型](#保存和加载模型)
  - [使用模型](#使用模型)
- [数据](#数据)
  - [Dataset](#dataset)
    - [自定义数据集](#自定义数据集)
    - [下载数据集](#下载数据集)
  - [Sampler](#sampler)
  - [DataLoader](#dataloader)
- [神经网络](#神经网络)
  - [卷积层](#卷积层)
  - [池化层](#池化层)
  - [BN 层](#bn-层)






## 模型
### 保存和加载模型
```py
# 保存整个模型的结构和参数
torch.save(model, path)

# 加载整个模型的结构和参数
model = torch.load(path)
model.eval()
```

```py
# 仅保存参数
model = nn.Model()
torch.save(model.state_dict(), path)

# 加载保存的参数到模型中
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

## 数据
### Dataset
#### 自定义数据集
PyTorch 支持两种不同类型的数据集。

映射式数据集继承 torch.utils.data.Dataset，它必须重写 \_\_getitem\_\_() 方法，用以返回指定键的数据样本，同时可以可选地重写 \_\_len\_\_()，用以返回数据集的大小。

可迭代式数据集继承 torch.utils.data.IterableDataset，它必须重写 \_\_iter\_\_() 方法，用以返回数据样本的迭代器。这适用于随机读取代价很大，以及批量大小取决于获取的数据的情况。

<br>

#### 下载数据集
**CIFAR10**
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

**ImageNet**
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

### Sampler
PyTorch 所有的采样器都是 torch.utils.data.Sampler 的子类，都要重写 \_\_iter\_\_()，用以返回一个迭代器，遍历数据集的所有索引；重写 \_\_len\_\_()，用以返回返回的迭代器的长度。

采样器不可用于可迭代式数据集，因为其不可使用索引。

- `torch.utils.data.SequentialSampler(data_source)` 按原有顺序采样，每次返回一个索引
- `torch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None, generator=None)` 随机采样，每次返回一个索引
  - `replacement` 若为 True，则可以返回相同的索引
  - `num_samples` 可以生成的样本数，默认为数据集的大小
<br>

- `torch.utils.data.BatchSampler(sampler, batch_size, drop_last)` 批次采样，每次返回一批索引
  - `drop_last` 若为 True，则会在最后一个批次的长度不足 `batch_size` 时抛弃该批次

<br>

### DataLoader
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
DataLoader 支持通过参数 batch_size, shuffle, batch_sampler, drop_last 和 collate_fn 实现自动批处理，将单个获取的数据样本整理成批次：
- `shuffle` 若为 True，则会使用随机采样器
- `sampler` 用于 `batch_sampler` 的构建，可由自己指定，不可与 `shuffle` 冲突
- `batch_sampler` 可由自己指定，不可与 `batch_size`, `shuffle`, `sampler` 和 `drop_last` 冲突
- `collate_fn` 用于处理每批从数据集加载的数据

当 batch_size 和 batch_sampler 都为 None 时，自动批处理会被禁止，DataLoader 会逐个返回样本。

DataLoader 默认使用单进程数据加载。当 num_workers 为正整数时，会打开相同数量的子进程，进行多进程数据加载，此时 dataset, collate_fn 和 worker_init_fn 会被传递给每个子进程，用于初始化和处理数据。

对于映射式数据集，每个子进程要加载的数据的索引是由主进程的采样器分发的。对于可迭代式数据集，需要使用 `torch.utils.data.get_worker_info()` 或 `worker_init_fn` 来改变每个子进程迭代的数据范围，否则会返回重复的数据。









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


