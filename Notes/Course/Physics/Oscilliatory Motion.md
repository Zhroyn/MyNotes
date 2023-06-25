<!-- TOC -->

- [Oscillatory Motion](#oscillatory-motion)
  - [Equilibrium](#equilibrium)
  - [Simple Harmonic Oscillation](#simple-harmonic-oscillation)
  - [Pendulum](#pendulum)
    - [Simple Pendulum](#simple-pendulum)
    - [Physical Pendulum](#physical-pendulum)
    - [Torsional Pendulum](#torsional-pendulum)
  - [Damped Oscillator](#damped-oscillator)
  - [Forced Oscillation](#forced-oscillation)
  - [Coupled Oscillators](#coupled-oscillators)
  - [Elastic Properties](#elastic-properties)

<!-- /TOC -->





## Oscillatory Motion
### Equilibrium
An object is in equilibrium if it is in both translational and rotational equilibrium, which means that both the **linear acceleration** and the **angular acceleration** are zero.

If an object is in equilibrium and the net torque is zero about one point, then the net torque must be zero about any other point:
$$
\begin{aligned}
\sum \bold{\tau}_{O'} &= \bold{(r_1-r')\times F_1 + (r_2-r')\times F_2 + \cdots} \\
&= \bold{r_1\times F_1 + r_2\times F_2 + \cdots - r'(F_1 + F_2 + \cdots) } \\
&= \sum \tau_O - \bold{r' \sum F} \\
&= \sum \tau_O
\end{aligned}
$$

Positions of **stable equilibrium** correspond to points for which $U(x)$ is a minimum:
$$\displaystyle \frac{dU}{dx}=0, \frac{d^2U}{dx^2}>0 $$

Quite generically, we expect linear restoring force if we neglect the higher order terms, which are usually small if we stay close enough to the equilibrium, for Taylor expansion of $U(x)$. This universal family of motion is known as the **simple harmonic motion**







<br>

### Simple Harmonic Oscillation
An object moves with simple harmonic motion whenever its acceleration is proportional to its displacement from some equilibrium position and is oppositely directed, that is
$$
F_s = -kx = ma \\~\\
\Rightarrow a = -\frac{k}{m} x
$$

Define $\omega = \sqrt{k/m}$, then we can get
$$
\frac{d^2x}{dt^2} = -\omega^2x,\\~\\
\Rightarrow x = A\cos(\omega t + \phi) \\~\\
\Rightarrow v = -A\omega\sin(\omega t + \phi) \\~\\
\Rightarrow a = -A\omega^2\cos(\omega t + \phi)
$$

So
$$T = \frac{2\pi}{\omega}, f = \frac{\omega}{2\pi}, \omega = 2\pi f $$

And the kinetic energy is
$$
\begin{aligned}
  K &= \frac{1}{2}mv^2 \\
  &= \frac{1}{2}m\omega^2A^2\sin^2(\omega t + \phi) \\
  &= \frac{1}{2}kA^2\sin^2(\omega t + \phi)
\end{aligned} \\~\\
U = \frac{1}{2}kx^2 = \frac{1}{2}kA^2\cos^2(\omega t + \phi) \\~\\
\Rightarrow E = K + U = \frac{1}{2}kA^2 
$$







<br>

### Pendulum
#### Simple Pendulum
$$
-mg\sin\theta = m\frac{d^2s}{dt^2} \\~\\
\Rightarrow \frac{d^2\theta}{dt^2} = -\frac{g}{L}\sin\theta \\~\\
\Rightarrow \frac{d^2\theta}{dt^2} = -\frac{g}{L}\theta
$$

So 
$$
\omega = \sqrt{\frac{g}{L}} \\~\\
T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{L}{g}}
$$

#### Physical Pendulum
If a hanging object oscillates about a fixed axis that does not pass through its center of mass, and the object cannot be approximated as a point mass, we cannot treat the system as a simple pendulum. In this case the system is called a physical pendulum.

$$
-mgd\sin\theta = I\frac{d^2\theta}{dt^2} \\~\\
\Rightarrow \frac{d^2\theta}{dt^2} = -\frac{mgd}{I}\theta
$$

So
$$
\omega = \sqrt{\frac{mgd}{I}} \\~\\
T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{I}{mgd}}
$$

#### Torsional Pendulum
Restoring torque is proportional to the angular displacement, that is $$\tau = I\frac{d^2\theta}{dt^2} = -\kappa\theta $$








<br>

### Damped Oscillator
$$
F_x = -kx - bv = ma_x \\~\\
\Rightarrow -kx - b\frac{dx}{dt} = m\frac{d^2x}{dt^2}
$$

**Weak Damping (Underdamped) Situation**
When
$$
b^2 - 4km < 0 \\~\\
\Rightarrow \frac{k}{m} > \left( \frac{b}{2m} \right)^2$$

We can get $$x = Ae^{-\frac{b}{2m}t} \cos(\omega t + \phi)$$

where $\displaystyle \omega = \sqrt{\frac{k}{m} - \left( \frac{b}{2m} \right)^2}$.

<br>

**Critical Damping Situation**
When
$$
b^2 - 4km = 0 \\~\\
\Rightarrow \frac{k}{m} = \left( \frac{b}{2m} \right)^2$$

We can get $$x = (A_1 + A_2t)e^{-\frac{b}{2m}t}$$

<br>

**Overdamped Situation**
When
$$
b^2 - 4km > 0 \\~\\
\Rightarrow \frac{k}{m} < \left( \frac{b}{2m} \right)^2$$

We can get $$x = A_1e^{r_1t} + A_2e^{r_2t}$$

where $r_1, r_2$ is the solution of $mr^2 + br + k = 0.$








<br>

### Forced Oscillation
$$ 
F_{ext}\cos\omega t - kx - b\frac{dx}{dt} = m\frac{d^2x}{dt^2}
$$

At the underdamped situation, we can get the solution
$$
\left\{
  \begin{aligned}
    & x = A'e^{-\frac{b}{2m}t} \cos(\omega' t + \phi') + A\cos(\omega t + \phi) \\
    & \omega' = \sqrt{\frac{k}{m} - \left( \frac{b}{2m} \right)^2} \\
    & A = \frac{F_{ext}/m}{\sqrt{(\omega^2 - \omega_0^2)^2 + \left( \dfrac{b\omega}{m} \right)^2}}, \omega_0 = \sqrt{\frac{k}{m}} \\
    & \cos\phi =  \frac{\omega^2_0 - \omega^2}{\sqrt{(\omega^2 - \omega_0^2)^2 + \left( \dfrac{b\omega}{m} \right)^2}}, \sin\phi =  \frac{-\dfrac{b\omega}{m}}{\sqrt{(\omega^2 - \omega_0^2)^2 + \left( \dfrac{b\omega}{m} \right)^2}}
  \end{aligned}
\right.
$$

When $\omega < \omega_0 = \sqrt{k/m}$, the driving force is slow enough that the oscillator can follow the force after the transient motion decays.

When $\omega > \omega_0 = \sqrt{k/m}$, the driving force is fast such the oscillator cannot follow the force and lags behind ($\pi$ out of phase). Note that the amplitude is smaller than that for slow drive.

When $\omega = \omega_0 = \sqrt{k/m}$, the amplitude quickly grows to a maximum. After the transient motion decays and the oscillator settles into steady state motion, the displacement $\pi/2$ out of phase with force. 

- The dramatic increase in amplitude near the **natural frequency** $w_0$ is called **resonance**, and for this reason $w_0$ is sometimes called the **resonance frequency** of the system.
- At resonance, the applied force is **in phase** with the velocity and that the power transferred to the oscillator is a maximum.








<br>

### Coupled Oscillators
1. List the vibration equations for each object.
2. Assume normal mode: $x_i = x_{i0}\cos(\omega t + \phi) $.
3. Substitute and get the linear equations about the amplitude and frequency of each normal mode.
4. Rerange the linear equations as matrix, and then calculate the eigenvalues and eigenvectors of the matrix, or find the eigenfrequency by solve $|A| = 0$.
5. For each eigenvalue, we can get the frequency of a normal mode, and the relation between the amplitudes of objects in this normal mode from corresponding eigenvector.
6. By the relation between amplitudes of all objects in all normal modes, We can write the displacement functions of all objects.






<br>

### Elastic Properties
$$ \text{Elastic modulus} \equiv \frac{\text{stress}}{\text{strain}} $$

- Stress: A quantity that is proportional to the force causing a deformation; more specifically, stress is the external force acting on an object per unit cross-sectional area.
- Strain: A measure of the degree of deformation.
- Elastic modulus: The constant of proportionality depends on the material being deformed and on the nature of the deformation.

Young’s Modulus: $\displaystyle Y = \frac{F/A}{\Delta L/L_i} $

Shear Modulus: $\displaystyle S = \frac{F/A}{\Delta x/h} $

Bulk Modulus: $\displaystyle B = -\frac{\Delta F/A}{\Delta V/V_i} = -\frac{\Delta P}{\Delta V/V_i} $





