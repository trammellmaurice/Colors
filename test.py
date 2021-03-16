#!/usr/bin/env python3
import numpy as np
import cv2

video = cv2.VideoCapture(0)

RED_MIN = np.array([100, 50, 50],np.uint8)
RED_MAX = np.array([255, 50, 50],np.uint8)

while True:
    ok,frame = video.read()
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    frame_threshed = cv2.inRange(hsv_img, RED_MIN, RED_MAX)
    cv2.imshow("CAMERA",frame_threshed)
    cv2.waitKey(27)
