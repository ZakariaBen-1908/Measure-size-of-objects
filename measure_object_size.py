import cv2
from object_detector import *
import numpy as np


# Load Aruco detector
parameters = cv2.aruco.DetectorParameters()
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)


#Load object detector
detector = HomogeneousBgDetector()

# Load image
img = cv2.imread("images/img_arucoo.jpg")

scale_percent = 0.75 

# Compute new dimensions while maintaining aspect ratio
new_width = int(img.shape[1] * scale_percent)
new_height = int(img.shape[0] * scale_percent)

# Resize image
img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

#Get Aruco Marker
corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

#Draw polygon around marker
int_corners = np.int0(corners)
cv2.polylines(img, int_corners, True, (0, 255, 0), 4)

# Aruco Parameters
aruco_perimeter = cv2.arcLength(corners[0], True)
print(aruco_perimeter)

# Pixel to cm ratio
pixel_to_cm = aruco_perimeter / 20
print(pixel_to_cm)

countours = detector.detect_objects(img)

#Draw objects boundaries
for cnt in countours:

    #Draw rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    # Get Width and Height of Objects by applying the Ratio pixel to cm
    object_width = w / pixel_to_cm
    object_height = h / pixel_to_cm

    # Display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {}".format(round(object_width, 1)), (int(x - 100), int(y - 15)), cv2.FONT_HERSHEY_PLAIN, 1, (100, 244, 0), 2)
    cv2.putText(img, "Height {}".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 1, (100, 244, 0), 2)



cv2.imshow("image", img)
cv2.waitKey(0)