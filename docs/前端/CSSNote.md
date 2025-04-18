# CSS 笔记
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





<div style="margin-top: 80pt"></div>

## 布局

CSS 的布局方式主要分为以下几类：

- 常规流（normal flow）或者说流式布局是浏览器默认的 HTML 布局方式，会根据 HTML 元素在文档中的先后顺序，自上而下，从左到右进行布局，其中每个元素要么是块级元素，要么是行内元素。可以通过修改元素的 `display` 属性来改变流式布局
- 弹性盒布局（flexbox）是指通过 `display: flex` 属性，将一个元素的子元素设置为弹性盒子，用于创建横向或是纵向的一维页面布局
- 网格布局（grid）是指通过 `display: grid` 属性，将一个元素的子元素设置为网格，用于同时在两个维度上把元素按行和列排列整齐
- 浮动布局（float）是指通过 `float` 属性，将元素从常规流中移除，然后浮动到左侧或者右侧，这时候其他的周围内容就会在这个被设置浮动的元素周围环绕
- 定位布局（positioning）是指通过 `position` 属性，将一个元素从它原本在常规流中应该在的位置移动到另一个位置

### 显示类型

`display` 属性用于设置元素的内部和外部的显示类型。外部类型设置元素如何参与流式布局，内部类型则设置子元素的布局。

外部显示类型主要有：

- `block` 生成一个块级盒子，在页面上占据一行，并且会尽可能地占据可用的宽度。常见的块级元素有 `div`、`p`、`h1` 等
- `inline` 生成一个或多个行级盒子，它们之前或者之后并不会产生换行。在正常的流中，如果有空间，下一个元素将会在同一行上。常见的行内元素有 `span`、`a`、`img` 等

内部显示类型主要有：

- `flow` 默认值，子元素按照常规文档流（块级或行内）排列
- `flow-root` 创建一个无副作用的块级格式化上下文（BFC），可以用于包含内部浮动、排除外部浮动或者防止外边距重叠
- `flex` 行为类似块级元素，并且根据弹性盒模型布局内容
- `grid` 行为类似块级元素，并且根据网格模型布局内容

当 `display` 属性仅有一个外部值时，内部值会被设置为 `flow`；当 `display` 属性仅有一个内部值时，外部值会被设置为 `block`。

`display` 属性可以使用多关键字语法同时定义外部和内部显示类型，例如用 `inline flex` 表示一个行级的弹性容器，此外也可以出于兼容性考虑，使用传统的单关键字预组合：

- `inline-block` 行为类似于行级元素，但会生成块级盒子，可以设置宽高，等同于 `inline flow-root`
- `inline-flex` 行为类似于行级元素，并且根据弹性盒模型布局内容，等同于 `inline flex`
- `inline-grid` 行为类似于行级元素，并且根据网格模型布局内容，等同于 `inline grid`

<div style="margin-top: 40pt"></div>

### 弹性盒布局

flexbox 是一种一维的布局，它有一个主轴和一个交叉轴，主轴的方向由 `flex-direction` 属性决定，交叉轴的方向垂直于主轴。

当一个容器的 `display` 属性被设置为 `flex` 时，它的所有直接子元素都会变为 flex 元素。flex 元素会有以下默认行为：

- 元素排列为一行（`flex-direction` 属性的初始值是 `row`）
- 元素从主轴的起始线开始
- 元素不会在主维度方向拉伸，但是可以缩小
- 元素被拉伸来填充交叉轴大小
- `flex-basis` 属性为 `auto`
- `flex-wrap` 属性为 `nowrap`

#### 在主轴上的流动

`flex-direction` 属性可以设置为以下值：

- `row` 主轴为水平方向，起点在左侧
- `row-reverse` 主轴为水平方向，起点在右侧
- `column` 主轴为垂直方向，起点在上侧
- `column-reverse` 主轴为垂直方向，起点在下侧

`flex-wrap` 属性可以设置为以下值：

- `nowrap` 不换行，所有元素在同一行内显示
- `wrap` 换行，第一行在上方
- `wrap-reverse` 换行，第一行在下方

`flex-direction` 和 `flex-wrap` 这两个属性可以组合为 `flex-flow` 属性，其中第一个指定的值为 `flex-direction`，第二个指定的值为 `flex-wrap`，例如 `flex-flow: row wrap` 表示从左到右排列并且换行。

