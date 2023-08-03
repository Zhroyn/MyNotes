- [对齐方式](#对齐方式)



### 对齐方式
```C
/* 对齐方式 */
justify-content: center;     /* 居中排列 */
justify-content: start;      /* 从行首开始排列 */
justify-content: end;        /* 从行尾开始排列 */
justify-content: flex-start; /* 从行首起始位置开始排列 */
justify-content: flex-end;   /* 从行尾位置开始排列 */
justify-content: left;       /* 一个挨一个在对齐容器得左边缘 */
justify-content: right;      /* 元素以容器右边缘为基准，一个挨着一个对齐, */

/* 基线对齐 */
justify-content: baseline;
justify-content: first baseline;
justify-content: last baseline;

/* 分配弹性元素方式 */
justify-content: space-between;  /* 均匀排列每个元素
                                   首个元素放置于起点，末尾元素放置于终点 */
justify-content: space-around;  /* 均匀排列每个元素
                                   每个元素周围分配相同的空间 */
justify-content: space-evenly;  /* 均匀排列每个元素
                                   每个元素之间的间隔相等 */
justify-content: stretch;       /* 均匀排列每个元素
                                   'auto'-sized 的元素会被拉伸以适应容器的大小 */

/* 溢出对齐方式 */
justify-content: safe center;
justify-content: unsafe center;

/* 全局值 */
justify-content: inherit;
justify-content: initial;
justify-content: unset;
```
