#!/usr/bin/env python3

"""
    blink.py - Repeatedly blink lights over and over again
    Created: Sadip Giri (sdipgiri@bennington.edu)
    Date: 04/30/2018
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)

for i in range(0, 100):
    GPIO.output(20, 1)    # turn the lights on
    time.sleep(0.25)
    GPIO.output(20, 0)    # turn the lights off
    time.sleep(0.25)      # people need to notice it so!!
    print(i)

GPIO.cleanup() # cleanups all the pins of rasberry pi