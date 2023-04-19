import speech_recognition as sr
import RPi.GPIO as GPIO
import time

# establecer el modo de pines GPIO
GPIO.setmode(GPIO.BOARD)

# pines GPIO a los que está conectado el controlador de motor
motor1_pin1 = 7
motor1_pin2 = 11
motor2_pin1 = 13
motor2_pin2 = 15

# pines GPIO a los que está conectado el servo motor
servo_pin = 12

# establecer los pines GPIO como salidas
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)

# crear objetos PWM para controlar el servo y el controlador de motor
pwm_servo = GPIO.PWM(servo_pin, 50)  # frecuencia de 50 Hz
pwm_motor1_pin1 = GPIO.PWM(motor1_pin1, 50)
pwm_motor1_pin2 = GPIO.PWM(motor1_pin2, 50)
pwm_motor2_pin1 = GPIO.PWM(motor2_pin1, 50)
pwm_motor2_pin2 = GPIO.PWM(motor2_pin2, 50)

# mover el servo a la posición inicial
pwm_servo.start(0)  # duty cycle del 0%

# detener los motores
pwm_motor1_pin1.start(0)
pwm_motor1_pin2.start(0)
pwm_motor2_pin1.start(0)
pwm_motor2_pin2.start(0)

def forward():
    # mover el coche hacia adelante
    pwm_motor1_pin1.ChangeDutyCycle(100)
    pwm_motor1_pin2.ChangeDutyCycle(0)
    pwm_motor2_pin1.ChangeDutyCycle(100)
    pwm_motor2_pin2.ChangeDutyCycle(0)

def backward():
    # mover el coche hacia atrás
    pwm_motor1_pin1.ChangeDutyCycle(0)
    pwm_motor1_pin2.ChangeDutyCycle(100)
    pwm_motor2_pin1.ChangeDutyCycle(0)
    pwm_motor2_pin2.ChangeDutyCycle(100)

def left():
    # girar el coche a la izquierda
    pwm_servo.ChangeDutyCycle(10)  # duty cycle del 10%

def right():
    # girar el coche a la derecha
    pwm_servo.ChangeDutyCycle(5)  # duty cycle del 5%

def stop():
    # detener el coche
    pwm_motor1_pin1.ChangeDutyCycle(0)
    pwm_motor1_pin2.ChangeDutyCycle(0)
    pwm_motor2_pin1.ChangeDutyCycle(0)
    pwm_motor2_pin2.ChangeDutyCycle(0)

# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

while True:

    # Seleccionar la tarjeta de sonido como fuente de audio
    with sr.Microphone() as source:
        while True:

            print("Da la instrucción...")
            # Calibrar el nivel de ruido de fondo
            r.adjust_for_ambient_noise(source)
            # Escuchar el audio de la tarjeta de sonido
            audio = r.listen(source)

            # Intentar reconocer el audio
            try:
            # Utilizar el servicio de reconocimiento de voz de Google
                text = r.recognize_google(audio, language='es-ES')
                print("Has dicho: {text}")
                #Movemos el servomotor según el comando recibido
                if(text=="adelante" or text == "acelera"):
                    forward()
                if(text=="marcha atrás" or text=="atras" or text=="retrocede")
                    backward()
                if(text=="izquierda" or text=="gira a la izquierda" ):
                    left()
                if(text=="derecha" or text=="gira a la derecha"):
                	right()
                if(text=="para" or text=="parate" or text=="frena"):
                    stop()
                if(text=="salir")
                	# detener el objeto PWM y limpiar los pines GPIO
                    stop()
                    GPIO.cleanup()
                else:
                	print("Comando no válido")
            except sr.UnknownValueError:
                print("No he podido reconocer lo que has dicho")
            except sr.RequestError as e:
                print("Error al conectarse al servicio de reconocimiento de voz: {e}")
            except KeyboardInterrupt:
                # detener el objeto PWM y limpiar los pines GPIO
                pwm.stop()
                GPIO.cleanup()