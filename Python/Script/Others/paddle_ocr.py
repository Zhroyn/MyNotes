import os
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr # type: ignore

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
src_path = "C:/Users/hrzhe/Pictures/OCR/"
font_path = "doc/fonts/simfang.ttf"
font_path = "C:/Users/hrzhe/AppData/Local/Microsoft/Windows/Fonts/LXGWWenKaiMono-Regular.ttf"

# 可用`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="japan")

def show_result(result):
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)
        print()

def draw_result(img_path, res_path, font_path, result):
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path=font_path)
    im_show = Image.fromarray(im_show)
    im_show.save(res_path)

img_path = src_path + "008.png"
res_path = src_path + "result_10.png"
result = ocr.ocr(img_path, cls=True)
show_result(result)
draw_result(img_path, res_path, font_path, result[0])

