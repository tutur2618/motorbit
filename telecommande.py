# Add your Python code here. E.g.
from microbit import *
import radio
display.scroll('4')
radio.on()

def send_speeds(leftspeed,rightspeed):
    cmd = bytearray()
    cmd += abs(leftspeed).to_bytes(2,'little')
    if leftspeed < 0:
        cmd += b'\x01'
    else:
        cmd += b'\x00'
    cmd += abs(rightspeed).to_bytes(2,'little')
    if rightspeed < 0:
        cmd += b'\x01'
    else:
        cmd += b'\x00'
    radio.send_bytes(cmd)

left=False
right=False
back = False
stopped = False
speed = 1000
while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
        if right:
            send_speeds(speed,speed) # forward
            right=False
        else:
            send_speeds(0,speed) # left turn
            left=True
    elif button_b.was_pressed():
        display.show(Image.SAD)
        if left:
            send_speeds(speed,speed) # forward
            left=False
        else:
            send_speeds(speed,0) # right turn
            right=True
    elif pin_logo.is_touched():
        display.show(Image.HEART)
        if back :
            send_speeds(speed,speed) # forward
            back = False
        else:
            send_speeds(-speed, -speed) # backward
            back = True
        sleep(700)
        display.clear()
        sleep(300)
    else:
        gesture = accelerometer.current_gesture()
        if gesture == "shake":
            display.show(Image.TRIANGLE)
            if stopped:
                send_speeds(speed,speed) # forward
                stopped = False
            else:
                send_speeds(0, 0)  # stop
                stopped = True
            sleep(700)
            display.clear()
            sleep(300)