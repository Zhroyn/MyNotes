
- [Maxwell's Equation](#maxwells-equation)
  - [The Basic Equations of Electromagnetisms](#the-basic-equations-of-electromagnetisms)
  - [Induced Magnetic Field and the Displacement current](#induced-magnetic-field-and-the-displacement-current)
  - [Maxwell’s Equations](#maxwells-equations)




## Maxwell's Equation
### The Basic Equations of Electromagnetisms
In vacuum, we have
$$
\begin{cases}
    \oiint \vec{E} \bullet d\vec{A} = \dfrac{q_0}{\epsilon_0} \\
    \oiint \vec{B} \bullet d\vec{A} = 0 \\
    \oint \vec{E} \bullet d\vec{l} = - \dfrac{d\Phi_B}{dt} = - \iint \dfrac{\partial \vec{B}}{\partial t} \bullet d\vec{A} \\
    \oint \vec{B} \bullet d\vec{l} = \mu_0 i
\end{cases}
$$

In the dielectric and magnetic materials,
$$
\begin{cases}
    \oiint \vec{D} \bullet d\vec{A} = q_0 \\
    \oiint \vec{B} \bullet d\vec{A} = 0 \\
    \oint \vec{E} \bullet d\vec{l} = - \iint \dfrac{\partial \vec{B}}{\partial t} \bullet d\vec{A} \\
    \oint \vec{H} \bullet d\vec{l} = i_0 = \iint \vec{j}_0 \bullet d\vec{A}
\end{cases}
\; \Rightarrow \; 
\begin{cases}
    \nabla \bullet \vec{D} = \rho_{e_0} \\
    \nabla \bullet \vec{B} = 0 \\
    \nabla \times \vec{E} = - \dfrac{\partial \vec{B}}{\partial t} \\
    \nabla \times \vec{H} = \vec{j}_0
\end{cases}
$$

where $\vec{D} = \epsilon_0 \vec{E} + \vec{P}$, $\vec{H} = \dfrac{\vec{B}}{\mu_0} - \vec{M}$, $\epsilon_0 = 8.85\times 10^{-12} F/m$, $\mu_0 = 4\pi\times 10^{-7} N/A^2$.







<br>

### Induced Magnetic Field and the Displacement current
To make $\oint \vec{H} \bullet d\vec{l}$ same for different surfaces, we need to introduce displacement current $i_D$ in the region between the plates, equal to the current in the wire. Then we have $$\oint \vec{H} \bullet d\vec{l} = i_0 + i_D$$

Because
$$
\Phi_D = \iint \vec{D} \bullet d\vec{A} \\~\\
i_D = \frac{d\Phi_D}{dt} = \iint \frac{\partial \vec{D}}{\partial t} \bullet d\vec{A} \\~\\
\vec{j}_D = \frac{\partial \vec{D}}{\partial t}
$$

Now we have the New Ampere’s Loop Law $$\oint \vec{H} \bullet d\vec{l} = \iint (\vec{j}_0 + \frac{\partial \vec{D}}{\partial t}) \bullet d\vec{A} = i_0 + \iint \frac{\partial \vec{D}}{\partial t} \bullet d\vec{A}$$

So the changing electric field will generate induced magnetic field.

For a enclosed surface, we have
$$
\begin{cases}
    \oiint \vec{j}_0 \bullet d\vec{A} = - \dfrac{dq_0}{dt} \\
    \oiint \vec{D} \bullet d\vec{A} = q_0
\end{cases}
\\~\\
\Rightarrow \oiint \vec{j}_0 \bullet d\vec{A} = - \oiint \frac{\partial \vec{D}}{\partial t} \bullet d\vec{A} \\~\\
\Rightarrow \oiint (\vec{j}_0 + \frac{\partial \vec{D}}{\partial t}) \bullet d\vec{A} = 0
$$






<br>

### Maxwell’s Equations
$$
\begin{cases}
    \oiint \vec{D} \bullet d\vec{A} = q_0 \\
    \oiint \vec{B} \bullet d\vec{A} = 0 \\
    \oint \vec{E} \bullet d\vec{l} = - \iint \dfrac{\partial \vec{B}}{\partial t} \bullet d\vec{A} \\
    \oint \vec{H} \bullet d\vec{l} = i_0 + \iint \dfrac{\partial \vec{D}}{\partial t} \bullet d\vec{A}
\end{cases}
\; \Rightarrow \; 
\begin{cases}
    \nabla \bullet \vec{D} = \rho_{e_0} \\
    \nabla \bullet \vec{B} = 0 \\
    \nabla \times \vec{E} = - \dfrac{\partial \vec{B}}{\partial t} \\
    \nabla \times \vec{H} = \vec{j}_0 + \dfrac{\partial \vec{D}}{\partial t}
\end{cases}
$$

