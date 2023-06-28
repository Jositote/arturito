import sys
sys.path.append('/usr/local/lib/python3/dist-packages') 
import freenect
import cv2
import numpy as np

def depth_callback():
    print("hi")
    # Convert the raw depth data to a numpy array
    depth= freenect.sync_get_depth()
    
    depth_thresh = np.array(depth).astype(np.uint16)

    # Apply a threshold to filter out the background
    #depth_thresh = cv2.threshold(depth, 1000, 65535, cv2.THRESH_BINARY)[1]

    # Find the contours of the depth data
    contours, _ = cv2.findContours(depth_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour (presumably the person)
    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)

        # Find the centroid of the largest contour
        M = cv2.moments(largest_contour)
        if M["m00"] > 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Calculate the distance from the Kinect sensor
            depth_value = depth[cy, cx]
            distance = 1.0 / (-0.00307 * depth_value + 3.33)

            # Create a visualization of the depth data
            depth_viz = cv2.applyColorMap(cv2.convertScaleAbs(depth, alpha=0.03), cv2.COLORMAP_JET)
            cv2.drawContours(depth_viz, [largest_contour], -1, (0, 255, 0), 2)
            cv2.circle(depth_viz, (cx, cy), 5, (0, 0, 255), -1)
            cv2.putText(depth_viz, f"{distance:.2f}m", (cx + 10, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

            # Display the visualization
            cv2.imshow("Depth", depth_viz)
            cv2.waitKey(1)

while True:
	depth_callback()
