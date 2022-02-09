# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 07:22:32 2022

@author: ACER
"""

def  invertirCadena ( palabra ):
    
    resolución = ''
    índice  =  len ( palabra )
    
     mientras que  el índice  >  0 :
        ultimo_caracter  =  palabra [ index - 1 ]
        res  =  res  +  ultimo_caracter  # concatenar
        índice =  índice  -  1
    volver  res

entrada =  input ( "ingrese una palabra:" )
palabraInvertida  =  invertirCadena ( entrada )
imprimir ( palabra Invertida )

cadena1 = "hola"
cadena2 = "mundo"
caracter_espacio =  " "
mensaje  =  cadena1  +   caracter_espacion  +  cadena2
# hola mundo
imprimir ( mensaje )
