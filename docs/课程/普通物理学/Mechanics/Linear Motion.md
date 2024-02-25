
- [Newton's Laws and Conservation Laws](#newtons-laws-and-conservation-laws)
    - [Elastic Collision in 1D](#elastic-collision-in-1d)
    - [Elastic Collision in 2D](#elastic-collision-in-2d)
- [Center of Mass](#center-of-mass)
    - [Perfectly Elastic Collision in CM Frame](#perfectly-elastic-collision-in-cm-frame)
    - [Perfectly inelastic scattering in CM Frame](#perfectly-inelastic-scattering-in-cm-frame)
- [Gravitation](#gravitation)
    - [The Law of Gravitation](#the-law-of-gravitation)
    - [Rocket Propulsion](#rocket-propulsion)








### Newton's Laws and Conservation Laws
#### Elastic Collision in 1D
The coefficient of restitution is $$e = \frac{v_{2f} - v_{1f}}{v_{1i} - v_{2i}}$$

When $e = 1$, the collision is **perfectly elastic collision**.
When $0 \le e \lt 1$, the collision is **inelastic collision**.
When $e = 0$, the collision is **perfectly inelastic collision**.

In the perfectly elastic collision,

$$
\begin{gathered}
  v_{1f} = \frac{m_1-m_2}{m_1+m_2} v_{1i} + \frac{2m_2}{m_1+m_2} v_{2i} = 2v_{CM} - v_{1i} \\\\
  v_{2f} = \frac{2m_1}{m_1+m_2} v_{1i} + \frac{m_2 - m_1}{m_1+m_2} v_{2i} = 2v_{CM} - v_{2i}
\end{gathered}
$$

When  $m_1 >> m_2$, we can get $v_{1f} = v_{1i}$, $v_{2f} = 2v_{1i} - v_{2i}$.
When  $m_1 = m_2$, we can get $v_{1f} = v_{2i}$, $v_{2f} = v_{1i}$.

<br>

#### Elastic Collision in 2D
$$
\begin{cases}
  m_1v_{1f}\cos\theta + m_2v_{2f}\cos\phi = m_1v_{1i} \\
  m_1v_{1f}\sin\theta - m_2v_{2f}\sin\phi = 0 \\
  \displaystyle \frac{1}{2}m_1v_{1i}^2 = \frac{1}{2}m_1v_{1f}^2 + \frac{1}{2}m_2v_{2f}^2
\end{cases}
$$

When $m_1 = m_2$ and $v_{2i} = 0$, we can get $\boldsymbol{v}_{1f} \cdot \boldsymbol{v}_{2f} = 0$







<br>

### Center of Mass
$$x_\text{CM} = \lim_{\Delta m_i \rightarrow 0} \frac{\sum x_i \Delta m_i}{M} = \frac{1}{M} \int x dm$$

$$\boldsymbol{r}_\text{CM} = \frac{\sum m_i \boldsymbol{r}_i}{M}$$

$$\boldsymbol{v}_\text{CM} = \frac{\sum m_i \boldsymbol{v}_i}{M}$$

$$\boldsymbol{a}_\text{CM} = \frac{\sum m_i \boldsymbol{a}_i}{M}$$

$$\boldsymbol{p}_\text{CM} = \sum m_i\boldsymbol{v}_i = M\boldsymbol{v}_\text{CM}$$

The kinetic energy of a system is equal to the kinetic energy of its center of mass plus its kinetic energy in the CM frame.

$$
\begin{aligned}
  E_k &= \sum \frac{1}{2} m_i (v_i' + v_\text{CM})(v_i' + v_\text{CM}) \\
  &= \sum \frac{1}{2} m_i v_\text{CM}^2 + \sum m_i v_i' v_\text{CM} + \sum \frac{1}{2} m_i v_i'^2 \\
  &= \frac{1}{2} v_\text{CM}^2 \sum m_i + \sum \frac{1}{2} m_i v_i'^2 + v_\text{CM} \sum m_i v_i' \\
  &= \frac{1}{2} v_\text{CM}^2 M + \sum \frac{1}{2} m_i v_i'^2 + v_\text{CM}\frac{d}{dt} \sum m_i r_i' \\
  &= E_{Kcm} + E_k'
\end{aligned}
$$

<br>

#### Perfectly Elastic Collision in CM Frame
$$
\begin{gathered}
  v_{1i}' = v_{1i} - v_\text{CM} = \frac{m_2}{m_1+m_2} (v_{1i} - v_{2i}) \\\\
  v_{2i}' = v_{2i} - v_\text{CM} = \frac{m_1}{m_1+m_2} (v_{2i} - v_{1i}) \\\\
  v_{1f}' = -v_{1i}' \\\\
  v_{2f}' = -v_{2i}'
\end{gathered}
$$

<br>

#### Perfectly inelastic scattering in CM Frame
$$
\begin{gathered}
  v_{1i}' = v_{1i} - v_\text{CM} = \frac{m_2}{m_1+m_2} (v_{1i} - v_{2i}) \\\\
  v_{2i}' = v_{2i} - v_\text{CM} = \frac{m_1}{m_1+m_2} (v_{2i} - v_{1i}) \\\\
  v_{1f}' = v_{2f}' = 0
\end{gathered}
$$








<br>

### Gravitation
#### The Law of Gravitation
The law of gravitation is $$F = G \frac{Mm}{R^2}$$

So the period at an circular orbit is

$$
\begin{gathered}
  \frac{GM}{R^2} = \omega^2 R = \frac{4\pi^2}{T^2}R \\\\
  \Rightarrow \frac{T^2}{R^3} = \frac{4\pi^2}{GM} \\\\
  \Rightarrow T = 2\pi\sqrt{\frac{R^3}{GM}}
\end{gathered}
$$

And the corresponding speed is

$$
\begin{gathered}
  \frac{GM}{r^2} = \frac{v^2}{r} \\\\
  \Rightarrow v = \sqrt{\frac{GM}{r}}
\end{gathered}
$$

Then we can get the energy of the satellite $$E = \frac{1}{2}mv^2 - \frac{GMm}{r} = -\frac{GMm}{2r}$$

<br>

#### Rocket Propulsion
The first cosmic speed is $v_1 = \sqrt{\frac{GM}{R}}$.

The second cosmic speed is $v_1 = \sqrt{\frac{2GM}{R}}$.

Let $m$ be the mass of the ejected medium in an instant, $v_e$ the speed of the medium relative to the rocket, then we can get 

$$
\begin{gathered}
  M dv = v_e dm = -v_e dM \\\\
  \Rightarrow dv = -v_e \frac{dM}{M} \\\\
  \Rightarrow v_f - v_i = v_e \ln \frac{M_i}{M_f}
\end{gathered}
$$

Plus, taking the gravity into consideration, we can get

$$
\begin{gathered}
  Ma = -v_e \frac{dM}{M} - gt \\\\
  \Rightarrow adt = v_e \frac{dM}{M} - gdt \\\\
  \Rightarrow v = v_e \ln(\frac{M_0}{M}) - gt
\end{gathered}
$$





