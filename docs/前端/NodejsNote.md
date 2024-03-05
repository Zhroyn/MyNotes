
## 安装包

### 全局安装
- `npm install <pageName> -g`
- `npm root -g` 查看全局包的安装目录
- `npm list -g --depth 0` 查看全局安装过的包


### 本地安装
- `npm install <pageName>`




<br>

## 镜像源

若要查看当前镜像源，可以使用：

```shell
npm config get registry
```

若要设置镜像源，可以使用：

```shell
# 官方原始镜像
npm config set registry https://registry.npmjs.org/

# 淘宝镜像
npm config set registry https://registry.npmmirror.com/

# 阿里云镜像
npm config set registry https://npm.aliyun.com/

# 华为云镜像
npm config set registry https://mirrors.huaweicloud.com/repository/npm/

# 腾讯云镜像
npm config set registry http://mirrors.cloud.tencent.com/npm/
```

