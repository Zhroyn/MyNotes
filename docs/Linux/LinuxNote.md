
- [文件管理](#文件管理)
  - [ls, pwd](#ls-pwd)
  - [mv, cp, rm](#mv-cp-rm)
  - [ln, touch, mkdir](#ln-touch-mkdir)
  - [chmod, chown, chgrp](#chmod-chown-chgrp)
  - [which, find, locate](#which-find-locate)
- [输出](#输出)
  - [echo, cat, tee](#echo-cat-tee)
  - [cut, head, tail](#cut-head-tail)
  - [wc](#wc)
- [网络远程](#网络远程)
  - [wget, curl](#wget-curl)
  - [hostname, ip, ifconfig](#hostname-ip-ifconfig)
  - [ssh, ssh-keygen](#ssh-ssh-keygen)
  - [scp, rsync](#scp-rsync)
- [硬件管理](#硬件管理)
  - [df, du](#df-du)
- [数据处理](#数据处理)
  - [sort](#sort)
  - [uniq](#uniq)
  - [grep](#grep)
  - [sed](#sed)
  - [awk](#awk)
- [终端复用器](#终端复用器)
  - [tmux](#tmux)
- [进程控制](#进程控制)
  - [jobs, ps, pgrep](#jobs-ps-pgrep)
  - [kill, pkill](#kill-pkill)
  - [nohup, bg, fg](#nohup-bg-fg)
- [其他](#其他)
  - [date](#date)
  - [who](#who)
  - [xargs](#xargs)
  - [tar](#tar)
  - [less](#less)
- [Packages](#packages)
  - [apt](#apt)
- [配置](#配置)
  - [镜像源](#镜像源)







## 文件管理
### ls, pwd
**ls**
```shell
ls    # 列出当前路径下的所有文件和目录
```
- `-1` 每行一个文件
- `-a` 列出所有文件，包括隐藏文件
- `-R` 递归列出每个子目录下的所有文件和目录
- `-F` 给列出的目录末尾加上 `/`
<br>

- `-t` 以时间排序，新的在最前面
- `-S` 以大小排序，大的在最前面
- `-X` 以扩展名排序
- `-r` 逆序列出
<br>

- `-l` 使用长列表模式

长列表格式从左到右依次为：文件类型和权限、硬链接计数、文件所有者、文件所属组、文件大小、修改时间、名称。

文件类型和权限共十个字符，第一个为文件类型字符，常见的文件类型包括：
- `-` 普通文件
- `d` 目录
- `l` 符号链接 (软链接)
- `c` 字符设备文件
- `b` 块设备文件
- `p` 命名管道 (FIFO)
- `s` 套接字 (Socket)

接下来九个权限字符分三组，分别表示文件所有者的权限、文件所属组的权限和其他用户的权限，`r` 表示读权限，`w` 表示写权限，`x` 表示执行权限

---
**pwd**
```shell
pwd   # 显示当前目录
```
- 相当于执行 `echo $PWD`

<br>

### mv, cp, rm
这三个命令都有以下选项：
- `-f` 强制覆盖/删除，不会提示
- `-i` 在覆盖/删除前提示
- `-v` 显示所作操作

**mv**
```shell
# 重命名文件或目录
mv path/to/source path/to/target

# 移动文件或目录到另一个目录
mv path/to/source path/to/existing_directory
mv path/to/source1 path/to/source2 ... path/to/existing_directory
```
- 若目标文件是只读的，会提示用户是否覆盖，否则会自动覆盖
- `-n` 不会覆盖原有文件

---
**cp**
```shell
# 将文件复制到目标路径
cp path/to/source_file.ext path/to/target_file.ext

# 将文件复制到目标目录，文件名不变
cp path/to/source_file.ext path/to/target_parent_directory

# 递归复制源目录到目标目录，若目标目录已存在，则将源目录复制到其内
cp -r/-R path/to/source_directory path/to/target_directory

# 复制多个文件到目标目录
cp -t path/to/destination_directory path/to/file1 path/to/file2 ...
```
- 若目标文件是只读的，会提示用户是否覆盖，否则会自动覆盖
- `-n` 不会覆盖原有文件
- `-r/R` 递归地复制目录
- `-t DIRECTORY` 将所有文件复制到目标目录
- `-l` 创建硬链接而不是复制文件
- `-L` 在复制前跟随符号链接

---
**rm**
```shell
# 删除指定文件
rm path/to/file1 path/to/file2 ...

# 递归删除指定文件或目录
rm -r path/to/file_or_directory1 path/to/file_or_directory2 ...
```
- 默认无法删除目录
- `-r/R` 递归地删除目录

<br>

### ln, touch, mkdir
**ln**
```shell
# 创建一个硬链接
ln /path/to/file path/to/hardlink

# 创建一个符号链接
ln -s /path/to/file_or_directory path/to/symlink
```
- `-f` 若创建的链接的路径已存在，则覆盖目标文件

---
**touch**
```shell
# 创建空文件，或更新时间戳为当前时间
touch path/to/file1 path/to/file2 ...
# Set the times on a file to a specific date and time:
touch -t YYYYMMDDHHMM.SS path/to/file
# Set the time on a file to one hour in the past:
touch -d "-1 hour" path/to/file
# Use the times from a file to set the times on a second file:
touch -r path/to/file1 path/to/file2
```
- `-c` 不创建文件
- `-a` 只改变访问时间
- `-m` 只改变修改时间
- `-r FILE` 使用指定文件的时间戳，而不是当前时间
<br>

- `-d STRING` 使用指定的日期时间
  - `-d "2023-09-04T12:30:30Z"`
  - `-d "2023-09-04 12:30:30"`
  - `-d "2023-9-4 12"` 必须包含年月日时，分和秒默认为零
  - `-d "yesterday"` 昨天的当前时间
  - `-d "1 hour ago"/"-1 hour"` 一个小时前的当前时间
  - `-d "3 day"/"+3 day"` 三天后的当前时间
  - `-d "next month"/"+1 month"` 下个月的第一天的当前时间
<br>

- `-t STAMP` 使用自定义的时间戳，格式必须为 `[[CC]YY]MMDDhhmm[.ss]`
  - `-t 202309041230.30`
  - `-t $(date "+%Y%m%d%H%M.%S")`

---
**mkdir**
```shell
# 创建目录
mkdir path/to/directory1 path/to/directory2 ...
```
- `-p` 递归地创建目录
- `-m` 指定权限，若不使用该选项则默认为 `rwxr-xr-x`

<br>

### chmod, chown, chgrp
**chmod**
```shell
# 改变文件或目录的权限
chmod mode path/to/file_or_directory

# 为所有者添加所有权限，移除其他人的读权限
chmod u+rwx,o-r path/to/file_or_directory
```
- 符号模式使用 `u` 表示用户，`g` 表示组，`o` 表示其他用户，`a` 表示所有用户，在不指定时默认为所有用户
- 符号模式使用 `+` 表示添加权限，`-` 表示移除权限
<br>

- `-R` 递归地修改权限
- `--reference=RFILE` 使用指定文件的权限

---
**chown, chgrp**
```shell
# 改变文件或目录的所有者
chown user path/to/file_or_directory

# 改变文件或目录的所有者和所属组
chown user:group path/to/file_or_directory

# 改变文件或目录的所属组
chgrp group path/to/file_or_directory
```
- `-R` 递归地改变所有者或所属组
- `-h` 改变符号链接的所有者和所属组，而不是其指向的文件或目录
- `--reference=RFILE` 使用指定文件的所有者和所属组

<br>

### which, find, locate
**which**
```shell
# 搜索环境变量，显示可执行文件的位置
which executable

# 显示所有的可执行文件的位置
which -a executable
```
---
**find**
```shell
# 查找当前目录及其子目录下的所有文件和目录
find

# 查找所有扩展名为 .py 的文件，除了 site-packages 目录
find root_path -name '*.py' -not -path '*/site-packages/*'

# 删除所有扩展名为 .tmp 的文件
find root_path -name '*.tmp' -exec rm -f {} \;
```
- `-name PATTERN` 根据文件名进行匹配搜索
- `-iname PATTERN` 根据文件名进行匹配搜索，不区分大小写
- `-path PATTERN` 根据路径进行匹配搜索
- `-ipath PATTERN` 根据路径进行匹配搜索，不区分大小写
<br>

- `-type [bcdpflsD]` 根据文件类型进行匹配搜索，`f` 表示普通文件，`d` 表示目录，`i` 表示普符号链接
- `-xtype [bcdpfls]` 根据文件类型进行匹配搜索，但是考虑符号链接指向的目标文件的类型
- `-maxdepth n` 限制搜索的最大深度
- `-mindepth n` 限制搜索的最小深度
- `-size [sign]n[bcwkMG]` 根据文件大小搜索
  - `+` 表示大于，`-` 表示小于，不带符号表示等于
  - `c` 表示字节，`k` 表示千字节，`M` 表示兆字节，`G` 表示千兆字节
<br>

- `-atime n` 根据文件的最后访问时间搜索，单位为日
- `-ctime n` 根据文件的最后更改时间搜索，单位为日
- `-mtime n` 根据文件的最后修改时间搜索，单位为日
- `-amin n` 根据文件的最后访问时间搜索，单位为分钟
- `-cmin n` 根据文件的最后更改时间搜索，单位为分钟
- `-mmin n` 根据文件的最后修改时间搜索，单位为分钟
  - `+` 表示在那之前，`-` 表示在那之后，不带符号表示刚好在那时
<br>

- `!` 和 `-not` 表示非操作，`-a` 和 `-and` 表示与操作，`-o` 和 `-or` 表示或操作
- 可用 `\(` 和 `\)` 包裹条件来明确优先级

---
**locate**
```shell
# 在数据库中进行模糊匹配
locate PATTERN

# 更新数据库
sudo updatedb
```
- `--localpaths='dir1 dir2...'` 指定 updatedb 的更新路径








<br>

## 输出
### echo, cat, tee
**echo**
```shell
-e     enable interpretation of backslash escapes
-E     disable interpretation of backslash escapes (default)
-n     do not output the trailing newline

# Print a message with environment variables, must with double quotation marks
echo "My path is $PATH"
# Append a message to the file
echo "Hello World" >> file.txt
# Assign a value to a variable
i=$(echo "123d56d89")
# 
```
**cat**
```shell
# Print and concatenate files
# With no FILE, or when FILE is -, read standard input

# Print the contents of a file to the standard output:
cat path/to/file
# Concatenate several files into an output file:
cat path/to/file1 path/to/file2 > path/to/output_file
# Append several files into an output file:
cat path/to/file1 path/to/file2 >> path/to/output_file
# Number all output lines:
cat -n path/to/file
```
**tee**
```shell
# Copy standard input to each FILE, and also to standard output

# Copy standard input to each file, and also to standard output:
echo "example" | tee path/to/file
# Append to the given files, do not overwrite:
echo "example" | tee -a path/to/file
# Print standard input to the terminal, and also pipe it into another program:
echo "example" | tee /dev/tty | xargs printf "[%s]"
```
### cut, head, tail
**cut**
```shell
# Print selected parts of lines from each FILE to standard output
# With no FILE, or when FILE is -, read standard input

-b, --bytes=LIST        #select only these bytes
-c, --characters=LIST   #select only these characters
-d, --delimiter=DELIM   #use DELIM instead of TAB for field delimiter
-f, --fields=LIST   #select only these fields;
                    #also print any line that contains no delimiter character,
                    #unless the -s option is specified

# Select the first, third to fifth, and seventh to end bytes from each line
command | cut -b 1,3-5,7-
# usefully when the size of a character exceeds a byte
command | cut -c 1,3-5,7-
# Select the first two fields from each line
command | cut -d : -f -2
```
**head**
```shell
# Print the first 10 lines of each FILE to standard output

# Output the first few lines of a file:
head -n/--lines count path/to/file
# Output everything but the last few lines of a file:
head -n/--lines -count path/to/file
# Output the first few bytes of a file:
head -c/--bytes count path/to/file
# Output everything but the last few bytes of a file:
head -c/--bytes -count path/to/file
```
**tail**
```shell
# Print the last 10 lines of each FILE to standard output

# Show last 'count' lines in file:
tail -n/--lines count path/to/file
# Print a file from a specific line number:
tail -n/--lines +count path/to/file
# Print a specific count of bytes from the end of a given file:
tail -c/--bytes count path/to/file
```
### wc
**wc**
```shell
# Print newline, word, and byte counts for each FILE
wc -l/--lines path/to/file
wc -w/--words path/to/file
wc -c/--bytes path/to/file
wc -m/--chars path/to/file
```







<br>

## 网络远程
### wget, curl
**wget**
```shell
# 下载链接内容并保存到当前目录，文件名为 foo
wget https://example.com/foo
```
- `-O/--output-document FILE` 指定保存的文件的名称
- `-P/--directory-prefix PREFIX` 指定保存到的目录，不可与 `-O` 一起使用
- `-i/--input-file FILE` 从指定文件中的链接下载内容
- `-c/--continue` 若保存位置已有部分下载的文件，则断点续传，否则重新下载
- `-r` 递归地下载链接中的所有文件
<br>

- `-b` 后台下载，若未指定则默认将进度输出到当前目录下的 wget-log 文件
- `-o/--output-file FILE` 将 log 输出到指定文件，若已存在则覆盖
- `-a/append-file FILE` 将 log 信息附加到指定文件
<br>

- `--limit-rate=RATE` 限制下载速度，`k` 为千字节每秒，`M` 为兆字节每秒
- `--user=USER` 提供验证用户名
- `--password=PASS` 提供验证密码

---
**curl**
```shell
# 下载链接内容并发送到标准输出
curl https://example.com
# 下载链接内容并保存到指定路径
curl url1 -o path/to/file1 url2 -o path/to/file2
# 下载链接内容并保存到当前目录，文件名为 URL 中的名称
curl url1 -O url2 -O
# 只显示响应头信息，而不下载内容
curl -I https://example.com

# 向 URL 发送一个 PUT 请求，请求添加了自定义的头部信息
curl --header 'X-My-Header: 123' --request PUT https://example.com
```
- curl 可以并行处理多个 url
- `-o/--output <file>` 保存文件到指定路径，而不是发送到标准输出
- `-O/--remote-name` 保存文件到当前目录，文件名为 URL 中的名称
- `-I/--head` 只显示响应头信息，而不下载内容
- `-L/--location` 跟随重定向
- `-#/--progress-bar` 不再显示传输详细信息，转而显示传输进度条
- `-C/--continue-at -` 恢复传输进度
- `--limit-rate <speed>` 限制传输速度
<br>

- `-x/--proxy [protocol://]host[:port]` 使用指定代理
- `-u/--user <user:password>` 服务器的用户名和密码
- `-U/--proxy-user <user:password>` 代理的用户名和密码
- `-k/--key <key>` 指定本地私钥路径
- `-E/--cert <certificate[:password]>` 指定客户端证书文件和密码
<br>

- `-d/--data <data>` 指定数据，用于向 URL 发送一个 POST 请求
- `-H/--header <header/@file>` 添加自定义的 HTTP 头部信息到请求中
- `-X/--request <method>` 指定 HTTP 请求方法，默认为 GET
- `-T/--upload-file <file>` 上传本地文件


<br>

### hostname, ip, ifconfig
**hostname**
```shell
# 显示主机名
hostname
# 显示主机名对应的 ip 地址，为本地回环地址
hostname -i/--ip-address
# 显示主机的所有网络接口的 ip 地址
hostname -I/--all-ip-address
```
---
**ip**
```shell
# 显示所有网络接口的信息
ip addr
# 只显示 eth0 接口的信息
ip addr show eth0

# 显示路由表
ip route
# 显示邻居 (APR) 表
ip neigh

# 启用/禁用网络接口
ip link set {{interface}} up/down
```
---
**ifconfig**
```shell
# 显示所有启用的网络接口的信息
ifconfig
# 只显示 lo 接口的信息
ifconfig lo
# 启用/禁用网络接口
ifconfig {{interface}} up/down
```


<br>

### ssh, ssh-keygen
**ssh**
```shell
# 连接到远程服务器
ssh username@remote_host
```
- `-i identity_file` 指定认证文件
- `-p port` 指定端口

---
**ssh-keygen**
```shell
# 交互式地生成密钥
ssh-keygen
```
- `-t dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa` 指定密钥类型，默认为 RSA
- `-C comment` 添加注释，通常使用邮箱


<br>

### scp, rsync
**scp**
```shell
# 将本地文件传输到远程服务器中
scp path/to/local_file remote_host:path/to/remote_file
# 将远程服务器中的文件传输到本地
scp remote_host:path/to/remote_file path/to/local_file
```
- `-r` 递归地拷贝文件
- `-i identity_file` 指定认证文件
- `-P port` 指定端口

---
**rsync**
```shell
# 传输文件
rsync path/to/source path/to/destination
```
- `--archive` 使用归档模式，会递归地复制目录、符号文件、权限、所有权和修改时间等，等效于 `-rlptgoD`
- `-r/--recursive` 递归地传输文件









<br>

## 硬件管理
### df, du
**df**
```shell
# 显示所有文件系统的磁盘空间使用情况
df
# 显示指定文件或目录所在的文件系统的磁盘空间使用情况
df path/to/file_or_directory
```
- `-h` 以更可读的形式显示
- `-T` 显示文件系统类型
- `-t TYPE` 显示指定类型的文件系统

---
**du**
```shell
# 递归地列出所有文件和目录的大小
du path/to/directory
# 列出所有的 jpg 文件及其总大小
du -ch */*.jpg
```
- `-h` 以更可读的形式显示
- `-b/--bytes` 以 B 为单位
- `-k` 以 KB 为单位
- `-m` 以 MB 为单位
- `-s/--summarize` 只显示单个目录的总结，等效于 `-d0`
- `-c/--total` 在最后显示列出文件的总大小
- `-d/--max-depth=N` 指定最大递归深度








<br>

## 数据处理
### sort
```shell
# Sort a file in ascending order
sort path/to/file
# Sort a file in descending order
sort -r/--reverse path/to/file
# Sort a file in case-insensitive way
sort -f/--ignore-case path/to/file
# Sort a file using numeric rather than alphabetic order
sort -n/--numeric-sort path/to/file
# Sort a file by the 3rd field of each line numerically, using ":" as a field separator
sort -t/--field-separator=: --key=3n path/to/file
# Sort a file preserving only unique lines
sort -u/--unique path/to/file
# Sort a file, printing the output to the specified output file (can be in-place)
sort -o/--output=path/to/file path/to/file
```
### uniq
```shell
# Display each line once:
sort file | uniq
# Display only unique lines:
sort file | uniq -u
# Display only duplicate lines:
sort file | uniq -d
# Display number of occurrences of each line along with that line:
sort file | uniq -c
# Display number of occurrences of each line, sorted by the most frequent:
sort file | uniq -c | sort -nr
```

### grep
**Anchoring**
- The caret `^` matchs the empty string at the beginning of a line
- The dollar sign `$` matchs the empty string at end of a line

**Character Classes and Bracket Expressions**
- Most meta-characters lose their special meaning inside bracket expressions
- A list starting wirh caret `^` matches any character not in the list
- To include a literal `]` place it first in the list
- To include a literal `^` place it anywhere but first
- To include a literal `-` place it last
```shell
[:alnum:], [:alpha:], [:digit:],
[:blank:], [:space:], [:punct:],
[:cntrl:], [:lower:], [:upper:],
# [0-9A-Za-z] is the same as [[:alnum:]]
# \w is the same as [[:alnum:]_]
# \W is the same as [^[:alnum:]_]
# \s is the same as [[:space:]]
# \S is the same as [^[:space:]]
```
**Repetition**
```shell
?      # The preceding item is optional and matched at most once.
*      # The preceding item will be matched zero or more times.
+      # The preceding item will be matched one or more times.
{n}    # The preceding item is matched exactly n times.
{n,}   # The preceding item is matched n or more times.
{,m}   # The preceding item is matched at most m times. This is a GNU extension.
{n,m}  # The preceding item is matched at least n but not more than m times.
```
**Alternation**
- Two regular expressions may be joined by the infix operator `|`

**Precedence**
- Repetition takes precedence over concatenation, which in turn takes precedence over alternation.
- A whole expression may be enclosed in parentheses to override these precedence rules and form a subexpression.

**Back-references and Subexpressions**
- The back-reference `\n`(0-9) matches the substring previously matched by the `n'th` parenthesized subexpression of the regular expression

**Basic vs Extended Regular Expressions**
- In basic regular expressions, `?, +, {, |, (, )` lose their special meaning
- In extended expressions, `\?, \+, \{, \|, \(, \)` lose their special meaning

**Commands**
```shell
# When FILE is '-', read standard input.  With no FILE, read '.'

# Search for a pattern within a file(default is STDIN):
grep "search_pattern" path/to/file
# Search for a pattern in all files recursively in a directory:
grep -r/--recursive "search_pattern" path/to/directory

-E, --extended-regexp     #PATTERNS are extended regular expressions
-G, --basic-regexp        #PATTERNS are basic regular expressions
-P, --perl-regexp         #PATTERNS are Perl regular expressions
-F, --fixed-strings       #PATTERNS are strings
-f, --file=FILE           #take PATTERNS from FILE
-e, --regexp=PATTERNS     #use PATTERNS for matching

-i, --ignore-case         #ignore case distinctions in patterns and data
-w, --word-regexp         #match only whole words
-x, --line-regexp         #match only whole lines
-v, --invert-match        #select non-matching lines

-n, --line-number         #print line number with output lines
-H, --with-filename       #print file name with output lines
-o, --only-matching       #show only nonempty parts of lines that match
-B, --before-context=NUM  #print NUM lines of leading context
-A, --after-context=NUM   #print NUM lines of trailing context
-C, --context=NUM         #print NUM lines of output context
```


### sed
- If no addresses are given, the command is performed on all lines.
- `NUM` matchs the `NUM'th` line
- `$` matches the last line of input
- `FIRST~STEP` matches every `STEP'th` line starting with line `FIRST`, such as `0~2` for even-numbered lines
- `/REGEXP/` will select any line which matches the regular expression. If `REGEXP` itself includes any '/' characters, each must be escaped by a backslash
- `\%REGEXP%` (The `%` may be replaced by any other single character) This allows one to use a different delimiter than `/`. If `REGEXP` itself includes any delimiter characters, each must be escaped by a backslash
- `/REGEXP/I` `\%REGEXP%I`: The 'I' modifier causes the `REGEXP` to be matched in a case-insensitive manner
<br>

- An address range is specified with two addresses separated by a comma,which can be numeric, regular expressions, or a mix of both
- If the second address is a NUMBER less than (or equal to) the line matching the first address, then only the one line is matched
- If the first address is a `REGEXP`, then the address range will start with all the lines matched the `REGEXP`
- If the second address is a `REGEXP`, then checking for the ending match will start with the line following the line matched the first address, for example, `/[2,6]/,/[0-9]/` is equal to `2,3` and `6,7`
- `ADDR1,+N` matches `ADDR1` and the N lines following
- `ADDR1,~N` matches `ADDR1` and the following until the line whose input line number is a multiple of N
- If the `!` character follows an address or an address range(before the command letter), then only lines which do not match the addresses will be selected.

```shell
# If no -e, --expression, -f, or --file option is given, then the first
# non-option argument is taken as the sed script to interpret.

# If no input files are specified, or input files is '-',
# then the standard input is read.

# Commands
-e script       #add the script to the commands to be executed
-f script-file  #add the contents of script-file to the commands to be executed
-i, --in-place  #edit files in place
-E, -r, --regexp-extended   #use extended regular expressions in the script
-n, --quiet, --silent       #suppress automatic printing of pattern space

'a\TEXT'or'a TEXT'    # Append TEXT after a line
'i\TEXT'or'i TEXT'    # Insert TEXT before a line
'c\TEXT'or'c TEXT'    # Change lines with TEXT
'd'     # Delete the pattern space
'p'     # Print the pattern space
'w filename'  # Write the pattern space to FILENAME
```
```shell
's/REGEXP/replacement/flags'    #'/' can be replaced by other character

# Regexp
'.' means “any single character” except newline
'*' zero or more of the preceding match
'+' one or more of the preceding match
'[abc]' any one character of a, b, and c
'(RX1|RX2)' either something that matches RX1 or RX2
'^' the start of the line
'$' the end of the line

# Replacement
'\N(0-9)' refers to the portion of the match between the Nth '\(' and '\)'
'&' refers to the whole matched portion of the pattern space.
'\L' Turn the replacement to lowercase until a '\U' or '\E' is found,
'\l' Turn the next character to lowercase,
'\U' Turn the replacement to uppercase until a '\L' or '\E' is found,
'\u' Turn the next character to uppercase,
'\E' Stop case conversion started by '\L' or '\U'.

# Flags
'g' Apply the replacement to all matches to the REGEXP
'NUMBER' Only replace the NUMBERth match of the REGEXP each line
'NUMBERg' Ignore matches before the NUMBERth, and then replace all matches after
'w FILENAME' Write out the result to the named file
'I' Match REGEXP in a case-insensitive manner.
```

### awk
```shell
NR  #Number of Record
NF  #Number of Field
FS  #Field Separator
RS  #Record Separator
OFS #Output Field Separator
ORS #Output Record Separator

-v var=val  #Assign val to the variable var, before execution of the program

# Print the fifth field
awk '{print $5}' filename
# Print the last field of each line, using comma and space as field separators
awk -F '[, ]' '{print $NF}' filename
# Print the fifth line
awk '{if(NR==5) print}'
# Print different values based on conditions:
awk '{if ($1 == "foo") print "Exact match foo"; else print "Baz"}' filename
# Print the sum of each line
awk 'BEGIN{sum = 0} { for(i=1;i<=NF;i++) sum += $i; print sum; sum=0 }' filename
# Print the average of each column
awk '{ for(i=1;i<=NF;i++) a[i]+=$i } END{ for(j=1;j<=NF;j++) printf a[j]/NR"\t"; print"" }'
```








<br>

## 终端复用器
### tmux
- Sessions
  - `tmux` start a new session.
  - `tmux new -s NAME` start a new session with `NAME`.
  - `tmux ls` list the current sessions
  - `<C-b> d` detaches the current session
  - `tmux a/attach-session` attach the last session
  - `tmux a/attach-session -t NAME` attach the specified session
  - `tmux kill-session` kill the last or current attached session
  - `tmux kill-session -t NAME` kill the specfied session
  - `tmux kill-session -a` kill all sessions except the last or current attached one
- Windows
  - `<C-b> c` Creates a new window 
  - `<C-b> p` Goes to the previous window
  - `<C-b> n` Goes to the next window
  - `<C-b> N` Go to the N th window
  - `<C-b> ,` Rename the current window
  - `<C-b> w` List current sessions and windows, and move
- Panes
  - `<C-b> "` Split the current pane horizontally
  - `<C-b> %` Split the current pane vertically
  - `<C-b> <direction>` Move to the pane in the specified direction
  - `<C-b> z` Toggle zoom for the current pane
  - `<C-b> <space>` Cycle through pane arrangements.
  - `<C-b> [` Start scrollback. You can then press <space> to start a selection and <enter> to copy that selection.
  - `<C-d>` Close pane except only one left
  - `<C-b> x` Kill pane with prompt









<br>

## 进程控制
### jobs, ps, pgrep
**jobs**
```shell
# Display status of jobs.

-l  #lists process IDs in addition to the normal information
-p  #lists process IDs only
-n  #lists only processes that have changed status since the last notification
-r  #restrict output to running jobs
-s  #restrict output to stopped jobs
```
**ps**
```shell
# Display information about a selection of the active processes.
This version(wsl2) of ps accepts several kinds of options:
1   UNIX options, which may be grouped and must be preceded by a dash.
2   BSD options, which may be grouped and must not be used with a dash.
3   GNU long options, which are preceded by two dashes.

a   list all processes within a terminal, or list all processes when with 'x'
x   list all processes owned by you, or list all processes when with 'a'
u   Display user-oriented format.
l   Display BSD long format, conflict with 'u'.
w   Wide output. Use this option twice for unlimited width.
f   ASCII art process hierarchy (forest)

-A, -e  Select all processes
-a  Select all processes except session leaders

o, -o, --format format   Specify user-defined format.
--sort spec              Specify sorting order.
-f     Do full-format listing.
-F     Extra full format.
-l     Long format.

# List all running processes:
ps aux
# List all running processes including the full command string:
ps auxww
# List all processes of the current user in extra full format:
ps --user $(id -u) -F
# List all processes of the current user as a tree:
ps --user $(id -u) f
# Get the parent PID of a process:
ps -o ppid= -p pid
# Sort processes by memory consumption:
ps --sort size
```
**pgrep**
```shell
-f, --full              use full process name to match
-u, --euid <ID,...>     match by effective user IDs

# Return PIDs of any running processes with a matching command string:
pgrep process_name
# Search for processes including their command-line options:
pgrep --full "process_name parameter"
# Search for processes run by a specific user:
pgrep --euid root process_name
```

### kill, pkill
**kill**
- `SIGINT` (interrupt): `Ctrl + C`
- `SIGQUIT` (quit): `Ctrl + \`
- `SIGSTOP` (stop): `Ctrl + Z`

```shell
# Send a signal to a job.
# If neither SIGSPEC nor SIGNUM is present, then SIGTERM is assumed.
kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... 
kill -l [sigspec]

-s sig    #SIG is a signal name
-n sig    #SIG is a signal number
-l        #list the signal names
-L        #synonym for -l

# Terminate a program using the default SIGTERM (terminate) signal:
kill process_id
# Terminate a program using the SIGHUP (hang up) signal. Many daemons will reload instead of terminating::
kill -HUP process_id
# Terminate a program using the SIGINT (interrupt) signal:
kill -INT process_id
# Signal the operating system to immediately terminate a program (which gets no chance to capture the signal):
kill -KILL process_id
# Signal the operating system to pause a program:
kill -STOP process_id
# Signal the operating system to continue a program:
kill -CONT process_id
```
**pkill**
```shell
-SIGNAL, --signal SIGNAL
      Defines the signal to send to each matched process. 
      Either the numeric or the symbolic signal name can be used.
-f, --full      use full process name to match
-n, --newest
      Select only the newest(most recently started) of the matching processes.
-o, --oldest
      Select only the oldest(least recently started) of the matching processes.

# Kill all processes which match:
pkill "process_name"
# Kill all processes which match full command instead of just process name:
pkill -f "command_name"
# Force kill matching processes (can't be blocked):
pkill -9/KILL "process_name"
# Send SIGUSR1 signal to processes which match:
pkill -USR1 "process_name"
# Kill the main firefox process to close the browser:
pkill --oldest "firefox"
```
### nohup, bg, fg
**nohup**
```shell
# Run a process that can live beyond the terminal:
nohup command argument1 argument2 ...
# Launch nohup in background mode:
nohup command argument1 argument2 ... &
# Run a shell script that can live beyond the terminal:
nohup path/to/script.sh &
# Run a process and write the output to a specific file:
nohup command argument1 argument2 ... > path/to/output_file &
```
**bg**
```shell
## Resumes jobs that have been suspended, and run them in the background.

# Resume the most recently suspended job and run it in the background:
bg
# Resume a specific job and run it in the background:
bg %job_id
```
**fg**
```shell
## Run jobs in foreground.

# Bring most recently suspended or running background job to foreground:
fg
# Bring a specific job to foreground:
fg %job_id
```











<br>

## 其他
### date
```shell
# Print the current date and time

date                    # >>> Wed Nov  9 15:22:08 CST 2022
date +%c                # >>> Wed Nov  9 15:22:08 2022
date +%x\ -\ %X                 # >>> 11/09/22 - 15:22:08
date +'%Y/%m/%d - %H:%M:%S'     # >>> 2022/11/09 - 15:22:08

# %c   locale's date and time
# %x   locale's date representation
# %X   locale's time representation
# %y   last two digits of year
```

### who
```shell
# Print information about users who are currently logged in

# Display the username, line, and time of all currently logged-in sessions:
who
# Display information only for the current terminal session:
who am i
# Display all available information:
who -a
```
### xargs
```shell
# Delete all files with a .backup extension
# -print0 uses a null character to split file names, and -0 uses it as delimiter
find . -name '*.backup' -print0 | xargs -0 rm -v
```


### tar
```shell
# 创建一个归档文件，包含指定的文件
tar cf path/to/target.tar path/to/file1 path/to/file2 ...
# 创建一个用 gzip 压缩的归档文件，包含指定的文件
tar czf path/to/target.tar.gz path/to/file1 path/to/file2 ...
# 向一个归档文件追加指定文件，同时进行压缩
tar rzf target.tar.gz path/to/file1 path/to/file2 ...
# 提取一个归档文件到当前目录，输出提取的文件名
tar xvf path/to/source.tar[.gz|.bz2|.xz]
# 列出一个归档文件中的内容，最多为两层目录
tar tf path/to/source.tar[.gz|.bz2|.xz] --exclude "*/*/*"
# 删除一个归档文件中的指定文件
tar --delete -f source.tar path/to/file1 path/to/file2 ...
```
- `-f/--file ARCHIVE` 指定归档文件
- `-C/--directory DIR` 指定目标目录
<br>

- `-c/--create` 创建归档文件，会覆盖删除原有归档文件
- `-x/--extract` 提取归档文件
- `-t/--list` 列出归档文件内容
- `-r/--append` 向归档文件末尾追加文件
- `--delete` 从归档文件中删除文件
<br>

- `-z/--gzip` 使用 gzip 压缩
- `-j/--bzip2` 使用 bzip2 压缩
- `-J/--xz` 使用 xz 压缩
- `-a/--auto-conpress` 根据后缀名自动决定压缩程序
<br>

- `--exclude PATTERN` 不对符合 PATTERN 的文件执行操作
- `--wildcards PATTERN` 只对符合 PATTERN 的文件执行操作

### less
```shell
# Open a file:
less source_file
# Page down / up:
<Space> (down), b (up)
# Go to end / start of file:
G (end), g (start)
# Forward / Backward search for a string, allowing regexp:
/something, ?something
# go to next/previous match:
n, N
# Follow the output of the currently opened file:
F
# Open the current file in an editor:
v
```




## Packages
### apt
```shell
# Update the list of available packages and versions
sudo apt update
# Upgrade all installed packages to their newest available versions
sudo apt update

# Install a package, or update it to the latest available version
sudo apt install package
# Remove a package
sudo apt remove package

apt search package      #search package
apt show package        #show information
apt list                #list all packages
apt list --installed    #list installed packages
```







<br>

## 配置
### 镜像源
更新镜像源可进行以下命令：
```shell
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo vim /etc/apt/sources.list
sudo apt update
sudo apt upgrade
```

Ubuntu22.04 的源有：
```shell
# 清华源
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse

# 阿里源
deb http://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse

# 中科大源
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse

# 网易163源
deb http://mirrors.163.com/ubuntu/ jammy main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-backports main restricted universe multiverse
```