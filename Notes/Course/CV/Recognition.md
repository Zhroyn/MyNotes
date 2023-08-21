
- [Recognition](#recognition)
  - [Semantic Segmentation](#semantic-segmentation)
  - [Object Detection](#object-detection)
    - [R-CNN](#r-cnn)
    - [Fast R-CNN](#fast-r-cnn)
    - [Faster R-CNN](#faster-r-cnn)
    - [Single-Stage Object Detection](#single-stage-object-detection)
  - [Instance Segmentation](#instance-segmentation)
  - [Human Pose Estimation](#human-pose-estimation)
    - [Top-down Method](#top-down-method)
    - [Bottom-up Method](#bottom-up-method)
  - [Other Tasks](#other-tasks)







## Recognition
### Semantic Segmentation
To realize semantic segmentation, we can use **fully convolutional network** to make predictions all at once, converting the input with size $3 \times H \times W$ to scores with size $C \times H \times W$, and then using argmax to get predictions with size $H \times W$. The loss function is **per-pixel cross entropy**.

To make the receptive field expand faster, we can use pooling or strided conv to realize **downsampling**, and then use interpolation or transposed conv to realize **upsampling**

Moreover, we can use **skip connection** between downsampling and
upsampling stages. We call such network as **U-Net**.

To overcome the poor localization property of the final output, we can combine the responses at the final layer with a fully connected **Conditional Random Field (CRF)**. That is
$$E(x) = \sum_i \theta_i(x_i) + \sum_{ij}\theta_{ij}(x_i, x_j)$$

The unary potential is
$$\theta_i(x_i) = -\log P(x_i)$$

The pairwise potential is
$$
\begin{aligned}
  \theta_{ij}(x_i, x_j) = \mu(x_i, x_j) & \left[ w_1 \exp\left( - \frac{\left\| p_i - p_j \right\|^2}{2\sigma_\alpha^2} - \frac{\left\| I_i - I_j \right\|^2}{2\sigma_\beta^2} \right) \right. \\
  & \left. + w_2 \exp\left( - \frac{\left\| p_i - p_j \right\|^2}{2\sigma_\gamma^2} \right) \right] \\
\end{aligned}
$$

One of evaluation metric of semantic segmentation is **Per-pixel Intersection-over-union (IoU)**, which is
$$\text{IoU} = \frac{\text{The area of intersection}}{\text{The area of union}}$$







<br>

### Object Detection
The input is a RGB image, the output is a set of bounding boxes that denote objects.

The **bounding box (bbox)** contains
- Class label
- Location (x, y)
- Size (w, h)

The evaluation metric of object detection can be IoU.

<br>

#### R-CNN
The procedures of **Regions with CNN features (R-CNN)** are
1. Firstly, run region proposal method to compute **Regions of Interest (Rols)**
2. Then, resize each region to 224x224 and run through CNN, predict class scores and bbox
3. Finally, select a subset of region proposals to output by **non-max suppression**. That is, firstly select the highest-scoring box, and then eliminate lower-scoring boxes with IoU > threshold

<br>

#### Fast R-CNN
The procedures of Fast R-CNN are
1. Run whole image through backbone network like AlexNet, ResNet, get the feature map of the image
2. Rol Pooling: Get Rols from a proposal method, and then use them to crop and resize feature map to the same size
3. Run through per-region network, predict class scores and bbox

<br>

#### Faster R-CNN
Faster R-CNN uses **Region Proposal Network (RPN)** to get Rols, that is,
1. Firstly, suppose $K$ anchor boxes of fixed size at each point in the feature map, thus we can get $K \times H \times W$ anchor boxes at all
2. Then run through the network, and get the scores and the offset coordinates for each anchor boxes
3. Sort all $K \times H \times W$ boxes by their scores, and take the highest ones as Rols

<br>

#### Single-Stage Object Detection
RCNN, Fast RCNN and Faster RCNN are all two-stage object detection. For faster computation, there are also single-stage object detection, such as YOLO, SSD, etc.

**You Only Look Once (YOLO)** firstly split image into $S \times S$ grids. Then for each grid, it predicts $B$ bounding boxes, which contains its location $(x, y)$, size $(w, h)$, and its confidence. It also predicts its probabilities for $C$ categories. So the size of the output of CNN is $S \times S \times (B \times 5 + C)$.








<br>

### Instance Segmentation
One method of instance segmentation is to firstly perform object detection, and then predict a segmentation mask for each object.

Beyond instance segmentation there is also **panoptic segmentation**, which labels all pixels in the image.







<br>

### Human Pose Estimation
We can represent the pose of a human by locating a set of **keypoints**, such as nose, eyes, ears, shoulders, elbows, wrists, hips, knees and ankles, which sum up to 17 keypoints.

<br>

#### Top-down Method
Top-down method detect humans firstly and then detect keypoints in each bbox. Its performance is usually better.

For each human, it outputs a single heatmap for each type of joint, and then choose the location with the highest value as the coordinate of the keypoint.



<br>

#### Bottom-up Method
Bottom-up method detect keypoints firstly and then group keypoints to form humans. It's usually faster.

OpenPose firstly generates **part confidence maps (heatmaps)** and **part affinity fields (PAF)** from the input images, and then link parts based on part affinity fields.







<br>

### Other Tasks
- **Video Classification**: Recognize actions
- **Temporal Action Localization**: Given a long untrimmed video sequence, identify frames corresponding to different actions
- **Spatial-temporal Detection**: Given a long untrimmed video, detect all the people in space and time and classify the activities they are performing
- **Multi-object Tracking**: Identify and track objects belonging to one or more categories without any prior knowledge about the appearance and number of targets.



