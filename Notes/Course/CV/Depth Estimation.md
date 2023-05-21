<!-- TOC -->

- [Depth Estimation](#depth-estimation)
  - [Stereo Matching](#stereo-matching)

<!-- /TOC -->





## Depth Estimation
### Stereo Matching
For a given stereo camera, suppose the relative pose of the two lenses is given, then the procedure to compute the depth are:
1. Find 2D-2D correspondences
2. Triangulate

So here comes stereo matching, which helps match all pixels efficiently

For every point, set $X, X_L$ and $X_R$.
Given $X_L$, then we can get the equation of the epipolar line on the right image plane: 
$$
X_L^T F X_R = 0 \\~\\
F = K_L^{{-1}^T} E K_R^{-1} = K_L^{{-1}^T} T_XR K_R^{-1} 
$$

When image planes of cameras are parallel to each other and to the baseline, $$R = E$$

When camera centers are at same height, 
$$
T_X = \begin{bmatrix}
  0 & 0 & 0 \\
  0 & 0 & -t_x \\
  0 & t_x & 0 \\
\end{bmatrix}
$$

When focal lengths are the same, 
$$
K_L^{{-1}} = K_R^{-1} = \begin{bmatrix}
  f_x^{-1} & 0 & -f_x^{-1}o_x \\
  0 & f_y^{-1} & -f_y^{-1}o_y \\
  0 & 0 & 1 \\
\end{bmatrix}
$$

Then we can get 
$$
F = \begin{bmatrix}
  0 & 0 & 0 \\
  0 & 0 & -f_y^{-1}t_x \\
  0 & f_y^{-1}t_x & 0 \\
\end{bmatrix}
$$

Therefore, epipolar lines fall along the horizontal scan lines of the images at this time.