"""
    Tracks and annotates objects w/ bounding box
"""

import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import time

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # Width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Height

new_frame_time = 0
prev_frame_time = 0

while True:
    _, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model.predict(img)

    for r in results:
        annotator = Annotator(frame)
        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            annotator.box_label(b, model.names[int(c)])

    # FPS counter
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    cv2.putText(frame, 
                f"FPS: {int(fps)}",
                (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 255, 0), 2)
          
    frame = annotator.result()
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()