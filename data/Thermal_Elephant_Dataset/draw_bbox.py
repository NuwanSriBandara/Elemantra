import os
from PIL import Image, ImageDraw
import numpy as np
import xml.etree.ElementTree as ET
import bbox_pascal from map_bbox
import bbox_yolo from map_bbox

all_files = os.listdir('./Thermal_Elephant_Dataset/annotations')

for file in all_files:
  if file.endswith('.xml'):
    _ = bbox_pascal('./Thermal_Elephant_Dataset', file, 'red')
  elif file.endswith('.txt'):
    _ = bbox_yolo('./Thermal_Elephant_Dataset', file, 'red')
  else:
    print('Error')
