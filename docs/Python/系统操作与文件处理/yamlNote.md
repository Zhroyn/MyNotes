# yaml 笔记

## 序列化

- `yaml.dump(data, stream=None, Dumper=<class 'yaml.dumper.Dumper'>, **kwds)`：将 Python 对象序列化为 YAML 文档
    - `data` 要序列化的 Python 对象
    - `stream` 输出流，可以是文件对象，若为 `None` 则返回字符串
- `yaml.safe_dump(data, stream=None, **kwds)`：与 `yaml.dump` 类似，但仅支持标准的 YAML 标签，避免潜在的安全风险


## 反序列化

- `yaml.load(stream, Loader)`：将 YAML 文档反序列化为 Python 对象
- `yaml.safe_load(stream)`：与 `yaml.load` 类似，但仅支持标准的 YAML 标签，避免潜在的安全风险
