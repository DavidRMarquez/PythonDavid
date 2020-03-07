# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:21:52 2020

@author: CEC
"""

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


while True:
    GPIO