from colmap import *
 
if __name__ == '__main__':
    images = read_images_binary('C:/Users/hrzhe/Documents/Homework/CV/final_project/21_cv_final_project/model_1/dense/sparse/images.bin')
 
    if len(images) == 0:
        mean_observations = 0
    else:
        mean_observations = sum((len(img.point3D_ids) for _, img in images.items()))/len(images)
    HEADER = "# Image list with two lines of data per image:\n" + \
             "#   IMAGE_ID, QW, QX, QY, QZ, TX, TY, TZ, CAMERA_ID, NAME\n" + \
             "#   POINTS2D[] as (X, Y, POINT3D_ID)\n" + \
             "# Number of images: {}, mean observations per image: {}\n".format(len(images), mean_observations)
 
    with open('C:/Users/hrzhe/Documents/Homework/CV/final_project/21_cv_final_project/model_1/dense/sparse/images.txt', "w") as fid:
        fid.write(HEADER)
        for _, img in images.items():
            image_header = [img.id, *img.qvec, *img.tvec, img.camera_id, img.name]
            first_line = " ".join(map(str, image_header))
            fid.write(first_line + "\n\n")