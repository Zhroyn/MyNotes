<!-- TOC -->

- [Cheatsheet](#cheatsheet)
  - [Environment](#environment)
  - [Package](#package)
  - [Specifying version numbers](#specifying-version-numbers)
- [Reference](#reference)
  - [conda info](#conda-info)
  - [conda list](#conda-list)
- [Source](#source)

<!-- /TOC -->

## Cheatsheet
### Environment
- `conda create -n/--name ENVIRNMENT [package_spec...]` Create a new envirenment with the specified packages
- `conda create -n/--name ENVIRNMENT --clone ENV` Create a new environment as a copy of an existing local environment
- `conda create -n/--name ENVIRNMENT --file FILE` Read package versions from the given file
<br>

- `conda info -e/--envs` or `conda env list` List all environments
- `conda list --explicit > FILE` or `conda list -e/--export > FILE` Save the current environment to a file, or another by adding `-n ENV`
<br>

- `conda activate ENV` Activate the new environment to use it
- `conda deactivate` Deactivate the current environment
<br>

- `conda env remove -n/--name ENV` Delete an environment and everything in it

### Package
- `conda install [-n ENV] package_spec...` Install a list of packages into the environment
- `conda update [-n ENV] package_spec...` Update a list of packages in the environment
- `conda update [-n ENV] --all/--update-all` Update all installed packages in the environment
- `conda remove [-n ENV] package_spec...` Delete a list of packages in the environment
<br>

- `conda list [-n ENV]` List all packages installed in the environment, including versions and channels
- `conda list REGEX` List only packages matching this regular expression
- `conda search REGEX` Search for a package

### Specifying version numbers
- `numpy=1.11` means `1.11.0`, `1.11.1`, `1.11.2`, `1.11.18` etc
- `numpy==1.11` means `1.11.0` exactly
- `numpy>=1.11` means `1.11.0` or higher
- `numpy=1.11.1|1.11.3` means `1.11.1`, `1.11.3`
- `numpy>=1.8,<2` means `1.8`, `1.9`, not `2.0`





## Reference
### conda info
```shell
usage: conda info [-h] [--json] [-v] [-q] [-a] [--base] [-e] [-s] [--unsafe-channels]
Display information about current conda install.

Options:

optional arguments:
  -h, --help         Show this help message and exit.
  -a, --all          Show all information.
  --base             Display base environment path.
  -e, --envs         List all known conda environments.
  -s, --system       List environment variables.
  --unsafe-channels  Display list of channels with tokens exposed.

Output, Prompt, and Flow Control Options:
  --json             Report all output as json. Suitable for using conda programmatically.
  -v, --verbose      Use once for info, twice for debug, three times for trace.
  -q, --quiet        Do not display progress bar.
```

### conda list
```shell
usage: conda-script.py list [-h] [-n ENVIRONMENT | -p PATH] [--json] [-v] [-q] [--show-channel-urls] [-c] [-f] [--explicit] [--md5] [-e] [-r] [--no-pip] [regex]
List installed packages in a conda environment.

Options:

positional arguments:
  regex                 List only packages matching this regular expression.

optional arguments:
  -h, --help            Show this help message and exit.
  --show-channel-urls   Show channel urls. Overrides the value given by `conda config --show show_channel_urls`.
  -c, --canonical       Output canonical names of packages only.
  -f, --full-name       Only search for full names, i.e., ^<regex>$. --full-name NAME is identical to regex '^NAME$'.
  --explicit            List explicitly all installed conda packages with URL (output may be used by conda create --file).
  --md5                 Add MD5 hashsum when using --explicit.
  -e, --export          Output explicit, machine-readable requirement strings instead of human-readable lists of packages. This output may be used by conda create
                        --file.
  -r, --revisions       List the revision history.
  --no-pip              Do not include pip-only installed packages.

Target Environment Specification:
  -n ENVIRONMENT, --name ENVIRONMENT
                        Name of environment.
  -p PATH, --prefix PATH
                        Full path to environment location (i.e. prefix).

Output, Prompt, and Flow Control Options:
  --json                Report all output as json. Suitable for using conda programmatically.
  -v, --verbose         Use once for info, twice for debug, three times for trace.
  -q, --quiet           Do not display progress bar.
```


## Source
**Tsinghua**
```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```
**USTC**
```shell
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
conda config --set show_channel_urls yes
```
**Revert to default source**
```shell
conda config --remove-key channels
```

