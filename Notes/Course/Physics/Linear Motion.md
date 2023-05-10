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
\text{When } m_1 >> m_2, v_{1f} = v_{1i}, v_{2f} = 2v_{1i} - v_{2i} \\
\text{When } m_1 = m_2, v_{1f} = v_{2i}, v_{2f} = v_{1i}
$

#### Elastic Collision in 2D
$
\begin{cases}
m_1v_{1f}\cos\theta + m_2v_{2f}\cos\phi = m_1v_{1i} \\
m_1v_{1f}\sin\theta - m_2v_{2f}\sin\phi = 0 \\
\displaystyle \frac{1}{2}m_1v_{1i}^2 = \frac{1}{2}m_1v_{1f}^2 + \frac{1}{2}m_2v_{2f}^2
\end{cases}
\\~\\
\text{When } m_1 = m_2 \; and \; v_{2i} = 0, \bm{v}_{1f} \cdot \bm{v}_{2f} = 0
$




### Center of Mass
$$
\displaystyle x_\text{CM} = \lim_{\Delta m_i \rightarrow 0} \frac{\sum x_i \Delta m_i}{M} = \frac{1}{M} \int x dm
$$
$
\displaystyle \bm{r}_\text{CM} = \frac{\sum m_i \bm{r}_i}{M} \\~\\
\displaystyle \bm{v}_\text{CM} = \frac{\sum m_i \bm{v}_i}{M} \\~\\
\displaystyle \bm{a}_\text{CM} = \frac{\sum m_i \bm{a}_i}{M} \\~\\
\displaystyle \bm{p}_\text{CM} = \sum m_i\bm{v}_i = M\bm{v}_\text{CM} \\~\\
\begin{aligned}
E_k &= \sum \frac{1}{2} m_i (v_i' + v_\text{CM})(v_i' + v_\text{CM}) \\
    &= \sum \frac{1}{2} m_i v_\text{CM}^2 + \sum m_i v_i' v_\text{CM} + \sum \frac{1}{2} m_i v_i'^2 \\
    &= \frac{1}{2} v_\text{CM}^2 \sum m_i + \sum \frac{1}{2} m_i v_i'^2 + v_\text{CM} \sum m_i v_i' \\
    &= \frac{1}{2} v_\text{CM}^2 M + \sum \frac{1}{2} m_i v_i'^2 + v_\text{CM}\frac{d}{dt} \sum m_i r_i' \\
    &= E_{Kcm} + E_k'
\end{aligned}
$

#### Perfectly inelastic scattering in CM Frame
$
\displaystyle v_{1i}' = v_{1i} - v_\text{CM} = \frac{m_2}{m_1+m_2} (v_{1i} - v_{2i}) \\~\\
\displaystyle v_{2i}' = v_{2i} - v_\text{CM} = \frac{m_1}{m_1+m_2} (v_{2i} - v_{1i}) \\~\\
\displaystyle v_{1f}' = v_{2f}' = 0
$
#### Elastic scattering in CM Frame
$
\displaystyle v_{1i}' = v_{1i} - v_\text{CM} = \frac{m_2}{m_1+m_2} (v_{1i} - v_{2i}) \\~\\
\displaystyle v_{2i}' = v_{2i} - v_\text{CM} = \frac{m_1}{m_1+m_2} (v_{2i} - v_{1i}) \\~\\
\displaystyle v_{1f}' = v_{1f} - v_\text{CM} = \frac{m_2}{m_1+m_2} (v_{2i} - v_{1i}) \\~\\
\displaystyle v_{2f}' = v_{2i} - v_\text{CM} = \frac{m_1}{m_1+m_2} (v_{1i} - v_{2i}) \\~\\
$



### Gravitation
$
\displaystyle F = G \frac{Mm}{r^2} \\~\\
\displaystyle \frac{GM}{r^2} = a = \omega^2 r = \frac{4\pi^2 r}{T^2} \\~\\
\displaystyle \text{Circular Orbit : } E = \frac{1}{2}mv^2 - \frac{GMm}{r} = -\frac{GMm}{2r} \\
\displaystyle v_1 = \sqrt{\frac{GM}{R}} \\
\displaystyle v_2 = \sqrt{\frac{2GM}{R}} \\
$

#### Rocket Propulsion
$
\displaystyle M dv = v_e dm = -v_e dM \\
\displaystyle \Rightarrow v_f - v_i = v_e \ln(\frac{M_i}{M_f}) \\~\\
\displaystyle Ma = -Mg + v_e \frac{dM}{dt} \\
\displaystyle \Rightarrow v = v_e \ln(\frac{M_0}{M}) - gt
$







