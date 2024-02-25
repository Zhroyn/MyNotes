
- [Lipschitz Conditon](#lipschitz-conditon)
- [Convex Function](#convex-function)
  - [Smooth and Convex Function](#smooth-and-convex-function)
- [Strongly Convex Function](#strongly-convex-function)
  - [Smooth and Strongly Convex Function](#smooth-and-strongly-convex-function)




## Lipschitz Conditon
**Definition**
Let $Q$ be a subset of $\mathbb{R}^n$. We denote by $C_{L}^{k,p}(Q)$ the class of functions with the following properties:
- Any $f \in C_{L}^{k,p}(Q)$ is $k$ times continuously differentiable on $Q$
- Its $p$­th derivative is Lipschitz continuous on $Q$ with the constant $L$: $$\left\| f^{(p)}(\bm{x}) - f^{(p)}(\bm{y}) \right\| \le L\left\| \bm{x} - \bm{y} \right\|$$

**Lemma7**
$f(\bm{x}) \in C_L^{2,1}$ if and only if $$\left\| \nabla^2 f(\bm{x}) \right\| \le L$$

**Lemma9**
If $f(\bm{x}) \in C_L^{1,1}$, then $$\left| f(\bm{y}) - f(\bm{x}) - \left< \nabla f(\bm{x}), \bm{y} - \bm{x} \right> \right| \le \frac{L}{2} \left\| \bm{y} - \bm{x} \right\|^2$$

**Lemma10**
If $f(\bm{x}) \in C_M^{2,2}$, then $$\left\| \nabla f(\bm{y}) - \nabla f(\bm{x}) - \nabla^2 f(\bm{x}) (\bm{y} - \bm{x}) \right\| \le \frac{M}{2} \left\| \bm{y} - \bm{x} \right\|^2$$





<br>

## Convex Function
**Difinition: Convex Set**
A set $\mathcal{Q} \subseteq \mathbb{R}^n$ is called convex if for any $x, y \in \mathcal{Q}$ and $\alpha \in [0, 1]$ we have $$\alpha\bm{x} + (1 - \alpha)\bm{y} \in \mathcal{Q}$$


**Difinition: Convex Function**
A continuously differentiable function $f(\cdot)$ is called convex on a convex set $\mathcal{Q}$ if for any $x, y \in Q$ we have $$f(\bm{y}) \ge f(\bm{x}) + \left< \nabla f(\bm{x}), \bm{y} - \bm{x} \right>$$

If $-f(\bm{x})$ is convex, we call $f(\bm{x})$ concave.

We denote by $\mathcal{F}^k(\mathcal{Q})$ the class of convex functions with the following properties:
- Any $f \in \mathcal{F}^k(\mathcal{Q})$ is a convex function
- Any $f \in \mathcal{F}^k(\mathcal{Q})$ is $k$ times continuously differentiable on $\mathcal{Q}$

<br>

**Theorem 23**
A continuously differentiable function $f$ belongs to the class $\mathcal{F}^1$ if and only if for any $\alpha \in [0, 1]$, we have $$f(\alpha\bm{x} + (1 - \alpha)\bm{y}) \le \alpha f(\bm{x}) + (1 - \alpha) f(\bm{y})$$

**Theorem 24**
A continuously differentiable function $f$ belongs to the class $\mathcal{F}^1$ if and only if $$\left< \nabla f(\bm{x}) - \nabla f(\bm{y}), \bm{x} - \bm{y} \right> \ge 0$$

**Theorem 24**
A continuously differentiable function $f$ belongs to the class $\mathcal{F}^2$ if and only if $$\nabla^2 f(\bm{x}) \ge 0$$


<br>

### Smooth and Convex Function
We denote by $\mathcal{F}_{L}^{k,l}(\mathbb{R}^n)$ the class of functions with the following properties:
- Any $f \in \mathcal{F}_{L}^{k,l}(\mathbb{R}^n)$ is convex
- Any $f \in \mathcal{F}_{L}^{k,l}(\mathbb{R}^n)$ also belongs to $C_{L}^{k,l}(\mathbb{R}^n)$

**Theorem 27**
All conditions below, holding for all $\bm{x}, \bm{y} \in \mathbb{R}^n$ and $\alpha \in [0, 1]$, are equivalent to the inclusion $f \in \mathcal{F}_{L}^{k,l}(\mathbb{R}^n)$:

$$0 \le f(\bm{y}) - f(\bm{x}) - \left< \nabla f(\bm{x}), \bm{y} - \bm{x} \right> \le \frac{L}{2} \left\| \bm{y} - \bm{x} \right\|^2$$

$$f(\bm{x}) + \left< \nabla f(\bm{x}), \bm{y} - \bm{x} \right> + \frac{1}{2L} \left\| \nabla f(\bm{x}) - \nabla f(\bm{y}) \right\|^2 \le f(\bm{y})$$

$$\frac{1}{L} \left\| \nabla f(\bm{x}) - \nabla f(\bm{y}) \right\|^2 \le \left< \nabla f(\bm{x}) - \nabla f(\bm{y}), \bm{x} - \bm{y} \right>$$

$$0 \le \left< \nabla f(\bm{x}) - \nabla f(\bm{y}), \bm{x} - \bm{y} \right> \le L\left\| \bm{x} - \bm{y} \right\|^2$$

$$\alpha f(\bm{x}) + (1 - \alpha) f(\bm{y}) \ge f(\alpha\bm{x} + (1 - \alpha)\bm{y}) + \frac{\alpha(1 - \alpha)}{2L} \left\| \nabla f(\bm{x}) - \nabla f(\bm{y}) \right\|^2$$

$$0 \le \alpha f(\bm{x}) + (1 - \alpha) f(\bm{y}) - f(\alpha\bm{x} + (1 - \alpha)\bm{y}) \le \alpha(1 - \alpha) \frac{L}{2} \left\| \bm{x} - \bm{y} \right\|^2$$

**Theorem 28**
Twice continuously differentiable function $f$ belongs to the class $\mathcal{F}_L^{2,1}$ if and only if $$0 \le \nabla^2 f(\bm{x}) \le LI_n$$






<br>

## Strongly Convex Function
**Difinition: Convex Function**
A continuously differentiable function $f(\bm{x})$ is called strongly convex on $\mathbb{R}^n$ if for any $x, y \in \mathbb{R}^n$ we have $$f(\bm{y}) \ge f(\bm{x}) + \left< \nabla f(\bm{x}), \bm{y} - \bm{x} \right> + \frac{1}{2} \mu \left\| \bm{y} - \bm{x} \right\|^2$$

which is notated as $f \in \mathcal{S}_{\mu}^1(\mathbb{R}^n)$. $\mu$ is called the convexity parameter of $f$.

<br>

**Theorem 32**
If $f \in \mathcal{S}_{\mu}^{1}(\mathbb{R}^n)$, then for all $\bm{x}, \bm{y} \in \mathbb{R}^n$, we have:
$$f(\bm{y}) \le f(\bm{x}) + \left< \nabla f(\bm{x}), \bm{y} - \bm{x} \right> + \frac{1}{2\mu} \left\| \nabla f(\bm{x}) - \nabla f(\bm{y}) \right\|^2$$

$$\left< \nabla f(\bm{x}) - \nabla f(\bm{y}), \bm{x} - \bm{y} \right> \le \frac{1}{\mu} \left\| \nabla f(\bm{x}) - \nabla f(\bm{y}) \right\|^2$$

**Theorem 33**
All conditions below, holding for all $\bm{x}, \bm{y} \in \mathbb{R}^n$ and $\alpha \in [0, 1]$, are equivalent to the inclusion $f \in \mathcal{S}_{\mu}^{1}(\mathbb{R}^n)$:

$$\left< \nabla f(\bm{x}) - \nabla f(\bm{y}), \bm{x} - \bm{y} \right> \ge \mu \left\| \bm{x} - \bm{y} \right\|^2$$

$$\alpha f(\bm{x}) + (1 - \alpha) f(\bm{y}) - f(\alpha\bm{x} + (1 - \alpha)\bm{y}) \ge \alpha(1 - \alpha) \frac{\mu}{2} \left\| \bm{x} - \bm{y} \right\|^2$$

**Theorem 34**
Two times continuously differentiable function $f$ belongs to the class $\mathcal{S}_{\mu}^{2}$ if and only if $$\nabla^2 f(\bm{x}) \ge \mu I_n$$


<br>

### Smooth and Strongly Convex Function
**Definition**
A function $f \in \mathcal{S}_{\mu, L}^{k, l}$ is and only if $f \in \mathcal{S}_{\mu}^k$ and $f \in C_L^{k, l}$.

<br>

**Theorem 36**
If $f \in \mathcal{S}_{\mu, L}^{1, 1}(\mathbb{R}^n)$, then for all $\bm{x}, \bm{y} \in \mathbb{R}^n$, we have:
$$\left< \nabla f(\bm{x}) - \nabla f(\bm{y}), \bm{x} - \bm{y} \right> \ge \frac{\mu L}{\mu + L} \left\| \bm{x} - \bm{y} \right\|^2 + \frac{1}{\mu + L} \left\| \nabla f(\bm{x}) - \nabla f(\bm{y}) \right\|^2$$

