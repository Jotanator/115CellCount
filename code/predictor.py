import os
import sys
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
ROOT_DIR = os.path.abspath("../")

# Import Mask RCNN
sys.path.append(os.path.join(ROOT_DIR, "MASK-R-CNN"))  # To find local version of the library
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
import mrcnn.model as modellib
from mrcnn.model import log

from samples.balloon import balloon

import jsonizer


# # Directory to save logs and trained model
MODEL_DIR = ROOT_DIR

# Path to Ballon trained weights
config = balloon.BalloonConfig()
BALLOON_DIR = os.path.join(ROOT_DIR, "data")

#########


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
    _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
    return ax

def predict(filename):
	jsonizer.jsonize(filename)
	config = InferenceConfig()
	# config.display()
	DEVICE = "/cpu:0"
	TEST_MODE = "inference"
	print(BALLOON_DIR)

	# Load validation Dataset
	dataset = balloon.BalloonDataset()
	dataset.load_balloon(BALLOON_DIR, "val")
	dataset.prepare()

	# print("Images: {}\nClasses: {}".format(len(dataset.image_ids), dataset.class_names))

	# Create model in inference mode
	with tf.device(DEVICE):
		model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
	weights_path = os.path.join(ROOT_DIR, "mask_rcnn_balloon_0030.h5")
	model.load_weights(weights_path, by_name=True)

	image_id = random.choice(dataset.image_ids)	
	image, image_meta, gt_class_id, gt_bbox, gt_mask =\
    	modellib.load_image_gt(dataset, config, image_id, use_mini_mask=False)
	info = dataset.image_info[image_id]
	#print("image ID: {}.{} ({}) {}".format(info["source"], info["id"], image_id, dataset.image_reference(image_id)))

	# Run object detection
	results = model.detect([image], verbose=1)
    # print(results)
	# Display results
	# ax = get_ax(1)
	r = results[0]
	visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                            	dataset.class_names, r['scores'],# ax=ax,
                            	title="Predictions")
	#log("gt_class_id", gt_class_id)
	#log("gt_bbox", gt_bbox)
	#log("gt_mask", gt_mask)
	return len(r['scores'])