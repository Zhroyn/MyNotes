
- [Steady Magnetic Field](#steady-magnetic-field)






# Steady Magnetic Field
The Ampere's Law is
$$d\vec{F}_{12} = \frac{\mu_0}{4\pi} \frac{i_2ds_2 \times (i_1ds_1 \times \hat{r}_{12})}{r_{12}^2}$$

$F_{12}$ and $F_{21}$ may not be equal.

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

Then we can define magnetic dipole moment
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
