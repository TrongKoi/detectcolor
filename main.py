# import os
import cv2 as cv
from util import get_limit
from PIL import Image

facecam = cv.VideoCapture(0)

yellow = [0,255,255]


while True:
    ret, frame = facecam.read()
    
    
    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower,upper = get_limit(colors=yellow)
    mask = cv.inRange(hsvImage, lower, upper)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)



    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


facecam.release()

cv.DestroyAllWindows()