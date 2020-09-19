import time
import pandas as pd
from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller
keyboard = Controller()


# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

zcpi = pd.read_csv("zip2propID.csv", index_col=0)
zcpi2 = zcpi.rename(columns = {"ZIP Code" : "Property ID"})
# pIDs = zcpi[1]
# print(pIDs)
print(zcpi2)
# for zipcode in zipcodes:
#     print('Searching properties under ' + str(zipcode) + ' ZIP code...')
#
#     idx = zipcodes.index(zipcode)+1
#     if idx == 1:
#         # Move mouse pointer to internet browser and click on it
#         mouse.position = (617, 842)
#         mouse.press(Button.left)
#         mouse.release(Button.left)
#         print('Now we have moved it to {0}'.format(
#             mouse.position) + ' to open the browser')
#         time.sleep(1)
#
#     # Move mouse pointer to property search bar and click on it
#     mouse.position = (574, 294)
#     print('Now we have moved it to {0}'.format(
#         mouse.position) + ' to click the property search bar')
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#
#     # Type ZIP code in the property search bar and click ENTER
#     keyboard.type(str(zipcode))
#     keyboard.press(Key.enter)
#     keyboard.release(Key.enter)
#     time.sleep(6)
#
#     # Move mouse pointer to 'Export' and click it
#     mouse.position = (1330, 183)
#     print('Now we have moved it to {0}'.format(
#         mouse.position) + ' to click the Export button')
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#     time.sleep(3)
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