#### 在主轴上的比例

`flex-basis` 属性定义了元素在主轴上的所占空间，默认值为 `auto`。此时，浏览器会检测这个元素是否具有确定的尺寸。如果没有给元素设定尺寸，`flex-basis` 的值就会采用元素内容的尺寸，这意味着浏览器会自动分配大小以充分展示元素的内容。

`flex-grow` 属性用于控制 flex 元素沿着主轴的延展行为。若它被赋值为一个正整数，flex 元素就会以 `flex-basis` 为基础，沿主轴方向增长尺寸。如果有其他元素也被允许延展，那么则会各自按照比例分配可用空间。

`flex-shrink` 属性用于控制 flex 元素沿着主轴的收缩行为。若它被赋值为一个正整数，当弹性容器中没有足够排列 flex 元素的空间时，flex 元素就可以收缩到 `flex-basis` 以下。给 `flex-shrink` 属性赋予更大的数值可以比赋予小数值的同级元素收缩程度更大。

`flex` 属性是 `flex-grow`、`flex-shrink` 和 `flex-basis` 的简写，其中第一个值为 `flex-grow`，第二个值为 `flex-shrink`，第三个值为 `flex-basis`。下面是几种预定义的值：

- `initial` 等价于 `0 1 auto`，不能拉伸但是可以收缩
- `auto` 等价于 `1 1 auto`，既能拉伸又能收缩
- `none` 等价于 `0 0 auto`，既不能拉伸也不能收缩
- `<positive-number>` 等价于 `<positive-number> 1 0`，可以拉伸，也可以收缩到 0

#### 排序

弹性盒布局可以通过 `order` 属性做到改变 flex 元素的布局位置，而不会影响到源顺序（即 dom 树里元素的顺序）。

具体细节为：

- 所有 flex 元素默认的 `order` 值是 0
- `order` 值大的 flex 元素比 `order` 值小的在显示顺序中更靠后
- 相同 `order` 值的 flex 项按源顺序显示
- `order` 值可以是负数

#### 对齐方式

`justify-content` 属性用于设置子元素在主轴上的的排列方式，可以被设置为以下值：

- `flex-start` 默认，元素向主轴起点对齐（左侧对齐）
- `flex-end` 元素向主轴终点对齐（右侧对齐）
- `center` 元素在主轴居中对齐
- `space-between` 元素均匀分布，首尾贴边，中间间距相等
- `space-around` 元素均匀分布，周围间距相等（首尾间距是中间间距的一半）
- `space-evenly` 元素均匀分布，所有间距（包括首尾）完全相等

`align-items` 属性用于设置子元素在交叉轴上的对齐方式，可以被设置为以下值：

- `stretch` 默认，元素被拉伸以适应容器
- `flex-start` 元素向交叉轴起点对齐（顶部对齐）
- `flex-end` 元素向交叉轴终点对齐（底部对齐）
- `center` 元素在交叉轴居中对齐
- `baseline` 元素按文本基线对齐

`align-self` 属性用于设置单个 flex 元素在交叉轴上的对齐方式，可以被设置为以下值：

- `auto` 默认，继承父元素的 `align-items` 属性
- `stretch` 元素被拉伸以适应容器
- `flex-start` 元素向交叉轴起点对齐（顶部对齐）
- `flex-end` 元素向交叉轴终点对齐（底部对齐）
- `center` 元素在交叉轴居中对齐
- `baseline` 元素按文本基线对齐

`align-content` 属性用于设置多行 flex 容器中行在交叉轴上的对齐方式（仅当 `flex-wrap: wrap` 时生效），可以被设置为以下值：

- `stretch` 默认，行被拉伸以适应容器
- `flex-start` 所有行向交叉轴起点对齐（顶部对齐）
- `flex-end` 所有行向交叉轴终点对齐（底部对齐）
- `center` 所有行在交叉轴居中对齐
- `space-between` 所有行均匀分布，首尾贴边，中间间距相等
- `space-around` 所有行均匀分布，周围间距相等（首尾间距是中间间距的一半）
- `space-evenly` 所有行均匀分布，所有间距（包括首尾）完全相等

<div style="margin-top: 40pt"></div>

### 网格布局

