import os
import cv2
import shutil
import struct
import sqlite3
import numpy as np
import pylab as plt
import read_write_model as model
import read_write_dense as dense
import export_to_visualsfm as visualsfm
from PIL import Image


def convert_sparse_model(input_path, output_path):
    cameras, images, points3D = model.read_model(path=input_path, ext=".bin") # type: ignore
    print("num_cameras:", len(cameras))
    print("num_images:", len(images))
    print("num_points3D:", len(points3D))
    model.write_model(cameras, images, points3D, path=output_path, ext=".txt")

def convert_depth_map(depth_map, min_depth_percentile=5, max_depth_percentile=95):
    if min_depth_percentile > max_depth_percentile:
        raise ValueError("min_depth_percentile should be less than or equal "
                         "to the max_depth_perceintile.")

    if not os.path.exists(depth_map):
        raise FileNotFoundError("File not found: {}".format(depth_map))

    depth_map = dense.read_array(depth_map)
    min_depth, max_depth = np.percentile(
        depth_map, [min_depth_percentile, max_depth_percentile])

    import matplotlib as mpl
    import matplotlib.cm as cm

    normalizer = mpl.colors.Normalize(vmin=min_depth, vmax=max_depth)
    mapper = cm.ScalarMappable(norm=normalizer, cmap='viridis')
    im = mapper.to_rgba(depth_map)
    im = (im * 255).astype(np.uint8) # type: ignore

    return Image.fromarray(im)

def convert_normal_map(normal_map):
    if not os.path.exists(normal_map):
        raise FileNotFoundError("File not found: {}".format(normal_map))

    normal_map = dense.read_array(normal_map)
    normal_map = normal_map / 2 + 0.5

    import matplotlib as mpl
    import matplotlib.cm as cm

    mapper = cm.ScalarMappable(cmap='viridis')
    im = mapper.to_rgba(normal_map)
    im = (im * 255).astype(np.uint8) # type: ignore
    Image.fromarray(im).show()

    return normal_map

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

def export_sift_and_matches(database_path, image_path, output_path,
                            min_num_matches=15,
                            binary_feature_files=False):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    try:
        os.makedirs(output_path)
    except:
        pass

    cameras = {}
    cursor.execute("SELECT camera_id, params FROM cameras;")
    for row in cursor:
        camera_id = row[0]
        params = np.frombuffer(row[1], dtype=np.double)
        cameras[camera_id] = params

    images = {}
    cursor.execute("SELECT image_id, camera_id, name FROM images;")
    for row in cursor:
        image_id = row[0]
        camera_id = row[1]
        image_name = row[2]
        print("Copying image", image_name)
        images[image_id] = (len(images), image_name)
        if not os.path.exists(os.path.join(output_path, image_name)):
            shutil.copyfile(os.path.join(image_path, image_name),
                            os.path.join(output_path, image_name))

    sift_name = 1413892435
    sift_version_v4 = 808334422
    sift_eof_marker = 1179600383

    for image_id, (image_idx, image_name) in images.items():
        print("Exporting key file for", image_name)
        base_name, ext = os.path.splitext(image_name)
        key_file_name = os.path.join(output_path, base_name + ".sift")
        if os.path.exists(key_file_name):
            continue

        cursor.execute("SELECT data FROM keypoints WHERE image_id=?;",
                       (image_id,))
        row = next(cursor)
        if row[0] is None:
            keypoints = np.zeros((0, 6), dtype=np.float32)
            descriptors = np.zeros((0, 128), dtype=np.uint8)
        else:
            keypoints = np.frombuffer(row[0], dtype=np.float32).reshape(-1, 6)
            cursor.execute("SELECT data FROM descriptors WHERE image_id=?;",
                           (image_id,))
            row = next(cursor)
            descriptors = np.frombuffer(row[0], dtype=np.uint8).reshape(-1, 128)

        if binary_feature_files:
            with open(key_file_name, "wb") as fid:
                fid.write(struct.pack("i", sift_name))
                fid.write(struct.pack("i", sift_version_v4))
                fid.write(struct.pack("i", keypoints.shape[0]))
                fid.write(struct.pack("i", 4))
                fid.write(struct.pack("i", 128))
                keypoints[:, :4].astype(np.float32).tofile(fid)
                descriptors.astype(np.uint8).tofile(fid)
                fid.write(struct.pack("i", sift_eof_marker))
        else:
            with open(key_file_name, "w") as fid:
                fid.write("%d %d\n" % (keypoints.shape[0],
                                       descriptors.shape[1]))
                for r in range(keypoints.shape[0]):
                    fid.write("%f %f 0 0 " % (keypoints[r, 0],
                                              keypoints[r, 1]))
                    fid.write(" ".join(map(str,
                                           descriptors[r].ravel().tolist())))
                    fid.write("\n")

    with open(os.path.join(output_path, "matches.txt"), "w") as fid:
        cursor.execute("SELECT pair_id, data FROM two_view_geometries "
                       "WHERE rows>=?;", (min_num_matches,))
        for row in cursor:
            pair_id = row[0]
            inlier_matches = np.frombuffer(row[1],
                                           dtype=np.uint32).reshape(-1, 2)
            image_id1, image_id2 = visualsfm.pair_id_to_image_ids(pair_id)
            image_name1 = images[image_id1][1]
            image_name2 = images[image_id2][1]
            fid.write("%s %s %d\n" % (image_name1, image_name2,
                                      inlier_matches.shape[0]))
            line1 = ""
            line2 = ""
            for i in range(inlier_matches.shape[0]):
                line1 += "%d " % inlier_matches[i, 0]
                line2 += "%d " % inlier_matches[i, 1]
            fid.write(line1 + "\n")
            fid.write(line2 + "\n")

    cursor.close()
    connection.close()


project_path = "C:/Users/hrzhe/Documents/Homework/CV/final_project/" \
               "21_cv_final_project/model_1/"
database_path = project_path + "database.db"
image_path = project_path + "images/"
model_path = project_path + "sparse/"
model_path = project_path + "new_model/"
model_path = project_path + "aligned_model/"

stereo_path = project_path + "dense/stereo/"
depth_path = stereo_path + "depth_maps/"
normal_path = stereo_path + "normal_maps/"
map_name = "1102_MMW_DJI_0076_00001.jpg.geometric.bin"

# convert_sparse_model(model_path, model_path)
# simplify_images_txt(model_path + "images.txt",
#                     model_path + "images_simplified.txt")

with open("C:/Users/hrzhe/Documents/Homework/CV/final_project/21_cv_final_project/2_dpt/test_list.txt") as fid:
    images = fid.readlines()
    images = [i[:-1] for i in images]

for i in images:
    img = convert_depth_map(depth_path + i + ".geometric.bin")
    img.convert("RGB").save("C:/Users/hrzhe/Documents/Homework/CV/final_project/21_cv_final_project/2_dpt/images/" + i)


