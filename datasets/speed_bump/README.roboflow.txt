
detecting speed bumps - v4 marked speed bumps
==============================

This dataset was exported via roboflow.ai on April 5, 2022 at 10:19 PM GMT

It includes 593 images.
Speed-bumps are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise
* Randomly crop between 0 and 37 percent of the image


