
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
### 自定义神经网络
PyTorch 提供了多种类用于自定义神经网络，其中最基础的就是 torch.nn.Module。所有神经网络都是 Module 的子类，必须重写 \_\_init\_\_() 和 forward() 方法。

此外，还有 Sequential, ModuleList, ModuleDict 等容器可用于快速构建网络。其中，Sequential 可用于顺序串联各层，直接构建网络：
```py
model = nn.Sequential(
          nn.Conv2d(1,20,5),
          nn.ReLU(),
          nn.Conv2d(20,64,5),
          nn.ReLU()
        )

model = nn.Sequential(OrderedDict([
          ('conv1', nn.Conv2d(1,20,5)),
          ('relu1', nn.ReLU()),
          ('conv2', nn.Conv2d(20,64,5)),
          ('relu2', nn.ReLU())
        ]))
```

ModuleList 可用于构建具有重复特性的网络，可像列表一样使用索引，其包含的模块会被正确注册：
```py
class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.linears = nn.ModuleList([nn.Linear(10, 10) for i in range(10)])

    def forward(self, x):
        for i, l in enumerate(self.linears):
            x = self.linears[i // 2](x) + l(x)
        return x
```

ModuleDict 可用于构建动态网络，可像字典一样使用索引，其包含的模块会被正确注册：
```py
class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.choices = nn.ModuleDict({
                'conv': nn.Conv2d(10, 10, 3),
                'pool': nn.MaxPool2d(3)
        })
        self.activations = nn.ModuleDict([
                ['lrelu', nn.LeakyReLU()],
                ['prelu', nn.PReLU()]
        ])

    def forward(self, x, choice, act):
        x = self.choices[choice](x)
        x = self.activations[act](x)
        return x
```


<br>

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
- `num_features` 特征数，对于全连接层来说是向量长度，对于卷积层来说是通道数
- `eps` 用来防止归一化时除零


<br>

### 激活函数
- `torch.nn.ReLU(inplace=False)`
    - `inplace` 若为 True，则会改变输入的原有值
- `torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)`
- `torch.nn.ELU(alpha=1.0, inplace=False)`
    - `alpha` 小于零时的系数
- `torch.nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)`
    - `num_parameters` 要学习的 $a$ (小于零时的系数) 的数量，只能等于 1 或者输入的通道数
    - `init` $a$ 的初始值
<br>

- `torch.nn.Softmax(dim=None)`


<br>

### 损失函数
- `torch.nn.L1Loss(size_average=None, reduce=None, reduction='mean')` L1 范数损失 $$l_n = |x_n - y_n|$$
    - `size_average` 已弃用
    - `reduce` 已弃用
    - `reduction` 指定对输出的处理
        - `'none'` 不做处理，保持原有形状
        - `'mean'` 取平均值
        - `'sum'` 取总和
<br>

- `torch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')` 均方误差损失 $$l_n = (x_n - y_n)^2$$
<br>

- `torch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=- 100, reduce=None, reduction='mean', label_smoothing=0.0)` 交叉熵损失 $$l_n = -w_{y_n} \log \frac{\exp(x_{n,y_n})}{\sum_{c=1}^C \exp(x_{n,c})} $$


