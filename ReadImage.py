import cv2

image = cv2.imread('logo.jpg')
cv2.imshow('image',image)
cv2.waitKey(0) # This is necessary to be required so that the image doesn't close immediately.  