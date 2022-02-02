# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 01:56:42 2022

@author: ACER
"""

# listar los numeros primos del 1 al 100
num = 1
while  num <= 100:
    num = num + 1
    cont = 1
    a = 0
    while cont <= num :
        if num % cont == 0:
            a = a+1
        cont = cont +1
        
if a==2:
   print(num)
             
   
   