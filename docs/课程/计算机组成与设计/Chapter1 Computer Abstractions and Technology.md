
# Computer Abstractions and Technology

## 重要思想

- Design for Moore’s Law
- Use Abstraction to Simplify Design
- Make the Common Case Fast
- Performance via Parallelism
- Performance via Pipelining
- Performance via Prediction
- Hierarchy of Memory
- Dependability via Redundancy




## 性能评价

评价性能有两种方式：

- **Response time (响应时间)**: 单个任务所花时间
- **Throughput (吞吐量)**: 单位时间的工作量

我们这里只讨论响应时间，定义性能表现为：

$$\text{Performance} = \dfrac{1}{\text{Execution Time}}$$

其中执行时间也分为 Elapsed Time 和 CPU Time，前者考虑了包括 I/O、操作系统开销、中断等在内的所有时间，后者只考虑了处理单个任务的时间。

### CPU 时钟

Clock period 是一个时钟周期的时间，Clock frequency (rate) 是每秒的时钟周期数。CPU Time 可以用以下公式表示：

$$
\begin{align*} 
\text{CPU Time} &= \text{CPU Clock Cycles} \times \text{Clock Cycle Time} \\
&=\dfrac{\text{CPU Clock Cycles}}{\text{Clock Rates}}
\end{align*}
$$ 

因此提高性能可以通过减少时钟周期数，或者提高时钟频率来实现。

现在我们定义时钟周期数为：

$$\text{Clock Cycles} = \text{Instruction Count} \times \text{Cycles per Instruction(CPI)}$$

那么就有：

$$
\begin{align*}
\text{CPU Time }& = \text{Instruction Count} \times \text{CPI} \times \text{CPI Cycle Time} \\
& = \dfrac{\text{Instruction Count} \times \text{CPI}}{\text{Clock Rate}}
\end{align*}
$$

精简指令集 (RISC) 有较低的 CPI，但是需要更多的指令，而复杂指令集 (CISC) 需要的指令较少，但是 CPI 较高。不同指令的 CPI 可能不同，需要考虑平均情况，因此任何因素都可能影响最终的 CPI。

综上, $\text{CPU Time} = \dfrac{\text{Instructions}}{\text{Program}}\times \dfrac{\text{Clock Cycles}}{\text{Instructions}}\times \dfrac{\text{Seconds}}{\text{Clock Cycles}}$ 

另一种评价指标是 MIPS (Million Instructions Per Second)，但是这个指标不够准确，因为不同的指令可能需要不同的时间，而且不同的 ISA (Instruction Set Architecture) 之间也不能直接比较。




## 性能制约

现在单核处理器 (Uniprocessor) 性能发展缓慢，主要受到以下三种限制。

### 功耗墙

功耗墙 (Power Wall) 指的是，由于功耗的增加，使得 CPU 的主频提高受到限制。功耗的公式为：

$$\text{Power} = \text{Capactive load} \times \text{Voltage}^2 \times \text{Frequency}$$

面临的困难有：

- 功耗效率下降，频率每翻一倍功耗也要翻倍
- 热量聚集，散热困难
- 功耗泄露

虽然现在主频提高了很多，但功耗并没有得到这么多的提升，这是因为我们降低了工作电压（5V->1V），但工作电压无法再降低，否则泄漏电流占比太大，也难以提高散热效率，因此难以再提高主频了。

### 内存墙

内存墙 (Memory Wall) 指的是，内存的性能增长不如 CPU 的性能增长，大部分时间花在读写内存了，影响整体性能。

解决方法：增大二级缓存，从而减少内存访问次数。

### 指令级并行墙

指令级并行 (Instruction Level Parallelism) 墙指的是，很难使单个进程的指令流有足够的并行性，来保持单核的高占用率。

由于功耗浪费和内存慢速，ILP 的利用率很低，因此现在主要转向 DLP (Data Level Parallelism) 和 TLP (Thread Level Parallelism)。不过与 ILP 相比，DLP 和 TLP 都需要显式的并行编程，更加麻烦。




## 杂项

Amdahl's Law: 提升计算机的某一方面，只能提升整体性能的一部分。因此，需要使最常见的情况更快。

Low Power at Idle: 当 CPU 占用率低时，功率仍然较高。然而现实中，大部分时间 CPU 都是空闲的，因此需要通过设计尽量让功耗与占用率保持线性关系。