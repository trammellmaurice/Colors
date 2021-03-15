import rospy
from turtleAPI import robot
import cv2

try:
    turtle = robot()
    while not rospy.is_shutdown():
        frame = turtle.getImage()
        cv2.imshow("CAMERA",frame)
        cv2.waitKey(27)
except:
    rospy.loginfo("Terminating")
