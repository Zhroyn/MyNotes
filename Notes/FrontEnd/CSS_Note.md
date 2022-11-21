
### CSS语法
```css
选择器,
选择器 {
/* 大括号为一条声明*/
    属性:值;
    属性:值;
}
```
```css
p {margin-left:20px;}

#paral,     /*id选择器*/
.center,    /*class选择器*/
p.center    /*指定HTML元素使用class*/    
h1 {
    background-color:yellow;
}
```
###### 选择器优先级
下列是一份优先级逐级增加的选择器列表：
- 通用选择器（*）
- 元素(类型)选择器
- 类选择器
- 属性选择器
- 伪类
- ID 选择器
- 内联样式



### CSS背景
###### 背景颜色
```css
body {background-color:#b0c4de;}
```
###### 背景图片
```css
body {background-image:url('paper.gif');}

body
{
background-image:url('gradient2.png');
background-repeat:repeat-x;
}

body
{
background-image:url('img_tree.png');
background-repeat:no-repeat;
background-position:right top;
}
```
- 默认情况下，背景图像进行平铺重复显示，以覆盖整个元素实体
- `background-repeat`属性：设置水平、垂直或者不平铺
- `background-position`属性：设置图片位置




### CSS文本
```css
/*颜色*/
body {color:red;}
h1 {color:#00ff00;}
h2 {color:rgb(255,0,0);}

/*对齐方式*/
h1 {text-align:center;}
p.date {text-align:right;}
p.main {text-align:justify;}    /*每一行左、右均对齐，展开宽度相等*/

/*修饰*/
a {text-decoration:none;}       /*删除链接的下划线*/
h1 {text-decoration:overline;}
h2 {text-decoration:line-through;}
h3 {text-decoration:underline;}

/*转换*/
p.uppercase {text-transform:uppercase;}
p.lowercase {text-transform:lowercase;}
p.capitalize {text-transform:capitalize;}

/*缩进*/
p {text-indent:50px;}
```
