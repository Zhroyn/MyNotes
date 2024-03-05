
## 关联样式表
使用 link 元素可以引入外部样式表，会阻塞渲染，直至样式表解析完成：
```html
<link rel="stylesheet" href="style.css">
```

使用 style 元素可以嵌入内部样式表，会异步解析：
```html
<style> ... </style>
```

在 css 内部还可以使用 @import 语法导入外部样式表，以下两种写法是等价的：
```css
@import url("style.css");
@import "style.css";
```



<br>

## 媒体查询
- 媒体查询由媒体类型和媒体特性描述符组成，特性描述符必须放在圆括号内
- 多个媒体特性可用 and 连接起来，还可以在媒体查询的最前面加上 not 取反
- 多个媒体查询可用 `,` 分隔，只要有一个计算结果为 true 对应样式表就会应用
<br>

- `[min/max-]width/height: <length>`  显示区域的宽高
    - `min-width: 1080px` 显示区域宽度大于等于 1080px 时成立
- `[min/max-]device-width-height: <length>`  设备屏幕的宽高

- `[min/max-]aspect-ratio: <w/h>` 显示区域的宽高比
- `[min/max-]device-aspect-ratio: <w/h>` 设备屏幕的宽高比
- `orientation: portrait/landscape` 屏幕方向
    - `portrait` 竖屏，height 大于等于 width 
    - `landscape` 横屏，width 大于等于 height 
<br>

- `[min/max-]color: <integer>` 每个色彩分量的深度
    - `color` 设备有色彩深度时成立
    - `min-color: 8` 色彩深度大于等于 8 位时成立
- `[min/max-]color-index: <integer>` 色彩搜寻列表的颜色总数
    - `min-color-index: 256` 至少有 256 色的设备成立
<br>

- `[min/max-]resolution: <resolution>` 设备的分辨率
    - `dpi` 每英寸像素数
    - `dpcm` 每厘米像素数
    - `dppx` 每 px 像素数，`1dppx` 相当于 `96dpi`
    - `x` 相当于 `dppx`

