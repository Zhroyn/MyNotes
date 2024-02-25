
- [Depth Estimation](#depth-estimation)
    - [Stereo Matching](#stereo-matching)
        - [Stereo Image Rectification](#stereo-image-rectification)
        - [Stereo Matching Algorithms](#stereo-matching-algorithms)
            - [Window-based Stereo Matching](#window-based-stereo-matching)
            - [MRF-based Stereo Matching](#mrf-based-stereo-matching)
    - [Multi-View Stereo (MVS)](#multi-view-stereo-mvs)
        - [Plane-Sweep](#plane-sweep)
        - [Patch Match](#patch-match)
- [3D Reconstruction](#3d-reconstruction)
    - [3D Representations](#3d-representations)
    - [3D Surface Reconstruction](#3d-surface-reconstruction)
        - [Poisson Reconstruction](#poisson-reconstruction)
        - [Marching Cubes](#marching-cubes)








## Depth Estimation
### Stereo Matching
For a given stereo camera, suppose the relative pose of the two lenses is given, then the procedures to compute the depth are:
1. Find 2D-2D correspondences
2. Triangulate

So here comes stereo matching, which helps match all pixels efficiently.

<br>

#### Stereo Image Rectification
For every point, set $X_L$ and $X_R$.
Given $X_L$, then the equation of the epipolar line on the right image plane is
$$
X_L^T F X_R = 0 \\~\\
F = K_L^{{-1}^T} E K_R^{-1} = K_L^{{-1}^T} T_XR K_R^{-1} 
$$

When image planes of cameras are parallel to each other and to the baseline, 
$$
R = \begin{bmatrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 1 \\
\end{bmatrix}
$$

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

Let $D = x_2 - x_1$ be the disparity of pixel $(x_1, y_1)$, and $B$ to be the length of baseline, then we can get the depth $$z = f \cdot \frac{B}{D}$$

When these conditions are not satisfied, we can simply use two homographies to reproject the image planes onto a common plane parallel to the line between camera centers.

<br>

#### Stereo Matching Algorithms
##### Window-based Stereo Matching
We can find the match of a point on the scanline by locally search the point that minimizes the dissimilarity.

To get the dissimilarity between two points, we can calculate the matching scores from all pixels in the windows of the two points.

There are many kinds of matching scores, such as:
- SSD (Sum of Squared Differences): $$\sum_{x, y}|W_1(x,y) - W_2(x,y)|^2 $$
- SAD (Sum of Absolute Differences): $$\sum_{x, y}|W_1(x,y) - W_2(x,y)| $$
- ZNCC (Zero-mean Normalized Cross Correlation): $$ \frac{\sum_{x,y}(W_1(x, y) - \overline{W}_1)(W_2(x, y) - \overline{W}_2)}{\sigma_{W_1}\sigma_{W_2}} $$
  where $\displaystyle \overline{W}_i = \frac{1}{n}\sum_{x,y}W_i$, $\displaystyle \sigma_{W_i} = \sqrt{\frac{1}{n} \sum_{x,y}(W_i - \overline{W}_i)^2} $. This can reduce the influence of brightness.

For smaller window, there will be more detail, but also more noise.
For larger window, there will be less noise, but also less detail.

<br>

##### MRF-based Stereo Matching
Define the energy function as
$$E(d) = E_d(d) + \lambda E_s(d) $$

where $d$ is the disparity of each pixel.

The match cost is $E_d(d) = \sum_{(x,y)\in I} C(x, y, d(x, y)) $, where $C$ can be SSD, SAD, ZNCC, etc.
The smoothness cost is $E_s(d) = \sum_{(p,q)\in \epsilon} V(d_p, d_q) $, where $\epsilon$ is the set of neighboring pixels, $V$ can be $L_1$ distance $$V(d_p, d_q) = |d_p - d_q| $$

or "Potts model" 
$$
V(d_p, d_q) = \begin{cases}
0 & \text{if } d_p = d_q \\
1 & \text{if } d_p \neq d_q
\end{cases}
$$

<br>

Then we can get a better match by minimizing the global cost, i.e., performing discrete optimization on this energy function.








<br>

### Multi-View Stereo (MVS)
To get a proper depth value of a point from multiple reference images, the basic procedures are
1. Assume a depth value and get the 3D coordinates.
2. Project the coordinates to other cameras and compute the total error.
3. For each point in the reference image, compute the error for each depth value, and find the depth value that gives the smallest error.

<br>

#### Plane-Sweep
This method is to compute the errors of all pixels at all depths efficiently. Its steps are
1. Assume the same depth for all pixels in the reference image, then we can get sweep family of planes parallel to the reference camera image plane.
2. Project each plane to neighbors views via homography and compute errors, then we can get a cost volume which is a 3D array that stores the errors of all pixels at all depths.
3. Get depth map from the cost volume.

<br>

#### Patch Match
It's an efficient algorithm for solving correspondence problems. Its steps are
1. **Random Initialization**: Each pixel is given a random patch offset as initialization.
2. **Propagation**: Each pixels checks if the offsets from neighboring patches give a better matching patch. If so, adopt neighbor’s patch offset.
3. **Random Search**: Each pixels searches for better patch offsets within a concentric radius around the current offset. The search radius starts with the size of the image and is halved each time until it is 1.
4. Go to Step 2 until converge.











<br>

## 3D Reconstruction
### 3D Representations
The methods for 3D representation include
- Point Cloud
- Volume
    - Occupancy
    - Signed Distance
- Mesh

**Occupancy**
$$
V_{ijk} = \begin{cases}
  1 & \text{if occupied} \\
  0 & \text{if empty}
\end{cases}
$$

**Signed Distance**
- Signed Distance Function (**SDF**): The distance of a point to the shape boundary.
- Truncated Signed Distance Function (**TSDF**): Truncate SDF’s distance value to $[−1, 1]$.

<br>

### 3D Surface Reconstruction
The basic procedures are
1. Use depth maps to get occupancy or TSDF volume through Poisson reconstruction, KinectFusion, etc.
2. Use occupancy or TSDF volume to get mesh through Marching Cubes, etc.

#### Poisson Reconstruction
This method can convert depth maps into a 3D volume. Its steps are
1. Convert depth map to point cloud.
2. Compute normal vector for each point, and represent the oriented points by a vector field $\vec{V}$.
3. Represent surface by the indicator (occupancy) function $$\mathcal{X}(p) = \begin{cases} 1 & \text{if } p\in M \\ 0 & \text{if } p\notin M \end{cases} $$
   
   And then find the function $\mathcal{X}$ whose gradient best approximates $\vec{V}$ by minimizing $$\underset{\mathcal{X}}{\text{min}} ||\Delta \mathcal{X} - \vec{V}||$$
4. Solve this by Poisson equation.

<br>

#### Marching Cubes
This method can extract 3D surface (mesh) from volumetric
representation. Its steps are
1. For each grid cell with a sign change, create one vertex on each grid edge with a sign change, and store their indices as the sign configuration of the grid cell.
2. Connect vertices by triangles using the pre-computed look-up table and make sure that triangles do not intersect.




