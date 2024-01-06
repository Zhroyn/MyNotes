
- [Diffraciton and Gates](#diffraciton-and-gates)
  - [Diffraction](#diffraction)
    - [Single-slit Diffraction](#single-slit-diffraction)
    - [Fraunhofer Diffraction at Circular Aperture and Angular Resolution](#fraunhofer-diffraction-at-circular-aperture-and-angular-resolution)
  - [Gratings](#gratings)
  - [Dispersion and resolving power](#dispersion-and-resolving-power)




## Diffraciton and Gates
### Diffraction
#### Single-slit Diffraction
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

#### Fraunhofer Diffraction at Circular Aperture and Angular Resolution
The intensity iof Fraunhofer diffraction is $$I(\theta) = I_0 \left( \frac{2J_1(x)}{x} \right)^2, \quad x = \frac{2\pi a\sin\theta}{\lambda}$$

where $J_1(x)$ is the first order Bessel function, $a$ is the radius of circular aperture.

The half-angle width is approximately $\Delta \theta = 0.61 \dfrac{\lambda}{a} = 1.22 \dfrac{\lambda}{D}$.

Rayleigh’s criterion: Two objects are just resolved when the maximum of one is at the minimum of the other. $\theta_R = \theta_{\min} = 1.22 \dfrac{\lambda}{D}$, the resolution ability is $1/\theta_R$.








<br>

### Gratings
The intensity of diffraction for $N$ slits is $$E_1 = E_m \left( \frac{\sin \alpha}{\alpha} \right)^2 e^{i0}, \cdots, E_N = E_m \left( \frac{\sin \alpha}{\alpha} \right)^2 e^{i(N-1)\delta}$$

where $\delta = 2\pi/\lambda \cdot d\sin\theta = 2\pi d\sin\theta/\lambda$ is the phase angle between adjacent waves.

$$\quad
\beta = \frac{\delta}{2} = \frac{\pi d\sin\theta}{\lambda} \\~\\
E_{\theta} = 2\cdot \frac{E_1}{2\sin\beta}\cdot \sin N\beta = E_1 \frac{\sin N\beta}{\sin \beta} \\~\\
\Rightarrow I_{\theta} = I_m \left( \frac{\sin \alpha}{\alpha} \right)^2 \left( \frac{\sin N\beta}{\sin \beta} \right)^2
$$

where $d = a + b$ is the distance between slits.

If $\sin\beta = 0$, we have $\lim\limits_{\sin\beta\rightarrow 0} \dfrac{\sin N\beta}{\sin\beta} = N$, $I_{\theta} = N^2 I_m$.

If $\sin N\beta = 0$, we have $\beta = (m + \dfrac{n}{N}) \pi$, $\sin\theta = \dfrac{\lambda}{d} (m + \dfrac{n}{N})$. So between two principal maxima, there are $N-1$ minima and $N-2$ maxima.

As for the half-angle width of a main maximum, we have 
$$
a\sin\theta = \lambda \\~\\
\Rightarrow Nd\cos\theta \Delta \theta = \lambda \\~\\
\Rightarrow \Delta \theta = \frac{\lambda}{Nd\cos\theta} \approx \frac{\lambda}{Nd}
$$








<br>

### Dispersion and resolving power
Define the dispersion power as the angular seperation per unit wavelength internal: 
$$
d\cos\theta \cdot \Delta \theta = m \Delta \lambda \\~\\
\Rightarrow D = \frac{\Delta \theta}{\Delta \lambda} = \frac{m}{d\cos\theta}
$$

Define the resolving power a grating as its ability to spatially separate two wavelengths. By the Rayleigh’s criterion, the half-angular width $\Delta \theta_w$ should be resolvable. Therefore, the smallest difference in wavelengths that can be distinguished at a wavelength of $\lambda$ is $$\Delta \lambda = \frac{\Delta \theta_w}{D_{\theta}} = \frac{\lambda}{Nd\cos\theta} \frac{d\cos\theta}{m} = \frac{\lambda}{Nm}$$

So the resolving power at $m$th order is $R = \dfrac{\lambda}{\Delta \lambda} = Nm$.



