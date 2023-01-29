import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

def remove_stains(impath, outpath):
    im = cv2.imread(impath)
    if im is None:
        print("File open failed :", impath)
    else:
        h, w = im.shape[:2]
        for y in range(h):
            for x in range(w):
                if (int(im[y, x, 0])
                  + int(im[y, x, 1])
                  + int(im[y, x, 1]) > 420):
                    im[y, x] = 255
        im = cv2.GaussianBlur(im, (3, 3), 0, 0)
        cv2.imwrite(outpath, im)

def change_background(impath, outpath):
    im = cv2.imread(impath)
    if im is None:
        print("File open failed :", impath)
    else:
        h, w = im.shape[:2]
        bg_color = im[10, 10].copy()
        print(bg_color)
        delta = 25
        for y in range(h):
            for x in range(w):
                b, g, r = im[y, x]
                if (abs(int(b) - int(bg_color[0])) <= delta
                and abs(int(g) - int(bg_color[1])) <= delta
                and abs(int(r) - int(bg_color[2])) <= delta):
                    im[y, x] = 255
        im = cv2.GaussianBlur(im, (3, 1), 0, 0)
        im = Image.fromarray(im[:, :, ::-1])
        enh_sha = ImageEnhance.Sharpness(im)
        im = enh_sha.enhance(2.0)
        im.save(outpath)


# remove_stains("C:/Users/hrzhe/Pictures/Calculus/500cef37a1fb8886d4c4ef664877a86.jpg",
#             "C:/Users/hrzhe/Pictures/Calculus/out.jpg")

change_background("C:/Users/hrzhe/Pictures/Calculus/2.png", 
                "C:/Users/hrzhe/Pictures/Calculus/gau20.jpg")