import RPi.GPIO as GPIO
import time

def power_led():

	led_pin = 24
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led_pin, GPIO.OUT)
	
	GPIO.output(led_pin, GPIO.HIGH)
	time.sleep(1)

	GPIO.output(led_pin, GPIO.LOW)
	GPIO.cleanup()

