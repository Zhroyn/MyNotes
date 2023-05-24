<!-- TOC -->

- [Thermal Physics](#thermal-physics)
  - [Basic Concepts](#basic-concepts)
    - [The Laws of Thermodynamics](#the-laws-of-thermodynamics)
    - [Temperature Scales](#temperature-scales)
    - [Thermal Expansion](#thermal-expansion)
    - [Ideal Gases](#ideal-gases)
    - [Real Gases](#real-gases)

<!-- /TOC -->






## Thermal Physics
### Basic Concepts
#### The Laws of Thermodynamics
**The Zeroth Law of Thermodynamics**: If two systems are in thermal equilibrium with a third system, then they must be in thermal equilibrium with each other.

**The Third Law of Thermodynamics**: It is impossible for any procedure to lead to the isotherm $T= 0$ in a finite number of steps.

#### Temperature Scales
Absolute temperature (Kelvin) scale: $\displaystyle T = T_{\text{triple}} \frac{p}{p_{\text{triple}}} \approx \frac{273.16}{610} p $
$273.16$ is the difference between absolute zero and the temperature of the triple point of water .

Celsius scale: $T_C = T - 273.15$

Fahrenheit scale: $\displaystyle T_F = \frac{9}{5}T_C + 32^{\circ}F$


#### Thermal Expansion
Linear expansion: $\Delta L = \alpha L_0 \Delta T$
Volume expansion: $\Delta V = \beta V_0 \Delta T$
$$
L^3 = [L_0(1 + \alpha \Delta T)]^3 = L_0^3(1 + 3\alpha \Delta T + O(\Delta T)^2) \\~\\
V = V_0(1 + \beta \Delta T) \\~\\
\Rightarrow \beta = 3\alpha 
$$


#### Ideal Gases
Equation of state for an ideal gas:
$$
PV = nRT \\~\\
PV = \frac{N}{N_A}RT = Nk_BT
$$

where $R = 8.315 \text{ J/mol}\cdot\text{K}$, $\displaystyle k_B = \frac{R}{N_A} = 1.38\times 10^{-23} \text{ J/K}$.

Therefore $$\ln V = \ln T + \ln(nR / P)$$

Then we can get 
$$
\beta = \left( \frac{1}{V} \frac{dV}{dT} \right)_p 
= \left( \frac{d(\ln V)}{dT} \right)_p 
= \frac{d(\ln T)}{dT} = \frac{1}{T}
$$

#### Real Gases
The van der Waals equation of state is
$$
(P + \frac{an^2}{V^2})(V - nb) = nRT
$$

$a$ is about the attractive forces between the gas molecules.
$b$ is about the volume of gas molecule.







