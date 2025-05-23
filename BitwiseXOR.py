import cv2
import numpy as np
     

img1 = cv2.imread('input1.png')
img2 = cv2.imread('input2.png') 

dest_and = cv2.bitwise_xor(img1, img2, mask = None)
cv2.imshow('Bitwise And', dest_and)
cv2.waitKey(0)