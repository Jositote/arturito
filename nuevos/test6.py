import sys
sys.path.append('/usr/local/lib/python3/dist-packages') 
import freenect
import numpy as np

# Set up the Freenect device
#dev = freenect.open_device(freenect.init(), 0)

# Start the depth stream
#freenect.start_depth(dev)

# Wait for the depth data to be captured
input("Press any key to capture depth data...")
while True:
	# Get the depth data
	depth_data, _ = freenect.sync_get_depth()

	# Get the depth value of the center pixel
	cx = depth_data.shape[1] // 2
	cy = depth_data.shape[0] // 2
	depth_value = depth_data[cy, cx]

	# Calculate the distance to the center pixel
	distance = 1.0 / (-0.00307 * depth_value + 3.33)

	# Print the distance
	print(f"Distance to center pixel: {distance:.2f}m")

