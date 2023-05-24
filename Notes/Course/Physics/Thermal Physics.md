<!-- TOC -->

- [Thermal Physics](#thermal-physics)
  - [Basic Concepts](#basic-concepts)
    - [Temperature Scales](#temperature-scales)
    - [Thermal Expansion](#thermal-expansion)
    - [Ideal Gases](#ideal-gases)
    - [Real Gases](#real-gases)

<!-- /TOC -->






## Thermal Physics
### Basic Concepts
#### Temperature Scales
Absolute temperature (Kelvin) scale: $\displaystyle T = T_{\text{triple}} \frac{p}{p_{\text{triple}}} \approx \frac{237.15}{610} p $

Celsius scale: $T_C = T - 237.15$

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
The Van der Waals equation of state is
$$
(P + \frac{an^2}{V^2})(V - nb) = nRT
$$

$a$ is about the attractive forces between the gas molecules
$b$ is about the volume of gas molecule







