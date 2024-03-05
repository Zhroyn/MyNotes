
### 读取图片
- `imread(uri, format=None, **kwargs)` 读取图像，返回一个 numpy 数组
    - `uri` 可以是文件路径、pathlib.Path、URL、文件对象
    - `format` 读取的格式，有 `'PNG'` `'JEPG'` `'TIFF'` `'ICO'` 等，会自动检测
