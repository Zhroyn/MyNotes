<!-- TOC -->

- [Image Matching](#image-matching)
  - [Detection](#detection)
    - [Principal Component Analysis](#principal-component-analysis)
    - [Corner Detection](#corner-detection)
    - [Gradient Operators](#gradient-operators)
    - [Harris Detector](#harris-detector)
    - [Blob Detector](#blob-detector)
  - [Description](#description)
    - [SIFT Descriptor](#sift-descriptor)
  - [Matching](#matching)
- [Image Warping](#image-warping)
  - [Affine Transformation](#affine-transformation)
  - [Projective Transformation (Homography)](#projective-transformation-homography)
  - [Implement](#implement)
- [Image Stitching](#image-stitching)
  - [Affine Transformation](#affine-transformation-1)
  - [Projective Transformation](#projective-transformation)
  - [RANSAC](#ransac)

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
\lambda_{\pm} = \frac{1}{2}((a  d) \pm \sqrt{4bc  (a - d)^2}) $

3. Classify points using eigenvalues of H

#### Gradient Operators
**Roberts Operator**
$\begin{bmatrix}
    1 & 0 \\ 
    0 & -1 \\ 
\end{bmatrix}, 
\begin{bmatrix}
    0 & 1 \\ 
    -1 & 0 \\ 
\end{bmatrix}$

**Prewitt Operator**
$\begin{bmatrix}
    -1 & 0 & 1\\ 
    -1 & 0 & 1\\ 
    -1 & 0 & 1\\ 
\end{bmatrix}, 
\begin{bmatrix}
    1 & 1 & 1 \\ 
    0 & 0 & 0 \\ 
    -1 & -1 & -1 \\ 
\end{bmatrix}$

**Sobel Operator**
$\begin{bmatrix}
    -1 & 0 & 1\\ 
    -2 & 0 & 2\\ 
    -1 & 0 & 1\\ 
\end{bmatrix}, 
\begin{bmatrix}
    1 & 2 & 1 \\ 
    0 & 0 & 0 \\ 
    -1 & -2 & -1 \\ 
\end{bmatrix}$

**Laplacian Operator**
$\begin{bmatrix}
    0 & 1 & 0 \\ 
    1 & -4 & 1 \\ 
    0 & 1 & 0 \\ 
\end{bmatrix}$


#### Harris Detector
$\displaystyle f = \frac{\lambda_1\lambda_2}{\lambda_1 + \lambda_2}
= \frac{determinant(H)}{trace(H)} = \frac{ad - bc}{a  d} \\
\text{f is called corner response} $
1. Compute derivatives at each pixel
2. Compute covariance matrix $H$ in a Gaussian window around each pixel 
3. Compute corner response function $f$
4. Threshold $f$
5. Find local maxima of response function (nonmaximum suppression)

- Invariant to intensity shift
- Not invariant to intensity scaling
- Invariant to translation and rotation
- Not invariant to scaling
  - Find scale that gives local maximum of f
  - Instead of computing $f$ for larger and larger windows, we can implement using a fixed window size with an image pyramid

#### Blob Detector
- Laplacian is sensitive to noise
- Usually using Laplacian of Gaussian (LoG) filter
- Feature points are local maxima in both position and scale
<br>

- LoG can be approximated by Difference of two Gaussians (DoG)
- Computing DoG at different scales



### Description
#### SIFT Descriptor
**Orientation Normalization**
- Compute orientation histogram
- Select dominant orientation
- Normalize: rotate to fixed orientation 

**Lowe’s SIFT algorithm**
- Run DoG detector
  - Find maxima in location/scale space
  - Remove edge points
- Find dominate orientation
- For each (x,y,scale,orientation), create descriptor

**Other detectors and descriptors**
- HOG: Histogram of oriented gradients
- SURF: Speeded Up Robust Features 
- FAST (corner detector) 
- ORB: an efficient alternative to SIFT or SURF 
- Fast Retina Key- point (FREAK) 

### Matching
- Define distance function that compares two descriptors
- Test all the features in another image, find the one with min distance
- Simple approach: $||f1 - f2 ||$
- Can give small distances for ambiguous (incorrect) matches

**Ratio test**
- Ratio score = $||f_1 - f_2 || / || f_1 - f_2^{'} ||$
  - $f_2$ is best match to $f_1$ in $I_2$
  - $f_2^{'}$ is 2nd best match to $f_1$ in $I_2$
- Ambiguous matches have large ratio scores

**Mutual nearest neighbor**
- Find mutual nearest neighbors
- $f_2$ is the nearest neighbor of $f_1$ in $I_2$
- $f_1$ is the nearest neighbor of $f_2$ in $I_1$







## Image Warping
### Affine Transformation
- Affine Map = Linear Map + Translation

$\begin{pmatrix}x'\\y' \end{pmatrix}
= \begin{pmatrix}a & b \\ c & d \end{pmatrix}
\begin{pmatrix}x \\ y \end{pmatrix} + 
\begin{pmatrix}t_x \\ t_y \end{pmatrix} $
- Using homogeneous coordinates

$\begin{pmatrix}x'\\ y' \\ 1 \end{pmatrix}
= \begin{pmatrix}a &b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{pmatrix}
\begin{pmatrix}x \\ y \\ 1 \end{pmatrix} $

### Projective Transformation (Homography)
$\begin{pmatrix}x'\\ y' \\ 1 \end{pmatrix}
= \begin{pmatrix}h_{00} & h_{01} & h_{02} \\ h_{10} & h_{11} & h_{12} \\ h_{20} & h_{21} & h_{22} \end{pmatrix}
\begin{pmatrix}x \\ y \\ 1 \end{pmatrix} $


- Homography matrix is up to scale (can be multiplied by a scalar), which means the degree of freedom is 8
- We usually constrain the length of the vector $[h_{00}, h_{01}, …, h_{22}]$ to be 1
- Can generate any synthetic camera view as long as it has the same center of projection

### Implement
- **Forward Warping** : Send each pixel in $f(x, y)$ to its corresponding location in $g(x', y')$ by $(x', y') = T(x, y)$
- **Inverse Warping** : Get each pixel in $g(x', y')$ from its corresponding location in $f(x, y)$ by $(x, y) = T^{-1}(x', y')$
- **Interpolation** : including nearest neighbor, bilinear, bicubic, sinc, etc.





## Image Stitching
### Affine Transformation
$\begin{bmatrix}x'\\ y' \\ 1 \end{bmatrix}
= \begin{bmatrix}a &b & c \\ d & e & f \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix}x \\ y \\ 1 \end{bmatrix}
= \begin{bmatrix}ax+by+c \\ dx+ey+f \\ 1 \end{bmatrix} $

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

$\Rightarrow \bold{\underset{2n\times 6}{A}\; \underset{6\times 1}{t} = \underset{2n\times 1}{b}} $

- Least squares: find $\bold{t} $ that minimizes $\bold{||At - b||^2}$
- The solution is given by
$$
\bold{A^TAt = A^tb } \\
\bold{t = (A^TA)^{-1}A^tb } \\
$$

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

$\Rightarrow \bold{\underset{2n\times 9}{A}\; \underset{9\times 1}{h} = \underset{2n\times 1}{0}} $

- Least squares: find $\bold{h} $ that minimizes $\bold{||Ah - 0||^2}$
- Since $\bold{h}$ is defined up to scale, solve for unit vector $\hat{\bold{h}}$
- Solution: $\hat{\bold{h}}$ = eigenvector of $\bold{A^TA}$ with smallest eigenvalue

### RANSAC
1. Randomly choose ***s*** samples. Typically ***s*** = minimum sample size that lets you fit a model
1. Fit a model (e.g., transformation matrix) to those samples
2. Count the number of inliers that approximately fit the model
3. Repeat N times
4. Choose the model that has the largest set of inliers





