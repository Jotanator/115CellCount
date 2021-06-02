import jsonizer
import os
import sys
import inspect
import random
import math
import re
import time
import numpy as np
import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# Root directory of the project
ROOT_DIR = os.path.join(os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe()))), "..")
# To find local version of the library
sys.path.append(os.path.join(ROOT_DIR, "MASK-R-CNN"))


# Import Mask RCNN
import balloon
from mrcnn.model import log
import mrcnn.model as modellib
from mrcnn.visualize import display_images
from mrcnn import visualize
from mrcnn import utils


# Directory to save logs and trained model
MODEL_DIR = ROOT_DIR
# Path to Ballon trained weights
config = balloon.BalloonConfig()
BALLOON_DIR = os.path.join(ROOT_DIR, ".")


class InferenceConfig(config.__class__):
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


def get_ax(rows=1, cols=1, size=16):
    """Return a Matplotlib Axes array to be used in
    all visualizations in the notebook. Provide a
    central point to control graph sizes.

    Adjust the size attribute to control how big to render images
    """
    _, ax = plt.subplots(rows, cols, figsize=(size * cols, size * rows))
    return ax


# Function to predict on an inputted filename
def predict(filename):
    # Prepare json and image.jpg
    jsonizer.jsonize(filename)
    # Setup config
    config = InferenceConfig()
    # Use CPU for local running
    DEVICE = "/cpu:0"
    # Use inference mode
    TEST_MODE = "inference"
    # Load validation dataset
    dataset = balloon.BalloonDataset()
    dataset.load_balloon(BALLOON_DIR, "val")
    dataset.prepare()
    # Create model in inference mode
    with tf.device(DEVICE):
        model = modellib.MaskRCNN(
            mode="inference",
            model_dir=MODEL_DIR,
            config=config)
    # Set path to pretrained weights
    weights_path = os.path.join(ROOT_DIR, "mask_rcnn_balloon_0030.h5")
    # Load pretrained weights
    model.load_weights(weights_path, by_name=True)
    # Get the image from the dataset
    image_id = 0
    # Load the image
    image, image_meta, gt_class_id, gt_bbox, gt_mask =\
        modellib.load_image_gt(dataset, config, image_id, use_mini_mask=False)
    info = dataset.image_info[image_id]
    # Run object detection
    results = model.detect([image], verbose=1)
    # Get results
    r = results[0]
    visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'],
        dataset.class_names, r['scores'],  # ax=ax,
        title="Predictions on " + filename)
    # Return the cell count
    return len(r['scores'])
