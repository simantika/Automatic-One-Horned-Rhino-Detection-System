# Automatic-One-Horned-Rhino-Detection-System

# Requirements

Python 3.8 or later with all requirements.txt dependencies installed, including torch>=1.6. To install run:

$ pip install -r requirements.txt

# Training

Start Training: python3 train.py to begin training after downloading One-Horned Rhino dataset. Each epoch trains on 4649 images from the training set, and tests on 418 images from the testing set.

Resume Training: python3 train.py --resume to resume training from weights/last.pt.

Plot Training: from utils import utils; utils.plot_results()

# Dataset

It will be available soon.

# Image Augmentation

datasets.py applies OpenCV-powered (https://opencv.org/) augmentation to the input image. We use a mosaic dataloader to increase image variability during training.

# Inference

python3 detect.py --source ...

Image: --source file.jpg
Video: --source file.mp4
Directory: --source dir/
Webcam: --source 0
