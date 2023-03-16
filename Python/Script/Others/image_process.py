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

def scale_image(src, factor):
    interpolation = cv2.INTER_AREA if factor < 1 \
        else cv2.INTER_CUBIC
    im = cv2.resize(src, None, fx=factor, fy=factor,
                    interpolation=interpolation)
    return im

def enhance_color(src, factor):
    im = Image.fromarray(src)
    enh_col = ImageEnhance.Color(im)
    im = enh_col.enhance(factor)
    return np.array(im)

def enhance_contrast(src, factor):
    im = Image.fromarray(src)
    enh_con = ImageEnhance.Contrast(im)
    im = enh_con.enhance(factor)
    return np.array(im)

def enhance_sharpness(src, factor):
    im = Image.fromarray(src)
    enh_sha = ImageEnhance.Sharpness(im)
    im = enh_sha.enhance(factor)
    return np.array(im)

def gaussian_blur(src, sigma):
    return cv2.GaussianBlur(src, None, sigma)

def remove_background(src, threshold):
    im = np.full(src.shape, [255, 255, 255])
    mask = src < [threshold, threshold, threshold]
    np.copyto(im, src, where=mask)
    return im

def clear_background(src, threshold):
    h, w = src.shape[:2]
    bg_colors = []
    for y in range(0, h, h // 10):
        for x in range(0, w, w // 10):
            bg_colors.append(src[y, x])
    bg_color = max(bg_colors, key=(lambda x : sum(x)))

    im = np.full(src.shape, bg_color)
    mask = src < [threshold, threshold, threshold]
    np.copyto(im, src, where=mask)
    return im

def change_line_space(src, factor):
    h, w = src.shape[:2]
    bg_colors = []
    for y in range(0, h, h // 10):
        for x in range(0, w, w // 10):
            bg_colors.append(src[y, x])
    bg_color = max(bg_colors, key=(lambda x : sum(x)))

    bg = np.full((1, w, 3), bg_color)
    im = bg
    n = 0
    for y in range(h):
        line = src[y, :, :]
        if ((line <= cv2.add(bg, 5)).all()
        and (line >= cv2.subtract(bg, 5)).all()):
            if n >= 0:
                n += 1
            else:
                im = np.concatenate((im, src[y + n:y, :, :]), axis=0)
                n = 0
        else:
            if n < 0:
                n -= 1
            elif n >= 3:
                interval_h = int(np.floor(factor * n))
                interval = np.full((interval_h, w, 3), bg_color)
                im = np.concatenate((im, interval), axis=0)
                n = -1
    if n >= 3:
        interval_h = int(np.floor(factor * n))
        interval = np.full((interval_h, w, 3), bg_color)
        im = np.concatenate((im, interval), axis=0)
    elif n < 0:
        im = np.concatenate((im, src[y + n:y, :, :]), axis=0)
    return im

def image_process(impath, outpath, argv):
    im = cv2.imread(impath)
    if im is None:
        raise FileNotFoundError(impath)

    operations = argv.split()
    for operation in operations:
        func, colon, arg = operation.partition(":")
        arg = float(arg)
        if func == "si":
            im = scale_image(im, arg)
        elif func == "col":
            im = enhance_color(im, arg)
        elif func == "con":
            im = enhance_contrast(im, arg)
        elif func == "sha":
            im = enhance_sharpness(im, arg)
        elif func == "rbg":
            im = remove_background(im, arg)
        elif func == "cbg":
            im = clear_background(im, arg)
        elif func == "cls":
            im = change_line_space(im, arg)
        elif func == "gau":
            im = gaussian_blur(im, arg)
        print(operation, end=" ")

    print("--", os.path.split(outpath)[1], "is generated.")
    cv2.imwrite(outpath, im)


rm_stains = " si:2 sha:2 rst:200 gau:0.5 si:0.5"
rm_stains_largen = " si:2 sha:2 si:2 rst:200 gau:0.5 si:0.5"
clear_bg = " sha:2 si:2 sha:2 si:2 rbg:25 rst:200 col:1.6 si:0.5"
clear_bg_blur = " si:2 sha:2 si:2 rbg:25 rst:200 col:1.6 si:0.5"
bolder = " sha:2 con:1.2"
clearer = " si:2 sha:2 cbg:220 con:1.2 gau:0.7 con:1.2"

src_dir = "C:/Users/hrzhe/Pictures/Calculus/"
argv = clearer + bolder + bolder + " cls:0.7"
out_suffix = argv.replace(":", "").replace(".", "")
out_suffix = "_"
# l = os.listdir(src_dir)
l = [i for i in range(1,8)]

for i in l:
    impath, outpath = get_paths(src_dir, str(i), ".jpg", out_suffix)
    impath, outpath = get_paths(src_dir, str(i), ".png", out_suffix)
    image_process(impath, outpath, argv)
