from picamera import PiCamera
from time import sleep

camera = PiCamera()

try :
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Pictures/image.jpg')
finally :
    camera.stop_preview()
