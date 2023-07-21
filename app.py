"""
    Test script for checking camera functionality with opencv library
"""

import cv2  
import numpy as np

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# * Custom resolution
#W, H = 1920, 1080
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, W)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, H)

cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cam.set(cv2.CAP_PROP_FPS, 30)

if(cam.isOpened() == False):
    print("Could not find cam!")

while(cam.isOpened()):
    ret, frame = cam.read()
    if ret == True:
        cv2.imshow("Camera", frame) # Display images

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cam.release()

cv2.destroyAllWindows()