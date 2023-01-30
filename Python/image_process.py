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
    
def change_quailty(impath, outpath, scale):
    if scale == 1 or scale <= 0:
        pass
    im = cv2.imread(impath)
    if im is None:
        raise FileNotFoundError(impath)
    else:
        if scale < 1:
            interpolation = cv2.INTER_AREA
        else:
            interpolation = cv2.INTER_CUBIC
        im = cv2.resize(im, None, fx=scale, fy=scale,
                        interpolation=interpolation)
        cv2.imwrite(outpath, im)

def enhance_color(impath, outpath, factor):
    im = Image.open(impath)
    out_ext = os.path.splitext(outpath)[1][1:]
    if out_ext == "jpg" and im.mode != "RGB":
        im = im.convert("RGB")
    enh_col = ImageEnhance.Color(im)
    im = enh_col.enhance(factor)
    im.save(outpath)

def enhance_sharpness(impath, outpath, factor):
    im = Image.open(impath)
    out_ext = os.path.splitext(outpath)[1][1:]
    if out_ext == "jpg" and im.mode != "RGB":
        im = im.convert("RGB")
    enh_sha = ImageEnhance.Sharpness(im)
    im = enh_sha.enhance(factor)
    im.save(outpath)

def gaussian_blur(impath, outpath, sigma):
    im = cv2.imread(impath)
    im = cv2.GaussianBlur(im, None, sigma)
    cv2.imwrite(outpath, im)

def remove_background(impath, outpath, delta):
    im = cv2.imread(impath)
    if im is None:
        raise FileNotFoundError(impath)
    else:
        h, w = im.shape[:2]
        bg_color = im[10, 10].copy()
        print("Background Color :",bg_color)
        for y in range(h):
            for x in range(w):
                b, g, r = im[y, x]
                if (abs(int(b) - int(bg_color[0])) <= delta
                and abs(int(g) - int(bg_color[1])) <= delta
                and abs(int(r) - int(bg_color[2])) <= delta):
                    im[y, x] = 255
        cv2.imwrite(outpath, im)

def remove_stains(impath, outpath, threshold):
    im = cv2.imread(impath)
    if im is None:
        raise FileNotFoundError(impath)
    else:
        h, w = im.shape[:2]
        threshold = 3 * threshold
        for y in range(h):
            for x in range(w):
                if (int(im[y, x, 0])
                + int(im[y, x, 1])
                + int(im[y, x, 1]) > threshold):
                    im[y, x] = 255
        cv2.imwrite(outpath, im)

def image_process(impath, outpath, argv):
    operations = argv.split()
    n = 0
    for operation in operations:
        func, colon, arg = operation.partition(":")
        arg = float(arg)
        if n > 0:
            impath = outpath
        if func == "cq":
            change_quailty(impath, outpath, arg)
        elif func == "col":
            enhance_color(impath, outpath, arg)
        elif func == "sha":
            enhance_sharpness(impath, outpath, arg)
        elif func == "rbg":
            remove_background(impath, outpath, arg)
        elif func == "rst":
            remove_stains(impath, outpath, arg)
        elif func == "gau":
            gaussian_blur(impath, outpath, arg)
        n += 1
    print(outpath, "ended.")






rm_stains = " cq:2 sha:2 cq:2 rst:200 gau:0.5 cq:0.5"
clear_bg = " sha:2 cq:2 sha:2 cq:2 rbg:25 rst:200 col:1.7 cq:0.5"
clear_bg_blur = " cq:2 sha:2 cq:2 rbg:25 rst:200 col:1.7 cq:0.5"

src_dir = "C:/Users/hrzhe/Pictures/Calculus/"
argv = "rst:200 gau:1"
out_suffix = "_"
out_suffix = argv.replace(":", "").replace(".", "")
# l = os.listdir(src_dir)
l = [2, 3, 4, 5, 6, 8, 9, 11, 12]
l = [7]

for i in l:
    impath, outpath = get_paths(src_dir, str(i), ".png", out_suffix)
    image_process(impath, outpath, argv)




