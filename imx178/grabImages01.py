
# This is my first whack and getting image data from the IMX178 wifi camera.
# The camera's IP address is hardwared to 192.168.42.10 and has the user name admin
# with no password.

import dvrip as dvr
import cv2
import time
import os

deviceInfo = 'rtsp://192.168.42.10:554/user=admin&password=&channel=1&stream=0.sdp'

print ('deviceInfo : ', deviceInfo)

capture = cv2.VideoCapture(deviceInfo)

#percent by which the image is resized

scale_percent = 25

while (True):
	ret, imageFrame = capture.read()

	#calculate the percent of original dimensions
	width = int(imageFrame.shape[1] * scale_percent / 100)
	height = int(imageFrame.shape[0] * scale_percent / 100)

	# dsize
	dsize = (width, height)

	# resize image. Using INTER_AREA as that is supposed to yield the best
	# results when reducing an image.

	reducedFrame = cv2.resize(imageFrame, dsize, cv2.INTER_AREA)

	cv2.imshow('frame', reducedFrame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		cv2.release()
		break
