
## Image Warping
### Affine Transformation
- Affine Map = Linear Map + Translation

$$
\begin{pmatrix}x'\\y' \end{pmatrix}
= \begin{pmatrix}a & b \\ c & d \end{pmatrix}
\begin{pmatrix}x \\ y \end{pmatrix} + 
\begin{pmatrix}t_x \\ t_y \end{pmatrix}
$$

- Using homogeneous coordinates

$$
\begin{pmatrix}x'\\ y' \\ 1 \end{pmatrix}
= \begin{pmatrix}a &b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{pmatrix}
\begin{pmatrix}x \\ y \\ 1 \end{pmatrix} 
$$

### Projective Transformation (Homography)
$$
\begin{pmatrix}x'\\ y' \\ 1 \end{pmatrix}
= \begin{pmatrix}
  h_{00} & h_{01} & h_{02} \\
  h_{10} & h_{11} & h_{12} \\
  h_{20} & h_{21} & h_{22}
\end{pmatrix}
\begin{pmatrix}x \\ y \\ 1 \end{pmatrix}
$$


- Homography matrix is up to scale (can be multiplied by a scalar), which means the degree of freedom is 8
- We usually constrain the length of the vector $[h_{00}, h_{01}, …, h_{22}]$ to be 1
- Can generate any synthetic camera view as long as it has the same center of projection

### Implement
- **Forward Warping** : Send each pixel in $f(x, y)$ to its corresponding location in $g(x', y')$ by $(x', y') = T(x, y)$
- **Inverse Warping** : Get each pixel in $g(x', y')$ from its corresponding location in $f(x, y)$ by $(x, y) = T^{-1}(x', y')$
- **Interpolation** : including nearest neighbor, bilinear, bicubic, sinc, etc.

