import cv2
import colors as color_helper

"""
This function below will draw the Head up display(HUD) on the frame
Input:  
    # frame: the video frame's name
    # color: any RBG color(can use any pre-defined color in colors.py)
    # center_x: the coordinate x of camera's Center
    # center_y: the coordinate y of camera's Center
    # center_radius: the the radius range from camera's center
    
Output:
    # No output
"""


def create_hud(frame, color):
    # draw 4 corners:
    cv2.line(frame, (10, 10), (60, 10), color, 2)
    cv2.line(frame, (10, 10), (10, 60), color, 2)

    cv2.line(frame, (1270, 10), (1220, 10), color, 2)
    cv2.line(frame, (1270, 10), (1270, 60), color, 2)

    cv2.line(frame, (10, 710), (60, 710), color, 2)
    cv2.line(frame, (10, 710), (10, 660), color, 2)

    cv2.line(frame, (1270, 710), (1220, 710), color, 2)
    cv2.line(frame, (1270, 710), (1270, 660), color, 2)

    # draw left curve
    cv2.line(frame, (70, 100), (70, 620), color, 3)
    cv2.line(frame, (70, 100), (110, 80), color, 3)
    cv2.line(frame, (70, 620), (110, 640), color, 3)

    # draw right curve
    cv2.line(frame, (1210, 100), (1210, 620), color, 3)
    cv2.line(frame, (1170, 80), (1210, 100), color, 3)
    cv2.line(frame, (1170, 640), (1210, 620), color, 3)


def rectangle(frame, topLeft, bottomRight, color, thickness=3):

    cv2.rectangle(frame, topLeft, bottomRight, color, thickness)


"""
This function below will return the current position of the target comparing to the camera center radius
Input:  
    # target_pos_x: the coordinate x of target's Center
    # target_pos_y: the coordinate y of target's Center
    # center_x: the coordinate x of camera's Center
    # center_y: the coordinate y of camera's Center
    # center_radius: the the radius range from camera's center
    
Output:
    # position: a string informing target's position
"""


cv2.FILLED
def infoBoxLabel(frame, label, topLeft, bottomRight, color, thickness=2):
    
    # Draw box around the Face
    rectangle(frame, topLeft, bottomRight, color)
    
    xmin, ymin = topLeft
    xmax, ymax = bottomRight

    # Draw background box
    center_x = (xmin + xmax) // 2
    center_y = (ymin + ymax) // 2
    
    rectangle(frame, (center_x - 100, ymin - 50), (center_x + 100, ymin - 10), color_helper.white, cv2.FILLED)     
    # Write Label text
    cv2.putText(frame, label, (center_x - 80, ymin - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, thickness)
