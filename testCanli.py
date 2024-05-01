import cv2
from ultralytics import YOLO

model = YOLO(r'...uzumDeneme\runs\detect\train\weights\last.pt')

cap = cv2.VideoCapture(0)
 

while cap.isOpened():

    success, frame = cap.read()

    if success:
        
     

        results = model(frame)

        # Sonuçları görüntüle
        annotated_frame = results[0].plot()
        
        # belirtilmiş kareyi göster
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Çık
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Hata oluşursa bitir
        break

# kamereyı ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()