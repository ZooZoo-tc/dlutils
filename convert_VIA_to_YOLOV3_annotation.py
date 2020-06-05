# -*- coding: utf-8 -*-

#Execution: 
# (yolov3) D:\Workspace\AI\YoloV3-Latest\keras-yolov3-ppe>
# python convert_VIA_to_YOLOV3_annotation.py --annotation_file via_region_ppe.json --image_dir images\

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
import io
import logging
import os

import yaml
import json

import numpy as np
import PIL.Image
import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string('annotation_file', '', 'Annotation file for raw dataset')
flags.DEFINE_string('image_dir', '', 'To append the image directory to file names')
FLAGS = flags.FLAGS
# classes = {'person': 0, 'helmet': 1,'vest':2,'mask':3,'gloves':4,'goggles':5,'Nohelmet':6,'NoVest':7,'NoGloves':8,'NoMask':9,'NoGoggles':10,'shoes':11,'no_shoes':12}
classes = {'person': 0, 'helmet': 1,'vest':2}

def main(_):

  annotation_path = FLAGS.annotation_file
  annotation_fid  = open(annotation_path)
  
  with open(annotation_path) as annotation_fid:
    annotations     = yaml.safe_load(annotation_fid)
    annotation_size = len(annotations)    
    annotation_keys = annotations.keys()
    for annotation_key in annotation_keys:
      data = annotations[annotation_key]
      fileName = data['filename']
      train_str = FLAGS.image_dir+fileName
      for attribute in data['regions']:        
        shape = attribute['shape_attributes']
        xmin = shape['x']
        ymin = shape['y']
        region_width = shape['width']
        region_height = shape['height']
        xmax = int(xmin)+int(region_width)
        ymax = int(ymin)+int(region_height)
      
        if ('ppe' in attribute['region_attributes']):
            cls = attribute['region_attributes']['ppe']
            if cls in classes:
              train_str +=  ' '+str(xmin)+','+str(ymin)+','+str(xmax)+','+str(ymax)+','+str(classes[cls])
      if(len(data['regions']) != 0):
        print(train_str)
      

if __name__ == '__main__':
  tf.app.run()
