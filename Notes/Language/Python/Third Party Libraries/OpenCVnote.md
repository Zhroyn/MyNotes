<!-- TOC -->

- [Display and Interaction](#display-and-interaction)
- [Image](#image)
  - [Attributes and Propeties](#attributes-and-propeties)
  - [Basic Operation](#basic-operation)
  - [Image Process](#image-process)
    - [Image Filtering](#image-filtering)
      - [Kernel and Operator](#kernel-and-operator)
      - [Smoothing](#smoothing)
    - [Geometric Transformation](#geometric-transformation)
      - [Resize](#resize)
      - [Flip](#flip)
      - [Affine](#affine)
      - [Perspective](#perspective)
      - [Remap](#remap)
    - [Miscellaneous Transformations](#miscellaneous-transformations)
      - [Thresholding Process](#thresholding-process)
      - [Color Space Conversions](#color-space-conversions)
  - [Image Matching](#image-matching)
    - [Detection and Description](#detection-and-description)
    - [Descriptor Matchers](#descriptor-matchers)
    - [Draw Keypoints and Matches](#draw-keypoints-and-matches)
- [Video](#video)
  - [VideoCapture](#videocapture)
  - [VideoWriter](#videowriter)
  - [fourcc](#fourcc)
- [Draw](#draw)
  - [Rectangle](#rectangle)
  - [Text](#text)

<!-- /TOC -->






# Display and Interaction
- `namedWindow(winname[, flags]) -> None`
  - If a window with the same name already exists, the function does nothing.
  - `flags` : By default is `cv2.WINDOW_AUTOSIZE` or `cv2.WINDOW_KEEPRATIO` or `cv2.WINDOW_GUI_EXPANDED`
    - `WINDOW_NORMAL` or `WINDOW_AUTOSIZE` : `WINDOW_NORMAL` enables you to resize the window, whereas `WINDOW_AUTOSIZE` adjusts automatically the window size to fit the displayed image and cannot change the window size.
    - `WINDOW_FREERATIO` or `WINDOW_KEEPRATIO` : `WINDOW_FREERATIO` adjusts the image with no respect to its ratio, whereas `WINDOW_KEEPRATIO` keeps the image ratio.
    - `WINDOW_GUI_NORMAL` or `WINDOW_GUI_EXPANDED` : `WINDOW_GUI_NORMAL` is the old way to draw the window without statusbar and toolbar, whereas `WINDOW_GUI_EXPANDED` is a new enhanced GUI.
- `destroyWindow(winname) -> None` Destroy the window with the given name.
- `destroyAllWindows() -> None` Destroy all of the opened HighGUI windows.
<br>

- `imshow(winname, mat) -> None`
  - If the window was not created before, it is assumed creating a window with `WINDOW_AUTOSIZE`.
  - Should be followed by a call to `waitKey()` or `pollKey()`. Otherwise, it won't display the image and the window might lock up.
- `waitKey([, delay]) -> retval`
  - Wait for a key event infinitely or for delay milliseconds if it is positive.
  - It returns the code of the pressed key or -1 if no key was pressed before the specified time had elapsed.








# Image
## Attributes and Propeties
**Image Propeties**
- `im.dtype` Image datatype
- `im.itemsize` Length of an element in bytes
- `im.nbytes` Number of bytes in memery, same as `im.itemsize * im.size`
- `im.ndim` Number of array dimensions, same as `len(im.shape)`
- `im.shape` A tuple of number of rows, columns, and channels (if image is color)
- `im.size` Total number of pixels, same as `im.shape[0] * im.shape[1]` or `im.shape[0] * im.shape[1] * im.shape[2]`

**ddepth**
- `CV_8U` = 0
- `CV_8S` = 1
- `CV_16U` = 2
- `CV_16S` = 3
- `CV_32S` = 4
- `CV_32F` = 5
- `CV_64F` = 6

**borderType**
- `BORDER_CONSTANT` : `iiiiii|abcdefgh|iiiiiii`
- `BORDER_REPLICATE` : `aaaaaa|abcdefgh|hhhhhhh`
- `BORDER_REFLECT` : `fedcba|abcdefgh|hgfedcb`
- `BORDER_WRAP` : `cdefgh|abcdefgh|abcdefg`
- `BORDER_REFLECT_101` : `gfedcb|abcdefgh|gfedcba`
- `BORDER_TRANSPARENT` : `uvwxyz|abcdefgh|ijklmno`
- `BORDER_REFLECT101` : same as `BORDER_REFLECT_101`
- `BORDER_DEFAULT` : same as `BORDER_REFLECT_101`


**interpolation**
- `INTER_NEAREST` nearest neighbor interpolation
- `INTER_LINEAR` bilinear interpolation
- `INTER_CUBIC` bicubic interpolation
- `INTER_AREA` resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire'-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
- `INTER_LANCZOS4` Lanczos interpolation over 8x8 neighborhood
- `INTER_LINEAR_EXACT` Bit exact bilinear interpolation
- `INTER_NEAREST_EXACT` Bit exact nearest neighbor interpolation. This will produce same results as the nearest neighbor method in PIL, scikit-image or Matlab.
- `INTER_MAX` mask for interpolation codes
- `WARP_FILL_OUTLIERS` flag, fills all of the destination image pixels. If some of them correspond to outliers in the source image, they are set to zero
- `WARP_INVERSE_MAP` flag, inverse transformation


## Basic Operation
- In RGB color space, the order of image channels is BGR.
- In pixel coordinates, the first index represents the row(height), the secend index represents the colunm(width).
- `+` `-` `*` `/` : The result will take the modulus. The operators can be two arrays or an array and a scalar.
- When used with `mask`, the operation will only be performed on pixels with non-zero mask value, and the value of other pixels will be set to 0.

**Load and Save**
- `imread(filename[, flags]) -> retval`
  - The function determines the type of image by content, not by file extension.
  - `flags` : The default value is `cv2.IMREAD_COLOR`.
    - `IMREAD_COLOR` : Load a color image. Any transparency of image will be neglected. Its value is 1.
    - `IMREAD_GRAYSCALE` : Load an image in grayscale mode. Its value is 0.
    - `IMREAD_UNCHANGED` : Load an image including alpha channel. Its value is -1.
- `imwrite(filename, img[, params]) -> retval`
  - Return true if image is saved successfully.
  - The image format is chosen based on the filename extension.

**Add and Subtract**
- `add(src1, src2[, dst[, mask[, dtype]]]) -> dst`
  - `src1` `src2` : If one of them is a scalar, then the scalar should be either a number or a tuple of four numbers. Saturation will be applied.
  - Saturation will be applied except when the output array has the depth `CV_32S`.
- `addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) -> dst`
  - `src1` `src2` : If one of them is a scalar, then the scalar should be either a number or a tuple of four numbers.
  - `gamma` : scalar added to each sum.
  - Saturation will be applied except when the output array has the depth `CV_32S`.
- `subtract(src1, src2[, dst[, mask[, dtype]]]) -> dst`
  - `src1` `src2` : If one of them is a scalar, then the scalar should be either a number or a tuple of four numbers. Saturation will be applied.
  - Saturation will be applied except when the output array has the depth `CV_32S`.

**Bit Operation**
- `bitwise_not(src[, dst[, mask]]) -> dst` Inverts every bit of an array.
- `bitwise_and(src1, src2[, dst[, mask]]) -> dst` Calculates the per-element bit-wise conjunction of two arrays or an array and a scalar.
- `bitwise_or(src1, src2[, dst[, mask]]) -> dst` Calculates the per-element bit-wise disjunction of two arrays or an array and a scalar.
- `bitwise_xor(src1, src2[, dst[, mask]]) -> dst` Calculates the per-element bit-wise "exclusive or" operation on two arrays or an array and a scalar.
  - `src1` `src2` : If one of them is a scalar, then the scalar should be either a number or a tuple, the number of which can be one or four or the number of channels.
  - In case of floating-point arrays, their machine-specific bit representations (usually IEEE754-compliant) are used for the operation.
  - If one of the src is scalar, the scalar is first converted to the array type.

**Split and Merge Channels**
- `split(m[, mv]) -> mv`
  - `m` : input multi-channel array.
- `merge(mv[, dst]) -> dst`
  - `mv` : input vector of matrices to be merged; all the matrices have the same size and the same depth.
- `b, g, r = cv2.split(im)`
- `out = cv2.merge([r, g, b])`




## Image Process
### Image Filtering
- `filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) -> dst` Convolve an image with the kernel.
  - In-place operation is supported.
  - `ddepth` : desired depth of the destination image.
  - `kernel` : convolution kernel (or rather a correlation kernel), a single-channel floating point matrix.
  - `anchor` : anchor of the kernel that indicates the relative position of a filtered point within the kernel; the anchor should lie within the kernel; default value (-1,-1) means at the kernel center.
  - `delta` : optional value added to the filtered pixels.
  - `cv2.filter2D(src, -1, kernel)`
  - `cv2.filter2D(src, -1, kernel, delta=5)`

#### Kernel and Operator
- `getGaussianKernel(ksize, sigma[, ktype]) ->	retval`
  - Return a $ksize\times 1$ matrix of Gaussian filter coefficients.
  - `ksize`	: Aperture size. It should be odd and positive.
  - `sigma`	: Gaussian standard deviation. If it is non-positive, it is computed from ksize as `sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8`.
  - `cv2.getGaussianKernel(ksize, 0) * cv2.getGaussianKernel(ksize, 0).T` Get 2-dimensional Gaussian kernel
<br>

- `Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst`
  - Calculates the first, second, third, or mixed image derivatives using an extended Sobel operator.
  - `ddepth` : output image depth; in the case of 8-bit input images it will result in truncated derivatives.
  - `dx` : order of the derivative x.
  - `dy` : order of the derivative y.
  - `ksize` : size of the extended Sobel kernel; it must be 1, 3, 5, or 7. Default is 3. When ksize = 1, the $3\times 1$ or $1\times 3$ kernel is used.
  - `scale` : optional scale factor for the computed derivative values; by default, no scaling is applied.
  - `delta` : optional delta value that is added to the results.
  - `cv2.Soble(src, -1, 1, 0)` use $\begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$
  - `cv2.Soble(src, -1, 0, 1)` use $\begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$


#### Smoothing
- `blur(src, ksize[, dst[, anchor[, borderType]]]) -> dst` Blur an image using the normalized box filter:
    $\displaystyle K = \frac{1}{width * height} 
    \begin{bmatrix} 
        1 & 1 & \cdots & 1 \\
        1 & 1 & \cdots & 1 \\
        \vdots & \vdots & \ddots & \vdots \\
        1 & 1 & \cdots & 1 \\ 
    \end{bmatrix}$
  - In-place filtering is supported.
  - `src` : it can have any number of channels, which are processed independently, but the depth should be `CV_8U`, `CV_16U`, `CV_16S`, `CV_32F` or `CV_64F`.
  - `ksize` : blurring kernel size which can be any size.
  - `anchor` : anchor point; default value (-1,-1) means at the kernel center.
  - `borderType` : border mode used to extrapolate pixels outside of image.
  - `cv2.blur(src, (3, 5))`
<br>

- `boxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]) -> dst` Blur an image using the box filter:
    $\displaystyle K = \alpha
    \begin{bmatrix} 
        1 & 1 & \cdots & 1 \\
        1 & 1 & \cdots & 1 \\
        \vdots & \vdots & \ddots & \vdots \\
        1 & 1 & \cdots & 1 \\ 
    \end{bmatrix}, 
    \alpha = \left\{ 
        \begin{aligned}
          &\frac{1}{width * height} &\text{when normalize=true} \\
          &1 &\text{otherwise} \\
        \end{aligned}
    \right. $
  - In-place filtering is supported.
  - `ddepth` : the output image depth (-1 to use `src.depth()`).
  - `ksize` : blurring kernel size which can be any size.
  - `anchor` : anchor point; default value (-1,-1) means at the kernel center.
  - `normalize` : Specifying whether the kernel is normalized, default is true.
  - `cv2.boxFilter(src, -1, (3, 5))`
  - `cv2.boxFilter(src, -1, (3, 5), normalize=False)`
<br>

- `GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst` Blur an image using a Gaussian filter.
  - In-place filtering is supported.
  - `src` : it can have any number of channels, which are processed independently, but the depth should be `CV_8U`, `CV_16U`, `CV_16S`, `CV_32F` or `CV_64F`.
  - `ksize` : Gaussian kernel size. Its width and height can differ but must be positive and odd. Or they can be zero's and then computed from sigma.
  - `sigmaX` : Gaussian kernel standard deviation in X direction.
  - `sigmaY` : Gaussian kernel standard deviation in Y direction; if sigmaY is zero, it is set to be equal to sigmaX, if both sigmas are zeros, they are computed from kernel's size.
  - `cv2.GaussianBlur(src, ksize, 0, 0)`
<br>

- `medianBlur(src, ksize[, dst]) -> dst` Blur an image using the median filter.
  - In-place operation is supported.
  - Use `BORDER_REPLICATE` internally for border pixels.
  - `src` : input 1-, 3-, or 4-channel image; when ksize is 3 or 5, the image depth should be `CV_8U`, `CV_16U`, or `CV_32F`, for larger aperture sizes, it can only be `CV_8U`.
  - `ksize` : aperture linear size; it must be odd and greater than 1.
<br>

- `bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) -> dst` Applies the bilateral filter to an image.
  - This filter does not work inplace.
  - `src` : Source 8-bit or floating-point, 1-channel or 3-channel image.
  - `d` : Diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from sigmaSpace.
  - `sigmaColor` : Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood will be mixed together.
  - `sigmaSpace` : Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other. When `d>0`, it specifies the neighborhood size regardless of `sigmaSpace`. Otherwise `d` is proportional to `sigmaSpace`.



### Geometric Transformation
#### Resize
- `resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) -> dst`
  - To shrink an image, it will generally look best with `cv2.INTER_AREA` interpolation
  - To enlarge an image, it will generally look best with `cv2.INTER_CUBIC` (slow) or `cv2.INTER_LINEAR` (default, faster but still looks OK).
  - `dsize` : output image size. The first parameter is width, and the second is height. If it is `None`, it will be computed from `fx` and `fy`
  - `fx` : scale factor along the horizontal axis.
  - `fy` : scale factor along the vertical axis.
  - `interpolation` : interpolation method.
  - `cv2.resize(src, (1920, 1080), interpolation=cv2.INTER_CUBIC)`
  - `cv2.resize(src, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)`

#### Flip
- `flip(src, flipCode[, dst]) -> dst` Flip a 2D array around vertical, horizontal, or both axes.
  - `flipCode` : a flag to specify how to flip the array.
    - 0 means flipping around the x-axis;
    - positive value means flipping around y-axis;
    - Negative value means flipping around both axes.
  - Here, x-axis is vertical.

#### Affine
- `warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) -> dst` Apply an affine transformation to an image.
    $\begin{aligned}
        \texttt{dst}(x,y) =  \texttt{src}( M_{11}x + M_{12}y + M_{13}, \\
                         M_{21}x + M_{22}y + M_{23} )
    \end{aligned}$
  - The function cannot operate in-place.
  - `M` : $2\times 3$ transformation matrix.
  - `dsize` : size of the output image.
  - `flags` : combination of interpolation methods and the optional flag `WARP_INVERSE_MAP` that means `M` is the inverse transformation.
  - `borderMode` : pixel extrapolation method; when it's `BORDER_TRANSPARENT`, it means that the pixels in the destination image corresponding to the "outliers" in the source image are not modified by the function.
  - `borderValue` : value used in case of a constant border; by default, it is 0.
<br>

- `getRotationMatrix2D(center, angle, scale) -> retval` Calculate an affine matrix of 2D rotation.
    $\alpha = scale \cdot \cos{\texttt{angle}} \\
    \beta =  scale \cdot \sin{\texttt{angle}} \\
    \begin{bmatrix}
        \alpha & \beta  & (1-\alpha) \cdot \texttt{center.x} - \beta \cdot \texttt{center.y} \\
        \beta  & \alpha & \beta \cdot \texttt{center.x} + (1-\alpha) \cdot \texttt{center.y} 
    \end{bmatrix}$
  - `center` : Center of the rotation in the source image. The coordinate origin is assumed to be the top-left corner.
  - `angle` : Rotation angle in degrees. Positive values mean counterclockwise rotation.
  - `scale` : Isotropic scale factor.
<br>

- `getAffineTransform(src, dst) -> retval` Calculate an affine transform from three pairs of the corresponding points.
  - `src` : $3\times 2$ matrix of coordinates of three points in the source image.
  - `dst` : $3\times 2$ matrix of coordinates of the corresponding points in the destination image.

#### Perspective
- `warpPerspective(src, M, dsize[,dst[, flags[, borderMode[, borderValue]]]]) -> dst` Apply an perspective transformation to an image.
    $\begin{aligned}
        \texttt{dst}(x,y) =  \texttt{src}( \frac{M_{11} x + M_{12} y + M_{13}}
                              {M_{31} x + M_{32} y + M_{33}} , \\
                         \frac{M_{21} x + M_{22} y + M_{23}}
                              {M_{31} x + M_{32} y + M_{33}} )
    \end{aligned}$
  - The function cannot operate in-place.
  - `M` : $3\times 3$ transformation matrix.
  - `dsize` : size of the output image.
<br>

- `getPerspectiveTransform(src, dst) -> retval` Calculate an perspective transform from four pairs of the corresponding points.
  - `src` : $4\times 2$ matrix of coordinates of three points in the source image.
  - `dst` : $4\times 2$ matrix of coordinates of the corresponding points in the destination image.

#### Remap
- `remap(src, map1, map2, interpolation[, dst[, borderMode[, borderValue]]]) -> dst` Apply a generic geometrical transformation to an image.
    $\texttt{dst}(x,y) = \texttt{src}(map_x(x,y), map_y(x,y))$,  where values of pixels with non-integer coordinates are computed using one of available interpolation methods.
  - This function cannot operate in-place.
  - `map1` : The first map of either (x,y) points or just x values having the type `CV_16SC2`, `CV_32FC1`, or `CV_32FC2`.
  - `map2` : The second map of y values having the type `CV_16UC1`, `CV_32FC1`, or none (empty map if map1 is (x,y) points), respectively.
  - `interpolation` : Interpolation method. The methods `INTER_AREA` and `INTER_LINEAR_EXACT` are not supported by this function.


### Miscellaneous Transformations
#### Thresholding Process
- `threshold(src, thresh, maxval, type[, dst]) ->	retval, dst`
  - Apply a fixed-level threshold to each array element.
  - `thresh` : threshold value.
  - `maxval` : maximum value to use with some thresholding types.
  - `type` : thresholding type.
<br>

- `THRESH_BINARY` : $\texttt{dst}(x,y) = \left\{ \begin{aligned} & \texttt{maxval} & \texttt{if src(x,y) > thresh} \\ & \texttt{0} & \texttt{otherwise} \end{aligned} \right.$
- `THRESH_BINARY_INV` : $\texttt{dst}(x,y) = \left\{ \begin{aligned} & \texttt{0} & \texttt{if src(x,y) > thresh} \\ & \texttt{maxval} & \texttt{otherwise} \end{aligned} \right.$
- `THRESH_TRUNC` : $\texttt{dst}(x,y) = \left\{ \begin{aligned} & \texttt{threshold} & \texttt{if src(x,y) > thresh} \\ & \texttt{src(x, y)} & \texttt{otherwise} \end{aligned} \right.$
- `THRESH_TOZERO` : $\texttt{dst}(x,y) = \left\{ \begin{aligned} & \texttt{src(x, y)} & \texttt{if src(x,y) > thresh} \\ & \texttt{0} & \texttt{otherwise} \end{aligned} \right.$
- `THRESH_TOZERO_INV` : $\texttt{dst}(x,y) = \left\{ \begin{aligned} & \texttt{0} & \texttt{if src(x,y) > thresh} \\ & \texttt{src(x, y)} & \texttt{otherwise} \end{aligned} \right.$

#### Color Space Conversions
- `cvtColor(src, code[, dst[, dstCn=0]]) -> dst`
  - Convert an image from one color space to another.
  - The conventional ranges for R, G, and B channel values are:
    - 0 to 255 for `CV_8U` images
    - 0 to 65535 for `CV_16U` images
    - 0 to 1 for `CV_32F` images
  - If conversion adds the alpha channel, its value will set to the maximum of corresponding channel range: 255 for `CV_8U`, 65535 for `CV_16U`, 1 for `CV_32F`.
  - `src`	: 8-bit unsigned, 16-bit unsigned, or single-precision floating-point.
  - `dst` : output image of the same size and depth as src.
  - `code` : color space conversion code
  - `dstCn` : number of channels in the destination image; if the parameter is 0, the number of the channels is derived automatically from src and code.

**code**
- `COLOR_BGR2BGRA` = 0
- `COLOR_RGB2RGBA` = `COLOR_BGR2BGRA`
- `COLOR_BGRA2BGR` = 1
- `COLOR_RGBA2RGB` = `COLOR_BGRA2BGR`
- `COLOR_BGR2RGBA` = 2
- `COLOR_RGB2BGRA` = `COLOR_BGR2RGBA`
- `COLOR_RGBA2BGR` = 3
- `COLOR_BGRA2RGB` = `COLOR_RGBA2BGR`
- `COLOR_BGR2RGB` = 4
- `COLOR_RGB2BGR` = `COLOR_BGR2RGB`
- `COLOR_BGRA2RGBA` = 5
- `COLOR_RGBA2BGRA` = `COLOR_BGRA2RGBA`
- `COLOR_BGR2GRAY` = 6
- `COLOR_RGB2GRAY` = 7
- `COLOR_GRAY2BGR` = 8
- `COLOR_GRAY2RGB` = `COLOR_GRAY2BGR`
- `COLOR_GRAY2BGRA` = 9
- `COLOR_GRAY2RGBA` = `COLOR_GRAY2BGRA`
- `COLOR_BGRA2GRAY` = 10
- `COLOR_RGBA2GRAY` = 11




## Image Matching
### Detection and Description
- `SIFT([, nfeatures[, nOctaveLayers[, contrastThreshold[, edgeThreshold[, sigma]]]]]) ->	retval`
- `SIFT(nfeatures, nOctaveLayers, contrastThreshold, edgeThreshold, sigma, descriptorType	 ->	retval`
  - Nearly the same as `SIFT_create()` and `SIFT.create()`.
  - `nfeatures` : The number of best features to retain. The features are ranked by their scores (measured in SIFT algorithm as the local contrast)
  - `nOctaveLayers` : The number of layers in each octave. 3 is the value used in D. Lowe paper. The number of octaves is computed automatically from the image resolution.
  - `contrastThreshold` : The contrast threshold used to filter out weak features in semi-uniform (low-contrast) regions. The larger the threshold, the less features are produced by the detector.
  - `edgeThreshold` : The threshold used to filter out edge-like features. Its meaning is different from the `contrastThreshold`, i.e. the larger the edgeThreshold, the less features are filtered out.
  - `sigma` : The sigma of the Gaussian applied to the input image at the octave 0. If your image is captured with a weak camera with soft lenses, you might want to reduce the number.
  - `descriptorType` : The type of descriptors. Only `CV_32F` and `CV_8U` are supported.
  - `sift = cv2.SIFT()`
<br>

- `detect(image[, mask]) -> keypoints`
- `detect(images[, masks]) -> keypoints`
  - Detect keypoints in an image (first variant) or image set (second variant).
  - `kpt = sift.detect(im)`
<br>

- `compute(image, keypoints[, descriptors]) -> keypoints, descriptors`
- `compute(images, keypoints[, descriptors]) -> keypoints, descriptors`
  - Compute the descriptors for a set of keypoints detected in an image (first variant) or image set (second variant).
  - `desc = sift.compute(im, kpt)`
<br>

- `detectAndCompute(image, mask[, descriptors[, useProvidedKeypoints]]) -> keypoints, descriptors`
  - Detect keypoints and compute the descriptors
  - `kpt, desc = sift.detectAndCompute(im, None)`

### Descriptor Matchers
- `BFMatcher([, normType=NORM=L2[, crossCheck=false]]) -> retval`
  - Nearly the same as `BFMatcher_create()` and `BFMatcher.create()`.
  - `normType` : One of `NORM_L1`, `NORM_L2`, `NORM_HAMMING`, `NORM_HAMMING2`.
    - `L1` and `L2` norms are preferable choices for SIFT and SURF descriptors.
    - `NORM_HAMMING` should be used with ORB, BRISK and BRIEF.
    - `NORM_HAMMING2` should be used with ORB when WTA_K==3 or 4.
  - `crossCheck` : If it is false, this is will be default BFMatcher behaviour when it finds the k nearest neighbors for each query descriptor. If it is true, then the `knnMatch()` method with k=1 will only return pairs (i,j).
  - `bf = cv2.BFMatcher()`
<br>

- `match(queryDescriptors, trainDescriptors[, mask]) -> matches`
  - `queryDescriptors` : Query set of descriptors.
  - `trainDescriptors` : Train set of descriptors.
  - `mask` : Mask specifying permissible matches between an input query and train matrices of descriptors.
  - `matches`:  Matches. If a query descriptor is masked out in mask , no match is added for this descriptor.
  - `matches = bf.match(desc1, desc2)`
<br>

- `knnMatch(queryDescriptors, trainDescriptors, k[, mask[, compactResult]]) -> matches`
  - Find the k best matches for each descriptor from a query set.
  - `k` : Count of best matches found per each query descriptor or less.
  - `matches` : Matches. Each `matches[i]` is k or less matches for the same query descriptor.
  - `matches = bf.knnMatch(desc1, desc2, 2)`

### Draw Keypoints and Matches
- `drawKeypoints(image, keypoints, outImage[, color[, flags]]) -> outImage`
  - `keypoints` : Keypoints from the source image.
  - `outImage` : Output image. Its content depends on the flags value defining what is drawn in the output image. See possible flags bit values below.
  - `color` : Color of keypoints.  If `color==Scalar::all(-1)`, the color is generated randomly.
  - `flags` : Flags setting drawing features.
  - `out = cv2.drawKeypoints(im, kpt, None)`
<br>

- `drawMatches(img1, keypoints1, img2, keypoints2, matches1to2, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]) -> outImg`
- `drawMatches(img1, keypoints1, img2, keypoints2, matches1to2, outImg, matchesThickness[, matchColor[, singlePointColor[, matchesMask[, flags]]]]) -> outImg`
- `drawMatchesKnn(img1, keypoints1, img2, keypoints2, matches1to2, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]) -> outImg`
  - Draw the found matches of keypoints from two images.
  - `matches1to2` : Matches from the first image to the second one, which means that `keypoints1[i]` has a corresponding point in `keypoints2[matches[i]]` .
  - `outImg` : Output image. Its content depends on the flags value defining what is drawn in the output image.
  - `matchColor` : Color of matches (lines and connected keypoints). If `matchColor==Scalar::all(-1)`, the color is generated randomly.
  - `singlePointColor` : Color of single keypoints (circles), which means that keypoints do not have the matches. If `singlePointColor==Scalar::all(-1)`, the color is generated randomly.
  - `matchesMask` : Mask determining which matches are drawn. If the mask is empty, all matches are drawn.
  - `flags` : Flags setting drawing features.
  - `out = cv2.drawMatches(img1, kpt1, img2, kpt2, matches, None)`



# Video
## VideoCapture
**Open and Release**
- `VideoCapture(filename[, apiPreference]) -> retval`
- `VideoCapture.open(filename[, apiPreference]) -> retval`
  - Open a video file or a capturing device or an IP video stream.
  - Passing 0 will open default camera using default backend.
  - Return true if the file has been successfully opened.
- `cap.isOpened() -> retval`
  - If the previous call to `cv2.VideoCapture()` or `cv2.VideoCapture.open()` succeeded, the method returns true.
- `cap.release() -> None`
  - Close video file or capturing device.

**Capture Frame**
- `cap.read([, image]) -> retval, image`
  - The video frame is returned in image. If no frames has been grabbed the image will be empty.
  - Return false if no frames has been grabbed
<br>

- `cap.grab() -> retval`
  - The method/function grabs the next frame from video file or camera.
  - Return true (non-zero) in the case of success.
- `cap.retrieve([, image[, flag]]) -> retval, image`
  - The method decodes and returns the just grabbed frame.
  - If no frames has been grabbed, the method returns false and the function returns an empty image.

**Get and Set Properties**
- `cap.get(propId) -> retval` Return the specified VideoCapture property.
- `cap.set(propId, value) -> retval` Set a property in the VideoCapture.
<br>

- Position
  - `CAP_PROP_POS_MSEC` Current position of the video file in milliseconds.
  - `CAP_PROP_POS_FRAMES` 0-based index of the frame to be decoded/captured next.
  - `CAP_PROP_POS_AVI_RATIO` Relative position of the video file: 0=start of the film, 1=end of the film.
- Frame
  - `CAP_PROP_FRAME_WIDTH` Width of the frames in the video stream.
  - `CAP_PROP_FRAME_HEIGHT` Height of the frames in the video stream.
  - `CAP_PROP_FRAME_COUNT` Number of frames in the video file.
- `CAP_PROP_FPS` Frame rate.
- `CAP_PROP_FOURCC` 4-character code of codec.
- `CAP_PROP_FORMAT` Format of the Mat objects returned by `VideoCapture.retrieve()`. Set value -1 to fetch undecoded RAW video streams (as Mat 8UC1).






## VideoWriter
**Create and Release**
- `VideoWriter(filename, fourcc, fps, frameSize, isColor=ture) -> retval`
- `VideoWriter.open(filename, fourcc, fps, frameSize, isColor=ture) -> retval`
  - Initializes or reinitializes video writer.
  - Return `true` if video writer has been successfully initialized
  - `fourcc` : 4-character code of codec used to compress the frames. If fourcc is -1, it will pop up the codec selection dialog.
    - `cv2.VideoWriter_fourcc(*"mp4v")` for `.mp4` video.
    - `cv2.VideoWriter_fourcc(*"XVID"/"AVI1")` for `.avi` video.
    - `cv2.VideoWriter_fourcc(*"I420")` for `.avi` raw video.
  - `fps`	: Framerate of the created video stream.
  - `frameSize` : Size of the video frames.
  - `isColor` : If it is not zero, the encoder will expect and encode color frames, otherwise it will work with grayscale frames.
<br>

- `isOpened() -> retval` Return true if video writer has been successfully initialized.
- `release() -> None` Close the video writer.

**Add Frame**
- `write(image) ->	None` Writes the next video frame.
    image : In general, color images are expected in BGR format.
            It must have the same size as has been specified when opening the 
            video writer.


## fourcc
**AVI**
- `I420`
  - `rawvideo (I420 / 0x30323449)`
  - YUV video stored in planar 4:2:0 format
  - largest
- `H264` `h264` `X264` `x264` `avc1`
  - `h264 (Constrained Baseline) (H264 / 0x34363248)`
  - H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10
  - larger
- `MJPG` `AVI1` `AVI2`
  - `mjpeg (Baseline) (MJPG / 0x47504A4D)`
  - Motion JPEG
  - smaller
- `FMP4` `XVID` `DIVD`
  - `mpeg4 (Simple Profile) (FMP4 / 0x34504D46)`
  - MPEG-4 part 2
  - smallest

**MP4**
- `avc1` `avc3`
  - `h264 (Constrained Baseline) (avc1 / 0x31637661)`
  - H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10
  - larger
- `mp4v`
  - `mpeg4 (Simple Profile) (mp4v / 0x7634706D)`
  - MPEG-4 part 2
  - smaller






# Draw
## Rectangle
- `rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img`
  - `pt1` : Vertex of the rectangle.
  - `pt2` : Vertex of the rectangle opposite to pt1 .
  - `color` : Rectangle color or brightness (grayscale image).
  - `thickness` : Thickness of lines that make up the rectangle. Negative values mean that the function has to draw a filled rectangle.
  - `lineType` : Type of the line.
  - `shift` : Number of fractional bits in the point coordinates.

## Text
- `putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img`
  - `org` : Bottom-left corner of the text string in the image.
  - `fontFace` : Font type.
  - `fontScale` : Font scale factor that is multiplied by the font-specific base size.
  - `color` : Text color in BGR orger.
  - `thickness` : Thickness of the lines used to draw a text.
  - `lineType` : Line type.
  - `bottomLeftOrigin` : When true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.

**fontFace**
- `cv2.FONT_HERSHEY_SIMPLEX` normal size sans-serif font
- `cv2.FONT_HERSHEY_PLAIN` small size sans-serif font
- `cv2.FONT_HERSHEY_DUPLEX` normal size sans-serif font (more complex than FONT_HERSHEY_SIMPLEX)
- `cv2.FONT_HERSHEY_COMPLEX` normal size serif font
- `cv2.FONT_HERSHEY_TRIPLEX` normal size serif font (more complex than FONT_HERSHEY_COMPLEX)
- `cv2.FONT_HERSHEY_COMPLEX_SMALL` smaller version of FONT_HERSHEY_COMPLEX
- `cv2.FONT_HERSHEY_SCRIPT_SIMPLEX` hand-writing style font
- `cv2.FONT_HERSHEY_SCRIPT_COMPLEX` more complex variant of FONT_HERSHEY_SCRIPT_SIMPLEX
- `cv2.FONT_ITALIC` flag for italic font










