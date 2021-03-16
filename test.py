#!/usr/bin/env python3
import numpy as np
import cv2
H = [90,125]
S= [100, 255]
V = [20,255]
video = cv2.VideoCapture(0)

BLUE_MIN = np.array([90, 100, 20],np.uint8)
BLUE_MAX = np.array([125, 255, 255],np.uint8)

while True:
    ok,frame = video.read()
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    frame_threshed = cv2.inRange(hsv_img, BLUE_MIN, BLUE_MAX)
    cv2.imshow("CAMERA",frame_threshed)
    cv2.waitKey(27)
