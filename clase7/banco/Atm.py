# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:58:18 2022

@author: ACER
"""

class Atm:
    
    def __init__ (self, ubicacion):
        self.ubicacion= ubicacion
        
    def showATM(self):
        print("cajero ubicado en ", self.ubicacion)
        