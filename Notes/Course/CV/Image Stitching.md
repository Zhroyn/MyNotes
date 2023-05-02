<!-- TOC -->

- [Image Stitching](#image-stitching)
  - [Affine Transformation](#affine-transformation)
  - [Projective Transformation](#projective-transformation)
  - [RANSAC](#ransac)

<!-- /TOC -->






## Image Stitching
### Affine Transformation
$\begin{bmatrix}x'\\ y' \\ 1 \end{bmatrix}
= \begin{bmatrix}a &b & c \\ d & e & f \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix}x \\ y \\ 1 \end{bmatrix}
= \begin{bmatrix}ax+by+c \\ dx+ey+f \\ 1 \end{bmatrix} $

$\texttt{Solution1:}$
$\begin{bmatrix}x' \\ y' \end{bmatrix}
= \begin{bmatrix}x & y & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & x & y & 1 \end{bmatrix}
= \begin{bmatrix}a \\ b \\ c \\ d \\ e \\ f \end{bmatrix} $

$\begin{bmatrix}
  x_1 & y_1 & 1 & 0 & 0 & 0 \\
  0 & 0 & 0 & x_1 & y_1 & 1 \\
  x_2 & y_2 & 1 & 0 & 0 & 0 \\
  0 & 0 & 0 & x_2 & y_2 & 1 \\
  \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
  x_n & y_n & 1 & 0 & 0 & 0 \\
  0 & 0 & 0 & x_n & y_n & 1 \\
\end{bmatrix}
\begin{bmatrix}a \\ b \\ c \\ d \\ e \\ f \end{bmatrix}
= \begin{bmatrix}x_1' \\ y_1' \\ x_2' \\ y_2' \\ \vdots \\ x_n' \\ y_n' \end{bmatrix} $

$\Rightarrow \bm{\underset{2n\times 6}{A}\; \underset{6\times 1}{t} = \underset{2n\times 1}{b}} $

- Least squares: find $\bm{t} $ that minimizes $\bm{||At - b||^2}$
- The solution is given by
$$
\bm{A^TAt = A^tb } \\
\bm{t = (A^TA)^{-1}A^tb } \\
$$

$\texttt{Solution2:}$
$\begin{bmatrix}
  x_1 & y_1 & 1 & 0 & 0 & 0 & -x_1' \\
  0 & 0 & 0 & x_1 & y_1 & 1 & -y_1' \\
  x_2 & y_2 & 1 & 0 & 0 & 0 & -x_1' \\
  0 & 0 & 0 & x_2 & y_2 & 1 & -y_1' \\
  &&&& \vdots \\
  x_n & y_n & 1 & 0 & 0 & 0 & -x_n' \\
  0 & 0 & 0 & x_n & y_n & 1 & -y_n' \\
\end{bmatrix}
\begin{bmatrix} a \\ b \\ c \\ d \\ e \\ f \\ 1 \end{bmatrix}
= \begin{bmatrix}0 \\ 0 \\ \vdots \\ 0 \\ 0 \end{bmatrix} $

### Projective Transformation
$\begin{bmatrix}x'\\ y' \\ 1 \end{bmatrix}
\cong \begin{bmatrix}h_{00} & h_{01} & h_{02} \\ h_{10} & h_{11} & h_{12} \\ h_{20} & h_{21} & h_{22} \end{bmatrix}
\begin{bmatrix}x \\ y \\ 1 \end{bmatrix} $

$\displaystyle x_i' = \frac{h_{00}x_i + h_{01}y_i + h_{02}}{h_{20}x_i + h_{21}y_i + h_{22}} \\~\\
\displaystyle y_i' = \frac{h_{10}x_i + h_{11}y_i + h_{12}}{h_{20}x_i + h_{21}y_i + h_{22}} $

$x_i'(h_{20}x_i + h_{21}y_i + h_{22}) = h_{00}x_i + h_{01}y_i + h_{02}\\
y_i'(h_{20}x_i + h_{21}y_i + h_{22}) = h_{10}x_i + h_{11}y_i + h_{12} $

$\begin{bmatrix}
  x_1 & y_1 & 1 & 0 & 0 & 0 & -x_1'x_1 & -x_1'y_1 & -x_1' \\
  0 & 0 & 0 & x_1 & y_1 & 1 & -y_1'x_1 & -y_1'y_1 & -y_1' \\
  &&&& \vdots \\
  x_n & y_n & 1 & 0 & 0 & 0 & -x_n'x_n & -x_n'y_n & -x_n' \\
  0 & 0 & 0 & x_n & y_n & 1 & -y_n'x_n & -y_n'y_n & -y_n'\\
\end{bmatrix}
\begin{bmatrix}h_{00} \\ h_{01} \\ h_{02} \\ h_{10} \\ h_{11} \\ h_{12} \\ h_{20} \\ h_{21} \\ h_{22} \end{bmatrix}
= \begin{bmatrix}0 \\ 0 \\ \vdots \\ 0 \\ 0 \end{bmatrix} $

$\Rightarrow \bm{\underset{2n\times 9}{A}\; \underset{9\times 1}{h} = \underset{2n\times 1}{0}} $

- Least squares: find $\bm{h} $ that minimizes $\bm{||Ah - 0||^2}$
- Since $\bm{h}$ is defined up to scale, solve for unit vector $\hat{\bm{h}}$
- Solution: $\hat{\bm{h}}$ = eigenvector of $\bm{A^TA}$ with smallest eigenvalue

### RANSAC
1. Randomly choose ***s*** samples. Typically ***s*** = minimum sample size that lets you fit a model
2. Fit a model (e.g., transformation matrix) to those samples
3. Count the number of inliers that approximately fit the model
4. Repeat N times
5. Choose the model that has the largest set of inliers



