import sys
sys.path.append('/usr/local/lib/python3/dist-packages') 
import freenect
import cv2

while True:
	array , _ = freenect.sync_get_video()
	array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)

	
	cv2.imshow('Video',array)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows
freenect.sync_stop()
