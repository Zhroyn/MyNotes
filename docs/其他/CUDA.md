# CUDA 笔记
## 基础概念

CUDA（Compute Unified Device Architecture）是 NVIDIA 推出的并行计算平台和编程模型，它允许开发者使用GPU进行通用计算。

在 CUDA 中，CPU 及其内存被称为**主机**（host），而 GPU 及其内存被称为**设备**(device)。CPU 和 GPU 之间的数据传输需要通过 CUDA API 来完成。

<div style="margin-top: 60pt"></div>

## 内核函数

在 GPU 上运行的函数称为**内核函数**（kernel function），它由 CPU 调用，在 GPU 上并行执行。

内核函数需要使用 `__global__` 关键字来声明，它的调用方式与普通函数不同，需要使用 `<<<...>>>` 来指定**执行配置**。

执行配置由四个部分组成：线程块的数量、线程块的大小、共享内存的大小和 CUDA 流。一般只会使用前两个参数。

一个基础的使用示例如下：

```cpp
__global__ void GPUFunction() {
    printf("This function is defined to run on the GPU.\n");
}

int main() {
    GPUFunction<<<1, 1>>>();
    cudaDeviceSynchronize(); // 等待 GPU 完成所有任务
}
```

<div style="margin-top: 60pt"></div>

## 线程索引

在内核中，可以使用以下内置变量确定线程位置：

- `threadIdx.x`, `threadIdx.y`, `threadIdx.z`: 线程在块中的索引
- `blockIdx.x`, `blockIdx.y`, `blockIdx.z`: 块在网格中的索引
- `blockDim.x`, `blockDim.y`, `blockDim.z`: 块的大小，即包含多少线程
- `gridDim.x`, `gridDim.y`, `gridDim.z`: 网格的大小，即包含多少块

可以将网格和线程块定义为最多具有 3 个维度。使用多个维度定义网格和线程块不会对性能造成任何影响，但这在处理具有多个维度的数据时可能非常有用，例如 2D 矩阵。如要定义二维或三维网格或线程块，可以使用 CUDA 的 `dim3` 类型，即如下所示：

```cpp
dim3 threads_per_block(16, 16, 1);
dim3 number_of_blocks(16, 16, 1);
someKernel<<<number_of_blocks, threads_per_block>>>();
```

在以上示例中，`someKernel` 内部的变量 `gridDim.x`、`gridDim.y`、`blockDim.x` 和 `blockDim.y` 均将等于 `16`。

<div style="margin-top: 60pt"></div>

## 最佳配置

鉴于 GPU 的硬件特性，所含线程的数量为 32 的倍数的线程块是最理想的选择，此时往往会出现执行配置所创建的线程数超过工作所需线程数的情况。这个问题可以通过以下方式轻松地解决：

- 编写执行配置，使其创建的线程数**超过**执行分配工作所需的线程数。
- 将一个值作为参数传递到核函数 (`N`) 中，该值表示要处理的数据集总大小或完成工作所需的总线程数。
- 计算网格内的线程索引后（使用 `threadIdx + blockIdx * blockDim`），请检查该索引是否超过 `N`，并且只在不超过的情况下执行与核函数相关的工作。

在实际情况中，还经常出现数据集远大于线程数的情况，此时可以通过跨网格循环来解决这个问题：

```cpp
__global void kernel(int *a, int N) {
    int indexWithinTheGrid = threadIdx.x + blockIdx.x * blockDim.x;
    int gridStride = gridDim.x * blockDim.x;

    for (int i = indexWithinTheGrid; i < N; i += gridStride) {
        // do work on a[i];
    }
}
```

<div style="margin-top: 60pt"></div>

## 内存管理

如要分配和释放内存，并获取可在主机和设备代码中引用的指针，请使用 `cudaMallocManaged` 和 `cudaFree` 来代替 `malloc` 和 `free`，如下例所示：

```cpp
int N = 2<<20;
size_t size = N * sizeof(int);

int *a;
cudaMallocManaged(&a, size);
cudaFree(a);
```

<div style="margin-top: 60pt"></div>

## 错误处理

有许多 CUDA 函数会返回类型为 `cudaError_t` 的值，该值可用于检查调用函数时是否发生错误。以下是对调用 `cudaMallocManaged` 函数进行错误处理的示例：

```cpp
cudaError_t err;
err = cudaMallocManaged(&a, N)

if (err != cudaSuccess) {
    printf("Error: %s\n", cudaGetErrorString(err));
}
```

启动定义为返回 `void` 的核函数后，将不会返回类型为 `cudaError_t` 的值。为检查启动核函数时是否发生错误（例如，如果启动配置错误），CUDA 提供 `cudaGetLastError` 函数，该函数会返回类型为 `cudaError_t` 的值。以下是对启动核函数进行错误处理的示例：

```cpp
someKernel<<<1, -1>>>();

cudaError_t err;
err = cudaGetLastError();
if (err != cudaSuccess) {
    printf("Error: %s\n", cudaGetErrorString(err));
}
```

最后，为捕捉异步错误（例如，在异步核函数执行期间），请务必检查后续同步 CUDA 运行时 API 调用所返回的状态（例如 `cudaDeviceSynchronize`）；如果之前启动的其中一个核函数失败，则将返回错误。

<div style="margin-top: 60pt"></div>

## 查询设备信息

- `cudaGetDeviceCount(&count)` 获取设备数量
- `cudaGetDevice(&deviceId)` 获取当前设备 ID
- `cudaGetDeviceProperties(&props, deviceId)` 获取设备属性，其中 `props` 是 `cudaDeviceProp` 类型的变量

设备属性包括：

- `name` 设备名称
- `totalGlobalMem` 全局内存大小
- `multiProcessorCount` 处理器数量




<div style="margin-top: 60pt"></div>

## 内存优化
### 异步内存预取

CUDA 可通过 `cudaMemPrefetchAsync` 函数，轻松将托管内存异步预取到 GPU 设备或 CPU，从而减少数据传输时间：

- `cudaMemPrefetchAsync(ptr, size, deviceId)` 将内存预取到 GPU 设备
- `cudaMemPrefetchAsync(ptr, size, cudaCpuDeviceId)` 将内存预取到 CPU，`cudaCpuDeviceId` 是 CUDA 内建常量。

### 分块与共享内存

在进行矩阵乘法时，如果每个元素都单独处理，则会导致许多数据被重复加载。此时，我们可以先将矩阵划分为小块，然后将小块加载到共享内存中，来加速计算：

```cpp
__shared__ float A_s[TILE_DIM][TILE_DIM];
__shared__ float B_s[TILE_DIM][TILE_DIM];

unsigned int row = blockIdx.y*blockDim.y + threadIdx.y;
unsigned int col = blockIdx.x*blockDim.x + threadIdx.x;

float sum = 0.0f;

for(unsigned int tile = 0; tile < N/TILE_DIM; ++tile) {

    // Load tile to shared memory
    A_s[threadIdx.y][threadIdx.x] = A[row*N + tile*TILE_DIM + threadIdx.x];
    B_s[threadIdx.y][threadIdx.x] = B[(tile*TILE_DIM + threadIdx.y)*N + col];
    __syncthreads();

    // Compute with tile
    for(unsigned int i = 0; i < TILE_DIM; ++i) {
        sum += A_s[threadIdx.y][i]*B_s[i][threadIdx.x];
    }
    __syncthreads();

}

C[row*N + col] = sum;
```