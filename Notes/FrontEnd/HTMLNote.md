[toc]




### HTML简介
###### 元素
- HTML文档由元素组成。每个元素以**开始标签**起始，以**结束标签**中止，在两者之间的称为元素的内容。
- 某些HTML元素具有空内容，可在开始标签中进行关闭，如`<br>`
- 在开始标签中添加斜杠，是关闭空元素的正确方法，如`<br />`
- 分为块级元素和内联元素

###### 属性
- 大多数HTML元素可具有属性，属性的描述一般位于开始标签
- 全局属性可用于不同标签，如：
  - `style="..."` 规定元素的行内样式（inline style），会覆盖intenal stylesheet和external stylesheet
  - `id="idname"` id名必须唯一且以字母开头，会检查大小写
  - `class="classname"`




### HTML head元素
`<title>`: 用于定义显示在标题栏，收藏夹，以及搜索引擎结果页面的标题

`<base>`: 规定页面上所有链接的默认URL和默认目标，如:
```html
<base href="url" target="_blank">
```

`<meta>`: 用于描述网页，如关键词、最后修改时间、作者等，并能指定网页编码如：
```html
<meta name="description" content="免费在线教程">
<meta name="keywords" content="HTML,CSS,XML,JavaScript">
<meta name="author" content="runoob">
<meta charset="UTF-8">
```

`<link>`: 用于定义文档与外部资源的关系
- media属性：规定被链接文档将显示在什么设备上，如：`screen`, `print`
- rel属性：定义当前文档与被链接文档之间的关系，如：`icon`, `stylesheet`
- type属性：规定被链接文档的MIME类型，如：`image/png`, `text/css`
- href属性：定义被链接文档的位置
- 同步加载

`<style>`: 用于定义HTML文档的样式文件
- media属性：为样式表规定不同的媒体类型，如：`screen`（默认）, `print`
- scoped属性：使样式仅应用到 style 元素的父元素及其子元素
- type属性：规定样式表的 MIME 类型，如：`text/css`
- 异步加载




### HTML排版
```html
<h1>...</h1>    <!--最大的标题-->
<h6>...</h6>    <!--最小的标题-->

<br> or <br />  <!--换行-->
<hr> or <hr />  <!--水平线-->

<p>...<br>...</p>   <!--段落中换行--->
```



### HTML文本格式化
```html
<b>指明要使用粗体样式</b>
<strong>表明要强调，通常使用粗体样式</strong>

<i>指明要使用斜体样式</i>
<em>表明要强调，通常使用斜体样式</em>

<ins>下划线，定义插入字</ins>
<del>删除线，定义删除字</del>

<sub>下标</sub>
<sup>上标</sup>
```

```html
<pre>定义预格式化文本，保留文本的换行和空格</pre>
<code>定义代码文本，将文本变成等宽字体，并表明该文本是源程序代码</code>
```




### HTML引用
`<q></q>` 用于短的引用，一般会自动加上双引号
`<blockquote></blockquote>` 用于长的引用，会另起一段
`<cite></cite>` 用于作品标题，，一般会显示为斜体

`<q>` and `<blockquote>` 具有`cite`属性，规定引用的源URL，如：
`<q cite="www.baidu.com">`



### HTML链接
```html
<a href="url">链接到网页</a>
<a href="#idname">链接到文档某个位置</a>
```
target属性：
- `_self`: 默认，当前页面跳转
- `_blank`: 新窗口打开
- `_parent`: 在父窗口中打开链接
- `_top`: 在当前窗体打开链接，并替换当前整个窗体




### HTML图像
```html
<img src="pulpit.jpg" alt="Pulpit rock" width="304" height="228">
```
scr属性：值为图像的URL
alt属性：为图像定义预备的可替换的文本，在浏览器无法载入图像时显示
width属性：设置图像的宽度，属性值默认单位为像素
height属性：设置图像的高度，属性值默认单位为像素




### HTML表格
```html
<table border="1">
	<caption>Table</caption>
  <tr>                      <!--table row-->
    <th>Header 1</th>       <!--table header cell-->
    <th colspan="2">Header 2</th>
  </tr>
  <tr>
    <td>row 1, cell 1</td>  <!--table data cell-->
    <td>row 1, cell 2</td>
  </tr>
  <tr>
    <td>row 2, cell 1</td>
    <td>row 2, cell 2</td>
  </tr>
</table>
```
`<table>`元素：定义表格
- border属性：规定表格是否拥有边框

`<th>`元素：文本通常呈现为粗体并且居中
- colspan属性：规定表头单元格可横跨的列数
- rowspan属性：规定表头单元格可横跨的行数

`<tr>`元素：定义表格的行
`<td>`元素：定义表格单元
`<caption>`元素：定义表格标题，标题置于表头并居中




