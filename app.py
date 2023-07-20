import cv2  
import numpy as np

capture = cv2.VideoCapture(0)

if(capture.isOpened() == False):
    print("Could not find cam!")

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        cv2.imshow("Camera", frame) # Display images

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

capture.release()

cv2.destroyAllWindows()