#!/usr/bin/python

# NOTE:  Could not get this to work on Mac OSX - had to use linux
# Pre-requisites:
#   sudo apt-get update
#   sudo apt-get upgrade
#   sudo apt-get install tcpdump tcpreplay wireshark python-scapy

import datetime
import RPi.GPIO as GPIO
from scapy.all import *

relayPin = 22  # GPIO22

# set pin mode to BCM
GPIO.setmode(GPIO.BCM)

# setup GPIO Output channel
GPIO.setup(relayPin, GPIO.OUT)

# default to ON
GPIO.output(relayPin, GPIO.HIGH)

# has the user ever pressed a button?
everPressedButton = False

# state to use for toggling GPIO
currentState = True

# use to prevent multiple button presses in a row
lastPressed = datetime.datetime.now()


def arp_display(pkt):
    if pkt.haslayer(ARP):
        if pkt[ARP].op == 1:
            if pkt[ARP].psrc == '0.0.0.0':
                if pkt[ARP].hwsrc == '74:c2:46:c7:57:8e':
                    print "Pushed Bounty button"
                    handle_button_push()
                else:
                    print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

        
def handle_button_push():
    global currentState
    global lastPressed
    global everPressedButton

    shouldPerformAction = True
    if everPressedButton is True:
        now = datetime.datetime.now()
        secondsSinceLastPress = (now - lastPressed).total_seconds()
        if secondsSinceLastPress < 180:
            shouldPerformAction = False
            print "Ignoring action due to not enough time between button presses"
    else:
        everPressedButton = True

    lastPressed = datetime.datetime.now()

    if shouldPerformAction is True:
        if currentState is True:
            print "Turning relay OFF"
            currentState = False
            GPIO.output(relayPin, GPIO.LOW)
        else:
            print "Turning relay ON"
            currentState = True
            GPIO.output(relayPin, GPIO.HIGH)
    
    
print sniff(prn=arp_display, filter="arp", store=0, count=0)
