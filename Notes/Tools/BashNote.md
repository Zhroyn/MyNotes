<!-- TOC -->

- [Quoting](#quoting)
- [Array](#array)
- [Parameters](#parameters)
- [Aliases](#aliases)
- [Pattern Matching](#pattern-matching)
- [Conditional Expressions](#conditional-expressions)
- [Compound Commands](#compound-commands)
    - [Looping Constructs](#looping-constructs)
    - [Conditional Constructs](#conditional-constructs)
    - [Grouping Commands](#grouping-commands)
- [Expansions](#expansions)
    - [Brace Expansion](#brace-expansion)
    - [Tilde Expansion](#tilde-expansion)
    - [Shell Parameter Expansion](#shell-parameter-expansion)
    - [Arithmetic Expansion](#arithmetic-expansion)
    - [Command Substitution](#command-substitution)
    - [Process Substitution](#process-substitution)
    - [Word Splitting](#word-splitting)
    - [Filename Expansion](#filename-expansion)
    - [Quote Removal](#quote-removal)
- [Builtin](#builtin)

<!-- /TOC -->



## Quoting
- A non-quoted backslash is the Bash escape character. It preserves the literal value of the next character that follows, with the exception of newline
- Within single quotes, each character preserves its literal value. A single quote may not occur between single quotes, even when preceded by a backslash.
- Within double quotes, the backslash retains its special meaning only when followed by ``$, `, ", \, or newline``.
- Character sequences of the form `$'string'` are treated as a special kind of single quotes. The sequence expands to string, with backslash-escaped characters in string replaced as specified by the ANSI C standard. 



## Array
- An indexed array is created automatically if any variable is assigned to using the syntax `name[subscript]=value`.
- To explicitly declare an indexed array, use `declare -a name` or `declare -a name[subscript]`. The subscript is ignored.
- Associative arrays are created using `declare -A name`. `declare` builtin also accept assignment syntax to initialize.
- Arrays are assigned to using compound assignments of the form `name=(value1 value2 … )` where each value may be of the form `[subscript]=string`. Indexed array assignments do not require anything but `string`. When assigning to indexed arrays, if the optional `subscript` is supplied, that index is assigned to; otherwise the index of the element assigned is the last index assigned to by the statement plus one. Indexing starts at zero.
- When assigning to an associative array, the words in a compound assignment may be either assignment statements, for which the subscript is required, or a list of words that is interpreted as a sequence of alternating keys and values: `name=(key1 value1 key2 value2 … )`. These are treated identically to `name=( [key1]=value1 [key2]=value2 … )`.
  - The first word in the list determines how the remaining words are interpreted.
  - When using key/value pairs, the keys may not be missing or empty; a final missing value is treated like the empty string.
- When assigning to an indexed array, if `name` is subscripted by a negative number, that means counting back from the end of the array, and an index of -1 references the last element.
- If the subscript is `@` or `*`, the word expands to all members of the array name. These subscripts differ only when the word appears within double quotes. If the word is double-quoted, `${name[*]}` expands to a single word with the value of each array member separated by the first character of the IFS variable, and `${name[@]}` expands each element of name to a separate word.






## Parameters
- A parameter is an entity that stores values. A variable is a parameter denoted by a name. A variable has a value and zero or more attributes. Attributes are assigned using the declare builtin command.
- A variable can be assigned the nameref attribute using the -n option to the `declare` or `local` builtin commands to create a nameref, or a reference to another variable.
- Whenever the nameref variable is referenced, assigned to, unset, or has its attributes modified, the operation is actually performed on the variable specified by the nameref variable’s value.


**Positional Parameters**
- A positional parameter is a parameter denoted by one or more digits, other than the single digit 0.
- Positional parameters are assigned from the shell’s arguments when it is invoked, and may be reassigned using the `set` builtin command.
- Positional parameter N may be referenced as `${N}`, or as `$N` when N consists of a single digit.

**Special Parameters**
- `$*` Expands to the positional parameters, starting from one.
- `$@` Expands to the positional parameters, starting from one.
- `$#` Expands to the number of positional parameters in decimal.
- `$?` Expands to the exit status of the most recently executed foreground pipeline.
- `$-` Expands to the current option flags as specified upon invocation, by the set builtin command, or those set by the shell itself (such as the -i option).
- `$$` Expands to the process ID of the shell. In a subshell, it expands to the process ID of the invoking shell, not the subshell.
- `$!` Expands to the process ID of the job most recently placed into the background, whether executed as an asynchronous command or using the bg builtin.
- `$0` Expands to the name of the shell or shell script.





## Aliases
- add a file named `.bash_aliases` to `~`
- add personal aliases to that file
- run `source .bashrc`
```shell
# List all aliases:
alias
# Create a generic alias:
alias word="command"
# View the command associated to a given alias:
alias word
# Remove an aliased command:
unalias word
```



## Pattern Matching
- Any character that appears in a pattern, other than the special pattern characters described below, matches itself.
- A backslash escapes the following character
- A single escaping backslash is discarded when matching.
- `*` Matches any string, including the null string.
- `?` Matches any single character.
- `[…]` Matches any one of the enclosed characters.
  - A pair of characters separated by a hyphen denotes a range expression; any character that falls between those two characters, inclusive, using the current locale’s collating sequence and character set, is matched.
  - If the first character following the `[` is a `!` or a `^` then any character not enclosed is matched.
  - A `-` may be matched by including it as the first or last character in the set.
  - A `]` may be matched by including it as the first character in the set.
  - character classes can be specified using the syntax `[:class:]`, where class is one of the following classes defined in the POSIX standard:
```shell
alnum   alpha   ascii   blank   cntrl   digit   graph   lower
print   punct   space   upper   word    xdigit
```
- a pattern-list is a list of one or more patterns separated by a `|`.
- `?(pattern-list)` Matches zero or one occurrence of the given patterns.
- `*(pattern-list)` Matches zero or more occurrences of the given patterns.
- `+(pattern-list)` Matches one or more occurrences of the given patterns.
- `@(pattern-list)` Matches one of the given patterns.
- `!(pattern-list)` Matches anything except one of the given patterns.







## Conditional Expressions
- Conditional expressions are used by the `[[` keyword and the `test` and `[` builtin commands.
- If true, return 0, otherwise return 1
- The words between the `[[` and `]]` do not undergo word splitting and filename expansion. The shell performs tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, process substitution, and quote removal on those words.

**File**
- `-a file` True if file exists.
- `-b file` True if file exists and is a block special file.
- `-c file` True if file exists and is a character special file.
- `-d file` True if file exists and is a **directory**.
- `-e file` True if file exists.
- `-f file` True if file exists and is a **regular file**.
- `-g file` True if file exists and its set-group-id bit is set.
- `-h file` True if file exists and is a **symbolic link**.
- `-k file` True if file exists and its "sticky" bit is set.
- `-p file` True if file exists and is a named pipe (FIFO).
- `-r file` True if file exists and is **readable**.
- `-s file` True if file exists and has a size greater than zero.
- `-t fd` True if file descriptor fd is open and refers to a terminal.
- `-u file` True if file exists and its set-user-id bit is set.
- `-w file` True if file exists and is **writable**.
- `-x file` True if file exists and is **executable**.
- `-G file` True if file exists and is owned by the effective group id.
- `-L file` True if file exists and is a **symbolic link**.
- `-N file` True if file exists and has been modified since it was last read.
- `-O file` True if file exists and is owned by the effective user id.
- `-S file` True if file exists and is a socket.
- `file1 -ef file2` True if file1 and file2 refer to the same device and inode numbers.
- `file1 -nt file2` True if file1 is newer (according to modification date) than file2, or if file1 exists and file2 does not.
- `file1 -ot file2` True if file1 is older than file2, or if file2 exists and file1 does not.

**Varible**
- `-o optname` True if the shell option optname is enabled.
- `-v varname` True if the shell variable varname is set (has been assigned a value).
- `-R varname` True if the shell variable varname is set and is a name reference.

**String**
- `-z string` True if the length of string is zero.
- `-n string` or `string` True if the length of string is non-zero.
- `string1 == string2` or `string1 = string2` True if the strings are equal.
  - `=` should be used with the test command for POSIX conformance.
- `string1 != string2` True if the strings are not equal.
  - When the `==` and `!=` operators are used between `[[` and `]]`, the string to the right of the operator is considered a pattern. When you use `=~`, the string to the right of the operator is considered a POSIX extended regular expression pattern. The return value is 0 if the string matches (`==` or `~=`) or does not match (`!=`) the pattern, and 1 otherwise.
  - You can quote any part of the pattern to force the quoted portion to be matched literally instead of as a regular expression. If the pattern is stored in a shell variable, quoting the variable expansion forces the entire pattern to be matched literally.
- `string1 < string2` True if string1 sorts before string2 lexicographically.
- `string1 > string2` True if string1 sorts after string2 lexicographically.
  - When used with `[[`, the `<` and `>` operators sort lexicographically using the current locale.
  - When used with `test` or `[`, the `<` and `>` operators sort lexicographically using ASCII ordering.

**Integer**
- `arg1 -eq arg2` True if arg1 is equal to arg2.
- `arg1 -ne arg2` True if arg1 is not equal to arg2.
- `arg1 -lt arg2` True if arg1 is less than arg2.
- `arg1 -le arg2` True if arg1 is less than or equal to arg2.
- `arg1 -gt arg2` True if arg1 is greater than arg2.
- `arg1 -ge arg2` True if arg1 is greater than or equal to arg2.
- Arg1 and arg2 may be positive or negative integers. When used with the `[[` command, Arg1 and Arg2 are evaluated as arithmetic expressions.

**Logical**
- `! expr` True if expr is false.
- `( expr )` Returns the value of expr. This may be used to override the normal precedence of operators.
- `expr1 -a expr2` True if both expr1 and expr2 are true.
- `expr1 -o expr2` True if either expr1 or expr2 is true.








## Compound Commands
#### Looping Constructs
**until**
```shell
until test-commands; do consequent-commands; done
```
- wherever a `;` appears in the description of a command’s syntax, it may be replaced with one or more newlines.
- Execute consequent-commands as long as test-commands has an exit status which is not zero.
- The return status is the exit status of the last command executed in consequent-commands, or zero if none was executed.

**while**
```shell
while test-commands; do consequent-commands; done
```
- Execute consequent-commands as long as test-commands has an exit status of zero.
- The return status is the exit status of the last command executed in consequent-commands, or zero if none was executed.

**for**
```shell
for name [ [in [words …] ] ; ] do commands; done
```
- Expand words, and execute commands once for each member in the resultant list, with name bound to the current member.
- If `in words` is not present, the for command executes the commands once for each positional parameter that is set, as if `in "$@"` had been specified.
- The return status is the exit status of the last command that executes. If there are no items in the expansion of words, no commands are executed, and the return status is zero.

An alternate form of the for command is also supported:
```shell
for (( expr1 ; expr2 ; expr3 )) ; do commands ; done
```
- First, the arithmetic expression expr1 is evaluated according to the rules described below.
- The arithmetic expression expr2 is then evaluated repeatedly until it evaluates to zero.
- Each time expr2 evaluates to a non-zero value, commands are executed and the arithmetic expression expr3 is evaluated.


#### Conditional Constructs
**if**
```shell
if test-commands; then
  consequent-commands;
[elif more-test-commands; then
  more-consequents;]
[else alternate-consequents;]
fi
```
- The test-commands list is executed, and if its return status is zero, the consequent-commands list is executed.
- If the test-commands are arithmetic expression, `((...))` return 1 if the evaluation is 0, otherwise return 0; for `let`, if the last `ARG` evaluates to 0, `let` returns 1, otherwise return 0.

**case**
```shell
case word in
    [ [(] pattern [| pattern]…) command-list ;;]…
esac
```
- Selectively execute the command-list corresponding to the first pattern that matches word.
- `|` is used to separate multiple patterns, and `)` operator terminates a pattern list.
- A list of patterns and an associated command-list is known as a clause. Each clause must be terminated with `;;`, `;&`, or `;;&`.
- The word undergoes tilde expansion, parameter expansion, command substitution, arithmetic expansion, and quote removal before matching is attempted.
- Each pattern undergoes tilde expansion, parameter expansion, command substitution, arithmetic expansion, process substitution, and quote removal.
- an Example:
```shell
echo -n "Enter the name of an animal: "
read ANIMAL
echo -n "The $ANIMAL has "
case $ANIMAL in
  horse | dog | cat) echo -n "four";;
  man | kangaroo ) echo -n "two";;
  *) echo -n "an unknown number of";;
esac
echo " legs."
```

**select**
```shell
select name [in words …]; do commands; done
```
- The list of words following in is expanded, generating a list of items, and the set of expanded words is printed on the standard error output stream, each preceded by a number.
- If the `in words` is omitted, the positional parameters are printed, as if `in "$@"` had been specified.
- `select` then displays the PS3 prompt and reads a line from the standard input.
- If the line consists of a number corresponding to one of the displayed words, then the value of name is set to that word.
- If the line is empty, the words and prompt are displayed again.
- If EOF is read, the select command completes and returns 1.
- Any other value read causes name to be set to null.
- The line read is saved in the variable REPLY.
- an Example:
```shell
select fname in *
do
	echo you picked $fname \($REPLY\)
	break
done
```

#### Grouping Commands

**( *list* )**
- Placing a list of commands between parentheses forces the shell to create a subshell, and each of the commands in list is executed in that subshell environment.
- The parentheses are operators, and are recognized as separate tokens by the shell even if they are not separated from the list by whitespace.

**{ *list;* }**
- Placing a list of commands between curly braces causes the list to be executed in the current shell context. No subshell is created.
- The semicolon (or newline) following list is required.
- The braces are reserved words, so they must be separated from the list by blanks or other shell metacharacters.







## Expansions
- The order of expansions is:
  - brace expansion
  - tilde expansion
  - parameter and variable expansion
  - arithmetic expansion
  - command substitution (done in a left-to-right fashion)
  - word splitting
  - filename expansion
- On systems that can support it, there is an additional expansion available: process substitution. This is performed at the same time as tilde, parameter, variable, and arithmetic expansion and command substitution.
- After all expansions, quote removal is performed.

#### Brace Expansion
- Brace expansions may be nested.
- Patterns to be brace expanded take the form of either a series of comma-separated strings or a sequence expression between a pair of braces.
- A sequence expression takes the form `{x..y[..incr]}`, where x and y are either integers or letters, and incr, an optional increment, is an integer.
- both x and y must be of the same type (integer or letter).
- When either x or y begins with a zero, the shell attempts to force all generated integers to contain the same number of digits, zero-padding where necessary.
- The default increment is 1 or -1 as appropriate.
- If the generated list is ascending, but incr is negative, the increment is actually positive.
- If incr is 0, then the increment is actually 1 or -1.

#### Tilde Expansion
- If a word begins with an unquoted tilde character (`~`), all of the characters up to the first unquoted slash (or all characters, if there is no unquoted slash) are considered a tilde-prefix.
- Each variable assignment is checked for unquoted tilde-prefixes immediately following a `:` or the first `=`. In these cases, tilde expansion is also performed.
- If none of the characters in the tilde-prefix are quoted, the characters in the tilde-prefix following the tilde are treated as a possible login name.
- The tilde is replaced with the home directory of the specified login name, or the home directory of the user executing the shell if the login name is a null string.
- If the tilde-prefix is `~+`, the value of the shell variable `PWD` replaces the tilde-prefix.
- If the tilde-prefix is `~-`, the value of the shell variable `OLDPWD`, if it is set, is substituted.
- If the tilde-prefix is `~+N` or `~-N`, the corresponding element from the directory stack is substituted, which is the string that would be displayed by `dirs +N` or `dirs -N`. If the tilde-prefix consists of a number without a leading `+` or `-`, `+` is assumed.

#### Shell Parameter Expansion
- The basic form of parameter expansion is `$parameter` or `${parameter}`. The value of parameter is substituted. The braces are required when parameter is a positional parameter with more than one digit, or when parameter is followed by a character that is not to be interpreted as part of its name.
- The only times a variable appears "naked" -- without the `$` prefix -- is when declared or assigned, when unset, when exported, in an arithmetic expression within double parentheses `(( ... ))`, or in the special case of a variable representing a signal
- If the first character of parameter is `!`, Bash would use the value formed by expanding the rest of parameter as the new parameter, which is known as indirect expansion. The value is subject to tilde expansion, parameter expansion, command substitution, and arithmetic expansion. Indirect expansion is not recursive.
<br>

- `${parameter:-word}` If parameter is unset or null, the expansion of word is substituted. Otherwise, the value of parameter is substituted.
- `${parameter:=word}` If parameter is unset or null, the expansion of word is assigned to parameter. The value of parameter is then substituted.
- `${parameter:?word}` If parameter is null or unset, the expansion of word is written to the standard error and the shell. Otherwise, the value of parameter is substituted.
- `${parameter:+word}` If parameter is null or unset, nothing is substituted, otherwise the expansion of word is substituted.
<br>

- `${parameter:offset[:length]}`
  - This is referred to as Substring Expansion. It expands to up to length characters of the value of parameter starting at the character specified by offset (Substring indexing is zero-based). If length is omitted, it expands to the end of the value.
  - length and offset are arithmetic expressions.
  - If offset evaluates to a number less than zero, the value is used as an offset in characters from the end of the value of parameter.
  - If length evaluates to a number less than zero, it is interpreted as an offset in characters from the end of the value of parameter rather than a number of characters, and the expansion is the characters between offset and that result.
  - a negative offset must be separated from the colon by at least one space to avoid being confused with the `:-` expansion.
- `${#parameter}` The length of the expanded value of parameter is substituted.
- `${parameter#word}` or `${parameter##word}` If the pattern produced from expaned word matches the **beginning** of the expanded value of parameter, then the shortest matching pattern (the `#` case) or the longest matching pattern (the `##` case) will be deleted.
- `${parameter%word}` or `${parameter%%word}` If the pattern produced from expaned word matches the **trailing portion** of the expanded value of parameter, then the shortest matching pattern (the `%` case) or the longest matching pattern (the `%%` case) will be deleted.
<br>

- `${parameter/pattern/string}`
- `${parameter//pattern/string}`
- `${parameter/#pattern/string}`
- `${parameter/%pattern/string}`
  - Parameter is expanded and the longest match of pattern against its value is replaced with string.
  - `pattern` undergoes filename expansion.
  - `string` undergoes tilde expansion, parameter and variable expansion, arithmetic expansion, command and process substitution, and quote removal.
  - In the first form above, only the first match is replaced.
  - In the second form above, all matches of pattern are replaced.
  - In the third form above, it must match at the beginning of the expanded value of parameter.
  - In the fourth form above, it must match at the end of the expanded value of parameter.
  - If string is null, matches of pattern are deleted and the `/` following pattern may be omitted.
- `${parameter^pattern}`
- `${parameter^^pattern}`
- `${parameter,pattern}`
- `${parameter,,pattern}`
  - The pattern is expanded to produce a pattern just as in filename expansion. The pattern should not attempt to match more than one character.
  - `^` converts lowercase to uppercase; `,` converts matching uppercase to lowercase.
  - The `^^` and `,,` expansions convert each matched character in the expanded value; the `^` and `,` expansions match and convert only the first character in the expanded value.
  - If pattern is omitted, it is treated like a `?`, which matches every character.
<br>

- `${parameter@operator}`
  - `U` The expansion is a string that is the value of parameter with lowercase alphabetic characters converted to uppercase.
  - `u` The expansion is a string that is the value of parameter with the first character converted to uppercase, if it is alphabetic.
  - `L` The expansion is a string that is the value of parameter with uppercase alphabetic characters converted to lowercase.
  - `Q` The expansion is a string that is the value of parameter quoted in a format that can be reused as input.
  - `E` The expansion is a string that is the value of parameter with backslash escape sequences expanded as with the $'…' quoting mechanism.
  - `P` The expansion is a string that is the result of expanding the value of parameter as if it were a prompt string (see Controlling the Prompt).
  - `A` The expansion is a string in the form of an assignment statement or declare command that, if evaluated, will recreate parameter with its attributes and value.
  - `K` Produces a possibly-quoted version of the value of parameter, except that it prints the values of indexed and associative arrays as a sequence of quoted key-value pairs (see Arrays).
  - `a` The expansion is a string consisting of flag values representing parameter’s attributes.
  - `k` Like the `K` transformation, but expands the keys and values of indexed and associative arrays to separate words after word splitting.

#### Arithmetic Expansion
```shell
$(( expression ))
```
- All tokens in the expression undergo parameter and variable expansion, command substitution, and quote removal. The result is treated as the arithmetic expression to be evaluated.
- Arithmetic expansions may be nested.

#### Command Substitution
```shell
$(command)
`command`
```
- Bash performs the expansion by executing command in a subshell environment and replacing the command substitution with the standard output of the command, with any trailing newlines deleted.
- Embedded newlines are not deleted, but they may be removed during word splitting.
- The command substitution `$(cat file)` can be replaced by the equivalent but faster `$(< file)`.

#### Process Substitution
- Process substitution allows a process’s input or output to be referred to using a filename. This filename is passed as an argument to the current command as the result of the expansion.
- `>(list)` Writing to the file will provide input for list.
- `<(list)` The file passed as an argument should be read to obtain the output of list.

#### Word Splitting
- The shell scans the results of parameter expansion, command substitution, and arithmetic expansion that did not occur within double quotes for word splitting.
- The shell treats each character of `$IFS` as a delimiter, and splits the results of the other expansions into words using these characters as field terminators.
- If `IFS` is unset, or its value is exactly `<space><tab><newline>`, the default, then sequences of `<space>`, `<tab>`, and `<newline>` at the beginning and end of the results of the previous expansions are ignored, and any sequence of IFS characters not at the beginning or end serves to delimit words.
- Explicit null arguments ("" or '') are retained and passed to commands as empty strings. Unquoted implicit null arguments, resulting from the expansion of parameters that have no values, are removed. If a parameter with no value is expanded within double quotes, a null argument results and is retained and passed to a command as an empty string. When a quoted null argument appears as part of a word whose expansion is non-null, the null argument is removed.

#### Filename Expansion
- After word splitting, unless the `-f` option has been set, Bash scans each word for the characters `*`, `?`, and `[`. If one of these characters appears, and is not quoted, then the word is regarded as a pattern, and replaced with an alphabetically sorted list of filenames matching the pattern.
- When a pattern is used for filename expansion, the character `.` at the start of a filename or immediately following a slash must be matched explicitly, unless the shell option `dotglob` is set.
- When matching a filename, the slash character must always be matched explicitly by a slash in the pattern.

#### Quote Removal
After the preceding expansions, all unquoted occurrences of the characters `\`, `'`, and `"` that did not result from one of the above expansions are removed.






## Builtin




