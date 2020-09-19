import time
from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller
keyboard = Controller()


# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# [78002, 78023, 78054, 78069, 78073, 78101, 78109, 78112, 78148,
#             78150, 78152, 78201, 78202, 78203, 78204, 78205, 78206, 78207,
#             78208, 78209, 78210, 78211, 78212, 78213, 78214, 78215, 78216,
#             78217, 78218, 78219, 78220, 78221, 78222, 78223, 78224, 78225,
#             78226, 78227, 78228, 78229, 78230, 78231, 78232, 78233,	78234,
#             78235, 78236, 78237, 78238,	78239, 78240, 78241, 78242, 78243,
#             78244, 78245, 78246, 78247, 78248, 78249, 78250, 78251, 78252,
#             78253, 78254,
zipcodes = [78255, 78256, 78257, 78258, 78259, 78260, 78261,
            78262, 78263, 78264, 78265, 78268, 78269, 78270, 78275, 78278,
            78279, 78280, 78283, 78284, 78285, 78286, 78287, 78288, 78289,
            78291, 78292, 78293, 78294, 78295, 78296, 78297, 78298, 78299]

    # [78002, 78015, 78023, 78039, 78054, 78069, 78073, 78101, 78108,
    #         78109, 78112, 78124, 78150, 78148, 78152, 78154, 78163, 78201,
    #         78203, 78202, 78205, 78204, 78207, 78206, 78209, 78208, 78211,
    #         78210, 78213, 78212, 78215, 78214, 78217, 78216, 78219, 78218,
    #         78221, 78220, 78223, 78222, 78225, 78224, 78227, 78226, 78229,
    #         78228, 78231, 78230, 78233, 78232, 78235, 78234, 78237, 78236,
    #         78239, 78238, 78240, 78243, 78242, 78245, 78244, 78247, 78249,
    #         78248, 78251, 78250, 78253, 78252, 78255, 78254, 78257, 78256,
    #         78259, 78258, 78261, 78260, 78263, 78265, 78264, 78266, 78280,
    #         78279, 78284, 78288]

for zipcode in zipcodes:
    print('Searching properties under ' + str(zipcode) + ' ZIP code...')

    idx = zipcodes.index(zipcode)+1
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

    # Type ZIP code in the property search bar and click ENTER
    keyboard.type(str(zipcode))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(6)

    # Move mouse pointer to 'Export' and click it
    mouse.position = (1330, 183)
    print('Now we have moved it to {0}'.format(
        mouse.position) + ' to click the Export button')
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(3)

    # CLick ENTER when asking how to save it
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    # Move mouse pointer to 'New Search' and click it
    mouse.position = (1455, 179)
    print('Now we have moved it to {0}'.format(
        mouse.position) + ' to click the New Search button')
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(4)

    # # Click BACKSPACE on keyboard to go back to property search
    # keyboard.press(Key.backspace)
    # keyboard.release(Key.backspace)
    #
    #
    # Click on property search bar, click on it, and hold BACKSPACE
    mouse.position = (574, 294)
    print('Now we have moved it to {0}'.format(
        mouse.position) + ' to click the property search bar')
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press(Key.backspace)
    # time.sleep(2)
    # keyboard.release(Key.backspace)
    # print('...Done!')
