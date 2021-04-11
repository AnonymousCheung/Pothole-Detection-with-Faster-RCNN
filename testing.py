import os
import sys
import json
import datetime
import numpy as np
import skimage.draw
import cv2
from pathlib import Path
# from mrcnn.config import Config
# from mrcnn import model as modellib, utils
# from mrcnn.visualize import display_instances
import matplotlib.pyplot as plt

# class ModelConfig(Config):
#     NAME = 'mrcnn'
#     IMAGES_PER_GPU = 2
#     NUM_CLASSES = 2
#     STEPS_PER_EPOCH = 100
#     DETECTION_MIN_CONFIDENCE = 90

# class CustomDataset(utils.Dataset):
#     def __init__(self, masks, img_dir):
#         super().__init__()
#         self.img_ids = masks['image_id']
#     def load_custom(self, dir, set):
#         self.add_class('mrcnn', 1, 'pothole')

# config = ModelConfig()
# model = modellib.MaskRCNN(mode='inference', config=config, model_dir='./')
# model.load_weights('mask_rcnn_coco.h5', by_name=True)


def load(dir):
    data = np.loadtxt(open(Path('.').parent.absolute() / 'archive' / 'train_df.csv', 'rt'), dtype=str, skiprows=1, delimiter=',')
    

    #data[:,5:6]=np.sum(data[:,5:6],data[:,3:4],axis=1)
    

    for a in range(len(data[:])):
       data[a, 4:5] = data[a, 2:3] + data[a, 4:5]
       data[a,5:6]=data[a,3:4]+data[a,5:6]
        



