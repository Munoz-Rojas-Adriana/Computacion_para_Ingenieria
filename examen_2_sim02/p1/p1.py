# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:19:11 2022

@author: ACER
"""
def tkinter  importar  *

def  sumar ():
    op1 = int ( entrada_op1 . obtener ())
    op2 = int ( entrada_op2 . obtener ())
    suma =  op1  +  op2
    print ( "la suma es" , suma )
    etiqueta_res . config ( texto = f"La suma es: { op1 } + { op2 } = { suma } " )
    
#crear una ventana
ventana  =  Tk ()
ventana _ geometría ( '400x400' )

# creamos los componentes
label_op1 =  Etiqueta ( ventana , texto = "Ingrese el valor de M:" )
label_op2 =  Etiqueta ( ventana , texto = "Ingrese el valor de N:" )
label_res = Etiqueta ( ventana , texto = "<<resultado>>" )
input_op1 =  Entrada ( ventana )
input_op2 =  Entrada ( ventana )
buton_res =  Botón ( ventana , texto = "Validar" , comando = lambda : sumar ())

#coordinaciones de los elementos
etiqueta_op1 . lugar ( x = 10 , y = 10 )
entrada_op1 . lugar ( x = 200 , y = 10 )

etiqueta_op2 . lugar ( x = 10 , y = 50 )
entrada_op2 . lugar ( x = 200 , y = 50 )

etiqueta_res . lugar ( x = 210 , y  =  90 )
buton_res . lugar ( x = 210 , y  =  110 )

ventana _ bucle principal ()
