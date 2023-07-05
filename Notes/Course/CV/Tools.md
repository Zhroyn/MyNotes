
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Open3d](#open3d)
- [Colmap](#colmap)
  - [自动重建](#自动重建)
  - [特征提取（SIFT）](#特征提取sift)
  - [特征匹配](#特征匹配)
  - [稀疏重建](#稀疏重建)
  - [稠密重建](#稠密重建)

<!-- /code_chunk_output -->








## Open3d
- `o3d.io.read_point_cloud(filename, format='auto', ...)` 读取点云文件
  - `pcd = o3d.io.read_point_cloud("a.txt", format="xyz")`
  - `pcd = o3d.io.read_point_cloud("a.ply")`
<br>

- `o3d.visualization.draw_geometries(geometry_list, window_name='Open3D', width=1920, height=1080, left=50, top=50)` 可视化点云
  - `o3d.visualization.draw_geometries([pcd])`







<br>

## Colmap
### 自动重建
```powershell
colmap automatic_reconstructor `
    --database_path $DATASET_PATH/database.db `
    --image_path $DATASET_PATH/images
```

<br>

### 特征提取（SIFT）
```powershell
colmap feature_extractor `
    --database_path $DATASET_PATH/database.db `
    --image_path $DATASET_PATH/images
```

<br>

### 特征匹配
```powershell
colmap exhaustive_matcher `
    --database_path $DATASET_PATH/database.db
```

<br>

### 稀疏重建
```powershell
mkdir $DATASET_PATH/sparse
colmap mapper `
    --database_path $DATASET_PATH/database.db `
    --image_path $DATASET_PATH/images `
    --output_path $DATASET_PATH/sparse
```

<br>

### 稠密重建
```powershell
# 重新校准图片
mkdir $DATASET_PATH/dense
colmap image_undistorter `
    --image_path $DATASET_PATH/images `
    --input_path $DATASET_PATH/sparse/0 `
    --output_path $DATASET_PATH/dense `
    --output_type COLMAP `
    --max_image_size 2000

# Stero算法（PatchMatch）
colmap patch_match_stereo `
    --workspace_path $DATASET_PATH/dense `
    --workspace_format COLMAP `
    --PatchMatchStereo.geom_consistency true

# Stereo Fusion算法
colmap stereo_fusion `
    --workspace_path $DATASET_PATH/dense `
    --workspace_format COLMAP `
    --input_type geometric `
    --output_path $DATASET_PATH/dense/fused.ply

# 泊松重建
colmap poisson_mesher `
    --input_path $DATASET_PATH/dense/fused.ply `
    --output_path $DATASET_PATH/dense/meshed-poisson.ply

# 德劳内重建
colmap delaunay_mesher `
    --input_path $DATASET_PATH/dense `
    --output_path $DATASET_PATH/dense/meshed-delaunay.ply
```

