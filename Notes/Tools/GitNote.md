[toc]


## Common usage
#### Redo commit
- `git commit --amend`  If you want to redo that commit, make the additional changes you forgot, stage them, and commit again using the `--amend` option. Or you can stage nothing to change commit message only.

#### Unstage
- `git restore --staged <file>...`
- `git reset HEAD <file>...`

#### Discard changes
- `git restore <file>...`
- `git checkout -- <file>...`

#### Show Objects
- `git show <object>` show human-readable information without specific `sha1`
- `git cat-file -p <object>` show all references within the object
- `git ls-files -s <object>` show all references within staging area





## Looking Info

#### git status
- `git status` 显示工作区与暂存区的区别，以及暂存区与HEAD的区别
- `git status -s` 输出更加简短

#### git diff
- `git diff` 显示工作区与暂存区的差别，但不包括未追踪的文件
- `git diff [<commit>]` 显示工作区与某次提交（默认为HEAD）的区别
- `git diff --cached|--staged [<commit>]` 显示暂存区与分支（默认为HEAD）的差别
- `git diff <commit> <commit>` 显示任意两次提交的区别
- `--stat` 显示摘要

#### git log
- `git log <commit>… ^<commit>…` 列出前面指定提交向上追溯的历史记录，但是不包括后面指定提交向上追溯的历史记录
- `--graph` adds a nice little ASCII graph showing your branch and merge history
- `-<n>` Show only the last n commits
- `--since|--after` Limit the commits to those made after the specified date.
- `--until|--before` Limit the commits to those made before the specified date.
- `git log -p|--patch` 显示提交的具体修改
- `git log --stat` 显示提交的简要修改
- `git log --pretty[=<format>]` 修改显示提交的格式，默认为`medium`
  - `=oneling` 显示在一行
  - `=short/medium/full/fuller` 显示内容依次变多
  - `=format:"%h - %an, %ar : %s"` 显示指定格式
```shell
%H  #Commit hash
%h  #Abbreviated commit hash
%T  #Tree hash
%t  #Abbreviated tree hash
%P  #Parent hashes
%p  #Abbreviated parent hashes
%an #Author name
%ae #Author email
%ad #Author date (format respects the --date=option)
%ar #Author date, relative
%cn #Committer name
%ce #Committer email
%cd #Committer date
%cr #Committer date, relative
%s  #Subject(message)
```

#### git show
- `git show [<options>] <object>…​`

#### git ls-files
- `-c|--cached` 查看暂存区中文件，默认是此命令
- `-m|--midified` 查看修改的文件
- `-d|--delete` 查看删除过的文件
- `-o|--other` 查看没有被git跟踪的文件
- `-s|--stage` 显示mode以及文件对应的Blob对象，进而可以获取暂存区中对应文件里面的内容。






## Basic Snapshotting

#### git add
- `git add .` 添加当前项目所有文件
- `git add [<pathspec>…​]` 添加任意多个文件或文件夹到暂存区

#### git commit
- `-a|--all` automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.
- `-m <msg>` use the given `<msg>` as the commit message. If multiple -m options are given, their values are concatenated as separate paragraphs.
- `-C <commit>` take an existing commit object, and reuse the log message and the authorship information (including the timestamp) when creating the commit.
- `-c <commit>` Like -C, but the user can further edit the commit message.
- `--amend` replace the tip of the current branch by creating a new commit. The new commit has the same parents. Roughly equivalent for `git reset --soft HEAD^` + `...` + `git commit -c ORIG_HEAD`

#### git mv
- `git mv <source> <destination>` 若目标文件不存在，则重命名
- `git mv <source> <destination directory>` 移动
- `-f` 强制重命名或移动，即使目标存在
- git不追踪文件的移动，所以直接移动或重命名会被当成直接删除原文件并增加新的未追踪文件，而`git rm`命令相当于`mv`+`git rm`+`git add`

