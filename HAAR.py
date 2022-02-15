from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import time
import numpy as np
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 45
camera.rotation = 180
ntime=0
ptime=0
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
haarcas=cv.CascadeClassifier('body.xml')
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    boxes = haarcas.detectMultiScale(image, winStride=(8,8) )
    for (x, y,w,h) in boxes:
        # display the detected boxes in the colour picture
        cv.rectangle(image, (x,y), (x+w, y+h),(0, 255, 0), 2)
        cv.putText(image,"person",(x,y-5),cv.FONT_HERSHEY_SIMPLEX,1,(100,255,0),1,cv.LINE_AA)
    ntime=time.time()
    fps=1/(ntime-ptime)
    ptime=ntime
    fps=(int)(fps)
    fps=str(fps)
    cv.putText(image,fps,(7,70),cv.FONT_HERSHEY_SIMPLEX,3,(100,255,0),3,cv.LINE_AA)
    cv.imshow("Frame", image);
    key = cv.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if(cv.waitKey(20)&0xFF==ord('d')):#imp for break in csmera
     break


  