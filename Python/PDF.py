import fitz
import re
import os
 
file_path = 'D:/E-books/C语言/C Primer Plus 第6版.pdf' # PDF 文件路径
dir_path = 'D:/E-books/C语言/C Primer Plus 第6版' # 存放图片的文件夹
 
def pdf2image1(path, pic_path):
    checkIM = r"/Subtype(?= */Image)"
    pdf = fitz.open(path)
    lenXREF = pdf._getXrefLength()
    count = 1
    for i in range(1, lenXREF):
        text = pdf._getXrefString(i)
        isImage = re.search(checkIM, text)
        if not isImage:
            continue
        pix = fitz.Pixmap(pdf, i)
        if pix.size < 10000: # 在这里添加一处判断一个循环
            continue # 不符合阈值则跳过至下
        new_name = f"img_{count}.png"

        if not os.path.exists(pic_path):  # 判断存放图片的文件夹是否存在
            os.makedirs(pic_path)  # 若图片文件夹不存在就创建

        pix.writePNG(os.path.join(pic_path, new_name))
        count += 1
        pix = None
 
pdf2image1(file_path, dir_path)