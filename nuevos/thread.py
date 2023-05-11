import sys
sys.path.append('/usr/local/lib/python3/dist-packages') 
from multiprocessing import Process
from detect_people import Detector
from servo import Servocar
import time
import sys
import cv2
import freenect
import RPi.GPIO as GPIO
import speech_recognition as sr
from buzzer import buzzer



def start_detect():
	try:
		hog = cv2.HOGDescriptor()
		hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

		detect = Detector(hog)		
		servo = Servocar()
		while True:
			image , _ = freenect.sync_get_video()
			print("image")
			image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
			depth_data, _ = freenect.sync_get_depth()
			print("depth")
			image = detect.detect_people(image, depth_data)
			print("people")
			center, depth = detect.detect_depth()
		
			if len(center) > 0:
				print(f"moving {center[0]}")
				
				servo.start(center[0],0)
			cv2.imshow('Video',image)
	finally:
		servo.stop()
		cv2.destroyAllWindows
		freenect.sync_stop()

def rand_move():
	try:
		servo = Servocar()
		servo.random_move()
	finally:
		servo.stop()

r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	while True:
		detectado = False
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio, language='es-ES')
			print(f"Has dicho: {text}")
			if(text=="seguir"):
				p = Process(target = start_detect)
				detectado = True
			elif text == "canta":
				p = Process(target = buzzer)
				detectado = True
			elif text == "baila":
				p = Process(target = rand_move)
				detectado = True
			if detectado:
				try:
					p.start()
					time.sleep(10.0)
				finally:
					p.terminate()
		except sr.UnknownValueError:
				print("No he podido reconocer lo que has dicho")
