# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:35:22 2022

@author: ACER
"""

def  tkinter  importar  *
def  invertirTexto ():
    texto = cadena ( entrada_texto . obtener ())
    textInvertido =  texto [:: - 1 ] ## invertir texto
    imprimir ( textoInvertido )
    etiqueta_resultado . config ( texto = textoInvertido )
    
    
# crear la ventana
ventana  =  Tk ()
ventana _ geometría ( '400x400' )

label_text = Etiqueta ( ventana , texto = "Ingrese una palabra:" )
input_text = Entrada ( ventana )
label_result = Etiqueta ( ventana , texto = "<<resultado>>" )
button_res = Botón ( ventana , texto = "Validar" , comando = lambda : invertirTexto ())

# coordinada de los componentes

etiqueta_texto . lugar ( x = 10 , y = 10 )
entrada_texto . lugar ( x = 100 , y = 10 )
etiqueta_resultado . lugar ( x = 100 , y = 50 )
botón_res . lugar ( x = 100 , y = 70 )

ventana _ bucle principal ()