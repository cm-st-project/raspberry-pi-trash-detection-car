from adafruit_motorkit import MotorKit
import time
kit = MotorKit()

    
def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0  


stop()
print("done")
