import RPi.GPIO as GPIO
import time

# establecer el modo de pines GPIO
GPIO.setmode(GPIO.BOARD)

# pin GPIO al que está conectado el servo
servo_pin = 12

# establecer el pin GPIO como salida
GPIO.setup(servo_pin, GPIO.OUT)

# crear un objeto PWM para controlar el servo
pwm = GPIO.PWM(servo_pin, 50)  # frecuencia de 50 Hz

# mover el servo a la posición inicial
pwm.start(0)  # duty cycle del 0%

try:
    while True:
        # mover el servo a la posición 0 grados
        pwm.ChangeDutyCycle(2.5)  # duty cycle del 2.5%
        time.sleep(1)

        # mover el servo a la posición 90 grados
        pwm.ChangeDutyCycle(7.5)  # duty cycle del 7.5%
        time.sleep(1)

        # mover el servo a la posición 180 grados
        pwm.ChangeDutyCycle(12.5)  # duty cycle del 12.5%
        time.sleep(1)

except KeyboardInterrupt:
    # detener el objeto PWM y limpiar los pines GPIO
    pwm.stop()
    GPIO.cleanup()