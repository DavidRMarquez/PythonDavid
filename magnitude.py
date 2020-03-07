# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:13:17 2020

@author: CEC
"""

class Magnitud:
    def __init__(self,valor):
        self.valor=valor
        
class Temperatura(Magnitud):
    def kelvinCelsius(self):
        self.valor=self.valor-273.1
        return self.valor
    
    def FaremgeiCelsius(self):
        self.valor=self.valor-32*5/9
        return self.valor
    def kelvinFarengei(self):
        self.valor=self.valor-273*1.8+32
        return self.valor

class Longitud(Magnitud):
    def centimetrosPulgada(self):
        self.valor=self.valor/2.54
        
class Masa(Magnitud):
    def libraTonelada(self):
        self.valor=self.valor/2205
        return self.valor