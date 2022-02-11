# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:52:39 2022

@author: ACER
"""

#import 
import matematicas.aritmetica

print(matematicas.aritmetica.sumar(2,4))
#import
from matematicas import aritmetica
print(aritmetica.sumar(6,6))

from matematicas.aritmetica import sumar
print(sumar(2,3))

#?importamos geometria
from matematicas.geometria import calcularArea
print(calcularArea())
