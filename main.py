from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load traffic video
cap = cv2.VideoCapture("car_moving.mp4")

# Counting line (y = 300 for example)
count_line_y = 300
vehicle_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    # Get detections
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1,y1,x2,y2 = map(int,box.xyxy[0])
            
            if cls in [2,3,5,7]:
                cx = int((x1 + x2)/2)
                cy = int((y1 + y2)/2)
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(frame,model.names[cls],(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
                
                if cy > count_line_y-5 and cy < count_line_y+5:
                    vehicle_count += 1
                    
    cv2.line(frame,(0,count_line_y),(frame.shape[1],count_line_y),(255,0,0),2)
    
    cv2.putText(frame,f"Vehicle : {vehicle_count}",(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(120,23,56),3)
    cv2.imshow("Traffic Monitoring", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
