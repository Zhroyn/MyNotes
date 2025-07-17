
## pip 管理

- `pip -V/--version` 显示版本
- `python -m pip install --upgrade pip` 更新 pip
- `python -m pip uninstall pip` 卸载 pip

若不清楚命令的用法，可以使用以下命令查看帮助文档：

- `pip -h/--help` 显示帮助文档
- `pip help <command>` 显示指定命令的帮助文档





<br>

## 包管理

### 安装包

pip 最常见的使用方法是通过指定包名，从 PyPI 等包索引下载并安装包，其命令格式为：

```shell
pip install [options] <requirement specifier> [package-index-options] ...
```

其中，requirement specifier 可以是包名，也可以是包名和版本号的组合，示例如下：

- `project==1.3` 指定精确版本
- `project>=1.2, <2.0` 指定版本范围，整个说明符需用引号括起来
- `project~=1.3` 指定 1.3 版本及其向后兼容的最新版本
- `project[extra]` 指定额外的特性，为了避免与 shell 中的方括号冲突，也需要用引号括起来

常用选项有：

- `-U/--upgrade` 将指定包更新到最新版本
- `-i/--index-url <url>` 手动指定包索引地址，只能有一个生效
- `--extra-index-url <url>` 添加额外的包索引地址，可以添加多个
- `-f/--find-links <url>` 扫描某个本地或远程目录，查找 `.whl` 或 `.tar.gz`，可以是 URL 或本地目录
- `-e/--editable <path>` 安装包的可编辑版本，即直接安装源码

requirement specifier 还可以替换成 URL、文件路径等，类型判断顺序为：

1. 项目或压缩包 URL
2. 本地文件夹，需包含 `pyproject.toml` 或 `setup.py` 文件
3. 本地文件，需要是一个源分发或 wheel 包
4. 版本说明符

除此以外，还可以使用 `-r/--requirement <file>` 从文件中读取包名和版本号，不再指定具体的包名，例如 `pip install -r requirements.txt`。

#### requirements.txt 文件格式

`requirements.txt` 文件用于指定项目的依赖包，格式如下：

```plaintext
# 指定包索引
--index-url https://mirrors.zju.edu.cn/pypi/web/simple/
--extra-index-url https://download.pytorch.org/whl/cu118

# 指定包及版本
package1==1.0.0
package2>=2.0.0,<3.0.0
package3~=1.4

# 指定额外特性
package4[extra1,extra2]

# 从本地包安装
./packages/mylib-0.1.0.tar.gz

# 从 URL 安装
https://example.com/packages/mypkg-0.1.0.tar.gz

# 从远程 Git 仓库安装
git+https://github.com/user/repo.git
git+https://github.com/user/repo.git@abcdef1    # 指定分支或提交
git+https://github.com/user/repo.git@v1.0.0     # 指定标签
git+https://github.com/user/repo.git@main#subdirectory=libname  # 带子目录
git+https://github.com/user/repo.git@main --recursive           # 递归克隆子模块
git+https://github.com/user/repo.git#egg=packagename            # 命名包名

# 从本地 Git 仓库安装
git+file:///absolute/path/to/repo#egg=mylib
```

### 删除包

- `pip uninstall <package> ...` 删除指定的包
- `pip uninstall -y/--yes <package> ...` 不需要确认，直接删除

### 列出包

- `pip list -o/--outdated` 列出过时的包
- `pip list -u/--uptodate` 列出最新的包
- `pip show <package> ...` 显示指定包的信息

### 导出包

- `pip freeze > requirements.txt` 导出当前环境的所有包




<br>

## 配置管理

- `pip config list` 列出所有配置
- `pip config get command.option` 显示指定配置
- `pip config set command.option value` 设置配置
- `pip config unset command.option` 删除配置

在 Windows 中，配置文件一般位于 `~\AppData\Roaming\pip\pip.ini`，在 Linux 中，配置文件一般位于 `~/.config/pip/pip.conf`。

以下为一些常用配置：

```shell
# 设置浙大源
pip config set global.index-url https://mirrors.zju.edu.cn/pypi/web/simple/
pip config set global.trusted-host mirrors.zju.edu.cn

# 设置清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
pip config set global.trusted-host pypi.tuna.tsinghua.edu.cn

# 设置中科大源
pip config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple/
pip config set global.trusted-host pypi.mirrors.ustc.edu.cn

# 设置阿里源
pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/
pip config set global.trusted-host mirrors.aliyun.com

# 设置豆瓣源
pip config set global.index-url http://pypi.douban.com/simple/
pip config set global.trusted-host pypi.douban.com
```