我们通过在元素上声明 `display：grid` 或 `display：inline-grid` 来创建一个网格容器。一旦我们这样做，这个元素的所有直系子元素都将成为网格项目。创建的网格容器默认是单列网格。

#### 网格轨道

网格轨道是网格上任意两条相邻线之间的空间。我们可以通过 `grid-template-columns` 和 `grid-template-rows` 属性来定义网格轨道的大小和数量，这样的网格被称为显式网格。

轨道可以使用任何长度单位进行定义，网格还引入另外一个长度单位 `fr`，它代表网格轨道的剩余空间，例如 `grid-template-columns: 1fr 1fr 1fr` 可以创建三个等宽的列。

在网格中，还可以使用 `repeat()` 函数来重复部分或整个轨道列表，例如 `grid-template-columns: repeat(3, 1fr)` 同样可以创建三个等宽的列。

`repeat()` 函数还可以与 `auto-fill` 关键字结合使用来自动填充列，例如 `grid-template-columns: repeat(auto-fill, minmax(200px, 1fr))` 会创建尽可能多的 200px 宽度的列，然后将剩余空间均分给每一列宽。

如果在定义的网格外放置内容，或者由于内容太多，需要更多的网格轨道，那么网格就会在隐式网格中创建行和列，此时可以通过 `grid-auto-rows` 和 `grid-auto-columns` 属性来为在隐式网格中创建的轨道设置大小。在这里，我们可以使用 `minmax()` 函数来指定最小尺寸，例如 `grid-auto-rows: minmax(100px, auto)`。

#### 网格线

网格布局会为我们创建带有编号的网格线来让我们来定位每一个网格元素。如果网格有三列，那么纵向的网格线的编号就是 1、2、3、4。

可以使用 `grid-column-start`、`grid-column-end`、`grid-row-start` 和 `grid-row-end` 属性来放置网格元素，例如：

```css
.box1 {
  grid-column-start: 1;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 3;
}
```

上面的样式会将 `.box1` 元素放置到前三列、前两行中。

可以使用 `grid-column` 和 `grid-row` 简写属性，以 `/` 分隔符将 `grid-column-start` 和 `grid-column-end` 以及 `grid-row-start` 和 `grid-row-end` 连接起来，例如 `.box1` 的样式可以简写为：

```css
.box1 {
  grid-column: 1 / 4;
  grid-row: 1 / 3;
}
```

如果网格项只跨越了一个轨道，可以省略终止值。

#### 网格区域

网格布局还可以使用 `grid-template-areas` 属性来为网格区域指定一个名称，然后使用 `grid-area` 属性来将网格元素放置到指定的区域中。网格区域必须是矩形的（例如不能创建 L 形区域）。

示例如下：

```css
.container {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar content"
    "footer footer";
  grid-template-columns: 1fr 3fr;
  gap: 20px;
}

header {
  grid-area: header;
}

article {
  grid-area: content;
}

aside {
  grid-area: sidebar;
}

footer {
  grid-area: footer;
}
```

#### 网格间距

网格单元格之间的横向间距（gutter）或纵向间距（alley）可以使用 `column-gap` 和 `row-gap` 属性。

`column-gap` 和 `row-gap` 也可以简写为 `gap` 属性。`gap` 属性可以接受一个或两个值，第一个值为 `row-gap`，第二个值为 `column-gap`。

`column-gap`、`row-gap` 和 `gap` 都带有 `grid-` 前缀的变体，分别为 `grid-column-gap`、`grid-row-gap` 和 `grid-gap`。

#### 网格对齐

网格布局可以使用以下属性来控制网格元素在网格中的对齐方式：

- `justify-*` 控制水平对齐方式
    - `justify-content` 控制如何沿着网格容器的行向轴分配列的空间，有 `start`（默认）、`end`、`center`、`space-between`、`space-around`、`space-evenly` 等值
    - `justify-items` 为所有子元素定义了默认的 `justify-self`，使子元素以指定方式沿行向轴对齐，默认为 `stretch`，即拉伸以填充整个行向轴
    - `justify-self` 控制单个网格元素在网格中的行向对齐方式，有 `stretch`、`center`、`start`、`end` 等值
