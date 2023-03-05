import RPi.GPIO as GPIO
import time

# Define el número de pin que usaremos
led_pin = 24

# Configura la librería GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:
	while True:
		# Enciende el LED
		GPIO.output(led_pin, GPIO.HIGH)

		print("Led H")
		# Espera 5 segundos
		time.sleep(1)

		# Apaga el LED
		GPIO.output(led_pin, GPIO.LOW)
		print("Led L")
		
		# Espera 5 segundos
		time.sleep(1)
	
except KeyboardInterrupt:
    # detener el objeto PWM y limpiar los pines GPIO
    pwm.stop()
    GPIO.cleanup()
