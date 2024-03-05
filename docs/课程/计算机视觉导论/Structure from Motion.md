
## Structure from Motion
### Camera Calibration
#### Perspective-n-Point (PnP) Problem
The goal of the Perspective-n-Point (PnP) problem is to estimate the position and orientation of a calibrated camera from known 3D-to-2D point correspondences.

<br>

##### Direct Linear Transform (DLT)
Suppose the relation between the 2D-coordinate and 3D-coordinate of a point is
$$
\begin{bmatrix} u^{(i)} \\ v^{(i)} \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
   p_{11} & p_{12} & p_{13} & p_{14} \\ 
   p_{21} & p_{22} & p_{23} & p_{24} \\ 
   p_{31} & p_{32} & p_{33} & p_{34} \\ 
\end{bmatrix}
\begin{bmatrix} x_w^{(i)} \\ y_w^{(i)} \\ z_w^{(i)} \\ 1 \end{bmatrix}
$$

That is
$$
u^{(i)} = \frac{p_{11}x_w^{(i)} + p_{12}y_w^{(i)} + p_{13}z_w^{(i)} + p_{14}}{p_{31}x_w^{(i)} + p_{32}y_w^{(i)} + p_{33}z_w^{(i)} + p_{34}}
\\~\\
v^{(i)} = \frac{p_{21}x_w^{(i)} + p_{22}y_w^{(i)} + p_{23}z_w^{(i)} + p_{24}}{p_{31}x_w^{(i)} + p_{32}y_w^{(i)} + p_{33}z_w^{(i)} + p_{34}}
$$

Rerange the equations, we can get
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

Because the projection matrix is defined up to scale, we can add a constraint condition $\left\| \bm{p} \right\|^2 = 1$, then the solution is
$$
\underset{p}{\min}\left\| A\bm{p} \right\|^2 \text{ such that } \left\| \bm{p} \right\|^2 = 1
$$

The eigenvector with smallest eigenvalue $\lambda$ of matrix $A^TA$ is the solution.

Then, to decompose projection matrices to intrinsic and extrinsic matrices, we can use QR factorization:
$$
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
\begin{bmatrix} p_{14} \\ p_{24} \\ p_{34} \end{bmatrix} = K\bm{t}
$$

<br>

##### P3P
P3P uses the geometric relationships of three points, the 3D-to-2D point correspondences, and the known internal parameters of the camera to get the external parameters of the camera.

Firstly, convert 2D points to corresponding 3D points in camera coordinate system
$$
x_c = \frac{u - o_x}{f_x}, \quad
y_c = \frac{v - o_y}{f_y}, \quad
z_c = 1 \\
$$

