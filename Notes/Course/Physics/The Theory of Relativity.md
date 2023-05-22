<!-- TOC -->

- [The Theory of Relativity](#the-theory-of-relativity)
  - [Relativistic Velocity Addition Law](#relativistic-velocity-addition-law)
  - [Synchronizing Clocks](#synchronizing-clocks)
  - [Moving Clocks and Sticks](#moving-clocks-and-sticks)
  - [Lorentz Transformation](#lorentz-transformation)
    - [Time Dilation](#time-dilation)
    - [Length Contraction](#length-contraction)
    - [Invariant Interval](#invariant-interval)
    - [Minkowski Diagram](#minkowski-diagram)
  - [Relativistic Doppler Effect](#relativistic-doppler-effect)

<!-- /TOC -->





## The Theory of Relativity
### Relativistic Velocity Addition Law
Here we derive the law by the example of a race between a ball and a pulse of light in a moving train. Suppose the location they meet devide the train carriage into two sections of $1 - f : f$ ratio.

In the train frame, set after time $T$, the ball and the light pulse meet again, and set $L$ to be the length of the train, $u$ to be the speed of the ball, then we can get
$$
uT = (1 - f)L, \quad cT = (1 + f)L \\~\\
\Rightarrow \frac{u}{c} = \frac{1 - f}{1 + f} \\~\\
\Rightarrow f = \frac{c - u}{c + u}
$$

In the track frame, set the light pulse reaches the right end of the train after time $T_0$, and the ball and the light pulse meet again after time $T_1$, and set $D$ to be the distance between the ball and the light pulse at this time, $L'$ to be the length of train in track frame, $w$ to be the speed of the ball, $v$ to be the speed of the train, then we can get
$$
\begin{aligned}
  & D = cT_0 - wT_0 \\
  & L' = cT_0 - vT_0 \\
\end{aligned}
\Rightarrow 
\frac{D}{L'} = \frac{c - w}{c - v}
\\~\\
\begin{aligned}
  D = cT_1 + wT_1 \\
  fL' = cT_1 + vT_1 \\
\end{aligned}
\Rightarrow 
\frac{D}{fL'} = \frac{c + w}{c + v}
\\~\\
\Rightarrow f = \frac{c - w}{c + w}\cdot \frac{c + v}{c - v}
$$

Therefore, we can get
$$
\frac{c - w}{c + w} = \frac{c - u}{c + u}\cdot \frac{c - v}{c + v} \\~\\
\Rightarrow w = \frac{u + v}{1 + \left( \dfrac{u}{c} \right)\left( \dfrac{v}{c} \right)}
$$

**For mutiple frames:**
$$
\frac{c - v_{AD}}{c + v_{AD}} 
= \frac{c - v_{AB}}{c + v_{AB}}\cdot \frac{c - v_{BC}}{c + v_{BC}}\cdot \frac{c - v_{CD}}{c + v_{CD}}
$$

**For speed in medium:**
$$
v' = \frac{\frac{c}{n} + v}{1 + \frac{1}{n}\frac{v}{c}}
\approx \frac{c}{n} + v(1 - \frac{1}{n^2})
$$





### Synchronizing Clocks
Now let's synchronize the clocks by emitting two opposite light pulses simultaneously.
In the train frame, the light pulses reach both ends simultaneously, so we set clocks on the train to 0 when the light pulses reach them.
In the track frame, the light pulses first reach the rear of train, so we set both clocks on the track to 0 when the light pulses reach the rear of train.

Let $L$ be the proper length of train, and $L_F, L_M$ the length of train in the track frame and train frame respectively.
Let $E_L, E_R$ denote the events of light pulse reaching the left and right end respectively, and $D_F, D_M$ the distance between the two events in the track and train frame respectively.

Then, in the track frame, we can get
$$
\begin{aligned}
  & T_F = \frac{L_F/2}{c - v} - \frac{L_F/2}{c + v} = \frac{vL_F}{c^2 - v^2} \\
  & D_F = c\left( \frac{L_F/2}{c - v} + \frac{L_F/2}{c + v} \right) = \frac{c^2L_F}{c^2 - v^2} \\
\end{aligned}
\Rightarrow T_F = \frac{D_Fv}{c^2}
$$

In fact, no matter which wave is used to synchronize the clocks, by the relative velocity addition law, the conclusion still holds.

So, if two clocks are **synchronized** and **separated** in a proper frame, then in a frame in which the clocks move along the line joining them with speed $v$, **the rear clock will be ahead of the front clock** by $\displaystyle \frac{Dv}{c^2}$, where $D$ denotes the distance between the clocks in their proper frame.







### Moving Clocks and Sticks
Let $v$ be the relative speed between the two frames, $s'$ the slowing-down factor, $s$ the shrinking factor, and $T$ the difference between the readings of the clock.
In the stick frame, the clock is moving, so due to time dilation, 
$$T = s' \times \frac{L}{v} = \frac{s'L}{v} $$

In the clock frame, the stick is moving, so due to length contraction, 
$$T = \frac{sL}{v} $$

So $s' = s$. By definition,
$$
\left\{
\begin{aligned}
  & s' = \frac{T_M}{T_F} = \frac{D_M}{D_F} = \frac{L}{D_F} \\
  & s = \frac{L_F}{L} \\
\end{aligned}
\right.
\\~\\
\Rightarrow s^2 = \frac{L_F}{D_F}
$$

So 
$$
D_F = L_F + vT_F = L_F + \frac{v^2D_F}{c^2}
\\~\\
\Rightarrow D_F = \frac{L_F}{1 - v^2 / c^2}
\\~\\
\Rightarrow s = \sqrt{1 - \frac{v^2}{c^2}}
$$








### Lorentz Transformation
Suppose there are two frames, one stationary and one moving, and set the moving frame is moving at speed $v$.
Set an event is $E(x, t)$ in the stationary frame, $E'(x', t')$ in the moving frame. We expect to find a linear map between them, that is
$$
t = At' + Bx' \\
x = Ct' + Dx' \\
$$

First, for an event happening at the origin in the stationary frame, we can get
$$
\begin{aligned}
  & (x = 0, t) \\
  & (x' = -vt', t')  \\
\end{aligned}
\quad \Rightarrow \quad
\frac{C}{D} = v
$$

Second, considering the event that the light pulse reaches the right end of the train, we can get
$$
\begin{aligned}
  & (x = D_F, t = T_F) \\
  & (x' = L_M, t' = 0) 
\end{aligned}
\quad \Rightarrow \quad
\frac{B}{D} = \frac{T_F}{D_F} = \frac{v}{c^2}
$$

And then, considering the event that the moving clock reaches the right end of the stick, we can get
$$
\begin{aligned}
  & (x = L, t = L / v) \\
  & (x' = 0, t' = sL / v)
\end{aligned}
\quad \Rightarrow \quad
A = \frac{1}{s}, C = \frac{v}{s}
$$

Finally, we can get
$$
t = \frac{t' + vx' / c^2}{\sqrt{1 - v^2 / c^2}},\quad
x = \frac{x' + vt'}{\sqrt{1 - v^2 / c^2}}
\\~\\
t' = \frac{t - vx / c^2}{\sqrt{1 - v^2 / c^2}},\quad
x' = \frac{x - vt}{\sqrt{1 - v^2 / c^2}}
$$

#### Time Dilation
A clock is moving on a stick of length $L$ with speed $v$, then in the clock frame, there are 
$$
x'_2 - x'_1 = 0 \\
t'_2 - t'_1 = \frac{sL}{v} 
$$

So $$t_2 - t_1 = \frac{sL/v}{\sqrt{1 - v^2 / c^2}} = \frac{t'_2 - t'_1}{s} $$

#### Length Contraction
A rod of length $L$ lying along the $x$-axis of an inertial frame $K$. An observer in system $K'$ moving with speed $v$ along the $x$-axis measures the length of the rod, then he can get
$$
t'_1 - t'_2 = 0 \Rightarrow t_1 - t_2 = \frac{v(x_1 - x_2)}{c^2}
\\~\\
\begin{aligned}
  x'_1 - x'_2 &= \frac{(x_1 - x_2) - v(t_1 - t_2)}{\sqrt{1 - v^2 / c^2}} \\
  &= (x_1 - x_2)\sqrt{1 - \frac{v^2}{c^2}}
\end{aligned}
$$

So $\displaystyle L' = sL = L\sqrt{1 - \frac{v^2}{c^2}}$.


#### Invariant Interval
$$
\begin{aligned}
  c^2(\Delta t)^2 - (\Delta x)^2 &= \frac{c^2(\Delta t' + v\Delta x' / c^2)^2}{1 - v^2 / c^2} - \frac{(\Delta x' + v\Delta t')^2}{1 - v^2 / c^2} \\
  &= \frac{(\Delta t')^2(c^2 - v^2) - (\Delta x')^2(1 - v^2 / c^2)}{1 - v^2 / c^2} \\
  &= c^2(\Delta t')^2 - (\Delta x')^2 \\
  &\equiv (\Delta s)^2
\end{aligned}
$$

So under Lorentz transformation, the interval between events, that is, $$(\Delta s)^2 = c^2(\Delta t)^2 - (\Delta x)^2 - (\Delta y)^2 - (\Delta z)^2 $$ is invariant.

- When $s^2 > 0$, it's **timelike separation**. It is possible to find a frame in which the two events happen at the same place but at different time. $s/c$ is called the *proper time*. 
- When $s^2 < 0$, it's **spacelike separation**. It is possible to find a frame in which the two events happen at the same time but at different place. $|s|$ is called the *proper distance* or *proper length*.
- When $s^2 = 0$, it's **lightlike separation**. In every frame a photon emitted at one of the events will arrive at the other. 


#### Minkowski Diagram
Set $\displaystyle \beta = \frac{v}{c}, \gamma = \frac{1}{s} = \frac{1}{\sqrt{1 - \beta^2}}$, then
$$
ct = \gamma (ct') + \gamma\beta x' \\
x = \gamma x' + \gamma\beta(ct')
\\~\\
\begin{aligned}
  \Rightarrow \begin{pmatrix} ct \\ x \end{pmatrix} 
  &= \begin{pmatrix} \gamma  & \gamma\beta \\ \gamma\beta & \gamma \end{pmatrix}
  \begin{pmatrix} ct' \\ x' \end{pmatrix} \\
  &= \gamma \begin{pmatrix} 1 & \beta \\ \beta & 1 \end{pmatrix}
  \begin{pmatrix} ct' \\ x' \end{pmatrix} \\
\end{aligned}
$$

So the event $(1, 0)$ in $K'$ frame is $(\gamma, \gamma\beta)$ in $K$ frame, the event $(0, 1)$ in $K'$ frame is $(\gamma\beta, \gamma)$ in $K$ frame, the unit lengths for the $ct'$ and $x'$ axes change to 
$$\gamma\sqrt{1 + \beta^2} = \sqrt{\frac{1 + \beta^2}{1 - \beta^2}}$$









### Relativistic Doppler Effect
Let $\Delta t_0, \Delta t'$ be the time interval between the emission of two adjacent wave crests in the source and observer frame respectively, $\Delta t$ the time interval between the reception of the adjacent wave crests in the observer frame.
When the source is moving towards the observer at speed $v$, we can get
$$
\Delta t' = \gamma \Delta t \\~\\
\Delta t = \frac{c\Delta t' - v\Delta t'}{c} = \frac{1 - v/c}{\sqrt{1 - v^2 / c^2}}\Delta t_0 = \sqrt{\frac{1 - v/c}{1 + v/c}}\Delta t_0
$$

So 
$$f = \frac{\Delta t_0}{\Delta t}f_0 = \sqrt{\frac{1 + v/c}{1 - v/c}}f_0 $$

- When the source is moving away from the observer, we can simply replace $v$ by $-v$.
- When the source is fixed and the observer approaches it with speed $v$, this result is also valid.
- When the source is approaching, the wavelength is shifted toward shorter wavelengths, which is called **blueshift**.
- When the source is receding, the wavelength is shifted toward longer wavelengths, which is called **redshift**.

