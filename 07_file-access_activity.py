# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:57:13 2020

@author: CEC
"""

file=open("devices.txt","a")
while True:
    newItem=input("Enter a new device: ")
    file.write(newItem+ "\n")
    if newItem=="exit":
        print("All done!")
        break
    else:
        continue
    for item in file:
        print(item)
    
file.close()
