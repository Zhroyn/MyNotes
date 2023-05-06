<!-- TOC -->

- [Structure from Motion](#structure-from-motion)
  - [Camera Model](#camera-model)
  - [Camera Calibration](#camera-calibration)
    - [Direct Linear Transform (DLT)](#direct-linear-transform-dlt)
    - [Perspective-n-Point (PnP) Problem](#perspective-n-point-pnp-problem)
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
\displaystyle u^{(i)} = \frac{p_{11}x_w^{(i)} + p_{12}y_w^{(i)} + p_{13}z_w^{(i)} + p_{14}}{p_{31}x_w^{(i)} + p_{32}y_w^{(i)} + p_{33}z_w^{(i)} + p_{34}}
\\~\\
\displaystyle v^{(i)} = \frac{p_{21}x_w^{(i)} + p_{22}y_w^{(i)} + p_{23}z_w^{(i)} + p_{24}}{p_{31}x_w^{(i)} + p_{32}y_w^{(i)} + p_{33}z_w^{(i)} + p_{34}}
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
So the solution can become: 
$$\text{arg }\underset{p}{\text{min}}||A\bm{p}||^2 \text{ such that } ||\bm{p}||^2 = 1 $$ It can be proven that eigenvector $\bm{p}$ with smallest eigenvalue $\lambda$ of matrix $A^TA$ is the solution.

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




