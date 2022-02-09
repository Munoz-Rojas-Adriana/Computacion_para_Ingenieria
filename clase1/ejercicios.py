# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:12:55 2022

@author: ACER
"""
#problema 1
oracion = input("ingresa una oracion")
cont = 0
for char in oracion:
    if char ==" ":
        cont =cont + 1
        
#pregunta 2
def contarPalabras(parrafo):
    cant_espacios = 0
    for char in parrafo:
        if char ==" ":
            cant_espacios = cant_espacios + 1
    return cant_espacios + 1
salida = contarPalabras ("hola Mundo")
print(f'El numero de palabras es {salida}')

#pregunta 3
oracion = input("ingresa una oracion")
cont = 0
for char in oracion:
    if char ==" ":
        cont =cont + 1
cont = cont + 1

print (cont)     

#pregunta 4
def mostrarDigito_porDigito (num):
    while num > 0:
        print (num%10)
        num = int(num/10)
        
n = int(input)("ingrese un numero: ")
print (f'Los digitos son: {mostrar digito}')
        