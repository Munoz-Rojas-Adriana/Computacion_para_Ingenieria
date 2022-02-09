# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:18:06 2022

@author: ACER
"""

def deNumero_aListaInvertida(nombre):
    lista = []
    while nombre > 0:
        lista.append(int(nombre%10))
        nombre = int(nombre/10)
    return lista 

def invertir_lista (lista):
    nueva_lista = []
    tamaño_lista = len(lista)
    while tamaño_lista > 0:
        palabra-sacado = lista[tamaño_lista-1]
        nueva_lista.append(palabra-sacado)
        tamaño_lista =tamaño_lista-1
    return nueva_lista

def esPalindromo(palabra):
    lista = dePalabra_aListaInvertida(palabra)
    lista_invertida = invertir_lista(lista)
    if lista == lista_invertida:
        print("SI ES PALINDROMA")
    else:
        print("NO ES PALINDROMA")
        
        
        
        

    
    
    
        
    