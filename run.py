#!/usr/bin/env python3

import numpy as np
import sys
import cv2
import imageio
from PIL import Image, ImageDraw
from argparse import ArgumentParser

import colors

TRANSPARENCY_THRESHOLD = 64

# read sticker image
# keep the alpha channel and convert to RGBA color space
def read_sticker(path):
    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
    return image

def get_cropped_images(image):
    height = image.shape[0]
    width = image.shape[1]

    unit_height = int(height/args.row)
    unit_width = int(width/args.column)
    for y in range(0, height, unit_height):
        for x in range(0, width, unit_width):
            cropped = image[y:y+unit_height, x:x+unit_width]

            # skip the empty image
            if np.sum(cropped) == 0:
                continue
                
            # alpha value of the pixel below threshold is taken as transparent
            cropped[cropped[:, :, -1] < TRANSPARENCY_THRESHOLD] = colors.red
            
            yield cropped


parser = ArgumentParser()
parser.add_argument(
    "-f", "--file", help="path of sticker file of Facebook (.png)", required=True)
parser.add_argument(
    "-r", "--row", help="number of rows in the sticker image", required=True, type=int)
parser.add_argument(
    "-c", "--column", help="number of rows in the sticker image", required=True, type=int)
parser.add_argument(
    "-o", "--output", help="specify the output filename", default="output.gif")
parser.add_argument(
    "-d", "--duration", help="specify the duration of each frame, smaller is faster", default=100, type=int)

args = parser.parse_args()
output_path = "./output/{}".format(args.output)


image = read_sticker(args.file)

# crop the image into pieces and convert them from np array to PIL Image
cropped_images = [Image.fromarray(image)
                  for image in get_cropped_images(image)]

# save the gif
cropped_images[0].save(output_path, save_all=True,
                       append_images=cropped_images[1:], duration=args.duration, loop=0, transparency=0, disposal=2)
