# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:58:40 2022

@author: ACER
"""

#importamos la libreria

def tkinter  importar  *

contador  =  0
def  aumentar ():
    # problema
     contador global
    contador = contador  + 1
    input_text_contador . eliminar ( 0 , FIN )
    input_text_contador . insertar ( 0 , cadena ( contador ))

def  incrementar_2 ():
    # obtener texto del texto de entrada
    cont  =  int ( input_text_contador . get ())
    continuo += 1
    input_text_contador . eliminar ( 0 , FIN )
    input_text_contador . insertar ( 0 , str ( continuación ))
# ventana

ventana  =  Tk ()
ventana _ geometría ( "300x300" )
ventana _ título ( "p1" )

# crear etiqueta
label_contador  =  Etiqueta ( ventana , texto = "Contador:" )
# crear campo de texto
input_text_contador  =  Entrada ( ventana )
# insertar valor inicial
input_text_contador . insertar ( 0 , cadena ( contador ))
button_contar  =  Botón ( ventana , texto = "+" , comando = lambda : incrementar_2 ())

# coordenadas
etiqueta_contador . lugar ( x = 10 , y = 10 )
input_text_contador . lugar ( x = 80 , y = 10 )
button_contar . lugar ( x = 220 , y = 10 )


# EVITAR CERRAR LA VENTANA
ventana _ bucle principal ()
