<!-- TOC -->

- [Mechanics](#mechanics)
  - [Conservation of Momentum](#conservation-of-momentum)
    - [Elastic Collision in 1D](#elastic-collision-in-1d)
    - [Elastic Collision in 2D](#elastic-collision-in-2d)
  - [Center of Mass](#center-of-mass)
    - [Perfectly inelastic scattering in CM Frame](#perfectly-inelastic-scattering-in-cm-frame)
    - [Elastic scattering in CM Frame](#elastic-scattering-in-cm-frame)
  - [Gravitation](#gravitation)
    - [Rocket Propulsion](#rocket-propulsion)
  - [Rotational Motion](#rotational-motion)

<!-- /TOC -->





## Mechanics
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


### Rotational Motion
**Constant Angular Acceleration**
$
\displaystyle \omega_f = \omega_i + \alpha t \\
\displaystyle \theta_f = \theta_i + \omega_i t + \frac{1}{2}\alpha t^2 \\
\displaystyle \omega_f^2 = \omega_i^2 + 2\alpha (\theta_f - \theta_i)
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
\displaystyle \tau = I\alpha = I\frac{d\omega}{dt} = I\omega\frac{d\omega}{d\theta} \\
\displaystyle \Rightarrow \tau d\theta = I\omega d\omega \\
\displaystyle W = \int_{\theta_i}^{\theta_f} \tau d\theta = \int_{\omega_i}^{\omega_f} I\omega d\omega = \frac{1}{2}I\omega_f^2 - \frac{1}{2}I\omega_i^2
$



