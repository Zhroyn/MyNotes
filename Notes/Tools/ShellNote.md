[toc]



## Syntax
#### Quoting
- A non-quoted backslash is the Bash escape character. It preserves the literal value of the next character that follows, with the exception of newline
- Within single quotes, each character preserves its literal value. A single quote may not occur between single quotes, even when preceded by a backslash.
- Within double quotes, the backslash retains its special meaning only when followed by ``$, `, ", \, or newline``.
- Character sequences of the form `$'string'` are treated as a special kind of single quotes. The sequence expands to string, with backslash-escaped characters in string replaced as specified by the ANSI C standard. 


#### Variable and Substitution
```shell
$PATH   #environment variable
$PWD    #Print working directory
$0      #Name of the script
$1 - $9 #Arguments to the script. $1 is the first argument and so on.
$@      #All the arguments
$#      #Number of arguments
$?      #Return code of the previous command
$$      #Process identification number (PID) for the current script
$_      #Last argument from the last command
!!      #Entire last command, including arguments

${variable} #variable substitution
$(command)  #command substitution
<(command) or >(command)    #process substitution
#place input or output in a temporary file, and
#its filename is passed as an argument to the current command
```

#### Control Flow
**if**
```shell
if [ expression ];then     #the whitespace are necessary
    statement
elif [ expression ];then
    statement
else
    statement
fi

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
**for**
```shell
for var in list
do
    commands
done
```
**while**
```shell
while conditon
do
    statement
done
```





## Files and Directory
#### mv, cp, rm
**mv**
```shell
# Move or rename files and directories

# Move a file or files to an arbitrary location
mv source ... target
# Prompt for confirmation before overwriting existing files
mv -i source target
# Do not prompt for confirmation before overwriting existing files
mv -f source target
# Do not overwrite an existing file
mv -n source target
# Move files in verbose mode, showing files after they are moved
mv -v source target
```
**cp**
```shell
# Copy files and directories
# will overwrite target if existed
# will report error if trying to overwrite source itself

# Copy a file to another location
cp path/to/source_file.ext path/to/target_file.ext
# Copy a file into another directory, keeping the filename
cp path/to/source_file.ext path/to/target_parent_directory

# Recursively copy a directory's contents to another location 
# if the destination exists, the directory is copied inside it
cp -r path/to/source_directory path/to/target_directory
```
**rm**
```shell
# Remove a file or files from arbitrary locations
rm path/to/file ...
# Recursively remove a directory and all its subdirectories
rm -r path/to/directory
# Forcibly remove a directory, without prompting
rm -rf path/to/directory
# Remove files in verbose mode, printing a message for each removed file
rm -v path/to/directory/*
```
#### ls, mkdir, touch, chmod
**ls**
```shell
ls -1   # List files one per line
ls -a   # List all files, including hidden files
ls -F   # List all files, with trailing / added to directory names
ls -R   # List subdirectories recursively

-l      #use a long listing format
-t      #sort by modification time, newest first
-S      #sort by file size, largest first
-X      #sort alphabetically by entry extension
-r      #reverse order while sorting
```
**mkdir**
```shell
# Create multiple directories in the current directory
mkdir directory_1 directory_2 ...
# Create directories recursively (useful for creating nested dirs)
mkdir -p path/to/directory
```
**touch**
```shell
# Change a file access and modification times

# Create a new empty file(s) or change the times to current time:
touch path/to/file{1,2,3}.txt
# Set the times on a file to a specific date and time:
touch -t YYYYMMDDHHMM.SS path/to/file
# Set the time on a file to one hour in the past:
touch -d "-1 hour" path/to/file
# Use the times from a file to set the times on a second file:
touch -r path/to/file1 path/to/file2
```
**chmod**
```shell
# Change the access permissions of a file or directory.

# Give the [u]ser who owns a file the right to e[x]ecute it:
chmod u+x path/to/file
# Give the [u]ser rights to [r]ead and [w]rite to a file/directory:
chmod u+rw path/to/file_or_directory
# Remove e[x]ecutable rights from the [g]roup:
chmod g-x path/to/file
# Give [a]ll users rights to [r]ead and e[x]ecute:
chmod a+rx path/to/file
```





