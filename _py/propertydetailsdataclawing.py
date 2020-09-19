import time
import pandas as pd
from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller
keyboard = Controller()


# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

zcpi = pd.read_csv("zip2propID.csv", index_col='ZIPCode', header=0)
ZIPs = list(zcpi.index.values)
pIDs = list(zcpi.PropertyID)
for zip in ZIPs:
    zip =ZIPs[0]
    # print('Searching properties under ' + str(zip) + ' ZIP code...')
    # print('Property ID is ' + str(pIDs[ZIPs.index(zip)]))


    idx = ZIPs.index(zip)+1
    if idx == 1:
        # Move mouse pointer to internet browser and click on it
        mouse.position = (617, 842)
        mouse.press(Button.left)
        mouse.release(Button.left)
        print('Now we have moved it to {0}'.format(
            mouse.position) + ' to open the browser')
        time.sleep(1)

    # Move mouse pointer to property search bar and click on it
    mouse.position = (574, 294)
    print('Now we have moved it to {0}'.format(
        mouse.position) + ' to click the property search bar')
    mouse.press(Button.left)
    mouse.release(Button.left)

    # Type property ID in the property search bar and click ENTER
    keyboard.type(str(pIDs[ZIPs.index(zip)]))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(7)

    # Move mouse pointer to 'Details' and click it
    mouse.position = (1326, 320)
    print('Now we have moved it to {0}'.format(
        mouse.position) + ' to click the Export button')
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(3)
#
#     # CLick ENTER when asking how to save it
#     keyboard.press(Key.enter)
#     keyboard.release(Key.enter)
#     time.sleep(2)
#
#     # Move mouse pointer to 'New Search' and click it
#     mouse.position = (1455, 179)
#     print('Now we have moved it to {0}'.format(
#         mouse.position) + ' to click the New Search button')
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#     time.sleep(4)
#
#     # # Click BACKSPACE on keyboard to go back to property search
#     # keyboard.press(Key.backspace)
#     # keyboard.release(Key.backspace)
#     #
#     #
#     # Click on property search bar, click on it, and hold BACKSPACE
#     mouse.position = (574, 294)
#     print('Now we have moved it to {0}'.format(
#         mouse.position) + ' to click the property search bar')
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#     keyboard.press(Key.backspace)
#     # time.sleep(2)
#     # keyboard.release(Key.backspace)
#     # print('...Done!')
