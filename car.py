from microbit import *
import radio

display.scroll('3')


def generic_wheel(speed, speed_pin, dir_pin):
    """speed is from 0 to 100. negative value means backward"""
    # first: set direction:
    if speed < 0:
        dir_pin.write_digital(1)
        speed = -speed
    else:
        dir_pin.write_digital(0)

    # second: set speed on pin1 with PWM
    # val = speed * 1023 // 100
    speed_pin.write_analog(speed)


def get_speed():
    cmdbytes = bytearray()
    while len(cmdbytes) < 6:
        cmd = None
        while cmd is None:
            cmd = radio.receive_bytes()
        cmdbytes += cmd
    leftbytes = cmdbytes[0:3]
    rightbytes = cmdbytes[3:6]
    leftspeed = int.from_bytes(leftbytes[0:2], 'little')
    rightspeed = int.from_bytes(rightbytes[0:2], 'little')
    if leftspeed > 1023:
        leftspeed = 1  # if radio sends non sens, we stop
    if rightspeed > 1023:
        rightspeed = 1  # if radio sends non sens, we stop
    if leftbytes[2]:
        leftspeed = -leftspeed
    if rightbytes[2]:
        rightspeed = -rightspeed
    # display.scroll(str(leftspeed))
    return (leftspeed, rightspeed)


def rightwheel(speed):
    generic_wheel(speed, speed_pin=pin1, dir_pin=pin8)


def leftwheel(speed):
    generic_wheel(-speed, speed_pin=pin2, dir_pin=pin12)


def wheels(leftspeed, rightspeed):
    leftwheel(leftspeed)
    rightwheel(rightspeed)


radio.on()
while True:
    leftspeed, rightspeed = get_speed()
    # display.scroll(str(leftspeed))
    # display.scroll(str(rightspeed))
    wheels(leftspeed, rightspeed)

