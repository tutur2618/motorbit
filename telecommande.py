# Add your Python code here. E.g.
from microbit import *
import radio
display.scroll('1')
radio.on()
#reading = accelerometer.get_x()_
left=False
right=False
back = False
stopped = False
while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
        if right:
            radio.send('forward')
            right=False
        else:
            radio.send('left')
            left=True
    elif button_b.was_pressed():
        display.show(Image.SAD)
        if left:
            radio.send('forward')
            left=False
        else:
            radio.send('right')
            right=True
    elif pin_logo.is_touched():
        display.show(Image.HEART)
        if back :
            radio.send('forward')
            back = False
        else :
            radio.send('backward')
            back = True
    else:
        gesture = accelerometer.current_gesture()
        if gesture == "shake":
            display.show(Image.TRIANGLE)
            if stopped:
                radio.send('forward')
                stopped = False
            else:
                radio.send('stop')
                stopped = True