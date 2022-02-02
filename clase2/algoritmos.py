# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 01:32:24 2022

@author: ACER
"""

# contadores
cont = 0
cont +=1 #--> cont + 1

# contar numero del 1 al 10 y mostrar en la pantalla

while cont <= 10:
    cont = cont +1
    print (cont)
 
 # 2.- sumar los numeros del 1 al 10
  #list = ^[1, 2, 3,,,,10] 
  #range (1,n)---> [1, 2, 3, 4, 5,,,,(n-1)]
sum=0
for num in range(1,4): #[1,2,3]
  
  sum = sum + num

print(f'la suma total del 1 al 10 es {sum}')

# 3. multiplicar del 1 al 10
mult = 1
for num in range (1,11):
    mult = mult*num
    print("la multiplicacion total es ", mult)
    
 # 4.- mostrar los impares del 1 al 10
for num in range (1,11):
    if num % 2 == 0 :
        print ("numeros pares:", num)
        
    