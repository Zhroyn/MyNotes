
[toc]




## PIL.Image
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
```

**Split**
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

**Cut, Copy and Paste**
```py
crop(box=None)
    Returns a rectangular region from this image. The box is a
    4-tuple defining the left, upper, right, and lower pixel
    coordinate.
copy(self)
    Copies this image.
paste(im, box=None, mask=None)
    Pastes another image into this image. The box argument is either
    a 2-tuple giving the upper left corner, a 4-tuple defining the
    left, upper, right, and lower pixel coordinate, or None (same as
    (0, 0)). If a 4-tuple is given, the size of the pasted image must 
    match the size of the region.
    If the modes don't match, the pasted image is converted to the mode of
    this image

>>> box = (100, 100, 300, 300)
>>> region = im.crop(box)
>>> im.paste(region, box)
```

**Resize**
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

**Rotate**
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

**Pixel**
```py
getpixel(xy)
    Returns the pixel value at a given position.
putpixel(xy, value)
    Modifies the pixel at the given position.
point(lut, mode=None)
    Maps this image through a lookup table or function.
    :param lut: A lookup table, containing 256 (or 65536 if
       self.mode=="I" and mode == "L") values per band in the
       image.  A function can be used instead, it should take a
       single argument. The function is called once for each
       possible pixel value, and the resulting table is applied to
       all bands of the image.
```

**Alpha**
```py
putalpha(alpha)
    Adds or replaces the alpha layer in this image.  If the image
    does not have an alpha layer, it's converted to "LA" or "RGBA".
    The new layer must be either "L" or "1".
    :param alpha: The new alpha layer.  This can either be an "L" or "1"
    image having the same size as this image, or an integer or
    other color value.
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



## PIL.ImageFilter

#### BuiltinFilter
- BLUR
- CONTOUR
- DETAIL
- EDGE_ENHANCE
- EDGE_ENHANCE_MORE
- EMBOSS
- FIND_EDGES
- SMOOTH
- SMOOTH_MORE
- SHARPEN

#### MultibandFilter
```py
BoxBlur(radius)
    Blurs the image by setting each pixel to the average value of the pixels
    in a square box extending radius pixels in each direction.
    Supports float radius of arbitrary size. Uses an optimized implementation
    which runs in linear time relative to the size of the image
    for any radius value.
     
    :param radius: Size of the box in one direction. Radius 0 does not blur,
                   returns an identical image. Radius 1 takes 1 pixel
                   in each direction, i.e. 9 pixels in total.


GaussianBlur(radius=2)
  Blurs the image with a sequence of extended box filters, which
  approximates a Gaussian kernel.

  :param radius: Standard deviation of the Gaussian kernel.
```




## PIL.ImageEnhance
```py
# An enhancement factor of 0.0 gives a black image.
# A factor of 1.0 gives the original image.
enh_bri = ImageEnhance.Brightness(image)
im = enh_bri.enhance(brightness)


# An enhancement factor of 0.0 gives a black and white image.
# A factor of 1.0 gives the original image.
enh_col = ImageEnhance.Color(image)
im = enh_col.enhance(color)


# An enhancement factor of 0.0 gives a solid grey image.
# A factor of 1.0 gives the original image.
enh_con = ImageEnhance.Contrast(image)
im = enh_con.enhance(contrast)


# An enhancement factor of 0.0 gives a blurred image.
# A factor of 1.0 gives the original image
# A factor of 2.0 gives a sharpened image.
enh_sha = ImageEnhance.Sharpness(image)
im = enh_sha.enhance(sharpness)
```


