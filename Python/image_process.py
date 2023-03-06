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

def remove_background(src, delta):
    h, w = src.shape[:2]
    bg_color = np.array([255, 255, 255])
    for y in range(0, h, h // 10):
        for x in range(0, w, w // 10):
            if src[y, x][0] > delta:
                bg_color = (bg_color + src[y, x]) / 2
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
        elif func == "rst":
            im = remove_stains(im, arg)
        elif func == "gau":
            im = gaussian_blur(im, arg)
        print(operation, end=" ")
    
    print("--", os.path.split(outpath)[1], "is generated.")
    cv2.imwrite(outpath, im)






rm_stains = " si:2 sha:2 rst:200 gau:0.5 si:0.5"
rm_stains_largen = " si:2 sha:2 si:2 rst:200 gau:0.5 si:0.5"
clear_bg = " sha:2 si:2 sha:2 si:2 rbg:25 rst:200 col:1.6 si:0.5"
clear_bg_blur = " si:2 sha:2 si:2 rbg:25 rst:200 col:1.6 si:0.5"
bold = " gau:1.2 sha:10"
bold_more = " gau:1.5 sha:10"
clearer = " si:2 sha:2 si:2 rst:220 con:1.2 gau:0.7 con:1.2 si:0.5"

src_dir = "C:/Users/hrzhe/Pictures/Calculus/"
argv = clear_bg
out_suffix = "_"
out_suffix = argv.replace(":", "").replace(".", "")
# l = os.listdir(src_dir)
l = [1]

for i in l:
    impath, outpath = get_paths(src_dir, str(i), ".jpg", out_suffix)
    impath, outpath = get_paths(src_dir, str(i), ".png", out_suffix)
    image_process(impath, outpath, argv)




