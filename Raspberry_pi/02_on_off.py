
import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,0)
for i in range(5): 
    GPIO.output(17,1)
    time.sleep(1)
    GPIO.output(17,0)
    time.sleep(1)
GPIO.cleanup()
