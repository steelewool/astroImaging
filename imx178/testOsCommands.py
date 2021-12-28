# Yanked the commands from the RMS_SetCameraParams.sh script and are now executing them inside of this program.

import os

os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl GetCameraParams")

#os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera GainParam Gain 60")

# Set the minimum exposure time to 1

#os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera ExposureTime 1")

# a few miscellaneous things - onscreen date/camera Id off, colour settings, autoreboot at 1500 every day
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetOSD off")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetColor 100,50,50,50,0,0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetAutoReboot Everyday,15")

# set the Video Encoder parameters

os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Encode Video Compression H.264")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Encode Video Resolution 720P")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Encode Video BitRateControl VBR")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Encode Video FPS 25")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Encode Video Quality 6")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Encode AudioEnable 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Encode VideoEnable 1")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Encode SecondStream 0")

# camera parameters

os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera Style type1")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera AeSensitivity 1")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera ApertureMode 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera BLCMode 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera DayNightColor 2")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera Day_nfLevel 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera DncThr 50")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera ElecLevel 100")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera EsShutter 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera ExposureParam LeastTime 40000")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera ExposureParam Level 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera ExposureParam MostTime 40000")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera GainParam AutoGain 1")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera GainParam Gain 60")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera IRCUTMode 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera IrcutSwap 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera Night_nfLevel 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera RejectFlicker 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera WhiteBalace 2")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera PictureFlip 0")
os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl SetParam Camera PictureMirror 0")

os.system("cd /home/pi/source/RMS; python -m Utils.CameraControl GetCameraParams")

