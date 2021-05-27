from shutil import copyfile
import os
from PIL import Image


def jsonize(filename):
    # print(filename)
    width, height = Image.open(filename).size
    size = width * height
    copyfile(filename, os.path.abspath("../data/val/image.jpg"))
    file = open("../data/val/via_region_data.json", "w")
    file.truncate()
    file.close()

    file = open("../data/val/via_region_data.json", "a")
    file.write('{"image.json' + str(size))
    file.write('": {"fileref": "", "size": ' + str(size))
    file.write(
        ', "filename": "image.jpg", "base64_img_data": "", "file_attributes": {}, ')
    file.write('"regions": {"0": {"shape_attributes": {"name": "polygon", ')
    file.write(
        '"all_points_x": [0, 1, 2], "all_points_y": [0, 1, 2]}, "region_attributes": {}}}}}')
    file.close()
