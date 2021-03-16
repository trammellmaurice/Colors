#!/usr/bin/env python3
import numpy as np
import cv2
H = [90,125]
S= [100, 255]
V = [20,255]
video = cv2.VideoCapture(0)

colors = {
    # BLUE VALUES
    "blue":
    [np.array([90, 100, 20],np.uint8),
    np.array([125, 255, 255],np.uint8)],

    # PINK VALUES
    "pink":
    [np.array([135, 50, 20],np.uint8),
    np.array([165, 255, 255],np.uint8)],

    # GREEN VALUES
    "green":
    [np.array([35, 100, 20],np.uint8),
    np.array([75, 255, 255],np.uint8)],

    # RED VALUES (0-10)
    "red":
    [np.array([0,50,50],np.uint8),
    np.array([10,255,255],np.uint8)],

    # mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
    #
    # # RED VALUES (170-180)
    # lower_red = np.array([170,50,50])
    # upper_red = np.array([180,255,255])
    # mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
}

desired_color = str(input("RED, GREEN, BLUE, OR PINK?")).lower()

while True:
    ok,frame = video.read()
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    frame_threshed = cv2.inRange(hsv_img, colors[desired_color][0], colors[desired_color][0])
    cv2.imshow("CAMERA",frame_threshed)
    cv2.waitKey(27)
