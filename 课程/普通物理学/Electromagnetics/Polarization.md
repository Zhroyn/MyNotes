
- [Polarization](#polarization)
  - [Linear Polarization](#linear-polarization)
  - [Other Polarization States](#other-polarization-states)
  - [Polarization by Reflection](#polarization-by-reflection)
  - [Birefringence](#birefringence)
    - [Wave Plates](#wave-plates)
  - [Polarization by Scattering](#polarization-by-scattering)






## Polarization
### Linear Polarization
When unpolarized light passes through a linear polarizer, the E-field component parallel to the slots is absorbed and/or reflected, the E-field component perpendicular to the slots is transmitted, becoming linearly polarized (LP) EM waves.

Long molecules absorb E-field parallel to molecule.

Law of Malus: $I_2 = I_1\cos^2\theta$






<br>

### Other Polarization States
- Unpolarized Light
- Linear Polarized Light
- Partial Polarized Light
- Circular Polarized Light
- Ellipse Polarized Light

Define degree of polarization as $P = \dfrac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}}$.

Electric field spirals CW in space (at fixed time)

Circular Polarization: For Right-handed (RCP), electric field spirals clockwize in space (at fixed time):
$$
\begin{cases}
  E_x = E_0 \sin (kz - \omega t + \dfrac{\pi}{2}) \\
  E_y = E_0 \sin (kz - \omega t)
\end{cases}
$$

For Left-handed (LCP), electric field spirals counterclockwize in space (at fixed time):
$$
\begin{cases}
  E_x = E_0 \sin (kz - \omega t - \dfrac{\pi}{2}) \\
  E_y = E_0 \sin (kz - \omega t)
\end{cases}
$$





<br>

### Polarization by Reflection
When unpolarized light is incident at Brewster's angle, the light that is reflected from the surface is perfectly polarized with its electric field vector perpendicular to the plane of incidence, and the light that is transmitted is therefore partially polarized.

The Brewster's angle is the angle that makes the reflected light and the refracted light perpendicular to each other. So we have $$\tan\theta_p = \frac{n_2}{n_1}$$






<br>

### Birefringence
When an arbitrary beam of light strikes the surface of a birefringent material at non-normal incidence, the polarization component normal to the optic axis (ordinary ray, its electric vector perpendicular to the optic axis) and the other linear polarization (extraordinary ray, its electric field polarization includes a component in the direction of the optic axis) will be refracted toward somewhat different paths. Natural light, so-called unpolarized light, consists of equal amounts of energy in any two orthogonal polarizations. Even linearly polarized light has some energy in both polarizations, unless aligned along one of the two axes of birefringence.

In birefringence, the ordinary ray has single index of refraction, the extraordinary ray has the index of refraction varies with direction of light. That's because the o-ray travels in the crystal with the same speed $v_o$ in all directions. The e-ray travels in the crystal with a speed that varies with the direction from $v_o$ to $v_e$. The corresponding $n_o$ and $n_e$ are called the principle indices of refraction.

If $v_e > v_o$, $n_e < n_o$, E-wave surface is externally tangent to the O-wave surface, it's call the negative crystal.

If $v_e < v_o$, $n_e > n_o$, E-wave surface is internally tangent to the O-wave surface, it's call the positive crystal.

The definition of the optical axis is that when light propagates along the optical axis, the velocities of O-wave and E-wave are the same. No birefringence occurs along the optical axis.


<br>

#### Wave Plates
Suppose the thickness of the wave plate is $d$, then the phase difference between the O-wave and the E-wave is $$\Delta\phi = \frac{2\pi}{\lambda} \cdot (\frac{d}{v_o} - \frac{d}{v_e}) c = \frac{2\pi}{\lambda}(n_o - n_e)d$$

If $(n_o - n_e)d = \pm \dfrac{1}{4}\lambda$, $\Delta \phi = \pm \dfrac{\pi}{2}$, it's Quater-wave Plate (QWP).

If $(n_o - n_e)d = \pm \dfrac{1}{2}\lambda$, $\Delta \phi = \pm \pi$, it's Full-wave Plate (FWP).

Suppose a linear polarized light is passing through a quater wave plate, and $\theta = 45^{\circ}$, then we can set $E_x = E_y = E_0 \sin(kz - \omega t)$. Because $E_x$ is parallel to the optical axis, it's the E-wave (slow axis), and $E_y$ is perpendicular to the optical axis, it's the O-wave (fast axis). So we have $\alpha_{slow} = \alpha_{fast} - \pi/2$:
$$
\begin{cases}
  E_{x} = E_0 \sin(kz - \omega t - \dfrac{\pi}{2}) \\
  E_{y} = E_0 \sin(kz - \omega t)
\end{cases}
$$

After the QWP, the light becomes circularly polarized light.







<br>

### Polarization by Scattering
When light is scattered by a small particle, the scattered light is polarized. The electric field of the scattered light is perpendicular to the plane formed by the incident light and the direction of the scattered light.

That's because the electric field of the incident light causes the electrons in the particle to oscillate, and the oscillating electrons emit light. The oscillating electrons are perpendicular to the direction of the incident light, so the electric field of the scattered light is perpendicular to the plane formed by the incident light and the direction of the scattered light.


