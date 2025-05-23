import cv2
import numpy as np
     
img1 = cv2.imread('input1.png')

img2 = cv2.imread('input2.png') 

# Check if images are loaded properly
if img1 is None or img2 is None:
    print("Error loading one or both images")
    exit()

# Show the original
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)

dest_and = cv2.bitwise_and(img1, img2, mask = None)
cv2.imshow('Bitwise And', dest_and)
cv2.waitKey(0)