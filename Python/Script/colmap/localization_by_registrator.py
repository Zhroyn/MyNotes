import os
import read_write_model

def convert_model(input_path, output_path):
    cameras, images, points3D = read_write_model.read_model(path=input_path, ext=".bin") # type: ignore
    print("num_cameras:", len(cameras))
    print("num_images:", len(images))
    print("num_points3D:", len(points3D))
    read_write_model.write_model(cameras, images, points3D, path=output_path, ext=".txt")

def simplify_images_txt(input_path, output_path):
    with open(input_path, "r") as fid:
        lines = fid.readlines()
        image_num = (len(lines) - 4) // 2
        for i in range(image_num):
            lines.pop(5 + i)
    with open(output_path, "w") as fid:
        for line in lines[:4]:
            fid.write(line)
        for line in lines[4:]:
            fid.write(line + "\n")

project_path = "C:/Users/hrzhe/Documents/Homework/CV/final_project/" \
               "21_cv_final_project/model_4/"
database_path = project_path + "database.db"
image_path = project_path + "images/"
model_path = project_path + "sparse/"

vocab_tree_path = "D:/Dataset/COLMAP/vocab_tree_flickr100K_words32K.bin"
image_list_path = project_path + "image-list.txt"
new_image_path = project_path + "new_images/"
new_model_path = project_path + "new_model/"


if not os.path.exists(new_image_path):
    os.mkdir(new_image_path)
if not os.path.exists(new_model_path):
    os.mkdir(new_model_path)

os.system("colmap feature_extractor"
          " --ImageReader.camera_model PINHOLE"
          " --database_path " + database_path +
          " --image_path " + image_path +
          " --image_list_path " + image_list_path)

matcher = "exh"
if matcher == "exh":
    os.system("colmap exhaustive_matcher"
            " --database_path " + database_path)
elif matcher == "voc":
    os.system("colmap vocab_tree_matcher"
            " --database_path " + database_path + 
            " --VocabTreeMatching.vocab_tree_path " + vocab_tree_path +
            " --VocabTreeMatching.match_list_path " + image_list_path)

os.system("colmap image_registrator"
          " --database_path " + database_path +
          " --input_path " + model_path +
          " --output_path " + new_model_path)

convert_model(new_model_path, new_model_path)
simplify_images_txt(new_model_path + "images.txt",
                    new_model_path + "images_before_BA.txt")

os.system("colmap bundle_adjuster"
          " --input_path " + new_model_path +
          " --output_path " + new_model_path)

convert_model(new_model_path, new_model_path)
simplify_images_txt(new_model_path + "images.txt",
                    new_model_path + "images_after_BA.txt")

