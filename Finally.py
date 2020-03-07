# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:27:56 2020

@author: CEC
"""

def reciproco(n):
    try:
        n=1/n
    except ZeroDivisionError:
        print("División Fallida")
        n=None
    else:
        print("Todo salió bien")
    finally:
        print("Es el momento de decir adiós")
        return n
print(reciproco(2))
print(reciproco(-5))