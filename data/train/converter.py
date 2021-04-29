"""
put this file in the same folder as the images to be converted
the output will be to a new folder within the folder
"""

import json
import os
from datetime import datetime

def convert_json(oldJ):
    newJ = dict()

    newJ['version'] = oldJ['version']
    newJ['last_modified'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    newJ['image_information'] = {
        'image_name': oldJ['imagePath'][15:], # "imagePath": "../Cell Photos/92.1 cells (092820, P11, 20X, S2).jpg"
        'image_height': oldJ['imageHeight'],
        'image_width': oldJ['imageWidth']
    }

    markup = []
    for shape in oldJ['shapes']:
        mark = {
            'shape': 5, # idk what 5 means, i'm just matching what they have
            'vertices': [{'x': point[0], 'y': point[1]} for point in shape['points']], # old is list of lists, new is list of dicts
            'bounding_box': {}, # computed below
            'object_label': shape['label'],
            'marker': 'DESKTOP-068MSQM', # ???
            'marker_comments': []
        }

        # theres probably a faster way to do this
        minX = maxX = shape['points'][0][0]
        minY = maxY = shape['points'][0][1]
        for point in shape['points']:
            if point[0] < minX:
                minX = point[0]
            elif point[0] > maxX:
                maxX = point[0]

            if point[1] < minY:
                minY = point[1]
            elif point[1] > maxY:
                maxY = point[1]

        mark['bounding_box'] = {
                "top_left": {
                    "x": minX,
                    "y": maxY
                },
                "top_right": {
                    "x": maxX,
                    "y": maxY
                },
                "bottom_left": {
                    "x": minX,
                    "y": minY
                },
                "bottom_right": {
                    "x": maxX,
                    "y": minY
                }
        }
        markup.append(mark)
    
    newJ['markup'] = markup

    newJ['completed_chips'] = '[]',
    newJ['last_viewed_chip'] = {
        'x': None,
        'y': None
    }
    newJ['percentage_complete'] = 0.0

    return newJ

if __name__ == '__main__':

    for filename in os.listdir('./'):
        print(filename)
        if filename.endswith('.json'):
            with open(filename) as file:
                oldJ = json.load(file)
                newJ = convert_json(oldJ)

                newfilename = 'convertOut/' + filename
                with open(newfilename, 'w') as newF:
                    json.dump(newJ, newF)

