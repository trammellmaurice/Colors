import rospy
import numpy as np
from turtleAPI import robot
import cv2

colors = {
    # BLUE VALUES
    "blue":{"min": np.array([100, 150, 0],np.uint8), "max": np.array([180, 255, 255],np.uint8)},

    # PINK VALUES
    "pink": {"min": np.array([135, 50, 20],np.uint8), "max": np.array([165, 255, 255],np.uint8)},

    # GREEN VALUES
    "green":  {"min": np.array([40, 52, 72],np.uint8), "max": np.array([100, 255, 255],np.uint8)},

    # YELLOW VALUES
    "yellow":  {"min": np.array([20, 90, 40],np.uint8), "max": np.array([30, 255, 255],np.uint8)},

    # RED VALUES (0-10)
    "red": {"min": np.array([0,50,50],np.uint8), "max": np.array([10,255,255],np.uint8)},
}


try:
    # INITIALIZE TURTLEBOT API
    turtle = robot()
    turtle.drive(0.5,0)

    # GET DESIRED COLOR
    desired_color = input("RED, GREEN, BLUE, YELLOW, OR PINK?")
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

        splits = np.copy(frame_threshed)

        # SPLIT COPY INTO 5 SECTIONS
        left2,left,front,right,right2 = np.hsplit(splits,5)

        #COUNT NON BLACK IN EACH SECTION
        sections = {
            'left2':(left2 != 0).sum(),
            'left':(left != 0).sum(),
            'front':(front != 0).sum(),
            'right':(right != 0).sum(),
            'right2':(right2 != 0).sum()
        }
        max_section = max(sections, key=sections.get)

        #2 SPEED P CONTROLLER BASED ON LOCATION ON SCREEN
        if sections[max_section] > 500:
            # print(max_section)
            if max_section == "left2":
                print("LEFT")
                turtle.drive(0.5,0.2)
            elif max_section == "left":
                print("LEFT")
                turtle.drive(0.25,0.5)
            elif max_section == "front":
                print("RIGHT")
                turtle.drive(0,1)
            elif max_section == "right":
                print("RIGHT")
                turtle.drive(-0.25,0.5)
            elif max_section == "right2":
                print("RIGHT")
                turtle.drive(-0.5,0.2)

        frame_threshed = cv2.bitwise_and(frame,frame,mask = frame_threshed)

        # Blur using 3 * 3 kernel.
        frame_threshed = cv2.blur(frame_threshed, (3, 3))

        cv2.imshow("CAMERA",frame_threshed)
        cv2.waitKey(27)
except Exception as e:
    turtle.stop()
    print(e)
    rospy.loginfo("Terminating")
