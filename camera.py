import rospy
import numpy as np
from turtleAPI import robot
import cv2

colors = {
    # BLUE VALUES
    "blue":{"min": np.array([90, 100, 20],np.uint8), "max": np.array([125, 255, 255],np.uint8)},


    # PINK VALUES
    "pink": {"min": np.array([135, 50, 20],np.uint8), "max": np.array([165, 255, 255],np.uint8)},

    # GREEN VALUES
    "green":  {"min": np.array([35, 100, 20],np.uint8), "max": np.array([75, 255, 255],np.uint8)},

    # RED VALUES (0-10)
    "red": {"min": np.array([0,50,50],np.uint8), "max": np.array([10,255,255],np.uint8)},
}


try:
    # INITIALIZE TURTLEBOT API
    turtle = robot()
    # GET DESIRED COLOR
    desired_color = input("RED, GREEN, BLUE, OR PINK?")
    # print(colors[desired_color])
    while not rospy.is_shutdown():

        # GET FRAME
        frame = turtle.getImage()
        # CONVERT FRAME TO HSV
        hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # THRESHOLD USING DESIRED COLOR
        frame_threshed = cv2.inRange(hsv_img, colors[desired_color]["min"], colors[desired_color]["max"])
        if desired_color == "red":
            # SECOND BAND FOR RED THRESHOLD
            red_thresh = cv2.inRange(hsv_img, np.array([170,50,50],np.uint8), np.array([180,255,255],np.uint8))
            frame_threshed += red_thresh

        splits = frame_threshed.copy()
        # SPLIT IMAGE INTO 5 SECTIONS
        sections = np.hsplit(frame_threshed,5)

        # REMOVE 0S
        for section in sections:
            section.sort()
        #     section = np.trim_zeros(section)
        #     section = section.size

        print(sections[0],sections[1],sections[2],sections[3],sections[4])
        frame_threshed = cv2.bitwise_and(frame,frame,mask = frame_threshed)

        # Blur using 3 * 3 kernel.
        frame_threshed = cv2.blur(frame_threshed, (3, 3))

        cv2.imshow("CAMERA",frame_threshed)
        cv2.waitKey(27)
except Exception as e:
    print(e)
    rospy.loginfo("Terminating")