#### git rm
- `git rm <file>` 若文件没有修改，则将文件从暂存区和工作区中移除
- `git rm -f <file>` 若已修改，可使用`-f`强制移除
- `git rm --cached <file>` 仅将文件从暂存区移除，解除git的追踪，但暂存区文件须与工作区文件或HEAD相同
- `git rm log/\*.log` 移除`log`文件夹下的所有`.log`文件，反斜杠用来避免shell的文件名拓展
- 直接删除只会从工作区移除，而`git rm` 会缓存文件的移除，可以直接提交，解除git对该文件的追踪，相当于`rm`+`git add`


## Recover and stash
#### git restore
- `git restore [<pathspec>…​]` 将工作区文件恢复至与暂存区一致
- `git restore --staged <pathspec>…​` 将暂存区文件恢复至与HEAD一致
- `-s <tree>|--source=<tree>` 指定还原源
- 若使用了`-S|--staged`，则还原源为HEAD，否则为index
- 若只使用`-S|--staged`，则只恢复暂存区文件
- 若同时使用`-S|--staged`和`-W|--worktree`，则同时还原工作区与暂存区文件
- 若还原源中不包含指定路径，则删除指定路径

#### git reset
- `git reset [<tree-ish>] [<pathspec>…​]` 将暂存区文件重置至与HEAD一致
- `git reset [<mode>] [<commit>]` 回退至某个版本，默认模式为`--mixed`
  - `--soft` 不改变工作区和暂存区
  - `--mixed` 仅重置暂存区
  - `--hard` 重置工作区与暂存区
- 会同时移动HEAD和分支到指定提交上，更加危险，而checkout只会移动HEAD

#### git stash
- `git stash` Record the current state of the working directory and the index
- `git stash list [<log-options>]` List the stash entries that you currently have.
- `git stash pop [--index] [<stash>]`  Remove a single stashed state from the stash list and apply it on top of the current working tree state. The working directory must match the index.
- `git stash apply [--index] [<stash>]` Like pop, but do not remove the state from the stash list. 
- `git stash drop [<stash>]` Remove a single stash entry from the list of stash entries.





## Branching and Merging

#### git branch
- `git branch [-l]` 显示本地分支信息
- `git branch -v|-vv` 显示详细信息
- `git branch <branchname> [<start-point>]` 在起始点（默认为HEAD）创建分支
- `git branch (-m|-M) [<oldbranch>] <newbranch>` 重命名分支
- `git branch (-c|-C) [<oldbranch>] <newbranch>` 拷贝分支
- `git branch (-d|-D) [-r] <branchname>…​` 删除分支
- `git branch -r|--remote` 显示远程仓库分支信息
- `git branch -u|--set-upstream-to=<upstream> [<branchname>]` 设置上游分支，将本地分支与远程分支进行关联，本地分支默认为当前分支

#### git checkout
- `git checkout <branch>` HEAD指向指定分支，并改变工作区和暂存区文件，工作区的修改会保持。如果`<branch>`本地不存在，但在一个远程仓库中存在，则相当于`git checkout -b <branch> --track <remote>/<branch>`
- `git checkout -b <new-branch> [<start-point>]` 若直接指明本地分支，则在其上新建分支，并切换到新建分支上
- `git checkout [-f] [<tree-ish>] <pathspec>…​` 未提供树时，用暂存区文件重写工作区文件，否则用树中文件重写工作区和暂存区文件
- 在本地新建分支关联到远程分支
  - `git checkout -b <new-branch> <remote>/<branch>` 若指明远程仓库/远程分支，则会新建分支关联到远程分支，并切换到远程分支的文件
  - `git checkout -b <new-branch> --track <remote>/<branch>`
  - `git checkout --track <remote>/<branch>` 会新建与远程分支同名的分支

#### git switch
- `git switch <branch>` 切换分支
- `git switch (-c|-C) <new-branch> [<start-point>]` 新建分支并切换

#### git merge
- `git merge <commit>…​`
  - Fast Forward Merge: 若HEAD指向分支为指定分支的祖先，HEAD指向分支移至指定分支（一般先移动到master）
  - Three-way Merge: 若master已有修改提交，则比较Mine, Yours, and Ancestor。若Mine和Yours一致，则不变；若不一致，但有一份与Ancestor一致，则保留不同的版本；若都不一致，则产生不可自动修改的冲突
