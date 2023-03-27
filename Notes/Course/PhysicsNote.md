<!-- TOC -->

- [Newton's Laws and Conservation Laws](#newtons-laws-and-conservation-laws)
  - [Conservation of Momentum](#conservation-of-momentum)
    - [Elastic Collision in 1D](#elastic-collision-in-1d)
    - [Elastic Collision in 2D](#elastic-collision-in-2d)
  - [Center of Mass](#center-of-mass)
    - [Perfectly inelastic scattering in CM Frame](#perfectly-inelastic-scattering-in-cm-frame)
    - [Elastic scattering in CM Frame](#elastic-scattering-in-cm-frame)
  - [Gravitation](#gravitation)
    - [Rocket Propulsion](#rocket-propulsion)
- [Rotational Motion](#rotational-motion)
  - [Formulas](#formulas)
  - [Moment of Inertia of differernt Objects](#moment-of-inertia-of-differernt-objects)
  - [Cross product](#cross-product)

<!-- /TOC -->





## Newton's Laws and Conservation Laws
### Conservation of Momentum
$
\displaystyle \frac{1}{2}m_1v_{1i}^2 + \frac{1}{2}m_2v_{2i}^2 = \frac{1}{2}m_1v_{1f}^2 + \frac{1}{2}m_2v_{2f}^2 + \Delta E_{internal} + \Delta U
\\~\\
\Rightarrow m_1v_{1i} + m_2v_{2i} = m_1v_{1f} + m_2v_{2f}
$

#### Elastic Collision in 1D
$
\displaystyle v_{1f} = \frac{m_1-m_2}{m_1+m_2} v_{1i} + \frac{2m_2}{m_1+m_2} v_{2i}
\\~\\
\displaystyle v_{2f} = \frac{2m_1}{m_1+m_2} v_{1i} + \frac{m_2 - m_1}{m_1+m_2} v_{2i}
\\~\\
When \; m_1 >> m_2, v_{1f} = v_{1i}, v_{2f} = 2v_{1i} - v_{2i} \\
When \; m_1 = m_2, v_{1f} = v_{2i}, v_{2f} = v_{1i}
$

#### Elastic Collision in 2D
$
\begin{cases}
m_1v_{1f}cos\theta + m_2v_{2f}cos\phi = m_1v_{1i} \\
m_1v_{1f}sin\theta - m_2v_{2f}sin\phi = 0 \\
\displaystyle \frac{1}{2}m_1v_{1i}^2 = \frac{1}{2}m_1v_{1f}^2 + \frac{1}{2}m_2v_{2f}^2
\end{cases}
\\~\\
When \; m_1 = m_2 \; and \; v_{2i} = 0, \bold{v_{1f} \cdot v_{2f}} = 0
$




### Center of Mass
$$
\displaystyle x_{CM} = \lim_{\Delta m_i \rightarrow 0} \frac{\sum x_i \Delta m_i}{M} = \frac{1}{M} \int x dm
$$
$
\displaystyle \bold{r_{CM}} = \frac{\sum m_i \bold{r_i}}{M} \\~\\
\displaystyle \bold{v_{CM}} = \frac{\sum m_i \bold{v_i}}{M} \\~\\
\displaystyle \bold{a_{CM}} = \frac{\sum m_i \bold{a_i}}{M} \\~\\
\displaystyle \bold{p_{CM}} = \sum m_i\bold{v_i} = M\bold{v_{CM}} \\~\\
\begin{aligned}
E_k &= \sum \frac{1}{2} m_i (v_i' + v_{CM})(v_i' + v_{CM}) \\
    &= \sum \frac{1}{2} m_i v_{CM}^2 + \sum m_i v_i' v_{CM} + \sum \frac{1}{2} m_i v_i'^2 \\
    &= \frac{1}{2} v_{CM}^2 \sum m_i + \sum \frac{1}{2} m_i v_i'^2 + v_{CM} \sum m_i v_i' \\
    &= \frac{1}{2} v_{CM}^2 M + \sum \frac{1}{2} m_i v_i'^2 + v_{CM}\frac{d}{dt} \sum m_i r_i' \\
    &= E_{Kcm} + E_k'
\end{aligned}
$

#### Perfectly inelastic scattering in CM Frame
$
\displaystyle v_{1i}' = v_{1i} - v_{CM} = \frac{m_2}{m_1+m_2} (v_{1i} - v_{2i}) \\~\\
\displaystyle v_{2i}' = v_{2i} - v_{CM} = \frac{m_1}{m_1+m_2} (v_{2i} - v_{1i}) \\~\\
\displaystyle v_{1f}' = v_{2f}' = 0
$
#### Elastic scattering in CM Frame
$
\displaystyle v_{1i}' = v_{1i} - v_{CM} = \frac{m_2}{m_1+m_2} (v_{1i} - v_{2i}) \\~\\
\displaystyle v_{2i}' = v_{2i} - v_{CM} = \frac{m_1}{m_1+m_2} (v_{2i} - v_{1i}) \\~\\
\displaystyle v_{1f}' = v_{1f} - v_{CM} = \frac{m_2}{m_1+m_2} (v_{2i} - v_{1i}) \\~\\
\displaystyle v_{2f}' = v_{2i} - v_{CM} = \frac{m_1}{m_1+m_2} (v_{1i} - v_{2i}) \\~\\
$



### Gravitation
$
\displaystyle F = G \frac{Mm}{r^2} \\~\\
\displaystyle \frac{GM}{r^2} = a = \omega^2 r = \frac{4\pi^2 r}{T^2} \\~\\
\displaystyle Circular \; Orbit : E = \frac{1}{2}mv^2 - \frac{GMm}{r} = -\frac{GMm}{2r} \\
\displaystyle v_1 = \sqrt{\frac{GM}{R}} \\
\displaystyle v_2 = \sqrt{\frac{2GM}{R}} \\
$

#### Rocket Propulsion
$
\displaystyle M dv = v_e dm = -v_e dM \\
\displaystyle \Rightarrow v_f - v_i = v_e \ln(\frac{M_i}{M_f}) \\~\\
\displaystyle Ma = Mg + v_e \frac{dM}{dt} \\
\displaystyle \Rightarrow v = v_e \ln(\frac{M_0}{M}) - gt
$









## Rotational Motion
### Formulas
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
\displaystyle \tau = rF\sin\phi = Fd = \bold{F \times r} \\~\\
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
\displaystyle dW = Fds = (F\sin\phi) rd\theta = \tau d\theta \\
\displaystyle P = \frac{dW}{dt} = \tau \frac{d\theta}{dt} = \tau \omega 
\\~\\
\displaystyle
\begin{aligned} 
W &= \int_{\theta_i}^{\theta_f} \tau d\theta = \int_{\theta_i}^{\theta_f} I\alpha d\theta = \int_{\theta_i}^{\theta_f} I\frac{d\theta}{dt} \frac{d\omega}{d\theta} d\theta \\
&= \int_{\omega_i}^{\omega_f} I\omega d\omega = \frac{1}{2}I\omega_f^2 - \frac{1}{2}I\omega_i^2 
\end{aligned}
$

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

Solid sphere : $\displaystyle I = \frac{2}{5}MR^2 $
Thin spherical shell : $\displaystyle I = \frac{2}{3}MR^2 $

**The Parallel-Axis Theorem**
$\displaystyle 
\begin{aligned}
I_P &= \sum m_i[(x_i - a)^2 + (y_i - b)^2] \\
    &= \sum m_i(x_i^2 + y_i^2) + (a^2 + b^2)\sum m_i - 2a\sum m_ix_i - 2b\sum m_iy_i \\
    &= I_{CM} + md^2
\end{aligned}$



$\displaystyle a = \frac{(m_1 - m_2)g}{m_1 + m_2 + \frac{nI}{R^2}} $

### Cross product
- The direction of angular velocity obeys **right-hand rule**
- The direction of vector in cross product also obeys **right-hand rule**

$\displaystyle \frac{d}{dt} (\bold{A \times B}) = \bold{A \times} \frac{d\bold{B}}{dt} + \frac{d\bold{A}}{dt} \bold{\times B}
\\~\\
\vec{v} = \frac{d\vec{r}}{dt} = \vec{\omega} \times \vec{r} \\~\\
\vec{a} = \frac{d\vec{v}}{dt} = \frac{d}{dt} (\vec{\omega} \times \vec{r}) = \frac{d\vec{\omega}}{dt} \times \vec{r} + \vec{\omega} \times \frac{d\vec{r}}{dt} = \vec{\alpha} \times \vec{r} + \vec{\omega} \times \vec{v}
$