- `align-*` 控制垂直对齐方式
    - `align-content` 控制如何沿着网格容器的纵向轴分配行的空间，与 `justify-content` 类似
    - `align-items` 为所有子元素定义了默认的 `align-self`，与 `justify-items` 类似
    - `align-self` 控制单个网格元素在网格中的纵向对齐方式，与 `justify-self` 类似
- `place-*` 是 `justify-*` 和 `align-*` 的简写，可以接受一个或两个值，第一个值为 `align-*`，第二个值为 `justify-*`

<div style="margin-top: 40pt"></div>

### 浮动

`float` 属性指定一个元素沿其容器的左侧或右侧放置，允许文本和内联元素环绕它。一个元素浮动之后，它会被移出正常的文档流，然后向左或者向右平移，直到碰到了所处盒子的边界，或者碰到另外一个浮动的元素。

`float` 接受下列值：

- `left` 元素必须浮动在所在的块容器的左侧
- `right` 元素必须浮动在所在的块容器的右侧
- `none` 元素不浮动
- `inline-start` 元素必须浮动在所在的块容器的起始位置
- `inline-end` 元素必须浮动在所在的块容器的结束位置

我们可以在浮动元素上应用 margin，将文字推开，但不能在文字上应用 margin 将浮动元素推走，这是因为浮动的元素脱离了正常文档流。

`clear` 属性指定一个元素是否必须移动（清除浮动后）到在它之前的浮动元素下面。当应用于非浮动块时，它会将非浮动块的边框边界移动到所有相关浮动元素外边界的下方，这个非浮动块的顶部外边距会折叠。

`clear` 接受下列值：

- `none` 元素不会被向下移动以清除浮动
- `left` 元素被向下移动以清除左浮动
- `right` 元素被向下移动以清除右浮动
- `both` 元素被向下移动以清除左右浮动

一个包含浮动元素的盒子不能保证浮动元素完全在盒子内。为了解决这个问题，有一种方法叫做 **clearfix**，即 clear 一个不浮动的 `::after` 伪元素：

```css
#container::after {
  content: "";
  display: block;
  clear: both;
}
```

一个替代的方案是将包裹元素的 `overflow` 属性设置为除 `visible` 外的其他值。这会创建一个块格式化上下文（BFC），将浮动元素包含在 BFC 及其背景之内。大部分情况下这种小技巧都可以奏效，但是可能会出现莫名其妙的滚动条或裁剪阴影，这是使用 overflow 带来的一些副作用。

另一个较为现代的方案是使用 `display` 属性的 `flow-root` 值。它可以直接创建块格式化上下文（BFC），在使用上没有副作用。

<div style="margin-top: 40pt"></div>

### 定位

`position` 属性指定一个元素在文档中的定位方式。它接受下列值：

- `static` 元素默认值，元素使用正常的布局行为
- `relative` 元素先放置在未添加定位时的位置，再在不改变页面布局的前提下调整元素位置
- `absolute` 元素会被移出正常文档流，然后相对于其最近的非 static 定位祖先元素进行偏移。如果所有的父元素都没有显式地定义 position 属性，那么绝对定位元素会被包含在初始块容器中。这个初始块容器有着和浏览器视口一样的尺寸，并且 \<html\> 元素也被包含在这个容器里面
- `fixed` 元素会被移出正常文档流，然后相对于浏览器视口进行偏移。即使页面滚动，元素也不会移动
- `sticky` 根据正常文档流进行定位，然后相对于其最近的滚动祖先元素和包含块进行偏移。一个 sticky 元素会“固定”在离它最近的一个拥有“滚动机制”的祖先上，即便这个祖先不是最近的真实可滚动祖先。粘性定位元素会创建一个层叠上下文，由此可以实现滚动索引页面（当后面的标题滚动到视口顶部时会覆盖前一个标题）

偏移量通过以下属性来指定：

- `top` 元素的上边缘距离其包含块上边缘的距离
- `bottom` 元素的下边缘距离其包含块下边缘的距离
- `left` 元素的左边缘距离其包含块左边缘的距离
- `right` 元素的右边缘距离其包含块右边缘的距离

当定位元素重叠时，源顺序较后的元素会覆盖源顺序较前的元素，或者可以使用 `z-index` 属性来改变定位元素及其后代元素的 Z 轴顺序，`z-index` 较大的重叠元素会覆盖较小的元素。







<div style="margin-top: 80pt"></div>

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

