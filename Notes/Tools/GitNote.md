[toc]


## Common usage
#### Redo commit
- `git commit --amend -C HEAD` Change the last commit with the files in the index ,and use the same commit message

#### Unstage
- `git restore --staged <file>...`
- `git reset HEAD <file>...`

#### Discard changes
- `git restore <file>...`
- `git checkout -- <file>...`

#### Untrack files
- `git rm --cached <file>...`

#### Relate upstream branch
- `git branch -u <upstream>` Set up the current branch's tracking information
- `git push -u <remote> <branch>` For every branch that is up to date or successfully pushed, add upstream (tracking) reference while pushing.

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
- `git branch <branchname> [<start-point>]` create branch
- `git branch -d|--delete <branchname>…​` delete branch
- `git branch -m|--move [<oldbranch>] <newbranch>` rename branch, default is `HEAD`
- `git branch -c|--copy [<oldbranch>] <newbranch>` copy branch, default is `HEAD`
- `git branch -l|--list [<pattern>]`
  - List branches. 
  - With optional `<pattern>`, list only the branches that match the pattern(s).
- `git branch -v|-vv`
  - When in list mode, show sha1 and commit subject line for each head, along with relationship to upstream branch (if any).
  - If given twice, print the path of the linked worktree (if any) and the name of the upstream branch
<br>

- `git branch -r|--remotes`
  - List or delete (if used with `-d`) the remote-tracking branches.
  - Combine with `--list` to match the optional pattern(s).
- `git branch -u|--set-upstream-to <upstream> [<branchname>]`
  - Set up `<branchname>`'s tracking information so `<upstream>` is considered `<branchname>`'s upstream branch. 
  - If no `<branchname>` is specified, then it defaults to the current branch.
- `git branch --unset-upstream [<branchname>]` 
  - Remove the upstream information for `<branchname>`.
  - If no branch is specified it defaults to the current branch.

#### git checkout
- `git checkout <branch>`
  - To prepare for working on `<branch>`, switch to it by updating the index and the files in the working tree, and by pointing `HEAD` at the branch.
  - Local modifications to the files in the working tree are kept.
  - If `<branch>` is not found but there does exist a tracking branch in exactly one remote with a matching name and `--no-guess` is not specified, treat as equivalent to `git checkout -b <branch> --track <remote>/<branch>`
<br>

- `git checkout -b <new-branch> [-t|--track[=direct|inherit]] [<start-point>]`
  - If no specified, the `<start-point>` branch is `HEAD`
  - `-t`, `--track`, or `--track=direct` means to use the `<start-point>` branch itself as the upstream
  - `--track=inherit` means to copy the upstream configuration of the `<start-point>` branch.
  - If no `-b` option is given, the name of the new branch will be derived from the remote-tracking branch. For example: `git checkout -t origin/dev`
<br>

- `git checkout [<tree-ish>] [--] <pathspec>…​`
  - Overwrite the contents of the files that match the pathspec.
  - When the `<tree-ish>` (most often a commit) is not given, overwrite working tree with the contents in the index.
  - When the `<tree-ish>` is given, overwrite both the index and the working tree with the contents at the <tree-ish>.
  - `--` means do not interpret any more arguments as options.

#### git switch
- `git switch <branch>` 切换分支
- `git switch -c|-C <new-branch> [<start-point>]` 新建分支并切换

#### git merge
- `git merge <commit>…​` Incorporates changes from the named commits into the current branch, since the time their histories diverged from the current branch.
- `git merge --continue`
  - After resolving the conflicts and `git add` them to the index, use `git commit` or `git merge --continue` to seal the deal.
  - The latter command checks whether there is a (interrupted) merge in progress before calling git commit.
- `git merge --abort` Abort the current merge process, and try to reconstruct the pre-merge state, including the index and working tree.
- `git merge --quit` Forget about the current merge in progress. Leave the index and the working tree as-is.
- `MERGE_HEAD` ref is set to point to the other branch head.
- `stage 1` stores the version from the common ancestor, `stage 2` from `HEAD`, and `stage 3` from `MERGE_HEAD` (you can inspect the stages with git ls-files -u). The working tree files contain the result of the "merge" program

