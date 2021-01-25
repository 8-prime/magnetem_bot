import pyautogui
import sys
import d3dshot
import numpy as np
from time import sleep

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

y = 800
#left bound for checking
# x = 980 -> 1100
# y = 800

#right bound for checking
# x = 1460 -> 1580
# y = 800

#color encoding 
# -1 = no color found
# 0 = blue
# 1 = red


c_left_prev = -1
c_right_prev = -1

c_left = -1
c_right = -1

while(True):
    #take screenshot
    image = d.screenshot()
    c_left_prev = c_left
    c_right_prev = c_right
    c_left = -1
    c_right = -1
    #loop trough small areas to check for non black/grey pixels
    #left
    for i in range(980,1100):
        blue = image[y,i][2]
        red = image[y,i][0]
        if blue > 240 and red < 100:
            c_left = 0
            break;
        if red > 150 and blue < 50:
            c_left = 1
            break;
    #right
    for i in range(1460,1580):
        blue = image[y,i][2]
        red = image[y,i][0]
        if blue > 240 and red < 100:
            c_right = 0
            break;
        if red > 150 and blue < 50:
            c_right = 1
            break;

    if c_left == -1 and c_right == -1 or c_left == c_left_prev and c_right == c_left_prev:
        continue
    else:
        pyautogui.mouseUp()
        #only blue
        if c_left != 1 and c_right != 1:
            pyautogui.moveTo(left)
            pyautogui.mouseDown()
        #only red
        if c_left != 0 and c_right != 0:
            pyautogui.moveTo(right)
            pyautogui.mouseDown()

        #blue from left red from right and state is not 0
        if c_left == 0 and c_right == 1 and state == 1:
            pyautogui.moveTo(center)
            pyautogui.mouseDown()
            sleep(0.1)
            pyautogui.mouseUp()
            state = 0
        #blue from right and red from left and state is not 1
        if c_left == 1 and c_right == 0 and state == 0:
            pyautogui.moveTo(center)
            pyautogui.mouseDown()
            sleep(0.1)
            pyautogui.mouseUp()
            state = 1