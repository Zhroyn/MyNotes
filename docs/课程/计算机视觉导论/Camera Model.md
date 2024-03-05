
### Camera Model
#### World-to-Camera Transformation
Suppose the position of camera in the world is $c_w$, and its orientation is 
$$R = 
\begin{bmatrix} \hat{x_c} \\ \hat{y_c} \\ \hat{z_c} \end{bmatrix} 
= \begin{bmatrix}
  r_{11} & r_{12} & r_{13} \\ 
  r_{21} & r_{22} & r_{23} \\ 
  r_{31} & r_{32} & r_{33} \\ 
\end{bmatrix}
$$

Then the coordinate of a position in the camera coordinate system is
$$
\bm{x}_c = R(\bm{x}_w - \bm{c}_w) = R\bm{x}_w - R\bm{c}_w = R\bm{x}_w + \bm{t} \\~\\
\bm{t} = -R\bm{c}_w = \begin{bmatrix} t_x \\ t_y \\ t_z \end{bmatrix}
$$

The whole equation can be expressed by a **extrinsic matrix**
$$
\tilde{\bm{x}}_c = 
\begin{bmatrix} x_c \\ y_c \\ z_c \\ 1 \end{bmatrix}
= \begin{bmatrix}
  r_{11} & r_{12} & r_{13} & t_x \\ 
  r_{21} & r_{22} & r_{23} & t_y \\ 
  r_{31} & r_{32} & r_{33} & t_z \\ 
  0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} x_w \\ y_w \\ z_w \\ 1 \end{bmatrix}
= M_{ext}\tilde{\bm{x}}_w
$$






<br>

#### Perspective Projection
We can transform the 3D-coordinate into 2D-coordinate by perspective projection
$$
\bm{x}_i = f \cdot \begin{bmatrix} x_c/z_c \\ y_c/z_c \\ 1 \end{bmatrix}
$$

Let $m_x, m_y$ be the pixel densities (pixels/mm) in x and y directions, and $(c_x, c_y)$ be the principle point where the optical axis pierces the sensor, then the final 2D-coordinate is:
$$
\bm{u} = \begin{bmatrix} u \\ v \end{bmatrix} = \begin{bmatrix} m_xf\frac{x_c}{z_c} + c_x \\ m_yf\frac{y_c}{z_c} + c_y \end{bmatrix}
$$

Let $f_x = m_xf$, $f_y = m_yf $, then the equation can be expressed in the form of homogenous coordinates by a **intrinsic matrix**
$$
\bm{\tilde{u}}
= \begin{bmatrix} \tilde{u} \\ \tilde{v} \\ 1 \end{bmatrix}
\equiv \begin{bmatrix}
  f_x & 0 & c_x & 0 \\ 
  0 & f_y & c_y & 0 \\ 
  0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix} x_c \\ y_c \\ z_c \\ 1 \end{bmatrix}
= M_{int}\tilde{\bm{x}}_c
$$

Finally, we can get a **projection matrix**
$$
\bm{\tilde{u}} \equiv M_{int}M_{ext}\bm{\tilde{x}_w} = P_{3\times 4}\bm{\tilde{x}_w}
$$







<br>

#### Pixel-to-World Transformation
Suppose the width of an image is $H$, the horizon field of view of the camera is $\theta$, the coordinates of a point on the corner of the image is $(x_0, y_0, z_0)$, then we have:
$$
f_x \frac{x_0}{z_0} = \frac{1}{2}W \\~\\
\Rightarrow \tan \frac{\theta}{2} = \frac{W}{2f_x},
\quad f_x = \frac{W}{2\tan(\theta/2)}
$$

After we get the focal length, we have:
$$
\hat{\bm{x}}_c =
\begin{bmatrix} x_c \\ y_c \\ 1 \end{bmatrix}
= \begin{bmatrix}
  1/f_x & 0 & - c_x/f_x \\ 
  0 & 1/f_y & - c_y/f_y \\ 
  0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = M_F^{-1}\tilde{\bm{u}}
$$

Then we can get the direction of the ray in the world coordinate system:
$$
\tilde{\bm{x}}_c = \begin{bmatrix} x_c \\ y_c \\ 1 \\ 1 \end{bmatrix},
\quad \tilde{\bm{x}}_w = M_{ext}^{-1} \tilde{\bm{x}}_c = \begin{bmatrix} x_w \\ y_w \\ z_w \\ 1 \end{bmatrix} \\~\\
\bm{d} = \frac{\bm{x}_w - \mathbf{o}}{\left\| \bm{x}_w - \mathbf{o} \right\|}
$$

Finally, we have the equation of the ray in the world coordinate system: $$\bm{x} = \mathbf{o} + t\mathbf{d}$$


