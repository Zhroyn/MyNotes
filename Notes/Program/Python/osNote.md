[toc]


### Datas
```py
os.path     # either posixpath or ntpath
os.name     # either 'posix' or 'nt'
os.environ  # environment varibles

os.curdir   # a string representing the current directory (always '.')
os.pardir   # a string representing the parent directory (always '..')

os.sep      # the (or a most common) pathname separator ('/' or '\\')
os.extsep   # the extension separator (always '.')
os.altsep   # the alternate pathname separator (None or '/')
os.pathsep  # the component separator used in $PATH etc (maybe ';')
os.linesep  # the line separator in text files ('\r' or '\n' or '\r\n')

os.defpath  # the default search path for executables ('.;C:\bin', etc.)
os.devnull  # the file path of the null device ('nul', etc.)
```

### Functions
#### Paths
```py
# Change the current working directory to the specified path.
chdir(path)

# Return a unicode string representing the current working directory.
getcwd()
# Return a list containing the names of the files in the directory.
listdir(path=None)
If path is None, uses the path='.'.
# Directory tree generator.
walk(top, topdown=True, onerror=None, followlinks=False)
For each directory in the directory tree rooted at top (including top
itself, but excluding '.' and '..'), yields a 3-tuple
    dirpath, dirnames, filenames

# Create a directory.
mkdir(path, mode=511, *, dir_fd=None)
# Create a leaf directory and all intermediate ones.
makedirs(name)


for root, dirs, files in os.walk('python/Lib/email'):
    print(root, "consumes ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
```

#### Files
```py
# Remove a file (same as unlink()).
remove(path, *, dir_fd=None)
# Remove a directory.
rmdir(path, *, dir_fd=None)
# Remove a leaf directory and all empty intermediate ones.
removedirs(name)
# Remove a file (same as remove()).
unlink(path, *, dir_fd=None)

# Rename a file or directory.
rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
# Create directories as necessary and delete any left empty.
renames(old, new)
# Rename a file or directory, overwriting the destination.
replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
```
```py
# Use the real uid/gid to test for access to a path.
access(path, mode)
    os.F_OK : Exist
    os.R_OK : Readable
    os.W_OK : Writeable
    os.X_OK : Executable

# Change the access permissions of a file.
chmod(path, mode)
    stat.S_IREAD : Read by owner.
    stat.S_IWRITE : Write by owner.
    stat.S_IEXEC : Execute by owner.
    stat.S_IRUSR : Read by owner
    stat.S_IWUSR : Write by owner.
    stat.S_IXUSR : Execute by owner.
    stat.S_IRWXU : Read, write, and execute by owner

    stat.S_IRGRP : Read by group
    stat.S_IWGRP : Write by group
    stat.S_IXGRP : Execute by group
    stat.S_IRWXG : Read, write, and execute by group

    stat.S_IROTH : Read by others
    stat.S_IWOTH : Write by others
    stat.S_IXOTH : Execute by others
    stat.S_IRWXO : Read, write, and execute by others.


# Create a hard link to a file.
link(src, dst)
# Create a symbolic link pointing to src named dst.
symlink(src, dst, target_is_directory=False)
```


#### Pipes
```py
# Return the result of the cmd
popen(cmd, mode='r', buffering=-1)

# Execute the command in a subshell. Return 0, 1, or 2.
system(command)
```



## Modules
#### os.path
```py
# Return the absolute version of a path.
abspath(path)
# Returns the final component of a pathname
basename(p)
# Returns the directory component of a pathname
dirname(p)

# Given a sequence of path names, returns the longest common sub-path.
commonpath(paths)
# Given a list of pathnames, returns the longest common leading component
commonprefix(m)

# Test whether a path exists.  Returns False for broken symbolic links
exists(path)
# Test whether a path is absolute
isabs(s)
# Return true if the pathname refers to an existing directory.
isdir(s)
# Test whether a path is a regular file
isfile(path)
# Test whether a path is a symbolic link.
islink(path)

# Join paths, just simply concatenate
join(path, *paths)
# Split a pathname.
split(p)
Return tuple (head, tail) where tail is everything after the final slash.
Either part may be empty.
# Split the extension from a pathname.
splitext(p)
Extension is everything from the last dot to the end, ignoring
leading dots.  Returns "(root, ext)"; ext may be empty.
```

