import cv2

def on_trace_bar_changed(args):
    pass

img = cv2.imread('dog.jpg')
if img is None:
    print("Error: Image not found or could not be read.")
    exit()
cv2.namedWindow("Image")
cv2.namedWindow("Real")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray: the input grayscale image.

# (5, 5): the size of the Gaussian kernel (height × width). It must be odd and positive.

# 0: the standard deviation in the X direction (sigmaX). If set to 0, OpenCV automatically calculates it based on the kernel size.
# To reduce high-frequency noise.

# To improve the results of thresholding, edge detection, or other post-processing steps.

# To soften the image and suppress irrelevant small details.
blurred = cv2.GaussianBlur(gray, (5, 5), 0)


cv2.createTrackbar('thres', 'Image', 0, 255, on_trace_bar_changed)

while True:
    if cv2.getWindowProperty('Image', cv2.WND_PROP_VISIBLE) < 1:
        break
    cv2.imshow("Real", img)
    thresh = cv2.getTrackbarPos('thres', 'Image')
     # Apply thresholding on a separate copy
    thresh_img = cv2.threshold(blurred, thresh, 255, cv2.THRESH_BINARY_INV)[1]
    # if thresh_img is None:
    #     print("Error: thresh_img not found or could not be read.")
    #     exit()
    cv2.imshow("Image", thresh_img)

    k = cv2.waitKey(1) & 0xFF
  
    if k == ord('q'):
        break


cv2.destroyAllWindows()

