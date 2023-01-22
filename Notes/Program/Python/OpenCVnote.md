<!-- TOC -->

- [Display](#display)
        - [Open and Close](#open-and-close)
        - [Keys](#keys)
- [Image](#image)
        - [Open and Save](#open-and-save)
- [Video](#video)
    - [VideoCapture](#videocapture)
        - [Open and Release](#open-and-release)
        - [Capture frame](#capture-frame)
        - [VideoCaptureProperties](#videocaptureproperties)
    - [VideoWriter](#videowriter)
        - [Create and Release](#create-and-release)
        - [fourcc](#fourcc)

<!-- /TOC -->






## Display
#### Open and Close
```py
namedWindow(winname[, flags]) -> None
    If a window with the same name already exists, the function does nothing.
    flags : 
    WINDOW_NORMAL or WINDOW_AUTOSIZE: WINDOW_NORMAL enables you to resize the
            window, whereas WINDOW_AUTOSIZE adjusts automatically the window 
            size to fit the displayed image, and you cannot change the window 
            size manually.
    WINDOW_FREERATIO or WINDOW_KEEPRATIO: WINDOW_FREERATIO adjusts the image
            with no respect to its ratio, whereas WINDOW_KEEPRATIO keeps the 
            image ratio.
    WINDOW_GUI_NORMAL or WINDOW_GUI_EXPANDED: WINDOW_GUI_NORMAL is the old way 
            to draw the window without statusbar and toolbar, whereas 
            WINDOW_GUI_EXPANDED is a new enhanced GUI.
    By default, flags == WINDOW_AUTOSIZE | WINDOW_KEEPRATIO | WINDOW_GUI_EXPANDED


imshow(winname, mat) -> None
    If the window was not created before this function, it is assumed creating 
    a window with cv::WINDOW_AUTOSIZE.
    This function should be followed by a call to cv::waitKey or cv::pollKey to 
    perform GUI housekeeping tasks that are necessary to actually show the given 
    image and make the window respond to mouse and keyboard events. Otherwise, 
    it won't display the image and the window might lock up.

destroyWindow(winname) -> None
    Destroy the window with the given name.

destroyAllWindows() -> None
    Destroy all of the opened HighGUI windows.
```

#### Keys
```py
waitKey([, delay]) -> retval
    Wait for a key event infinitely or for delay milliseconds if it is positive.
    It returns the code of the pressed key or -1 if no key was pressed before 
    the specified time had elapsed.
```






## Image
#### Open and Save
```py
imread(filename[, flags]) -> retval
    If the image cannot be read, the function returns an empty matrix.
    The function determines the type of image by content, not by file extension.
    flags : The default value is cv2.IMREAD_COLOR.
        cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency 
                          of image will be neglected. Its value is 1.
        cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. 
                              Its value is 0.
        cv2.IMREAD_UNCHANGED: It specifies to load an image as such including 
                              alpha channel. Its value is -1.

imwrite(filename, img[, params]) -> retval
    Return true if image is saved successfully.
    The image format is chosen based on the filename extension.
```







## Video
### VideoCapture
#### Open and Release
```py
VideoCapture(filename[, apiPreference]) -> retval
open(filename[, apiPreference]) -> retval
    Opens a video file or a capturing device or an IP video stream for video 
    capturing.
    Parameters are same as the constructor VideoCapture.
    Return `true` if the file has been successfully opened.

isOpened() -> retval
    If the previous call to VideoCapture constructor or VideoCapture::open() 
    succeeded, the method returns true.

release() -> None
    Close video file or capturing device.
    The method is automatically called by subsequent VideoCapture::open and 
    by VideoCapture destructor.
```

#### Capture frame
```py
read([, image]) -> retval, image
    The video frame is returned in image.
    If no frames has been grabbed the image will be empty.
    Return false if no frames has been grabbed

grab() -> retval
    The method/function grabs the next frame from video file or camera and 
    returns true (non-zero) in the case of success.

retrieve([, image[, flag]]) -> retval, image
    The method decodes and returns the just grabbed frame. If no frames has 
    been grabbed, the method returns false and the function returns an empty 
    image.
    [out] image : the video frame is returned here. If no frames has been 
    grabbed the image will be empty.
    flag : it could be a frame index or a driver specific flag
```

#### VideoCaptureProperties
```py
get(propId) -> retval
    Return the specified VideoCapture property.

set(propId, value) -> retval
    Set a property in the VideoCapture.
```
- `cv.CAP_PROP_POS_MSEC` Current position of the video file in milliseconds.
- `cv.CAP_PROP_POS_FRAMES` 0-based index of the frame to be decoded/captured next.
- `cv.CAP_PROP_POS_AVI_RATIO` Relative position of the video file: 0=start of the film, 1=end of the film.
- `cv.CAP_PROP_FRAME_WIDTH` Width of the frames in the video stream.
- `cv.CAP_PROP_FRAME_HEIGHT` Height of the frames in the video stream.
- `cv.CAP_PROP_FPS` Frame rate.
- `cv.CAP_PROP_FOURCC` 4-character code of codec.
- `cv.CAP_PROP_FRAME_COUNT` Number of frames in the video file.
- `cv.CAP_PROP_FORMAT` Format of the Mat objects returned by VideoCapture::retrieve(). Set value -1 to fetch undecoded RAW video streams (as Mat 8UC1).
- `cv.CAP_PROP_MODE` Backend-specific value indicating the current capture mode.
- `cv.CAP_PROP_BRIGHTNESS` Brightness of the image (only for those cameras that support).
- `cv.CAP_PROP_CONTRAST` Contrast of the image (only for cameras).
- `cv.CAP_PROP_SATURATION` Saturation of the image (only for cameras).
- `cv.CAP_PROP_HUE` Hue of the image (only for cameras).
- `cv.CAP_PROP_GAIN` Gain of the image (only for those cameras that support).
- `cv.CAP_PROP_EXPOSURE` Exposure (only for those cameras that support).
- `cv.CAP_PROP_CONVERT_RGB` Boolean flags indicating whether images should be converted to RGB.




### VideoWriter
#### Create and Release
```py
VideoWriter(filename, fourcc, fps, frameSize, isColor=ture) -> retval
open(filename, fourcc, fps, frameSize, isColor=ture) -> retval
    Initializes or reinitializes video writer.
    The method opens video writer. Parameters are the same as in the constructor.
    Return `true` if video writer has been successfully initialized

    filename : Name of the output video file.
    fourcc : 4-character code of codec used to compress the frames.
             If fourcc is -1, it will pop up the codec selection dialog.
    fps	: Framerate of the created video stream.
    frameSize : Size of the video frames.
    isColor : If it is not zero, the encoder will expect and encode color frames,
              otherwise it will work with grayscale frames.


isOpened() -> retval
    Return true if video writer has been successfully initialized.

write(image) ->	None
    Writes the next video frame.
    image : In general, color images are expected in BGR format.
            It must have the same size as has been specified when opening the 
            video writer.

release() -> None
    Close the video writer.
    The method is automatically called by subsequent VideoWriter::open and 
    by the VideoWriter destructor.
```

#### fourcc
**AVI**
- `I420`
  - `rawvideo (I420 / 0x30323449)`
  - YUV video stored in planar 4:2:0 format
  - largest
- `H264` `h264` `X264` `x264` `avc1`
  - `h264 (Constrained Baseline) (H264 / 0x34363248)`
  - H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10
  - larger
- `MJPG` `AVI1` `AVI2`
  - `mjpeg (Baseline) (MJPG / 0x47504A4D)`
  - Motion JPEG
  - smaller
- `FMP4` `XVID` `DIVD`
  - `mpeg4 (Simple Profile) (FMP4 / 0x34504D46)`
  - MPEG-4 part 2
  - smallest

**MP4**
- `avc1` `avc3`
  - `h264 (Constrained Baseline) (avc1 / 0x31637661)`
  - H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10
  - larger
- `mp4v`
  - `mpeg4 (Simple Profile) (mp4v / 0x7634706D)`
  - MPEG-4 part 2
  - smaller









