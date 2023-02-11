<!-- TOC -->

- [Cheatsheet](#cheatsheet)
- [Reference](#reference)
  - [conda info](#conda-info)
  - [conda list](#conda-list)
- [Source](#source)

<!-- /TOC -->

## Cheatsheet

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

