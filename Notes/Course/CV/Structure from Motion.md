<!-- TOC -->

- [Structure from Motion](#structure-from-motion)
  - [Camera Model](#camera-model)
  - [Camera Calibration](#camera-calibration)
    - [Direct Linear Transform (DLT)](#direct-linear-transform-dlt)
    - [Perspective-n-Point (PnP) Problem](#perspective-n-point-pnp-problem)
  - [Structure from Motion](#structure-from-motion-1)
    - [Epipolar Geometry](#epipolar-geometry)
    - [Triangulation](#triangulation)
      - [Linear Solution](#linear-solution)
      - [Non-linear Solution](#non-linear-solution)
    - [Sequential Structure from Motion](#sequential-structure-from-motion)

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
The relation between the coordinates in world and camera coordinate systems is
$$
\begin{bmatrix} u^{(i)} \\ v^{(i)} \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
   p_{11} & p_{12} & p_{13} & p_{14} \\ 
   p_{21} & p_{22} & p_{23} & p_{24} \\ 
   p_{31} & p_{32} & p_{33} & p_{34} \\ 
\end{bmatrix}
\begin{bmatrix} x_w^{(i)} \\ y_w^{(i)} \\ z_w^{(i)} \\ 1 \end{bmatrix}
$$ That is
$$
u^{(i)} = \frac{p_{11}x_w^{(i)} + p_{12}y_w^{(i)} + p_{13}z_w^{(i)} + p_{14}}{p_{31}x_w^{(i)} + p_{32}y_w^{(i)} + p_{33}z_w^{(i)} + p_{34}}
\\~\\
v^{(i)} = \frac{p_{21}x_w^{(i)} + p_{22}y_w^{(i)} + p_{23}z_w^{(i)} + p_{24}}{p_{31}x_w^{(i)} + p_{32}y_w^{(i)} + p_{33}z_w^{(i)} + p_{34}}
$$ Rerange the equations, we can get:
$$
\bm{x}_w^{(i)} = \begin{bmatrix} x_w^{(i)} & y_w^{(i)} & z_w^{(i)} & 1 \end{bmatrix}, \bm{p}_i = \begin{bmatrix} p_{i1} \\ p_{i2} \\ p_{i3} \\ p_{i4} \end{bmatrix}
\\~\\
\begin{bmatrix}
  \bm{x}_w^{(1)} & \bm{0} & -u_1\bm{x}_w^{(1)} \\
  \bm{0} & \bm{x}_w^{(1)} & -v_1\bm{x}_w^{(1)} \\
  \vdots & \vdots & \vdots \\
  \bm{x}_w^{(n)} & \bm{0} & -u_n\bm{x}_w^{(n)} \\
  \bm{0} & \bm{x}_w^{(n)} & -v_n\bm{x}_w^{(n)} \\
\end{bmatrix}
\begin{bmatrix} \bm{p}_1 \\ \bm{p}_2 \\ \bm{p}_3 \end{bmatrix} = \bm{0} \\~\\
\Rightarrow A\bm{p} = \bm{0}
$$

Projection matrix is up to scale, we can use $p_{34}=1$ or $||\bm{p}||^2 = 1$ as constraint condition.
So the solution is the $\bm{p}$ that satisfies: 
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

#### Perspective-n-Point (PnP) Problem
- Perspective-n-Point(PnP) is the problem of estimating the pose of a calibrated camera given a set of n 3D points in the world and their corresponding 2D projections in the image.
- The camera's intrinsic parameters are known, extrinsic parameters are unknown ,which consist of 6 degrees-of-freedom (DOF), 3 for rotation, 3 for translation.
- Usually called 6DoF pose estimation.

**P3P**
To get the extrinsic matrix, we need to get the coordinates of the 3D points in camera reference.

Firstly, convert the pixel coordinates to the normalized coordinates in camera reference:
$$
x_c = \frac{u - o_x}{f_x} \\~\\
y_c = \frac{v - o_y}{f_y} \\~\\
z_c = 1 \\
$$ By these, we can get $\cos\left\langle a, b \right\rangle, \cos\left\langle b, c \right\rangle, \cos\left\langle a, c \right\rangle$.

Then, by the cosine theorem, we can get:
$$
\left\{
\begin{aligned}
  & OA^2 + OB^2 - 2OA\cdot OB\cdot \cos\left\langle a, b \right\rangle = AB^2 \\
  & OB^2 + OC^2 - 2OB\cdot OC\cdot \cos\left\langle b, c \right\rangle = BC^2 \\
  & OA^2 + OC^2 - 2OA\cdot OC\cdot \cos\left\langle a, c \right\rangle = AC^2 \\
\end{aligned}
\right.
$$ Devided by $OC^2$, and denote $\displaystyle x = \frac{OA}{OC}, y = \frac{OB}{OC} $, then:
$$
\left\{
\begin{aligned}
  & x^2 + y^2 - 2xy\cos\left\langle a, b \right\rangle = AB^2/OC^2 \\
  & y^2 + 1 - 2y\cos\left\langle b, c \right\rangle = BC^2/OC^2 \\
  & x^2 + 1 - 2y\cos\left\langle a, c \right\rangle = AC^2/OC^2 \\
\end{aligned}
\right.
$$
Denote $\displaystyle v = \frac{AB^2}{OC^2}, u = \frac{BC^2}{AB^2}, w = \frac{AC^2}{AB^2}$, then:
$$
\left\{
\begin{aligned}
  & x^2 + y^2 - 2xy\cos\left\langle a, b \right\rangle - v = 0 \\
  & y^2 + 1 - 2y\cos\left\langle b, c \right\rangle - uv = 0 \\
  & x^2 + 1 - 2y\cos\left\langle a, c \right\rangle - wv = 0 \\
\end{aligned}
\right.
$$ Rerange the equations, then we can get:
$$
\left\{
\begin{aligned}
  & (1 - u)y^2 - ux^2 - \cos\left\langle b, c \right\rangle y + 2uxy\cos\left\langle a, b \right\rangle + 1 = 0 \\
  & (1 - w)x^2 - wy^2 - \cos\left\langle b, c \right\rangle x + 2wxy\cos\left\langle a, b \right\rangle + 1 = 0 \\
\end{aligned}
\right.
$$ This binary quadratic equation has 4 possible answers, we use one extra point to determine the most possible one.

**Bundle Adjustment (BA)**
Minimize the reprojection error:
$$
\underset{R,t}{\text{min}} \sum_i ||p_i - K(RP_i + t)||^2
$$ Initialized by P3P, optimized by Gauss-Newton.












### Structure from Motion
- Compute 3D structure of the scene and camera poses from multiple views
- Assume intrinsic matrix $K$ is known for each camera

#### Epipolar Geometry
- Epipolar geometry describes the geometric relation between the 2D projections ($u_l$ and $u_r$) of a 3D point in two views
- Epipolar geometry tells us how to solve $t$ and $R$ between the two cameras given a few pairs of 2D correspondences
<br>

- **Epipole** : Image point of origin/pinhole of one camera as viewed by the other camera.
- **Epipolar Plane** : The plane formed by camera origins($O_l$ and $O_r$), epipoles ($e_l$ and $e_r$) and scene point $P$.

The normal vecter to the epipolar plane is $\bm{n} = \bm{t} \times \bm{x}_l $, so $\bm{x}_l \cdot (\bm{t} \times \bm{x}_l) = 0 $
That is 
$$
\begin{bmatrix} x_l & y_l & z_l \end{bmatrix}
\begin{bmatrix} t_yz_l - t_zy_l \\ t_zx_l - t_xz_l \\ t_xy_l - t_yx_l \end{bmatrix} = 0
\\~\\
\Rightarrow 
\begin{bmatrix} x_l & y_l & z_l \end{bmatrix}
\begin{bmatrix}
  0 & -t_z & t_y \\
  t_z & 0 & -t_x \\
  -t_y & t_x & 0 \\
\end{bmatrix}
\begin{bmatrix} x_l \\ y_l \\ z_l \end{bmatrix} = 0
\\~\\
\Rightarrow 
\bm{x}_l^T T_X \bm{x}_l = 0
$$

Substitute $\bm{x}_l = R\bm{x}_r + \bm{t} $ into the epipolar constraint, then we can get:
$$
\bm{x}_l^T (T_XR\bm{x}_r + T_X\bm{t}) = 0
\\~\\
\Rightarrow \bm{x}_l^T (T_XR\bm{x}_r + \bm{t}\times \bm{t}) = 0
\\~\\
\Rightarrow 
\begin{bmatrix} x_l & y_l & z_l \end{bmatrix}
\begin{bmatrix}
  e_{11} & e_{12} & e_{13} \\
  e_{21} & e_{22} & e_{23} \\
  e_{31} & e_{32} & e_{33} \\
\end{bmatrix}
\begin{bmatrix} x_r \\ y_r \\ z_r \end{bmatrix} = 0
\\~\\
\begin{bmatrix}
  e_{11} & e_{12} & e_{13} \\
  e_{21} & e_{22} & e_{23} \\
  e_{31} & e_{32} & e_{33} \\
\end{bmatrix}
= \begin{bmatrix}
  0 & -t_z & t_y \\
  t_z & 0 & -t_x \\
  -t_y & t_x & 0 \\
\end{bmatrix}
\begin{bmatrix}
  r_{11} & r_{12} & r_{13} \\
  r_{21} & r_{22} & r_{23} \\
  r_{31} & r_{32} & r_{33} \\
\end{bmatrix}
\\~\\
\text{Essential Matrix : } E = T_XR
$$

Given that $T_X$ is a Skew-Symmetric matrix ($a_{ij} = -a_{ji} $) and $R$ is an Orthonormal matrix, it is possible to “decouple” $T_X$ and $R$ from their product using “Singular Value Decomposition”.
So if $E$ is known, we can calculate $\bm{t}$ and $R$.

To calculate $E$, fistly, we can get:
$$
z_l\begin{bmatrix} u_l \\ v_l \\ 1 \end{bmatrix}
= \begin{bmatrix}
  f_x^{(l)} & 0 & o_x^{(l)} \\
  0 & f_y^{(l)} & o_y^{(l)} \\
  0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix} x_l \\ y_l \\ z_l \end{bmatrix}, 
z_r\begin{bmatrix} u_r \\ v_r \\ 1 \end{bmatrix}
= \begin{bmatrix}
  f_x^{(r)} & 0 & o_x^{(r)} \\
  0 & f_y^{(r)} & o_y^{(r)} \\
  0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix} x_r \\ y_r \\ z_r \end{bmatrix}
\\~\\
\Rightarrow x_l^T = \begin{bmatrix} u_l & v_l & 1 \end{bmatrix}z_l K_l^{{-1}^T}, 
x_r = K_r^{-1} z_r \begin{bmatrix} u_r \\ v_r \\ 1 \end{bmatrix}
$$ Substitute these into the epipolar constraint, then we can get:
$$
\begin{bmatrix} u_l & v_l & 1 \end{bmatrix} K_l^{{-1}^T}
\begin{bmatrix}
  e_{11} & e_{12} & e_{13} \\
  e_{21} & e_{22} & e_{23} \\
  e_{31} & e_{32} & e_{33} \\
\end{bmatrix}
K_r^{-1} \begin{bmatrix} u_r \\ v_r \\ 1 \end{bmatrix} = 0
\\~\\
\Rightarrow \begin{bmatrix} u_l & v_l & 1 \end{bmatrix}
\begin{bmatrix}
  f_{11} & f_{12} & f_{13} \\
  f_{21} & f_{22} & f_{23} \\
  f_{31} & f_{32} & f_{33} \\
\end{bmatrix}
\begin{bmatrix} u_r \\ v_r \\ 1 \end{bmatrix} = 0
\\~\\
\text{Fundamental Matrix : } 
F = \begin{bmatrix}
  f_{11} & f_{12} & f_{13} \\
  f_{21} & f_{22} & f_{23} \\
  f_{31} & f_{32} & f_{33} \\
\end{bmatrix}
\\~\\
E = K_l^T F K_r
$$

Fundamental Matrix $F$ and $kF$ describe the same epipolar geometry. That is, $F$ is defined only up to a scale.
So we can add a scale constraint on $F$ : $||f||^2 = 1$

Expand the matrix to get linear equation:
$$
\begin{aligned}
  & (f_{11}u_r^{(i)} + f_{12}v_r^{(i)} + f_{13})u_l^{(l)} \\
  &+ (f_{21}u_r^{(i)} + f_{22}v_r^{(i)} + f_{23})v_l^{(l)} \\
  &+ f_{31}u_r^{(i)} + f_{32}v_r^{(i)} + f_{33} \\
  &= 0
\end{aligned}
$$ Rerange the terms, and set $\bm{p}_r = \begin{bmatrix} u_r & v_r & 1 \end{bmatrix}$, then we can get:
$$
\begin{bmatrix}
  u_l^{(1)}\bm{p}_r & v_l^{(1)}\bm{p}_r & \bm{p}_r \\
  \vdots & \vdots & \vdots \\
  u_l^{(i)}\bm{p}_r & v_l^{(i)}\bm{p}_r & \bm{p}_r \\
  \vdots & \vdots & \vdots \\
  u_l^{(n)}\bm{p}_r & v_l^{(n)}\bm{p}_r & \bm{p}_r \\
\end{bmatrix}
\begin{bmatrix} f_{11} \\ f_{12} \\ f_{13} \\ f_{21} \\ f_{22} \\ f_{23} \\ f_{31} \\ f_{32} \\ f_{33} \end{bmatrix}
= \bm{0}
\\~\\
\Rightarrow A\bm{f} = \bm{0}
$$
So the solution is the $\bm{f}$ that satisfies: 
$$\underset{f}{\text{min}}||A\bm{f}||^2 \text{ such that } ||\bm{f}||^2 = 1 $$ The eigenvector with smallest eigenvalue $\lambda$ of matrix $A^TA$ is the solution.


#### Triangulation
##### Linear Solution
Given corresponding 2D coordinates of one point in two views, and the parameters of the two cameras, we want to calculate the 3D coordinate of the point.

Firstly, we can get the image equations:
$$
\begin{bmatrix} u_{r} \\ v_{r} \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
  f_x^{(r)} & 0 & o_x^{(r)} & 0 \\
  0 & f_y^{(r)} & o_y^{(r)} & 0 \\
  0 & 0 & 1 & 0 \\
\end{bmatrix}
\begin{bmatrix} x_{r} \\ y_{r} \\ z_{r} \\ 1 \end{bmatrix}
\\~\\
\begin{bmatrix} u_{l} \\ v_{l} \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
  f_x^{(l)} & 0 & o_x^{(l)} & 0 \\
  0 & f_y^{(l)} & o_y^{(l)} & 0 \\
  0 & 0 & 1 & 0 \\
\end{bmatrix}
\begin{bmatrix} x_{l} \\ y_{l} \\ z_{l} \\ 1 \end{bmatrix} \\
\equiv \begin{bmatrix}
  f_x^{(l)} & 0 & o_x^{(l)} & 0 \\
  0 & f_y^{(l)} & o_y^{(l)} & 0 \\
  0 & 0 & 1 & 0 \\
\end{bmatrix}
\begin{bmatrix}
  r_{11} & r_{12} & r_{13} & t_{x} \\
  r_{21} & r_{22} & r_{23} & t_{y} \\
  r_{31} & r_{32} & r_{33} & t_{z} \\
  0 & 0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix} x_{r} \\ y_{r} \\ z_{r} \\ 1 \end{bmatrix}
$$ Rewrite the imaging equations:
$$
\tilde{\bm{u}}_r = M_r \tilde{\bm{x}}_r
\Rightarrow
\begin{bmatrix} u_{r} \\ v_{r} \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
  m_{11} & m_{12} & m_{13} & m_{14} \\
  m_{21} & m_{22} & m_{23} & m_{24} \\
  m_{31} & m_{32} & m_{33} & m_{34} \\
\end{bmatrix}
\begin{bmatrix} x_{r} \\ y_{r} \\ z_{r} \\ 1 \end{bmatrix}
\\~\\
\tilde{\bm{u}}_l = P_l \tilde{\bm{x}}_r
\Rightarrow
\begin{bmatrix} u_{l} \\ v_{l} \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
  p_{11} & p_{12} & p_{13} & p_{14} \\
  p_{21} & p_{22} & p_{23} & p_{24} \\
  p_{31} & p_{32} & p_{33} & p_{34} \\
\end{bmatrix}
\begin{bmatrix} x_{r} \\ y_{r} \\ z_{r} \\ 1 \end{bmatrix}
$$ So
$$
u_r = \frac{m_{11}x_r + m_{12}y_r + m_{13}z_r + m_{14}}{m_{31}x_r + m_{32}y_r + m_{33}z_r + m_{34}}
\\~\\
v_r = \frac{m_{21}x_r + m_{22}y_r + m_{23}z_r + m_{24}}{m_{31}x_r + m_{32}y_r + m_{33}z_r + m_{34}}
\\~\\
u_l = \frac{p_{11}x_r + p_{12}y_r + p_{13}z_r + p_{14}}{p_{31}x_r + p_{32}y_r + p_{33}z_r + p_{34}}
\\~\\
v_l = \frac{p_{21}x_r + p_{22}y_r + p_{23}z_r + p_{24}}{p_{31}x_r + p_{32}y_r + p_{33}z_r + p_{34}}
$$ That is
$$
\begin{bmatrix}
  u_rm_{31} - m_{11} & u_rm_{32} - m_{12} & u_rm_{33} - m_{13} \\
  v_rm_{31} - m_{11} & v_rm_{32} - m_{12} & v_rm_{33} - m_{13} \\
  u_lp_{31} - p_{11} & u_lp_{32} - p_{12} & u_lp_{33} - p_{13} \\
  v_lp_{31} - p_{11} & v_lp_{32} - p_{12} & v_lp_{33} - p_{13} \\
\end{bmatrix}
\begin{bmatrix} x_{r} \\ y_{r} \\ z_{r} \end{bmatrix}
= \begin{bmatrix} 
  m_{14} - u_rm_{34} \\
  m_{24} - v_rm_{34} \\
  p_{14} - u_lp_{34} \\
  p_{24} - v_lp_{34} \\
\end{bmatrix}
\\~\\
\Rightarrow A\bm{x}_r = \bm{b}
$$ Find least squares solution by:
$$\bm{x}_r = (A^TA)^{-1} A^T \bm{b} $$


##### Non-linear Solution
Minimize reprojection error:
$$\text{cons}(\bold{P}) = ||\bold{u}_l - \hat{\bold{u}_l}||^2 + ||\bold{u}_r - \hat{\bold{u}_r}||^2 $$



#### Sequential Structure from Motion
1. Initialize camera motion and scene structure
2. For each additional view
   - Determine projection matrix of new camera using all the known 3D points that are visible in its image
   - Refine and extend structure: compute new 3D points, reoptimize existing points that are also seen by this camera
3. Refine structure and motion: Bundle Adjustment
   - Refining 3D points and camera parameters by minimizing reprojection error over all frames: $$E(P_{proj}, \bold{P}) = \sum_{i=1}^{m} \sum_{j=1}^{n} ||u_j^{(i)} - P_{proj}^{(i)}\bold{P}_j||^2 $$



