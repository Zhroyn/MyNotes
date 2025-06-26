# logging 笔记

`logging` 是 Python 的标准库模块，用于记录程序运行时的信息。它比简单的 `print()` 语句更强大，提供了灵活的日志记录系统。




<div style="margin-top: 60pt"></div>

## 日志级别

logging 模块定义了以下几个级别，按严重程度递增：

| 级别 | 数值 | 描述 |
|------|------|------|
| NOTSET | 0 | 未设置 |
| DEBUG | 10 | 详细的信息，通常只在诊断问题时使用 |
| INFO | 20 | 一般信息，证明程序按预期工作 |
| WARNING | 30 | 警告信息，程序仍能正常工作，但可能存在问题 |
| ERROR | 40 | 错误信息，程序某些功能无法正常执行 |
| CRITICAL | 50 | 严重错误，程序可能无法继续运行 |





<div style="margin-top: 60pt"></div>

## 基础用法
### 简单使用

```python
logging.debug('这是调试信息')
logging.info('这是一般信息')
logging.warning('这是警告信息')
logging.error('这是错误信息')
logging.critical('这是严重错误信息')
```

### 基本配置

`logging.basicConfig()` 用于配置日志系统的基本设置，其有以下常用参数：

- `level`: 设置日志级别，默认是 `WARNING`
- `format`: 设置日志输出格式，默认为 `%(levelname)s:%(name)s:%(message)s`
    - `%(name)s` Logger 名称
    - `%(levelno)s` 日志级别数值
    - `%(levelname)s` 日志级别名称
    - `%(pathname)s` 调用日志记录函数的文件路径
    - `%(filename)s` 文件名
    - `%(module)s` 模块名
    - `%(lineno)d` 行号
    - `%(funcName)s` 函数名
    - `%(created)f` 创建时间
    - `%(asctime)s` 格式化时间
    - `%(msecs)03d` 毫秒
    - `%(message)s` 日志消息
    - `%(thread)d` 线程 ID
    - `%(threadName)s` 线程名称
    - `%(process)d` 进程 ID
- `datefmt`: 设置时间格式
    - `%Y/%y/%m/%d` 年/两位数年/月/日
    - `%H/%M/%S` 小时/分钟/秒
    - `%z/%Z` 时区代码/时区名称
    - `%a/%A` 星期几缩写/全称
    - `%b/%B` 月份缩写/全称
    - `%p` AM/PM
    - `%j` 一年中的第几天
    - `%U` 一年中的第几周，以周日为一周的开始
    - `%W` 一年中的第几周，以周一为一周的开始
    - `%x` 本地化的日期，包含年月日
    - `%X` 本地化的时间，包含时分秒
    - `%c` 本地化的日期和时间
- `filename`: 指定日志输出到文件，若不指定则输出到控制台
- `filemode`: 设置文件模式，默认为 `'a'`（追加模式）
- `encoding`: 设置文件编码
- `force`: 强制覆盖已有的日志配置




<div style="margin-top: 60pt"></div>

## Logger 对象

当使用 `logging.info()` 等函数时，实际上是使用了一个默认的 root logger。可以通过 `logging.getLogger(name)` 创建独立的 logger 来更好地管理日志：

- `logging.getLogger()` 不输入参数时会返回 root logger
- 支持层级结构，可以输入 `parent.child` 形式的名称，子 Logger 可继承父 Logger 的配置

logger 的常见属性有：

- `name`: Logger 名称
- `level`: 当前日志级别
- `parent`: 父 Logger，若不存在则为根日志器
- `handlers`: 处理器列表
- `propagate`: 是否将日志消息传递给父 Logger，若为 True 可能会导致日志重复输出，默认为 True

常见方法有：

- `setLevel(level)`: 设置日志级别
- `addHandler(handler)`: 添加处理器
- `removeHandler(handler)`: 移除处理器
- `hasHandlers()`: 检查是否有处理器
- `isEnabledFor(level)`: 检查是否启用指定级别的日志记录






