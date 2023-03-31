<!-- TOC -->

- [Display and Interaction](#display-and-interaction)
- [Image](#image)
  - [Attributes](#attributes)
  - [Basic Operation](#basic-operation)
  - [Image Process](#image-process)
    - [Smoothing](#smoothing)
    - [Geometric Transformation](#geometric-transformation)
- [Video](#video)
  - [VideoCapture](#videocapture)
    - [Open and Release](#open-and-release)
    - [Capture frame](#capture-frame)
    - [VideoCaptureProperties](#videocaptureproperties)
  - [VideoWriter](#videowriter)
    - [Create and Release](#create-and-release)
    - [fourcc](#fourcc)
- [Draw](#draw)
  - [Rectangle](#rectangle)
  - [Text](#text)
- [Shorthand](#shorthand)

<!-- /TOC -->






## Display and Interaction
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








## Image
### Attributes
```py
im.dtype
im.itemsize
im.nbytes
im.ndim
im.shape
im.size
```

**borderType**
- `cv2.BORDER_CONSTANT` : `iiiiii|abcdefgh|iiiiiii`
- `cv2.BORDER_REPLICATE` : `aaaaaa|abcdefgh|hhhhhhh`
- `cv2.BORDER_REFLECT` : `fedcba|abcdefgh|hgfedcb`
- `cv2.BORDER_WRAP` : `cdefgh|abcdefgh|abcdefg`
- `cv2.BORDER_REFLECT_101` : `gfedcb|abcdefgh|gfedcba`
- `cv2.BORDER_TRANSPARENT` : `uvwxyz|abcdefgh|ijklmno`
- `cv2.BORDER_REFLECT101` : same as `BORDER_REFLECT_101`
- `cv2.BORDER_DEFAULT` : same as `BORDER_REFLECT_101`


**interpolation**
- `cv2.INTER_NEAREST` nearest neighbor interpolation
- `cv2.INTER_LINEAR` bilinear interpolation
- `cv2.INTER_CUBIC` bicubic interpolation
- `cv2.INTER_AREA` resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire'-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
- `cv2.INTER_LANCZOS4` Lanczos interpolation over 8x8 neighborhood
- `cv2.INTER_LINEAR_EXACT` Bit exact bilinear interpolation
- `cv2.INTER_NEAREST_EXACT` Bit exact nearest neighbor interpolation. This will produce same results as the nearest neighbor method in PIL, scikit-image or Matlab.
- `cv2.INTER_MAX` mask for interpolation codes
- `cv2.WARP_FILL_OUTLIERS` flag, fills all of the destination image pixels. If some of them correspond to outliers in the source image, they are set to zero
- `cv2.WARP_INVERSE_MAP` flag, inverse transformation


### Basic Operation
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




### Image Process
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
<br>

- `filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) -> dst` Convolve an image with the kernel.
  - In-place operation is supported.
  - `ddepth` : desired depth of the destination image.
  - `kernel` : convolution kernel (or rather a correlation kernel), a single-channel floating point matrix.
  - `anchor` : anchor of the kernel that indicates the relative position of a filtered point within the kernel; the anchor should lie within the kernel; default value (-1,-1) means at the kernel center.
  - `delta` : optional value added to the filtered pixels.
  - `cv2.filter2D(src, -1, kernel)`
  - `cv2.filter2D(src, -1, kernel, delta=5)`


#### Geometric Transformation
**Resize**
- `resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) -> dst`
  - To shrink an image, it will generally look best with `cv2.INTER_AREA` interpolation
  - To enlarge an image, it will generally look best with `cv2.INTER_CUBIC` (slow) or `cv2.INTER_LINEAR` (default, faster but still looks OK).
  - `dsize` : output image size. The first parameter is width, and the second is height. If it is `None`, it will be computed from `fx` and `fy`
  - `fx` : scale factor along the horizontal axis.
  - `fy` : scale factor along the vertical axis.
  - `interpolation` : interpolation method.
  - `cv2.resize(src, (1920, 1080), interpolation=cv2.INTER_CUBIC)`
  - `cv2.resize(src, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)`

**Flip**
- `flip(src, flipCode[, dst]) -> dst` Flip a 2D array around vertical, horizontal, or both axes.
  - `flipCode` : a flag to specify how to flip the array.
    - 0 means flipping around the x-axis;
    - positive value means flipping around y-axis;
    - Negative value means flipping around both axes.
  - Here, x-axis is vertical.

**Affine**
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

**Perspective**
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

**Remap**
- `remap(src, map1, map2, interpolation[, dst[, borderMode[, borderValue]]]) -> dst` Apply a generic geometrical transformation to an image.
    $\texttt{dst}(x,y) = \texttt{src}(map_x(x,y), map_y(x,y))$,  where values of pixels with non-integer coordinates are computed using one of available interpolation methods.
  - This function cannot operate in-place.
  - `map1` : The first map of either (x,y) points or just x values having the type `CV_16SC2`, `CV_32FC1`, or `CV_32FC2`.
  - `map2` : The second map of y values having the type `CV_16UC1`, `CV_32FC1`, or none (empty map if map1 is (x,y) points), respectively.
  - `interpolation` : Interpolation method. The methods `INTER_AREA` and `INTER_LINEAR_EXACT` are not supported by this function.









## Video
### VideoCapture
#### Open and Release
```py
VideoCapture(filename[, apiPreference]) -> retval
open(filename[, apiPreference]) -> retval
    Opens a video file or a capturing device or an IP video stream for video 
    capturing.
    Parameters are same as the constructor VideoCapture.
    Return `true` if the file has been successfully opened.

isOpened() -> retval
    If the previous call to VideoCapture constructor or VideoCapture::open() 
    succeeded, the method returns true.

release() -> None
    Close video file or capturing device.
    The method is automatically called by subsequent VideoCapture::open and 
    by VideoCapture destructor.
```

#### Capture frame
```py
read([, image]) -> retval, image
    The video frame is returned in image.
    If no frames has been grabbed the image will be empty.
    Return false if no frames has been grabbed

grab() -> retval
    The method/function grabs the next frame from video file or camera and 
    returns true (non-zero) in the case of success.

retrieve([, image[, flag]]) -> retval, image
    The method decodes and returns the just grabbed frame. If no frames has 
    been grabbed, the method returns false and the function returns an empty 
    image.
    [out] image : the video frame is returned here. If no frames has been 
    grabbed the image will be empty.
    flag : it could be a frame index or a driver specific flag
```

#### VideoCaptureProperties
```py
get(propId) -> retval
    Return the specified VideoCapture property.

set(propId, value) -> retval
    Set a property in the VideoCapture.
```
- `cv.CAP_PROP_POS_MSEC` Current position of the video file in milliseconds.
- `cv.CAP_PROP_POS_FRAMES` 0-based index of the frame to be decoded/captured next.
- `cv.CAP_PROP_POS_AVI_RATIO` Relative position of the video file: 0=start of the film, 1=end of the film.
- `cv.CAP_PROP_FRAME_WIDTH` Width of the frames in the video stream.
- `cv.CAP_PROP_FRAME_HEIGHT` Height of the frames in the video stream.
- `cv.CAP_PROP_FPS` Frame rate.
- `cv.CAP_PROP_FOURCC` 4-character code of codec.
- `cv.CAP_PROP_FRAME_COUNT` Number of frames in the video file.
- `cv.CAP_PROP_FORMAT` Format of the Mat objects returned by VideoCapture::retrieve(). Set value -1 to fetch undecoded RAW video streams (as Mat 8UC1).
- `cv.CAP_PROP_MODE` Backend-specific value indicating the current capture mode.
- `cv.CAP_PROP_BRIGHTNESS` Brightness of the image (only for those cameras that support).
- `cv.CAP_PROP_CONTRAST` Contrast of the image (only for cameras).
- `cv.CAP_PROP_SATURATION` Saturation of the image (only for cameras).
- `cv.CAP_PROP_HUE` Hue of the image (only for cameras).
- `cv.CAP_PROP_GAIN` Gain of the image (only for those cameras that support).
- `cv.CAP_PROP_EXPOSURE` Exposure (only for those cameras that support).
- `cv.CAP_PROP_CONVERT_RGB` Boolean flags indicating whether images should be converted to RGB.




### VideoWriter
#### Create and Release
```py
VideoWriter(filename, fourcc, fps, frameSize, isColor=ture) -> retval
open(filename, fourcc, fps, frameSize, isColor=ture) -> retval
    Initializes or reinitializes video writer.
    The method opens video writer. Parameters are the same as in the constructor.
    Return `true` if video writer has been successfully initialized

    filename : Name of the output video file.
    fourcc : 4-character code of codec used to compress the frames.
             If fourcc is -1, it will pop up the codec selection dialog.
    fps	: Framerate of the created video stream.
    frameSize : Size of the video frames.
    isColor : If it is not zero, the encoder will expect and encode color frames,
              otherwise it will work with grayscale frames.


isOpened() -> retval
    Return true if video writer has been successfully initialized.

write(image) ->	None
    Writes the next video frame.
    image : In general, color images are expected in BGR format.
            It must have the same size as has been specified when opening the 
            video writer.

release() -> None
    Close the video writer.
    The method is automatically called by subsequent VideoWriter::open and 
    by the VideoWriter destructor.
```

#### fourcc
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








## Draw
### Rectangle
```py
rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
    pt1 : Vertex of the rectangle.
    pt2 : Vertex of the rectangle opposite to pt1 .
    color : Rectangle color or brightness (grayscale image).
    thickness : Thickness of lines that make up the rectangle. Negative 
                values mean that the function has to draw a filled rectangle.
    lineType : Type of the line.
    shift : Number of fractional bits in the point coordinates.
```

### Text
```py
putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType
        [, bottomLeftOrigin]]]) -> img
    org : Bottom-left corner of the text string in the image.
    fontFace : Font type.
    fontScale : Font scale factor that is multiplied by the font-specific 
                base size.
    color : Text color in `BGR` orger.
    thickness : Thickness of the lines used to draw a text.
    lineType : Line type. See #LineTypes
    bottomLeftOrigin : When true, the image data origin is at the bottom-left 
                       corner. Otherwise, it is at the top-left corner.
```
- `cv.FONT_HERSHEY_SIMPLEX` normal size sans-serif font
- `cv.FONT_HERSHEY_PLAIN` small size sans-serif font
- `cv.FONT_HERSHEY_DUPLEX` normal size sans-serif font (more complex than FONT_HERSHEY_SIMPLEX)
- `cv.FONT_HERSHEY_COMPLEX` normal size serif font
- `cv.FONT_HERSHEY_TRIPLEX` normal size serif font (more complex than FONT_HERSHEY_COMPLEX)
- `cv.FONT_HERSHEY_COMPLEX_SMALL` smaller version of FONT_HERSHEY_COMPLEX
- `cv.FONT_HERSHEY_SCRIPT_SIMPLEX` hand-writing style font
- `cv.FONT_HERSHEY_SCRIPT_COMPLEX` more complex variant of FONT_HERSHEY_SCRIPT_SIMPLEX
- `cv.FONT_ITALIC` flag for italic font









## Shorthand
**Open, Save and Close**
- `im = cv2.imread(filename[, flags])`
  - `cv2.IMREAD_COLOR` Default, whose value is 1.
  - `cv2.IMREAD_GRAYSCALE` Load an image in grayscale mode, whose value is 0.
  - `cv2.IMREAD_UNCHANGED` Load an image as such including alpha channel, whose value is -1.
- `cv2.imwrite(filename, im)`
<br>

- `cap = cv2.VideoCapture(filename/index)` Passing `0` will open default camera using default backend.
- `cap.release()`
- `video = VideoWriter(filename, fourcc, fps, frameSize)`
  - `cv2.VideoWriter_fourcc(*"mp4v")` for `.mp4` video.
  - `cv2.VideoWriter_fourcc(*"XVID"/"AVI1")` for `.avi` video.
  - `cv2.VideoWriter_fourcc(*"I420")` for `.avi` raw video.
- `video.release()`




