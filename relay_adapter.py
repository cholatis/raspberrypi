import RPi.GPIO as GPIO
from time import sleep


relay_pins = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pins, GPIO.OUT)

GPIO.output(relay_pins, 1)


try:
	while True:
		GPIO.output(relay_pins, 0)
		sleep(5)
		GPIO.output(relay_pins, 1)
		sleep(5)
except KeyboardInterrupt:
	pass

GPIO.cleanup()


