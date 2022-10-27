import RPi.GPIO as GPIO
from time import sleep


relay_pins = [26]
led_pins = [21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pins, GPIO.OUT)
GPIO.setup(led_pins, GPIO.OUT)
GPIO.output(relay_pins, 1)
GPIO.output(led_pins, 1)

try:
	while True:
		for pin in relay_pins:
			GPIO.output(pin, 0)
			sleep(2)
		for pin in relay_pins:
			GPIO.output(pin, 1)
			sleep(2)
except KeyboardInterrupt:
	pass

GPIO.cleanup()


