# Python Raspberry Pi LED Blinker
# Alden Dent
# 11/6/21

import RPi.GPIO as GPIO # Imports library for working with RPi GPIO pins
from time import sleep
GPIO.setwarnings(False) # Turns off annoying warnings

led1, led2, = 21, 26 # Pin each LED is connected to
led1Mode, led2Mode = 1, 0 # Starting state of each LED

GPIO.setmode(GPIO.BCM) # Switches to BCM pin numbering which is used by the T-Cobbler
GPIO.setup(led1, GPIO.OUT) # Sets pins to output
GPIO.setup(led2, GPIO.OUT)
GPIO.output(led1, False) # Starts pins as off
GPIO.output(led2, False)

sleepTime = float(input("Enter delay in seconds: ")) # Asks for the delay

while True:
    GPIO.output(led1, led1Mode) # Sets each led to the current mode
    GPIO.output(led2, led2Mode)
    led1Mode = not led1Mode # Switches both led modes (so one is on and the other is off)
    led2Mode = not led2Mode
    sleep(sleepTime) # Delays the desired amount of time
