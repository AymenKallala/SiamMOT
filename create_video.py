import cv2
import numpy as np
from os import listdir
import re
from sys import argv

def make_video(name: str):

    reg = name + "-[0-9]{3}.bmp"
    path = "./sequences-train-untouched/"
    export_path = "./sequences-train/" + name + '/'
    print('source_path :',path)
    print('export_path :',export_path)
    
    img0 = cv2.imread(path + name + "-001.bmp")
    height, width, _ = img0.shape
    size = (width,height)
    out = cv2.VideoWriter(export_path + 'project-' + name + '.mp4', cv2.VideoWriter_fourcc(*'avc1'), 15, size)

    for filename in listdir(path):
        if re.match(reg, filename):
            img = cv2.imread(path + filename)
            out.write(img)

    out.release()

    return None

if __name__=="main":
    name = str(argv[1])
    make_video(name)