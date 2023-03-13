<!-- TOC -->

- [窗口系统（Window System）](#窗口系统window-system)
- [编辑器（Editor）](#编辑器editor)
  - [3D视图（3D Viewport）](#3d视图3d-viewport)
    - [模式（Mode）](#模式mode)
    - [变换控件（Controls）](#变换控件controls)
    - [导航（Navigating）](#导航navigating)
    - [3D游标（3D Cursor）](#3d游标3d-cursor)
    - [显示方式（Display）](#显示方式display)
    - [视图着色（Shading）](#视图着色shading)
    - [选择（Select）](#选择select)
- [建模](#建模)
  - [网格](#网格)

<!-- /TOC -->




## 窗口系统（Window System）
- Blender界面分为以下三个部分：
  - 顶部标题栏（Topbar）
  - 工作区（Workspaces）
  - 状态栏（Status Bar）

**顶部标题栏**
- Edit
  - Repeat Last : `Shift R`
  - Repeat History
  - Adjust Last Operation : `F9`
  - Lock Object Modes
  - Preference
- Window
  - Next Workspace : `Ctrl Page Down`
  - Previous Workspace : `Ctrl Page Up`
  - Show Status Bar

**工作区**
- 工作区本质上是预定义的窗口布局，每个工作区由一组区域和编辑器组成
- Blender的默认启动在主区域显示了`Layout`工作区。这个工作区是一个一般的工作区，用于预览你的场景，包含以下编辑器：
  - 左上角的3D视图
  - 右上角的大纲
  - 右下角的属性
  - 左下角的时间轴

**状态栏**
- 状态栏的右侧显示有关Blender实例的信息，显示哪些信息可以通过点击`RMB`来选择
  - 场景统计
    - 集合：活动的集合的名称
    - 活动的对象：显示当前所选活动物体的名称
    - 几何数据（Geometry）：根据模式和物体类型显示有关当前场景的信息，可以是顶点、面、三角形或骨骼的数量
    - 物体：所选物体的数量和总数
  - 系统内存：Blender内存消耗估计值
  - Blender 版本

**区域**
- Blender窗口被划分为若干矩形，称为区域（Area）。区域为编辑器保留屏幕空间，例如3D视图或大纲。每个编辑器都提供了一个特定的功能。
- 拆分：左上角按下`LMB`向内拖动
  - 在释放鼠标前按下`Esc`或`RMB`，操作将被取消
- 合并：左上角按下`LMB`向外拖动
  - 在释放鼠标前按下`Esc`或`RMB`，操作将被取消
- 互换：左上角按下`Ctrl-LMB`向目标区域拖动
- 切换区域最大化(Toggle Maximum Area) : `Ctrl-Spacebar`

**区块**
- Blender中的每个编辑器都分成几个区块（Region），区块可以具有较小的结构元素
  - 主区块：至少有一个区块始终可见，被称为主区块，是编辑器中最重要的部分
  - 标题栏：是一个小的水平条，位于区域的顶部或底部。所有编辑器都有标题栏，用于容纳菜单和常用工具，菜单和按钮将随编辑器类型、所选物体、模式而改变
  - 工具栏：在编辑器区域的左侧，包含一组交互式工具
  - 侧栏：位于编辑器区域右侧，包含编辑器中物体与编辑器自身的设置面板
  - 底栏：一些编辑器显示一个栏，显示例如活动工具或操作者的信息
  - 调整上一步操作：出现在左下角

**选项卡 & 面板**
- 选项卡：标签是用来控制用户界面中的重叠部分的，每次只有一个标签的内容是可见的。标签被列在一个标签头中，它可以是水平的或垂直的
  - 切换/循环：垂直标签可以在标签的任何地方用 `Ctrl-Wheel` 进行切换
  - 也可以用 `Ctrl-Tab` 和 `Shift-Ctrl-Tab` 循环切换标签
- 面板：用户界面中最小的组织单元是一个面板。面板顶部显示面板的标题，它总是可见的，有些面板还包括子面板

**通用快捷键**
- `Ctrl` : 拖动时吸附倍数步长
- `Shift` : 精确控制拖拽的值
<br>




## 编辑器（Editor）
### 3D视图（3D Viewport）
- 顶部标题栏（Header Rigion）
  - 模式
  - 菜单
  - 变换控件
  - 显示方式
  - 着色类型
- 工具栏（Toolbar Rigion）
  - `T` : 切换显示工具栏
  - `Shift-Spacebar` 弹出工具栏
- 侧栏（Sidebar Rigion）
  - `N` : 切换显示侧栏

#### 模式（Mode）
- 按 `Tab` 在物体模式和编辑模式之间切换
- 按 `Ctrl+Tab` 弹出一个饼状菜单用于快速切换，如果选择了一个骨架，将会在物体模式和姿势模式之间切换

#### 变换控件（Controls）
- 变换方向
  - `,` : 切换变换方向
- 变换轴心点
  - `.` : 切换变换轴心点
- 吸附
  - `Shift-Tab` : 开关吸附
  - `Shift-Ctrl-Tab` : 切换吸附方式
- 衰减编辑
  - `O` : 开关衰减编辑
  - `Shift-O` : 切换衰减模式
  - `WheelUp` : 增加衰减半径
  - `WheelDown` : 减小衰减半径

#### 导航（Navigating）
**视图（Viewpoint）**
- `Numpad1` or `Ctrl-Numpad1` : 正视图
- `Numpad3` or `Ctrl-Numpad3` : 侧视图
- `Numpad7` or `Ctrl-Numpad7` : 俯视图
- `Numpad9` : 反转视图
- `Numpad0` : 相机视图

**导航（Navigation）**
- 环绕（Orbit）
  - `MMB`, `Numpad2`, `Numpad4`, `Numpad6`, `Numpad8` : 围绕关注点旋转视图
  - `Numpad9` : 切换到视图的另一侧，使摄像机围绕Z轴旋转180°
  - 单击具有 `Alt-MMB` 的点将使其成为兴趣点，它将成为视图环绕的中心点
  - 按住 `Alt` ，然后用 `MMB` 向某个方向拖动将对齐视图到轴并使其正交
  - 使用 `MMB` 拖动，然后按住 `Alt` 将执行环绕，同时捕捉到世界轴以及它们之间的对角线
- 扭转（Roll）
  - `Shift-Numpad4`, `Shift-Numpad6` : 左转/右转15°
- 平移（Pan）
  - `Shift-MMB`, `Ctrl-Numpad2`, `Ctrl-Numpad4`, `Ctrl-Numpad6`, `Ctrl-Numpad8`
- 缩放（Zoom）
  - `Ctrl-MMB`, `Wheel`, `NumpadPlus`, `NumpadMinus`
- `Shift-B` : 框选放大
- `Home` : 显示全部

**飞行/步行导航（Fly/Walk Navigation）**
- 从相机视图激活时 `Numpad0`，相机将跟随移动
- 步行导航
  - `W/Up` : 前进
  - `S/Down` : 后退
  - `A/Left` : 左平移
  - `D/Right` : 右平移
  - `E` : 向上移动，仅当重力关闭时才可用
  - `Q` : 向下移动，仅当重力关闭时才可用
  - `Shift` : 暂时加速移动
  - `Alt` : 暂时慢速移动
  - `Tab` : 切换重力
- 飞行导航
  - `W/Up` : 向前加速
  - `S/Down` : 向后加速
  - `A/Left` : 向左加速
  - `D/Right` : 正确加速
  - `E` : 向上加速
  - `Q` : 向下加速
  - `MMB` : 拖动来平移视图，飞行会暂停
  - `WheelUp/NumpadPlus` : 增加运动方向的加速度。如果没有动作，开始向前加速
  - `WheelDown/NumpadMinus` : 减小运动方向的加速度。如果没有动作，则开始向后加速
  - `Alt` : 只要按住Alt键，就会慢下来，直到视图最终陷入停顿

**对齐（Aligning）**
- `Ctrl-Alt-Numpad0` : 活动相机对齐当前视角
- 活动相机对齐选中的物体
- `Shift-C` : 游标回到中间并显示全部
- 视图中心对齐游标
- 视图居中对齐3D游标。
- 锁定视图至活动物体
- 清除视图锁定

**透视/正交（Perspective/Orthographic）**
- `Numpad5` : 切换透视投影和正交投影

**视图区块（View Region）**
- `Alt-B` : 裁剪区块/删除裁剪
- `Ctrl-B` : 渲染区块

**区域（Areas）**
- `Ctrl-Alt-Q` : 切换四格视图


#### 3D游标（3D Cursor）
- `Shift-RMB` : 在视图中直接放置
- `Shift-S` : 弹出吸附菜单
- `N` : 在侧栏中修改


#### 显示方式（Display）
- 视口小部件（Gizoms）
- 视图叠加层（Overlays）

#### 视图着色（Shading）
- 有四种模式：线框、实体、材质预览、渲染
- `Z` : 切换着色模式
- `Shift-Z` : 在当前模式和线框模式之前切换
- `Alt-Z` : 切换X-透视

#### 选择（Select）
- 在物体模式中最后被选择的物件叫活动物体，且它在大纲中呈黄色，其它为橙色
- 如果你已有一个选中项，但想要使另一个物体成为活动物体，只需再用 `Shift-LMB` 选择一次
<br>

- `A` : 全部选择
- `Alt-A` : 全不选
- `Ctrl-I` : 反选
- `H` : 隐藏选择
- `Alt-H` : 取消隐藏
<br>

- `B` : 框选
- `C` : 刷选
- `Ctrl-LMB` : 套选
- 调整
- `W` : 快捷键循环







## 建模
### 网格
- 细分（Subdivide）：需要是三边形或四边形
- 删除 & 融并
  - 直接删除：`Delete`
  - 融并（上下文敏感）: `Ctrl-X`
  - 融并顶点：移除选中顶点，并合并周围的面；在选中两条边时，将其融并为一条边
  - 融并边：移除面之间的公共边，合并这些面
  - 融并面：将存在公共边的面融并为一个面
  - 有限融并：融并平坦区域中的顶点和边线，简化网格
  - 塌陷边线&面：将每个独立的边和线区域坍塌为一个顶点
  - 循环边：删除夹在两组循环边之间的选定循环边，将现有的两组面循环转变为一组面循环
- 挤出（Extrude）




