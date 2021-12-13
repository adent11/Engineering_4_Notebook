import picamera
import RPi.GPIO as GPIO #Python Package Reference: https://pypi.org/project/RPi.GPIO/
import os
import time

# Pin definition
cameraPin = 21

# Suppress warnings
GPIO.setwarnings(False)

# Use "BCM" pin numbering
GPIO.setmode(GPIO.BCM)

# Use built-in internal pullup resistor so the pin is not floating
# if using a momentary push button without a resistor.
GPIO.setup(cameraPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
name = input("Enter project name")
os.mkdir(f"../Media/{name}")
counter = 0
with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	time.sleep(2)
	while True:
		if not GPIO.input(cameraPin):
			counter = counter + 1
			camera.capture(f"../Media/{name}/image{counter}.jpg")
			print(f"Picture {counter} taken")
