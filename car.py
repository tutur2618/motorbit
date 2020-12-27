from microbit import *
import radio
display.scroll('6')

def generic_wheel(speed,speed_pin,dir_pin):
    """speed is from 0 to 100. negative value means backward"""
    #first: set direction:
    if speed<0:
        dir_pin.write_digital(1)
        speed = -speed
    else:
        dir_pin.write_digital(0)

    #second: set speed on pin1 with PWM
    #val = speed * 1023 // 100
    speed_pin.write_analog(speed)


def rightwheel(speed):
    generic_wheel(speed,speed_pin=pin1,dir_pin=pin8)
    

def leftwheel(speed):
    generic_wheel(-speed,speed_pin=pin2,dir_pin=pin12)
    
    
def wheels(leftspeed,rightspeed):
    leftwheel(leftspeed)
    rightwheel(rightspeed)

speed=700
radio.on()
while True:
    cmd = None
    while cmd is None:
        cmd = radio.receive()
    if cmd == 'forward':
        wheels(speed,speed)
        display.show(Image.HEART)
    elif cmd == 'left':
        wheels(0,speed)
        display.show(Image.HAPPY)
    elif cmd == 'right':
        wheels(speed,0)
        display.show(Image.SAD)
    
        
    elif cmd == 'backward' :
        wheels(-speed,-speed)
        display.show(Image.SURPRISED)
    elif cmd == 'stop' :
        wheels(0,0)
        display.show(Image.TRIANGLE)
        






    
    
    