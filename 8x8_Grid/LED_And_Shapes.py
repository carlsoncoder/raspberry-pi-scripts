#!/usr/bin/python

import time
import datetime
import RPi.GPIO as GPIO
from Adafruit_8x8 import EightByEight

GPIO.setwarnings(False)

# variables
firstLED = 11
secondLED = 7
thirdLED = 22
slightDelay = 0.1

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid = EightByEight(address=0x70)
GPIO.setmode(GPIO.BOARD)

# setup all GPIO output channels for LEDs
GPIO.setup(firstLED, GPIO.OUT)
GPIO.setup(secondLED, GPIO.OUT)
GPIO.setup(thirdLED, GPIO.OUT)


def manipulateLED(pin, turnOn):
    if turnOn:
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)


def makeSmiley():
    grid.setPixel(1, 1)
    grid.setPixel(1, 2)
    grid.setPixel(1, 5)
    grid.setPixel(1, 6)
    grid.setPixel(2, 1)
    grid.setPixel(2, 2)
    grid.setPixel(2, 6)
    grid.setPixel(3, 3)
    grid.setPixel(3, 6)
    grid.setPixel(4, 3)
    grid.setPixel(4, 6)
    grid.setPixel(5, 1)
    grid.setPixel(5, 2)
    grid.setPixel(5, 6)
    grid.setPixel(6, 1)
    grid.setPixel(6, 2)
    grid.setPixel(6, 5)
    grid.setPixel(6, 6)


def makeHeart():
    grid.setPixel(0, 1)
    grid.setPixel(0, 2)
    grid.setPixel(0, 3)
    grid.setPixel(1, 0)
    grid.setPixel(1, 4)
    grid.setPixel(2, 1)
    grid.setPixel(2, 5)
    grid.setPixel(3, 2)
    grid.setPixel(3, 6)
    grid.setPixel(4, 2)
    grid.setPixel(4, 6)
    grid.setPixel(5, 1)
    grid.setPixel(5, 5)
    grid.setPixel(6, 0)
    grid.setPixel(6, 4)
    grid.setPixel(7, 1)
    grid.setPixel(7, 2)
    grid.setPixel(7, 3)


def makeLetterJ():
    grid.setPixel(0, 0)
    grid.setPixel(0, 1)
    grid.setPixel(0, 6)
    grid.setPixel(0, 7)
    grid.setPixel(1, 0)
    grid.setPixel(1, 1)
    grid.setPixel(1, 6)
    grid.setPixel(1, 7)
    grid.setPixel(2, 0)
    grid.setPixel(2, 1)
    grid.setPixel(2, 6)
    grid.setPixel(2, 7)

    grid.setPixel(3, 0)
    grid.setPixel(3, 1)
    grid.setPixel(3, 2)
    grid.setPixel(3, 3)
    grid.setPixel(3, 4)
    grid.setPixel(3, 5)
    grid.setPixel(3, 6)
    grid.setPixel(3, 7)

    grid.setPixel(4, 0)
    grid.setPixel(4, 1)
    grid.setPixel(4, 2)
    grid.setPixel(4, 3)
    grid.setPixel(4, 4)
    grid.setPixel(4, 5)
    grid.setPixel(4, 6)
    grid.setPixel(4, 7)

    grid.setPixel(5, 0)
    grid.setPixel(5, 1)
    grid.setPixel(6, 0)
    grid.setPixel(6, 1)
    grid.setPixel(7, 0)
    grid.setPixel(7, 1)


def makeMovingX():
    grid.setPixel(0, 0)
    time.sleep(slightDelay)
    grid.setPixel(1, 1)
    time.sleep(slightDelay)
    grid.setPixel(2, 2)
    time.sleep(slightDelay)
    grid.setPixel(3, 3)
    grid.setPixel(4, 3)
    time.sleep(slightDelay)
    grid.setPixel(5, 2)
    time.sleep(slightDelay)
    grid.setPixel(6, 1)
    time.sleep(slightDelay)
    grid.setPixel(7, 0)
    time.sleep(slightDelay)
    grid.setPixel(0, 7)
    time.sleep(slightDelay)
    grid.setPixel(1, 6)
    time.sleep(slightDelay)
    grid.setPixel(2, 5)
    time.sleep(slightDelay)
    grid.setPixel(3, 4)
    time.sleep(slightDelay)
    grid.setPixel(4, 4)
    time.sleep(slightDelay)
    grid.setPixel(5, 5)
    time.sleep(slightDelay)
    grid.setPixel(6, 6)
    time.sleep(slightDelay)
    grid.setPixel(7, 7)


while True:
    grid.clear()
    time.sleep(1.25)
    makeMovingX()
    time.sleep(1.25)
    grid.clear()

    manipulateLED(firstLED, True)
    makeLetterJ()
    time.sleep(1.25)
    grid.clear()
    manipulateLED(firstLED, False)

    manipulateLED(secondLED, True)
    makeHeart()
    time.sleep(1.25)
    grid.clear()
    manipulateLED(secondLED, False)

    manipulateLED(thirdLED, True)
    makeLetterJ()
    time.sleep(1.25)
    grid.clear()
    manipulateLED(thirdLED, False)

    makeSmiley()
    time.sleep(1.25)
    grid.clear()
