# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:23:02 2020

@author: CEC
"""

from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)