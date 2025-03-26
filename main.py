import cv2
import numpy as np
from object_detector import HomogeneousBgDetector

# Initialize the camera
cap = cv2.VideoCapture(0)  # Change to the correct camera index if needed

# Initialize the object detector
detector = HomogeneousBgDetector()

# Reference object dimensions (in cm)
ref_width_cm = 9.2
ref_height_cm = 6.1

# Scaling factor (pixels per cm), initialized as None
pixels_per_cm = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame for consistency
    frame = cv2.resize(frame, (640, 480))

    # Detect objects
    contours = detector.detect_objects(frame)

    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect

        # Sort width and height
        width_px, height_px = max(w, h), min(w, h)

        # Set reference object size if not already set
        if pixels_per_cm is None:
            pixels_per_cm = width_px / ref_width_cm  # Use width or height for scaling

        # Compute real-world dimensions
        width_cm = width_px / pixels_per_cm
        height_cm = height_px / pixels_per_cm

        # Get the bounding box
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # Draw detections
        cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)
        cv2.polylines(frame, [box], True, (255, 0, 0), 2)
        cv2.putText(frame, "Width: {:.1f} cm".format(width_cm), (int(x - 100), int(y - 20)),
                    cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
        cv2.putText(frame, "Height: {:.1f} cm".format(height_cm), (int(x - 100), int(y + 15)),
                    cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

    # Show the live frame
    cv2.imshow("Live Object Measurement", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
