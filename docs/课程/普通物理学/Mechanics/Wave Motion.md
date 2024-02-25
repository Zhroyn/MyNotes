
- [Wave Motion](#wave-motion)
    - [Wave Function](#wave-function)
    - [Wave Equation](#wave-equation)
    - [Linear Wave](#linear-wave)
        - [Phenomenon](#phenomenon)
        - [Speed of Wave in a Solid](#speed-of-wave-in-a-solid)
    - [Sinusoidal Wave](#sinusoidal-wave)
        - [Sinusoidal Wave Function](#sinusoidal-wave-function)
        - [Speed of Wave on a String](#speed-of-wave-on-a-string)
        - [Energy Transfer](#energy-transfer)
        - [Different Cases of Superposition](#different-cases-of-superposition)
            - [Interference Case](#interference-case)
            - [Beating Case](#beating-case)
            - [Standing Wave](#standing-wave)
    - [Sound Wave](#sound-wave)
        - [Pressure Fluctuation](#pressure-fluctuation)
        - [Speed of Sound in a Fluid](#speed-of-sound-in-a-fluid)
        - [Sound Intensity](#sound-intensity)
        - [Spherical Waves](#spherical-waves)
        - [Doppler Effect](#doppler-effect)
        - [Shock Waves](#shock-waves)







## Wave Motion
### Wave Function
- A wave that causes the particles to move parallel to the direction of wave motion is called a **longitudinal wave**.
- A wave that causes the particles to move perpendicular to the wave motion is called a **transverse wave**.

The displacement $y$ depends on both $x$ and $t$. For this reason, it is often written as $y(x,t)$, which is called **wave function**.
- Right moving : $y(x, t) = f(x - vt)$
- Left moving : $y(x, t) = f(x + vt)$




### Wave Equation
Set $y = f(x + vt) = f(u) $, then

$$
\begin{gathered}
  \frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial u^2} \\\\
  \frac{\partial^2 y}{\partial x^2} = \frac{\partial^2 y}{\partial u^2} \\\\
  \Rightarrow \frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2}
\end{gathered}
$$





### Linear Wave
#### Phenomenon
- **Superposition Principle** : If two or more traveling waves are moving through a medium, the resultant wave function at any point is the **algebraic sum** of the wave functions of the individual waves.
- Linear Waves :
    - Waves that obey the superposition principle are called **linear waves**.
    - Waves that violate the superposition principle are called **nonlinear waves**.
- The combination of separate waves in the same region of space to produce a resultant wave is called **interference**.

<br>

- **Reflection** :
    - When the string's end is fixed, the pulse moves back in the opposite direction.
    - When the string is tied to a light ring that is free to slide vertically on a smooth post, again, the pulse moves back in the same direction.
- **Transmission** :
    - When the boundary is intermediate between these two extremes, part of the incident pulse is reflected and part undergoes transmission.
    - When from soft to hard, the reflected wave is invertd.
    - When from hard to soft, the reflected wave is not invertd.

<br>

#### Speed of Wave in a Solid
Set $x_n$ to be the positions of atoms, and $X_n = na $ to be the equilibrium positions.
Let the wave function be $u_n = u(X_n, t) $, then we can get $$U^{\text{harm}} = \frac{1}{2}K\sum_n (u_{n+1}-u_n)^2$$

So for every atom, there are

$$
\begin{aligned} 
  M\frac{\partial^2 u_n}{\partial t^2}
  &= -\frac{dU^{\text{harm}}}{d u_n} \\
  &= K(u_{n+1} - u_n) - K(u_n - u_{n-1}) \\
  &= Ka\left.\frac{\partial u}{\partial x}\right|_{X_n} - Ka\left.\frac{\partial u}{\partial x}\right|_{X_{n-1}} \\
  &= Ka^2\left.\frac{\partial^2 u}{\partial x^2}\right|_{X_n}
\end{aligned}
$$

So we can get $$\frac{\partial^2 u}{\partial t^2} = \frac{Ka^2}{M}\frac{\partial^2 u}{\partial x^2}$$

Therefore $$v = a\sqrt\frac{K}{M}$$








<br>

### Sinusoidal Wave
#### Sinusoidal Wave Function
$$
\begin{aligned} 
  y &= A\sin(kx - \omega t + \phi) \\
  &= A\sin\left[2\pi \left(\frac{x}{\lambda} - \frac{t}{T}\right) + \phi \right] \\
  &= A\sin\left[ \frac{2\pi}{\lambda}(x - vt) + \phi \right]
\end{aligned} 
$$

$$
k = \frac{2\pi}{\lambda} = \frac{2\pi f}{v}, \quad
\omega = \frac{2\pi}{T} = 2\pi f, \quad
v = \frac{\omega}{k}
$$

<br>

#### Speed of Wave on a String
Set $\mu$ to be the linear density, then we can get

$$
\begin{gathered}
  \Delta ma_y = \mu \Delta x \frac{\partial^2 y}{\partial t^2} = F \left.\frac{\partial y}{\partial x}\right|_{x+\Delta x} - F \left.\frac{\partial y}{\partial x}\right|_{x} = F \frac{\partial^2y}{\partial x^2} \cdot \Delta x \\\\
  \Rightarrow \frac{\partial^2y}{\partial t^2} = \frac{F}{\mu} \frac{\partial^2y}{\partial x^2}
\end{gathered}
$$

Therefore $$v = \sqrt{\frac{F}{\mu}}$$

<br>

#### Energy Transfer
The power of energy transfer at a particular position and time is

$$
\begin{aligned}
  P(x, t) &= F_y(x, t)v_y(x, t) \\
  &= -F \frac{\partial y(x, t)}{\partial x} \frac{\partial y(x, t)}{\partial t} \\
  &= Fk\omega A^2\cos^2(kx - \omega t)
\end{aligned} 
$$

So The average rate of energy transfer is $$P_{avg} = \frac{1}{2}Fk\omega A^2 = \frac{1}{2}\mu\omega^2 A^2v$$

<br>

#### Different Cases of Superposition
##### Interference Case
$$
\begin{aligned}
  y = y_1 + y_2 &= A\left[ \sin(kx - \omega t) + \sin(kx - \omega t + \phi) \right] \\
  &= 2A\cos\left( \frac{\phi}{2} \right) \sin(kx - \omega t + \frac{\phi}{2})
\end{aligned}
$$

$$
\begin{gathered}
  \Delta r = v\Delta t = \lambda f \Delta t \\
  \phi = \omega \Delta t = 2\pi f \Delta t
\end{gathered}
$$

So we can get $$\Delta r = \frac{\phi}{\pi}\cdot \frac{\lambda}{2}, \quad \frac{\phi}{2} = \pi \frac{\Delta r}{\lambda}$$

When $\displaystyle \cos\left( \frac{\phi}{2} \right) = \pm 1$ or $\displaystyle \Delta r = (2n)\cdot \frac{\lambda}{2}$, the waves are said to be everywhere *in phase* and thus *interfere constructively*.

When $\displaystyle \cos\left( \frac{\phi}{2} \right) = 0$ or $\displaystyle \Delta r = (2n+1)\cdot \frac{\lambda}{2}$, the resultant wave has zero amplitude everywhere, as a consequence of *destructive interference*.


##### Beating Case
Beating is the periodic variation in intensity at a given point due to the superposition of two waves having slightly different frequencies.

Set

$$
\begin{gathered}
  y_1 = A\cos\omega_1t = A\cos 2\pi f_1t \\
  y_2 = A\cos\omega_2t = A\cos 2\pi f_2t
\end{gathered}
$$

Then we can get

$$
\begin{aligned}
  y = y_1 + y_2 &= A(\cos 2\pi f_1t + \cos 2\pi f_2t) \\
  &= \left[ 2A \cos 2\pi\left( \frac{f_1-f_2}{2} \right)t \right]\cos 2\pi\left( \frac{f_1+f_2}{2} \right)t
\end{aligned} 
$$

Beat frequency: $f_b = |f_1 - f_2| $


##### Standing Wave
Set

$$
\begin{gathered}
  y_1 = A\sin(kx - \omega t) \\
  y_2 = A\sin(kx + \omega t) \\
\end{gathered}
$$

Then we can get

$$
\begin{aligned}
  y = y_1 + y_2 &= A\sin(kx - \omega t) + A\sin(kx + \omega t) \\
  &= (2A\sin kx)\cos\omega t
\end{aligned} 
$$

Nodes: $kx = n\pi$

Antiodes: $\displaystyle kx = (n + \frac{1}{2})\pi$

The wavelengths of standing waves for a string fixed at both ends are $\displaystyle \lambda_n = \frac{2L}{n} $

Then the frequencies are $\displaystyle f_n = \frac{v}{\lambda_n} = n\frac{v}{2L} $

This series is called **harmonic series**. The frequency with $n=1$ is called **fundamental frequency** or the first harmonic. The frequency with $n>1$ is called the $n$th harmonic, or the $(n-1)$th **overtones**.









<br>

### Sound Wave
- Sound waves in liquids and air are longitudinal waves.
- Sound waves in solids can be either longitudinal or transverse. 

#### Pressure Fluctuation
For a sound wave confined to a tube, there are $$\Delta V = S[u(x + \Delta x, t) - u(x, t)]$$

So we can get

$$
\begin{aligned}
  \frac{\text{d}V}{V} &= \lim_{\Delta x \rightarrow 0} \frac{S[u(x + \Delta x, t) - u(x, t)]}{S\Delta x} \\
  &= \frac{\partial u(x,t)}{\partial x}
\end{aligned} 
$$

Hence $$\Delta p(x, t) = -B \frac{\text{d}V}{V} = -B \frac{\partial u(x,t)}{\partial x}$$

<br>

#### Speed of Sound in a Fluid
We consider an idealized case of a sound wave confined to a tube.
Set $A$ to be the area of cross section, $v_y$ to be the initial speed the fluid is pushed as well as the speed of fluid, $V$ to be the volume of fluid being pushed, $\Delta V$ to be the reduced volume of the fluid, then we can get

$$
\begin{gathered}
  V = Avt \\\\
  \Delta V = Av_yt \\\\
  \Delta p = -B \frac{\Delta V}{V} = -B \frac{v_y}{v}
\end{gathered}
$$

By $P = I$, we can get

$$
\begin{gathered}
  P = \rho V v_y = \rho (Av_yt)v \\\\
  I = Ft = \Delta p At = B \frac{Av_yt}{v} \\\\
  \Rightarrow v = \sqrt{\frac{B}{\rho}}
\end{gathered}
$$

<br>

#### Sound Intensity
Sound intensity $I$ is defined as the power carried by sound waves per unit area in a direction perpendicular to that area, that is to say, $\boldsymbol{I} = p\boldsymbol{v}$.

$$
\begin{aligned}
  I(x, t) &= \Delta p(x, t) v(x, t) \\
  & = -B \frac{\partial u(x,t)}{\partial x} \frac{\partial u(x,t)}{\partial t} \\
  &= kB\omega s_{max}^2 \cos^2(kx - \omega t + \phi)
\end{aligned}
$$

So the average is

$$
\begin{aligned}
  I = \frac{\mathscr{P}_{avg}}{A} &= \frac{1}{2} kB\omega s_{max}^2 \\ 
  &= \frac{1}{2} k\rho v^2\omega s_{max}^2 \\
  &= \frac{1}{2} \rho v(\omega s_{max})^2 \\
\end{aligned}
$$

which means $I \sim s^2$.

**Sound intensity level** is the logarithmic measure of the intensity of a sound relative to a reference value, that is

$$\beta = 10 \log\left( \frac{I}{I_0} \right) (\text{dB})$$

$$I_0 = 1.00\times 10^{-12} \text{ W}/\text{m}^2$$

<br>

#### Spherical Waves
- **Wavefronts** are surfaces over which the oscillations have the same value.
- **Rays** are directed lines perpendicular to the wavefronts that indicate the direction of travel of the wavefronts. 

$$
\begin{gathered}
  I = \frac{\mathscr{P}_{avg}}{A} = \frac{\mathscr{P}_{avg}}{4\pi r^2} \\\\
  \Rightarrow \phi(r, t) = \frac{s_0}{r}\sin(kr - \omega t)
\end{gathered}
$$

<br>

#### Doppler Effect
**Moving Observer, Stationary Source**
Assume $v_O$ is positive if the observer is moving from $O$ to $S$, then the speed of the sound relative to the observer become $$v' = v + v_O$$

However, the wavelength of the sound the observer receive is unchanged, so $$f' = \frac{v'}{\lambda} = \frac{v + v_O}{\lambda} = (1 + \frac{v_O}{v})f$$

**Moving Source, Stationary Observer**
Assume $v_S$ is positive if the source is moving from $S$ to $O$, then the wavelengh of the sound become $$\lambda' = \lambda - v_ST = \lambda - \frac{v_S}{f}$$

However, the speed of the sound the observer receive is unchanged, so $$f' = \frac{v}{\lambda'} = \frac{v}{\lambda - \dfrac{v_S}{f}} = \frac{v}{\dfrac{v}{f} - \dfrac{v_S}{f}} = \frac{1}{1 - \dfrac{v_S}{v}}f$$

**Both Source and Observer in Motion**
The speed of the sound the observer receive is $\displaystyle v' = v + v_O $, the wavelengh of the sound the observer receive is $\displaystyle \lambda' = \lambda - \frac{v_S}{f} $, so we can get $$f' = \frac{v'}{\lambda'} = \frac{v + v_O}{v - v_S} f$$

<br>

#### Shock Waves
When $v_S$ is higher than the wave velocity $v$, the envelope surface of the wave surface is a cone, which is called **Mach cone**.

Set the conical angle to be $\theta$, then we can get $$\sin\theta = \frac{vt}{v_St} = \frac{v}{v_S}$$

By this, we can set **Mach number**: $v_S/v$

At the shock front, which is the generatrix of the cone, it will form constructive interference and generate a wave with a very large amplitude.




