from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

pir = MotionSensor(23)
camera = PiCamera()

now = datetime.now()
print(now)

while True:
	#print(pir.motion_detected)
	filename = "helpme.h264"
	pir.wait_for_motion()
	camera.start_recording(filename)
	print("Recording Started")
	pir.wait_for_no_motion()
	camera.stop_recording()
	print("Recording Stopped")

