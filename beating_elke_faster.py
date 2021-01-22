from datetime import datetime
import pyautogui
from pynput import keyboard
import sys


pyautogui.screenshot(region=(977,47,1584,1393), 'screen.png')

"""

#center button to switch sides 1280,1220
#left button 1080, 1220
#right button 1480
left = (1080,1220)
center = (1280,1220)
right = (1480,1220)

#state 0 blue left red right
state = 0

#left first bound
l1 = 2049000
#left second bound
l2 =2049200

#right first bound
r1 = 2049380
#right second bound
r2 = 2049560

#height for pixels in the middle

#left end of the screen
#1000  and right 1560
# left end of left 1200
# right end of right 1360


def on_press(key):
    sys.exit()

def on_release(key):
    sys.exit()

def set_state_and_color(px_list, state, time):
    time = datetime.now()
    #col left red 1 blue 0
    c_left = -1
    #col left red 1 blue 0
    c_right = -1

    #check color left
    for i in range(l1,l2):
        if px_list[i][0] > 200 and px_list[i][2] < 200:
            #left is red
            c_left = 1
        elif px_list[i][0] < 200 and px_list[i][2] > 200:
            #left is blue
            c_left = 0
    #check for color on right and left
    for i in range(r1,r2):
        if px_list[i][0] > 200 and px_list[i][2] < 200:
            #right is red
            c_right = 1
        elif px_list[i][0] < 200 and px_list[i][2] > 200:
            #righ is blue
            c_right = 0

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

#keylistener
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


while(True):
    if((datetime.now().timestamp() * 1000) - start > 5):
        image = pyautogui.screenshot()
        pixel_val = list(image.getdata())
        set_state_and_color(pixel_val,state,start)
    pyautogui.mouseDown()
    #keep mouse pressed


"""