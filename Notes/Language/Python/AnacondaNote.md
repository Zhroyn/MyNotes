<!-- TOC -->

- [Environment](#environment)
  - [Create environment](#create-environment)
  - [Remove environment](#remove-environment)
  - [List environments](#list-environments)
  - [Save environment](#save-environment)
  - [Activate environment](#activate-environment)
  - [Rename environment](#rename-environment)
- [Package](#package)
  - [Install package](#install-package)
  - [Remove package](#remove-package)
  - [Update package](#update-package)
  - [List packages](#list-packages)
  - [Search package](#search-package)
- [Version Control](#version-control)
  - [Specify version](#specify-version)
  - [Version downgrade](#version-downgrade)
  - [Version rollback](#version-rollback)
- [Source](#source)

<!-- /TOC -->





### Environment
#### Create environment
- `conda create -n/--name ENVIRNMENT [package_spec...]` Create a new envirenment with the specified packages
- `conda create -n/--name ENVIRNMENT --clone ENV` Create a new environment as a copy of an existing local environment
- `conda create -n/--name ENVIRNMENT --file FILE` Read package versions from the given file

#### Remove environment
- `conda env remove -n/--name ENV` Delete an environment and everything in it

#### List environments
- `conda info -e/--envs` or `conda env list` List all environments

#### Save environment
- `conda list --explicit > FILE` or `conda list -e/--export > FILE` Save the current environment to a file, or another by adding `-n ENV`

#### Activate environment
- `conda activate ENV` Activate the new environment to use it
- `conda deactivate` Deactivate the current environment

#### Rename environment
- `conda create -n/--name NEWENV --clone OLDENV`
- `conda env remove -n\--name OLDENV`








### Package
#### Install package
- `conda install [-n ENV] package_spec...` Install a list of packages into the environment
- `conda install package_spec -c/--channel CHANNEL` Use additional channel to search for packages. These are URLs or pathes
- `conda install --use-local PATH` Use locally built packages. Identical to `-c local`

#### Remove package
- `conda remove [-n ENV] package_spec...` Delete a list of packages in the environment

#### Update package
- `conda update [-n ENV] package_spec...` Update a list of packages in the environment
- `conda update [-n ENV] --all/--update-all` Update all installed packages in the environment

#### List packages
- `conda list [-n ENV]` List all packages installed in the environment, including versions and channels
- `conda list REGEX` List only packages matching this regular expression

#### Search package
- `conda search REGEX` Search for a package








### Version Control
#### Specify version
- `numpy=1.11` means `1.11.0`, `1.11.1`, `1.11.2`, `1.11.18` etc
- `numpy==1.11` means `1.11.0` exactly
- `numpy>=1.11` means `1.11.0` or higher
- `numpy=1.11.1|1.11.3` means `1.11.1`, `1.11.3`
- `numpy>=1.8,<2` means `1.8`, `1.9`, not `2.0`

#### Version downgrade
- `conda install package_spec=...` Downgrade the package to the specified version

#### Version rollback
- `conda list -r/--revisions` List the revision history
- `conda install --revision REVISION` Revert to the specified REVISION








### Source
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

