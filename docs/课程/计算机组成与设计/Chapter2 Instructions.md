
# 指令：计算机的语言

这里主要讲的是 RISC-V 指令集，若要了解 x86 指令集，可以参考[另一篇笔记](https://zhroyn.github.io/MyNotes/%E5%85%B6%E4%BB%96/8086Note.html)。


## 指令集设计原则

1. Simplicity favors regularity，简单源自规整
    - 指令包含3个操作数
    - 基本 RISC-V ISA 是定长的 32-bit 的指令
2. Smaller is faster，越少越快
    - 寄存器个数一般不超过 32 个
3. Make the common case fast，让常见的情况快
    - 小常数是常见的，针对立即数的操作避免了额外的加载操作
    - 经常有 0 参与计算，因此专门将零存在 `x0` 中
4. Good design demands good compromises，好的设计需要好的折中
    - 例如，为了扩大立即数的范围，牺牲了操作码的位数


## 操作数

指令集中的操作数分为三种：

- 寄存器
- 内存
- 立即数

RISC-V 有 32 个 64 位的通用寄存器，分别用 `x0` 到 `x31` 表示，使用规范为：

- `x0` 一直为 0
- `x1` 返回地址寄存器 (Return address, ra)
- `x2` 栈指针 (Stack pointer, sp)
- `x3` 全局指针 (Global pointer, gp)
- `x4` 线程指针 (Thread pointer, tp)
- `x5-x7` 临时寄存器 (Temporaries)
- `x8-x9` 保留寄存器 (Saved)
- `x10-x17` 参数/结果寄存器 (Arguments/results)
- `x18-x27` 保留寄存器 (Saved)
- `x28-x31` 临时寄存器 (Temporaries)

其中 ra, sp, gp, tp 也是保留寄存器，保留寄存器需要在被调用时将原来的值保存到栈中，并在之后恢复，而临时寄存器可以不管原来的值，直接修改。

内存是字节寻址的，内存地址在指令中的格式为 `offset(base)`，其中 `offset` 为立即数，`base` 为基址寄存器。例如，对于一个双字数组 `A`，`A[8]` 可以表示为 `64(x22)`，其中 `x22` 存储了数组 `A` 的基址。

RISC-V 是小端 (Little endian) 存储的，即数据的低位放在低地址，高位放在高地址，存取数据都是从低往高处理。而且 RISC-V 不要求字对齐，即一个字的起始地址不一定是 4 的倍数。



## 指令

RV32I 基础指令集中的指令有以下几种格式：

![](../../assets/co_instruction_format.png)

各符号的含义为：

- `opcode` 操作码，指明指令的类型
- `rd` 目标寄存器
- `funct3` 附加操作码
- `rs1` 第一个源寄存器
- `rs2` 第二个源寄存器
- `funct7` 附加操作码
- `imm` 立即数

### 算术指令

- `add rd, rs1, rs2` 加法，`rd = rs1 + rs2`
- `sub rd, rs1, rs2` 减法，`rd = rs1 - rs2`
- `xor rd, rs1, rs2` 异或，`rd = rs1 ^ rs2`
- `or rd, rs1, rs2` 或，`rd = rs1 | rs2`
- `and rd, rs1, rs2` 与，`rd = rs1 & rs2`
- `sll rd, rs1, rs2` 逻辑左移 (Shift Left Logical)，`rd = rs1 << rs2`
- `srl rd, rs1, rs2` 逻辑右移 (Shift Right Logical)，`rd = rs1 >> rs2`
- `sra rd, rs1, rs2` 算术右移 (Shift Right Arithmetic)，会进行符号扩展
- `slt rd, rs1, rs2` 设置小于 (Set Less Than)，`rd = (rs1 < rs2) ? 1 : 0`
- `sltu rd, rs1, rs2` 无符号设置小于 (Set Less Than Unsigned)

上述指令都是 R 型指令，即操作数都在寄存器中。除了减法以外，都可以在后面加上一个 `i` 变成 I 型指令，如 `addi rd, rs1, imm`，并且移位指令只会取立即数的低五位，最多只能移动 31 位。

取反可以通过与全为 1 的立即数异或实现。

### 内存操作指令

从内存中加载数据到寄存器 `rd` 中的操作为 I 型指令：

- `lb rd, offset(rs1)` 加载字节
- `lh rd, offset(rs1)` 加载半字
- `lw rd, offset(rs1)` 加载字
- `lbu rd, offset(rs1)` 加载无符号字节
- `lhu rd, offset(rs1)` 加载无符号半字

将寄存器 `rs2` 中的数据存储到内存中的操作为 S 型指令：

- `sb rs2, offset(rs1)` 存储字节
- `sh rs2, offset(rs1)` 存储半字
- `sw rs2, offset(rs1)` 存储字

