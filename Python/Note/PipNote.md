[toc]



### Pip
```shell
-m mod  #run library module as a script

# Updata pip
Windows: python -m pip install --upgrade pip
Linux: pip install --upgrade pip
# Uninstall pip
python -m pip uninstall pip
# Show help
pip -h/--help
# Show version and exit
pip -V/--version
```

### Packages
```shell
install     # Install packages.
download    # Download packages.
uninstall   # Uninstall packages.
freeze      # Output installed packages in requirements format.
inspect     # Inspect the python environment.
list        # List installed packages.
show        # Show information about installed packages.
check       # Verify installed packages have compatible dependencies.
config      # Manage local and global configuration.
search      # Search PyPI for packages.
index       # Inspect information available from package indexes.
help        # Show help for commands.

# Install packages
pip install [package]...
# Install specified version of package
pip install [package]==version
# Upgrade all specified packages to the newest available version
pip install -U/--upgrade [package]...
# Uninstall packages
pip uninstall [packname]...

# List installed packages
pip list
# List outdated packages
pip list -o/--outdated
# List uptodate packages
pip list -u/--uptodate
# Restrict to the specified installation path for listing packages
pip list --path PATH

# Show information about specified packages
pip show [package]...
# Show more information, and can be used up to 3 times
pip show -v/--verbose [packages]...
# Show the full list of installed files for each package
pip show -f/--files [package]...
```

### Mirror Source
```shell
# Check mirror source config
pip config list

# Base URL of the Python Package Index (default https://pypi.org/simple)
pip install -i/--index-url <url> [package]... 

# Change PyPI source
pip config set global.index-url <url>
##### https://pypi.tuna.tsinghua.edu.cn/simple/
##### https://pypi.mirrors.ustc.edu.cn/simple/
##### http://mirrors.aliyun.com/pypi/simple/
```