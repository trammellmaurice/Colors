import rospy
import numpy as np
from turtleAPI import robot
import cv2

colors = {
    # BLUE VALUES
    "blue":
    [BLUE_MIN = np.array([90, 100, 20],np.uint8),
    BLUE_MAX = np.array([125, 255, 255],np.uint8)],

    # PINK VALUES
    "pink":
    [PINK_MIN = np.array([135, 50, 20],np.uint8),
    PINK_MAX = np.array([165, 255, 255],np.uint8)],

    # GREEN VALUES
    "green":
    [GREEN_MIN = np.array([35, 100, 20],np.uint8),
    GREEN_MAX = np.array([75, 255, 255],np.uint8)],

    # RED VALUES (0-10)
    "red":
    [RED_MIN = np.array([0,50,50],np.uint8),
    RED_MAX = np.array([10,255,255],np.uint8)],
}



try:
    turtle = robot()
    desired_color = str(input("RED, GREEN, BLUE, OR PINK?")).lower()
    while not rospy.is_shutdown():
        frame = turtle.getImage()
        hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        frame_threshed = cv2.inRange(hsv_img, colors[desired_color][0], colors[desired_color][0])
        if desired_color == "red":
            red_thresh = cv2.inRange(hsv_img, np.array([170,50,50],np.uint8), np.array([180,255,255],np.uint8))
            frame_threshed += red_thresh
        cv2.imshow("CAMERA",frame_threshed)
        cv2.waitKey(27)
except:
    rospy.loginfo("Terminating")
