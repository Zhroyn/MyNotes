- [控件](#控件)
    - [应用程序](#应用程序)
    - [窗口桌面](#窗口桌面)
    - [文本](#文本)
    - [输入框](#输入框)
    - [按钮](#按钮)
    - [布局](#布局)
        - [QBoxLayout](#qboxlayout)
        - [QGroupBox](#qgroupbox)
        - [QGridLayout](#qgridlayout)
        - [QFormLayout](#qformlayout)
        - [QStackedLayout](#qstackedlayout)





## 控件
### 应用程序
```py
QApplication(argv: List[str])

app = QApplication(sys.argv)
```
- `app.exec()` 使程序保持运行

<br>

### 窗口桌面
```py
QWidget(
    parent: typing.Optional[QWidget] = None,
    flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()
)
QDesktopWidget()

w = QWidget()
screen = QDesktopWidget()
```
- `w.setWindowTitle(title)` 设置窗口标题
- `w.setWindowIcon(QIcon)` 设置窗口 icon
    - `QIcon = PyQt5.QtGui.QIcon(icon_path)` 图片会变形为正方形
- `w.setLayout` 设置窗口布局
- `w.setStyleSheet(styleSheet)` 设置窗口样式
    - `w.setStyleSheet("background-color:green;")` 背景颜色会变为绿色
<br>

- `w.resize(w, h)` 调整窗口大小
- `w.setFixedSize(w, h)` 设置固定尺寸
- `w.setFixedWidth(w, h)` 设置固定宽度
- `w.setFixedHeight(w, h)` 设置固定高度
<br>

- `w/screen.frameGeometry()` 获得 QRect 类
- `w/screen.frameGeometry().getRect()` 获得边界矩阵，形式为 (x, y, w, h)
- `center = w/screen.frameGeometry().center()` 获得中点
- `center.x()` 获得中点的 x 坐标
- `center.y()` 获得中点的 y 坐标

<br>

### 文本
```py
QLabel(
    parent: typing.Optional[QWidget] = None,
    flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()
)
QLabel(
    text: str,
    parent: typing.Optional[QWidget] = None,
    flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()
)

label = QLabel(text, w)
```
- `label.setGeometry(x, y, w, h)` 设置控件位置
- `label.setText(text)` 设置文本内容
- `label.setFixedSize(w, h)` 设置固定尺寸

<br>

### 输入框
```py
QLineEdit(
    parent: typing.Optional[QWidget] = None
)
QLineEdit(
    contents: str,
    parent: typing.Optional[QWidget] = None
)

edit = QLineEdit(text, w)
```
- `edit.setGeometry(x, y, w, h)` 设置控件位置
- `edit.setText(text)` 设置文本内容
- `edit.setFixedSize(w, h)` 设置固定尺寸
- `edit.setPlaceholderText(text)` 设置占位文本，在无文本时显示

<br>

### 按钮
```py
QPushButton(parent: typing.Optional[QWidget] = None)
QPushButton(
    text: str,
    parent: typing.Optional[QWidget] = None
)
QPushButton(
    icon: QIcon,
    text: str,
    parent: typing.Optional[QWidget] = None
)

QRadioButton(parent: typing.Optional[QWidget] = None)
QRadioButton(
    text: str,
    parent: typing.Optional[QWidget] = None
)

btn = QPushButton(text, w)
btn = QRadioButton(text, w)
```
- `btn.setGeometry(x, y, w, h)` 设置控件位置
- `btn.setText(text)` 设置文本内容
- `btn.setFixedSize(w, h)` 设置固定尺寸
<br>

- `btn.clike.connect(slot)` 绑定鼠标左键按下
- `btn.cliked.connect(slot)` 绑定鼠标左键释放

<br>

### 布局
#### QBoxLayout
```py
QVBoxLayout()
QVBoxLayout(parent: QWidget)

QHBoxLayout()
QHBoxLayout(parent: QWidget)

v_layout = QVBoxLayout()
h_layout = QHBoxLayout()
```
- `box.addWidget(widget, alignment=Qt.Alignment())` 添加控件
    - 对齐标志在 `PyQt5.QtCore.Qt.AlignmentFlag`，包括 `AlignTop, AlignBottom, AlignLeft, AlignRight` `AlignCenter, AlignVCenter, AlignVCenter` 等
- `box.addStretch(stretch=0)` 添加伸缩量，用以控制控件之间距离的比例
- `box.addLayout(layout)` 添加布局

<br>

#### QGroupBox
```py
QGroupBox(parent: typing.Optional[QWidget] = None)
QGroupBox(
    title: str,
    parent: typing.Optional[QWidget] = None
)

# 可用于嵌套布局，如
box1 = QGroupBox()
vbox = QVBoxLayout()
vbox.addWidget(widget)
vbox.addWidget(widget)
box1.setLayout(vbox)

box2 = QGroupBox()
hbox = QHBoxLayout()
hbox.addWidget(widget)
hbox.addWidget(widget)
box2.setLayout(hbox)

layout = QVBoxLayout()
layout.addWidget(box1)
layout.addWidget(box2)
w.setLayout(layout)
```

<br>

#### QGridLayout
```py
QGridLayout(parent: QWidget)
QGridLayout()

grid = QGridLayout()
```
- `grid.addWidget(widget)` 默认沿竖排排列
- `grid.addWidget(widget, row, column[, alignment])`
- `grid.addWidget(widget, row, column, rowSpan, columnSpan[, alignment])`
<br>

- `grid.addLayout(widget, row, column[, alignment])`
- `grid.addLayout(widget, row, column, rowSpan, columnSpan[, alignment])`

<br>

#### QFormLayout
```py
QFormLayout(parent: typing.Optional[QWidget] = None)

form_layout = QFormLayout()
```
- `form_layout.addRow(label, field)`
- `form_layout.addRow(labelText, field)`

<br>

#### QStackedLayout
```py
QStackedLayout()
QStackedLayout(parent: QWidget)
QStackedLayout(parentLayout: QLayout)

stacked_layout = QStackedLayout()

# 将多个界面添加进布局中
w1 = QWidget()
w2 = QWidget()
stacked_layout.addWidget(w1)
stacked_layout.addWidget(w2)

# 创建按钮用来切换界面
btn_press1 = QPushButton("Main Interface")
btn_press2 = QPushButton("Setting Interface")
btn_press1.clicked.connect(btn_press1_clicked)
btn_press2.clicked.connect(btn_press2_clicked)

# 创建布局用来安放所有布局与控件
layout = QVBoxLayout()
layout.addLayout(stacked_layout)
layout.addWidget(btn_press1)
layout.addWidget(btn_press2)
w.setLayout(layout)

def btn_press1_clicked():
    stacked_layout.setCurrentIndex(0)

def btn_press2_clicked():
    stacked_layout.setCurrentIndex(1)
```



