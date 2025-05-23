import cv2

def on_trace_bar_changed(x):
    pass

# Mapping from index to readable threshold type name and OpenCV constant
thresh_type_options = {
    0: ("THRESH_BINARY", cv2.THRESH_BINARY),
    1: ("THRESH_BINARY_INV", cv2.THRESH_BINARY_INV),
    2: ("THRESH_TRUNC", cv2.THRESH_TRUNC),
    3: ("THRESH_TOZERO", cv2.THRESH_TOZERO),
    4: ("THRESH_TOZERO_INV", cv2.THRESH_TOZERO_INV)
}

# Load and prepare the image
img = cv2.imread('dog.jpg')
if img is None:
    print("Error: Image not found or could not be read.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Create windows
cv2.namedWindow("Black & White Threshold")
cv2.namedWindow("Green Contours")

# Trackbars
cv2.createTrackbar('Threshold Value', 'Black & White Threshold', 127, 255, on_trace_bar_changed)
cv2.createTrackbar('Threshold Type', 'Black & White Threshold', 0, len(thresh_type_options)-1, on_trace_bar_changed)
cv2.waitKey(100)  # short delay to ensure window is initialized

while True:
    # Get trackbar values
    thresh_val = cv2.getTrackbarPos('Threshold Value', 'Black & White Threshold')
    thresh_type_index = cv2.getTrackbarPos('Threshold Type', 'Black & White Threshold')
    thresh_type_name, thresh_type = thresh_type_options.get(thresh_type_index, ("THRESH_BINARY", cv2.THRESH_BINARY))

    # Apply thresholding
    thresh_img = cv2.threshold(blurred, thresh_val, 255, thresh_type)[1]

    # Find contours
    contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a copy for green contours
    contour_img = img.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

    # Put label
    cv2.putText(contour_img, f'{thresh_type_name} | Thresh: {thresh_val}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 200, 0), 2, cv2.LINE_AA)

    # Show both views
    cv2.imshow("Black & White Threshold", thresh_img)
    cv2.imshow("Green Contours", contour_img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite('saved_contours.png', contour_img)
        print("Saved image as 'saved_contours.png'")


cv2.destroyAllWindows()
