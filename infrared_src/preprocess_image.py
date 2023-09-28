import numpy as np
import cv2
import matplotlib.pyplot as plt

def preprocess_image(image_path):
  image = cv2.imread(image_path)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  (thresh, im_bw) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  im_floodfill = im_bw.copy()
  h, w = im_bw.shape[:2]
  mask = np.zeros((h+2, w+2), np.uint8)
  cv2.floodFill(im_floodfill, mask, (0,0), 255);
  im_floodfill_inv = cv2.bitwise_not(im_floodfill)
  image = cv2.bitwise_not(image)
  image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
  # plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  # plt.show()

  return image
