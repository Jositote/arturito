import RPi.GPIO as GPIO
import time
import random

class Servocar:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		self.servo_pin=18
		self.motor_pin=17

		GPIO.setup(self.servo_pin,GPIO.OUT)
		GPIO.setup(self.motor_pin,GPIO.OUT)

		self.pwservo = GPIO.PWM(self.servo_pin,50)
		self.pwmotor = GPIO.PWM(self.motor_pin,100)

		self.pwservo.start(0)
		self.pwmotor.start(0)

	def get_turn(self, x):
		if x == 0:
			x = 1
		valor = (x - 320) / 320 # valor en rango de -1 a 1
		porcentaje = valor * 100 # valor e rango de -100 a 100

		return porcentaje

	def set_velocity(self, x):
		if(x<=0):
			vel=0
		elif(x>100):
			vel=100
		else:
			##Calculamos la velocidad según una regla de tres.
			#Sabemos que nuestros valores oscilan entre 14 y 22
			#Aplicando una regla de tres nos queda la siguiente formula
			vel= ((7.25*x)/100)+14.75
		
		self.pwmotor.ChangeDutyCycle(vel)	
		print("Velocidad "+str(vel))
		
	def set_turn(self, x):
		if(x<-100):
			x=-100
		elif(x>100):
			x=100
		else:
			#Primero vamos a transformar nuestro valor de entrada por un rango positivo, por eso vamos a mover todos los valores 100 unidades más.
			x=x+100
			##Calculamos el giro según una regla de tres.
			#Sabemos que nuestros valores oscilan entre 5 y 9.5, siendo 7 que esté recto
			#Aplicando una regla de tres nos queda la siguiente formula
			turn = ((4.5*x)/200)+5
		self.pwservo.ChangeDutyCycle(turn)
		print("Giro "+str(turn))
	
	def start(self, giro, velocidad):
		self.set_turn(self.get_turn(giro))
		self.set_velocity(velocidad)
		
	def random_move(self):		
		while True:
			self.set_turn(random.randint(-100,100))
			time.sleep(0.5)
			
	def stop(self):
		self.pwservo.stop()
		self.pwmotor.stop()
	
