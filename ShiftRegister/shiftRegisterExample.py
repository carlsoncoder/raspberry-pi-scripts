#!/usr/bin/python

# NOTE: In order for this to work, you must put this script in the directory that shiftpi creates after cloning
# https://github.com/mignev/shiftpi
# git clone https://github.com/mignev/shiftpi.git

from time import sleep
import shiftpi


def allOnorAllOff(turnOff, localDelayTime):
    if turnOff:
        shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)
        shiftpi.delay(localDelayTime)
    else:
        shiftpi.digitalWrite(shiftpi.ALL, shiftpi.HIGH)
        shiftpi.delay(localDelayTime)


def christmasKnightrider(localDelayTime):
    for index in range(8):
        if index > 0:
            # turn off previous LED
            shiftpi.digitalWrite(index - 1, shiftpi.LOW)

        # turn on the current LED
        shiftpi.digitalWrite(index, shiftpi.HIGH)
        shiftpi.delay(localDelayTime)

    for index in range(7, 0, -1):
        shiftpi.digitalWrite(index, shiftpi.LOW)
        shiftpi.digitalWrite(index - 1, shiftpi.HIGH)
        shiftpi.delay(localDelayTime)


def alternateBlinks():
    # turn all off
    allOnorAllOff(True, 10)

    # turn on and off evens
    shiftpi.digitalWrite(0, shiftpi.HIGH)
    shiftpi.digitalWrite(2, shiftpi.HIGH)
    shiftpi.digitalWrite(4, shiftpi.HIGH)
    shiftpi.digitalWrite(6, shiftpi.HIGH)
    shiftpi.delay(300)
    shiftpi.digitalWrite(0, shiftpi.LOW)
    shiftpi.digitalWrite(2, shiftpi.LOW)
    shiftpi.digitalWrite(4, shiftpi.LOW)
    shiftpi.digitalWrite(6, shiftpi.LOW)

    # turn on and off odds
    shiftpi.digitalWrite(1, shiftpi.HIGH)
    shiftpi.digitalWrite(3, shiftpi.HIGH)
    shiftpi.digitalWrite(5, shiftpi.HIGH)
    shiftpi.digitalWrite(7, shiftpi.HIGH)
    shiftpi.delay(300)
    shiftpi.digitalWrite(1, shiftpi.LOW)
    shiftpi.digitalWrite(3, shiftpi.LOW)
    shiftpi.digitalWrite(5, shiftpi.LOW)
    shiftpi.digitalWrite(7, shiftpi.LOW)


while True:
    for i in range(4):
        allOnorAllOff(True, 300)
        allOnorAllOff(False, 300)
        sleep(1)

    for i in range(8):
        christmasKnightrider(50)

    for i in range(8):
        alternateBlinks()
