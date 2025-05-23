import cv2

image = cv2.imread('logo.jpg')
  
roi = image[100 : 155, 30 : 230]
cv2.imshow('image',roi)
# cv2.imwrite will save the image in the path folder.
cv2.imwrite('imageROI.jpg', roi)
cv2.waitKey(0) 