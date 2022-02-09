# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:18:47 2022

@author: ACER
"""

#pregunta 2

lista = [ 10,20,30,10,5,1,3,5,4]

lista_pares= []
lista_impares=[]

for i in lista:
    if i%2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
        
print("Lista pares: ")
print(lista_pares)
print("Lista Impares")
print(lista_impares)

