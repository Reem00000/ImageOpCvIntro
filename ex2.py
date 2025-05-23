import cv2
import matplotlib.pyplot as plt

image = cv2.imread('logo.jpg')

# Check if the image was loaded
if image is None:
    print("Error: Could not read the image.")
else:
    cv2.imshow('image',image)
    # cv2 read image as BGR, need to translate to RGB
    image_rgb =  cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_gray =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_, image_bw = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
 # Plot using matplotlib
    plt.figure(figsize=(15, 7))

    # Original BGR image (shown incorrectly in matplotlib unless converted)
    plt.subplot(1, 3, 1)
    plt.imshow(image)  # This will show with wrong colors (BGR)
    plt.title("Original (BGR)")
    plt.axis("off")

    # Corrected RGB image
    plt.subplot(1, 3, 2)
    plt.imshow(image_rgb)
    plt.title("RGB Image")
    plt.axis("off")

    # Grayscale image
    plt.subplot(1, 3, 3)
    plt.imshow(image_gray, cmap='gray')
    plt.title("Grey Image")
    plt.axis("off")

    plt.tight_layout()
    # Save the figure to a file
    plt.savefig("comparison_plot.png", dpi=300, bbox_inches='tight')  # You can change the filename and dpi
    plt.show()

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