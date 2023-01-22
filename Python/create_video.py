import cv2
import os

def create_video(filepath, fourcc, fps, size,
                 impath, imnum=0):
    codec = cv2.VideoWriter_fourcc(*fourcc)
    output = cv2.VideoWriter(filepath, codec, fps, size)

    os.chdir(impath)
    if imnum > 0:
        images = os.listdir()[:imnum]
    else:
        images = os.listdir()

    for imname in images:
        im = cv2.imread(imname)
        output.write(im)
    
    output.release()


dest = "C:/Users/hrzhe/Videos/jntm/"
fps = 8
size = (1920, 1080)
impath = dest + "line/fps"

create_video(dest + "aaa03.mp4", "X264", fps, size, impath, 100)



