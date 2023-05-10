<!-- TOC -->

- [Wave Motion](#wave-motion)
  - [Wave Function](#wave-function)
  - [Linear Wave](#linear-wave)
    - [Phenomenon](#phenomenon)
    - [Linear Wave Equation](#linear-wave-equation)
  - [Sinusoidal Wave](#sinusoidal-wave)
    - [The Speed of Waves on Strings](#the-speed-of-waves-on-strings)
    - [Energy Transfer](#energy-transfer)
    - [Different Cases of Superposition](#different-cases-of-superposition)
  - [Sound Wave](#sound-wave)
    - [Pressure Fluctuation](#pressure-fluctuation)
    - [Speed of Sound in a Fluid](#speed-of-sound-in-a-fluid)
    - [Sound Intensity](#sound-intensity)
    - [Spherical Waves](#spherical-waves)
    - [Doppler Effect](#doppler-effect)
    - [Shock Waves](#shock-waves)

<!-- /TOC -->




## Wave Motion
### Wave Function
- A wave that causes the particles to move parallel to the direction of wave motion is called a **longitudinal wave**.
- A wave that causes the particles to move perpendicular to the wave motion is called a **transverse wave**.

The displacement $y$ depends on both $x$ and $t$. For this reason, it is often written as $y(x,t)$, which is called **wave function**.
- Right moving : $y = f(x - vt)$
- Left moving : $y = f(x + vt)$



### Linear Wave
#### Phenomenon
**Superposition Principle** : If two or more traveling waves are moving through a medium, the resultant wave function at any point is the **algebraic sum of the wave functions** of the individual waves.
**Linear Waves** : Waves that obey the superposition principle are called linear waves. Waves that violate the superposition principle are called nonlinear waves. 
**Interference** : The combination of separate waves in the same region of space to produce a resultant wave is called interference.

**Reflection** : When the pulse reaches the fixed end of the string, the pulse moves back along the string in the opposite direction.
**Free Boundary Condition** : When the string is tied to a light ring that is free to slide vertically on a smooth post, again, the pulse is reflected, but this time it is not inverted. 
**Transmission** : We may have a situation in which the boundary is intermediate between these two extremes. In this case, part of the incident pulse is reflected and part undergoes transmission—that is, some of the pulse passes through the boundary.

#### Linear Wave Equation
$\text{Equilibrium: } X_n = na \\
\text{Deviations from the equilibrium: } u_n = x_n - X_n \\ 
\text{Wave function: } u_n = u(X_n, t) $

$\displaystyle U^{\text{harm}} = \frac{1}{2}K\sum_n (x_{n+1}-x_n-a)^2 = \frac{1}{2}K\sum_n (u_{n+1}-u_n)^2 $

$\displaystyle \begin{aligned} 
M\frac{\partial^2 u_n}{\partial t^2}
&= -\frac{dU^{\text{harm}}}{\partial u_n} \\
&= K(u_{n+1} - u_n) - K(u_n - u_{n-1}) \\
&= Ka\left.\frac{\partial u}{\partial x}\right|_{X_n} - Ka\left.\frac{\partial u}{\partial x}\right|_{X_{n-1}} \\
&= Ka^2\left.\frac{\partial^2 u}{\partial x^2}\right|_{X_n}
\end{aligned} $

$\displaystyle \Rightarrow \frac{\partial^2 u}{\partial t^2} = v^2\frac{\partial^2 u}{\partial x^2}, 
\text{where } v = a\sqrt\frac{K}{M} $

- Wave functions $y= f(x–vt)$ and $y= f(x+ vt)$ are obviously solutions to the linear wave equation.
- The most important family of the solutions are $y = A\sin(kx - \omega t + \phi) $



### Sinusoidal Wave
$\displaystyle \begin{aligned} 
y &= A\sin(kx - vt + \phi) \\
&= A\sin\left[2\pi \left(\frac{x}{\lambda} - \frac{t}{T}\right) + \phi \right] \\
&= A\sin\left[ \frac{2\pi}{\lambda}(x - vt) + \phi \right]
\end{aligned} $

$\displaystyle k = \frac{2\pi}{\lambda} = \frac{2\pi f}{v} $

$\displaystyle \omega = \frac{2\pi}{T} = 2\pi f$

#### The Speed of Waves on Strings
$\Delta m = \mu \Delta x $

$\displaystyle \left\{ \begin{aligned}
  &F_{1x} = F_{2x} = F \\
  &\Delta ma_y
  = \mu \Delta x \frac{\partial^2 y}{\partial t^2} 
  = F \left.\frac{\partial y}{\partial x}\right|_{x+\Delta x} - F \left.\frac{\partial y}{\partial x}\right|_{x} 
  = F \frac{\partial^2y}{\partial x^2} \cdot \Delta x
\end{aligned} \right. $

$\displaystyle \Rightarrow \frac{\partial^2y}{\partial t^2} = \frac{F}{\mu} \frac{\partial^2y}{\partial x^2}, \; v = \sqrt{\frac{F}{\mu}} $


#### Energy Transfer
$\displaystyle \begin{aligned}
P(x, t) &= F_y(x, t)v_y(x, t) \\
&= -F \frac{\partial y(x, t)}{\partial x} \frac{\partial y(x, t)}{\partial t} \\
&= Fk\omega A^2\cos^2(kx - \omega t)
\end{aligned} $

$\displaystyle \text{The average rate of energy transfer: } P_{avg} = \frac{1}{2}Fk\omega A^2 = \frac{1}{2}\mu\omega^2 A^2v $


#### Different Cases of Superposition
**Interference**
$\displaystyle \begin{aligned}
  y = y_1 + y_2 &= A[\sin(kx - \omega t) + \sin(kx - \omega t + \phi)] \\
  &= 2A\cos\left( \frac{\phi}{2} \right) \sin(kx - \omega t + \frac{\phi}{2})
\end{aligned} $
$\displaystyle \Delta r = \frac{\phi}{2\pi}\lambda, \frac{\phi}{2} = \pi \frac{\Delta r}{\lambda} $

- Same frequency, wavelength, amplitude, direction
- Different phase
- When $\displaystyle \cos\left( \frac{\phi}{2} \right) = \pm 1 $ or $\displaystyle \Delta r = (2n)\cdot \frac{\lambda}{2} $, the waves are said to be everywhere **in phase** and thus **interfere constructively**.
- When $\displaystyle \cos\left( \frac{\phi}{2} \right) = 0 $ or $\displaystyle \Delta r = (2n+1)\cdot \frac{\lambda}{2} $, the resultant wave has zero amplitude everywhere, as a consequence of **destructive interference**.

**Beating**
$\displaystyle 
y_1 = A\cos\omega_1t = A\cos 2\pi f_1t \\
y_2 = A\cos\omega_2t = A\cos 2\pi f_2t \\
\begin{aligned}
y = y_1 + y_2 &= A(\cos 2\pi f_1t + \cos 2\pi f_2t) \\
&= \left[ 2A \cos 2\pi\left( \frac{f_1-f_2}{2} \right)t \right]\cos 2\pi\left( \frac{f_1+f_2}{2} \right)t
\end{aligned} $
$\text{Beat frequency: }f_b = |f_1 - f_2| $

- Beating is the periodic variation in intensity at a given point due to the superposition of two waves having slightly different frequencies.

**Standing Wave**
$\displaystyle 
y_1 = A\sin(kx - \omega t) \\
y_2 = A\sin(kx + \omega t) \\
\begin{aligned}
y = y_1 + y_2 &= A\sin(kx - \omega t) + A\sin(kx + \omega t) \\
&= (2A\sin kx)\cos\omega t
\end{aligned} $

- Same frequency, wavelength, amplitude
- Different direction
- Nodes: $kx = n\pi$
- Antiodes: $\displaystyle kx = (n + \frac{1}{2})\pi$
<br>

- In general, the wavelengths of the various standing waves for a string of length $L$ fixed at both ends are $\displaystyle \lambda_n = \frac{2L}{n} $
- The frequencies of the standing waves are $\displaystyle f_n = \frac{v}{\lambda_n} = n\frac{v}{2L} $
- This series is called **harmonic series**. The frequency with $n=1$ is called **fundamental frequency** or the first harmonic. The frequency with $n>1$ is called the $n$th harmonic, or the $(n-1)$th **overtones**.



### Sound Wave
- Sound waves in liquids and air are longitudinal waves.
- Sound waves in solids can be either longitudinal or transverse. 

#### Pressure Fluctuation
For a sound wave confined to a tube:
$\Delta V = S[u(x + \Delta x, t) - u(x, t)] $

$\displaystyle
\begin{aligned}
  \frac{\text{d}V}{V} &= \lim_{\Delta x \rightarrow 0} \frac{S[u(x + \Delta x, t) - u(x, t)]}{S\Delta x} \\
  &= \frac{\partial u(x,t)}{\partial x}
\end{aligned} $
Hence, $\displaystyle \Delta p(x, t) = -B \frac{\text{d}V}{V} = -B \frac{\partial u(x,t)}{\partial x} $


#### Speed of Sound in a Fluid
We consider an idealized case of a sound wave confined to a tube to derive the wave speed.

$V = Avt $
$\Delta V = Av_yt $
Momentum : $P = \rho V v_y = (\rho v_yt)v $
Impulse : $I = Ft = \Delta pAt $
Bulk modulus : $\displaystyle B = - \frac{\Delta p}{(-Av_yt) / (Avt)} = \Delta p \frac{v}{v_y} $

$\displaystyle P = I \\
\Rightarrow v = \sqrt{\frac{B}{\rho}} $

#### Sound Intensity
We define the intensity $I$ of a wave, or the average power per unit area, to be the average rate at which the energy being transported by the wave flows through a unit area $A$ perpendicular to the direction of travel of the wave.
$$
\begin{aligned}
  I(x, t) &= \Delta p(x, t) v(x, t) \\
  & = -B \frac{\partial u(x,t)}{\partial x} \frac{\partial u(x,t)}{\partial t} \\
  &= kB\omega s_{max}^2 \cos^2(kx - \omega t + \phi)
\end{aligned}
$$ $\Rightarrow$
$$
\begin{aligned}
  I &= \frac{1}{2} kB\omega s_{max}^2 \\ 
  &= \frac{1}{2} k\rho v^2\omega s_{max}^2 
  = \frac{1}{2} \rho v\omega^2 s_{max}^2 \\ 
  &= \frac{1}{2} \rho v(\omega s_{max})^2 \\
  &= \frac{\mathscr{P}}{A} 
\end{aligned}
$$

Because the range of sound intensities is so wide, it is convenient to use a logarithmic scale, where the **sound level** is defined by the equation
$$
\beta = 10 \log\left( \frac{I}{I_0} \right) (\text{dB}) \\~\\
I_0 = 1.00\times 10^{-12} \text{ W}/\text{m}^2
$$

#### Spherical Waves
- **Wavefronts** are surfaces over which the oscillations have the same value.
- **Rays** are directed lines perpendicular to the wavefronts that indicate the direction of travel of the wavefronts. 

$$
I = \frac{\mathscr{P}_{avg}}{A} = \frac{\mathscr{P}_{avg}}{4\pi r^2} \\~\\
\Rightarrow \phi(r, t) = \frac{s_0}{r}\sin(kr - \omega t)
$$

#### Doppler Effect
**Moving Observer, Stationary Source**
Positive $v_O$ for observer moving toward source, 
and negative $v_O$ for observer moving away from source.
Then
$$
v' = v + v_O \\~\\
f' = \frac{v'}{\lambda} = \frac{v + v_O}{\lambda} = (1 + \frac{v_O}{v})f
$$

**Moving Source, Stationary Observer**
Positive $v_S$ for source moving toward observers, 
and negative $v_O$ for source moving away from observer.
Then
$$
\lambda' = \lambda - v_ST = \lambda - \frac{v_S}{f} \\~\\
f' = \frac{v}{\lambda'} = \frac{v}{\lambda - \dfrac{v_S}{f}} = \frac{v}{\dfrac{v}{f} - \dfrac{v_S}{f}} = \frac{1}{1 - \dfrac{v_S}{v}}f
$$

**Both Source and Observer in Motion**
$v_O$ and $v_S$ are measured relative to the medium,
$v_O$ is positive if from $O$ to $S$,
$v_S$ is positive if from $S$ to $O$.
$$
f' = \frac{v + v_O}{v - v_S} f
$$

#### Shock Waves
When the $v_S$ is higher than the wave velocity $v$, the envelope surface of the wave surface is conical, called the **Mach cone**.
It is called **shock waves**, whick will form constructive interference at the shock front, a very large amplitude of wave crest.

Mach number : $\displaystyle \frac{v_S}{v}$

$\displaystyle \sin\theta = \frac{vt}{v_St} = \frac{v}{v_S} $



