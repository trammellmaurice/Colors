import rospy
from turtleAPT import robot
import cv2

COLORS = {"red":,"blue":,"green":,"pink":}

try:
    turtle = robot()
    while not rospy.is_shutdown():
        target_color = input()
except:
    rospy.loginfo("Terminating")
