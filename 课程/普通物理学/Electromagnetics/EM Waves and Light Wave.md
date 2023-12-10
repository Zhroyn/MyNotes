
- [EM Waves and Light Wave](#em-waves-and-light-wave)
  - [Electromagnetic Wave Spectrum](#electromagnetic-wave-spectrum)
  - [The Properties Of Electromagnetic Wave](#the-properties-of-electromagnetic-wave)
  - [The Energy Flux Density of Electromagnetic Wave](#the-energy-flux-density-of-electromagnetic-wave)





## EM Waves and Light Wave
### Electromagnetic Wave Spectrum
- Visible Light: 400nm ~ 700nm
- Infrared: 0.7um ~ 1mm
- Microwave: 1mm ~ 1m
- Radio: 1m ~ 100km
- Ultraviolet: 10nm ~ 400nm
- X-ray: 0.01nm ~ 10nm
- Gamma Ray: < 0.01nm




<br>

### The Properties Of Electromagnetic Wave
- $E \perp H$
- $E$ and $H$ are in phase
- The direction of propagation is parallel to $E \times H$, obey Right-Hand rule
- The speed of electromagnetic wave is $v = \dfrac{1}{\sqrt{\kappa_e\epsilon_0\kappa_m\mu_0}}$






<br>

### The Energy Flux Density of Electromagnetic Wave
The rate of the electromagnetic energy changing is
$$
\frac{dU}{dt} = \frac{d}{dt} \iiint \left( \frac{1}{2} \vec{D} \bullet \vec{E} + \frac{1}{2} \vec{B} \bullet \vec{H} \right) dv
$$

Beacuse
$$
\begin{aligned}
  & \frac{d}{dt} \left( \frac{1}{2} \vec{D} \bullet \vec{E} + \frac{1}{2} \vec{B} \bullet \vec{H} \right) \\
  =& \frac{1}{2} \kappa_e\epsilon_0 \frac{\partial}{\partial t} (\vec{E} \bullet \vec{E}) + \kappa_m\mu_0 \frac{\partial}{\partial t} (\vec{H} \bullet \vec{H}) \\
  =& \kappa_e\epsilon_0 \vec{E} \bullet \frac{\partial \vec{E}}{\partial t} + \kappa_m\mu_0 \vec{H} \bullet \frac{\partial \vec{H}}{\partial t} \\
  =& \vec{E} \bullet \frac{\partial \vec{D}}{\partial t} + \vec{H} \bullet \frac{\partial \vec{B}}{\partial t} \\
  =& \vec{E} \bullet (\nabla \times \vec{H} - \vec{j}_0) - \vec{H} \bullet (\nabla \times \vec{E}) \\
  =& \vec{E} \bullet (\nabla \times \vec{H}) - \vec{H} \bullet (\nabla \times \vec{E}) - \vec{j}_0 \bullet \vec{E} \\
  =& - \nabla \bullet (\vec{E} \times \vec{H}) - \vec{j}_0 \bullet \vec{E} \\
\end{aligned}
$$

So
$$
\begin{aligned}
  \frac{dU}{dt} &= - \iiint \nabla \bullet (\vec{E} \times \vec{H}) dv - \iiint (\vec{j}_0 \bullet \vec{E}) dv \\
  &= - \oiint (\vec{E} \times \vec{H}) d\vec{A} - \iiint (\vec{j}_0 \bullet \vec{E}) dv \\
\end{aligned}
$$

For the latter term, we have
$$
\vec{j}_0 = \sigma (\vec{E} + \vec{K}) \\~\\
\begin{aligned}
  \iiint (\vec{j}_0 \bullet \vec{E}) dv &= \vec{j}_0 \bullet (\rho \vec{j}_0 - \vec{K}) \Delta A \Delta l \\
  &= \rho \vec{j}_0^2 \Delta A \Delta l - (\vec{j}_0 \Delta A) (\vec{K} \Delta l) \\
  &= i_0^2R - i_0 \Delta \epsilon \\
  &= Q - P
\end{aligned}
$$

For the former term, we introduce Poynting Vector $\vec{S} = \vec{E} \times \vec{H}$. Then we have the Electromagnetic Energy Flux: $$\frac{dU}{dt} = - \oiint \vec{S} \bullet d\vec{A} - Q + P$$

Define $Z_0 = \mu_0c = 377 \Omega$, then we have $$S = \frac{EB}{\mu_0} = \frac{E^2}{\mu_0c} = \frac{E^2}{Z_0}$$

Then the Intensity of a wave ($W/m^2$) is $$I = \left\langle S \right\rangle = \frac{\left\langle E^2 \right\rangle}{Z_0} = \frac{1}{2} \frac{E^2_{\max}}{377 \Omega} = \frac{E^2_{\text{rms}}}{377 \Omega}$$

We can also define the Intensity of a wave as average energy density times wave velocity $$I = c\left\langle u \right\rangle = c\epsilon_0 \left\langle E^2 \right\rangle = c\epsilon_0 E^2_{\text{rms}} = \frac{E^2_{\text{rms}}}{\mu_0c}$$
