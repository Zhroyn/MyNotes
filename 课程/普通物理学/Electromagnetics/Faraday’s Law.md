
- [Faraday's Law](#faradays-law)
  - [Faraday's Law of Induction and Lenz's Law](#faradays-law-of-induction-and-lenzs-law)
  - [Motional emf and Induced emf](#motional-emf-and-induced-emf)




## Faraday's Law
### Faraday's Law of Induction and Lenz's Law
Define the flux of the magnetic field through an open surface as: $$\Phi_B = \iint B \bullet dA$$

**Faraday's Law**: The electromotive force (emf) induced in a circuit is $$\epsilon = - \frac{d\Phi_B}{dt}$$

The minus sign is given by **Lenz's Law**. The induced current will appear in such a direction that it opposes the change in flux that produced it.

---
For generator, 
$$
\Phi_B = BA\cos\theta = BA\cos\omega t \\~\\
\Rightarrow \epsilon = BA\omega \sin\omega t
$$





<br>

### Motional emf and Induced emf
For motional emf, we have $$\epsilon = \int_{-}^{+} K \bullet dl = \int_C^D (\vec{v} \times \vec{B}) \bullet dl$$

For induced emf, we have 
$$
\epsilon = \oint \vec{E} \bullet d\vec{l}
= \oint (\vec{E}_{std} + \vec{E}_{ind}) \bullet d\vec{l}
= - \iint \frac{\partial \vec{B}}{\partial t} \cdot d\vec{A} \\~\\
\Rightarrow \nabla \times \vec{E} =
\begin{vmatrix}
  \vec{i} & \vec{j} & \vec{k} \\[1pt]
  \frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\[3pt]
  E_x & E_y & E_z \\
\end{vmatrix}
= - \frac{\partial \vec{B}}{\partial t}
$$

In spherical coordinates,
$$
\nabla \times \vec{E} = \frac{1}{r^2\sin\theta}
\begin{vmatrix}
  \hat{r} & r\hat{\theta} & r\sin\theta\hat{\phi} \\[1pt]
  \frac{\partial }{\partial r} & \frac{\partial }{\partial \theta} & \frac{\partial }{\partial \phi} \\[3pt]
  E_r & r E_{\theta} & r\sin\theta E_{\phi} \\
\end{vmatrix}
$$

In cylindrical coordinates,
$$
\nabla \times \vec{E} = \frac{1}{r}
\begin{vmatrix}
  \hat{r} & r\hat{\theta} & \hat{z} \\[1pt]
  \frac{\partial }{\partial r} & \frac{\partial }{\partial \theta} & \frac{\partial }{\partial z} \\[3pt]
  E_r & r E_{\theta} & E_{z} \\
\end{vmatrix}
$$

