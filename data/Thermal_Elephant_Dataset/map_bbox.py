import os
from PIL import Image, ImageDraw
import numpy as np
import xml.etree.ElementTree as ET

def bbox_yolo(folder_path, file, outline_color, width=5):
  image_name = os.path.splitext(file)[0]
  image_path = os.path.join(folder_path, 'images', image_name + '.png')
  annotation_path = os.path.join(folder_path, 'annotations', file)

  image = Image.open(image_path)
  image_width, image_height = image.size
  anno_data = np.loadtxt(annotation_path)
  draw = ImageDraw.Draw(image)

  if anno_data.shape[0]==0:
    print(f"No elephants detected in {file}")
  elif anno_data.ndim == 1:
    anno_data = anno_data.reshape(1, -1)
    x_centre, y_centre, width, height = anno_data[0, 1:]
    # Calculate the coordinates for the top-left and bottom-right points of the rectangle
    top_left = ((x_centre-width/2)*image_width, (y_centre-height/2)*image_height)
    bottom_right = ((x_centre+width/2)*image_width, (y_centre+height/2)*image_height)
    draw.rectangle([top_left, bottom_right], outline=outline_color, width=5)

  elif anno_data.ndim == 2:
    for j in range(anno_data.shape[0]):
      x_centre, y_centre, width, height = anno_data[j, 1:]
      # Calculate the coordinates for the top-left and bottom-right points of the rectangle
      top_left = ((x_centre-width/2)*image_width, (y_centre-height/2)*image_height)
      bottom_right = ((x_centre+width/2)*image_width, (y_centre+height/2)*image_height)
      draw.rectangle([top_left, bottom_right], outline=outline_color, width=5)

  image.show()
  image.save(f'output_image_{image_name}'+'.png')

  return image

def bbox_pascal(folder_path, i, outline_color, width=5):
  # Load the XML file
  xml_file = os.path.join(folder_path, 'annotations', file)
  tree = ET.parse(xml_file)
  root = tree.getroot()

  # Extract image dimensions
  width = int(root.find('size/width').text)
  height = int(root.find('size/height').text)

  # Load the image
  image_name = os.path.splitext(file)[0]
  image_path = os.path.join(folder_path, 'images', image_name + '.png')
  image = Image.open(image_path)

  # Create an ImageDraw object to draw bounding boxes
  draw = ImageDraw.Draw(image)

  # Iterate through objects and draw bounding boxes
  try:
    for obj in root.findall('object'):
        name = obj.find('name').text
        if name == 'elephant':
            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)
            draw.rectangle([xmin, ymin, xmax, ymax], outline='red', width=3)

    # Save or display the image with bounding boxes
    image.show()  # Display the image with bounding boxes
    image.save(f"output_image_{image_name}.png")  # Save the image with bounding boxes

  except:
    print(f"No elephants detected in {image_name}.png")

  return image
