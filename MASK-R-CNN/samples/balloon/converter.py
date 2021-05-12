"""
put this file outside directories named 'train' and 'val'
'train' and 'val' should contain jsons with the old json format
the output will be a new json in each folder
"""

import json
import os
from datetime import datetime

def convert_json(oldJ):
    newJ = dict()

    newJ['fileref'] = ""
    newJ['size'] = oldJ['imageWidth'] * oldJ['imageHeight']
    newJ['filename'] = oldJ['imagePath'][15:] # "imagePath": "../Cell Photos/92.1 cells (092820, P11, 20X, S2).jpg"
    newJ['base64_img_data'] = ""
    newJ['file_attributes'] = {}
    
    # create list of regions
    regions = []
    for shape in oldJ['shapes']:
        region = dict()
        region['shape_attributes'] = {
            'name': 'polygon',
            'all_points_x': [int(point[0]) for point in shape['points']],
            'all_points_y': [int(point[1]) for point in shape['points']]
        }
        region['region_attributes'] = {}
        regions.append(region)

    # ennumerate regions and put them in dictionary
    newJ['regions'] = {}
    for i in range(len(regions)):
        newJ['regions'][str(i)] = regions[i]

    return newJ

if __name__ == '__main__':

    output = dict()

    outfilename = 'via_region_data.json'

    for folder in ['val', 'train']:
        for filename in os.listdir(folder):
            if filename.endswith('.json') and filename :
                print("reading ", filename)
                with open(folder + '/' + filename) as file:
                    oldJ = json.load(file)
                    newJ = convert_json(oldJ)

                    outname = filename + str(newJ['size'])
                    output[outname] = newJ

        newfilename = folder + '/' + outfilename
        with open(newfilename, 'w') as newF:
            json.dump(output, newF)