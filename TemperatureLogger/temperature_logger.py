#!/usr/bin/python

import smbus
import time
import datetime
import RPi.GPIO as GPIO

bus = smbus.SMBus(1)
led = 17

address = 0x48

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, True)


def getTemperature():
    rvalue0 = bus.read_word_data(address, 0)
    rvalue1 = (rvalue0 & 0xff00) >> 8
    rvalue2 = rvalue0 & 0x00ff
    rvalue = (((rvalue2 * 256) + rvalue1) >> 4) * 0.0625
    return rvalue


while True:
    GPIO.output(led, True)
    now = datetime.datetime.now() - datetime.timedelta(minutes=360)
    timestamp = now.strftime("%Y/%m/%d %H:%M")
    temp = getTemperature()
    message = str(timestamp) + " -  " + str(temp * 1.8 + 32) + " F" + "\n"
    print message
    temperatureFile = open('tempLoggerStats.txt', 'a')
    temperatureFile.write("%s" % message)
    temperatureFile.close()

    time.sleep(1)
    GPIO.output(led, False)
    time.sleep(900)
