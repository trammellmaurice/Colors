import rospy
from turtleAPI import robot
import cv2

RED_MIN = np.array([100, 50, 50],np.uint8)
RED_MAX = np.array([255, 50, 50],np.uint8)

try:
    turtle = robot()
    while not rospy.is_shutdown():
        frame = turtle.getImage()
        hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        frame_threshed = cv2.inRange(hsv_img, RED_MIN, RED_MAX)
        cv2.imshow("CAMERA",frame_threshed)
        cv2.waitKey(27)
except:
    rospy.loginfo("Terminating")
