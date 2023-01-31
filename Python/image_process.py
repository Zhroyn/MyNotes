import os
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance



def impath_add_suffix(impath, out_suffix, out_dir=None, format="jpg"):
    src_dir, src = os.path.split(impath)
    name, ext = os.path.splitext(src)
    if out_dir == None:
        out_dir = src_dir
    if out_dir[-1] != "/":
        out_dir = out_dir + "/"
    return out_dir + name + out_suffix + "." + format

def get_paths(prefix, name, suffix, out_suffix=""):
    impath = prefix + name + suffix
    outpath = impath_add_suffix(impath, out_suffix)
    return impath, outpath
    
def change_quailty(src, scale):
    if scale == 1 or scale <= 0:
        pass
    else:
        if scale < 1:
            interpolation = cv2.INTER_AREA
        else:
            interpolation = cv2.INTER_CUBIC
        im = cv2.resize(src, None, fx=scale, fy=scale,
                        interpolation=interpolation)
        return im

def enhance_color(src, factor):
    im = Image.fromarray(src)
    enh_col = ImageEnhance.Color(im)
    im = enh_col.enhance(factor)
    return np.asarray(im)

def enhance_sharpness(src, factor):
    im = Image.fromarray(src)
    enh_sha = ImageEnhance.Sharpness(im)
    im = enh_sha.enhance(factor)
    return np.asarray(im)

def gaussian_blur(src, sigma):
    return cv2.GaussianBlur(src, None, sigma)

def remove_background(src, delta):
    h, w = src.shape[:2]
    bg_color = src[5, 5].copy()
    print("Background Color :",bg_color)
    for y in range(h):
        for x in range(w):
            b, g, r = src[y, x]
            if (abs(int(b) - int(bg_color[0])) <= delta
            and abs(int(g) - int(bg_color[1])) <= delta
            and abs(int(r) - int(bg_color[2])) <= delta):
                src[y, x] = 255
    return src

def remove_stains(src, threshold):
    h, w = src.shape[:2]
    threshold = 3 * threshold
    for y in range(h):
        for x in range(w):
            if (int(src[y, x, 0])
            + int(src[y, x, 1])
            + int(src[y, x, 1]) > threshold):
                src[y, x] = 255
    return src

def image_process(impath, outpath, argv):
    im = cv2.imread(impath)
    if im is None:
        raise FileNotFoundError(impath)
    
    operations = argv.split()
    for operation in operations:
        func, colon, arg = operation.partition(":")
        arg = float(arg)
        if func == "cq":
            im = change_quailty(im, arg)
        elif func == "col":
            im = enhance_color(im, arg)
        elif func == "sha":
            im = enhance_sharpness(im, arg)
        elif func == "rbg":
            im = remove_background(im, arg)
        elif func == "rst":
            im = remove_stains(im, arg)
        elif func == "gau":
            im = gaussian_blur(im, arg)
    
    cv2.imwrite(outpath, im)
    print(outpath, "ended.")






rm_stains = " cq:2 sha:2 cq:2 rst:200 gau:0.5 cq:0.5"
clear_bg = " sha:2 cq:2 sha:2 cq:2 rbg:25 rst:200 col:1.7 cq:0.5"
clear_bg_blur = " cq:2 sha:2 cq:2 rbg:25 rst:200 col:1.7 cq:0.5"

src_dir = "C:/Users/hrzhe/Pictures/Calculus/"
argv = clear_bg
out_suffix = argv.replace(":", "").replace(".", "")
out_suffix = "_"
# l = os.listdir(src_dir)
l = [2, 3, 4, 5, 6, 8, 9, 11, 12]
l = [2]

for i in l:
    impath, outpath = get_paths(src_dir, str(i), ".png", out_suffix)
    image_process(impath, outpath, argv)




