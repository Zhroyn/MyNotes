[toc]





### Operators and motions
- Every motion can be used after an operator command, so the command operates on the text comprised by the movement's reach.
- If the motion includes a count and the operator also had a count before it,the two counts are multiplied. For example: `2d3w` deletes six words.
- Two repeated operators operate on the current line. For example: `g~~/guu/gUU` change case of all characters in a line

##### Operators
- `d` delete
- `c` change
- `y` yank into register
- `g~` swap case
- `gu/U` make lowercase / uppercase
- `</>` shift left / right
- `zf` define a fold

##### Word motions
- `w` next word (beginning)
- `b` beginning of this word or previous word
- `e` end of this word or next word
- `ge` end of previous word

##### Left-right motions
- `0` To the first character of the line
- `^` To the first non-blank character of the line
- `$` To the end of the line
- `f/F{char}` To the {count}'th occurrence of `{char}` to the right / left.
- `t/T{char}` Till before {count}'th occurrence of `{char}` to the right / left of the cursor on the same line. The cursor is placed on the character left / right of `{char}`
- `;` Repeat latest `f, t, F or T` {count} times
- `,` Repeat latest `f, t, F or T` in opposite direction {count} times

##### Up-down motions
- `{count}Enter/j/gj/+` {count} lines downward
- `{count}Enter/k/gk/-` {count} lines upward

##### Text object motions
- `( / )`	{count} sentences backward / forward
- `{ / }`	{count} paragraphs backward / forward
- `[[ / ]]` {count} sections backward / forward
- A sentence is defined as ending at a `. or ! or ?` followed by either the end of a line, or by a space or tab.
- A paragraph begins after each empty line.
- A section begins after a form-feed (`<C-L>`) in the first column

##### Text object selection
- `a/iw` around / inner word[sd[sdas]a]
- `a/is` around / inner sentence
- `a/ip` around / inner paragraph
- `a/it` around / inner tag, select {count} tag blocks, from the {count}'th unmatched `<tag>` backwards to the matching `</tag>`
- `a/ib or ( / )` a / inner block
- `a/iB or { / }` a / inner {} block
- `` a/i [/]/</>/'/"/` `` a / inner `...` block


##### Jumps
- `*` To the next occurrence of the word under the cursor
- `#` To the previous occurrence of the word under the cursor
- `/{string}` To the next occurrence of `{string}`
- `?{string}` To the previous occurrence of `{string}`
- `n` Repeat latest search in same direction
- `N` Repeat latest search in opposite direction
<br>

- `:[range]` Set the cursor on the last line number in [range]
- `gg/G` Go to line {count}, default first / last line, on the first non-blank character
- `{count}%`	Go to {count} percentage in the file, on the first non-blank in the line
- `H` top of screen
- `M` middle of screen
- `L` bottom of screen
- `%` corresponding item
<br>

- `g;` Go to {count} older position in change list
- `g,` Go to {count} newer position in change list
- `` `{a-z/A-Z} `` To the position of the specified mark
- `'{a-z/A-Z}` To the first non-blank character in the line of the specified mark
- ``` ``/'' ``` To the position before the latest jump




### Other Operator
- `p` paste
- `x` delete character, equal to `dl`
- `o/O` insert line below / above
- `s/S` substitute character / line, equal to `cl/cc`
- `C` change character to end of line
- `u` undo
- `U` restore the line to initial state
- `<C-R>` redo





### Other Commands
##### File
- `:e {relative path}` open or create a file
- `:q` close window
- `:w` save(write)
- `:wq` save and quit
- `:q!` force quit and unsave
- `:wq!` force quit and save

##### Fold
- `zo` open fold
- `zc` close fold
- `za` open / close fold
- `zR` open all folds
- `zM` close all folds
- `zf` define a fold
- `zd` delete a fold

##### Substitute
- `:{scope}s/{from}/{to}/{tag}`
- `{scope}`: default is current line
  - `%` all lines in file
  - `10,20` from tenth line to twentieth line
  - `1,$` from first line to last line
  - `.,$` from current line to last line
  - `'a,'b` from line with mark a to line with mark b
  - `'<,'>` from the scope selected in visual mode
- `{tag}`: default is substiting the first matched string
  - `g` globally in scope
  - `c` prompt for each substitution
  - `i/I` case insensitive / sensitive
- `:s/{old}/{new}` 替换当前行第一个`old`为`new`
- `:s/{old}/{new}/g` 替换当前行所有`old`为`new`
- `:#,#s/{old}/{new}/g` 替换两行内所有`old`为`new`
- `:%s/{old}/{new}/g` 替换文件内所有`old`为`new`

##### Mark
- `m{a-z/A-Z}` Set mark at cursor position
- `a-z` for in-file mark
- `A-Z` for global mark

##### Multiple Windows
- `:sp` split windows horizontally
- `:vsp` split windows vertically

##### Macro
- `q{a-z}` record a macro into register
- `q` stop recording
- `{count}@{a-z}` replay a macro {count} times

##### Goto
- `gt or T` 切换标签页
- `ngt` 切换至第n个标签页
- `ngT` 向前n个标签页
- `^0` 跳转至文件栏，而后`l`在右侧打开光标所在文件
- `^n` 跳转至第n组，若无且n刚好大一则创建
- `%` 跳转至另一个配对括号，若不处于括号内则跳转至后一对括号的后一个

##### Others
- `gh` 显示悬浮信息
- `^G` 显示当前编辑文件中当前光标所在行位置以及文件状态信息










