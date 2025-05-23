import cv2

image = cv2.imread('logo.jpg')  
h, w = image.shape[:2]
print("Height = {},  Width = {}".format(h, w))
(B, G, R) = image[150, 150]
print("R = {}, G = {}, B = {}".format(R, G, B))
if image is None:
    print("Error loading one image")
    exit()
else:
    # Show the original
    cv2.imshow('Original Image', image) 
cv2.waitKey(0)