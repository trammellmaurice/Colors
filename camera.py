import rospy
from turtleAPI import robot
import cv2

try:
    turtle = robot()
    while not rospy.is_shutdown():
        frame = turtle.getImage()
        for pixel in frame:
            if pixel[0] > pixel[1] and pixel[0] > pixel[2]:
                pixel = (255,255,255)
            else:
                pixel = (0,0,0)
        cv2.imshow("CAMERA",frame)
        cv2.waitKey(27)
except:
    rospy.loginfo("Terminating")
