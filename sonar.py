import RPi.GPIO as GPIO
import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.D5,echo_pin = board.D6)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("retry")
    time.sleep(0.1)

trigPin = 5
echoPin = 6

GPIO.setmode(GPIO.BCM )

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)



print('start')

    

while True:
#    GPIO.output(trigPin, False)
 #   time.sleep (1.5)
    GPIO.output(trigPin, True)
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
    
    pulse_start = time.time()
    pulse_end = time.time()

    print('start pulse')
    while GPIO.input(echoPin) == 0:
        pluse_start = time.time()
        
    print('emd pulse')
    while GPIO.input (echoPin) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    
    distance = (pulse_duration * 34300) / 2
    
    #print(pulse_duration, distance)
    print(distance)
