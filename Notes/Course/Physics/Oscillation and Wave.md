<!-- TOC -->

- [Oscillatory Motion](#oscillatory-motion)
  - [Equilibrium](#equilibrium)
  - [Simple Harmonic Oscillation](#simple-harmonic-oscillation)
  - [Applications of Oscillatory Motion](#applications-of-oscillatory-motion)
    - [Pendulum](#pendulum)
    - [Damped Oscillator](#damped-oscillator)
    - [Forced Oscillation](#forced-oscillation)
    - [Coupled Oscillators](#coupled-oscillators)
    - [Elastic Properties](#elastic-properties)
- [Wave Motion](#wave-motion)
  - [Wave Function](#wave-function)
  - [Linear Wave](#linear-wave)
    - [Phenomenon](#phenomenon)
    - [Linear Wave Equation](#linear-wave-equation)
  - [Sinusoidal Wave](#sinusoidal-wave)
    - [The Speed of Waves on Strings](#the-speed-of-waves-on-strings)
    - [Energy Transfer](#energy-transfer)
    - [Different Cases of Superposition](#different-cases-of-superposition)

<!-- /TOC -->





## Oscillatory Motion
### Equilibrium
- An object is in equilibrium if it is in both translational and rotational equilibrium, which means that both the linear acceleration and the angular acceleration are zero
- If an object is in equilibrium and the net torque is zero about one point, then the net torque must be zero about any other point
$\displaystyle \begin{aligned}
\sum \bold{\tau}_{O'} &= \bold{(r_1-r')\times F_1 + (r_2-r')\times F_2 + \cdots} \\
&= \bold{r_1\times F_1 + r_2\times F_2 + \cdots - r'(F_1 + F_2 + \cdots) } \\
&= \sum \tau_O - \bold{r' \sum F} \\
&= \sum \tau_O
\end{aligned} $

- Positions of **stable equilibrium** correspond to points for which $U(x)$ is a minimum : $\displaystyle \frac{dU}{dx}=0, \frac{d^2U}{dx^2}>0 $
- Quite generically, we expect linear restoring force if we neglect the higher order terms, which are usually small if we stay close enough to the equilibrium, for Taylor expansion of $U(x)$. This universal family of motion is known as the **simple harmonic motion**


### Simple Harmonic Oscillation
- An object moves with simple harmonic motion whenever its acceleration is proportional to its displacement from some equilibrium position and is oppositely directed
$\displaystyle F_s = -kx = ma\\
a = -\frac{k}{m} x \\$

$\displaystyle
\text{Define } \omega = \sqrt{k/m }, \\
\text{then } \frac{d^2x}{dt^2} = -\omega^2x,\\
\Rightarrow x = A\cos(\omega t + \phi) \\
\Rightarrow v = -A\omega\sin(\omega t + \phi) \\
\Rightarrow a = -A\omega^2\cos(\omega t + \phi) \\
$

$\displaystyle T = \frac{2\pi}{\omega}, f = \frac{\omega}{2\pi}, \omega = 2\pi f $

$\displaystyle K = \frac{1}{2}mv^2 = \frac{1}{2}m\omega^2A^2\sin^2(\omega t + \phi) = \frac{1}{2}k^2A^2\sin^2(\omega t + \phi) \\
U = \frac{1}{2}kx^2 = \frac{1}{2}kA^2\cos^2(\omega t + \phi) \\ 
\Rightarrow E = K + U = \frac{1}{2}kA^2 $



### Applications of Oscillatory Motion
#### Pendulum
**Simple Pendulum**
$\displaystyle -mg\sin\theta = m\frac{d^2s}{dt^2} \\
\Rightarrow \frac{d^2\theta}{dt^2} = -\frac{g}{L}\sin\theta \\
\Rightarrow \frac{d^2\theta}{dt^2} = -\frac{g}{L}\theta \\ $
$\displaystyle \omega = \sqrt{\frac{g}{L}}, T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{L}{g}} $

**Physical Pendulum**
If a hanging object oscillates about a fixed axis that does not pass through its center of mass, and the object cannot be approximated as a point mass, we cannot treat the system as a simple pendulum. In this case the system is called a physical pendulum.

$\displaystyle -mgd\sin\theta = I\frac{d^2\theta}{dt^2} \\
\Rightarrow \frac{d^2\theta}{dt^2} = -\frac{mgd}{I}\theta \\ $
$\displaystyle \omega = \frac{mgd}{I}, T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{I}{mgd}} $

**Torsional Pendulum**
Restoring torque is proportional to the angular displacement.
$\displaystyle \tau = -\kappa\theta = I\frac{d^2\theta}{dt^2} $


#### Damped Oscillator
$\displaystyle F_x = -kx - bv = ma_x \\
\Rightarrow -kx - b\frac{dx}{dt} = m\frac{d^2x}{dt^2} $
- **Weak Damping (Underdamped)** : 
  $When \; b^2 - 4km < 0 \; or \; \displaystyle \frac{k}{m} > (\frac{b}{2m})^2, x = Ae^{-\frac{b}{2m}t} \cos(\omega t + \phi), $ 
  where $\displaystyle \omega = \sqrt{\frac{k}{m} - (\frac{b}{2m})^2}. $
- **Critical Damping** : 
  $\displaystyle When \; b^2 - 4km = 0 \; or \; \frac{k}{m} = (\frac{b}{2m})^2, x = (A_1 + A_2t)e^{-\frac{b}{2m}t}. $
- **Overdamped** : 
  $\displaystyle When \; b^2 - 4km > 0 \; or \; \frac{k}{m} < (\frac{b}{2m})^2, x = A_1e^{r_1t} + A_2e^{r_2t} $, 
  where $r_1, r_2$ is the solution of $mr^2 + km + b = 0.$


#### Forced Oscillation
$\displaystyle F_{ext}\cos\omega t - kx - b\frac{dx}{dt} = m\frac{d^2x}{dt^2} \\~\\
\Rightarrow \left\{
  \begin{aligned}
    &x = A'e^{-\frac{b}{2m}t} \cos(\omega' t + \phi') + A\cos(\omega t + \phi) \\
    &\omega' = \sqrt{\frac{k}{m} - (\frac{b}{2m})^2} \\
    &\omega_0 = \sqrt{\frac{k}{m}} \\
    &A = \frac{F_{ext}/m}{\sqrt{(\omega^2 - \omega_0^2)^2 + (\frac{b\omega}{m})^2}} \\
    &\cos\phi =  \frac{\omega^2_0 - \omega^2}{\sqrt{(\omega^2 - \omega_0^2)^2 + (\frac{b\omega}{m})^2}}, \sin\phi =  \frac{-\frac{b\omega}{m}}{\sqrt{(\omega^2 - \omega_0^2)^2 + (\frac{b\omega}{m})^2}}
  \end{aligned}
\right. \\
\text{it's the solution at underdamped situation.} $

- When $\omega < \omega_0 = \sqrt{k/m}$, that is, the driving force is slow enough that the oscillator can follow the force after the transient motion decays.
- When $\omega > \omega_0 = \sqrt{k/m}$, that is, the driving force is fast such the oscillator cannot follow the force and lags behind ($\pi$ out of phase). Note that the amplitude is smaller than that for slow drive.
- When $\omega = \omega_0 = \sqrt{k/m}$, the amplitude quickly grows to a maximum. After the transient motion decays and the oscillator settles into steady state motion, the displacement $\pi/2$ out of phase with force. 
  - The dramatic increase in amplitude near the **natural frequency** $w_0$ is called **resonance**, and for this reason $w_0$ is sometimes called the **resonance frequency** of the system.
  - At resonance, the applied force is **in phase** with the velocity and that the power transferred to the oscillator is a maximum.



#### Coupled Oscillators
1. List the vibration equations for each object.
2. Assume normal mode : $x_i = x_{i0}\cos(\omega t + \phi) $.
3. Substitute and get the linear equations about the amplitude and frequency of each normal mode.
4. Rerange the linear equations as matrix, and then calculate the eigenvalues and eigenvectors of the matrix, or find the eigenfrequency by solve $|A| = 0$.
5. For each eigenvalue, we can get the frequency of a normal mode, and the relation between the amplitudes of objects in this normal mode from corresponding eigenvector.
6. By the relation between amplitudes of all objects in all normal modes, We can write the displacement functions of all objects.


#### Elastic Properties
$\displaystyle \text{Elastic modulus} \equiv \frac{\text{stress}}{\text{strain}} $
- Stress: A quantity that is proportional to the force causing a deformation; more specifically, stress is the external force acting on an object per unit cross-sectional area.
- Strain: A measure of the degree of deformation.
- Elastic modulus: The constant of proportionalitydepends on the material being deformed and on the nature of the deformation.
- Young’s Modulus : $\displaystyle Y = \frac{F/A}{\Delta L/L_i} $
- Shear Modulus : $\displaystyle Y = \frac{F/A}{\Delta x/h} $
- Bulk Modulus : $\displaystyle Y = -\frac{F/A}{\Delta V/V_i} = -\frac{\Delta P}{\Delta V/V_i} $









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

$\displaystyle \omega = \frac{2\pi}{T} = 2\pi f \\~\\
k = \frac{2\pi}{\lambda} = \frac{2\pi f}{v} $

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
&= 2A\cos(\frac{\phi}{2})\sin(kx - \omega t + \frac{\phi}{2})
\end{aligned} $
$\displaystyle \Delta r = \frac{\phi}{2\pi}\lambda, \frac{\phi}{2} = \pi \frac{\Delta r}{\lambda} $

- Same frequency, wavelength, amplitude, direction
- Different phase
- When $\displaystyle \cos(\frac{\phi}{2}) = \pm 1 $ or $\displaystyle \Delta r = (2n)\cdot \frac{\lambda}{2} $, the waves are said to be everywhere **in phase** and thus **interfere constructively**.
- When $\displaystyle \cos(\frac{\phi}{2}) = 0 $ or $\displaystyle \Delta r = (2n+1)\cdot \frac{\lambda}{2} $, the resultant wave has zero amplitude everywhere, as a consequence of **destructive interference**.

**Beating**
$\displaystyle 
y_1 = A\cos\omega_1t = A\cos 2\pi f_1t \\
y_2 = A\cos\omega_2t = A\cos 2\pi f_2t \\
\begin{aligned}
y = y_1 + y_2 &= A(\cos 2\pi f_1t + \cos 2\pi f_2t) \\
&= [2A \cos 2\pi(\frac{f_1-f_2}{2})t]\cos 2\pi(\frac{f_1+f_2}{2})t
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





