
- [Interference](#interference)
  - [Steady Wave](#steady-wave)
  - [Wave Superposition and Interference](#wave-superposition-and-interference)
    - [Young’s Double Slit Quantitative](#youngs-double-slit-quantitative)
    - [Thin Film Interference](#thin-film-interference)





## Interference
### Steady Wave
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

### Wave Superposition and Interference
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

#### Young’s Double Slit Quantitative
In Young’s double slit expriment, we have $$\Delta L = d\sin\theta, \quad \sin\theta = \frac{y}{L}$$

So constructive interference happens at $y = \dfrac{m\lambda L}{d}$.

Destructive interference happens at $y = \dfrac{(m + \dfrac{1}{2})\lambda L}{d}$.



<br>

#### Thin Film Interference
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