### HTML列表
###### 无序列表
```html
<ul style="list-style-type:disc">     <!--默认，圆点-->
<ul style="list-style-type:circle">   <!--圆圈-->
<ul style="list-style-type:square">   <!--正方形-->

<ul>
  <li>Coffee</li>
  <li>Milk</li>
</ul>
```

###### 有序列表
```html
<ol type="1">   <!--默认，数字编号-->
<ol type="a">   <!--小写字母-->
<ol type="A">   <!--大写字母-->
<ol type="i">   <!--小写罗马数字-->
<ol type="I">   <!--大写罗马数字-->

<ol style="list-style-type:decimal">
<ol style="list-style-type:decimal-leading-zero">
<ol style="list-style-type:lower-alpha">
<ol style="list-style-type:lower-greek">
<ol style="list-style-type:lower-latin">
<ol style="list-style-type:lower-roman">
<ol style="list-style-type:upper-alpha">
<ol style="list-style-type:upper-latin">
<ol style="list-style-type:upper-roman">

<ol>
  <li>Coffee</li>
  <li>Milk</li>
</ol>
```

###### 定义列表
```html
<dl>                    <!--definition list-->
  <dt>项目 1</dt>       <!--definition term-->
    <dd>描述项目 1</dd> <!--definion description-->
  <dt>项目 2</dt>
    <dd>描述项目 2</dd>
</dl>
```




### HTML表单
`<form>`: 用于收集用户的输入信息，表示文档中的一个区域，此区域包含交互控件，将用户收集到的信息发送到 Web 服务器
- action属性：规定当提交表单时向何处发送表单数据
- name属性：规定表单的名称
- target属性：规定在何处打开 action URL

#### 输入域
多数情况下被用到的表单标签是输入标签`<input>`
`<input>`: 定义输入域，其输入类型由 type 属性定义
- type属性：规定要`<input>`元素输入类型/显示类型
- name属性：规定`<input>`元素的名称
- value属性：规定`<input>`元素的值

###### 文本域、密码字段
```html
<form>
First name: <input type="text" name="FirstName"><br>
Last name: <input type="text" name="LastName" value="Mouse"><br>

Password: <input type="password" name="pwd"><br>
Password: <input type="password" name="pwd" value="123456"><br>
</form>
```
- value属性：规定默认显示的值，是显性的
- size属性：规定可见宽度

###### 单选按钮（Radio Buttons）、复选框（Checkboxes）
```html
<form action="">
<input type="radio" name="sex" value="male">男<br>
<input type="radio" name="sex" value="female">女
</form>

<form>
<input type="checkbox" name="vehicle" value="Bike">我喜欢自行车<br>
<input type="checkbox" name="vehicle" value="Car">我喜欢小汽车
</form>
```
- value属性：是隐性的

###### 提交按钮
```html
<form name="input" action="html_form_action.php" method="get">
  Username: <input type="text" name="user">
  <input type="submit" value="Submit">
</form>
```
- value属性：规定显示在按钮上的值，是显性的





### HTML框架
```html
<iframe src="URL"></iframe>
<iframe src="demo_iframe.htm" width="200" height="200"></iframe>
<iframe src="demo_iframe.htm" width="200" height="200" framwborder="0"></iframe>

<!--使用 iframe 来显示目标链接页面-->
<iframe src="demo_iframe.htm" name="iframe_a"></iframe>
<a href="https://www.runoob.com" target="iframe_a">RUNOOB.COM</a>
```




### HTML脚本
```html
<body>
	
  <h1>我的第一段 JavaScript</h1>
  <p id="demo">
    JavaScript 能改变 HTML 元素的样式。
  </p>
  <script>
    function myFunction()
    {
    	x=document.getElementById("demo") // 找到元素
    	x.style.color="#FF0000";          // 改变样式
    }
  </script>
<button type="button" onclick="myFunction()">点击这里</button>
	
</body>
```



### HTML颜色
黑色：`#000000 | rgb(0,0,0) | black`
白色：`#FFFFFF | rgb(255,255,255) | white`
红色：`#FF0000 | rgb(255,0,0) | red`
绿色：`#00FF00 | rgb(0,255,0) | green`
蓝色：`#0000FF | rgb(0,0,255) | blue`

透明度：`rgba(255,0,0,0.5)` 0为全透明




### HTML字符实体

|显示结果|描述|实体名称|实体编号|
|:---|:---|:---|:---|
| 	|空格|	&nbsp;|	&#160;|
|<	|小于号|	&lt;|	&#60;|
|>	|大于号|	&gt;|	&#62;|
|&	|和号|	&amp;|	&#38;|
|"	|引号|	&quot;|	&#34;|
|'	|撇号| 	&apos;| (IE不支持)	&#39;|
|×	|乘号|	&times;|	&#215;|
|÷	|除号|	&divide;|	&#247;|

