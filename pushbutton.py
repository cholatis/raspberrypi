import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pushpin = 17
#init
GPIO.setup(pushpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	state = GPIO.input(pushpin)
	if state == False:
		print "button press"
		time.sleep(0.2)