## Print like
#### echo, cat, tee
**echo**
```shell
# Print a message with environment variables, must with double quotation marks
echo "My path is $PATH"
# Append a message to the file
echo "Hello World" >> file.txt
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
#### cut, head, tail
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
#### wc
**wc**
```shell
# Print newline, word, and byte counts for each FILE
wc -l/--lines path/to/file
wc -w/--words path/to/file
wc -c/--bytes path/to/file
wc -m/--chars path/to/file
```





## Data Wrangling
#### sort
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
#### uniq
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
#### find
```shell
# Find files by extension:
find root_path -name '*.ext'
# Find files matching multiple path/name patterns:
find root_path -path '**/path/**/*.ext' -or -name '*pattern*'
# Find directories matching a given name, in case-insensitive mode:
find root_path -type d -iname '*lib*'
# Find files matching a given pattern, excluding specific paths:
find root_path -name '*.py' -not -path '*/site-packages/*'
# Find files matching a given size range, limiting the recursive depth to "1":
find root_path -maxdepth 1 -size +500k -size -10M
# Delete all files with .tmp extension
find root_path -name '*.tmp' -exec rm {} \;
```

#### grep
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


#### sed
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

#### awk
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






## Info
#### date
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
#### which
```shell
# Locate a program in the user's path
which which             # >>> /usr/bin/which
```
#### who
```shell
# Print information about users who are currently logged in

# Display the username, line, and time of all currently logged-in sessions:
who
# Display information only for the current terminal session:
who am i
# Display all available information:
who -a
```
#### ps
```shell
# Information about running processes.

# List all running processes:
ps aux
# List all running processes including the full command string:
ps auxww
# Sort processes by memory consumption:
ps --sort size
```






## Other Programs
#### curl
```shell
# Transfers data from or to a server.
# Supports most protocols, including HTTP, FTP, and POP3

# Send GET request to get link content to standard output
curl http://example.com
# Only show the head of HTTP
curl -I/--head http://example.com
# Download the contents of a URL to a file:
curl http://example.com -o/--output filename
# Download a file, saving the output under the filename indicated by the URL:
curl -O/--remote-name http://example.com/filename
```
#### xargs
```shell
# Delete all files with a .backup extension
# -print0 uses a null character to split file names, and -0 uses it as delimiter
find . -name '*.backup' -print0 | xargs -0 rm -v
```
#### tar
```shell
-c, --create #create a new archive.Directories are archived recursively
-r, --append #append files to the end of an archive(uncompressed)
--delete     #delete MEMBERS from the archive(uncompressed)
-A, --catenate, --concatenate #append archive to the end of another archive
-a, --auto-compress #use archive suffix to determine the compression program

# [c]reate an archive and write it to a [f]ile:
tar cf target.tar file1 file2 file3
# [c]reate a g[z]ipped archive and write it to a [f]ile:
tar czf target.tar.gz file1 file2 file3
# [c]reate a g[z]ipped archive from another directory:
tar czf target.tar.gz --directory=path/to/directory .
# E[x]tract a (compressed) archive [f]ile [v]erbosely:
tar xvf source.tar[.gz|.bz2|.xz]
# E[x]tract a (compressed) archive [f]ile into the target directory:
tar xf source.tar[.gz|.bz2|.xz] --directory=directory
# Lis[t] the contents of a tar [f]ile:
tar tf source.tar
# E[x]tract files matching a pattern from an archive [f]ile:
tar xf source.tar --wildcards "*.html"
```




## Packages
#### apt
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






## Configuration
#### Mirror Source(Ubuntu20.04)
```shell
sudo vim /etc/apt/source.list
sudo apt update
sudo apt upgrade

清华源
# 默认注释了源码镜像以提高 apt update 速度
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse

阿里源
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse

中科大源
deb https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse

网易163源
deb http://mirrors.163.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ focal-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ focal-backports main restricted universe multiverse
```