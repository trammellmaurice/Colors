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

        circles = cv2.HoughCircles(frame_threshed, cv2.HOUGH_GRADIENT, 1.2, 100)

        if circles is not None:
            print("YES")
            circles = np.round(circles[0, :]).astype("int")
            for (x,y,r) in circles:
               cv2.circle(frame_threshed, (x, y), r, (0, 255, 0), 4)
               cv2.rectangle(frame_threshed, (x - 5, y - 5), (x + 5, y + 5), (255, 0, 0), -1)

        cv2.imshow("CAMERA",frame_threshed)
        cv2.waitKey(27)
except Exception as e:
    print(e)
    rospy.loginfo("Terminating")
