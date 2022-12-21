#### 命令形式
```C
#pragma omp 指令 子句,子句,子句...
```



#### 简单指令
```C
// 用每个线程处理紧跟着的一条语句
#pragma omp parallel

// 指定线程数处理紧跟着的一条语句
#pragma omp parallel num_threads(5)

// 或使用函数指定线程数
omp_set_num_thread(5)
#pragma omp parallel
```
```C
// 获取最大线程数
opm_get_max_threads()
```



#### for循环
```C
// 并行下一个for语句
#pragma omp for

// 静态调度，分配给每个线程的任务数都是iterate_num/threads_num
#pragma omp for schedule(static)
// 动态调度，先到先得
#pragma omp for schedule(dynamic)
```



#### sections制导命令
```C
// 把不同的区域交给不同的线程去执行
#pragma omp parallel sections
{
    #pragma omp section
    {
        statements
    }
    #pragma omp section
    {
        statements
    }
    #pragma omp section
    {
        statements
    }
}
```




#### single制导指令
single制导指令所包含的代码段只有一个线程执行，别的线程跳过该代码，如果没有nowait子句，那么其他线程将会在single制导指令结束的隐式同步点等待。有nowait子句其他线程将跳过等待往下执行。
```C
#pragma omp single [nowait]
{
    statements
}
```


