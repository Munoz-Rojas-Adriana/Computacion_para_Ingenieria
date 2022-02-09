# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 07:22:08 2022

@author: ACER
"""

def cuentaPalabras(texto):
    palabras = texto.split(" ")
    palabrasContadas ={}
    contador  = 0
    longitud = len(palabras)
    for i in range(0, longitud):
        primera = palabra[i]
        print(primera)
        for j in range(0, longitud):
            segunda = palabra [j]
            if primera == segunda:
                contador += 1 #contador= contador +1
        palabrasContadas[primera] = contador
        contador  = 0
    return palabrasContadas
 
 texto = ("hola mundo como esta")        
 cuentaPalabras = cuentaaPalabras(texto)
 
                                        