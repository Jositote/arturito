import RPi.GPIO as GPIO
import time

# Define el número de pin que usaremos
led_pin = 17

# Configura la librería GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# Enciende el LED
GPIO.output(led_pin, GPIO.HIGH)

# Espera 5 segundos
time.sleep(5)

# Apaga el LED
GPIO.output(led_pin, GPIO.LOW)

# Limpia los pines GPIO
GPIO.cleanup()
