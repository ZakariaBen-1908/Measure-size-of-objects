#Object Size Measurement using Aruco Marker

Overview

This project provides a method to measure object sizes using an Aruco marker as a reference. The system can process both static images and real-time video feeds from a camera to determine the width and height of objects in centimeters.

Features

Detects objects with a homogeneous background.

Uses an Aruco marker (5 cm x 5 cm) to calibrate pixel-to-centimeter conversion.

Measures object dimensions in both images and real-time video.

Displays object dimensions on the processed image or video feed.

Dependencies

Ensure you have the following Python packages installed:

pip install opencv-python numpy

File Descriptions

measure_object_size.py: Measures object sizes from a static image.

real_time_measure.py: Measures object sizes in real-time using a webcam.

object_detector.py: Contains the HomogeneousBgDetector class used for object detection.

Usage

1. Measuring Objects in an Image

Place the image containing an Aruco marker and the object to measure in the images/ folder and run:

python measure_object_size.py

2. Measuring Objects in Real-Time

Ensure a webcam is connected and run:

python real_time_measure.py

Press Esc to exit the real-time measurement window.

How It Works

Detect Aruco Marker:

Identifies the Aruco marker in the image or video feed.

Calculates its perimeter to determine the pixel-to-centimeter ratio.

Object Detection:

Detects objects with a homogeneous background.

Computes object dimensions based on the pixel-to-centimeter ratio.

Display Results:

Draws bounding boxes around detected objects.

Displays object width and height on the output image or video feed.

Example Output

The processed image or video feed will display detected objects with dimensions annotated as follows:

Width: 12.3 cm
Height: 8.7 cm

Future Improvements

Improve object detection for complex backgrounds.

Support multiple reference objects for better accuracy.

Implement a GUI for easier interaction.

Author

Zakaria BENCHEIKH
