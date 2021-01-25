import pyautogui
import sys
import d3dshot
import numpy as np
from datetime import datetime


#dis be the mofo that will do the screenshotting via d.screenshot()
d = d3dshot.create(capture_output="numpy")


#center button to switch sides 1280,1220
#left button 1080, 1220
#right button 1480
left = (1080,1220)
center = (1280,1220)
right = (1480,1220)

#state 0 blue left red right
state = 0

#left balls coming in at 
#x=990 y = 800
#eft stop coming in at
#x=1230

#right balls stop coming in at
#x=1340
#right start coming in at 
#x=1580 y = 800

#height for pixels in the middle

#left end of the screen
#1000  and right 1560
# left end of left 1200
# right end of right 1360


def set_state_and_color(im_arr, state, time):
    time = datetime.now()
    #col left red 1 blue 0
    c_left = -1
    #col left red 1 blue 0
    c_right = -1

    #lookup y cooridante is constant
    y = 800

    #check for left
    for i in range (990,1230):
        if(im_arr[y,i][0] > 200 and im_arr[y,i][2] < 200):
            c_left = 1
            break
        if(im_arr[y,i][2] > 200 and im_arr[y,i][0] < 200):
            c_left = 0
            break

    for i in range (1340,1580):
        if(im_arr[y,i][0] > 200 and im_arr[y,i][2] < 200):
            c_right = 1
            break
        if(im_arr[y,i][2] > 200 and im_arr[y,i][0] < 200):
            c_right = 0
            break


    if c_left == -1 and c_right == 0:
        pyautogui.moveTo(left)

    if c_left == -1 and c_right == 1:
        pyautogui.moveTo(right)

    if c_left == 0 and c_right == -1:
        pyautogui.moveTo(left)

    if c_left == 1 and c_right == -1:
        pyautogui.moveTo(right)

    if c_left == c_right and c_left == 0:
        #mouse to left
        pyautogui.moveTo(left)
    if c_left == c_right and c_left == 1:
        #moues to right
        pyautogui.moveTo(right)
    
    if c_left == 0 and c_right == 1:
        if state == 1:
            pyautogui.mouseUp()
            pyautogui.click(center)
            pyautogui.moveRel(0,-300)
            state = 0
    
    if c_right == 0 and c_left == 1:
        if state == 0:
            pyautogui.mouseUp()
            pyautogui.click(center)
            pyautogui.moveRel(0,-300)
            state = 1


start = datetime.now().timestamp() * 1000


try:
    while(True):
        pyautogui.mouseUp()
        if((datetime.now().timestamp() * 1000) - start > 5):
            image = d.screenshot()
            set_state_and_color(image,state,start)
        pyautogui.mouseDown()
        #keep mouse pressed
except KeyboardInterrupt:
    sys.exit()


