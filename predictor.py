import os
import sys
import random
import math
import re
import time
import numpy as np
import tensorflow as tf
import keras
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

ROOT_DIR = os.path.abspath(".")
sys.path.append(ROOT_DIR)
# Import Mask RCNN
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
import mrcnn.model as modellib
from mrcnn.model import log

#from samples.balloon
import balloon

config = balloon.BalloonConfig()
class InferenceConfig(config.__class__):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()

# Load validation dataset
dataset = balloon.BalloonDataset()
dataset.load_balloon(ROOT_DIR, "val")

# Must call before using the dataset
dataset.prepare()

def get_ax(rows=1, cols=1, size=16):
    """Return a Matplotlib Axes array to be used in
    all visualizations in the notebook. Provide a
    central point to control graph sizes.
    
    Adjust the size attribute to control how big to render images
    """
    _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
    return ax

with tf.device("/cpu:0"):
    model = modellib.MaskRCNN(mode="inference", model_dir=os.path.join(ROOT_DIR, "logs"),
                              config=config)

weights_path = os.path.join(ROOT_DIR, "mask_rcnn_balloon_0029.h5")
model.load_weights(weights_path, by_name=True)

image_id = 0

image, image_meta, gt_class_id, gt_bbox, gt_mask =\
    modellib.load_image_gt(dataset, config, image_id, use_mini_mask=False)
info = dataset.image_info[image_id]
print("image ID: {}.{} ({}) {}".format(info["source"], info["id"], image_id, 
                                       dataset.image_reference(image_id)))

# Run object detection
results = model.detect([image])

# Display results
ax = get_ax(1)
r = results[0]
print(len(r['class_ids']))
visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                            dataset.class_names, r['scores'], ax=ax,
                            title="Predictions")
# log("gt_class_id", gt_class_id)
# log("gt_bbox", gt_bbox)
# log("gt_mask", gt_mask)