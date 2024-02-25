
- [窗口显示](#窗口显示)
- [图像处理](#图像处理)
    - [图像属性](#图像属性)
    - [基本 I/O](#基本-io)
    - [算术操作](#算术操作)
    - [颜色转换](#颜色转换)
    - [阈值处理](#阈值处理)
    - [几何变换](#几何变换)
        - [调整尺寸](#调整尺寸)
        - [翻转](#翻转)
        - [仿射变换](#仿射变换)
        - [透视变换](#透视变换)
        - [重映射](#重映射)
- [图像滤波](#图像滤波)
    - [通用滤波](#通用滤波)
    - [平滑图像](#平滑图像)
    - [边缘检测](#边缘检测)
- [图像匹配](#图像匹配)
    - [SIFT 算法](#sift-算法)
    - [描述符匹配](#描述符匹配)
    - [绘制关键点与匹配](#绘制关键点与匹配)
- [视频](#视频)
    - [视频捕获](#视频捕获)
        - [打开与关闭视频](#打开与关闭视频)
        - [读取帧](#读取帧)
        - [获得与设置视频属性](#获得与设置视频属性)
    - [视频写入](#视频写入)
        - [创建与保存视频](#创建与保存视频)
        - [写入帧](#写入帧)
- [绘制](#绘制)
    - [矩形](#矩形)
    - [文本](#文本)







## 窗口显示
- `namedWindow(winname[, flags]) -> None` 若该名窗口不存在，则创建一个新窗口
    - `flags`: 默认为 `cv2.WINDOW_AUTOSIZE` 或 `cv2.WINDOW_KEEPRATIO` 或 `cv2.WINDOW_GUI_EXPANDED`
        - `WINDOW_NORMAL` 允许任意调节窗口大小，`WINDOW_AUTOSIZE` 自动调整为图片大小且不可改变
        - `WINDOW_FREERATIO` 允许改变窗口长宽比例，`WINDOW_KEEPRATIO` 保持窗口比例不变
        - `WINDOW_GUI_NORMAL` 窗口没有状态栏和工具栏，`WINDOW_GUI_EXPANDED` 使用新的增强 GUI
- `destroyWindow(winname) -> None` 摧毁指定名字的窗口，若不存在则报错
- `destroyAllWindows() -> None` 摧毁所有窗口
<br>

- `imshow(winname, mat) -> None` 会自动创建窗口，必须跟随 `waitKey()` 或 `pollKey()`
- `waitKey([, delay]) -> retval` 等待按键并返回按键编码，或等待 `delay` 个毫秒并返回 -1








<br>

## 图像处理
### 图像属性
- `im.dtype` 数据类型
- `im.itemsize` 每个元素的字节数
- `im.size` 总元素数
- `im.nbytes` 所占字节数，等于 im.itemsize * im.size
- `im.shape` 格式为 (行数, 列数, 通道数)
- `im.ndim` 数组维数，等于 len(im.shape)

<br>

### 基本 I/O
- `imread(filename[, flags]) -> retval`
    - 通过文件内容决定图像格式，而不是扩展名
    - `flags`: 默认为 `cv2.IMREAD_COLOR`
        - `IMREAD_COLOR`: 用 BGR 模式加载图像，透明度会被忽略
        - `IMREAD_GRAYSCALE`: 用灰度模式加载图像
        - `IMREAD_UNCHANGED`: 若包含 alpha 通道则会保留
<br>

- `imwrite(filename, img) -> retval`
    - 通过文件扩展名决定图像保存格式
    - 若保存成功，则返回 True

<br>

### 算术操作
- 若数据类型为 `CV_8U`，则使用 `+` `-` `*` 运算符会对结果进行求模
- 当使用 `mask` 时，运算只会在掩膜的非零值处发生，其余会被置零

**加减运算**
- `add(src1, src2[, dst[, mask[, dtype]]]) -> dst`
    - dst = saturate(src1 + src2)
    - `src1` `src2`: 数组或标量，标量的形式只能为一个数或一个四元组。若为四元组，则参与运算的元素由图像通道数决定
    - `mask`: 类型需为 `CV_8UC1` 或 `CV_8SC1`
    - `dtype`: 输出数组的数据类型
- `subtract(src1, src2[, dst[, mask[, dtype]]]) -> dst`
    - dst = saturate(src1 - src2)
<br>

- `addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) -> dst`
    - dst = saturate(src1 * alpha + src2 * beta + gamma)

**位运算**
- `bitwise_not(src[, dst[, mask]]) -> dst` 非运算
- `bitwise_and(src1, src2[, dst[, mask]]) -> dst` 与运算
- `bitwise_or(src1, src2[, dst[, mask]]) -> dst` 或运算
- `bitwise_xor(src1, src2[, dst[, mask]]) -> dst` 异或运算
    - `src1` `src2`: 数组或标量，标量的形式只能为一个数或一个元组。若为元组，则元素数可为 1 或 4 或通道数。在参与运算前，标量会先转换为图像的数据类型
    - `mask`: 类型只能为单通道整数数组

<br>

### 颜色转换
- `split(m[, mv]) -> mv`
- `merge(mv[, dst]) -> dst`
    - `m`: 多通道图像
    - `mv`: 由单通道图像组成的元组，每个单通道图像的大小和深度相同
- `b, g, r = cv2.split(im)`
- `out = cv2.merge([r, g, b])`
<br>

- `cvtColor(src, code[, dst[, dstCn=0]]) -> dst`
    - 若图像新增一个 alpha 通道，则通道值会被设为该数据类型的最大值，即 CV_8U - 255，CV_16U - 65535，CV_32F - 1
    - `src`: 类型仅能为 `CV_8U` `CV_16U` 或 `CV_32F`
    - `code`: 转换码，可为 `cv2.COLOR_BGR2RGB` `cv2.COLOR_GRAY2BGR` 等
    - `dstCn`: 输出图像的通道数，若为 0，则从输入图像和转换码推断出来

<br>

### 阈值处理
- `threshold(src, thresh, maxval, type[, dst]) ->	retval, dst`
    - `thresh`: 阈值
    - `maxval`: 最大值，在某些阈值处理方法中会用到
    - `type`: 阈值处理方法

阈值处理方法有以下几种：
- `cv2.THRESH_BINARY`: $$\texttt{dst}(x,y) = \left\{ \begin{aligned} & \texttt{maxval} & \texttt{if src(x,y) > thresh} \\ & \texttt{0} & \texttt{otherwise} \end{aligned} \right.$$
- `cv2.THRESH_BINARY_INV`: $$\texttt{dst}(x,y) = \left\{ \begin{aligned} & \texttt{0} & \texttt{if src(x,y) > thresh} \\ & \texttt{maxval} & \texttt{otherwise} \end{aligned} \right.$$
- `cv2.THRESH_TRUNC`: $$\texttt{dst}(x,y) = \left\{ \begin{aligned} & \texttt{threshold} & \texttt{if src(x,y) > thresh} \\ & \texttt{src(x, y)} & \texttt{otherwise} \end{aligned} \right.$$
- `cv2.THRESH_TOZERO`: $$\texttt{dst}(x,y) = \left\{ \begin{aligned} & \texttt{src(x, y)} & \texttt{if src(x,y) > thresh} \\ & \texttt{0} & \texttt{otherwise} \end{aligned} \right.$$
- `cv2.THRESH_TOZERO_INV`: $$\texttt{dst}(x,y) = \left\{ \begin{aligned} & \texttt{0} & \texttt{if src(x,y) > thresh} \\ & \texttt{src(x, y)} & \texttt{otherwise} \end{aligned} \right.$$

<br>

### 几何变换
#### 调整尺寸
- `resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) -> dst`
    - `dsize`: 输出图像尺寸，格式为 (宽度, 高度)。若为 None，则从 fx 和 fy 计算出来
    - `fx`: x 轴缩放因数
    - `fy`: y 轴缩放因数
    - `interpolation`: 插值方法，默认为 `cv2.INTER_LINEAR`
        - `cv2.INTER_NEAREST` 最近邻插值
        - `cv2.INTER_LINEAR` 双线性插值
        - `cv2.INTER_CUBIC` 双立方插值，放大图像时效果最好
        - `cv2.INTER_AREA` 区域插值，缩小图像时效果最好
    - `cv2.resize(src, (1920, 1080), interpolation=cv2.INTER_CUBIC)`
    - `cv2.resize(src, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)`

<br>

#### 翻转
- `flip(src, flipCode[, dst]) -> dst` 翻转图像
    - `flipCode`: 翻转码
        - 若为 0，则上下翻转
        - 若为正整数，则左右翻转
        - 若为负整数，则上下翻转和左右翻转同时进行

<br>

#### 仿射变换
- `warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) -> dst` 对图像应用变换矩阵：$$\begin{aligned} \texttt{dst}(x,y) = \texttt{src} \left(M_{11}x + M_{12}y + M_{13}, M_{21}x + M_{22}y + M_{23} \right.) \end{aligned}$$
    - `M`: $2\times 3$ 变换矩阵
    - `dsize`: 输出图像的尺寸，格式为 (宽度, 高度)
    - `flags`: 插值方法或标志 `cv2.WARP_INVERSE_MAP`，代表逆变换
    - `borderMode`: 像素外推方法，默认为 `cv2.BORDER_CONSTANT`
        - `cv2.BORDER_CONSTANT`: `iiiiii|abcdefgh|iiiiiii`
        - `cv2.BORDER_REPLICATE`: `aaaaaa|abcdefgh|hhhhhhh`
        - `cv2.BORDER_REFLECT`: `fedcba|abcdefgh|hgfedcb`
        - `cv2.BORDER_WRAP`: `cdefgh|abcdefgh|abcdefg`
        - `cv2.BORDER_TRANSPARENT`: `uvwxyz|abcdefgh|ijklmno`
        - `cv2.BORDER_REFLECT_101` `cv2.BORDER_REFLECT101` `cv2.BORDER_DEFAULT`: `gfedcb|abcdefgh|gfedcba`
    - `borderValue`: 在 `cv2.BORDER_CONSTANT` 中作为边界外像素值，默认为 0
<br>

- `getRotationMatrix2D(center, angle, scale) -> retval` 计算得到一个 2D 旋转仿射矩阵：$$\alpha = \texttt{scale} \cdot \cos{\texttt{angle}} \\ \beta =  \texttt{scale} \cdot \sin{\texttt{angle}} \\ \begin{bmatrix} \alpha & \beta & (1-\alpha) \cdot \texttt{center.x} - \beta \cdot \texttt{center.y} \\ \beta  & \alpha & \beta \cdot \texttt{center.x} + (1-\alpha) \cdot \texttt{center.y} \end{bmatrix}$$
    - `center`: 旋转中心，格式为 (x, y)
    - `angle`: 旋转角度，正数为逆时针方向
    - `scale`: 缩放因数
<br>

- `getAffineTransform(src, dst) -> retval` 用三对点计算得到仿射矩阵
    - `src`: $3\times 2$ 矩阵，存放源图像的三对点
    - `dst`: $3\times 2$ 矩阵，存放目标图像的三对点

```py
def rotate(src, center, angle, scale=1, color=0):
    h, w = src.shape[:2]
    bound_h = scale * (h * abs(np.cos(angle * np.pi / 180)) + 
                       w * abs(np.sin(angle * np.pi / 180)))
    bound_w = scale * (h * abs(np.sin(angle * np.pi / 180)) + 
                       w * abs(np.cos(angle * np.pi / 180)))
    M = cv2.getRotationMatrix2D(center, angle, scale)
    M[0, 2] += (bound_w - w) / 2
    M[1, 2] += (bound_h - h) / 2
    size = (int(bound_w), int(bound_h))
    dst = cv2.warpAffine(src, M, size, borderValue=color)
    return dst

def translate(src, x, y, color=0):
    M = np.array([[1.0, 0, x],
                  [0, 1.0, y]])
    h, w = src.shape[:2]
    bound_h = h + y if y > 0 else h
    bound_w = w + x if x > 0 else w
    size = (int(bound_w), int(bound_h))
    dst = cv2.warpAffine(src, M, size, borderValue=color)
    return dst
```

<br>

#### 透视变换
- `warpPerspective(src, M, dsize[,dst[, flags[, borderMode[, borderValue]]]]) -> dst` 对图像应用变换矩阵：$$\begin{aligned} \texttt{dst}(x,y) =  \texttt{src}\left( \frac{M_{11} x + M_{12} y + M_{13}}{M_{31} x + M_{32} y + M_{33}}, \frac{M_{21} x + M_{22} y + M_{23}}{M_{31} x + M_{32} y + M_{33}} \right) \end{aligned}$$
    - `M`: $3\times 3$ 变换矩阵
    - `dsize`: 输出图像的尺寸
<br>

- `getPerspectiveTransform(src, dst) -> retval` 用四对点计算得到投影矩阵
    - `src`: $4\times 2$ 矩阵，存放源图像的四对点
    - `dst`: $4\times 2$ 矩阵，存放目标图像的四对点

<br>

#### 重映射
- `remap(src, map1, map2, interpolation[, dst[, borderMode[, borderValue]]]) -> dst` 对图像应用通用几何变换：$$\texttt{dst}(x,y) = \texttt{src}(map_x(x,y), map_y(x,y))$$
    - `map1`: 第一个映射，返回值为 (x,y) 点或 x 值，类型为 `CV_16SC2` `CV_32FC1` 或 `CV_32FC2`
    - `map2`: 第二个映射，返回值为 y 值，类型为 `CV_16UC1` `CV_32FC1` 或 None
    - `interpolation`: 插值方法











<br>

## 图像滤波
### 通用滤波
- `filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) -> dst` 用卷积核对图像进行卷积
    - `ddepth`: 输出图像的深度，若为 -1 则与输入相同
    - `kernel`: 卷积核
    - `anchor`: 指定卷积核内的滤波点的相对位置，应该位于卷积核内，默认值为 (-1, -1)，表示在内核中心
    - `delta`: 结果加上的值
    - `cv2.filter2D(src, -1, kernel)`
    - `cv2.filter2D(src, -1, kernel, delta=5)`


<br>

### 平滑图像
- `blur(src, ksize[, dst[, anchor[, borderType]]]) -> dst` 均值滤波
  $$K = \frac{1}{width * height} 
  \begin{bmatrix} 
      1 & 1 & \cdots & 1 \\
      1 & 1 & \cdots & 1 \\
      \vdots & \vdots & \ddots & \vdots \\
      1 & 1 & \cdots & 1 \\ 
  \end{bmatrix}$$
    - `ksize`: 卷积核的尺寸，可以为任意二元组
    - `anchor`: 锚点，默认值为 (-1, -1)，指卷积核中点
    - `borderType`: 像素外推方法
<br>

- `boxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]) -> dst` 方框滤波
    $$K = \alpha
    \begin{bmatrix} 
        1 & 1 & \cdots & 1 \\
        1 & 1 & \cdots & 1 \\
        \vdots & \vdots & \ddots & \vdots \\
        1 & 1 & \cdots & 1 \\ 
    \end{bmatrix}, \\~\\
    \alpha = \left\{ 
        \begin{aligned}
          &\frac{1}{width * height} &\text{when normalize=true} \\
          &1 &\text{otherwise} \\
        \end{aligned}
    \right. $$
    - `ddepth`: 输出图像的深度，若为 -1 则与输入相同
    - `ksize`: 卷积核的尺寸，可以为任意二元组
    - `normalize`: 指定是否规范化，默认为 True
<br>

- `GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst` 高斯滤波
    - `ksize`: 高斯核的尺寸，宽和高必须全为奇数。若全为零，则会从 sigma 算出
    - `sigmaX`: x 方向的高斯标准差
    - `sigmaY`: y 方向的高斯标准差，若为零则与 sigmaX 相等，若全为零则会从 ksize 算出
- `getGaussianKernel(ksize, sigma[, ktype]) ->	retval`
    - 返回一个大小为 $\texttt{ksize}\times 1$ 的矩阵，存放高斯滤波器的系数
    - `ksize`: 孔径的宽高，必须为一个大于 0 的奇数
    - `sigma`: 高斯标准差，若非正数，则等于 0.3 * ((ksize - 1) * 0.5 - 1) + 0.8
    - 若想得到 $\texttt{ksize} \times \texttt{ksize}$ 的 2D 高斯核，可以使用 `kernel = cv2.getGaussianKernel(ksize, 0); kernel = kernel * kernel.T`
<br>

- `medianBlur(src, ksize[, dst]) -> dst` 中值滤波
    - `ksize`: 孔径的宽高，必须为一个大于 1 的奇数
    - 对边界像素，会使用 `cv2.BORDER_REPLICATE`
<br>

- `bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) -> dst` 双边滤波
    - `d`: 像素邻域的直径，若非正则会从 sigmaSpace 算出
    - `sigmaColor`: 颜色空间中的标准差，值越大，像素邻域内更远的颜色将混合在一起
    - `sigmaSpace`: 坐标空间中的标准差，值越大，更远的像素将相互影响。当 d > 0 时，d 指定了邻域的大小，sigmaSpace 不起作用，否则 d 与 sigmaSpace 成比例


<br>

### 边缘检测
- `Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst` 用扩展 Sobel 运算符，计算图像的指定阶导数
  $$\texttt{dst} = \frac{\partial^{dx+dy} \texttt{src}}{\partial x^{dx} \partial y^{dy}} $$
    - `dx`: x 方向的导数的阶
    - `dy`: y 方向的导数的阶
    - `ksize`: 卷积核的尺寸，只能为 1, 3, 5 或 7，默认为 3。当 kernel = 1 时，实际尺寸为 $3\times 1$ 或 $1\times 3$
    - `scale`: 缩放因数，默认为 1
    - `delta`: 偏移值，默认为 0
    - `cv2.Soble(src, -1, 1, 0)` 使用的卷积核是 $\begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$
<br>

- `Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst` 计算图像的拉普拉斯算子
  $$\texttt{dst} = \Delta \texttt{src} = \frac{\partial^{2} \texttt{src}}{\partial x^2} + \frac{\partial^{2} \texttt{src}}{\partial y^2} $$
    - `ksize` 孔径的宽高，只能为大于 0 的奇数，默认为 1，此时使用的卷积核为 $\begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \\ \end{bmatrix}$








<br>

## 图像匹配
### SIFT 算法
```py
sift = cv2.SIFT_create()

keypoints = sift.detect(im)
keypoints, descriptors = sift.compute(im, keypoints)

keypoints, descriptors = sift.detectAndCompute(im, None)
```
SIFT 关键点的属性有：
- `pt` 关键点坐标
- `size` 关键点邻域直径
- `angle` 关键点的方向
- `response` 关键点的响应强度，可用于后续排序
- `octave` 关键点所在的图像金字塔的层组
- `class_id` 用于聚类的 id
<br>

- `sift.detect(image[, mask]) -> keypoints`
    - keypoints[i] 为第 i 个关键点
    - mask 指定了寻找关键点的区域
- `sift.detect(images[, masks]) -> keypoints`
    - keypoints[i] 为 image[i] 的关键点
    - mask[i] 为 image[i] 的掩膜


<br>

### 描述符匹配
```py
bf = cv2.BFMatcher_create()
matches = bf.match(descriptors1, descriptors2)
matches = bf.knnMatch(descriptors1, descriptors2, 2)
```
匹配的属性有
- `queryIdx` 关键点在 keypoints1 中的索引
- `trainIdx` 关键点在 keypoints2 中的索引
- `imgIdx` 当前匹配点对应训练图像的索引
- `distance` 关键点之间的欧氏距离
<br>

- `match(queryDescriptors, trainDescriptors[, mask]) -> matches`
    - 对查询集中的每个描述符，找到 1 个最佳匹配项
    - `queryDescriptors`: 查询描述符集
    - `trainDescriptors`: 训练描述符集
    - `matches`: 每一项都是对应查询点与其最佳匹配项的匹配
<br>

- `knnMatch(queryDescriptors, trainDescriptors, k[, mask[, compactResult]]) -> matches`
    - 对查询集中的每个描述符，找到 k 个最佳匹配项
    - `matches`: 每一项都是一个列表，包含对应查询点与其 k 个最佳匹配项的匹配

<br>

### 绘制关键点与匹配
- `drawKeypoints(image, keypoints, outImage[, color[, flags]]) -> outImage`
    - 绘制一张图上的关键点
    - `color`: 关键点的颜色，默认为随机选择
    - `out = cv2.drawKeypoints(im, kpts, None)`
<br>

- `drawMatches(img1, keypoints1, img2, keypoints2, matches1to2, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]) -> outImg`
- `drawMatches(img1, keypoints1, img2, keypoints2, matches1to2, outImg, matchesThickness[, matchColor[, singlePointColor[, matchesMask[, flags]]]]) -> outImg`
- `drawMatchesKnn(img1, keypoints1, img2, keypoints2, matches1to2, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]) -> outImg`
    - 绘制两张图之间的匹配
    - `out = cv2.drawMatches(im1, kpts1, im2, kpts2, matches, None)`









<br>

## 视频
### 视频捕获
#### 打开与关闭视频
- `VideoCapture(filename[, apiPreference]) -> retval` 打开一个视频或一个捕获设备
- `cap.isOpened() -> retval` 检测是否打开成功
- `cap.release() -> None` 释放视频流

<br>

#### 读取帧
- `cap.read([, image]) -> retval, image` 读取一帧

<br>

#### 获得与设置视频属性
- `cap.get(propId) -> retval` 返回指定属性
- `cap.set(propId, value) -> retval` 设置指定属性
<br>

- `cv2.CAP_PROP_POS_MSEC` 当前视频所在位置，以毫秒计
- `cv2.CAP_PROP_POS_FRAMES` 下一帧的索引，从零开始计
- `cv2.CAP_PROP_POS_AVI_RATIO` 当前视频的相对位置，0 代表开头，1 代表结尾
- `cv2.CAP_PROP_FRAME_WIDTH` 帧的宽度
- `cv2.CAP_PROP_FRAME_HEIGHT` 帧的高度
- `cv2.CAP_PROP_FRAME_COUNT` 帧的总数
- `cv2.CAP_PROP_FPS` 帧率
- `cv2.CAP_PROP_FOURCC` 编解码器的四字符代码

<br>

### 视频写入
#### 创建与保存视频
- `VideoWriter(filename, fourcc, fps, frameSize, isColor=ture) -> retval` 初始化视频写入器
    - `fourcc`: 用于压缩帧的编解码器的四字符代码，若为 -1，会列出所有可选项
        - `cv2.VideoWriter_fourcc(*"mp4v"/"avc1"/"avc3")` 可用于 mp4 视频
        - `cv2.VideoWriter_fourcc(*"XVID"/"MJPG"/"h264")` 可用于 avi 视频
        - `cv2.VideoWriter_fourcc(*"I420")` 可用于 `.avi` 未压缩视频
    - `fps`: 帧率
    - `frameSize`: 帧的尺寸，格式为 (宽, 高)，必须全为整数
    - `isColor`: 若非零，则会以彩色模式编码视频
<br>

- `video.isOpened() -> retval` 检测是否初始化成功
- `video.release() -> None` 关闭视频写入器

<br>

#### 写入帧
- `write(image) ->	None` 写入一帧，image 需为 BGR 模式且尺寸必须一致










<br>

## 绘制
### 矩形
- `rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img`
    - `pt1`: 一个顶点
    - `pt2`: 另一个顶点
    - `color`: 颜色（RGB 模式）或亮度（灰度模式）
    - `thickness`: 线的厚度，负数意味着填满

<br>

### 文本
- `putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img`
    - `org`: 文本的左下角位置
    - `fontFace`: 字体类型
    - `fontScale`: 缩放因数，用以乘上字体的基本大小
    - `color`: 文本颜色（RGB 模式）
    - `thickness`: 厚度
    - `lineType`: 线条类型
    - `bottomLeftOrigin`: 若为 True，则图像的数据原点设为左下角

**lineType**
- `cv2.LINE_4` 4 连通线条（默认值），线条的像素相互连接
- `cv2.LINE_8` 8 连通线条，可以更精确地绘制斜线
- `cv2.LINE_AA` 抗锯齿线条，会进行平滑处理，使线条的边缘更柔和

**fontFace**
- `cv2.FONT_HERSHEY_SIMPLEX` 普通大小的无衬线字体
- `cv2.FONT_HERSHEY_PLAIN` 小号无衬线字体
- `cv2.FONT_HERSHEY_DUPLEX` 普通大小的无衬线字体，更加复杂
- `cv2.FONT_HERSHEY_COMPLEX` 普通大小的衬线字体
- `cv2.FONT_HERSHEY_TRIPLEX` 普通大小的衬线字体，更加复杂
- `cv2.FONT_HERSHEY_COMPLEX_SMALL` 小号衬线字体
- `cv2.FONT_HERSHEY_SCRIPT_SIMPLEX` 手写风格字体
- `cv2.FONT_HERSHEY_SCRIPT_COMPLEX` 手写风格字体，更加复杂
- `cv2.FONT_ITALIC` 斜体字体标记



