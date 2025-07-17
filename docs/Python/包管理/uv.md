## 安装 uv

### Windows
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Linux 和 macOS
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 通过 pip 安装
```shell
pip install uv
```

### 更新 uv
```shell
uv self update
```







<br>

## Python 版本管理

### 安装 Python 版本
- `uv python install 3.10` 安装 Python 3.10
- `uv python install 3.11 3.12` 安装多个 Python 版本
- `uv python install cpython@3.12` 安装特定实现的 Python

### 列出 Python 版本
- `uv python list` 列出所有已安装的 Python 版本
- `uv python list --all` 列出所有可用的 Python 版本

### 设置默认 Python 版本
- `uv python pin 3.11` 在当前目录设置 Python 版本（创建 `.python-version` 文件）
- `uv python pin --global 3.11` 设置全局默认 Python 版本

### 查找 Python 版本
- `uv python find` 查找当前使用的 Python 版本
- `uv python find 3.11` 查找特定版本的 Python 路径







<br>

## 虚拟环境管理

### 创建虚拟环境
- `uv venv` 在当前目录创建 `.venv` 虚拟环境，会使用当前环境的 Python 版本
- `uv venv ENV_NAME` 创建指定名称的虚拟环境，而不是 `.venv`
- `uv venv -p/--python 3.11` 使用指定 Python 版本创建虚拟环境
- `uv venv --system-site-packages` 创建可访问系统包的虚拟环境

### 激活虚拟环境

#### Windows (PowerShell)
```powershell
.venv\Scripts\Activate.ps1
```

#### Windows (cmd)
```cmd
.venv\Scripts\activate.bat
```

#### Linux/macOS
```shell
source .venv/bin/activate
```

### 退出虚拟环境
```shell
deactivate
```

### 删除虚拟环境
```shell
# 删除 .venv 目录
rm -rf .venv  # Linux/macOS
Remove-Item -Recurse -Force .venv  # Windows PowerShell
```

### pip 兼容接口

`uv pip` 提供了与 `pip` 兼容的命令行接口，支持大部分 `pip` 命令，例如：

- `uv pip install PACKAGES` 安装包到当前环境
- `uv pip uninstall PACKAGES` 卸载指定包
- `uv pip list` 列出已安装的包
- `uv pip show PACKAGES` 显示包详细信息
- `uv pip freeze` 输出已安装包的精确版本

此外，`uv pip` 还支持一些额外命令：

- `uv pip sync requirements.txt` 同步环境到指定状态，会卸载多余的包
- `uv pip tree` 显示包依赖树
- `uv pip check` 检查已安装包是否兼容
- `uv pip compile SRC_FILE... -o requirements.txt` 将 `pyproject.toml` 或 `setup.py` 等文件编译成 `requirements.txt`，用来确保依赖一致性






<br>

## 项目管理

### 创建项目
- `uv init` 在当前目录初始化项目
- `uv init PATH` 在指定路径创建新项目目录并初始化
    - `--package` 创建可发布的包项目
    - `--lib` 创建库项目
    - `--app` 创建应用项目
    - `--script` 创建脚本项目
    - `--python <PYTHON>` 指定 Python 版本

### 项目结构
```
project/
├── .python-version
├── README.md
├── main.py
├── pyproject.toml
├── uv.lock          # 锁文件
└── .venv/           # 虚拟环境
```

### 同步项目环境
- `uv sync` 同步环境，移除依赖中未列出的包，安装缺失的包，并更新锁文件
- `uv sync --frozen` 不更新锁文件，严格按照锁文件同步，即使 `pyproject.toml` 中添加了锁文件还没有的依赖也不会安装
- `uv sync --locked` 不更新锁文件，如果锁文件不是最新的会报错

### 锁定依赖
- `uv lock` 生成或更新 `uv.lock` 文件
- `uv lock --check` 检查锁文件是否是最新的，等价于 `--locked`
- `uv lock -U/--upgrade` 升级所有依赖到最新兼容版本
- `uv lock -P/--upgrade-package PACKAGE` 只升级指定包

### 添加依赖
- `uv add PACKAGES` 添加依赖到 `pyproject.toml` 中，会自动更新 `uv.lock` 并同步环境，包格式与 pip 基本一致
- `uv add PACKAGES --no-sync` 添加依赖但不同步环境 
- `uv add PACKAGES --frozen` 添加依赖但不更新锁文件
- `uv add PACKAGES --dev` 添加到开发依赖组，等价于 `--group dev`
- `uv add -r requirements.txt` 从 requirements.txt 添加依赖

