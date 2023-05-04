import RPi.GPIO as GPIO
import time
 
#######################
####INICIALIZADORES####
#######################

GPIO.setmode(GPIO.BOARD)

servo_pin=12
motor_pin=11

GPIO.setup(servo_pin,GPIO.OUT)
GPIO.setup(motor_pin,GPIO.OUT)

pwservo = GPIO.PWM(servo_pin,50)
pwmotor = GPIO.PWM(motor_pin,100)

pwservo.start(0)
pwmotor.start(0)

###############	
###FUNCIONES###
###############

def get_turn(x):
    if x == 0:
        x = 1
    valor = (x - 320) / 320 # valor en rango de -1 a 1
    porcentaje = valor * 100 # valor e rango de -100 a 100

    return porcentaje

##Recibe un valor entre 0-100:
def set_velocity(x):
	if(x<=0):
		vel=0
	elif(x>100):
		vel=100
	else:
		##Calculamos la velocidad según una regla de tres.
		#Sabemos que nuestros valores oscilan entre 14 y 22
		#Aplicando una regla de tres nos queda la siguiente formula
		vel= ((7.25*x)/100)+14.75
	
	pwmotor.ChangeDutyCycle(vel)	
	print("Velocidad "+str(vel))
	
#Recibe un valor entre -100 y 100
def set_turn(x):
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
	pwservo.ChangeDutyCycle(turn)
	print("Giro "+str(turn))
	
##########
###MAIN###
##########

#VAMOS A RECIBIR UN PARAMETRO POR TECLADO SIMULANDO LA ENTRADA DE LO QUE ESTAMOS DESPLAZADOS DEL CENTRO Y LA VELOCIDAD A LA QUE QUERAMOS IR
try:
	while True:
		g = input("Introduzca distancia del centro (0,640)")
		v = input("Introduzca VELOCIDAD (0,100)")
		
		giro=int(g)
		velocidad= int(v)
		set_turn(get_turn(giro))
		set_velocity(velocidad)
		
except KeyBoardInterrupt:
	pwm.stop()
	GPIO.cleanup()
	



#############################################     BORRADORES        ###############################################################################################
""" 
#VALORES DE PRUEBA PARA IR OSCILANDO
incr = False
valor = 5

incrr = False
valorr = 14.75
"""
#LOS VALORES OSCILAN del servo ENTRE 5 Y 9.5, ESTNAOD RECTOS EN 7
#LOS VALORES DEL MOTOR OSCILAN DEL 14.75 AL 22
"""
try:
	while True:
		if(valor <= 5):
			incr=True
		if(valor>=9):
			incr=False
		
		if(valorr<=10):
			incrr=True
		if(valorr>=25):
			incrr=False
		
			
		if(incr):
			valor+=0.025
		else:
			valor-=0.025
		
		if(incrr):
			valorr+=0.025
		else:
			valorr-=0.025
			
		pwmm.ChangeDutyCycle(valorr)		
		pwm.ChangeDutyCycle(valor)
		print("Valor:"+str(valor))
		print("Valor Motor: "+str(valorr))
		
		time.sleep(0.025)
		
except KeyBoardInterrupt:
	pwm.stop()
	GPIO.cleanup()
	
"""	
	
