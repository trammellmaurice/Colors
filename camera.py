import rospy
import numpy as np
from turtleAPI import robot
import cv2

BLUE_MIN = np.array([90, 100, 20],np.uint8)
BLUE_MAX = np.array([125, 255, 255],np.uint8)

PINK_MIN = np.array([135, 50, 20],np.uint8)
PINK_MAX = np.array([165, 255, 255],np.uint8)

GREEN_MIN = np.array([35, 100, 20],np.uint8)
GREEN_MAX = np.array([75, 255, 255],np.uint8)

try:
    turtle = robot()
    while not rospy.is_shutdown():
        frame = turtle.getImage()
        hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        frame_threshed = cv2.inRange(hsv_img, PINK_MIN, PINK_MAX)
        cv2.imshow("CAMERA",frame_threshed)
        cv2.waitKey(27)
except:
    rospy.loginfo("Terminating")