- `git merge --continue` 冲突之后经过手动修改，继续合并
- `git merge --abort` 返回合并前的状态
- `git merge --quit` 保持工作区和暂存区文件不变，退出合并

#### git tag
- `git tag` 列出所有标签
- `git tag <tagname> [<commit>]` 在指定位置（默认为HEAD）创建轻量标签 
- `git tag -a <tagname> [-m "..."] [<commit>]` 在指定位置（默认为HEAD）创建附注标签 
- `git tag -d|--delete <tagname>…` 删除标签
- `git push <remote> :refs/tags/<tagname>` 从远程删除标签
- `git push <remote> -d|--delete <tagname>` 从远程删除标签
- `git tag -l|--list [<pattern>...]` 列出所有匹配的标签
- `git tag -l|--list --contains [<commit>]` 列出在指定提交（默认为HEAD）上的标签
- `git tag -l|--list --no-contains [<commit>]` 列出所有不在指定提交（默认为HEAD）上的标签



## Remote
#### git clone
- `git clone <url>` 克隆服务器代码到本地`origin`远程仓库中，并自动使本地master分支追踪远程master分支
- `git clone <url> <directory-name>` 指定仓库名

#### git remote
- `git remote` 显示所有的远程仓库
- `git remote -v|--verbose` 在远程仓库的名字后显示url
- `git remote add <shortname> <url>` 添加新的远程仓库
- `git remote rename <old> <new>` 重命名远程仓库
- `git remote remove|rm <remote>` 删除远程仓库

#### git fetch
- `git fetch <remote>`

#### git push
- `git push` 推送到关联的远程仓库，默认为`origin`
- `git push <remote>` 若远程仓库存在同名分支则推送至远程
- `git push <remote> master` 将本地的master分支推送到到远程主机的master分支，如果远程主机的的master分支不存在则会新建
- `git push -u|--set-upstream <remote-repo> <remote-branch>` 将当前分支与指定远程分支关联，若不存在则新建，
- `git push <remote> <tagname>` 将本地标签上传到远程
- `git push <remote> --tags` 将本地所有轻量标签和附注标签上传到远 程





## Configuration
#### show config
```shell
# list all the settings Git can find at that point
git config --list

# check a specific key’s value
git config user.name

# show which configuration file had the final say in setting that value
git config --show-origin rerere.autoUpdate
```
#### ssh
```shell
# set user name and email
git congif --global user.name "Pxtkn"
git config --global user.name "hr.zheng@outlook.com"

# generate a ssh key
ssh-keygen -t rsa -C "hr.zheng@outlook.com"
# by default, will form '.ssh' under '~'
# then need to copy all the content in 'id_rsa.pub' to Github

# check if can connect to Github by ssh
ssh -T git@github.com
```

#### crlf
- `git config --global core.autocrlf true` 在push时把行结束符CRLF转换成LF，在pull时把LF转换成CRLF
- `git config --global core.autocrlf input` 在push时把行结束符CRLF转换成LF
- `git config --global core.autocrlf false` 什么都不改变

#### gitignore
- 当前目录定义的规则，高于父级目录定义的规则，高于`git config --global core.excludesfile /path/to/.gitignore`中定义的全局规则
```shell
# ignore all .a files
*.a
# do track lib.a, even though you're ignoring .a files above
!lib.a
# only ignore the file in the current directory, avoid recursivity
/file
# ignore all files in any directory named build
build/
# only ignore all files in build/ in the current directory
/build/
# only ignore all .txt files in doc/
doc/*.txt
# ignore all .pdf files in doc/ recursively
doc/**/*.pdf
# ignore a0, a1, ..., c8, c9.txt
[abc][0-9].txt
```
#### alias
```shell
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.last 'log -1 HEAD'
git config --global alias.unstage 'reset HEAD --'
```
#### Other configurations
```shell
#### Default Editor
# On a Windows system, must specify the full path to its executable file
git config --global core.editor emacs

#### Default Branch Name
git config --global init.defaultBranch main
```