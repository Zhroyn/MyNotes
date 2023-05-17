<!-- TOC -->

- [The Theory of Relativity](#the-theory-of-relativity)
  - [Relativistic Velocity Addition Law](#relativistic-velocity-addition-law)
  - [Synchronizing Clocks](#synchronizing-clocks)

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

In the track frame, set after time $T_0$, the light pulse reaches the right end of the train, and set $D$ to be the distance between the ball and the light pulse at this time, $w$ to be the speed of the ball, $v$ to be the speed of the train, then
$$
D = cT_0 - wT_0 \\
L = cT_0 - vT_0
$$ Set after time $T_1$, the ball and the light pulse meet again, then:
$$
D = cT_1 + wT_1 \\
fL = cT_1 + vT_1
$$ So we can get
$$
\frac{D}{L} = \frac{c - w}{c - v} \\~\\
\frac{D}{fL} = \frac{c + w}{c + v} \\~\\
\Rightarrow f = \frac{c - w}{c + w}\cdot \frac{c + v}{c - v} \\~\\
\Rightarrow \frac{c - u}{c + u} = \frac{c - w}{c + w}\cdot \frac{c + v}{c - v} \\~\\
\Rightarrow \frac{c - w}{c + w} = \frac{c - u}{c + u}\cdot \frac{c - v}{c + v} \\~\\
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
Suppose two clocks have been synchronized by light in the train frame.
In the track frame, set $L_F$ to be length of train, $v$ to be the speed of the train, then we can get
$$
T_L = \frac{L_F/2}{c + v} \\~\\
T_R = \frac{L_F/2}{c - v} \\~\\
T_F = T_R - T_L = \frac{vL_F}{c^2 - v^2} \\~\\
D_F = c(T_L + T_R) = \frac{c^2L_F}{c^2 - v^2} \\~\\
\Rightarrow T_F = \frac{D_Fv}{c^2}
$$

Now suppose the two clocks are synchronized by sound instead in the train frame, and set $u$ to be the speed of the sound in the train frame, $w_L$ to be the left speed of the sound in the track frame, $w_R$ to be the right speed of the sound in the track frame, then we can get
$$
T_L = \frac{L_F/2}{w_L + v} \\~\\
T_R = \frac{L_F/2}{w_R - v} \\~\\
T = T_R - T_L = \frac{L_F}{2}\left( \frac{1}{w_R - v} - \frac{1}{w_L + v} \right) \\~\\
D = w_LT_L + w_RT_R = \frac{L_F}{2}\left( \frac{w_R}{w_R - v} + \frac{w_L}{w_L + v} \right) \\~\\
\Rightarrow \frac{T}{D} = \frac{2v - (w_R - w_L)}{2w_Rw_L + v(w_R - w_L)}
$$

Because $$w_R = \frac{u + v}{1 + \left( \dfrac{u}{c} \right)\left( \dfrac{v}{c} \right)}, w_L = \frac{u - v}{1 - \left( \dfrac{u}{c} \right)\left( \dfrac{v}{c} \right)} $$

So we can get 
$$
\begin{aligned}
  T &= \frac{L_F}{2}\left[ \frac{1 + \left( \frac{u}{c} \right)\left( \frac{v}{c} \right)}{u + v - v - v\left( \frac{u}{c} \right)\left( \frac{v}{c} \right)} - \frac{1 - \left( \frac{u}{c} \right)\left( \frac{v}{c} \right)}{u - v + v - v\left( \frac{u}{c} \right)\left( \frac{v}{c} \right)} \right] \\
  &= \frac{L_F}{2} \frac{2\left( \frac{u}{c} \right)\left( \frac{v}{c} \right)}{u - v\left( \frac{u}{c} \right)\left( \frac{v}{c} \right)} 
  = \frac{vL_F}{c^2 - v^2} = T_F
\end{aligned}
\\~\\
\begin{aligned}
  D &= \frac{L_F}{2}\left[ \frac{u + v}{u + v - v - v\left( \frac{u}{c} \right)\left( \frac{v}{c} \right)} + \frac{u - v}{u - v + v - v\left( \frac{u}{c} \right)\left( \frac{v}{c} \right)} \right] \\
  &= \frac{L_F}{2} \frac{2u}{u - v\left( \frac{u}{c} \right)\left( \frac{v}{c} \right)} 
  = \frac{c^2L_F}{c^2 - v^2} = D_F
\end{aligned}
$$

All in all, if two clocks are **synchronized** and **separated** in a proper frame, then in a frame in which the clocks move along the line joining them with speed $v$, **the rear clock will be ahead of the front clock** by $\displaystyle \frac{Dv}{c^2}$, where $D$ denotes the distance between the clocks in the second frame.






