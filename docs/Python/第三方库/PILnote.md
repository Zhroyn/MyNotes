
- [Image](#image)
    - [图像属性](#图像属性)
    - [基本 I/O](#基本-io)
    - [颜色转换](#颜色转换)
    - [剪切粘贴](#剪切粘贴)
    - [几何变换](#几何变换)
    - [像素操作](#像素操作)
    - [创建图像](#创建图像)
- [ImageFilter](#imagefilter)
    - [MultibandFilter](#multibandfilter)
        - [BuiltinFilter](#builtinfilter)
- [ImageEnhance](#imageenhance)
- [ImageGrab](#imagegrab)







### Image
#### 图像属性
- `im.filename` 图像名
- `im.format` 图像格式，如 JPEG, PNG
- `im.size` 图像尺寸，形式为(宽, 高)
- `im.width` 图像宽度
- `im.height` 图像高度
- `im.mode` 颜色模式
        - `1` 1-bit 黑白
        - `L` 8-bit 灰度
        - `P` 8-bit 256色
        - `RGB` 24-bit Red, Green, Blue
        - `RGBA` 32-bit Red, Green, Blue, Alpha
        - `CMYK` 32-bit Cyan, Magenta, Yellow, Key plate
        - `YCbCr` 24-bit Luminance, Blue, Red

<br>

#### 基本 I/O
- `Image.open(fp, mode='r', formats=None)` 打开图像
- `im.save(fp, format=None)` 保存图片，格式默认由后缀名决定
- `im.close()` 关闭图片
<br>

- `im.show()` 展示图片
- `im.load()` 加载图片，返回可索引的对象

<br>

#### 颜色转换
- `im.convert(mode=None, ...)` 转换颜色模式，返回副本
- `im.split()` 分离图像通道
    - `r, g, b = im.split()`
- `im.getchannel(channel)` 得到图像单个通道
    - `channel` 索引或通道名
- `im.putalpha(alpha)` 添加或替换透明度通道
    - `alpha` 图像或整数。若为图像，则必须尺寸相同，颜色模式为 1 或 L
<br>

- `Image.merge(mode, bands)` 混合通道
    - `Image.merge("RGB", (b, g, r))`

<br>

#### 剪切粘贴
- `im.copy()` 返回图片副本
- `im.crop(box=None)` 裁剪出矩形区域
    - `box` 四元元组，形式为 (左, 上, 右, 下)
- `im.paste(im, box=None, mask=None)` 将另一张图像粘贴至此图像，不返回副本
    - `im` 图像或像素值
    - `box` 包含左上角坐标的二元元组，或包含左上右下边界的四元元组，默认为图像左上角，尺寸应与被粘贴图像一致
    - `mask` 掩膜尺寸应与被粘贴图像一致，颜色模式可为 1, L, RGBA 等，其中后者使用透明度通道
        - 若掩膜值为 0，则原图像像素值不变
        - 若掩膜值为 255，则采用被粘贴图像的像素值
        - 若掩膜值介于两者之间，则采用原图像与被粘贴图像混合的像素值

<br>

#### 几何变换
- `im.resize(size, resample=None, box=None, reducing_gap=None)` 改变尺寸，返回副本
    - `size` 图像尺寸，形式为 (宽, 高)
    - `resample` 一般默认为 `Image.BICUBIC`
    - `box` 被改变尺寸的区域，形式为 (左, 上, 右, 下)，可以用浮点数
<br>

- `im.transpose(method)` 翻转或旋转图像，返回副本
    - `Image.Transpose.FLIP_LEFT_RIGHT` 左右翻转
    - `Image.Transpose.FLIP_TOP_BOTTOM` 上下翻转
    - `Image.Transpose.ROTATE_90` 逆时针旋转 90 度
    - `Image.Transpose.ROTATE_180` 逆时针旋转 180 度
    - `Image.Transpose.ROTATE_270` 逆时针旋转 270 度
    - `Image.Transpose.TRANSPOSE` 转置
    - `Image.Transpose.TRANSVERSE` 转置后旋转 180 度
<br>

- `im.rotate(angle, resample=<Resampling.NEAREST: 0>, expand=0, center=None, translate=None, fillcolor=None)` 逆时针旋转图像，返回副本
    - `angle` 旋转角度，可以为负数或浮点数
    - `expand` 若为 True，会扩张旋转后的图像
    - `center` 默认为图像中心
    - `translate` 在旋转之后进行平移，形式为 (横轴, 纵轴)
    - `fillcolor` 填充颜色。若为整数，则为第一个通道的值，其余通道置零；若为元组，则大小应与通道数相同

<br>

#### 像素操作
- `im.getpixel(xy)` 获得像素值
    - `xy` 横轴为 x，纵轴为 y，形式为 (x, y)
- `im.putpixel(xy, value)` 设置像素值
<br>

- `im.point(lut, mode=None)` 映射图像，返回副本
    - `lut` 查找表或函数。若为函数，则输入一个像素值，返回一个像素值
    - `im.point(lambda x: 0 if x < 128 else 255)`
- `Image.eval(im, *args)` 对每个像素值应用一个函数
    - `Image.eval(im, lambda x: 0 if x < 128 else 255)`
<br>

- `im.filter(filter)` 对图像进行滤波，返回副本
    - `im.filter(ImageFilter.GaussianBlur)`

<br>

#### 创建图像
- `Image.new(mode, size, color=0)`
- `Image.fromarray(obj, mode=None)` 如果传入数组的 shape 为 (x, x, 3)，会当作 RGB 模式处理
- `Image.blend(im1, im2, alpha)` 融合两张图像
    - 两张图像尺寸和颜色模式应相同
    - 新的图像 = image1 * (1.0 - alpha) + image2 * alpha








<br>

### ImageFilter
#### MultibandFilter
- `ImageFilter.GaussianBlur(radius=2)` 高斯滤波
- `ImageFilter.BoxBlur(radius)` 方框滤波，取平均值
<br>

- 当 radius = 0 时，滤波不起作用
- 当 radius = 1 时，卷积核大小为 3x3
<br>

##### BuiltinFilter
```py
class Kernel(BuiltinFilter):
    name = "Kernel"

    def __init__(self, size, kernel, scale=None, offset=0):
        if scale is None:
            scale = functools.reduce(lambda a, b: a + b, kernel)
        if size[0] * size[1] != len(kernel):
            raise ValueError("not enough coefficients in kernel")
        self.filterargs = size, scale, offset, kernel
```
- `size` 二元数组，形式为 (宽, 高)，宽高可以不同
- `kelnel` 卷积核，展开为一维形式，支持整数或浮点数
- `scale` 作为结果像素值的除数，默认为卷积核之和
- `offset` 在除完以后作为偏移量，默认为 0

<br>

**BLUR**
```py
filterargs = (5, 5), 16, 0, (
    1, 1, 1, 1, 1,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 1, 1,
)
```
**CONTOUR**
```py
filterargs = (3, 3), 1, 255, (
    -1, -1, -1,
    -1,  8, -1,
    -1, -1, -1,
)
```
**DETAIL**
```py
filterargs = (3, 3), 6, 0, (
    0,  -1,  0,
    -1, 10, -1,
    0,  -1,  0,
)
```
**EDGE_ENHANCE**
```py
filterargs = (3, 3), 2, 0, (
    -1, -1, -1,
    -1, 10, -1,
    -1, -1, -1,
)
```
**EDGE_ENHANCE_MORE**
```py
filterargs = (3, 3), 1, 0, (
    -1, -1, -1,
    -1,  9, -1,
    -1, -1, -1,
)
```
**EMBOSS**
```py
filterargs = (3, 3), 1, 128, (
    -1, 0, 0,
    0,  1, 0,
    0,  0, 0,
)
```
**FIND_EDGES**
```py
filterargs = (3, 3), 1, 0, (
    -1, -1, -1,
    -1,  8, -1,
    -1, -1, -1,
)
```
**SHARPEN**
```py
filterargs = (3, 3), 16, 0, (
    -2, -2, -2,
    -2, 32, -2,
    -2, -2, -2,
)
```
**SMOOTH**
```py
filterargs = (3, 3), 13, 0, (
    1, 1, 1,
    1, 5, 1,
    1, 1, 1,
)
```
**SMOOTH_MORE**
```py
filterargs = (5, 5), 100, 0, (
    1, 1,  1, 1, 1,
    1, 5,  5, 5, 1,
    1, 5, 44, 5, 1,
    1, 5,  5, 5, 1,
    1, 1,  1, 1, 1,
)
```






<br>

### ImageEnhance
```py
class _Enhance:
    def enhance(self, factor):
        """
        Returns an enhanced image.

        :param factor: A floating point value controlling the enhancement.
                       Factor 1.0 always returns a copy of the original image,
                       lower factors mean less color (brightness, contrast,
                       etc), and higher values more. There are no restrictions
                       on this value.
        :rtype: :py:class:`~PIL.Image.Image`
        """
        return Image.blend(self.degenerate, self.image, factor)


class Color(_Enhance):
    def __init__(self, image):
        self.image = image
        self.intermediate_mode = "L"
        if "A" in image.getbands():
            self.intermediate_mode = "LA"

        self.degenerate = image.convert(self.intermediate_mode).convert(image.mode)


class Contrast(_Enhance):
    def __init__(self, image):
        self.image = image
        mean = int(ImageStat.Stat(image.convert("L")).mean[0] + 0.5)
        self.degenerate = Image.new("L", image.size, mean).convert(image.mode)

        if "A" in image.getbands():
            self.degenerate.putalpha(image.getchannel("A"))


class Brightness(_Enhance):
    def __init__(self, image):
        self.image = image
        self.degenerate = Image.new(image.mode, image.size, 0)

        if "A" in image.getbands():
            self.degenerate.putalpha(image.getchannel("A"))


class Sharpness(_Enhance):
    def __init__(self, image):
        self.image = image
        self.degenerate = image.filter(ImageFilter.SMOOTH)

        if "A" in image.getbands():
            self.degenerate.putalpha(image.getchannel("A"))
```

```py
enh_col = ImageEnhance.Color(image)
im = enh_col.enhance(color)

enh_con = ImageEnhance.Contrast(image)
im = enh_con.enhance(contrast)

enh_bri = ImageEnhance.Brightness(image)
im = enh_bri.enhance(brightness)

enh_sha = ImageEnhance.Sharpness(image)
im = enh_sha.enhance(sharpness)
```







<br>

### ImageGrab
- `ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=False, xdisplay=None)` 截取屏幕区域
    - `bbox` 边界框，形式为 (左, 上, 右, 下)，默认为整个屏幕