#### git rebase
- `git rebase [<upstream> [<branch>]]`
  - All changes made by commits in the current branch but that are not in `<upstream>` are saved to a temporary area.
  - The current branch is reset to `<upstream>`
  - The commits that were previously saved into the temporary area are then reapplied to the current branch, one by one, in order.
- `<<branch>` Working branch; defaults to `HEAD`. If `<branch>` is specified, git rebase will perform an automatic `git switch <branch>`
- If `<upstream>` is not specified, the upstream configured in `branch.<name>.remote` and `branch.<name>.merge` options will be used
- `--continue` Restart the rebasing process after having resolved a merge conflict.
- `--abort` Abort the rebase operation and reset HEAD to the original branch.
- `--quit` Abort the rebase operation but HEAD is not reset back to the original branch. The index and working tree are also left unchanged as a result.

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
- `git clone <repository> [<directory>]` Clones a repository into a newly created directory, creates remote-tracking branches for each branch in the cloned repository, and creates and checks out an initial branch that is forked from the cloned repository’s currently active branch.

#### git remote
- `git remote` show all remotes
- `git remote -v|--verbose` show all remotes verbosely
- `git remote add <name> <URL>` add remote
- `git remote rename <old> <new>` rename remote
- `git remote rm|remove <name>` remove remote

#### git fetch
- `git fetch [<options>] [<repository> [<refspec>…​]]`
- `--all` Fetch all remotes.
- The names of refs that are fetched, together with the object names they point at, are written to `.git/FETCH_HEAD`.

#### git pull
- `git pull [<options>] [<repository> [<refspec>…​]]` Incorporates changes from a remote repository into the current branch.
- `<repository>` should be the name of a remote repository as passed to `git-fetch`.
- `<refspec>` can name an arbitrary remote ref (for example, the name of a tag) or even a collection of refs with corresponding remote-tracking branches, but usually it is the name of a branch in the remote repository.
- `--all` Fetch all remotes.
- `--set-upstream` If the remote is fetched successfully, add upstream (tracking) reference

#### git push
- `git push [<repository> [<refspec>…​]]` Updates remote refs using local refs, while sending objects necessary to complete the given refs.
- If `<repository>` argument is not specified, the upstream configured in `branch.<name>.remote` will be used. If the configuration is missing, it defaults to origin.
- If `<refspec>...` arguments or `--all`, `--mirror`, `--tags` options is not specified, the command finds the default `<refspec>` by consulting `remote.<name>.push` configuration, and if it is not found, honors `push.default` configuration to decide what to push
-  The format of a `<refspec>` parameter is an optional plus +, followed by `<src>:<dst>`.
-  If `<dst>` doesn’t start with refs/ (e.g. refs/heads/master) we will try to infer where in refs/* on the destination `<repository>` it belongs based on the type of `<src>` being pushed and whether `<dst>` is ambiguous.
-  Pushing an empty `<src>` allows you to delete the `<dst>` ref from the remote repository. Deletions are always accepted without a leading `+` in the refspec.
<br>

- `--all` Push all branches (i.e. refs under `refs/heads/`); cannot be used with other `<refspec>`.
- `-d|--delete` All listed refs are deleted from the remote repository. This is the same as prefixing all refs with a colon.
- `--tags` All refs under refs/tags are pushed, in addition to refspecs explicitly listed on the command line.
- `-u|--set-upstream` For every branch that is up to date or successfully pushed, add upstream (tracking) reference, i.e. `git push -u origin main`








## Configuration
#### show config
```shell
# list all the settings Git can find at that point
git config --list

# show a specific key’s value
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
#### mergetool and difftool
```shell
merge.tool=code
mergetool.code.cmd='code --wait $MERGED'

diff.tool=code
difftool.code.cmd='code --wait --diff $LOCAL $REMOTE'
```
#### Other configurations
```shell
#### Default Editor
# On a Windows system, must specify the full path to its executable file
git config --global core.editor emacs

#### Default Branch Name
git config --global init.defaultBranch main
```