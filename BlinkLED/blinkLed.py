#!/usr/bin/python

import RPi.GPIO as GPIO
import time

ledPin = 7  # GPIO4


def blinkLed(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return

# use RPi board numbers
GPIO.setmode(GPIO.BOARD)

# setup GPIO Output channel
GPIO.setup(ledPin, GPIO.OUT)

# blink it 50 times
for i in range(0, 50):
    blinkLed(ledPin)

GPIO.cleanup()