By these, we can get $\cos\left< a, b \right>, \cos\left< b, c \right>, \cos\left< a, c \right>$. Then, by the cosine theorem, we can get
$$
\left\{
\begin{aligned}
  & OA^2 + OB^2 - 2OA\cdot OB\cdot \cos\left< a, b \right> = AB^2 \\
  & OB^2 + OC^2 - 2OB\cdot OC\cdot \cos\left< b, c \right> = BC^2 \\
  & OA^2 + OC^2 - 2OA\cdot OC\cdot \cos\left< a, c \right> = AC^2 \\
\end{aligned}
\right.
$$

Devided both sides by $OC^2$, and let $\displaystyle x = \frac{OA}{OC}, y = \frac{OB}{OC}, v = \frac{AB^2}{OC^2}, u = \frac{BC^2}{AB^2}, w = \frac{AC^2}{AB^2}$, then the equations become

$$
\left\{
\begin{aligned}
  & x^2 + y^2 - 2xy\cos\left< a, b \right> - v = 0 \\
  & y^2 + 1 - 2y\cos\left< b, c \right> - uv = 0 \\
  & x^2 + 1 - 2y\cos\left< a, c \right> - wv = 0 \\
\end{aligned}
\right.
$$

Rerange the equations, then we can get
$$
\left\{
\begin{aligned}
  & (1 - u)y^2 - ux^2 - \cos\left< b, c \right> y + 2uxy\cos\left< a, b \right> + 1 = 0 \\
  & (1 - w)x^2 - wy^2 - \cos\left< b, c \right> x + 2wxy\cos\left< a, b \right> + 1 = 0 \\
\end{aligned}
\right.
$$ This binary quadratic equation has 4 possible answers, we use one extra point to determine the most possible one.

<br>

##### Bundle Adjustment (BA)
Suppose $P_i$ is the coordinate of a point in the world coordinate system, $p_i$ is the homogeneous coordinate of corresponding point in camera coordinate system, $\omega_i$ is the depth of correspoinding point, then we can define the reprojection error
$$
e(R, t) = \sum_i \left\| p_i - \frac{1}{\omega_i}K(RP_i + t) \right\|^2
$$

We can initialize $R, t$ by P3P, and then optimize them by Gauss-Newton.










<br>

### Structure from Motion (SFM)
Structure from motion (SfM) is a photogrammetric range imaging technique for estimating three-dimensional structures from two-dimensional image sequences that may be coupled with local motion signals.

<br>

#### Epipolar Geometry
Epipolar geometry uses the 2D point correspondences and the known internal parameters of cameras to get $R, t$ between two cameras.

**Baseline** ($O_lO_r$): Line connecting the two camera centers.
**Epipoles** ($e_l$ and $e_r$): Intersections of baseline with image planes.
**Epipolar Plane** ($XO_lO_r$): Plane containing $X, O$ and $O'$.
**Epipolar Lines** ($l_l$ and $l_r$): Intersections of epipolar plane with image planes.

---

The normal vecter of the epipolar plane is $\bm{n} = \bm{t} \times \bm{x}_l $, so $\bm{x}_l \cdot (\bm{t} \times \bm{x}_l) = 0$. That is 
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

Substitute $\bm{x}_l = R\bm{x}_r + \bm{t} $ into $\bm{x}_l^T T_X \bm{x}_l = 0$, we can get
$$
\bm{x}_l^T (T_XR\bm{x}_r + T_X\bm{t}) = 0
\\~\\
\Rightarrow \bm{x}_l^T (T_XR\bm{x}_r + \bm{t}\times \bm{t}) = 0
\\~\\
\Rightarrow \bm{x}_l^T E \bm{x}_r = 0
$$

where $E = T_XR$ is called **essential matrix**.

Given that $T_X$ is a skew-symmetric matrix ($a_{ij} = -a_{ji} $) and $R$ is an orthonormal matrix, we can decouple $T_X$ and $R$ from $E$ using singular value decomposition, so our goal becomes getting $E$.

---

To calculate $E$, fistly, we have
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
\Rightarrow \bm{x}_l^T = \begin{bmatrix} u_l & v_l & 1 \end{bmatrix}z_l K_l^{{-1}^T},
\bm{x}_r = K_r^{-1} z_r \begin{bmatrix} u_r \\ v_r \\ 1 \end{bmatrix}
$$

Substitute these into $\bm{x}_l^T E \bm{x}_r = 0$, we can get:
$$
\begin{bmatrix} u_l & v_l & 1 \end{bmatrix} K_l^{{-1}^T} E K_r^{-1} \begin{bmatrix} u_r \\ v_r \\ 1 \end{bmatrix} = 0
\\~\\
\Rightarrow \bm{u}_l^T F \bm{u}_r = 0
$$

where $F = K_l^{{-1}^T} E K_r^{-1}$ is called **fundamental matrix**.

---

Expand $\bm{u}_l^T F \bm{u}_r = 0$, we can get
$$
\begin{aligned}
  & (f_{11}u_r^{(i)} + f_{12}v_r^{(i)} + f_{13})u_l^{(l)} + (f_{21}u_r^{(i)} + f_{22}v_r^{(i)} + f_{23})v_l^{(l)} + \\
  & f_{31}u_r^{(i)} + f_{32}v_r^{(i)} + f_{33} = 0
\end{aligned}
$$

Rerange the terms, and set $\bm{p}_r^{(i)} = \begin{bmatrix} u_r^{(i)} & v_r^{(i)} & 1 \end{bmatrix}$, then we can get:
$$
\begin{bmatrix}
  u_l^{(1)}\bm{p}_r^{(1)} & v_l^{(1)}\bm{p}_r^{(1)} & \bm{p}_r^{(1)} \\
  \vdots & \vdots & \vdots \\
  u_l^{(i)}\bm{p}_r^{(i)} & v_l^{(i)}\bm{p}_r^{(i)} & \bm{p}_r^{(i)} \\
  \vdots & \vdots & \vdots \\
  u_l^{(n)}\bm{p}_r^{(n)} & v_l^{(n)}\bm{p}_r^{(n)} & \bm{p}_r^{(n)} \\
\end{bmatrix}
\begin{bmatrix} f_{11} \\ f_{12} \\ f_{13} \\ f_{21} \\ f_{22} \\ f_{23} \\ f_{31} \\ f_{32} \\ f_{33} \end{bmatrix}
= \bm{0}
\\~\\
\Rightarrow A\mathbf{f} = \bm{0}
$$

Because $\mathbf{f}$ is defined up to scale, we can add a constraint condition $\left\| \mathbf{f} \right\|^2 = 1$, then the solution is
$$
\underset{\mathbf{f}}{\min}\left\| A\mathbf{f} \right\|^2 \text{ such that } \left\| \mathbf{f} \right\|^2 = 1
$$

The eigenvector with smallest eigenvalue $\lambda$ of matrix $A^TA$ is the solution.

<br>

#### Triangulation
##### Linear Solution
Triangulation uses 2D point correspondence and all parameters of two cameras to get 3D coordinate of a point.

Firstly, we have imaging equations
$$
\begin{bmatrix} u_{r} \\ v_{r} \\ 1 \end{bmatrix}
\equiv M_{int}^{(r)} \bm{\tilde{x}}_r 
= \begin{bmatrix}
  m_{11} & m_{12} & m_{13} & m_{14} \\
  m_{21} & m_{22} & m_{23} & m_{24} \\
  m_{31} & m_{32} & m_{33} & m_{34} \\
\end{bmatrix}
\begin{bmatrix} x_{r} \\ y_{r} \\ z_{r} \\ 1 \end{bmatrix}
\\~\\
\begin{bmatrix} u_l \\ v_l \\ 1 \end{bmatrix}
\equiv M_{int}^{(l)} \bm{\tilde{x}}_l = M_{int}^{(l)} M_{ext} \bm{\tilde{x}}_r
= \begin{bmatrix}
  p_{11} & p_{12} & p_{13} & p_{14} \\
  p_{21} & p_{22} & p_{23} & p_{24} \\
  p_{31} & p_{32} & p_{33} & p_{34} \\
\end{bmatrix}
\begin{bmatrix} x_{r} \\ y_{r} \\ z_{r} \\ 1 \end{bmatrix}
$$

That is
$$
u_r = \frac{m_{11}x_r + m_{12}y_r + m_{13}z_r + m_{14}}{m_{31}x_r + m_{32}y_r + m_{33}z_r + m_{34}}
\\~\\
v_r = \frac{m_{21}x_r + m_{22}y_r + m_{23}z_r + m_{24}}{m_{31}x_r + m_{32}y_r + m_{33}z_r + m_{34}}
\\~\\
u_l = \frac{p_{11}x_r + p_{12}y_r + p_{13}z_r + p_{14}}{p_{31}x_r + p_{32}y_r + p_{33}z_r + p_{34}}
\\~\\
v_l = \frac{p_{21}x_r + p_{22}y_r + p_{23}z_r + p_{24}}{p_{31}x_r + p_{32}y_r + p_{33}z_r + p_{34}}
$$

Rerange the equations, we can get
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
\Rightarrow A\bm{x}_r = \mathbf{b}
$$

The least squares solution is
$$\bm{x}_r = (A^TA)^{-1} A^T \mathbf{b} $$

<br>

##### Non-Linear Solution
Suppose $\mathbf{P}$ is the coordinate of a point, $\bm{\hat{u}}_l, \bm{\hat{u}}_r$ are projections of the point on the two image planes, then we can define the reprojection error
$$\text{cost}(\mathbf{P}) = \left\| \bm{u}_l - \bm{\hat{u}}_l \right\|^2 + \left\| \bm{u}_r - \bm{\hat{u}}_r \right\|^2$$

The solution is $\mathbf{P}$ such that minimize the reprojection error.


