
- [Wave Optics](#wave-optics)
  - [Steady Wave](#steady-wave)
  - [Wave Superposition and Interference](#wave-superposition-and-interference)
    - [Young’s Double Slit Quantitative](#youngs-double-slit-quantitative)
    - [Thin Film Interference](#thin-film-interference)
  - [Diffraction](#diffraction)
    - [Single-slit Diffraction](#single-slit-diffraction)
    - [Fraunhofer Diffraction at Circular Aperture and Angular Resolution](#fraunhofer-diffraction-at-circular-aperture-and-angular-resolution)
  - [Gratings](#gratings)
  - [Dispersion and resolving power](#dispersion-and-resolving-power)





# Wave Optics
## Steady Wave
There are two forms of steady wave. One is steady vecter wave, like the EM wave:
$$
\begin{cases}
  \vec{E}(P, t) = \vec{E}_0(P) \cos (\omega t - \phi(P)) \\
  \vec{H}(P, t) = \vec{H}_0(P) \cos (\omega t - \phi(P))
\end{cases}
$$

The other is steady scalar wave: 
$$
U(P, t) = A(P) \cos (\omega t - \phi(P)) \\~\\
\tilde{U}(P, t) = A(P) e^{i(\phi(P) - \omega t)} = A(P) e^{i\phi(P)} e^{-i\omega t} \\~\\
\tilde{U}(P) = A(P) e^{i\phi(P)}
$$

For steady plane wave, we have
$$
\begin{cases}
  A(P) = \text{constant} \\
  \phi(P) = \vec{k} \bullet \vec{r} = k_x x + k_y y + k_z z + \phi_0
\end{cases}
\\~\\
\tilde{U}(P) = A e^{i\phi(P)} = A e^{i(\vec{k} \bullet \vec{r} + \phi_0)} = A e^{i(k_x x + k_y y + k_z z + \phi_0)}
$$

For steady spherical wave, we have
$$
\begin{cases}
  A(P) = \dfrac{a}{r} \\
  \phi(P) = kr + \phi_0
\end{cases}
\\~\\
\tilde{U}(P) = \frac{a}{r} e^{i(kr + \phi_0)}
$$

The wave intensity is $$I(P) = [A(P)]^2 = \tilde{U}^*(P) \cdot \tilde{U}(P)$$








<br>

## Wave Superposition and Interference
The wave superposition principle is that, for scalar wave, the resultant wave is the sum of all the waves; For vector wave, the resultant wave is the vector sum of all the waves.

When two waves interfere, the intensity of the resultant wave is
$$
\begin{aligned}
  I(P, t) &= \tilde{U}^*(P, t) \cdot \tilde{U}(P, t) \\
  &= \left( A_1 e^{-i\phi_1} e^{i\omega_1 t} + A_2 e^{-i\phi_2} e^{i\omega_2 t} \right) \left( A_1 e^{i\phi_1} e^{-i\omega_1 t} + A_2 e^{i\phi_2} e^{-i\omega_2 t} \right) \\
  &= A_1^2 + A_2^2 + 2A_1A_2 \cos [(\phi_1 - \phi_2) - (\omega_1 - \omega_2)t] \\
  &= I_1 + I_2 + 2\sqrt{I_1I_2} \cos [(\phi_1 - \phi_2) - (\omega_1 - \omega_2)t]
\end{aligned}
$$

So if $\delta(P) = \phi_1 - \phi_2$ is not steady, or $\omega_1 \neq \omega_2$, no interference will occur. If $\delta$ changes with time, we call it incohrent.

For two spherical plane waves, if $\phi_1 = \phi_2$, then $$\delta(P) = \frac{2\pi}{\lambda} (r_1 - r_2)$$

If $\Delta L = r_1 - r_2 = m\lambda$, $I(P)$ is maximum; If $\Delta L = r_1 - r_2 = (m + \dfrac{1}{2})\lambda$, $I(P)$ is minimum.



<br>

### Young’s Double Slit Quantitative
In Young’s double slit expriment, we have $$\Delta L = d\sin\theta, \quad \sin\theta = \frac{y}{L}$$

So constructive interference happens at $y = \dfrac{m\lambda L}{d}$.

Destructive interference happens at $y = \dfrac{(m + \dfrac{1}{2})\lambda L}{d}$.



<br>

### Thin Film Interference
If $n_1 > n_2$, no phase change upon reflection.

If $n_1 < n_2$, phase change of $180^{\circ}$ upon reflection, equivalent to the wave shifting by $\lambda/2$.

If the thickness is the same at every point, fringes of equal inclination will appear:
$$
\begin{aligned}
  \Delta L &= (ARC) - (AB) \\
  &= n \frac{2h}{\cos i} - n_1 \cdot 2h\tan i \cdot \sin i_1 \\
  &= 2h (\frac{n}{\cos i} - \frac{n_1\sin i_1 \sin i}{\cos i}) \\
  &= 2nh (\frac{1}{\cos i} - \frac{\sin^2 i}{\cos i}) \\
  &= 2nh\cos i
\end{aligned}
$$

Consider the half-wave loss, $\Delta L = 2nh\cos i + \lambda/2$.

$$
\cos i_{m+1} - \cos i_m = -\sin i (i_{m+1} - i_m) = \frac{\lambda}{2nh} \\~\\
\Delta r_m = r_{m+1} - r_m = f(i_{m+1} - i_m) = - \frac{f\lambda}{2nh\sin i_m}
$$

So the fringes of equal inclination are internally sparse and externally dense. Moreover, $n$ or $h$ is bigger, $\Delta r$ is smaller.

---
If the thickness is the same at every point, fringes of equal thickness will appear. The difference of optical path is: 
$$
\begin{aligned}
  \Delta L &= (QABP) - (QP) \\
  &= (QA) - (QP) + (ABP) \\
  &= -n AP \sin i + 2(AB) \\
  &= -n \cdot (2h\tan i) \cdot \sin i + \frac{2nh}{\cos i} \\
  &= 2nh (\frac{1}{\cos i} - \frac{\sin^2 i}{\cos i}) \\
  &= 2nh \cos i
\end{aligned}
$$

For the air film, the gap between fringes is $$\Delta x = \frac{\Delta h}{\tan\theta} = \frac{\lambda}{2\theta}$$

For the Newton's ring, the radis of its minimum fringes is
$$
h_m = R - \sqrt{R^2 - r_m^2} \approx \frac{1}{2} \frac{r_m^2}{R} = \frac{1}{2} m\lambda \\~\\
\Rightarrow r_m = \sqrt{m\lambda R}
$$

It can be seen that the fringes of the Newton's ring are also internally sparse and externally dense.








<br>

## Diffraction
### Single-slit Diffraction
The intensity in single-slit diffraction is 
$$
\Delta \varphi = \frac{2\pi}{\lambda} \frac{a}{N} \sin\theta \\~\\
\delta = N \Delta \varphi = \frac{2\pi a\sin\theta}{\lambda} \\~\\
\alpha = \frac{\delta}{2} = \frac{\pi a\sin\theta}{\lambda} \\~\\
I_{\theta} = E_{\theta}^2 = E_m^2 \left( \frac{\sin \alpha}{\alpha} \right)^2 = I_m \left( \frac{\sin \alpha}{\alpha} \right)^2
$$

When $\alpha = m\pi$, that is $a\sin\theta = m\lambda$, $I_{\theta} = 0$, which is the minimum. The half-angle width for the bright fringe at the center takes $m = 1$, that is, $\Delta \theta \approx \sin\theta = \lambda/a$, $\Delta y_m \approx f\cdot \Delta \theta = f\lambda/a$. So $a$ is smaller, $\Delta \theta$ and $\Delta y_m$ is bigger.

When $\theta = 0$, the intensity is the maximum. As for others, we have:
$$
\frac{d}{d\alpha} \left( \frac{\sin \alpha}{\alpha} \right) = 0 
\quad \Rightarrow \quad \alpha = \tan \alpha \\~\\
\Rightarrow \alpha = \pm 1.43\pi, \pm 2.46\pi, \pm 3.47\pi, \cdots \\~\\
\frac{I_1}{I_m} = 0.045, \quad \frac{I_2}{I_m} = 0.016, \quad \frac{I_3}{I_m} = 0.0083
$$

All in all,
$$
\delta = a\sin\theta = \begin{cases}
  0 & \text{Bright fringe at the center} \\
  2m \cdot \dfrac{\lambda}{2} & m = \pm 1, \pm 2, \pm 3, \cdots \text{ minima} \\
  (2m + 1) \cdot \dfrac{\lambda}{2} & m = \pm 1, \pm 2, \pm 3, \cdots \text{ maxima}
\end{cases}
$$



<br>

### Fraunhofer Diffraction at Circular Aperture and Angular Resolution
The intensity iof Fraunhofer diffraction is $$I(\theta) = I_0 \left( \frac{2J_1(x)}{x} \right)^2, \quad x = \frac{2\pi a\sin\theta}{\lambda}$$

where $J_1(x)$ is the first order Bessel function, $a$ is the radius of circular aperture.

The half-angle width is approximately $\Delta \theta = 0.61 \dfrac{\lambda}{a} = 1.22 \dfrac{\lambda}{D}$.

Rayleigh’s criterion: Two objects are just resolved when the maximum of one is at the minimum of the other. $\theta_R = \theta_{\min} = 1.22 \dfrac{\lambda}{D}$, the resolution ability is $1/\theta_R$.










<br>

## Gratings
The intensity of diffraction for $N$ slits is $$E_1 = E_m \left( \frac{\sin \alpha}{\alpha} \right)^2 e^{i0}, \cdots, E_N = E_m \left( \frac{\sin \alpha}{\alpha} \right)^2 e^{i(N-1)\delta}$$

where $\delta = 2\pi/\lambda \cdot d\sin\theta = 2\pi d\sin\theta/\lambda$ is the phase angle between adjacent waves.

$$\quad
\beta = \frac{\delta}{2} = \frac{\pi d\sin\theta}{\lambda} \\~\\
E_{\theta} = 2\cdot \frac{E_1}{2\sin\beta}\cdot \sin N\beta = E_1 \frac{\sin N\beta}{\sin \beta} \\~\\
\Rightarrow I_{\theta} = I_m \left( \frac{\sin \alpha}{\alpha} \right)^2 \left( \frac{\sin N\beta}{\sin \beta} \right)^2
$$

where $d = a + b$ is the distance between slits.

If $\sin N\beta = 0$, we have $\beta = (m + \dfrac{n}{N}) \pi$, $\sin\theta = \dfrac{\lambda}{d} (m + \dfrac{n}{N})$. So between two principal maxima, there are $N-1$ minima and $N-2$ maxima.

As for the half-angle width of a main maximum, we have 
$$
a\sin\theta = \lambda \\~\\
\Rightarrow Nd\cos\theta \Delta \theta = \lambda \\~\\
\Rightarrow \Delta \theta = \frac{\lambda}{Nd\cos\theta} \approx \frac{\lambda}{Nd}
$$








<br>

## Dispersion and resolving power
Define the dispersion power as the angular seperation per unit wavelength internal: 
$$
d\cos\theta \cdot \Delta \theta = m \Delta \lambda \\~\\
\Rightarrow D = \frac{\Delta \theta}{\Delta \lambda} = \frac{m}{d\cos\theta}
$$

Define the resolving power a grating as its ability to spatially separate two wavelengths. By the Rayleigh’s criterion, the half-angular width $\Delta \theta_w$ should be resolvable. Therefore, the smallest difference in wavelengths that can be distinguished at a wavelength of $\lambda$ is $$\Delta \lambda = \frac{\Delta \theta_w}{D_{\theta}} = \frac{\lambda}{Nd\cos\theta} \frac{d\cos\theta}{m} = \frac{\lambda}{Nm}$$

So the resolving power at $m$th order is $R = \dfrac{\lambda}{\Delta \lambda} = Nm$.

