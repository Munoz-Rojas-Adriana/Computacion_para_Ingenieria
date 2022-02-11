# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:15:16 2022

@author: ACER
"""

#imprtar modulo
import aritmetica
print(aritmetica.sumar(1,2))
print(aritmetica.div(1,1))
print(aritmetica.restar(1,1))

# otra manera de import solo funciones especificas

from aritmetica import sumar, div 

print(sumar(1,1))
print(div(1,1))

# importar todas las funciones de la libreria

from aritmetica import *
print(sumar(1,1))

