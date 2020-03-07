# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:32:24 2020

@author: CEC
"""

def readint(prompt, min, max):
    while True:   
        try:
            x=int(input(prompt))
            print("The number is:", x)
            if x>max or x<min:
                print('Value should be between the range. The value of x was: '.format(x))
                continue
        except ValueError:
            print("Enter an integer ")
            continue
        break
v = readint("Enter a number from -10 to 10: ", -10, 10)


