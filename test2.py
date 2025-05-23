import cv2

def on_trackbar_changed(args):
    pass

# Threshold types dictionary
thresh_types = {
    0: cv2.THRESH_BINARY,
    1: cv2.THRESH_BINARY_INV,
    2: cv2.THRESH_TRUNC,
    3: cv2.THRESH_TOZERO,
    4: cv2.THRESH_TOZERO_INV
}

# Load the image
img = cv2.imread('dog.jpg')
if img is None:
    print("Error: Image not found.")
    exit()

# Preprocessing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Create display windows
cv2.namedWindow("Image")
cv2.namedWindow("Real")
cv2.imshow("Real", img)

# Create trackbars
cv2.createTrackbar('Thresh Value', 'Image', 127, 255, on_trackbar_changed)
cv2.createTrackbar('Thresh Type', 'Image', 0, 4, on_trackbar_changed)  # 0–4

while True:
    if cv2.getWindowProperty('Image', cv2.WND_PROP_VISIBLE) < 1:
        break

    # Get current values
    thresh_val = cv2.getTrackbarPos('Thresh Value', 'Image')
    thresh_type_index = cv2.getTrackbarPos('Thresh Type', 'Image')
    thresh_type = thresh_types.get(thresh_type_index, cv2.THRESH_BINARY)

    # Apply threshold
    thresholded = cv2.threshold(blurred, thresh_val, 255, thresh_type)[1]

    # Find contours
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on a copy of the original
    img_with_contours = img.copy()
    cv2.drawContours(img_with_contours, contours, -1, (0, 255, 0), 2)

    # Show the image with contours
    cv2.imshow("Image", img_with_contours)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
