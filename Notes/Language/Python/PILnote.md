
<!-- TOC -->

- [Image](#image)
  - [Attributes](#attributes)
  - [Methods](#methods)
    - [Convert](#convert)
    - [Split](#split)
    - [Cut, Copy and Paste](#cut-copy-and-paste)
    - [Resize](#resize)
    - [Rotate](#rotate)
    - [Pixel](#pixel)
    - [Alpha](#alpha)
    - [Filter](#filter)
  - [Functions](#functions)
- [ImageFilter](#imagefilter)
  - [MultibandFilter](#multibandfilter)
    - [GaussianBlur](#gaussianblur)
    - [BoxBlur](#boxblur)
    - [BuiltinFilter](#builtinfilter)
- [ImageEnhance](#imageenhance)

<!-- /TOC -->






### Image
#### Attributes
```py
>>> from PIL import Image
>>> im = Image.open('a.jpg')
>>> print(im.filename)
a.jpg
>>> print(im.format)
JPEG
>>> print(im.mode)
RGB
>>> print(im.size)
(2894, 4093)
>>> print(im.width)
2894
>>> print(im.height)
4093
```

#### Methods
```py
show(title=None)
    Displays this image.
load()
    Allocates storage for the image and loads the pixel data

save(fp, format=None, **params)
    Saves this image under the given filename.  If no format is
    specified, the format to use is determined from the filename
    extension, if possible.
close()
    Closes the file pointer, if possible.
```
##### Convert
```py
convert(mode=None, matrix=None, ...)
    Returns a converted copy of this image.
    "1" : 1-bit black and white
    "L" : 8-bit grey
    "P" : 8-bit color
    "RGB" : 24-bit Red, Green, Blue
    "RGBA" : 32-bit Red, Green, Blue, Alpha
    "CMYK" : 32-bit Cyan, Magenta, Yellow, Key plate
    "YCbCr" : 24-bit Luminance, Blue, Red
```

##### Split
```py
split()
    Split this image into individual bands. This method returns a
    tuple of individual image bands from an image.
getchannel(channel)
    Returns an image containing a single channel of the source image.
    
    :param channel: What channel to return. Could be index
    (0 for "R" channel of "RGB") or channel name
    ("A" for alpha channel of "RGBA").
    :returns: An image in "L" mode.

>>> r, g, b = im1.split()
>>> im2 = Image.merge('RGB', (b, g, r))
```

##### Cut, Copy and Paste
```py
crop(box=None)
    Returns a rectangular region from this image. The box is a
    4-tuple defining the left, upper, right, and lower pixel
    coordinate.
copy(self)
    Copies this image.
paste(im, box=None, mask=None)
    Pastes another image into this image.
    :param im: Source image or pixel value (integer or tuple). Instead 
        of an image, the source can be a integer or tuple containing 
        pixel values.The method then fills the region with the given 
        color.
    :param box: The box argument is either a 2-tuple giving the upper 
        left corner, a 4-tuple defining the left, upper, right, and 
        lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple 
        is given, the size of the pasted image must  match the size of 
        the region.
    :param mask: If a mask is given, this method updates only the 
        regions indicated by the mask. You can use either "1", "L", 
        "LA", "RGBA" or "RGBa" images (if present, the alpha band is 
        used as mask). If the modes don't match, the pasted image is 
        converted to the mode of this image.
        Where the mask is 255, the given image is copied as is. Where 
        the mask is 0, the current value is preserved. Intermediate 
        values will mix the two images together, including their alpha 
        channels if they have them.

>>> box = (100, 100, 300, 300)
>>> region = im.crop(box)
>>> im.paste(region, box)
```

##### Resize
```py
resize(size, resample=None, box=None, reducing_gap=None)
    Returns a resized copy of this image.
    :param size: The requested size in pixels, as a 2-tuple:
       (width, height).
    :param resample: An optional resampling filter.
    :param box: An optional 4-tuple of floats providing the source image region 
       to be scaled.
       The values must be within (0, 0, width, height) rectangle.
       If omitted or None, the entire source is used.

```

##### Rotate
```py
transpose(method)
    Returns a flipped or rotated copy of this image.
    :param method: :py:data:"Transpose.FLIP_LEFT_RIGHT",
      :py:data:"Transpose.FLIP_TOP_BOTTOM", :py:data:"Transpose.ROTATE_90",
      :py:data:"Transpose.ROTATE_180", :py:data:"Transpose.ROTATE_270",
      :py:data:"Transpose.TRANSPOSE" or :py:data:"Transpose.TRANSVERSE".
    If rotated, it will rotate counter clockwise around its centre.

rotate(angle, ..., expand=0, center=None, translate=None, fillcolor=None)
    Returns a rotated copy of this image. This method returns a
    copy of this image, rotated the given number of degrees counter
    clockwise around its centre.
    :param expand: Optional expansion flag.  If true, expands the output
       image to make it large enough to hold the entire rotated image.
    :param center: Optional center of rotation (a 2-tuple).  Origin is
       the upper left corner.  Default is the center of the image.
    :param translate: An optional post-rotate translation (a 2-tuple).
    :param fillcolor: An optional color for area outside the rotated image.

>>> im = im.transpose(Image.Transpose.ROTATE_90)
>>> im = im.rotate(-10, expand=True, translate=(100, 100), fillcolor="white")
```

##### Pixel
```py
getpixel(xy)
    Returns the pixel value at a given position.
putpixel(xy, value)
    Modifies the pixel at the given position.
point(lut, mode=None)
    Map this image through a lookup table or function.
    :param lut: A lookup table, containing 256 (or 65536 if
       self.mode=="I" and mode == "L") values per band in the
       image. A function can be used instead, it should take a
       single argument. The function is called once for each
       possible pixel value, and the resulting table is applied to
       all bands of the image.

>>> im.mode
'RGB'
>>> new = im.point(lambda x: 0 if x < 128 else 255)
```

##### Alpha
```py
putalpha(alpha)
    Adds or replaces the alpha layer in this image.  If the image
    does not have an alpha layer, it's converted to "LA" or "RGBA".
    The new layer must be either "L" or "1".
    :param alpha: The new alpha layer.  This can either be an "L" or 
        "1" image having the same size as this image, or an integer or 
        other color value.
```

##### Filter
```py
filter(filter)
    Filters this image using the given filter.  For a list of
    available filters, see the :py:mod:`~PIL.ImageFilter` module.

    :param filter: Filter kernel.
    :returns: An :py:class:`~PIL.Image.Image` object.
```








#### Functions
```py
open(fp, mode='r', formats=None)
    Opens and identifies the given image file.

blend(im1, im2, alpha)
    Creates a new image by interpolating between two input images, using
    a constant alpha::

        out = image1 * (1.0 - alpha) + image2 * alpha

    :param im1: The first image.
    :param im2: The second image.  Must have the same mode and size as
       the first image.
    :param alpha: The interpolation alpha factor.  If alpha is 0.0, a
       copy of the first image is returned. If alpha is 1.0, a copy of
       the second image is returned. There are no restrictions on the
       alpha value. If necessary, the result is clipped to fit into
       the allowed output range.
merge(mode, bands)
    Merge a set of single band images into a new multiband image.
    
    :param mode: The mode to use for the output image. See:
        :ref:`concept-modes`.
    :param bands: A sequence containing one single-band image for
        each band in the output image.  All bands must have the
        same size.
new(mode, size, color=0)
    Creates a new image with the given mode and size.
    :param mode: The mode to use for the new image. See:
    :param size: A 2-tuple, containing (width, height) in pixels.
    :param color: What color to use for the image.  Default is black.
       If given, this should be a single integer or floating point value
       for single-band modes, and a tuple for multi-band modes (one value
       per band).  When creating RGB images, you can also use color
       strings as supported by the ImageColor module.  If the color is
       None, the image is not initialised.

eval(image, *args)
    Applies the function (which should take one argument) to each pixel
    in the given image. If the image has more than one band, the same
    function is applied to each band. Note that the function is
    evaluated once for each possible pixel value, so you cannot use
    random components or other generators.
    
    :param image: The input image.
    :param function: A function object, taking one integer argument.
```













### ImageFilter

#### MultibandFilter
##### GaussianBlur
```py
class GaussianBlur(MultibandFilter):
    """Blurs the image with a sequence of extended box filters, which
    approximates a Gaussian kernel.

    :param radius: Standard deviation of the Gaussian kernel.
    """

    name = "GaussianBlur"

    def __init__(self, radius=2):
        self.radius = radius

    def filter(self, image):
        return image.gaussian_blur(self.radius)
```

##### BoxBlur
```py
class BoxBlur(MultibandFilter):
    """Blurs the image by setting each pixel to the average value of the pixels
    in a square box extending radius pixels in each direction.
    Supports float radius of arbitrary size. Uses an optimized implementation
    which runs in linear time relative to the size of the image
    for any radius value.

    :param radius: Size of the box in one direction. Radius 0 does not blur,
                   returns an identical image. Radius 1 takes 1 pixel
                   in each direction, i.e. 9 pixels in total.
    """

    name = "BoxBlur"

    def __init__(self, radius):
        self.radius = radius

    def filter(self, image):
        return image.box_blur(self.radius)
```

##### BuiltinFilter
```py
def filter(self, image):
    if image.mode == "P":
        raise ValueError("cannot filter palette images")
    return image.filter(*self.filterargs)

class Kernel(BuiltinFilter):
    """
    Create a convolution kernel.  The current version only
    supports 3x3 and 5x5 integer and floating point kernels.

    In the current version, kernels can only be applied to
    "L" and "RGB" images.

    :param size: Kernel size, given as (width, height). In the current
                    version, this must be (3,3) or (5,5).
    :param kernel: A sequence containing kernel weights.
    :param scale: Scale factor. If given, the result for each pixel is
                    divided by this value.  The default is the sum of the
                    kernel weights.
    :param offset: Offset. If given, this value is added to the result,
                    after it has been divided by the scale factor.
    """

    name = "Kernel"

    def __init__(self, size, kernel, scale=None, offset=0):
        if scale is None:
            # default scale is sum of kernel
            scale = functools.reduce(lambda a, b: a + b, kernel)
        if size[0] * size[1] != len(kernel):
            raise ValueError("not enough coefficients in kernel")
        self.filterargs = size, scale, offset, kernel
```
**BLUR**
```py
filterargs = (5, 5), 16, 0, (
    1, 1, 1, 1, 1,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 1, 1,
)
```
**CONTOUR**
```py
filterargs = (3, 3), 1, 255, (
    -1, -1, -1,
    -1,  8, -1,
    -1, -1, -1,
)
```
**DETAIL**
```py
filterargs = (3, 3), 6, 0, (
    0,  -1,  0,
    -1, 10, -1,
    0,  -1,  0,
)
```
**EDGE_ENHANCE**
```py
filterargs = (3, 3), 2, 0, (
    -1, -1, -1,
    -1, 10, -1,
    -1, -1, -1,
)
```
**EDGE_ENHANCE_MORE**
```py
filterargs = (3, 3), 1, 0, (
    -1, -1, -1,
    -1,  9, -1,
    -1, -1, -1,
)
```
**EMBOSS**
```py
filterargs = (3, 3), 1, 128, (
    -1, 0, 0,
    0,  1, 0,
    0,  0, 0,
)
```
**FIND_EDGES**
```py
filterargs = (3, 3), 1, 0, (
    -1, -1, -1,
    -1,  8, -1,
    -1, -1, -1,
)
```
**SHARPEN**
```py
filterargs = (3, 3), 16, 0, (
    -2, -2, -2,
    -2, 32, -2,
    -2, -2, -2,
)
```
**SMOOTH**
```py
filterargs = (3, 3), 13, 0, (
    1, 1, 1,
    1, 5, 1,
    1, 1, 1,
)
```
**SMOOTH_MORE**
```py
filterargs = (5, 5), 100, 0, (
    1, 1,  1, 1, 1,
    1, 5,  5, 5, 1,
    1, 5, 44, 5, 1,
    1, 5,  5, 5, 1,
    1, 1,  1, 1, 1,
)
```






### ImageEnhance
```py
class _Enhance:
    def enhance(self, factor):
        """
        Returns an enhanced image.

        :param factor: A floating point value controlling the enhancement.
                       Factor 1.0 always returns a copy of the original image,
                       lower factors mean less color (brightness, contrast,
                       etc), and higher values more. There are no restrictions
                       on this value.
        :rtype: :py:class:`~PIL.Image.Image`
        """
        return Image.blend(self.degenerate, self.image, factor)


class Color(_Enhance):
    def __init__(self, image):
        self.image = image
        self.intermediate_mode = "L"
        if "A" in image.getbands():
            self.intermediate_mode = "LA"

        self.degenerate = image.convert(self.intermediate_mode).convert(image.mode)


class Contrast(_Enhance):
    def __init__(self, image):
        self.image = image
        mean = int(ImageStat.Stat(image.convert("L")).mean[0] + 0.5)
        self.degenerate = Image.new("L", image.size, mean).convert(image.mode)

        if "A" in image.getbands():
            self.degenerate.putalpha(image.getchannel("A"))


class Brightness(_Enhance):
    def __init__(self, image):
        self.image = image
        self.degenerate = Image.new(image.mode, image.size, 0)

        if "A" in image.getbands():
            self.degenerate.putalpha(image.getchannel("A"))


class Sharpness(_Enhance):
    def __init__(self, image):
        self.image = image
        self.degenerate = image.filter(ImageFilter.SMOOTH)

        if "A" in image.getbands():
            self.degenerate.putalpha(image.getchannel("A"))
```





