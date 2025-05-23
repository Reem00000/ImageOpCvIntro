import cv2
import numpy as np

img = cv2.imread('dog.jpg')
if img is None:
    print("Error loading one image")
    exit()
else:
    # Show the original
    cv2.imshow('Original Image', img)
# Make the image a gray image, easy to find the edges.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Check if image is  loaded properly
if img_gray is None:
    print("Error loading one image")
    exit()
else:
    # Show the original
    cv2.imshow('Grey Image', img_gray)

# Gaussian Blur the image
blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
# Check if image is  loaded properly
if blurred is None:
    print("Error loading one image")
    exit()
else:
    # Show the original
    cv2.imshow('Blured Grey Image', blurred)
# Find the Thresholding, here we used 109, 255, which you can change to do the test
img_i = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow('', img_i)
# Make the area to mask
# Using the masking to cover the area in original image
image2 = cv2.bitwise_and(img, img, mask = img_i)
# Check if image is  loaded properly
if image2 is None:
    print("Error loading one image")
    exit()
else:
    # Show the original
    cv2.imshow('Detected Dog Image', image2)
cv2.imshow('Bitwise And', image2)
cv2.waitKey(0)

