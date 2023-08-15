
- [属性](#属性)
- [更改与查看路径](#更改与查看路径)
- [列出文件](#列出文件)
- [创建与删除文件夹](#创建与删除文件夹)
- [删除与重命名文件](#删除与重命名文件)
- [创建链接](#创建链接)
- [执行命令](#执行命令)
- [切割与合并路径](#切割与合并路径)
- [判断文件与文件夹属性](#判断文件与文件夹属性)
- [查看与修改文件权限](#查看与修改文件权限)





### 属性
- `os.name` 操作系统的类型，Windows 为 nt，Linux 为 posix
- `os.environ` 环境变量，返回一个字典
- `os.sep` 当前平台的路径分隔符，Windows 为 `\\`，Linux 为 `/`
- `os.extsep` 扩展名分隔符
- `os.pathsep` 当前平台环境变量不同路径之间的分隔符，Windows 为 `;`，Linux 为 `:`
- `os.linesep` 当前平台的行分隔符，Windows 为 `\r\n`，Linux 为 `\n`


<br>

### 更改与查看路径
- `os.chdir(path)` 改变当前路径
- `os.getcwd()` 得到当前路径


<br>

### 列出文件
- `os.listdir(path=None)` 列出指定路径下的所有文件，默认为当前路径
- `os.walk(top, topdown=True, onerror=None, followlinks=False)` 返回一个文件树生成器，里面的元素的形式为 (当前路径, 当前路径下的文件夹名列表, 当前路径下的文件名列表)


<br>

### 创建与删除文件夹
- `os.mkdir(path, *, dir_fd=None)` 创建文件夹，若已存在会报错
- `os.makedirs(name)` 创建文件夹，会连带创建所有的中间文件夹，若已存在会报错
- `os.rmdir(path, *, dir_fd=None)` 删除文件夹，若文件夹内不为空会报错
- `os.removedirs(name)` 删除文件夹，并删除所有的中间文件夹，除非中间文件夹内有其他文件，若底层文件夹不为空会报错


<br>

### 删除与重命名文件
- `os.remove(path, *, dir_fd=None)` 删除文件，若不存在会报错
- `os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)` 重命名文件或文件夹，若目标位置不存在会报错，在 Windows 下若目标路径已存在会报错
- `os.renames(old, new)` 重命名文件或文件夹，若目标位置不存在会创建路径，在 Windows 下若目标路径已存在会报错
- `os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)` 重命名文件或文件夹，若目标位置不存在会报错，若目标路径已存在会覆盖



<br>

### 创建链接
- `os.link(src, dst)` 创建一个硬链接，目标只能是文件
- `os.symlink(src, dst, target_is_directory=False)` 创建一个符号链接



<br>

### 执行命令
- `os.system(command)` 在一个子进程中执行命令并返回状态码，父进程会阻塞
- `os.popen(cmd, mode='r', buffering=-1)` 创建一个管道并执行命令
  - `pipe = os.popen("ls"); result = pipe.read()`



<br>

### 切割与合并路径
- `os.path.abspath(path)` 返回绝对路径
- `os.path.basename(path)` 返回最后一个路径分割符之后的内容
- `os.path.dirname(path)` 返回最后一个路径分割符之前的内容
- `os.path.split(p)` 返回最后一个路径分割符前后的内容，形式为 (head, tail)
- `os.path.splitext(p)` 返回扩展名分割符前后的内容，形式为 (root, ext)，扩展名会包含 `.`
- `os.path.join(path, *paths)` 将多个路径连接在一起，若最后一项为空，结果末尾会加上分隔符



<br>

### 判断文件与文件夹属性
- `os.path.exists(path)` 判断是否存在
- `os.path.isabs(s)` 判断是否是绝对路径
- `os.path.isdir(s)` 判断是否是文件夹
- `os.path.isfile(path)` 判断是否是文件
- `os.path.islink(path)` 判断是否是符号链接



<br>

### 查看与修改文件权限
- `os.access(path, mode)` 查看是否存在或查看权限
  - `os.F_OK` 存在
  - `os.R_OK` 可读
  - `os.W_OK` 可写
  - `os.X_OK` 可执行
- `os.chmod(path, mode)` 修改文件权限
  - `stat.S_IREAD` 所有者读权限
  - `stat.S_IWRITE` 所有者写权限
  - `stat.S_IEXEC` 所有者执行权限
  - `stat.S_IRUSR` 所有者读权限
  - `stat.S_IWUSR` 所有者写权限
  - `stat.S_IXUSR` 所有者执行权限
  - `stat.S_IRWXU` 所有者全部权限
  - `stat.S_IRGRP` 组用户读权限
  - `stat.S_IWGRP` 组用户写权限
  - `stat.S_IXGRP` 组用户执行权限
  - `stat.S_IRWXG` 组用户全部权限
  - `stat.S_IROTH` 其他用户读权限
  - `stat.S_IWOTH` 其他用户写权限
  - `stat.S_IXOTH` 其他用户执行权限
  - `stat.S_IRWXO` 其他用户全部权限

