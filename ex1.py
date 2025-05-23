import cv2
import numpy as np

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Set image dimensions
height = 250
width = 500

# Create a blank white image
image = np.ones((height, width), dtype=np.uint8) * 255  # white

# Make the right half black
image[:, width//2:] = 0  # black on the right half

cv2.imshow('image',image)


# Optional: Save to file
Image.fromarray(image).save('input1_1.png')

     
img1 = cv2.imread('input1_1.png')

img2 = cv2.imread('input2.png') 
print("Image 1 shape:", img1.shape)
print("Image 2 shape:", img2.shape)
img1 = img1[:, :499, :]  # Crop the width from 500 to 499
print("Image 1 shape:", img1.shape)
# or
# img1 = cv2.resize(img1, (499, 250))  # Note: width comes before height in OpenCV

# Check if images are loaded properly
if img1 is None or img2 is None:
    print("Error loading one or both images")
    exit()

# Show the original
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)

dest_and = cv2.bitwise_and(img1, img2, mask = None)
cv2.imshow('Bitwise And', dest_and)

dest_xor = cv2.bitwise_xor(img1, img2, mask = None)
cv2.imshow('Bitwise XOR', dest_xor)
cv2.waitKey(0)

# all the images are read and shown in BGR coloring system