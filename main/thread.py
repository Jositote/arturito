import sys
sys.path.append('/usr/local/lib/python3.9/site-packages') 
from multiprocessing import Process
from detect_people import Detector
from servo import Servocar
import time
import cv2
import freenect
import RPi.GPIO as GPIO
import speech_recognition as sr
from buzzer import finish_sound, recognized_sound, start_sound, error_sound
from LED import power_led

def start_detect():
	try:
		hog = cv2.HOGDescriptor()
		hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

		detect = Detector(hog)		
		servo = Servocar()
		while True:
			image, _ = freenect.sync_get_video()
			print("image")
			image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
			depth_data, _ = freenect.sync_get_depth()
			print("depth")
			image = detect.detect_people(image, depth_data)
			print("people")
			center, depth = detect.detect_depth()
			print(depth)
			if len(center) > 0 and depth > 0:
				print(f"moving {center[0]}")
				servo.start(center[0],50)
			else:
				servo.set_velocity(0)
			cv2.imshow('Kinect',image)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	finally:
		print("finishing")
		servo.stop()
		cv2.destroyAllWindows
		freenect.sync_stop()

def rand_move():
	try:
		servo = Servocar()
		servo.random_move()
	finally:
		print("finishing")
		servo.stop()

r = sr.Recognizer()
with sr.Microphone() as source:
	try:
		r.adjust_for_ambient_noise(source)
		while True:
			totalTime = 0
			detectado = False
			audio = r.listen(source)
			try:
				text = r.recognize_google(audio, language='es-ES')
				print(f"Has dicho: {text}")
				if text=="seguir":
					start_sound()
					cv2.namedWindow('Kinect', cv2.WINDOW_NORMAL)
					p = Process(target = start_detect)
					detectado = True
					totalTime = 100
				elif text == "baila":
					start_sound()
					p = Process(target = rand_move)
					detectado = True
					totalTime = 10
				elif text == "apagar":
					break
				else:
					recognized_sound()
				if detectado:
					try:
						p.start()
						time.sleep(totalTime)
					finally:
						finish_sound()
						p.terminate()
						cv2.destroyAllWindows
						freenect.sync_stop()
						
			except sr.UnknownValueError:
				power_led()
				error_sound()
				print("No he podido reconocer lo que has dicho")
				
	except KeyboardInterrupt:
		print ("finish")
		finish_sound()
		GPIO.cleanup()
		
		cv2.destroyAllWindows
		freenect.sync_stop()
	finally:		
		print ("finish")
		finish_sound()
		GPIO.cleanup()
		
		cv2.destroyAllWindows
		freenect.sync_stop()
