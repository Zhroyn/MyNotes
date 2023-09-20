
- [Electric Charge](#electric-charge)






## Electric Charge
There are three kinds of charge density:
- Linear charge density: $\lambda = dq/dx$
- Surface charge density: $\sigma = dq/dA$
- Volume charge density: $\rho = dq/dV$

The force between a point charge and a ring of charge is $$F_z = \frac{1}{4\pi \epsilon_0} \frac{q_0qz}{(z^2 + R^2)^{3/2}}$$

The force between a point charge and a disk of charge is
$$
\begin{aligned}
  F_z &= \int_0^R \frac{1}{4\pi \epsilon_0} \frac{q_0 (2\pi \omega d \omega \cdot \sigma)}{z^2 + R^2} \frac{z}{\sqrt{z^2 + R^2}} \\
  &= \frac{1}{4\pi \epsilon_0} q_0 2\pi\sigma z \int_0^R \frac{\omega d\omega}{(z^2 + \omega^2)^{2/3}} \\
  &= \frac{1}{4\pi \epsilon_0} \cdot q_0 \frac{2\pi R^2 \sigma}{R^2} \cdot \left. \frac{z}{\sqrt{z^2 + \omega^2}} \right|_R^0 \\
  &= \frac{1}{4\pi \epsilon_0} \frac{2q_0q}{R^2} \left( 1 - \frac{z}{\sqrt{z^2 + R^2}} \right)
\end{aligned}
$$

