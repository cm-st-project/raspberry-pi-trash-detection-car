from adafruit_motorkit import MotorKit
import time
import RPi.GPIO as GPIO
import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.D5,echo_pin = board.D6)




print('start')

   

kit = MotorKit()

def drive(speed = 0.25, reverse = False):
    if reverse:
        speed = -1 * speed
    kit.motor1.throttle = speed
    kit.motor2.throttle = speed
    kit.motor3.throttle = speed
    kit.motor4.throttle = speed

def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0  


def right(speed = 0.25, reverse = False):
    if reverse:
        speed = -1 * speed
    kit.motor1.throttle = speed
    kit.motor2.throttle = speed
    kit.motor3.throttle = -1 * speed
    kit.motor4.throttle = -1 * speed

def left(speed = 0.25, reverse = False):
	right(speed, not reverse)
    
    
#drive(duration = 2, speed = 0.5)
#drive(duration = 2, speed = 0.5, reverse = True)
#stop()
#right(1,1)
#left(1,1)

stop()


exit()

safe = True
safe_dist = 50 # in cm
speed = 0.5
sleep_time = 0.05
turn_speed = .75
turn_sleep_time = 0.1


while True:
	try:
		if safe:
			dist = sonar.distance
			print("forward sonar:", dist)
			if dist > safe_dist:
				drive(speed)
			else:
				safe = False
				stop()
				print(dist)
			time.sleep(sleep_time)


		else:
			dist = sonar.distance
			print("turning sonar:", dist)
			if dist < safe_dist:
				right(turn_speed)
			else:
				safe = True
				stop()
				print(dist)
			
			time.sleep(turn_sleep_time)
	except RuntimeError:
		print("retry")

stop()
print("done")
