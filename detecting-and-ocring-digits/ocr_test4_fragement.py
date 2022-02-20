#!/usr/bin/python3

import numpy as np
import cv2
from pyocr import pyocr
from pyocr import builders
from PIL import Image
from time import sleep


###############################################################
### Imagery
###############################################################
def initialize_images():    
#  p_img = 'img/example.png'
  p_img = 'pic_1644164410.jpg'
  image = cv2.imread(p_img, 1) 
  ##
  # Read image from which text needs to be extracted
  #image = cv2.imread("pic_1644164401.jpg", 1)
  #image = cv2.imread("sample4.jpg")

  # Preprocessing the image starts
  #-----Converting image to LAB Color model----------------------------------- 
  lab= cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
  #-----Splitting the LAB image to different channels-------------------------
  l, a, b = cv2.split(lab)
  #-----Applying CLAHE to L-channel-------------------------------------------
  clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
  cl = clahe.apply(l)
  #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
  limg = cv2.merge((cl,a,b))
  #-----Converting image from LAB Color model to RGB model--------------------
  final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
  # Convert the image to gray scale
  img_temp = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)
  cv2.imshow("gray", img_temp)
  ##
  #    cv2.imshow('imagetemp',img_temp)
  img = img_temp.copy()
  return img, img_temp, None

