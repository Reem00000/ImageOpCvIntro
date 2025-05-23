import cv2
import numpy as np
     
image = cv2.imread('logo.jpg')
if image is None:
    print("Error loading one image")
    exit()
else:
    # Show the original
    cv2.imshow('Original Image', image) 
edges = cv2.Canny(image, 100, 200)
# edges = cv2.Canny(image, 50, 150)  # More sensitive
# edges = cv2.Canny(image, 150, 250) # Less sensitive, cleaner edges
if edges is None:
    print("Error loading one image")
    exit()
else:
    # Show the original
    cv2.imshow('Canny', edges)

cv2.waitKey(0)