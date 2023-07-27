import os
import cv2
import struct
import sqlite3
import numpy as np
import read_write_model as model
import read_write_dense as dense
import export_to_bundler as bundler
import export_to_visualsfm as visualsfm
import export_inlier_matches as eim
from PIL import Image


def get_cameras(database_path):
    cameras = {}
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute("SELECT camera_id, params FROM cameras;")
    for row in cursor:
        camera_id = row[0]
        params = np.frombuffer(row[1], dtype=np.double)
        cameras[camera_id] = params
    return cameras

def get_images(database_path):
    images = {}
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute("SELECT image_id, camera_id, name FROM images;")
    for row in cursor:
        image_id = row[0]
        camera_id = row[1]
        image_name = row[2]
        images[image_id] = (len(images), image_name)
    return images

def get_keypoints_and_desciptors(database_path):
    image_keypoints = {}
    image_descriptors = {}
    images = get_images(database_path)

    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    for image_id, (image_idx, image_name) in images.items():
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

        # keypoint[0] 为横轴上的坐标，keypoint[1] 为纵轴上的坐标
        keypoints = [cv2.KeyPoint(kpt[0], kpt[1], 1) for kpt in keypoints]

        image_keypoints[image_id] = keypoints
        image_descriptors[image_id] = descriptors
    return image_keypoints, image_descriptors

def get_matches(database_path):
    image_matches = {}
    _, image_descriptors = get_keypoints_and_desciptors(database_path)

    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute("SELECT pair_id, data FROM two_view_geometries "
                "WHERE rows>=?;", (15,))
    for row in cursor:
        pair_id = row[0]
        inlier_matches = np.frombuffer(row[1],
                                    dtype=np.uint32).reshape(-1, 2)
        image_id1, image_id2 = eim.pair_id_to_image_ids(pair_id)

        matches = []
        for i, (queryIdx, trainIdx) in enumerate(inlier_matches):
            des1 = image_descriptors[image_id1][queryIdx]
            des2 = image_descriptors[image_id2][trainIdx]
            distance = np.sqrt(np.sum(np.square(des1 - des2)))
            match = cv2.DMatch(queryIdx, trainIdx, i, distance)
            matches.append(match)

        image_matches[(image_id1, image_id2)] = matches
    return image_matches


def draw_matches(database_path, image_path, image_id1, image_id2):
    images = get_images(database_path)
    image_keypoints, _ = get_keypoints_and_desciptors(database_path)
    image_matches = get_matches(database_path)

    if (image_id1, image_id2) in image_matches.keys():
        matches = image_matches[(image_id1, image_id1)]
    else:
        print("No such matches.")
        return

    im1 = cv2.imread(image_path + images[image_id1][1])
    im2 = cv2.imread(image_path + images[image_id2][1])
    kpts1 = image_keypoints[image_id1]
    kpts2 = image_keypoints[image_id2]

    out = cv2.drawMatches(im1, kpts1, im2, kpts2, matches, None)
    return out

def draw_good_matches(database_path, image_path, output_path, threshold):
    images = get_images(database_path)
    image_keypoints, _ = get_keypoints_and_desciptors(database_path)
    image_matches = get_matches(database_path)

    for i, item in enumerate(image_matches.items()):
        (image_id1, image_id2), matches = item
        if len(matches) > threshold:
            im1 = cv2.imread(image_path + images[image_id1][1])
            im2 = cv2.imread(image_path + images[image_id2][1])
            kpts1 = image_keypoints[image_id1]
            kpts2 = image_keypoints[image_id2]

            out = cv2.drawMatches(im1, kpts1, im2, kpts2, matches, None)
            cv2.imwrite(output_path + str(i).zfill(4) + ".jpg", out)


def convert_sparse_model(input_path, output_path):
    cameras, images, points3D = model.read_model(path=input_path, ext=".bin") # type: ignore
    print("num_cameras:", len(cameras))
    print("num_images:", len(images))
    print("num_points3D:", len(points3D))
    model.write_model(cameras, images, points3D, path=output_path, ext=".txt")

