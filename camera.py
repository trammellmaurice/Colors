import rospy
import numpy as np
from turtleAPI import robot
import cv2

BLUE_MIN = np.array([90, 100, 20],np.uint8)
BLUE_MAX = np.array([125, 255, 255],np.uint8)


try:
    turtle = robot()
    while not rospy.is_shutdown():
        frame = turtle.getImage()
        hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        frame_threshed = cv2.inRange(hsv_img, BLUE_MIN, BLUE_MAX)
        cv2.imshow("CAMERA",frame_threshed)
        cv2.waitKey(27)
except:
    rospy.loginfo("Terminating")
