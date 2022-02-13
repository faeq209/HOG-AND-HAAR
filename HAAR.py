from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import time
import numpy as np
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 45
camera.rotation = 180
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
haarcas=cv.CascadeClassifier('body.xml')
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    boxes = haarcas.detectMultiScale(image, winStride=(8,8) )
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv.rectangle(image, (xA, yA), (xB, yB),(0, 255, 0), 2)
    cv.imshow("Frame", image);
    key = cv.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
       break
  