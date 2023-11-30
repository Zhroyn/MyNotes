
- [Array](#array)
  - [属性](#属性)
  - [生成数组](#生成数组)
  - [转换类型](#转换类型)
  - [合并拆分](#合并拆分)
  - [改变形状](#改变形状)
  - [转置翻转](#转置翻转)
  - [数值计算](#数值计算)
  - [其他方法](#其他方法)
- [Random](#random)
  - [生成随机数](#生成随机数)
  - [随机选择](#随机选择)
  - [随机排序](#随机排序)
- [Broadcasting](#broadcasting)







## Array
### 属性
- `a.dtype` 数组的数据类型
- `a.flags` 返回内存布局的信息
- `a.itemsize` 每个元素的字节长度
- `a.ndim` 数组的维度数
- `a.size` 数组的元素数
- `a.shape` 各维度的长度组成的元组
- `a.strides` 各维度前进一步所需跨越的字节数组成的元组
<br>

- `a.data` 返回指向数据块的 buffer 对象
- `a.flat` 返回数组的 flatitier 对象
- `a.base` 若使用的内存来自别的对象，则返回原对象，否则返回 None
<br>

- `a.__array_interface__` 返回 (数据块地址, 是否只读)


<br>

### 生成数组
- `np.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)`
  - `dtype` 数据类型
    - `'u1'` 等效于 `'uint8'` 和 `np.uint8`
    - `'i'` `'i4'` 等效于 `'int32'` 和 `np.int32`
    - `'f'` `'f4'` 等效于 `'float32'` 和 `np.float32`
  - `copy` 若为 True 则深拷贝 object，否则视情况而决定是否拷贝
  - `order` 内存布局，若 object 非数组则默认为 C 顺序
  - `subok` 若为 True 则 array 的子类的类别会被保留，否则会强制转换
  - `ndmin` 最小的维度数，1 会被用来填充空白
<br>

- `np.empty(shape, dtype=float, order='C', *, like=None)` 返回未初始化的数组
- `np.zeros(shape, dtype=float, order='C', *, like=None)` 返回初始化为 0 的数组
- `np.ones(shape, dtype=float, order='C', *, like=None)` 返回初始化为 1 的数组
- `np.full(shape, fill_value, dtype=None, order='C', *, like=None)` 返回初始化为指定值的数组
  - `dtype` 默认为 `np.array(fill_value).dtype`
<br>

- `np.arange([start,] stop[, step,], dtype=None, *, like=None)`
  - `start`, `stop` 和 `step` 支持使用浮点数
  - `dtype` 若为 None 则从其他参数中推断
- `np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)`
  - `num` 生成的样本数，默认为 50
  - `endpoint` 若为 True 则会包含 `stop`
  - `retstep` 若为 True 则返回的是 (样本, 步长)
  - `dtype` 若为 None 则从其他参数中推断，但绝不会是整数
<br>

- `np.meshgrid(*xi, copy=True, sparse=False, indexing='xy')` 生成网格点坐标矩阵，返回的坐标矩阵数等于输入的坐标向量数
  - `copy` 若为 False，则只会返回原有数组的视图
  - `indexing` 坐标矩阵的索引方式，假设坐标向量的长度依次为 M, N, P
    - `'xy'` 网格点先沿横轴展开，坐标矩阵的形状为 (M, N) 或 (M, N, P)
    - `'ij'` 网格点先沿纵轴展开，坐标矩阵的形状为 (N, M) 或 (N, M, P)


<br>

### 转换类型
- `np.asarray(a, dtype=None, order=None, *, like=None)` 将输入数据转换为数组
  - 已存在的数组不会被拷贝
  - 若设置了 `dtype`，则只有当数据类型不匹配时会拷贝
- `np.asfarray(a, dtype=<class 'numpy.float64'>)` 强制转换为数据类型为 float64 的数组
  - 只有当数据类型不匹配时会拷贝
<br>

- `a.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)` 返回数组的副本，已被转换为指定数据类型



<br>

### 合并拆分
- `np.concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")` 沿指定维度连接多个数组，返回副本
  - `a1, a2, ...` 除了 `axis` 指定的维度，其他维度必须相同
  - `axis` 用于连接的维度的索引，若为 None 则会先展平数组
  - `out` 结果输出的数组，形状需与输出相同，此时返回的也是该数组
<br>

- `np.stack(arrays, axis=0, out=None, *, dtype=None, casting='same_kind')` 沿**新的维度**连接多个数组，返回副本
  - `arrays` 所有数组应有相同的形状
  - `axis` 新的维度的索引
- `np.vstack(tup, *, dtype=None, casting='same_kind')` 沿第一个维度连接多个数组，返回副本，一维数组的形状会转换为 (1, N)
  - `tup` 除了第一个维度，其他维度必须相同，若为一维数组则必须长度相同
- `np.hstack(tup, *, dtype=None, casting='same_kind')` 沿第二个维度连接多个数组，返回副本，一维数组会直接拼接
  - `tup` 除了第二个维度，其他维度必须相同
<br>

- `np.split(ary, indices_or_sections, axis=0)` 沿指定维度切割数组，返回视图
  - `indices_or_sections` 整数或一维数组
    - 若为整数 N，则会平分为 N 份，无法平分则报错
    - 若为一维数组，例如 (M, N, P)，则会取索引 [0: M], [M: N], [N: P], [P, len(ary.shape[axis])]，若不存在则会返回空数组
- `np.vsplit(ary, indices_or_sections)` 沿第一个维度切割数组，返回视图
- `np.hsplit(ary, indices_or_sections)` 沿第二个维度切割数组，返回视图，一维数组会沿第一个维度切割


<br>

### 改变形状
- `np.reshape(a, newshape, order='C')` 改变数组形状，返回视图，仅在必要时返回副本
  - `newshape` 若为整数，则会转换为一维数组；若为数组，其中一个维度可以使用 -1，其具体值由其他值推断出
- `a.reshape(shape, order='C')` 改变数组形状，返回视图，仅在必要时返回副本
  - `shape` 若为数组，其元素可直接分开传入
<br>

- `a.flatten(order='C')` 展平数组，返回副本
- `a/np.ravel(a, order='C')` 展平数组，返回视图，仅在必要时返回副本
<br>

- `a/np.squeeze(axis=None)` 除去数组中长度为一的维度
  - `axis` None 或整数或整数元组，若指定的维度长度不为一则报错
<br>

- `np.expand_dims(a, axis)` 扩展维度，返回视图
  - `axis` 整数或整数元组，指定的索引会插入新的维度
- 此外，还可以使用 np.newaxis (None) 来扩展维度：
```py
>>> a = np.arange(6).reshape(2, 3)
>>> a[np.newaxis, :, np.newaxis].shape
(1, 2, 1, 3)
>>> a[np.newaxis, :, :, np.newaxis].shape
(1, 2, 3, 1)
```


<br>

### 转置翻转
- `np.transpose(a, axes=None)` 转置数组，返回视图
  - `axes` 必须为 [0,1,...,N-1] 的一个排列，默认为 a.shape[::-1]
- `np.flip(m, axis=None)` 沿指定轴翻转数组，返回视图
  - `axis` 若为 None，则沿所有轴翻转；若为整数或整数元组，则沿指定轴翻转


<br>

### 数值计算
- `a/np.all(axis=None, out=None, keepdims=False, *, where=True)` 若所有元素的计算结果均为 True，则返回 True
- `a/np.any(axis=None, out=None, keepdims=False, *, where=True)` 若任意元素的计算结果为 True，则返回 True
  - `axis` None 或整数或整数元组
    - 若为 None，则会沿所有维度移动做逻辑运算，返回一个布尔值
    - 若指定维度，则会保持其他维度不变，沿指定维度移动做逻辑运算，运算结果保存在其他维度指定的位置，返回一个维度数减少的数组
  - `keepdims` 若为 True，则被消去的维度会保留，其长度变为一
  - `where` 布尔数组，只有为 True 的元素参与逻辑运算
<br>

- `a/np.max(axis=None, out=None, keepdims=False, initial=<no value>, where=True)` 返回沿指定轴的最大值
- `a/np.min(axis=None, out=None, keepdims=False, initial=<no value>, where=True)` 返回沿指定轴的最小值
  - `axis` None 或整数或整数元组
  - `initial` 输出值的最小/大值
<br>

- `a/np.sum(axis=None, dtype=None, out=None, keepdims=False, initial=0, where=True)` 返回沿指定轴的累加值
- `a/np.prod(axis=None, dtype=None, out=None, keepdims=False, initial=1, where=True)` 返回沿指定轴的累乘值
  - `dtype` 默认使用原数组的数据类型，除非原数组的数据类型是整数类型，且精度不足平台默认整型精度，此时会使用平台默认整型
  - `initial` 计算累加/乘值的起始值
- `a/np.mean(axis=None, dtype=None, out=None, keepdims=False, *, where=True)` 返回沿指定轴的平均值
  - `dtype` 默认情况下，整数数组的输出类型为 float64，浮点数数组的输出类型保持不变
<br>

- `a/np.cumsum(axis=None, dtype=None, out=None)` 返回沿指定轴的累积和
- `a/np.cumprod(axis=None, dtype=None, out=None)` 返回沿指定轴的累积乘积
  - `axis` None 或整数
    - 若为 None，则会先展平数组，返回一个一维数组
    - 若指定维度，则会保持其他维度不变，沿指定维度移动做累加/累积，运算结果保存在原来位置，返回一个形状不变的数组
<br>

- `a/np.dot(b, out=None)` 返回 a 与 b 的点积，与 `@` 相似
  - 若 a 与 b 均为一维数组，则作内积
  - 若 a 与 b 均为二维数组，则作矩阵乘法
  - 若 a 或 b 为标量，则作简单相乘
  - 若 a 为 N 维数组，b 为一维数组，则沿最后一个维度作点积，返回的数组的维度数减一
  - 若 a 为 N 维数组，b 为 M(M>=2) 维数组，则沿 a 的最后一个维度和 b 的倒数第二个维度作点积，返回的数组的维度数减二，如 ` dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])`


<br>

### 其他方法
- `np.copy(a, order='K', subok=False)` 拷贝数组
- `np.copyto(dst, src, casting='same_kind', where=True)` 拷贝 src 到 dst，可用于选择性复制
- `a.copy(order='C')` 返回数组的副本，更为推荐使用
- `a.view([dtype][, type])` 返回数组的视图
<br>

- `a.tobytes(order='C')` 将数组转换为字节序列，返回副本
- `a.tolist()` 将数组转换为列表，返回副本，若数组零维则返回一个标量
<br>

- `a.fill(value)` 用一个标量填充数组










<br>

## Random
### 生成随机数
- `np.random.rand(d0, d1, ..., dn)` 生成均匀分布的随机数数组，取值范围为 [0, 1)，若无参数则返回单个浮点数
- `np.random.random(size=None)` 生成取值范围为 [0, 1) 的随机数
- `np.random.random_sample(size=None)` 生成取值范围为 [0, 1) 的随机数
- `np.random.uniform(low=0.0, high=1.0, size=None)` 生成均匀分布的随机数
  - `size` 若为 None，则返回一个数；若为整数或元组，则返回一个数组
<br>

- `np.random.randn(d0, d1, ..., dn)` 生成标准正态分布的随机数数组，若无参数则返回单个浮点数
- `np.normal(loc=0.0, scale=1.0, size=None)` 生成标准分布的随机数
<br>

- `np.randint(low, high=None, size=None, dtype=int)` 返回指定范围内的随机整数
  - `high` 若为 None，则取值范围为 [0, low)，否则为 [low, high)

<br>

### 随机选择
- `np.random.choice(a, size=None, replace=True, p=None)` 随机选择一维数组的元素
  - `a` 若为一维数组，则从中选择元素；若为整数，则视为使用 `np.arange(a)`
  - `size` 若为 None，则只返回一个元素，否则返回指定形状的数组
  - `replace` 若为 True，则同一元素可被多次选择
  - `p` 一维数组，表示每个元素的概率，必须和为 1

<br>

### 随机排序
- `np.random.shuffle(x)` 沿第一个轴打乱序列顺序，原序列变化，返回 None
- `np.random.permutation(x)` 沿第一个轴随机排列序列，原序列不变，返回副本
  - `x` 若为数组，则会进行拷贝；若为整数，则视为使用 `np.arange(a)`








<br>

## Broadcasting
- 当对两个数组进行逐元素操作时，如 `a * b`，会从右到左比较它们的形状
- 若两个维度长度相同，或其中一个为 1，则称这两个维度兼容
- 若两个数组的维度数不同，则会在左边补全维度，长度全为 1
- 长度为 1 的维度会被拉伸复制，以匹配另一个数组对应位置的维度


