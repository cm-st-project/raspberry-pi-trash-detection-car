from adafruit_motorkit import MotorKit
import time
kit = MotorKit()

def drive(duration = 1, speed = 1, reverse = False):
    if reverse:
        speed = -1 * speed
    kit.motor1.throttle = speed
    kit.motor2.throttle = speed
    kit.motor3.throttle = speed
    kit.motor4.throttle = speed
    time.sleep(duration)
    stop()
    
def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0  


def right(ROneThree = -1, RTwoFour = 1, sec = 1):
    kit.motor1.throttle = ROneThree
    kit.motor3.throttle = ROneThree
    kit.motor2.throttle = RTwoFour
    kit.motor4.throttle = RTwoFour
    time.sleep(sec)
    stop()
    
def left(LOneThree = 1, LTwoFour = -1, lSec = 1):
    kit.motor1.throttle = LOneThree
    kit.motor3.throttle = LOneThree
    kit.motor2.throttle = LTwoFour
    kit.motor4.throttle = LTwoFour
    time.sleep(lSec)
    stop()

drive(duration = 1, speed = 0.5, reverse = True)
right(ROneThree = -1, RTwoFour = 1, sec = 1)
left(LOneThree = 1, LTwoFour = -1, lSec = 1)
print("done")