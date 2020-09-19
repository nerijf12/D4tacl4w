from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# Set pointer position
mouse.position = (617, 842)
print('Now we have moved it to {0}'.format(
    mouse.position) + ' to open the browser')

# Move pointer relative to current position
# mouse.move(5, -5)

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

# Set pointer position
mouse.position = (574, 294)
print('Now we have moved it to {0}'.format(
    mouse.position) + ' to click the property search bar')

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

# Set pointer position
# mouse.position = (1352, 189)
# print('Now we have moved it to {0}'.format(
#     mouse.position) + ' to click the Export button')
#
# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on macOS
# mouse.click(Button.left, 2)

# Scroll two steps down
# mouse.scroll(0, 2)