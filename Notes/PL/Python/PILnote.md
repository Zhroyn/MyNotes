

## PIL.Image
#### Attributes
```py
>>> from PIL import Image
>>> img = Image.open('a.jpg')
>>> print(img.filename)
a.jpg
>>> print(img.format)
JPEG
>>> print(img.mode)
RGB
>>> print(img.size)
(2894, 4093)
>>> print(img.width)
2894
>>> print(img.height)
4093
```

#### Methods
```py
show(title=None)
    Displays this image.
save(fp, format=None, **params)
    Saves this image under the given filename.  If no format is
    specified, the format to use is determined from the filename
    extension, if possible.
```
**Convert**
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
split()
    Split this image into individual bands. This method returns a
    tuple of individual image bands from an image.

>>> r, g, b = image.split()
>>> img = Image.merge('RGB', (b, g, r))
```

**Cut and Paste**
```py
crop(box=None)
    Returns a rectangular region from this image. The box is a
    4-tuple defining the left, upper, right, and lower pixel
    coordinate.
paste(im, box=None, mask=None)
    Pastes another image into this image. The box argument is either
    a 2-tuple giving the upper left corner, a 4-tuple defining the
    left, upper, right, and lower pixel coordinate, or None (same as
    (0, 0)). If a 4-tuple is given, the size of the pasted image must 
    match the size of the region.
    If the modes don't match, the pasted image is converted to the mode of
    this image
resize(size, resample=None, box=None, reducing_gap=None)
    Returns a resized copy of this image.
    :param size: The requested size in pixels, as a 2-tuple:
       (width, height).
    :param resample: An optional resampling filter.
    :param box: An optional 4-tuple of floats providing
       the source image region to be scaled.
       The values must be within (0, 0, width, height) rectangle.
       If omitted or None, the entire source is used.

>>> box = (100, 100, 300, 300)
>>> region = img.crop(box)
>>> img.paste(region, box)
```

**Rotate**
```py
transpose(method)
    Returns a flipped or rotated copy of this image.
    :param method: :py:data:"Transpose.FLIP_LEFT_RIGHT",
      :py:data:"Transpose.FLIP_TOP_BOTTOM", :py:data:"Transpose.ROTATE_90",
      :py:data:"Transpose.ROTATE_180", :py:data:"Transpose.ROTATE_270",
      :py:data:"Transpose.TRANSPOSE" or :py:data:"Transpose.TRANSVERSE".

rotate(angle, ..., expand=0, center=None, translate=None, fillcolor=None)
    Returns a rotated copy of this image. This method returns a
    copy of this image, rotated the given number of degrees counter
    clockwise around its centre.
    :param expand: Optional expansion flag.  If true, expands the output
       image to make it large enough to hold the entire rotated image.
    :param center: Optional center of rotation (a 2-tuple).  Origin is
       the upper left corner.  Default is the center of the image.

>>> img = img.transpose(Image.Transpose.ROTATE_90)
>>> translation = (100, 100)
>>> white = (255, 255, 255)
>>> img = img.rotate(-10, expand=True, translation. white)
```

**Pixel**
```py
point(lut, mode=None)
    Maps this image through a lookup table or function.
    :param lut: A lookup table, containing 256 (or 65536 if
       self.mode=="I" and mode == "L") values per band in the
       image.  A function can be used instead, it should take a
       single argument. The function is called once for each
       possible pixel value, and the resulting table is applied to
       all bands of the image.
```



#### Functions
```py
open(fp, mode='r', formats=None)
    Opens and identifies the given image file.

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
```

