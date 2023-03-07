import speech_recognition as sr
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
# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

# mover el servo a la posición inicial
pwm.start(0)  # duty cycle del 0%


while True:
        
    # Seleccionar la tarjeta de sonido como fuente de audio
    with sr.Microphone() as source:
        while True:
            
            print("Da la instruccion...")
            # Calibrar el nivel de ruido de fondo
            r.adjust_for_ambient_noise(source)
            # Escuchar el audio de la tarjeta de sonido
            audio = r.listen(source)
        
            # Intentar reconocer el audio
            try:
                # Utilizar el servicio de reconocimiento de voz de Google
                text = r.recognize_google(audio, language='es-ES')
                print(f"Has dicho: {text}")
		#Movemos el servomotor según el comando recibido
		if(text=="cero"):
			# mover el servo a la posición 0 grados
        		pwm.ChangeDutyCycle(2.5)  # duty cycle del 2.5%
		if(text=="noventa"):
			# mover el servo a la posición 90 grados
        		pwm.ChangeDutyCycle(7.5)  # duty cycle del 7.5%
		if(text=="mitad"):
			# mover el servo a la posición 180 grados
        		pwm.ChangeDutyCycle(12.5)  # duty cycle del 12.5%
		if(text=="salir")
			# detener el objeto PWM y limpiar los pines GPIO
    			pwm.stop()
    			GPIO.cleanup()	

		else:
			print("Comando no válido")
		
		time.sleep(1)

            except sr.UnknownValueError:
                print("No he podido reconocer lo que has dicho")
            except sr.RequestError as e:
                print(f"Error al conectarse al servicio de reconocimiento de voz: {e}")
	except KeyboardInterrupt:
    		# detener el objeto PWM y limpiar los pines GPIO
    		pwm.stop()
    		GPIO.cleanup()

"""
Revisar las indentaciones, puesto que lo he programado en el bloc de notas y quizás algo me haya fallado.
Revisar el while True si ahí está bien o mejor antes del with sr.Microphone() as source
Comprobar si al transformar el texto de voz a sonido (en la línea dónde se crea la variable text) la primera letra es mayúsculas, todas minúsculas, etc. Ya que es importante para la comparación. 
"""