<div style="margin-top: 60pt"></div>

## Handler 对象

Handler 是日志记录的处理器，用于将日志消息发送到不同的目的地，如控制台、文件、网络等。每个 Handler 都可以有自己的日志级别和格式化器。

常见的 Handler 有：

- `logging.StreamHandler`: 输出到控制台
    - `stream`: 指定输出流，默认为 `sys.stderr`
- `logging.FileHandler`: 输出到文件
    - `filename`: 指定输出文件名
    - `mode`: 文件模式，默认为 `'a'`（追加模式）
    - `encoding`: 文件编码
- `logging.handlers.RotatingFileHandler`: 按大小轮转日志文件，当日志文件达到指定大小时，自动创建新文件并归档旧日志
    - `filename` `mode` `encoding`: 同 `FileHandler`
    - `maxBytes`: 单个文件的最大字节数，默认为 0
    - `backupCount`: 保留的备份文件数量，默认为 0
- `logging.handlers.TimedRotatingFileHandler`: 按时间轮转日志文件
    - `filename` `mode` `encoding` `backupCount`: 同 `RotatingFileHandler`
    - `when`: 轮转时间单位，支持 `S`（秒）、`M`（分钟）、`H`（小时）、`D`（天）、`midnight`（午夜）
    - `interval`: 轮转间隔，单位为 `when`
- `logging.handlers.SMTPHandler`: 通过 SMTP 发送日志邮件
    - `mailhost`: 邮件服务器地址，元组形式 `(host, port)`，例如 `("smtp.example.com", 587)`
    - `fromaddr`: 发件人地址，email 格式的字符串
    - `toaddrs`: 收件人地址列表，email 格式的字符串列表
    - `subject`: 邮件主题
    - `credentials`: 邮箱登录凭据，可以是元组形式 `(username, password)`
- `logging.handlers.HTTPHandler`: 通过 HTTP 发送日志
    - `host`: 服务器地址
    - `url`: 发送日志的 URL 路径
    - `method`: HTTP 方法，默认为 `GET`

Handler 的常见方法有：

- `setLevel(level)`: 设置 Handler 的日志级别
- `setFormatter(formatter)`: 设置 Handler 的格式化器，其中 Formatter 格式化器通过 `logging.Formatter` 创建，其参数为 `fmt` 和 `datefmt`，基本用法如前文 `basicConfig` 中所述

使用示例：

```python
import logging

# 创建 logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

# 创建 handler
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

# 设置级别
console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)

# 创建 formatter
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

# 设置 formatter
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 添加 handler
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 使用 logger
logger.debug('这是调试信息')
logger.info('这是信息')
logger.warning('这是警告')
logger.error('这是错误')
```





<div style="margin-top: 60pt"></div>

## 日志配置

### 通过字典配置

`logging.config.dictConfig()` 可以通过字典配置日志系统，一个典型的配置字典包括：

- `version`: 配置版本，必须为 1
- `disable_existing_loggers`: 是否禁用已存在的日志器，默认为 False
- `formatters`: 格式化器配置
- `handlers`: 处理器配置
- `loggers`: 日志器配置

```python
import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(name)s %(filename)s:%(lineno)d: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'detailed',
            'filename': 'app.log',
            'encoding': 'utf-8',
            'mode': 'w'
        }
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
logger.info('配置完成')
```

需要注意的是，`ext://` 是一种外部引用语法，格式为 `ext://<python_import_path>`，解析时会通过 `importlib` 动态导入模块并获取属性。

### 通过文件配置

`logging.config.fileConfig()` 可以通过配置文件来设置日志系统，支持 INI 格式的配置文件。

例如，先创建一个名为 `logging.conf` 的配置文件，内容如下：

```ini
[loggers]
keys=root,my_app

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_my_app]
level=DEBUG
handlers=consoleHandler,fileHandler
qualname=my_app
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('app.log',)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

然后使用配置文件：

```python
import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('my_app')
logger.debug('这是调试信息')
```
