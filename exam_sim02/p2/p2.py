# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 07:21:05 2022

@author: ACER
"""
# pregunta 

lista=[12,1,3,5,15,24]

lista_pares = []
lista_impares = []
for i in lista:
    if i %2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
        
print("lista pares")
print(lista_pares)
print("lista impares")
print(lista_impares)



        