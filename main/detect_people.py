import sys
sys.path.append('/home/arturito/.local/lib/python3.9/site-packages')
import cv2

class Detector:
	def __init__(self, hog):
		self.hog = hog
		self.centers = []
		self.depth_data =[]
	
	def detect_people(self, image, depth_data):
		self.depth_data = depth_data
		humans, _ = self.hog.detectMultiScale(image, winStride=(8, 8))
		
		for (x, y, w, h) in humans:
			pad_w, pad_h = int(0.15 * w), int(0.01 * h)
			cv2.rectangle(image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)
			self.centers.append([int(x+w/2), int(y+h/2)])
			cv2.circle(image, (int(x+w/2), int(y+h/2)), 5, (0, 255, 0), -1)
		return image
		
	def detect_depth(self):
		minDistance = 10
		minCenters = []
		if len(self.centers) > 0:
			
			for x,y in self.centers:
				depth_value = self.depth_data[y, x]
				distance = 1.0 / (-0.00307 * depth_value + 3.33)
				if distance < minDistance:
					minDistance = distance
					minCenters = [x,y]
		
		self.centers = []
		return minCenters, minDistance
