
- [Git 笔记](#git-笔记)
    - [基本文件操作](#基本文件操作)
        - [git add](#git-add)
        - [git commit](#git-commit)
        - [git mv](#git-mv)
        - [git rm](#git-rm)
    - [信息查看](#信息查看)
        - [git status](#git-status)
        - [git diff](#git-diff)
        - [git log](#git-log)
        - [git show](#git-show)
        - [git cat-file](#git-cat-file)
        - [git ls-files](#git-ls-files)
    - [恢复保存](#恢复保存)
        - [git restore](#git-restore)
        - [git reset](#git-reset)
        - [git reflog](#git-reflog)
        - [git stash](#git-stash)
    - [分支管理](#分支管理)
        - [git branch](#git-branch)
        - [git checkout](#git-checkout)
        - [git switch](#git-switch)
        - [git merge](#git-merge)
        - [git rebase](#git-rebase)
        - [git tag](#git-tag)
    - [远程管理](#远程管理)
        - [git remote](#git-remote)
        - [git fetch](#git-fetch)
        - [git pull](#git-pull)
        - [git push](#git-push)
    - [配置管理](#配置管理)
        - [git config](#git-config)
        - [gitignore](#gitignore)





# Git 笔记

## 基本文件操作

### git add

- `git add .` 添加当前项目所有文件
- `git add [<pathspec>…​]` 添加任意多个文件或文件夹到暂存区

### git commit

git commit 的常用选项有：

- `-a/--all` 自动暂存所有文件，未追踪的文件不受影响
- `-m/--message <msg>` 指定提交的注释，若不指定则会弹出编辑器
- `-C <commit>` 重用指定提交的信息，包括注释、作者信息和时间戳
- `-c <commit>` 与 `-C` 选项相似，但会打开编辑器提供机会修改提交信息
- `--amend` 让新的提交替换当前分支的末端，相当于`git reset --soft HEAD^` + `git commit -c ORIG_HEAD`

### git mv

- `git mv <source> <destination>` 若目标不存在则改变路径，若目标已存在且是文件则会报错，加上 `-f/--force` 选项则可以强制重命名或移动
- `git mv <source>…​ <destination directory>` 移动多个文件到目标文件夹

由于 git 不追踪文件的移动或重命名，直接操作被当成删除原文件并增加新的未追踪文件，使用 git mv 可以避免这一点，减少麻烦，这在大规模移动文件时尤其重要。

### git rm

- `git rm [<pathspec>…​]` 若文件没有修改，则将文件从暂存区和工作区中移除；若已修改，可使用 `-f/--force` 选项强制移除
- `git rm --cached [<pathspec>…​]` 仅将文件从暂存区移除，解除追踪

在 pathspec 中，可以使用通配符进行匹配，例如 `git rm 'log/*.log'` 会删除 log 文件夹中的所有 .log 文件。







<br>

## 信息查看

### git status

- `git status` 显示当前所处分支、暂存区与 HEAD 有区别的文件、工作区与暂存区有区别的文件，以及未追踪的文件
- `git status -s/--short` 以简短的形式输出

### git diff

- `git diff [--] [<path>…​]` 显示工作区与暂存区的差别，不包括未追踪的文件
- `git diff --no-index [--] <path> <path>` 显示两个指定文件的差别
- `git diff --cached/--staged [<commit>] [--] [<path>…​]` 显示暂存区与某次提交的差别，默认为 HEAD
- `git diff <commit> [--] [<path>…​]` 显示工作区与某次提交的差别
- `git diff <commit> <commit> [--] [<path>…​]` 显示任意两次提交的区别

若在上述命令中使用了 `--stat` 选项，则只会显示每个文件的统计情况。

在 git 中，可用 `--` 分隔 path 与其前面部分，以避免选项混淆。

### git log

```shell
git log [<options>] [<revision-range>] [[--] <path>…​]
```

git log 会列出可由指定提交追溯到的提交历史，并会排除可由前带有 `^` 的提交追溯到的提交历史，例如 `git log ^foo bar` 会列出 bar 的提交历史，但不包括 foo 的提交历史，`foo..bar` 可用作其简写，常用于表示一连串提交。

需要注意的是，与之类似还有 `foo...bar`，其定义为 `r1 r2 --not $(git merge-base --all r1 r2)`，常用于表示由同一祖先分出的两串分支。同时，这两种写法都可以省略一端，以默认的 HEAD 来代替，例如 `origin..HEAD` 可以简写为 `origin..`，表示当前分支尚未推送到远程的提交。

若指定了 path，则只会显示与 path 相关的提交历史。

以下选项可以用于筛选提交：

- `-<number>` 最多只显示 number 条提交
- `--since/--after=<date>` 只显示在指定日期之后的提交，日期格式可为：
    - `YYYY-MM-DD` `YYYY.MM.DD` `YYYY/MM/DD`，若不指定则默认为今天
    - `HH:MM:SS`，若不指定则默认为午夜
    - `n minutes/hours/days/weeks/months/years ago`，其中末尾的 `s` 可省略，空格也可替换成 `.` `-` `/`
- `--until/--before=<date>` 只显示在指定日期之前的提交
- `--author/--commiter=<pattern>` 只显示作者名符合 pattern 的提交，可使用 `-i` 选项忽略大小写

以下选项可用于修改显示格式：

- `--stat` 显示修改的统计信息
- `-p/--patch` 显示提交的具体修改，可与 `--stat` 选项一起使用
- `--abbrev-commit` 显示提交哈希的缩写
- `--pretty[=<format>]` `--format=<format>` 修改显示格式，默认为 `medium`
- `--oneline` 等价于 `--pretty=oneline --abbrev-commit`
- `--graph` 在左侧绘制图，显示分支与合并历史

`--pretty` 或 `--format` 选项中的 format 可为：

- `=oneling` 显示在一行
- `=short/medium/full/fuller` 显示内容依次变多，short 只含提交哈希、作者名与标题行，fuller 则包括提交哈希、作者名、作者日期、提交者名、提交日期、标题行与完整提交注释
- `=format:<format-string>` 显示指定格式，可以使用以下占位符：
    - `%H` 提交哈希
    - `%h` 提交哈希的缩写
    - `%an` 作者名
    - `%ae` 作者邮箱
    - `%ad` 作者日期
    - `%ar` 作者相对日期
    - `%ai` 类 ISO 8601 格式的作者日期
    - `%as` 作者日期的缩写，格式为 `YYYY-MM-DD`
    - `%cn` 提交者名。其余各占位符与作者信息相同，只需将 `a` 替换成 `c`
    - `%d` 引用名，包括分支与标签
    - `%s` 标题行，即提交注释的第一行
    - `%Cred` `%Cgreen` `%Cblue` `%Creset` `%C(…​)` 切换之后的颜色，其中 `%Creset` 用于重置颜色，`%C(auto)` 可以自动设置颜色

### git show

```shell
git show [<options>] [<object>…​]
```

与 git log 和 git cat-file 类似，但侧重于显示指定对象且可读性更强，可以是提交、标签、树或者 blob，会根据对象的类型，显示对象的内容：

- 若对象是提交和标签，则会显示详细信息与具体修改，可接受 git log 的那些修改显示格式的选项
- 若是树，则会列出其下文件名称
- 若是 blob，则会显示其内容

### git cat-file

- `git cat-file -t <object>` 显示对象的类型
- `git cat-file -s <object>` 显示对象的大小
- `git cat-file -p <object>` 根据对象的类型，显示对象的内容
    - 若对象是提交或标签，则会显示其所有信息，包括树、父提交、作者等
    - 若对象是树，则会显示其所有 blob 与子树的信息，包括权限、类型、哈希值与文件名
    - 若对象是 blob，则会显示其内容

### git ls-files

- `git ls-files [-c/--cached]` 列出暂存区的文件，即所有被追踪的文件
- `git ls-files -d/--deleted` 列出所有已被删除但尚未暂存的文件
- `git ls-files -m/--modified` 列出所有已被修改但尚未暂存的文件，包括被删除
- `git ls-files -o/--other` 列出尚未被追踪的文件
- `git ls-files -i/--ignored` 列出所有被忽略的文件，必须使用 `-c` 或 `-o` 选项来指定搜索范围，同时还必须使用 `--exclude*` 选项来进行匹配，例如 `git ls-files -io --exclude='*.log'` 可以列出所有未追踪的被忽略的 .log 文件
- `git ls-files -s/--stage` 列出暂存区文件的信息，包括权限、哈希值与文件名等








<br>

## 恢复保存

### git restore

```shell
git restore [<options>] [--source=<tree>] [--staged] [--worktree] [--] <pathspec>…​
```

git restore 可用于恢复工作区和暂存区中的文件，恢复源可以通过 `-s/--source <tree>` 手动指定。若 pathspec 已被追踪但不存在于恢复源中，则会被删除以匹恢复源。

默认情况下，git restore 恢复工作区文件，恢复源为 index；若使用了 `-S/--stage` 选项，则恢复暂存区文件，恢复源为 HEAD；若同时使用了 `-S/--stage` 和 `-W/--worktree` 选项，则同时恢复工作区与暂存区文件。

### git reset

git reset 可用于重置暂存区的文件，如：

- `git reset [<tree-ish>] [--] <pathspec>…​` 重置暂存区的文件，使其与 tree-ish 一致，tree-ish 默认为 HEAD

但相比之下，git reset 更常用于回退版本，具体命令为：

- `git reset [<mode>] [<commit>]` 将当前分支重置为指定 commit，暂存区和工作区的文件的改变视模式而定，默认为 mixed
    - `--soft` 不改变工作区和暂存区
    - `--mixed` 仅重置暂存区
    - `--hard` 重置工作区与暂存区

需要注意的是，该操作会同时移动 HEAD 和当前分支到指定提交上，更加危险。不过在进行该操作前，git 会将原分支设为 `ORIG_HEAD`，以便回退。

在指定提交时，可以使用相对引用，例如 `HEAD^` 可以表示 HEAD 的父提交，其中 `^` 可以叠加使用；`HEAD~2` 可以更方便地表示 HEAD 的父提交的父提交；当存在多个父提交时，可以使用 `^n` 来指定第 n 父级，若不使用则默认为第一父级。

### git reflog

```shell
git reflog [show] [<log-options>] [<ref>]
```

git 的引用存储在 .git/refs 文件夹中，主要分为以下几类：

- 本地分支，格式为 `refs/heads/<branch>`
- 远程追踪分支，格式为 `refs/remotes/<remote>/<branch>`
- 标签，格式为 `refs/tags/<tagname>`

以上引用在使用时，大多可将 `refs/heads` 等前缀略去。

除此以外，还会有一些特殊的引用存储在 .git 文件夹中，例如 `HEAD` 指向当前检出 commit，`ORIG_HEAD` 指向危险操作前的 HEAD，`FETCH_HEAD` 指向最近一次拉取的分支（可能会有多个），`MERGE_HEAD` 指向欲合并的目标分支。

git 会记录下所有引用的变动，包括提交、合并、重置等，这些记录被称为 reflog，可以通过 `git reflog` 来查看，具体形式为 `HEAD@{n}`，可用于恢复历史。

git reflog 的默认子命令为 show，可以接受 git log 的所有参数。

### git stash

- `git stash [push] [--] [<pathspec>…]` 临时保存未提交的更改，使工作目录回到干净的状态，默认会贮藏所有更改
    - `-S/--staged` 仅贮藏暂存区的更改
    - `-u/--include-untracked` 也贮藏未追踪的文件
    - `-k/--keep-index` 保留暂存区的更改
    - `-m/--message <msg>` 指定贮藏项的注释，默认为当前 commit 的注释
- `git stash list [<log-options>]` 列出所有贮藏项，具体形式为 `stash@{n}: <message>`
- `git stash show [<diff-options>] [<stash>]` 显示贮藏项的内容
- `git stash pop [<stash>]` 弹出一个贮藏项并应用，默认为 `stash@{0}`
- `git stash drop [<stash>]` 删除一个贮藏项
- `git stash clear` 删除所有贮藏项








<br>

## 分支管理

### git branch

以下命令可以列出分支：

- `git branch` `git branch -l/--list` 列出所有本地分支
- `git branch -r/--remotes` 列出所有远程追踪分支
- `git branch -a/--all` 列出所有分支
- `git branch -v` 列出本地分支的最后一次提交
- `git branch -vv` 列出本地分支的最后一次提交与上游分支

上述各选项可以组合使用，而且需要注意的是，如果想要使用 pattern 匹配分支，则必须要使用 `--list` 选项，例如 `git branch -rl *dev*`。

以下命令可以修改分支：

- `git branch <branchname> [<start-point>]` 新建一个指向 start-point 的本地分支，默认为 HEAD，若为远程追踪分支则会自动设置其为上游分支
- `git branch -d/--delete <branchname>…​` 删除本地分支
- `git branch -m/--move [<oldbranch>] <newbranch>` 重命名本地分支
- `git branch -c/--copy [<oldbranch>] <newbranch>` 复制本地分支

被删除的分支不能是当前分支，且必须要完全合并进上游分支，若没有上游分支则要完全合并进 HEAD，也就是说，删除目标需要能通过上游分支或 HEAD 恢复，以免丢失未合并的更改；newbranch 也不能是已存在的分支名。若要强制如此，可以使用 `-f/--force` 选项，或者直接使用 `-D` `-M` `-C` 选项来代替。此外，`-d` 和 `-r` 选项可以组合使用，以删除存储在本地的远程追踪分支。

以下命令可以设置上游分支：

- `git branch -u/--set-upstream-to <upstream> [<branchname>]` 设置上游分支
- `git branch --unset-upstream [<branchname>]` 移除上游分支
- `<upstream>` 的形式为 `<remote>/<branch>`
- `<branchname>` 若未被指定，则默认为当前分支

本地分支在推送和拉取前，需要先设置上游分支，以与某个远程仓库的远程分支建立联系，其在本地的存在形式为远程追踪分支。如果此前本地并没有远程追踪分支，可以先使用 `git fetch` 拉取远程仓库，然后再将拉取来远程追踪分支的设置为上游分支。

### git checkout

`git checkout` 可以切换 HEAD 的位置，更新工作区和暂存区，常用的命令有：

- `git checkout <branch>` 切换到指定分支
- `git checkout <commit>` 切换到指定 commit
- `git checkout -` 切换到前一个位置
- `git checkout -d/--detach [<branch>]` 切换分支并分离 HEAD
- `git checkout -b <new-branch> [<start-point>]` 新建分支并切换，start-point 默认为 HEAD，若为远程追踪分支则会自动设置其为上游分支

需要注意的是，只有在前后 HEAD 的文件完全相同的情况下，`git checkout` 才会保持本地的更改，否则会报错，这样可以避免本地的更改被覆盖。

此外，`git checkout` 还可以做到从已给分支名推测远程追踪分支，或者从远程追踪分支推测分支名：在使用 `git checkout <branch>` 时，如果本地没有该分支名，而且刚好有一个远程仓库有一个同名的远程追踪分支，则会自动新建分支并追踪；在使用 `git checkout -t <remote>/<branch>` 时，如果本地没有该分支名，同样也会自动新建分支并追踪。这两种情况都相当于在使用 `git checkout -b <branch> --track <remote>/<branch>`。当然，如果想要新建分支名和远程追踪分支名不同，就不能省略 `-b` 选项了。

### git switch

- `git switch <branch>` 切换分支
- `git switch -` 切换到前一个分支，不能是 commit
- `git switch -d/--detach [<start-point>]` 切换位置并分离 HEAD
- `git switch -c/--create <new-branch> [<start-point>]` 新建分支并切换

`git switch` 和 `git checkout` 一样，可以在前后 HEAD 的文件完全相同的情况下保持更改，也可以做到从已给分支名推测远程追踪分支，或者从远程追踪分支推测分支名，从而在省略 `-c` 选项的情况下完成自动新建与追踪。

### git merge

- `git merge <commit>…​` 将指定提交合并到当前分支
- `git merge --continue` 在解决了冲突后继续合并，需要处于合并过程
- `git merge --abort` 取消合并，回到合并前的状态
- `git merge --quit` 退出合并，但不回到合并前的状态

若当前分支是目标分支的祖先，则会进行快进合并，不会产生 merge commit，否则在没有冲突的情况下，会自动产生一个新的 merge commit。如果不想自动产生合并提交，可以使用 `--no-commit` 选项。

合并分支有多种策略，可以使用 `-s/--strategy` 选项来指定，常用的策略有：

- `ort` 是合并两个分支时的默认策略，使用三路合并算法，具体就是，如果只有一方有修改，或者双方都有修改但修改相同，则选择修改后的文件，否则就会产生冲突，需要手动解决
    - 可以使用 `-X/--strategy-option ours/theirs` 选项来指定合并时的冲突解决策略，`ours` 代表保留当前分支的修改，`theirs` 代表保留合并分支的修改
- `octopus` 是合并多于两个分支时的默认策略，在合并过程中一旦出现需要手动解决的冲突就会拒绝合并
- `ours` 策略不同于 `-X ours`，会完全保留当前分支的更改，不考虑其他分支

如果不想留下其他分支的记录，保持线性的提交历史，可以使用 `--squash` 选项，这样就会将其他分支的所有提交合并成一个提交附加到当前分支。

### git rebase

- `git rebase [--onto <newbase>] [<upstream> [<branch>]]` 保存 branch 有而 upstream 没有的提交，也即保存从 upstream 到 branch 的提交，然后将其逐个应用到 upstream 上
    - 若有 `--onto` 选项，则会将补丁应用到 newbase 上
    - 若未指定 `<upstream>`，则会使用当前分支的上游分支
- `git rebase --continue` 在解决了冲突后继续变基
- `git rebase --abort` 取消变基，回到变基前的状态，若有 branch 则会切换到 branch
- `git rebase --quit` 退出变基，但不回到变基前的状态
- `git rebase --skip` 继续变基，跳过当前补丁

`git rebase` 可用于删除提交，例如 `git rebase --onto feature~5 feature~3 feature` 会删除从 `feature^4` 到 `feature^3` 的提交；也可用于将某一分支的部分更改应用到另一分支上，例如 `git rebase --onto master feature bugfix` 会将 feature 分支上对 bug 的修复应用到 master 分支上。

`git rebase` 更常用的用法是加上 `-i/--interactive` 选项，以交互式的方式来变基，可以方便地对提交进行删除、合并等操作，并且只会改变提交时间，不会改变作者时间，其命令有：

- `p, pick <commit>` 使用提交
- `r, reword <commit>` 使用提交，但是会弹出编辑器，提供修改提交信息的机会
- `e, edit <commit>` 使用提交，但是会在应用该提交后停下，以便使用 `--amend` 选项来修改提交
- `s, squash <commit>` 使用提交，但是会将该提交合并进上一个提交，然后弹出编辑器，显示合并后的提交信息，适用于合并多个相似的小更改
- `f, fixup [-C | -c] <commit>` 和 squash 一样能够合并多个提交，但会自动使用之前的提交信息，若使用 `-C` 选项则会使用当前提交信息，若使用 `-c` 选项还会在使用当前提交信息的基础上打开编辑器，适用于将修复合并进之前的提交
- `d, drop <commit>` 移除提交

### git tag

- `git tag` 列出所有标签
- `git tag -l/--list [<pattern>…]` 列出所有标签，若有 pattern 则会匹配
- `git tag <tagname> [<commit>]` 创建轻量标签 
- `git tag -a/--annotate <tagname> [-m <msg>] [<commit>]` 创建附注标签 
- `git tag -d/--delete <tagname>…` 删除标签








<br>

## 远程管理

### git remote

- `git remote` 显示所有远程仓库
- `git remote -v/--verbose` 显示所有远程仓库的详细信息，包括 URL
- `git remote add <name> <URL>` 添加远程仓库
- `git remote rename <old> <new>` 重命名远程仓库
- `git remote rm/remove <name>` 删除远程仓库
- `git remote set-url [--push] <name> <newurl>` 修改远程仓库的 URL，若使用 `--push` 选项则只修改 push 地址

### git fetch

```shell
git fetch [<options>] [<repository> [<refspec>…​]]
```

git fetch 能从远程仓库拉取分支，用以更新远程追踪分支，其常用选项有：

- `--all` 拉去所有的远程仓库
- `-v/--verbose` 显示详细信息
- `-p/--prune` 删除远程仓库中不存在的远程追踪分支

refspec 用于表示本地引用和远程引用之间的映射关系，其格式为 `[+]<src>:<dst>`。在 git fetch 中，src 表示要拉取的远程引用，dst 表示要更新的本地引用，+ 号表示允许 non-fast-forward。

在使用 git fetch 时，若未指定 repository，则会使用上游分支的远程仓库，若没有上游分支，则会使用 origin 仓库；若未指定 refspec，则会使用 `remote.<repository>.fetch` 中的配置，一般为 `+refs/heads/*:refs/remotes/origin/*`，即将远程仓库的所有分支都拉取到本地对应的远程追踪分支中；若 refspec 中的 `:<dst>` 被忽略，则会更新与 src 对应的远程追踪分支。

### git pull

```shell
git pull [<options>] [<repository> [<refspec>…​]]
```

git pull 形式与 git fetch 相同，但会在拉取后自动合并，相当于 git fetch + git merge，其常用选项有：

- `-r/--rebase[=false|true|merges|interactive]` 使用变基而不是合并，可以在 `pull.rebase` `branch.<name>.rebase` `branch.autoSetupRebase` 中配置
- `--no-rebase` 相当于 `--rebase=false`
- `--set-upstream` 若拉取成功，则设置上游分支
- 其余更多选项可见 git fetch 和 git merge

### git push

```shell
git push [<repository> [<refspec>…​]]
```

git push 能推送本地分支到远程仓库，使用本地引用更新远程引用，其常用选项有：

- `--all` 推送所有分支
- `--tags` 推送所有标签
- `--prune` 删除远程仓库中不存在对应本地分支的分支
- `-f/--force` 强制推送
- `-d/--delete` 从远程仓库删去列出的引用，常见用法为 `git push origin --delete <branch>`
- `-u/--set-upstream` 若分支已最新或推送成功，则设置上游分支，常见用法为 `git push -u origin main`

在 git push 中，src 表示要推送的本地引用，dst 表示要更新的远程引用，+ 号表示强制推送。可以使用 `git push <repository> +:<dst>` 强制删除任意引用。

在使用 git push 时，若未指定 repository，则会使用 `branch.<name>.remote` 中的配置，若没有配置则会默认使用 origin 仓库；若未指定 refspec，则会使用 `remote.<name>.push` 中的配置，若没有配置则会默认推送到远程仓库的同名分支；若 refspec 中的 `:<dst>` 被忽略，则默认为 `:<src>`，即推送到同名分支。








<br>

## 配置管理

### git config

- `git config <name> <value>` 设置配置
- `git config -l/--list` 列出所有配置
- `git config --get <name>` 显示指定配置
- `git config --get-regexp <name-regex> [<value-pattern>]` 显示匹配 name-regex 以及可选的 value-pattern 的配置
- `git config --unset <name>` 删除指定配置

在 git 中，配置分为三个级别：系统级别、全局级别和仓库级别，分别对应三个配置文件：`/etc/gitconfig` `~/.gitconfig` `.git/config`。在使用 `git config` 时，可以使用 `--system` `--global` `--local` 选项来指定配置级别，若未指定则默认为 `--local`。

在列出和显示配置时，可以使用 `--show-origin` 选项来显示配置的来源，还可以使用 `--show-scope` 选项来显示配置的级别。

常见的配置有：

- `user.name` 用户名
- `user.email` 用户邮箱
- `alias.<name>` 别名
- `core.editor` 默认编辑器
- `core.autocrlf` 行结束符的转换
    - 若为 `true`，则在提交时将 CRLF 转换成 LF，在检出时将 LF 转换成 CRLF
    - 若为 `input`，则在提交时将 CRLF 转换成 LF
    - 若为 `false`，则不做任何转换
- `merge.tool` 默认合并工具
- `mergetool.<tool>.cmd` 使用某合并工具时的命令
- `diff.tool` 默认比较工具
- `difftool.<tool>.cmd` 使用某比较工具时的命令
- `init.defaultBranch` 默认分支名

另外一种与 git 无关但与 Github 有关的配置是 SSH 密钥，可以使用 `ssh-keygen` 来生成密钥，然后将 .pub 公钥添加到 Github 上。

```shell
# 生成带邮箱注释的的 rsa 密钥
ssh-keygen -t rsa -C "hr.zheng@outlook.com"

# 检验能否成功连接到 Github
ssh -T git@github.com
```

### gitignore

可在项目根目录中的 .gitignore 文件中定义忽略规则，以忽略不需要追踪的文件，已追踪的文件不受影响。常见的规则如下：

- `build` 忽略所有名为 build 的文件或文件夹
- `build/` 只忽略名为 build 的文件夹，忽略其内所有文件
- `/build/` 只忽略当前目录下的名为 build 的文件夹
- `/codes/*.c` 只忽略 codes 第一层目录下的 .c 文件
- `/codes/*/*.c` 只忽略 codes 第二层目录下的 .c 文件
- `/codes/**/*.c` 忽略 codes 内的所有 .c 文件，`/**/` 可匹配零个或多个目录
- `!` 所有因之前规则被忽略的匹配文件会被重新追踪

