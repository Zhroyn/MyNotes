<!-- TOC -->

- [Image Matching](#image-matching)
  - [Detection](#detection)
    - [Principal Component Analysis](#principal-component-analysis)
    - [Corner Detection](#corner-detection)
    - [Gradient Operators](#gradient-operators)
    - [Harris Detector](#harris-detector)
  - [Description](#description)
  - [Matching](#matching)

<!-- /TOC -->






## Image Matching
### Detection
#### Principal Component Analysis
- To measure uniqueness, We can use principal component analysis (PCA).
- The 1st principal component is the direction with highest variance.
- The 2nd principal component is the direction with highest variance which is orthogonal to the previous components.
- Procedures
  1. Subtract off the mean for each data point.
  2. Compute the covariance matrix.
  3. Compute eigenvectors and eigenvalues.
  4. The components are the eigenvectors ranked by the eigenvalues.

#### Corner Detection
1. Compute the covariance matrix at each point
$\displaystyle H = \sum_{(u,v)} w(u,v) 
\begin{bmatrix} I_x^2 & I_xI_y \\ I_xI_y & I_y^2 \end{bmatrix}, 
I_x = \frac{\partial f}{\partial x}, 
I_y = \frac{\partial f}{\partial x} \\
\text{w(u,v) is typically Gaussian weights} $

2. Compute eigenvalues
$\displaystyle H = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, 
\lambda_{\pm} = \frac{1}{2}((a + d) \pm \sqrt{4bc + (a - d)^2}) $

3. Classify points using eigenvalues of H

#### Gradient Operators
**Roberts operator**
$\begin{bmatrix}
    +1 & 0 \\ 
    0 & -1 \\ 
\end{bmatrix}, 
\begin{bmatrix}
    0 & +1 \\ 
    -1 & 0 \\ 
\end{bmatrix}$

**Prewitt operator**
$\begin{bmatrix}
    -1 & 0 & +1\\ 
    -1 & 0 & +1\\ 
    -1 & 0 & +1\\ 
\end{bmatrix}, 
\begin{bmatrix}
    +1 & +1 & +1 \\ 
    0 & 0 & 0 \\ 
    -1 & -1 & -1 \\ 
\end{bmatrix}$

**Sobel operator**
$\begin{bmatrix}
    -1 & 0 & +1\\ 
    -2 & 0 & +2\\ 
    -1 & 0 & +1\\ 
\end{bmatrix}, 
\begin{bmatrix}
    +1 & +2 & +1 \\ 
    0 & 0 & 0 \\ 
    -1 & -2 & -1 \\ 
\end{bmatrix}$

#### Harris Detector
$\displaystyle f = \frac{\lambda_1\lambda_2}{\lambda_1 + \lambda_2}
= \frac{determinant(H)}{trace(H)} = \frac{ad - bc}{a + d} \\
\text{f is called corner response} $
1. Compute derivatives at each pixel
2. Compute covariance matrix $H$ in a Gaussian window around each pixel 
3. Compute corner response function $f$
4. Threshold $f$
5. Find local maxima of response function (nonmaximum suppression)



### Description
### Matching






