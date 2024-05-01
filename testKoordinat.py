import cv2
from ultralytics import YOLO

model = YOLO(r'...uzumDeneme\runs\detect\train\weights\last.pt')

cap = cv2.VideoCapture(0)
cap.set(3, 240)  
cap.set(4, 180) 

classes=[1]
while cap.isOpened():

    success, frame = cap.read()

    if success:
        
        frame = cv2.resize(frame, (240, 180))

        results = model.predict(source=frame,conf=0.6,classes=classes)
           
            
        # Sonuçları görüntüle
        annotated_frame = results[0].plot()  
        # belirtilmiş kareyi göster
        cv2.imshow("YOLOv8 Inference", annotated_frame) 
        
        for r in results:
             # Tespit var mı 
             if r.boxes.xyxy.shape[0] > 0 and r.boxes.cls.shape[0] > 0:
                if r.boxes.cls.item() == 1:
                 # Kordinat alma
                    boxes = results[0].boxes.xyxy.tolist()
                    print("Salkım kordinatları:", boxes)
        # Çık
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Hata oluşursa bitir
        break
       

# kamereyı ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()