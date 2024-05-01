from ultralytics import YOLO

# Load 
model = YOLO()  

# Predict 
model.predict(r'path', save=True, imgsz=1088, conf=0.17)