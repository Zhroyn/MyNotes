
- [Rotational Motion](#rotational-motion)
    - [Common Formulas](#common-formulas)
        - [Constant Angular Acceleration](#constant-angular-acceleration)
        - [Instant Angular Acceleration](#instant-angular-acceleration)
        - [Torque](#torque)
        - [Rotational Kinetic Energy](#rotational-kinetic-energy)
        - [Work and Power](#work-and-power)
    - [Moment of Inertia of differernt Objects](#moment-of-inertia-of-differernt-objects)
    - [Cross product and Coriolis force](#cross-product-and-coriolis-force)
    - [Angular Momentum](#angular-momentum)
        - [Gravity torque](#gravity-torque)
        - [Angular Momentum](#angular-momentum-1)







## Rotational Motion
### Common Formulas
#### Constant Angular Acceleration
$$\omega_f = \omega_i + \alpha t$$

$$\theta_f = \theta_i + \omega_i t + \frac{1}{2}\alpha t^2$$

$$\omega_f^2 = \omega_i^2 + 2\alpha (\theta_f - \theta_i)$$

#### Instant Angular Acceleration
$$a_r = \omega^2 r$$

$$a_t = \frac{d(\omega r)}{dt} = \alpha r$$

#### Torque
$$\tau = rF\sin\phi = Fd = \boldsymbol{r} \times \boldsymbol{F}$$

$$
\begin{gathered}
  d\tau = r dF_t = (r dm)a_t = (r^2 dm)\alpha \\
  \Rightarrow \tau = \alpha \int r^2dm = I\alpha
\end{gathered}
$$

#### Rotational Kinetic Energy
$$I = \sum m_i r_i^2$$

$$K_R = \sum \frac{1}{2}m_iv_i^2 = \frac{1}{2}\sum m_i  r_i^2 \omega^2 = \frac{1}{2} I\omega^2$$


#### Work and Power
$$dW = Fds = (F\sin\phi) r\text{d}\theta = \tau \text{d}\theta$$

$$P = \frac{dW}{dt} = \tau \frac{\text{d}\theta}{dt} = \tau \omega$$

$$
\begin{aligned} 
  W &= \int_{\theta_i}^{\theta_f} \tau \text{d}\theta = \int_{\theta_i}^{\theta_f} I\alpha \text{d}\theta = \int_{\theta_i}^{\theta_f} I\frac{\text{d}\theta}{dt} \frac{d\omega}{\text{d}\theta} \text{d}\theta \\
  &= \int_{\omega_i}^{\omega_f} I\omega d\omega = \frac{1}{2}I\omega_f^2 - \frac{1}{2}I\omega_i^2 
\end{aligned}
$$








<br>

### Moment of Inertia of differernt Objects
- Thin rod around end : $\displaystyle I = \frac{1}{3}ML^2 $
- Thin rod around center : $\displaystyle I = \frac{M}{L} \int_{-L/2}^{L/2} x^2dx = \frac{1}{12}ML^2 = \frac{1}{3}MR^2 $
- Thin rectangular plate around coplanar axis (center or edge) : $\displaystyle I = \frac{1}{3}MR^2 $
- Thin rectangular plate around perpendicular axis (center or corner) : $\displaystyle I = \int_0^{R_2} dy \int_0^{R_1} \frac{M}{R_1R_2} (x^2 + y^2) dx = \frac{1}{3}M(R_1^2 + R_2^2) $

<br>

- Thin circular ring : $\displaystyle I = MR^2 $
- Thin cylindrical shell : $\displaystyle I = MR^2 $
- Thin circular plate : $\displaystyle I = \int_0^R M\cdot \frac{2\pi r dr}{\pi R^2} \cdot r^2 = \frac{1}{2}MR^2 $
- Solid cylinder : $\displaystyle I = \frac{1}{2}MR^2 $
- Hollow cylinder : $\displaystyle I = \int_{R_1}^{R_2} M\cdot \frac{2\pi r dr}{\pi (R_2^2-R_1^2)} \cdot r^2 = \frac{1}{2}M(R_1^2 + R_1^2) $

<br>

- Solid sphere : $\displaystyle I = \int_{-R}^{R} \frac{1}{2}\rho\pi (R^2-y^2)^2 dy = \frac{2}{5}\cdot (\frac{2}{3}\rho\pi R^3)\cdot R^2 = \frac{2}{5}MR^2 $
- Thin spherical shell : $\displaystyle I = \int_0^\pi \rho(R\text{d}\theta \cdot h \cdot 2\pi R \sin\theta)(R\sin\theta)^2 = \frac{2}{3}\cdot (\rho \cdot 4\pi R^2\cdot h)\cdot R^2 = \frac{2}{3}MR^2 $

<br>

**The Parallel-Axis Theorem**

$$
\begin{aligned}
  I_P &= \sum m_i[(x_i - a)^2 + (y_i - b)^2] \\
  &= \sum m_i(x_i^2 + y_i^2) + (a^2 + b^2)\sum m_i - 2a\sum m_ix_i - 2b\sum m_iy_i \\
  &= I_\text{CM} + md^2
\end{aligned}
$$







<br>

### Cross product and Coriolis force
The direction of angular velocity obeys **right-hand rule**.

The direction of vector in cross product also obeys **right-hand rule**.

Below are some formulas for cross product:

$$
\boldsymbol{C} = \boldsymbol{A} \times \boldsymbol{B} = \hat{i}
\begin{vmatrix}
  A_y & A_z \\
  B_y & B_z
\end{vmatrix} + \hat{j}
\begin{vmatrix}
  A_z & A_x \\
  B_z & B_x
\end{vmatrix} + \hat{k}
\begin{vmatrix}
  A_x & A_y \\
  B_x & B_y
\end{vmatrix}
$$

$$
\frac{d}{dt} (\boldsymbol{A} \times \boldsymbol{B}) = \boldsymbol{A} \times \frac{d\boldsymbol{B}}{dt} + \frac{d\boldsymbol{A}}{dt} \times \boldsymbol{B}
$$

$$
(\vec{a}\times \vec{b})\cdot(\vec{c}\times \vec{d}) = (\vec{a}\cdot \vec{c})(\vec{b}\cdot \vec{d}) - (\vec{a}\cdot \vec{d})(\vec{b}\cdot \vec{c})
$$

$$
\vec{a}\times(\vec{b}\times \vec{c}) = \vec{b}(\vec{a}\cdot \vec{c}) - \vec{c}(\vec{a}\cdot \vec{b})
$$

For velocity and acceleration:

$$
\vec{v} = \frac{d\vec{r}}{dt} = \vec{\omega} \times \vec{r}
$$

$$
\begin{aligned}
  \vec{a} &= \frac{d\vec{v}}{dt} = \frac{d}{dt} (\vec{\omega} \times \vec{r}) = \frac{d\vec{\omega}}{dt} \times \vec{r} + \vec{\omega} \times \frac{d\vec{r}}{dt} \\
  &= \vec{\alpha} \times \vec{r} + \vec{\omega} \times \vec{v} \\
  &= \vec{\alpha} \times \vec{r} + \vec{\omega} \times (\vec{\omega}\times \vec{r}) \\
  &= \vec{a_t} + \vec{a_r} \\
  &\Rightarrow a = r^2\sqrt{\alpha^2 + \omega^4} 
\end{aligned}
$$

For kinetic energy of pure rolling object:

$$
\begin{aligned}
  K &= \frac{1}{2} \sum m_i|\vec{\omega}\times \vec{r_i}|^2 \\
  &= \frac{1}{2} \sum m_i(\vec{\omega}\times \vec{r_i})\cdot(\vec{\omega}\times \vec{r_i}) \\
  &= \frac{1}{2} \sum m_i[\omega^2r_i^2 - \omega^2(\hat{\omega} \cdot r_i)^2] \\
  &= \frac{1}{2} (\sum m_i r_{i,\perp}^2)\omega^2 = \frac{1}{2}I \omega^2
\end{aligned}
$$

For kinetic energy of rolling object:

$$
\begin{aligned}
E &= \frac{1}{2}I_P \omega^2 = \frac{1}{2}(I_\text{CM} + MR^2) \omega^2 \\
&= \frac{1}{2}I_\text{CM} \omega^2 + \frac{1}{2}Mv_\text{CM}^2 \\
&= \frac{1}{2}(\frac{I_\text{CM}}{R^2} + M) v_\text{CM}^2 \\
&= K_r + K_t
\end{aligned}
$$

For the motion in uniform rotating frame:

$$
\left. \frac{d\vec{r}}{dt}\right|_I = \left.\frac{d\vec{r}}{dt}\right|_R + \vec{\omega}\times \vec{r} = \vec{v}_R + \vec{\omega}\times \vec{r}
$$

$$
\left. \frac{d^2\vec{r}}{dt^2}\right|_I = \left.\frac{d^2\vec{r}}{dt^2}\right|_R + 2\vec{\omega}\times \left.\frac{d\vec{r}}{dt}\right|_R + \vec{\omega}\times(\vec{\omega}\times \vec{r})
$$

$$
\begin{aligned}
  & \vec{F}_R = \vec{F} - 2m\vec{\omega}\times \vec{v}_R - m \vec{\omega}\times(\vec{\omega}\times \vec{r}) \\
  & \vec{F}_{\text{Coriolis}} = - 2m\vec{\omega}\times \vec{v}_R \\
  & \vec{F}_{\text{Centrifugal}} = - m \vec{\omega}\times(\vec{\omega}\times \vec{r}) \\
\end{aligned}
$$








<br>

### Angular Momentum
#### Gravity torque
$$
\vec{\tau} = \sum\vec{r}_i \times m_i\vec{g} = \sum(m_i\vec{r}_i)\times \vec{g} = \vec{r}_\text{CM} \times M\vec{g}
$$

The center of gravity is located at the center of mass as long as the object is in a uniform gravitational field: $\vec{r}_\text{CM} = \vec{r}_{\text{CG}}$

<br>

#### Angular Momentum
First we have $$\boldsymbol{\tau} = \boldsymbol{r} \times \boldsymbol{F} = \boldsymbol{r} \times \frac{d\boldsymbol{p}}{dt}$$

Then we have $$\frac{d}{dt}(\boldsymbol{r} \times \boldsymbol{p}) = \boldsymbol{r} \times \frac{d\boldsymbol{p}}{dt} + \frac{d\boldsymbol{r}}{dt} \times \boldsymbol{p} = \boldsymbol{r} \times \boldsymbol{F} + \boldsymbol{v} \times (m\boldsymbol{v}) = \boldsymbol{\tau}$$

So the angular momentum can be defined as $$\boldsymbol{L} = \boldsymbol{r} \times \boldsymbol{p}$$

Because $\tau = dL/dt$, when external torque is zero, the angular momentum is constant.

The common formulas for angular momentum and torque are: $$L_z = \sum r_{i,\perp} (m_i \omega r_{i,\perp}) = \sum (m_ir_{i,\perp}^2)\omega = I\omega$$ $$\sum \tau_{ext,z} = \frac{dL_z}{dt} = I\frac{d\omega}{dt} = I\alpha$$




