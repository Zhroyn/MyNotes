<!-- TOC -->

- [Display](#display)
        - [Open and Close](#open-and-close)
        - [Keys](#keys)
- [Image](#image)
    - [Basic](#basic)
        - [Open and Save](#open-and-save)
        - [Image representation](#image-representation)
    - [Image Process](#image-process)
        - [Arithmetic Operation](#arithmetic-operation)
            - [Add and Subtract](#add-and-subtract)
            - [Bit Operation](#bit-operation)
        - [Split and Merge](#split-and-merge)
        - [Smoothing](#smoothing)
        - [Geometric Image Transformations](#geometric-image-transformations)
    - [Attributes](#attributes)
        - [borderType](#bordertype)
        - [interpolation](#interpolation)
- [Video](#video)
    - [VideoCapture](#videocapture)
        - [Open and Release](#open-and-release)
        - [Capture frame](#capture-frame)
        - [VideoCaptureProperties](#videocaptureproperties)
    - [VideoWriter](#videowriter)
        - [Create and Release](#create-and-release)
        - [fourcc](#fourcc)
- [Draw](#draw)
    - [Text](#text)
- [Shorthand](#shorthand)

<!-- /TOC -->






## Display
#### Open and Close
```py
namedWindow(winname[, flags]) -> None
    If a window with the same name already exists, the function does nothing.
    flags : 
    WINDOW_NORMAL or WINDOW_AUTOSIZE: WINDOW_NORMAL enables you to resize the
            window, whereas WINDOW_AUTOSIZE adjusts automatically the window 
            size to fit the displayed image, and you cannot change the window 
            size manually.
    WINDOW_FREERATIO or WINDOW_KEEPRATIO: WINDOW_FREERATIO adjusts the image
            with no respect to its ratio, whereas WINDOW_KEEPRATIO keeps the 
            image ratio.
    WINDOW_GUI_NORMAL or WINDOW_GUI_EXPANDED: WINDOW_GUI_NORMAL is the old way 
            to draw the window without statusbar and toolbar, whereas 
            WINDOW_GUI_EXPANDED is a new enhanced GUI.
    By default, flags == WINDOW_AUTOSIZE | WINDOW_KEEPRATIO | WINDOW_GUI_EXPANDED


imshow(winname, mat) -> None
    If the window was not created before this function, it is assumed creating 
    a window with cv::WINDOW_AUTOSIZE.
    This function should be followed by a call to cv::waitKey or cv::pollKey to 
    perform GUI housekeeping tasks that are necessary to actually show the given 
    image and make the window respond to mouse and keyboard events. Otherwise, 
    it won't display the image and the window might lock up.

destroyWindow(winname) -> None
    Destroy the window with the given name.

destroyAllWindows() -> None
    Destroy all of the opened HighGUI windows.
```

#### Keys
```py
waitKey([, delay]) -> retval
    Wait for a key event infinitely or for delay milliseconds if it is positive.
    It returns the code of the pressed key or -1 if no key was pressed before 
    the specified time had elapsed.
```






## Image
### Basic
#### Open and Save
```py
imread(filename[, flags]) -> retval
    If the image cannot be read, the function returns an empty matrix.
    The function determines the type of image by content, not by file extension.
    flags : The default value is cv2.IMREAD_COLOR.
        cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency 
                          of image will be neglected. Its value is 1.
        cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. 
                              Its value is 0.
        cv2.IMREAD_UNCHANGED: It specifies to load an image as such including 
                              alpha channel. Its value is -1.

imwrite(filename, img[, params]) -> retval
    Return true if image is saved successfully.
    The image format is chosen based on the filename extension.
```

#### Image representation
- In RGB color space, the order of image channels is BGR.
- In pixel coordinates, the first index represents the row(height), the secend index represents the colunm(width).





### Image Process
#### Arithmetic Operation
- `+` `-` `*` `/` : The result will take the modulus. If operators are two arrays, the new pixel value is the value obtained after the corresponding operation of the original two pixel values.
- When used with `mask`, the operation will only be performed on pixels with non-zero mask value, and the value of other pixels will be set to 0.


##### Add and Subtract
```py
add(src1, src2[, dst[, mask[, dtype]]]) -> dst
    @brief Calculates the per-element sum of two arrays or an array and a scalar.
    The function add calculates the sum of two arrays when both input arrays 
    have the same size and the same number of channels, or the sum of an array 
    and a scalar when src1 or src2 is constructed from Scalar or has the same 
    number of elements as `src1.channels()` or `src2.channels()`.
    @note Saturation is not applied when the output array has the depth CV_32S.

    @param src1 : first input array or a scalar.
    @param src2 : second input array or a scalar.
    @param dst : output array that has the same size and number of channels as 
                 the input array(s); the depth is defined by dtype or src1/src2.
    @param mask : optional operation mask - 8-bit single channel array, that 
                  specifies elements of the output array to be changed.
    @param dtype : optional depth of the output array.

addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) -> dst
    @brief Calculates the weighted sum of two arrays.
    The function addWeighted calculate the weighted sum of two arrays as follows:
        dst = src1*alpha + src2*beta + gamma
    @note Saturation is not applied when the output array has the depth CV_32S.
    @param src1 : first input array.
    @param alpha : weight of the first array elements.
    @param src2 : second input array of the same size and channel number as src1.
    @param beta : weight of the second array elements.
    @param gamma : scalar added to each sum.
    @param dst : output array that has the same size and number of channels as 
                 the input arrays.
    @param dtype : optional depth of the output array; when both input arrays 
                   have the same depth, dtype can be set to -1, which will be 
                   equivalent to src1.depth().

subtract(src1, src2[, dst[, mask[, dtype]]]) -> dst
    @brief Calculates the per-element difference between two arrays or array 
    and a scalar.
    The function subtract calculates difference between two arrays, or difference
    between an array and a scalar, when src1 or src2 is constructed from Scalar
    or has the same number of elements as `src1.channels()` or `src2.channels()`.
    The function calculate as follows:
        dst = src1 - src2
    @note Saturation is not applied when the output array has the depth CV_32S.

    @param src1 : first input array or a scalar.
    @param src2 : second input array or a scalar.
    @param dst : output array that has the same size and number of channels as 
                 the input array.
    @param mask : optional operation mask - 8-bit single channel array, that 
                  specifies elements of the output array to be changed.
    @param dtype : optional depth of the output array.
```
##### Bit Operation
```py
bitwise_and(src1, src2[, dst[, mask]]) -> dst
    @brief computes bitwise conjunction of the two arrays (dst = src1 & src2)
    or an array and a scalar.
bitwise_or(src1, src2[, dst[, mask]]) -> dst
    @brief Calculates the per-element bit-wise disjunction of two arrays or an
    array and a scalar.
bitwise_xor(src1, src2[, dst[, mask]]) -> dst
    @brief Calculates the per-element bit-wise "exclusive or" operation on two
    arrays or an array and a scalar.
bitwise_not(src[, dst[, mask]]) -> dst
    @brief  Inverts every bit of an array.

    In case of floating-point arrays, their machine-specific bit representations
    (usually IEEE754-compliant) are used for the operation.
    In case of multi-channel arrays, each channel is processed independently.
    If one of the src is scalar, the scalar is first converted to the array type.

    @param src1 : first input array or a scalar.
    @param src2 : second input array or a scalar.
    @param dst : output array that has the same size and type as input arrays.
    @param mask : optional operation mask, 8-bit single channel array, that
    specifies elements of the output array to be changed.
```

#### Split and Merge
```py
split(m[, mv]) -> mv
    @param m : input multi-channel array.
    @param mv : output vector of arrays; the arrays themselves are reallocated, 
                if needed.

merge(mv[, dst]) -> dst
    @param mv : input vector of matrices to be merged; all the matrices in mv 
                must have the same size and the same depth.
    @param dst : output array of the same size and the same depth as mv[0]; The 
                 number of channels will be the total number of channels in the
                 matrix array.

b, g, r = cv2.split(im)
b = cv2.split(im)[0]
out = cv2.merge([b, g, r])  #original image
out = cv2.merge([r, g, b])
```

#### Smoothing
```py
blur(src, ksize[, dst[, anchor[, borderType]]]) -> dst
    @brief Blurs an image using the normalized box filter.
    The function smooths an image using the kernel:
    \f[
        K = \frac{1}{ksize.width*ksize.height} 
        \begin{bmatrix} 
            1 & 1 & 1 &  \cdots & 1 & 1  \\
            1 & 1 & 1 &  \cdots & 1 & 1  \\
            \hdotsfor{6} \\
            1 & 1 & 1 &  \cdots & 1 & 1  \\ 
        \end{bmatrix}
    \f]
    In-place filtering is supported.
    @param src : input image; it can have any number of channels, which are 
                 processed independently, but the depth should be CV_8U, CV_16U, 
                 CV_16S, CV_32F or CV_64F.
    @param dst : output image of the same size and type as src.
    @param ksize : blurring kernel size which can be any size.
    @param anchor : anchor point; default value Point(-1,-1) means that the 
                    anchor is at the kernel center.
    @param borderType : border mode used to extrapolate pixels outside of image.


boxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]) -> dst
    @brief Blurs an image using the box filter.
    The function smooths an image using the kernel:
    \f[
        K =  \alpha
        \begin{bmatrix} 
            1 & 1 & 1 &  \cdots & 1 & 1  \\
            1 & 1 & 1 &  \cdots & 1 & 1  \\
            \hdotsfor{6} \\
            1 & 1 & 1 &  \cdots & 1 & 1  \\ 
        \end{bmatrix}
    \f]
    In-place filtering is supported.
    @param src : input image.
    @param dst : output image of the same size and type as src.
    @param ddepth : the output image depth (-1 to use src.depth()).
    @param ksize : blurring kernel size which can be any size.
    @param anchor : anchor point; default value Point(-1,-1) means that the 
                    anchor is at the kernel center.
    @param normalize : flag, specifying whether the kernel is normalized by 
                       its area or not, default is true.
    @param borderType : border mode used to extrapolate pixels outside of image.


GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst
    @brief Blurs an image using a Gaussian filter.
    The function convolves the source image with the specified Gaussian kernel.
    In-place filtering is supported.

    @param src : input image; the image can have any number of channels, which 
                 are processed independently, but the depth should be CV_8U, 
                 CV_16U, CV_16S, CV_32F or CV_64F.
    @param dst : output image of the same size and type as src.
    @param ksize : Gaussian kernel size. ksize.width and ksize.height can differ 
                   but they both must be positive and odd. Or they can be zero's 
                   and then they are computed from sigma.
    @param sigmaX : Gaussian kernel standard deviation in X direction.
    @param sigmaY : Gaussian kernel standard deviation in Y direction; if sigmaY 
                    is zero, it is set to be equal to sigmaX, if both sigmas are 
                    zeros, they are computed from ksize.width and ksize.height.
    @param borderType : pixel extrapolation method

medianBlur(src, ksize[, dst]) -> dst
    @brief Blurs an image using the median filter.
    The function smoothes an image using the median filter.
    Each channel of a multi-channel image is processed independently.
    In-place operation is supported.
    @note The median filter uses BORDER_REPLICATE internally for border pixels.

    @param src : input 1-, 3-, or 4-channel image; when ksize is 3 or 5, the 
                 image depth should be CV_8U, CV_16U, or CV_32F, for larger 
                 aperture sizes, it can only be CV_8U.
    @param dst : destination array of the same size and type as src.
    @param ksize : aperture linear size; it must be odd and greater than 1.


bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) -> dst
    @brief Applies the bilateral filter to an image.
    This filter does not work inplace.

    @param src : Source 8-bit or floating-point, 1-channel or 3-channel image.
    @param dst : Destination image of the same size and type as src .
    @param d : Diameter of each pixel neighborhood that is used during filtering.
               If it is non-positive, it is computed from sigmaSpace.
    @param sigmaColor : Filter sigma in the color space. A larger value of the 
                        parameter means that farther colors within the pixel 
                        neighborhood will be mixed together.
    @param sigmaSpace : Filter sigma in the coordinate space. A larger value of 
                        the parameter means that farther pixels will influence 
                        each other. When d>0, it specifies the neighborhood size 
                        regardless of sigmaSpace. Otherwise d is proportional 
                        to sigmaSpace.
    @param borderType : border mode used to extrapolate pixels outside of image.


filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) -> dst
    @brief Convolves an image with the kernel.
    The function applies an arbitrary linear filter to an image.
    In-place operation is supported.

    @param src : input image.
    @param dst : output image of the same size and the same number of channels 
                 as src.
    @param ddepth : desired depth of the destination image.
    @param kernel : convolution kernel (or rather a correlation kernel), a 
                    single-channel floating point matrix.
    @param anchor : anchor of the kernel that indicates the relative position of 
                    a filtered point within the kernel; the anchor should lie 
                    within the kernel; default value (-1,-1) means that anchor 
                    is at the kernel center.
    @param delta : optional value added to the filtered pixels before storing 
                   them in dst.
    @param borderType : pixel extrapolation method.
```


#### Geometric Image Transformations
**Resize**
```py
resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) -> dst
    @brief Resizes an image.
    To shrink an image, it will generally look best with INTER_AREA interpolation
    , whereas to enlarge an image, it will generally look best with INTER_CUBIC 
    (slow) or INTER_LINEAR (default, faster but still looks OK).
    Note that the first parameter of dsize is width, and the second parameter is 
    height.
 
    @param src : input image.
    @param dst : output image; the type of dst is the same as of src.
    @param dsize : output image size; if it equals zero (`None` in Python), it 
                   is computed from fx and fy, otherwise it will determine the 
                   size of dst. Either dsize or both fx and fy must be non-zero.
    @param fx : scale factor along the horizontal axis.
    @param fy : scale factor along the vertical axis.
    @param interpolation : interpolation method.
```
**Flip**
```py
flip(src, flipCode[, dst]) -> dst
    @brief Flips a 2D array around vertical, horizontal, or both axes.
    @param flipCode : a flag to specify how to flip the array. 0 means flipping 
                      around the x-axis; positive value means flipping around 
                      y-axis; Negative value means flipping around both axes. In 
                      here, the x-axis is the vertical axis.
```
**Affine**
```py
warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) -> dst
    @brief Applies an affine transformation to an image.
    The function warpAffine transforms the source image using the specified 
    matrix (the x-axis is horizonal):
        dst(x,y) =  src( M_{11}*x + M_{12}*y + M_{13},
                         M_{21}*x + M_{22}*y + M_{23} )
    The function cannot operate in-place.

    @param dst : output image that has the size dsize and the same type as src.
    @param M : 2 * 3 transformation matrix.
    @param dsize : size of the output image.
    @param flags : combination of interpolation methods and the optional flag 
                   WARP_INVERSE_MAP that means M is the inverse transformation.
    @param borderMode : pixel extrapolation method; when borderMode=BORDER_TR
                        ANSPARENT, it means that the pixels in the destination 
                        image corresponding to the "outliers" in the source 
                        image are not modified by the function.
    @param borderValue : value used in case of a constant border; by default, 
                         it is 0.

getRotationMatrix2D(center, angle, scale) -> retval
    @brief Calculates an affine matrix of 2D rotation.
    The function calculates the following matrix:
    \f[
        \alpha = scale * \cos{angle}
        \beta =  scale * \sin{angle}
        \begin{bmatrix}
            \alpha & \beta  & (1-\alpha)*center.x - \beta*center.y \\
            \beta  & \alpha & \beta*center.x + (1-\alpha)*center.y 
        \end{bmatrix}
    \f]
    The transformation maps the rotation center to itself. If this is not the 
    target, adjust the shift.
 
    @param center : Center of the rotation in the source image. The coordinate 
                    origin is assumed to be the top-left corner
    @param angle : Rotation angle in degrees. Positive values mean counter-
                   clockwise rotation.
    @param scale : Isotropic scale factor.

getAffineTransform(src, dst) -> retval
    @brief Calculates an affine transform from three pairs of the corresponding 
    points.
    @param src : 3 * 2 matrix of coordinates of three points in the source image.
    @param dst : 3 * 2 matrix of coordinates of the corresponding points in the 
                 destination image.
```
**Perspective**
```py
warpPerspective(src, M, dsize[,dst[, flags[, borderMode[, borderValue]]]]) -> dst
    @brief Applies an perspective transformation to an image.
    The function perspective transforms the source image using the specified 
    matrix (the x-axis is horizonal):
        dst(x,y) =  src( \frac{M_{11} x + M_{12} y + M_{13}}
                              {M_{31} x + M_{32} y + M_{33}} ,
                         \frac{M_{21} x + M_{22} y + M_{23}}
                              {M_{31} x + M_{32} y + M_{33}} )
    The function cannot operate in-place.

    @param dst : output image that has the size dsize and the same type as src.
    @param M : 3 * 3 transformation matrix.
    @param dsize : size of the output image.
    @param flags : combination of interpolation methods and the optional flag 
                   WARP_INVERSE_MAP that means M is the inverse transformation.
    @param borderMode : pixel extrapolation method; when borderMode=BORDER_TR
                        ANSPARENT, it means that the pixels in the destination 
                        image corresponding to the "outliers" in the source 
                        image are not modified by the function.
    @param borderValue : value used in case of a constant border; by default, 
                         it is 0.

getPerspectiveTransform(src, dst) -> retval
    @brief Calculates an perspective transform from four pairs of the 
    corresponding points.
    @param src : 4 * 2 matrix of coordinates of four points in the source image.
    @param dst : 4 * 2 matrix of coordinates of the corresponding points in the 
                 destination image.
```
**Remap**
```py
remap(src, map1, map2, interpolation[, dst[, borderMode[, borderValue]]]) -> dst
    @brief Applies a generic geometrical transformation to an image.
    The function remap transforms the source image using the specified map:
        dst(x,y) = src(map_x(x,y), map_y(x,y))
    where values of pixels with non-integer coordinates are computed using one 
    of available interpolation methods.
    This function cannot operate in-place.
 
    @param dst : Destination image. It has the same size as map1 and the same 
                 type as src.
    @param map1 : The first map of either (x,y) points or just x values having 
                  the type CV_16SC2 , CV_32FC1, or CV_32FC2.
    @param map2 : The second map of y values having the type CV_16UC1, CV_32FC1, 
                  or none (empty map if map1 is (x,y) points), respectively.
    @param interpolation : Interpolation method. The methods INTER_AREA and 
                           INTER_LINEAR_EXACT are not supported by this function.
    @param borderMode : Pixel extrapolation method.
    @param borderValue : Value used in case of a constant border. By default, 
                         it is 0.
```


### Attributes
#### borderType
- `cv.BORDER_CONSTANT` : `iiiiii|abcdefgh|iiiiiii` with some specified i
- `cv.BORDER_REPLICATE` : `aaaaaa|abcdefgh|hhhhhhh`
- `cv.BORDER_REFLECT` : `fedcba|abcdefgh|hgfedcb`
- `cv.BORDER_WRAP` : `cdefgh|abcdefgh|abcdefg`
- `cv.BORDER_REFLECT_101` : `gfedcb|abcdefgh|gfedcba`
- `cv.BORDER_TRANSPARENT` : `uvwxyz|abcdefgh|ijklmno`
- `cv.BORDER_REFLECT101` : same as `BORDER_REFLECT_101`
- `cv.BORDER_DEFAULT` : same as `BORDER_REFLECT_101`

#### interpolation
- `cv.INTER_NEAREST` nearest neighbor interpolation
- `cv.INTER_LINEAR` bilinear interpolation
- `cv.INTER_CUBIC` bicubic interpolation
- `cv.INTER_AREA` resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire'-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
- `cv.INTER_LANCZOS4` Lanczos interpolation over 8x8 neighborhood
- `cv.INTER_LINEAR_EXACT` Bit exact bilinear interpolation
- `cv.INTER_NEAREST_EXACT` Bit exact nearest neighbor interpolation. This will produce same results as the nearest neighbor method in PIL, scikit-image or Matlab.
- `cv.INTER_MAX` mask for interpolation codes
- `cv.WARP_FILL_OUTLIERS` flag, fills all of the destination image pixels. If some of them correspond to outliers in the source image, they are set to zero
- `cv.WARP_INVERSE_MAP` flag, inverse transformation





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

**Arithmetic Operations**
  - The operation will only be performed on pixels with non-zero mask value, and the value of other pixels will be set to 0.
- `cv2.add(src1, src2[, mask])` or `cv2.add(src, (b, g, r, 0)[, mask])`
  - The scalar should be either a number or a tuple of four numbers.
  - Saturation will be applied.
- `cv2.subtract(src1, src2[, mask])` or `cv2.subtract(src, (b, g, r, 0)[, mask])` The same as `cv2.add()`.
- `cv2.addWeighted(src1, alpha, src2, beta)` Between two arrays.
- `cv2.bitwise_and(src1, src2[, mask])`
- `cv2.bitwise_or(src1, src2[, mask])`
- `cv2.bitwise_xor(src1, src2[, mask])`
- `cv2.bitwise_not(src1, src2[, mask])`

**Smooth**
- `cv2.blur(src, ksize)` In-place filtering is supported.
- `cv2.boxFilter(src, -1, ksize)` or `cv2.boxFilter(src, -1, ksize, normalize=False)`
  - The second argument is `ddepth`.
  - In-place filtering is supported.
- `cv2.GaussianBlur(src, ksize, 0, 0)`
  - `ksize.width` and `ksize.height` can differ but they both must be positive and odd. Or they can be zero's and then they are computed from sigma.
  - In-place filtering is supported.
- `cv2.medianBlur(src, ksize)`
  - `ksize` must be an odd integer.
  - In-place filtering is supported.
- `cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)`
  - `d` Diameter of each pixel neighborhood. If it is non-positive, it is computed from `sigmaSpace`.
  - `sigmaColor` A larger value means that farther colors will be mixed together.
  - `sigmaSpace` A larger value means that farther pixels will influence each other. When `d>0`, it will be neglected.
  - If the two sigma value are smaller than 10, the filter will not have much effect. If they are larger than 150, they will have a very strong effect, making the image look "cartoonish". They could be like `20, 50`.
- `cv2.filter2D(src, -1, kernel)` or `cv2.filter2D(src, -1, kernel[, delta=])`
  - The second argument is `ddepth`.
  - In-place filtering is supported.

**Geometric Image Transformations**
- `cv2.resize(src, dsize[, interpolation])` or `cv2.resize(src, None, fx=, fy=[, interpolation=])`
  - To shrink an image, it will generally look best with `INTER_AREA` interpolation, whereas to enlarge an image, it will generally look best with `INTER_CUBIC` (slow) or `INTER_LINEAR` (default, faster but still looks OK).
  - `fx` and `fy` are scale factors along the axes. The latter form must use keyword arguments.
- `cv2.flip(src, flipCode)`
  - 0 means flipping around the x-axis, that is, vertically.
  - Positive value means flipping around y-axis.
  - Negative value means flipping around both axes.
- `cv2.warpAffine(src, np.float32([[1, 0, x], [0, 1, y]]), src.shape[:2][::-1])` Translation, `x` is horizontal direction.
- `cv2.warpAffine(src, cv2.getRotationMatrix2D((width/2, height/2), angle, scale), (width, height))` Positive values mean counter-clockwise rotation.


