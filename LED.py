import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#init
GPIO.setup(18, GPIO.OUT)

print "LED on"

GPIO.output(18, GPIO.HIGH)
time.sleep(3)

print "LED off"

GPIO.output(18, GPIO.LOW)


