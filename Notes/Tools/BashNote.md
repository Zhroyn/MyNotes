<!-- TOC -->

- [Quoting](#quoting)
        - [Variable and Substitution](#variable-and-substitution)
- [Aliases](#aliases)
- [Compound Commands](#compound-commands)
        - [Looping Constructs](#looping-constructs)
        - [Conditional Constructs](#conditional-constructs)
        - [Grouping Commands](#grouping-commands)
- [Expansions](#expansions)
        - [Brace Expansion](#brace-expansion)
        - [Tilde Expansion](#tilde-expansion)
        - [Shell Parameter Expansion](#shell-parameter-expansion)

<!-- /TOC -->



## Quoting
- A non-quoted backslash is the Bash escape character. It preserves the literal value of the next character that follows, with the exception of newline
- Within single quotes, each character preserves its literal value. A single quote may not occur between single quotes, even when preceded by a backslash.
- Within double quotes, the backslash retains its special meaning only when followed by ``$, `, ", \, or newline``.
- Character sequences of the form `$'string'` are treated as a special kind of single quotes. The sequence expands to string, with backslash-escaped characters in string replaced as specified by the ANSI C standard. 


#### Variable and Substitution
**Built-in varibles**
```shell
$PATH   #environment variable
$PWD    #Print working directory
$0      #Name of the script
$1 - $9 #Arguments to the script. $1 is the first argument and so on.
$@      #All the arguments
$#      #Number of arguments
$?      #Return code of the previous command
$!      #Return the pid of the last backgrounded job 
$$      #Process identification number (PID) for the current script
$_      #Last argument from the last command
!!      #Entire last command, including arguments
```




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




## Compound Commands
- wherever a `;` appears in the description of a command’s syntax, it may be replaced with one or more newlines.
```shell
#the whitespace are necessary

File Comparision
[ -e FILE ] #FILE exists
[ -d FILE ] #FILE exists and is a directory
[ -f FILE ] #FILE exists and is a regular file
[ -r FILE ] #FILE exists and read permission is granted
[ -w FILE ] #FILE exists and write permission is granted
[ -x FILE ] #FILE exists and execute permission is granted

String Comparison
[ -z STRING ]   #true if strlen is zero
[ -n STRING ]   #ture if strlen is nonzero
[ STRING ]　    #ture if strlen is nonzero
[ STRING1 == STRING2 ]  #ture if equal
[ STRING1 != STRING2 ]  #true if not equal
[ STRING1 < STRING2 ]   #true if STRING1 is ahead of STRING2
[ STRING1 > STRING2 ]   #true if STRING1 is behind of STRING2

Integer Comparison
[ INT1 -eq INT2 ], [ INT1 -ne INT2 ]
[ INT1 -gt INT2 ], [ INT1 -ge INT2 ]
[ INT1 -lt INT2 ], [ INT1 -le INT2 ]

Conditional Evaluation
[ ! EXPR ]
[ EXPR1 -a EXPR2 ], [ ] && [ ]
[ EXPR1 -o EXPR2 ], [ ] || [ ]
```
#### Looping Constructs
**until**
```shell
until test-commands; do consequent-commands; done
```
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

**Variable substitution**
- The only times a variable appears "naked" -- without the `$` prefix -- is when declared or assigned, when unset, when exported, in an arithmetic expression within double parentheses `(( ... ))`, or in the special case of a variable representing a signal
- Assignment may be with an `=` (as in `var1=27`), in a read statement, and at the head of a loop (`for var2 in 1 2 3`)`.
- `${var:-value}` If `var` is not-set (or null) then the value is substituted for `var`.
- `${var:+value}` If `var` is set then the value is substituted for `var`
- `${var:=value}` If `var` is not-set (or null), then it is set to value.
- `${var:?message}`	If `var` is not-set (or null) then the message is printed as standard error.
- `${var#pattern}` delete from the left to the first matched pattern
- `${var##pattern}` delete from the left to the last matched pattern
- `${var%pattern}` delete from the right to the first matched pattern
- `${var%%pattern}` delete from the right to the last matched pattern
- `${var/pattern/new}` substitute the first matched string from the left
- `${var//pattern/new}` substitute all the matched string from the left
```shell
var='abc.123.abc.123'
$ echo ${var#*.}
123.abc.123
$ echo ${var##*.*}

$ echo ${var%%.*}
abc
$ echo ${var//./:}
abc:123:abc:123
```
**Command substitution and Process substitution**
```shell
$(command)

<(command) or >(command)
Place input or output in a temporary file, and its filename is passed 
as an argument to the current command
```


