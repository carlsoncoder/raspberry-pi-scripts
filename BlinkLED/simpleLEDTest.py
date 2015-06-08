#!/usr/bin/python

import RPi.GPIO as GPIO  # Import the GPIO library as GPIO
import time

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Set the numbers to Broadcom Mode
GPIO.setwarnings(False)  # Ignore any errors

# Assign variables to pins
print 'using blueLED with BCM pin 37'
blueLED = 37  # greenwire
GPIO.setup(blueLED, GPIO.OUT)  # Set Blue LED as output

print 'off'
GPIO.output(blueLED, GPIO.LOW)
time.sleep(2)
print 'on'
GPIO.output(blueLED, GPIO.HIGH)
time.sleep(2)
print 'off'
GPIO.output(blueLED, GPIO.LOW)
