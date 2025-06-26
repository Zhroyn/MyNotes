# json 笔记

## 序列化

json 模块提供了两个方法用于序列化 Python 对象：

- `json.dumps(obj, *, **kw)`：将 Python 对象序列化为 JSON 格式的字符串
- `json.dump(obj, fp, *, **kw)`：将 Python 对象序列化为 JSON 格式的字符串，并将其写入文件对象 `fp`

每个方法都有一些可选参数，用于控制序列化的行为：

- `skipkeys` 若为 `True`，则字典中的键不是基本类型时会抛出 `TypeError`，默认为 `False`
- `ensure_ascii` 若为 `True`，则所有非 ASCII 字符会被转义为 `\uXXXX` 形式，若为 `False` 则不转义，默认为 `True`
- `check_circular` 若为 `True`，则检查循环引用，默认为 `True`
- `allow_nan` 若为 `True`，则允许 `nan`、`inf`、`-inf`，默认为 `True`
- `indent` 缩进空格数，若为 `None` 则不缩进，默认为 `None`
- `separators` 分隔符，为一个元组，包含两个字符串，第一个字符串用于分隔键值对，第二个字符串用于分隔元素，默认为 `(', ', ': ')`
- `default` 用于处理不支持的类型，可以是一个函数或类，会被调用并返回一个可序列化的对象
- `sort_keys` 若为 `True`，则输出的 JSON 字符串中的键会按字典顺序排序，默认为 `False`


## 反序列化

json 模块提供了两个方法用于反序列化 JSON 字符串：

- `json.loads(s, *, **kw)`：将 JSON 格式的字符串反序列化为 Python 对象
- `json.load(fp, *, **kw)`：将文件对象 `fp` 中的 JSON 字符串反序列化为 Python 对象
