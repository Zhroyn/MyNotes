
- [Steady Magnetic Field](#steady-magnetic-field)
  - [Biot-Savart Law](#biot-savart-law)
  - [The Gauss’Law and Ampere’s Loop Law of a magnetic field](#the-gausslaw-and-amperes-loop-law-of-a-magnetic-field)






# Steady Magnetic Field
## Biot-Savart Law
The Ampere's Law is
$$d\vec{F}_{12} = \frac{\mu_0}{4\pi} \frac{i_2ds_2 \times (i_1ds_1 \times \hat{r}_{12})}{r_{12}^2}$$

with $\mu_0 = 4\pi\times 10^{-7} N/A^2$. $F_{12}$ and $F_{21}$ may not be equal.

The Magnetic Induction Strength is $$\vec{B} = \frac{\mu_0}{4\pi} \oint_{L} \frac{id\vec{s} \times \hat{r}}{r^2}$$

---
For a section of line,
$$
x = -r_0\cot\theta \Rightarrow dx = \frac{r_0d\theta}{\sin^2\theta} \\~\\
B = \int_{\theta_1}^{\theta_2} \frac{\mu_0i}{4\pi} \frac{\sin\theta \cdot \dfrac{r_0d\theta}{\sin^2\theta}}{(r_0/\sin\theta)^2} = \frac{\mu_0i}{4\pi r_0} \int_{\theta_1}^{\theta_2} \sin\theta d\theta = \frac{\mu_0i}{4\pi r_0} (\cos\theta_1 - \cos\theta_2)
$$

When the line is infinite, $B = \dfrac{\mu_0i}{2\pi r_0}$.

---
For a circular loop,
$$
B = \frac{\mu_0i}{4\pi} \oint \frac{ds}{(r_0/\sin\theta)^2} \cos\theta = \frac{\mu_0iR}{2r_0^2} \sin^2\theta \cos\theta = \frac{\mu_0}{2} \frac{iR^2}{(R^2 + r_0^2)^{3/2}}
$$

When at center, $B = \dfrac{\mu_0i}{2R}$.

When $r >> R$, $B = \dfrac{\mu_0iR^2}{2r_0^3} = \dfrac{\mu_0i\pi R^2}{2\pi r_0^3} = \dfrac{\mu_0iA}{2\pi r_0^3}$.

Then we can define magnetic dipole moment as
$$
\mu = iA = i\pi R^2 \\~\\
B = \frac{\mu_0}{2\pi} \frac{\mu}{r^3}
$$

---
For a flat strip of copper with negligible thickness
$$
d = \frac{R}{\cos\theta} \\~\\
dB_x = dB \cdot \cos\theta = \frac{\mu_0 \dfrac{i}{a} dx}{2\pi d} \cdot \cos\theta \\~\\
x = R\tan\theta \Rightarrow dx = \frac{Rd\theta}{\cos^2\theta} \\~\\
\begin{aligned}
  B_x &= \frac{\mu_0 i}{2\pi aR} \int \cos^2\theta dx = \frac{\mu_0 i}{2\pi a} \int_{-\alpha}^{\alpha} d\theta \\
  &= \frac{\mu_0 i}{\pi a} \alpha = \frac{\mu_0 i}{\pi a} \tan^{-1} \frac{a}{2R}
\end{aligned}
$$

When $R >> a$, $B = \dfrac{\mu_0 i}{2\pi R}$.

When $R \rightarrow 0$, $B = \dfrac{\mu_0 i}{2a}$.

---
Let the length of solenoid be $L$, the radius as $R$, the number of turns per unit length as $n$, then
$$
B = \frac{\mu_0}{2} \int_{- \frac{L}{2}}^{\frac{L}{2}} \frac{iR^2 \cdot ndl}{[R^2 + (x - l)^2]^{3/2}} \\~\\
\frac{x - 1}{R} = \cot\beta \Rightarrow dl = \frac{R}{\sin^2\beta} d\beta \\~\\
\begin{aligned}
  B &= \frac{\mu_0}{2} \int_{-\beta_1}^{\beta_2} \frac{R^2 ni \dfrac{R}{\sin^2\beta} d\beta}{\left( \dfrac{R^2}{\sin^2\beta} \right)^{3/2}} \\
  &= \frac{\mu_0}{2} \cdot ni \int_{-\beta_1}^{\beta_2} \sin\beta d\beta \\
  &= \frac{1}{2} \mu_0ni (\cos\beta_1 - \cos\beta_2)
\end{aligned}
$$

When $L\rightarrow \infty$, $\beta_1 = 0, \beta = \pi, B = \mu_0ni$.

At the end of solenoid, $\beta_1 = 0, \beta_2 = \dfrac{\pi}{2}, B = \frac{1}{2} \mu_0ni$.

For a solenoid with many layers,
$$
\begin{aligned}
  B &= \int_{R_1}^{R_2} \frac{1}{2} \mu_0 \frac{Ni}{2l(R_2 - R_1)} \cdot \frac{2l}{\sqrt{l^2 + r^2}} dr \\
  &= \mu_0 jl \int_{R_1}^{R_2} \frac{dr}{\sqrt{l^2 + r^2}} \\
  &= \mu_0 jl \ln \frac{R_2 + \sqrt{R_2^2 + l^2}}{R_1 + \sqrt{R_1^2 + l^2}} \\
\end{aligned}
$$








<br>

## The Gauss’Law and Ampere’s Loop Law of a magnetic field
The Gauss' Law of s magnetic field is $$\oiint B\bullet dA = 0$$

The Ampere’s Loop Law of a magnetic field is $$\oint B\bullet dl = \mu_0 \sum_{in\ loop} i$$

