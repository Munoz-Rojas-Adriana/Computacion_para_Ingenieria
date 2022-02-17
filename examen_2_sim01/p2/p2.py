# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:07:14 2022

@author: ACER
"""
def tkinter  importar  *

def  añadirPeli ():
    # obtener el nombre de la peli de entrada del usuario
    nombre_peli  =  input_peli . obtener ()
    # agregar al cuadro de lista
    lista_pelis . insert ( 0 , peli_name )
    

# crear una ventana
ventana  =  Tk ()
ventana _ geometría ( '400x400' )
# crear elementos
# crear etiquetas
label_in_text  =  Label ( window , text = "Escriba el titulo de una pelicula" )
# cuadro de lista de etiquetas
label_list  =  Etiqueta ( ventana , texto = "Peliculas:" )
# texto de entrada
input_peli =  Entrada ( ventana )
# boton agregar peli
button_add_peli  =  Botón ( ventana , texto = "Agregar Peli" , comando = lambda : addPeli ())
# cuadro de lista
list_pelis  =  Cuadro de lista ( ventana )
# coordenadas
etiqueta_en_texto . lugar ( x = 10 , y = 10 )
lista_etiquetas . lugar ( x = 250 , y = 10 )

input_peli . lugar ( x = 10 , y =  50 )
button_add_peli . lugar ( x = 10 , y = 100 )

# cuadro de lista
lista_pelis . lugar ( x = 250 , y = 50 )




ventana _ bucle principal ()