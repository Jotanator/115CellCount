from shutil import copyfile
import os
import inspect
from PIL import Image


# Function to prepare json and image.jpg
def jsonize(filename):
    # Get image size
    width, height = Image.open(filename).size
    size = width * height
    VAL_DIR = os.path.join(os.path.dirname(
        os.path.abspath(inspect.getfile(inspect.currentframe()))), "../val")
    # Copy file to image.jpg in our folder
    copyfile(filename, os.path.join(VAL_DIR, "image.jpg"))
    # Open json file in write mode
    file = open(os.path.join(VAL_DIR, "via_region_data.json"), "w")
    # Delete contents of json file
    file.truncate()
    # Close the json file
    file.close()
    # Reopen the json file in append mode
    file = open(os.path.join(VAL_DIR, "via_region_data.json"), "a")
    # Write the default json text but with the actual size of the image
    file.write(
        '{"image.json' + str(size) + '": {"fileref": "", "size": ' +
        str(size) + ', "filename": "image.jpg", "base64_img_data": "",'
        '"file_attributes": {}, "regions": {"0": {"shape_attributes":'
        ' {"name": "polygon", "all_points_x": [0, 1, 2], "all_points_y":'
        ' [0, 1, 2]}, "region_attributes": {}}}}}')
    # Close the image
    file.close()
