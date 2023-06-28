import sys
sys.path.append('/usr/local/lib/python3/dist-packages') 
import freenect
import numpy as np
from PIL import Image

while True:
	array, _ = freenect.sync_get_video()
	array = np.rot90(array)
	array = np.fliplr(array)
	
	img = Image.fromarray(array)
	img.show()
	
	if input() == 'q':
		break
		
freenect.sync_stop()
  
