<!-- TOC -->

- [Rotational Motion](#rotational-motion)
  - [Velocity, Acceleration, Torque, Energy and Power](#velocity-acceleration-torque-energy-and-power)
  - [Moment of Inertia of differernt Objects](#moment-of-inertia-of-differernt-objects)
  - [Cross product and Coriolis force](#cross-product-and-coriolis-force)
  - [Angular Momentum](#angular-momentum)

<!-- /TOC -->






## Rotational Motion
### Velocity, Acceleration, Torque, Energy and Power
**Constant Angular Acceleration**
$
\displaystyle \omega_f = \omega_i + \alpha t \\
\displaystyle \theta_f = \theta_i + \omega_i t + \frac{1}{2}\alpha t^2 \\
\Rightarrow \displaystyle \omega_f^2 = \omega_i^2 + 2\alpha (\theta_f - \theta_i)
$

**Instant Angular Acceleration**
$
\displaystyle a_r = \omega^2 r \\
\displaystyle a_t = \frac{d(\omega r)}{dt} = \alpha r
$

**Torque**
$
\displaystyle \tau = rF\sin\phi = Fd = \bm{r \times F} \\~\\
\displaystyle d\tau = r dF_t = (r dm)a_t = (r^2 dm)\alpha \\
\displaystyle \Rightarrow \tau = \alpha \int r^2dm = I\alpha
$

**Rotational Kinetic Energy**
$
\displaystyle I = \sum m_i r_i^2 \\
\displaystyle K_R = \sum \frac{1}{2}m_iv_i^2 = \frac{1}{2}\sum m_i  r_i^2 \omega^2 = \frac{1}{2} I\omega^2
$

**Work and Power**
$
\displaystyle dW = Fds = (F\sin\phi) r\text{d}\theta = \tau \text{d}\theta \\
\displaystyle P = \frac{dW}{dt} = \tau \frac{\text{d}\theta}{dt} = \tau \omega 
\\~\\
\displaystyle
\begin{aligned} 
  W &= \int_{\theta_i}^{\theta_f} \tau \text{d}\theta = \int_{\theta_i}^{\theta_f} I\alpha \text{d}\theta = \int_{\theta_i}^{\theta_f} I\frac{\text{d}\theta}{dt} \frac{d\omega}{\text{d}\theta} \text{d}\theta \\
  &= \int_{\omega_i}^{\omega_f} I\omega d\omega = \frac{1}{2}I\omega_f^2 - \frac{1}{2}I\omega_i^2 
\end{aligned}
$








<br>

### Moment of Inertia of differernt Objects
Thin rod around end : $\displaystyle I = \frac{1}{3}ML^2 $
Thin rod around center : $\displaystyle I = \frac{M}{L} \int_{-L/2}^{L/2} x^2dx = \frac{1}{12}ML^2 = \frac{1}{3}MR^2 $
Thin rectangular plate around coplanar axis (center or edge) : $\displaystyle I = \frac{1}{3}MR^2 $
Thin rectangular plate around perpendicular axis (center or corner) : $\displaystyle I = \int_0^{R_2} dy \int_0^{R_1} \frac{M}{R_1R_2} (x^2 + y^2) dx = \frac{1}{3}M(R_1^2 + R_2^2) $
<br>

Thin circular ring : $\displaystyle I = MR^2 $
Thin cylindrical shell : $\displaystyle I = MR^2 $
Thin circular plate : $\displaystyle I = \int_0^R M\cdot \frac{2\pi r dr}{\pi R^2} \cdot r^2 = \frac{1}{2}MR^2 $
Solid cylinder : $\displaystyle I = \frac{1}{2}MR^2 $
Hollow cylinder : $\displaystyle I = \int_{R_1}^{R_2} M\cdot \frac{2\pi r dr}{\pi (R_2^2-R_1^2)} \cdot r^2 = \frac{1}{2}M(R_1^2 + R_1^2) $
<br>

Solid sphere : $\displaystyle I = \int_{-R}^{R} \frac{1}{2}\rho\pi (R^2-y^2)^2 dy = \frac{2}{5}\cdot (\frac{2}{3}\rho\pi R^3)\cdot R^2 = \frac{2}{5}MR^2 $
Thin spherical shell : $\displaystyle I = \int_0^\pi \rho(R\text{d}\theta \cdot h \cdot 2\pi R \sin\theta)(R\sin\theta)^2 = \frac{2}{3}\cdot (\rho \cdot 4\pi R^2\cdot h)\cdot R^2 = \frac{2}{3}MR^2 $


**The Parallel-Axis Theorem**

$\displaystyle 
\begin{aligned}
I_P &= \sum m_i[(x_i - a)^2 + (y_i - b)^2] \\
    &= \sum m_i(x_i^2 + y_i^2) + (a^2 + b^2)\sum m_i - 2a\sum m_ix_i - 2b\sum m_iy_i \\
    &= I_\text{CM} + md^2
\end{aligned}$







<br>

### Cross product and Coriolis force
The direction of angular velocity obeys **right-hand rule**.
The direction of vector in cross product also obeys **right-hand rule**.

$\bm{C} = \bm{A\times B} = \hat{i}\begin{vmatrix}A_y & A_z \\ B_y & B_z \end{vmatrix} + \hat{j}\begin{vmatrix}A_z & A_x \\ B_z & B_x \end{vmatrix} + \hat{k}\begin{vmatrix}A_x & A_y \\ B_x & B_y \end{vmatrix} $

$\displaystyle \frac{d}{dt} (\bm{A \times B}) = \bm{A \times} \frac{d\bm{B}}{dt} + \frac{d\bm{A}}{dt} \bm{\times B} $

$(\vec{a}\times \vec{b})\cdot(\vec{c}\times \vec{d}) = (\vec{a}\cdot \vec{c})(\vec{b}\cdot \vec{d}) - (\vec{a}\cdot \vec{d})(\vec{b}\cdot \vec{c}) $

$\vec{a}\times(\vec{b}\times \vec{c}) = \vec{b}(\vec{a}\cdot \vec{c}) - \vec{c}(\vec{a}\cdot \vec{b}) $
<br>

$\displaystyle
\vec{v} = \frac{d\vec{r}}{dt} = \vec{\omega} \times \vec{r}$

$\displaystyle
\begin{aligned}
\vec{a} &= \frac{d\vec{v}}{dt} = \frac{d}{dt} (\vec{\omega} \times \vec{r}) = \frac{d\vec{\omega}}{dt} \times \vec{r} + \vec{\omega} \times \frac{d\vec{r}}{dt} \\
  &= \vec{\alpha} \times \vec{r} + \vec{\omega} \times \vec{v} \\
  &= \vec{\alpha} \times \vec{r} + \vec{\omega} \times (\vec{\omega}\times \vec{r}) \\
  &= \vec{a_t} + \vec{a_r} \\
  &\Rightarrow a = r^2\sqrt{\alpha^2 + \omega^4} 
\end{aligned} $

$\displaystyle
\begin{aligned}
K &= \frac{1}{2} \sum m_i|\vec{\omega}\times \vec{r_i}|^2 \\
  &= \frac{1}{2} \sum m_i(\vec{\omega}\times \vec{r_i})\cdot(\vec{\omega}\times \vec{r_i}) \\
  &= \frac{1}{2} \sum m_i[\omega^2r_i^2 - \omega^2(\hat{\omega} \cdot r_i)^2] \\
  &= \frac{1}{2} (\sum m_i r_{i,\perp}^2)\omega^2 = \frac{1}{2}I \omega^2
\end{aligned} $


For the motion in uniform rotating frame:

$\displaystyle \left. \frac{d\vec{r}}{dt}\right|_I = \left.\frac{d\vec{r}}{dt}\right|_R + \vec{\omega}\times \vec{r} = \vec{v}_R + \vec{\omega}\times \vec{r} $

$\displaystyle \left. \frac{d^2\vec{r}}{dt^2}\right|_I = \left.\frac{d^2\vec{r}}{dt^2}\right|_R + 2\vec{\omega}\times \left.\frac{d\vec{r}}{dt}\right|_R + \vec{\omega}\times(\vec{\omega}\times \vec{r}) $

$\vec{F}_R = \vec{F} - 2m\vec{\omega}\times \vec{v}_R - m \vec{\omega}\times(\vec{\omega}\times \vec{r}) \\
\vec{F}_{\text{Coriolis}} = - 2m\vec{\omega}\times \vec{v}_R \\
\vec{F}_{\text{Centrifugal}} = - m \vec{\omega}\times(\vec{\omega}\times \vec{r}) $








<br>

### Angular Momentum
**Kinetic energy of rolling object**
$\displaystyle \begin{aligned}
E &= \frac{1}{2}I_P \omega^2 = \frac{1}{2}(I_\text{CM} + MR^2) \omega^2 \\
&= \frac{1}{2}I_\text{CM} \omega^2 + \frac{1}{2}Mv_\text{CM}^2 \\
&= \frac{1}{2}(\frac{I_\text{CM}}{R^2} + M) v_\text{CM}^2 \\
&= K_r + K_t
\end{aligned} $

**Gravity torque**

$\displaystyle \vec{\tau} = \sum\vec{r}_i \times m_i\vec{g} = \sum(m_i\vec{r}_i)\times \vec{g} = \vec{r}_\text{CM} \times M\vec{g} $
- The center of gravity is located at the center of mass as long as the object is in a uniform gravitational field : $\vec{r}_\text{CM} = \vec{r}_{\text{CG}}$

**Angular Momentum**
$\displaystyle \bm{\tau} = \bm{r\times F} = \bm{r\times}\frac{d\bm{p}}{dt} $

$\displaystyle \frac{d}{dt}(\bm{r\times p}) = \bm{r\times}\frac{d\bm{p}}{dt} + \frac{d\bm{r}}{dt}\bm{\times p} = \bm{r\times F} + \bm{v}\times (m\bm{v}) = \bm{\tau} $

$\Rightarrow \bm{L \equiv r\times p} $

$\displaystyle \sum \bm{\tau}_{ext} = \frac{d\bm{L}}{dt} = 0 \\
\Rightarrow \bm{L} = \text{constant} $

$\displaystyle L_z = \sum r_{i,\perp} (m_i \omega r_{i,\perp}) = \sum (m_ir_{i,\perp}^2)\omega = I\omega \\
\sum \tau_{ext,z} = \frac{dL_z}{dt} = I\frac{d\omega}{dt} = I\alpha $
<br>

$\vec{L} = \sum \vec{r}_i\times (m_i \vec{v}_i) = \sum m_i\vec{r}_i\times (\vec{\omega} \times \vec{r}_i) = \sum m_i[r_i^2\vec{\omega} - \vec{r}_i(\vec{r}_i \times \vec{\omega})] $

$L_x = \omega_x\sum m_i(y_i^2 + z_i^2) - \omega_y\sum m_ix_iy_i - \omega_y\sum m_ix_iz_i \\
L_y = - \omega_x\sum m_iy_ix_i + \omega_y\sum (z_i^2 + x_i^2) - \omega_y\sum m_iy_iz_i \\
L_z = - \omega_x\sum m_iz_ix_i - \omega_y\sum m_iz_iy_i + \omega_y\sum m_i(x_i^2 + y_i^2) \\ $

$\begin{pmatrix} L_x \\ L_y \\ L_z \end{pmatrix}
= \begin{pmatrix}
    I_{xx} & I_{xy} & I{xz} \\
    I_{yx} & I_{yy} & I{yz} \\
    I_{zx} & I_{zy} & I{zz} \\
\end{pmatrix}
\begin{pmatrix} \omega_x \\ \omega_y \\ \omega_z \end{pmatrix} $