def convert_depth_map(depth_map, to_PIL=False,
                      min_depth_percentile=5, max_depth_percentile=95):
    if min_depth_percentile > max_depth_percentile:
        raise ValueError("min_depth_percentile should be less than or equal "
                         "to the max_depth_perceintile.")

    if not os.path.exists(depth_map):
        raise FileNotFoundError("File not found: {}".format(depth_map))

    depth_map = dense.read_array(depth_map)
    min_depth, max_depth = np.percentile(
        depth_map, [min_depth_percentile, max_depth_percentile])
    depth_map[depth_map < min_depth] = min_depth
    depth_map[depth_map > max_depth] = max_depth

    if to_PIL:
        import matplotlib as mpl
        import matplotlib.cm as cm

        mapper = cm.ScalarMappable(cmap="viridis")
        depth_map = mapper.to_rgba(depth_map)
        depth_map = (depth_map * 255).astype(np.uint8) # type: ignore
        depth_map = Image.fromarray(depth_map)

    return depth_map

def convert_normal_map(normal_map, to_PIL=False):
    if not os.path.exists(normal_map):
        raise FileNotFoundError("File not found: {}".format(normal_map))

    normal_map = dense.read_array(normal_map)

    if to_PIL:
        import matplotlib.cm as cm

        normal_map = normal_map / 2 + 0.5
        mapper = cm.ScalarMappable(cmap="viridis")
        normal_map = mapper.to_rgba(normal_map)
        normal_map = (normal_map * 255).astype(np.uint8) # type: ignore
        normal_map = Image.fromarray(normal_map)

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

def export_sifts(database_path, output_path, binary_feature_files=False):
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
        images[image_id] = (len(images), image_name)

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

def export_matches(database_path, output_path, min_num_matches=15):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    try:
        os.makedirs(output_path)
    except:
        pass

    images = {}
    cursor.execute("SELECT image_id, camera_id, name FROM images;")
    for row in cursor:
        image_id = row[0]
        camera_id = row[1]
        image_name = row[2]
        images[image_id] = (len(images), image_name)

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

    with open(os.path.join(output_path, "matches.init.txt"), "w") as fid:
        cursor.execute("SELECT pair_id, data FROM two_view_geometries "
                       "WHERE rows>=?;", (min_num_matches,))
        for row in cursor:
            pair_id = row[0]
            inlier_matches = np.frombuffer(row[1],
                                           dtype=np.uint32).reshape(-1, 2)
            image_id1, image_id2 = bundler.pair_id_to_image_ids(pair_id)
            image_idx1 = images[image_id1][0]
            image_idx2 = images[image_id2][0]
            fid.write("%d %d\n%d\n" % (image_idx1, image_idx2,
                                       inlier_matches.shape[0]))
            for i in range(inlier_matches.shape[0]):
                fid.write("%d %d\n" % (inlier_matches[i, 0],
                                       inlier_matches[i, 1]))

    cursor.close()
    connection.close()


def main():
    project_path = "C:/Users/hrzhe/Documents/Homework/CV/final_project/" \
                   "21_cv_final_project/model_3/"
    database_path = project_path + "database.db"
    image_path = project_path + "images/"
    model_path = project_path + "sparse/"
    model_path = project_path + "aligned_model/"
    model_path = project_path + "new_model/"

    stereo_path = project_path + "dense/stereo/"
    depth_path = stereo_path + "depth_maps/"
    normal_path = stereo_path + "normal_maps/"
    map_name = "1102_MMW_DJI_0076_00001.jpg.geometric.bin"


    # convert_sparse_model(model_path, model_path)
    # simplify_images_txt(model_path + "images.txt",
    #                     model_path + "images_simplified.txt")

    # export_sifts(database_path, project_path + "features")
    # export_matches(database_path, project_path + "features")

    # draw_good_matches(database_path, image_path
    #                   project_path + "match_images/ ", 100)

if __name__ == "__main__":
    main()