### 移除依赖
- `uv remove PACKAGES` 从 `pyproject.toml` 移除指定包，会自动更新 `uv.lock` 并同步环境
- `uv remove PACKAGES --no-sync` 移除依赖但不同步环境
- `uv remove PACKAGES --frozen` 移除依赖但不更新锁文件
- `uv remove PACKAGES --dev` 从开发依赖组中移除，等价于 `--group dev`

### 运行命令
- `uv run COMMAND` 运行命令或脚本
    - 确保会在 Python 虚拟环境中运行
    - 当 `COMMAND` 是一个 Python 脚本或 URL 时，会当作 Python 脚本，用 Python 解释器运行，即 `uv run file.py` 等价于 `uv run python file.py`
    - 当在项目中时，会先同步项目环境
    - 当不在项目中时，会使用当前目录或父目录的虚拟环境，如果没有则用当前 Python 环境
    - 命令或脚本后的选项不会被当作 uv 的选项，可以使用 `--` 分隔 uv 选项和命令选项
- `uv run --with requests script.py` 临时添加依赖，会被放在独立的环境中，不影响项目环境
- `uv run -m/--module MODULE` 运行指定模块，等价于 `python -m MODULE`

### 构建项目
- `uv build [SRC]` 构建项目分发包，默认为当前目录
- `uv build --wheel` 只构建预编译包
- `uv build --sdist` 只构建源码包
- `uv build --wheel package.tar.gz` 从源码包构建预编译包

### 发布项目
- `uv publish [FILES]...` 发布到 PyPI，默认对象为 `dist/*`
    - `--index INDEX` 指定索引名，该索引必须有 `publish-url` 配置
    - `--publish-url URL` 指定发布 URL
    - `--check-url URL` 在 URL 检查是否已存在文件以避免重复上传
    - `-u/--username USERNAME` 指定用户名
    - `-p/--password PASSWORD` 指定密码
    - `-t/--token TOKEN` 指定令牌







<br>

## 脚本依赖管理

```python
#!/usr/bin/env python
# /// script
# dependencies = [
#     "requests",
#     "rich",
# ]
# ///

import requests
from rich.console import Console

console = Console()
console.print("Hello from uv!", style="bold blue")
```

- `uv run script.py` 自动解析并安装脚本依赖
- `uv add --script script.py requests` 添加依赖到脚本的内联元数据中







<br>

## 缓存管理

默认缓存目录为：

- Linux/macOS: `~/.cache/uv`
- Windows: `%LOCALAPPDATA%\uv\cache`

关于缓存的命令有：

- `uv cache dir` 显示缓存目录路径
- `uv cache prune` 清理缓存中未使用的文件
- `uv cache clean PACKAGES` 清理指定包的缓存





<br>

## 配置管理

### 全局配置
默认配置文件位置：

- Linux/macOS: `~/.config/uv/uv.toml`
- Windows: `%APPDATA%\uv\uv.toml`

### 项目配置
uv 会从 `pyproject.toml` 中的 `[tool.uv]` 表读取配置，示例如下：

```toml
[tool.uv]
index-url = "https://pypi.org/simple"
find-links = ["https://download.pytorch.org/whl/cpu"]
extra-index-url = ["https://download.pytorch.org/whl/cpu"]

[[tool.uv.index]]
name = "pypi"
url = "https://pypi.org/simple"
publish-url = "https://upload.pypi.org/legacy/"
```

uv 还会从 `uv.toml` 全局配置文件读取配置，其结构与 `pyproject.toml` 中的 `[tool.uv]` 部分相同，但省略了 `[tool.uv]` 前缀，示例如下：

```toml
[[index]]
url = "https://mirrors.zju.edu.cn/pypi/web/simple/"
default = true
```

### 常见选项与环境变量
- Python 选项
    - `-p/--python`     指定 Python 解释器，对应于 `UV_PYTHON` 环境变量
- 全局选项
    - `--directory` 指定工作目录，会在执行命令前切换到该目录
    - `--project` 指定项目目录，对应于 `UV_PROJECT` 环境变量
    - `--offline` 离线模式，对应于 `UV_OFFLINE` 环境变量
- 索引选项
    - `--index` 设置包索引，对应于 `UV_INDEX` 环境变量
    - `--default-index` 设置默认索引，对应于 `UV_DEFAULT_INDEX` 环境变量
    - `-i/--index-url` 设置包索引 URL，对应于 `UV_INDEX_URL` 环境变量
    - `--extra-index-url` 设置额外索引 URL，对应于 `UV_EXTRA_INDEX_URL` 环境变量
    - `-f/--find-links` 设置查找链接，对应于 `UV_FIND_LINKS` 环境变量
- 缓存选项
    - `--no-cache` 禁用缓存，对应于 `UV_NO_CACHE` 环境变量
    - `--cache-dir` 设置缓存目录，对应于 `UV_CACHE_DIR` 环境变量
