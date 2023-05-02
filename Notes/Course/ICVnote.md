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
- [Structure from Motion](#structure-from-motion)
  - [Camera Model](#camera-model)
  - [Camera Calibration](#camera-calibration)
    - [Direct Linear Transform (DLT)](#direct-linear-transform-dlt)
  - [Structure from Motion](#structure-from-motion-1)

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








## Structure from Motion
### Camera Model
**World-to-Camera Transformation**

Position : $c_w$
Orientation : $R = 
\begin{bmatrix} \hat{x_c} \\ \hat{y_c} \\ \hat{z_c} \end{bmatrix} 
= \begin{bmatrix}
  r_{11} & r_{12} & r_{13} \\ 
  r_{21} & r_{22} & r_{23} \\ 
  r_{31} & r_{32} & r_{33} \\ 
\end{bmatrix} $

$\bm{x_c} = R(\bm{x_w - c_w}) = R\bm{x_w} - R\bm{c_w} = R\bm{x_w} + \bm{t}, \bm{t} = -R\bm{c_w} $

Extrinsic Matrix : $\bm{x_c} = 
\begin{bmatrix} x_c \\ y_c \\ z_c \\ 1 \end{bmatrix}
= \begin{bmatrix}
  r_{11} & r_{12} & r_{13} & t_x \\ 
  r_{21} & r_{22} & r_{23} & t_y \\ 
  r_{31} & r_{32} & r_{33} & t_z \\ 
  0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} x_w \\ y_w \\ z_w \\ 1 \end{bmatrix} $


**Perspective Projection**

$$\bm{x_c} = \begin{bmatrix} x_c \\ y_c \\ z_c \end{bmatrix} \\~\\
\Rightarrow \bm{x_i} = \bm{f} \cdot \begin{bmatrix} x_c/z_c \\ y_c/z_c \\ 1 \end{bmatrix} $$


**Image Plane to Image Sensor Mapping**

If $m_x$ and $m_y$ are the pixel densities (pixels/mm) in x and y directions, and pixel $(c_x, c_y)$ is the Principle Point where the optical axis pierces the sensor, then pixel coordinates are:
$$\displaystyle u = m_xf\frac{x_c}{z_c} + c_x, \displaystyle v = m_yf\frac{y_c}{z_c} + c_y $$

If $f_x = m_xf$, $f_y = m_yf $, then in homogenous coordinates:
$$
\begin{bmatrix} u \\ v \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
  f_x & 0 & c_x \\ 
  0 & f_y & c_y \\ 
  0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} x_c \\ y_c \\ z_c \end{bmatrix}
$$

Intrinsic Matrix : $\bm{\tilde{u}_c} = 
\begin{bmatrix} \tilde{u} \\ \tilde{v} \\ \tilde{w} \end{bmatrix}
= \begin{bmatrix}
  f_x & 0 & c_x & 0 \\ 
  0 & f_y & c_y & 0 \\ 
  0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix} x_c \\ y_c \\ z_c \\ 1 \end{bmatrix} $

**Projection Matrix**
$$
\bm{\tilde{u}} = M_{int}\bm{\tilde{x}_c} \\~\\
\bm{\tilde{x}_c} = M_{ext}\bm{\tilde{x}_w} \\~\\
\bm{\tilde{u}} = M_{int}M_{ext}\bm{\tilde{x}_w} = P_{3\times 4}\bm{\tilde{x}_w} \\~\\
$$


### Camera Calibration
#### Direct Linear Transform (DLT)
The relation between the coordinates in world coordinate and camera coordinate:
$$
\begin{bmatrix} u^{(i)} \\ v^{(i)} \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
   p_{11} & p_{12} & p_{13} & p_{14} \\ 
   p_{21} & p_{22} & p_{23} & p_{24} \\ 
   p_{31} & p_{32} & p_{33} & p_{34} \\ 
\end{bmatrix}
\begin{bmatrix} x_w^{(i)} \\ y_w^{(i)} \\ z_w^{(i)} \\ 1 \end{bmatrix}
$$ That is:
$$
\displaystyle u^{(i)} = \frac{p_{11}x_w^{(i)} + p_{12}y_w^{(i)} + p_{13}z_w^{(i)} + p_{14}}{p_{31}x_w^{(i)} + p_{32}y_w^{(i)} + p_{33}z_w^{(i)} + p_{34}}
\\~\\
\displaystyle v^{(i)} = \frac{p_{21}x_w^{(i)} + p_{22}y_w^{(i)} + p_{23}z_w^{(i)} + p_{24}}{p_{31}x_w^{(i)} + p_{32}y_w^{(i)} + p_{33}z_w^{(i)} + p_{34}}
$$ Rerange the equations, we can get:
$$
\begin{bmatrix}
  x_w^{(1)} & y_w^{(1)} & z_w^{(1)} & 1 & 0 & 0 & 0 & 0 & -u_1x_w^{(1)} & -u_1y_w^{(1)} & -u_1z_w^{(1)} & -u_1 \\
  0 & 0 & 0 & 0 & x_w^{(1)} & y_w^{(1)} & z_w^{(1)} & 1 & -u_1x_w^{(1)} & -u_1y_w^{(1)} & -u_1z_w^{(1)} & -u_1 \\
  \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \\
  x_w^{(i)} & y_w^{(i)} & z_w^{(i)} & 1 & 0 & 0 & 0 & 0 & -u_ix_w^{(i)} & -u_1y_w^{(i)} & -u_1z_w^{(i)} & -u_i \\
  0 & 0 & 0 & 0 & x_w^{(i)} & y_w^{(i)} & z_w^{(i)} & 1 & -u_ix_w^{(i)} & -u_iy_w^{(i)} & -u_iz_w^{(i)} & -u_i \\
  \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \\
  x_w^{(n)} & y_w^{(n)} & z_w^{(n)} & 1 & 0 & 0 & 0 & 0 & -u_nx_w^{(n)} & -u_1y_w^{(n)} & -u_1z_w^{(n)} & -u_n \\
  0 & 0 & 0 & 0 & x_w^{(n)} & y_w^{(n)} & z_w^{(n)} & 1 & -u_nx_w^{(n)} & -u_ny_w^{(n)} & -u_nz_w^{(n)} & -u_n \\
\end{bmatrix}
\begin{bmatrix}
   p_{11} \\ p_{12} \\ p_{13} \\ p_{14} \\ 
   p_{21} \\ p_{22} \\ p_{23} \\ p_{24} \\ 
   p_{31} \\ p_{32} \\ p_{33} \\ p_{34} \\
\end{bmatrix} = \bm{0} \\
\Rightarrow A\bm{p} = \bm{0}
$$

Projection matrix is up to scale, we can use $p_{34}=1$ or $||\bm{p}||^2 = 1$ as constraint condition.
So the solution can become: 
$$\underset{p}{\text{min}}||A\bm{p}||^2 \text{ such that } ||\bm{p}||^2 = 1 $$ It can be proven that eigenvector $\bm{p}$ with smallest eigenvalue $\lambda$ of matrix $A^TA$ is the solution.

Then, to decompose projection matrices to intrinsic and extrinsic matrices, we can use QR factorization:
$$
\begin{bmatrix}
  p_{11} & p_{12} & p_{13} & p_{14} \\
  p_{21} & p_{22} & p_{23} & p_{24} \\
  p_{31} & p_{32} & p_{33} & p_{34} \\
\end{bmatrix}
= \begin{bmatrix}
  f_x & 0 & o_x & 0 \\
  0 & f_y & o_y & 0 \\
  0 & 0 & 1 & 0 \\
\end{bmatrix}
\begin{bmatrix}
  r_{11} & r_{12} & r_{13} & t_{x} \\
  r_{21} & r_{22} & r_{23} & t_{y} \\
  r_{31} & r_{32} & r_{33} & t_{z} \\
  0 & 0 & 0 & 1 \\
\end{bmatrix}
\\~\\
\begin{bmatrix}
  p_{11} & p_{12} & p_{13} \\
  p_{21} & p_{22} & p_{23} \\
  p_{31} & p_{32} & p_{33} \\
\end{bmatrix}
= \begin{bmatrix}
  f_x & 0 & o_x \\
  0 & f_y & o_y \\
  0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
  r_{11} & r_{12} & r_{13} \\
  r_{21} & r_{22} & r_{23} \\
  r_{31} & r_{32} & r_{33} \\
\end{bmatrix}
= KR
\\~\\
\bm{t} = \begin{bmatrix} t_{x} \\ t_{y} \\ t_{z} \end{bmatrix}
= K^{-1} \begin{bmatrix} p_{14} \\ p_{24} \\ p_{34} \end{bmatrix} 
$$



### Structure from Motion




