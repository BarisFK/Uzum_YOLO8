# Grape Detection Computer Vision Project

This computer vision project utilizes the YOLOv8 model to detect and analyze grape bunches, bruises, stems, and leaves. The model was trained on a custom dataset I curated, which included annotated images of grape-related objects. Through iterative training, the model's weights were fine-tuned to improve its accuracy. Future work may involve expanding the dataset and fine-tuning the model architecture for enhanced performance.

## Project Structure

- testLive.py - This script uses a webcam to perform real-time detection of objects. It visualizes the detection results on each frame captured from the webcam.
- testKoordinat.py - Focuses on detecting specific classes (in this case, grape bunches) and prints their coordinates on the screen.
- testCenterPoint.py - Draws a rectangle and a center point on a static image to illustrate object detection results.

## Setup and Installation

### Requirements

- Python 3.x
- OpenCV library
- Ultralytics YOLO library

Install the required Python libraries using pip:

bash
pip install opencv-python-headless ultralytics


Example

<img src="https://github.com/BarisFK/Uzum_YOLO8/assets/92215497/3df85b15-08d0-4832-a7a4-d246d709a2c7" alt="Örnek" style="width:600px;height:800px;">
