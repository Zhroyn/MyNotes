<!-- TOC -->

- [Structure from Motion](#structure-from-motion)
  - [Camera Model](#camera-model)
  - [Camera Calibration](#camera-calibration)
    - [Direct Linear Transform (DLT)](#direct-linear-transform-dlt)
    - [Perspective-n-Point (PnP)](#perspective-n-point-pnp)
  - [Structure from Motion](#structure-from-motion-1)

<!-- /TOC -->






## Structure from Motion
### Camera Model
**World-to-Camera Transformation**

Position : $c_w$
Orientation : $R = 
\begin{bmatrix} \hat{x_c} \\ \hat{y_c} \\ \hat{z_c} \end{bmatrix} 
= \begin{bmatrix}
  r_{11} & r_{12} & r_{13} \\ 
  r_{21} & r_{22} & r_{23} \\ 
  r_{31} & r_{32} & r_{33} \\ 
\end{bmatrix} $

$\bm{x_c} = R(\bm{x_w - c_w}) = R\bm{x_w} - R\bm{c_w} = R\bm{x_w} + \bm{t}, \bm{t} = -R\bm{c_w} $

Extrinsic Matrix : $\bm{x_c} = 
\begin{bmatrix} x_c \\ y_c \\ z_c \\ 1 \end{bmatrix}
= \begin{bmatrix}
  r_{11} & r_{12} & r_{13} & t_x \\ 
  r_{21} & r_{22} & r_{23} & t_y \\ 
  r_{31} & r_{32} & r_{33} & t_z \\ 
  0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} x_w \\ y_w \\ z_w \\ 1 \end{bmatrix} $


**Perspective Projection**

$$\bm{x_c} = \begin{bmatrix} x_c \\ y_c \\ z_c \end{bmatrix} \\~\\
\Rightarrow \bm{x_i} = \bm{f} \cdot \begin{bmatrix} x_c/z_c \\ y_c/z_c \\ 1 \end{bmatrix} $$


**Image Plane to Image Sensor Mapping**

If $m_x$ and $m_y$ are the pixel densities (pixels/mm) in x and y directions, and pixel $(c_x, c_y)$ is the Principle Point where the optical axis pierces the sensor, then pixel coordinates are:
$$\displaystyle u = m_xf\frac{x_c}{z_c} + c_x, \displaystyle v = m_yf\frac{y_c}{z_c} + c_y $$

If $f_x = m_xf$, $f_y = m_yf $, then in homogenous coordinates:
$$
\begin{bmatrix} u \\ v \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
  f_x & 0 & c_x \\ 
  0 & f_y & c_y \\ 
  0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} x_c \\ y_c \\ z_c \end{bmatrix}
$$

Intrinsic Matrix : $\bm{\tilde{u}_c} = 
\begin{bmatrix} \tilde{u} \\ \tilde{v} \\ \tilde{w} \end{bmatrix}
= \begin{bmatrix}
  f_x & 0 & c_x & 0 \\ 
  0 & f_y & c_y & 0 \\ 
  0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix} x_c \\ y_c \\ z_c \\ 1 \end{bmatrix} $

**Projection Matrix**
$$
\bm{\tilde{u}} = M_{int}\bm{\tilde{x}_c} \\~\\
\bm{\tilde{x}_c} = M_{ext}\bm{\tilde{x}_w} \\~\\
\bm{\tilde{u}} = M_{int}M_{ext}\bm{\tilde{x}_w} = P_{3\times 4}\bm{\tilde{x}_w} \\~\\
$$


### Camera Calibration
#### Direct Linear Transform (DLT)
The relation between the coordinates in world coordinate and camera coordinate:
$$
\begin{bmatrix} u^{(i)} \\ v^{(i)} \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
   p_{11} & p_{12} & p_{13} & p_{14} \\ 
   p_{21} & p_{22} & p_{23} & p_{24} \\ 
   p_{31} & p_{32} & p_{33} & p_{34} \\ 
\end{bmatrix}
\begin{bmatrix} x_w^{(i)} \\ y_w^{(i)} \\ z_w^{(i)} \\ 1 \end{bmatrix}
$$ That is:
$$
\displaystyle u^{(i)} = \frac{p_{11}x_w^{(i)} + p_{12}y_w^{(i)} + p_{13}z_w^{(i)} + p_{14}}{p_{31}x_w^{(i)} + p_{32}y_w^{(i)} + p_{33}z_w^{(i)} + p_{34}}
\\~\\
\displaystyle v^{(i)} = \frac{p_{21}x_w^{(i)} + p_{22}y_w^{(i)} + p_{23}z_w^{(i)} + p_{24}}{p_{31}x_w^{(i)} + p_{32}y_w^{(i)} + p_{33}z_w^{(i)} + p_{34}}
$$ Rerange the equations, we can get:
$$
\begin{bmatrix}
  x_w^{(1)} & y_w^{(1)} & z_w^{(1)} & 1 & 0 & 0 & 0 & 0 & -u_1x_w^{(1)} & -u_1y_w^{(1)} & -u_1z_w^{(1)} & -u_1 \\
  0 & 0 & 0 & 0 & x_w^{(1)} & y_w^{(1)} & z_w^{(1)} & 1 & -u_1x_w^{(1)} & -u_1y_w^{(1)} & -u_1z_w^{(1)} & -u_1 \\
  \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \\
  x_w^{(i)} & y_w^{(i)} & z_w^{(i)} & 1 & 0 & 0 & 0 & 0 & -u_ix_w^{(i)} & -u_1y_w^{(i)} & -u_1z_w^{(i)} & -u_i \\
  0 & 0 & 0 & 0 & x_w^{(i)} & y_w^{(i)} & z_w^{(i)} & 1 & -u_ix_w^{(i)} & -u_iy_w^{(i)} & -u_iz_w^{(i)} & -u_i \\
  \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \\
  x_w^{(n)} & y_w^{(n)} & z_w^{(n)} & 1 & 0 & 0 & 0 & 0 & -u_nx_w^{(n)} & -u_1y_w^{(n)} & -u_1z_w^{(n)} & -u_n \\
  0 & 0 & 0 & 0 & x_w^{(n)} & y_w^{(n)} & z_w^{(n)} & 1 & -u_nx_w^{(n)} & -u_ny_w^{(n)} & -u_nz_w^{(n)} & -u_n \\
\end{bmatrix}
\begin{bmatrix}
   p_{11} \\ p_{12} \\ p_{13} \\ p_{14} \\ 
   p_{21} \\ p_{22} \\ p_{23} \\ p_{24} \\ 
   p_{31} \\ p_{32} \\ p_{33} \\ p_{34} \\
\end{bmatrix} = \bm{0} \\
\Rightarrow A\bm{p} = \bm{0}
$$

Projection matrix is up to scale, we can use $p_{34}=1$ or $||\bm{p}||^2 = 1$ as constraint condition.
So the solution can become: 
$$\underset{p}{\text{min}}||A\bm{p}||^2 \text{ such that } ||\bm{p}||^2 = 1 $$ It can be proven that eigenvector $\bm{p}$ with smallest eigenvalue $\lambda$ of matrix $A^TA$ is the solution.

Then, to decompose projection matrices to intrinsic and extrinsic matrices, we can use QR factorization:
$$
\begin{bmatrix}
  p_{11} & p_{12} & p_{13} & p_{14} \\
  p_{21} & p_{22} & p_{23} & p_{24} \\
  p_{31} & p_{32} & p_{33} & p_{34} \\
\end{bmatrix}
= \begin{bmatrix}
  f_x & 0 & o_x & 0 \\
  0 & f_y & o_y & 0 \\
  0 & 0 & 1 & 0 \\
\end{bmatrix}
\begin{bmatrix}
  r_{11} & r_{12} & r_{13} & t_{x} \\
  r_{21} & r_{22} & r_{23} & t_{y} \\
  r_{31} & r_{32} & r_{33} & t_{z} \\
  0 & 0 & 0 & 1 \\
\end{bmatrix}
\\~\\
\begin{bmatrix}
  p_{11} & p_{12} & p_{13} \\
  p_{21} & p_{22} & p_{23} \\
  p_{31} & p_{32} & p_{33} \\
\end{bmatrix}
= \begin{bmatrix}
  f_x & 0 & o_x \\
  0 & f_y & o_y \\
  0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
  r_{11} & r_{12} & r_{13} \\
  r_{21} & r_{22} & r_{23} \\
  r_{31} & r_{32} & r_{33} \\
\end{bmatrix}
= KR
\\~\\
\bm{t} = \begin{bmatrix} t_{x} \\ t_{y} \\ t_{z} \end{bmatrix}
= K^{-1} \begin{bmatrix} p_{14} \\ p_{24} \\ p_{34} \end{bmatrix} 
$$

#### Perspective-n-Point (PnP)
intrinsic parameters are known


### Structure from Motion




