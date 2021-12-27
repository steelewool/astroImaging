
# This is my first whack and getting image data from the IMX178 wifi camera.
# The camera's IP address is hardwared to 192.168.42.10 and has the user name admin
# with no password.

import dvrip as dvr
import cv2
import time


deviceInfo = 'rtsp://192.168.42.10:554/user=admin&password=&channel=1&stream=0.sdp'

print ('deviceInfo : ', deviceInfo)

capture = cv2.VideoCapture(deviceInfo)

#percent by which the image is resized

scale_percent = 25

print ('cv2.CAP_PROP_POS_MSEC       : ', cv2.CAP_PROP_POS_MSEC)
print ('cv2.CAP_PROP_POS_FRAMES     : ', cv2.CAP_PROP_POS_FRAMES)
print ('cv2.CAP_PROP_POS_AVI_RATIO  : ', cv2.CAP_PROP_POS_AVI_RATIO)
print ('cv2.CAP_PROP_FRAME_WIDTH    : ', cv2.CAP_PROP_FRAME_WIDTH)
print ('cv2.CAP_PROP_FRAME_HEIGHT   : ', cv2.CAP_PROP_FRAME_HEIGHT)
print ('cv2.CAP_PROP_FPS            : ', cv2.CAP_PROP_FPS)
print ('cv2.CAP_PROP_FOURCC         : ', cv2.CAP_PROP_FOURCC)
print ('cv2.CAP_PROP_FRAME_COUNT    : ', cv2.CAP_PROP_FRAME_COUNT)
print ('cv2.CAP_PROP_FORMAT         : ', cv2.CAP_PROP_FORMAT)
print ('cv2.CAP_PROP_MODE           : ', cv2.CAP_PROP_MODE)
print ('cv2.CAP_PROP_BRIGHTNESS     : ', cv2.CAP_PROP_BRIGHTNESS)
print ('cv2.CAP_PROP_CONTRAST       : ', cv2.CAP_PROP_CONTRAST)
print ('cv2.CAP_PROP_SATURATION     : ', cv2.CAP_PROP_SATURATION)
print ('cv2.CAP_PROP_HUE            : ', cv2.CAP_PROP_HUE)
print ('cv2.CAP_PROP_GAIN           : ', cv2.CAP_PROP_GAIN)
print ('cv2.CAP_PROP_EXPOSURE       : ', cv2.CAP_PROP_EXPOSURE)
print ('cv2.CAP_PROP_CONVERT_RGB    : ', cv2.CAP_PROP_CONVERT_RGB)
#print ('cv2.CAP_PROP_WHITE_BALANCE : ', cv2.CAP_PROP_WHITE_BALANCE) unsupported
print ('cv2.CAP_PROP_RECTIFICATION  : ', cv2.CAP_PROP_RECTIFICATION)

print ('capture.get(<prop_id>)')

print ('capture.get(cv2.CAP_PROP_POS_MSEC)       : ', capture.get(cv2.CAP_PROP_POS_MSEC))
print ('capture.get(cv2.CAP_PROP_POS_FRAMES)     : ', capture.get(cv2.CAP_PROP_POS_FRAMES))
print ('capture.get(cv2.CAP_PROP_POS_AVI_RATIO)  : ', capture.get(cv2.CAP_PROP_POS_AVI_RATIO))
print ('capture.get(cv2.CAP_PROP_FRAME_WIDTH)    : ', capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print ('capture.get(cv2.CAP_PROP_FRAME_HEIGHT)   : ', capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print ('capture.get(cv2.CAP_PROP_FPS)            : ', capture.get(cv2.CAP_PROP_FPS))
print ('capture.get(cv2.CAP_PROP_FOURCC)         : ', capture.get(cv2.CAP_PROP_FOURCC))
print ('capture.get(cv2.CAP_PROP_FRAME_COUNT)    : ', capture.get(cv2.CAP_PROP_FRAME_COUNT))
print ('capture.get(cv2.CAP_PROP_FORMAT)         : ', capture.get(cv2.CAP_PROP_FORMAT))
print ('capture.get(cv2.CAP_PROP_MODE)           : ', capture.get(cv2.CAP_PROP_MODE))
print ('capture.get(cv2.CAP_PROP_BRIGHTNESS)     : ', capture.get(cv2.CAP_PROP_BRIGHTNESS))
print ('capture.get(cv2.CAP_PROP_CONTRAST)       : ', capture.get(cv2.CAP_PROP_CONTRAST))
print ('capture.get(cv2.CAP_PROP_SATURATION)     : ', capture.get(cv2.CAP_PROP_SATURATION))
print ('capture.get(cv2.CAP_PROP_HUE)            : ', capture.get(cv2.CAP_PROP_HUE))
print ('capture.get(cv2.CAP_PROP_GAIN)           : ', capture.get(cv2.CAP_PROP_GAIN))
print ('capture.get(cv2.CAP_PROP_EXPOSURE)       : ', capture.get(cv2.CAP_PROP_EXPOSURE))
print ('capture.get(cv2.CAP_PROP_CONVERT_RGB)    : ', capture.get(cv2.CAP_PROP_CONVERT_RGB))
#print ('capture.get(cv2.CAP_PROP_WHITE_BALANCE) : ', capture.get(cv2.CAP_PROP_WHITE_BALANCE)) unsupported
print ('capture.get(cv2.CAP_PROP_RECTIFICATION)  : ', capture.get(cv2.CAP_PROP_RECTIFICATION))

#print ('Set FPS to 100')
#capture.set(cv2.CAP_PROP_FPS, 100)
#time.sleep(1)
#print ('capture.get(cv2.CAP_PROP_FPS)            : ', capture.get(cv2.CAP_PROP_FPS))

print ('set exposure to -5')
capture.set(cv2.CAP_PROP_EXPOSURE, -5.0)
time.sleep(2)
print ('capture.get(cv2.CAP_PROP_EXPOSURE)       : ', capture.get(cv2.CAP_PROP_EXPOSURE))

print ('set exposure to 5')
capture.set(cv2.CAP_PROP_EXPOSURE, 5.0)
time.sleep(2)
print ('capture.get(cv2.CAP_PROP_EXPOSURE)       : ', capture.get(cv2.CAP_PROP_EXPOSURE))

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
