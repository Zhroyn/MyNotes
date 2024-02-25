
- [环境管理](#环境管理)
    - [创建环境](#创建环境)
    - [移除环境](#移除环境)
    - [列出环境](#列出环境)
    - [导出环境](#导出环境)
    - [激活环境](#激活环境)
    - [重命名环境](#重命名环境)
- [包管理](#包管理)
    - [安装包](#安装包)
    - [删除包](#删除包)
    - [更新包](#更新包)
    - [列出包](#列出包)
    - [搜索包](#搜索包)
    - [指定版本与降级](#指定版本与降级)
    - [版本回退](#版本回退)
    - [清理空间](#清理空间)
- [通道管理](#通道管理)
    - [显示配置](#显示配置)
    - [添加与删除通道](#添加与删除通道)
        - [清华源](#清华源)
        - [中科大源](#中科大源)
    - [初始化配置](#初始化配置)
    - [其他配置](#其他配置)






## 环境管理
### 创建环境
- `conda create -n/--name ENVIRNMENT [package_spec...]` 创建一个新环境，可以指定新环境中要安装的包
- `conda create -n/--name ENVIRNMENT --clone ENV` 通过复制环境来创建环境
- `conda create -n/--name ENVIRNMENT --file FILE` 通过导入配置文件来创建环境，编码需为 UTF-8
<br>

- `conda env create -f FILE` 通过 yaml 文件来导入环境

### 移除环境
- `conda env remove -n/--name ENV` 删除指定名称的环境

### 列出环境
- `conda info -e/--envs` 列出所有环境
- `conda env list` 列出所有环境

### 导出环境

- `conda list --explicit > FILE` 列出所有安装包的 URL，可用于创建环境
- `conda list -e/--export > FILE` 导出安装包的名称与版本，可用于创建环境
<br>

- `conda env export > FILE` 导出环境的所有配置至 yaml 文件

### 激活环境
- `conda activate ENV` 激活环境
- `conda deactivate` 退回 base 环境，若已在 base 环境，则退出 conda 环境

### 重命名环境
目前没找到重命名指令，若要重命名，可用下列指令：
1. `conda create -n/--name NEWENV --clone OLDENV` 先复制环境
2. `conda env remove -n/--name OLDENV` 再删除原环境







<br>

## 包管理
### 安装包
- `conda install [-n ENV] package_spec...` 安装指定的包
- `conda install package_spec -c/--channel CHANNEL` 从指定通道安装包
- `conda install package_spec -c CHANNEL --override-channels` 只从指定通道安装包，忽略其他配置的通道
- `conda install package_spec -c conda-forge -c bioconda` 从多个指定通道安装包，左边优先级更高
- `conda install --use-local PATH` 安装本地包

### 删除包
- `conda uninstall [-n ENV] package_spec...` 删除指定的包，同时删除所有依赖指定包的包
- `conda uninstall package_spec... --force` 只删除指定的包

### 更新包
- `conda update [-n ENV] package_spec...` 更新指定的包
- `conda update [-n ENV] --all/--update-all` 更新所有包

### 列出包
- `conda list [-n ENV]` 列出所有包
- `conda list REGEX` 列出匹配正则表达式的包

### 搜索包
- `conda search REGEX` 搜索所有通道中匹配正则表达式的包

### 指定版本与降级
- `numpy=1.11` 意指 `1.11.0`, `1.11.1`, `1.11.2`, `1.11.18` 等版本
- `numpy==1.11` 意指 `1.11.0`
- `numpy>=1.11` 意指 `1.11.0` 或更高的版本
- `numpy=1.11.1|1.11.3` 意指 `1.11.1` 和 `1.11.3`
- `numpy>=1.8,<2` 意指 `1.8` 和 `1.9`，不包括 `2.0`
<br>

- `conda install package_spec=...` 将包降级到指定版本

### 版本回退
- `conda list -r/--revisions` 列出当前环境所有修订历史
- `conda install --revision REVISION` 回退到指定修订版本

### 清理空间
- `conda clean -p/--packages` 清除未使用的包
- `conda clean -t/--tarballs` 清除压缩包
- `conda clean -a/--all` 清除索引缓存、锁定文件、未使用的包、压缩包和日志







<br>

## 通道管理
### 显示配置
- `conda config --show` 显示所有配置
- `conda config --show channels` 只显示通道配置

### 添加与删除通道
- `conda config --add channels CHANNEL` 将添加的通道放在 channels 的最上方，优先级最高
- `conda config --append channels CHANNEL` 将添加的通道放在 channels 的最下方，优先级最低
- `conda config --remove channels CHANNEL` 删除通道列表中指定的通道，若不存在会报错

#### 清华源
```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls True
```
#### 中科大源
```shell
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
conda config --set show_channel_urls True
```

### 初始化配置
- `conda config --remove-key channels` 移除自定义的通道列表

### 其他配置
- `conda config --set always_yes True` 当要求继续时，总是选择 yes
- `conda config --set show_channel_urls True` 在下载时和使用 `conda list` 时显示 url
- `conda config --set channel_priority strict` 将通道优先级设置为 strict
    - `strict` 不考虑低优先级的通道
    - `flexible` 默认行为，先按通道排序，再按版本号排序，再按构建号排序
    - `disabled` 先按版本号排序，再按通道排序，再按构建号排序
- `conda config --set channel_alias https://conda.anaconda.org` 在非 url 通道前加上的地址

