# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:25:09 2020

@author: CEC
"""

def reciproco(n):
    try:
        n=1/n
    except ZeroDivisionError:
        print("Division Fallida")
        return None
    else:
        print("Todo salio bien")
        return n

print(reciproco(2))
print(reciproco(-5))