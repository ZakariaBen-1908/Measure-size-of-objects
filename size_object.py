import cv2
import numpy as np
from object_detector import HomogeneousBgDetector

# Load the image
img = cv2.imread("images/img4.jpg")
# Define the scale factor (e.g., 0.5 for 50% reduction)
scale_percent = 0.25  

# Compute new dimensions while maintaining aspect ratio
new_width = int(img.shape[1] * scale_percent)
new_height = int(img.shape[0] * scale_percent)

# Resize image
img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

# Initialize the detector
detector = HomogeneousBgDetector()

# Detect contours
contours = detector.detect_objects(img)

# Reference object size (in cm)
ref_width_cm = 15
ref_height_cm = 10

# Initialize scaling factor
pixels_per_cm = None

for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    # Sorting width and height
    width_px, height_px = max(w, h), min(w, h)

    # Identify reference object (assuming largest detected object is reference)
    if pixels_per_cm is None:
        pixels_per_cm = width_px / ref_width_cm  # You can also use height_px / ref_height_cm

    # Convert to cm
    width_cm = width_px / pixels_per_cm
    height_cm = height_px / pixels_per_cm

    # Get bounding box
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # Draw detections
    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width: {:.1f} cm".format(width_cm), (int(x - 100), int(y - 20)),
                cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, "Height: {:.1f} cm".format(height_cm), (int(x - 100), int(y + 15)),
                cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

# Show the image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
