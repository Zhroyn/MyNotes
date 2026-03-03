# 相机模型

## 从世界到相机

假设相机坐标轴在世界坐标系的方向分别是 $\hat{x}_c$，$\hat{y}_c$ 和 $\hat{z}_c$，那么易得 C2W 的旋转矩阵为 $[\hat{x}_c, \hat{y}_c, \hat{z}_c]$，任意向量在相机坐标系下的坐标右乘这个矩阵就会变为世界坐标系下的坐标：

$$
R_{c2w} \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \hat{x}_c, \quad
R_{c2w} \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} = \hat{y}_c, \quad
R_{c2w} \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} = \hat{z}_c
$$

其逆矩阵就是 W2C 的旋转矩阵，也就是相机的方向：

$$
R_{w2c} = 
\begin{bmatrix} \hat{x}_c \\ \hat{y}_c \\ \hat{z}_c \end{bmatrix} 
= \begin{bmatrix}
  r_{11} & r_{12} & r_{13} \\ 
  r_{21} & r_{22} & r_{23} \\ 
  r_{31} & r_{32} & r_{33} \\ 
\end{bmatrix}
$$

令 $\mathbf{p}_w$ 表示一个点在世界坐标系中的坐标，$\mathbf{p}_c$ 表示该点在相机坐标系中的坐标，$\mathbf{t}_{c2w}$ 表示相机原点在世界坐标系中的坐标，那么有：

$$
\begin{aligned}
    \mathbf{p}_c &= R_{w2c}(\mathbf{p}_w - \mathbf{t}_{c2w}) \\
    &= R_{w2c}\mathbf{p}_w - R_{w2c}\mathbf{t}_{c2w} \\
    &= R_{w2c}\mathbf{p}_w + \mathbf{t}_{w2c}
\end{aligned}
$$

其中 $\mathbf{t}_{w2c} = -R_{w2c} \mathbf{t}_{c2w}$ 是世界坐标系的原点在相机坐标系中的坐标，整个方程可以通过一个**外参矩阵**（extrinsic matrix）表示：

$$
\begin{bmatrix}
    \mathbf{p}_c \\
    1 \\
\end{bmatrix}
= \begin{bmatrix}
  R_{w2c} & \mathbf{t}_{w2c} \\ 
  \mathbf{0} & 1
\end{bmatrix}
\begin{bmatrix}
    \mathbf{p}_w \\
    1 \\
\end{bmatrix}
= T_{w2c}
\begin{bmatrix}
    \mathbf{p}_w \\
    1 \\
\end{bmatrix}
$$

W2C 外参和 C2W 外参是严格互逆的，有以下关系：

$$
T_{c2w} = T_{w2c}^{-1} = \begin{bmatrix}
  R_{w2c}^T & -R_{w2c}^T\mathbf{t}_{w2c} \\ 
  \mathbf{0} & 1
\end{bmatrix}
$$

一般 OpenCV/COLMAP 等计算机视觉库使用 W2C 外参表示相机位姿，而 OpenGL/DirectX 等计算机图形库使用 C2W 外参表示相机位姿。




## 从相机到像素

我们可以通过透视投影将三维坐标转换为二维坐标：

$$ \mathbf{x}_i = f \cdot \begin{bmatrix} x_c/z_c \\ y_c/z_c \\ 1 \end{bmatrix} $$

令 $m_x, m_y$ 分别为 x 和 y 方向上的像素密度（像素/毫米），$(c_x, c_y)$ 为主点（Principal Point），即光轴与传感器的交点，那么最终的二维坐标为：

$$
\mathbf{u} = \begin{bmatrix} u \\ v \end{bmatrix} = \begin{bmatrix} m_xf\frac{x_c}{z_c} + c_x \\ m_yf\frac{y_c}{z_c} + c_y \end{bmatrix}
$$

令 $f_x = m_xf$，$f_y = m_yf$，则该方程可以通过一个**内参矩阵**（intrinsic matrix）以齐次坐标的形式表示：

$$
\begin{bmatrix} u \\ v \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
  f_x & 0 & c_x \\ 
  0 & f_y & c_y \\ 
  0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} x_c/z_c \\ y_c/z_c \\ 1 \end{bmatrix}
= K \begin{bmatrix} x_c/z_c \\ y_c/z_c \\ 1 \end{bmatrix}
$$

将 $K$ 从 3x3 扩展为 3x4 矩阵 $M_{intr}$，并将 $\mathbf{x}_c$ 从三维向量扩展为四维齐次坐标 $\mathbf{\tilde{x}}_c = [x_c, y_c, z_c, 1]^T$，则有：

$$
\mathbf{\tilde{u}} \equiv M_{intr}\mathbf{\tilde{x}}_c = M_{intr}T_{w2c}\mathbf{\tilde{x}}_w = P_{3\times 4}\mathbf{\tilde{x}}_w
$$

最终，我们可以得到一个**投影矩阵**（projection matrix） $P_{3\times 4}$，将世界坐标系下的三维点 $\mathbf{\tilde{x}}_w$ 投影到图像平面上的二维点 $\mathbf{\tilde{u}}$。




## 从像素到光线

若我们不知道相机的内参矩阵，可以尝试从图像的大小和视角计算出来。假设图像的宽度为 $W$，相机的水平视角（FOV，Field of View）为 $\theta_x$，图像某一角的像素点在相机坐标系中的坐标为 $(x_0, y_0, z_0)$，那么我们有：

$$ f_x \frac{x_0}{z_0} = \frac{1}{2}W $$

$$ \Rightarrow \tan \frac{\theta_x}{2} = \frac{x_0}{z_0} = \frac{W}{2f_x} $$

$$ \Rightarrow f_x = \frac{W}{2\tan(\theta_x/2)} $$

类似地，我们可以得到 $f_y$，然后就可以构建出内参矩阵（$c_x = W/2$，$c_y = H/2$）。

假设我们已经知道某一相机在世界坐标系的位置为 $\mathbf{o}$，该相机中某一像素的坐标为 $(u, v)$，那么我们可以通过内参矩阵得到该像素点在相机坐标系中的坐标：

$$
\hat{\mathbf{x}}_c =
\begin{bmatrix} x_c \\ y_c \\ 1 \end{bmatrix}
= \begin{bmatrix}
  1/f_x & 0 & - c_x/f_x \\ 
  0 & 1/f_y & - c_y/f_y \\ 
  0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = K^{-1}\mathbf{\tilde{u}}
$$

$$\mathbf{\tilde{x}}_c = \begin{bmatrix} x_c \\ y_c \\ 1 \\ 1 \end{bmatrix}$$

再通过外参矩阵得到该像素点在世界坐标系中的坐标，并由此计算出从相机中心出发的光线方向

$$ \quad \mathbf{\tilde{x}}_w = T_{c2w} \mathbf{\tilde{x}}_c = \begin{bmatrix} x_w \\ y_w \\ z_w \\ 1 \end{bmatrix} $$

$$ \mathbf{d} = \frac{\mathbf{x}_w - \mathbf{o}}{\left\| \mathbf{x}_w - \mathbf{o} \right\|} $$

最后，即可得到光线的参数方程

$$ \mathbf{x} = \mathbf{o} + t\mathbf{d} $$
