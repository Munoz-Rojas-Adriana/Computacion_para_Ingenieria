# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:37:28 2022

@author: ACER
"""

def  tkinter  importar  *
def tkinter  importar  ttk
def  seleccionarIdioma ( evento ):
    imprimir ( "seleccionado!!!" )
    seleccionado  =  comboBox_languages . obtener ()
    imprimir ( "el seleccionado" , seleccionado )
    etiqueta_resultado . config ( texto = f"idioma: { seleccionado } " )
    
# crear una ventana
ventana = Tk ()
ventana _ geometría ( '400x400' )
# Crear los componentes
label_result  =  Etiqueta ( ventana , texto = "<<resultado>>" )
comboBox_languages =  ttk . Combobox ( ventana , valores = [ 'java' , 'python' , 'C#' ])

# coordenadas
comboBox_idiomas . lugar ( x = 20 , y = 20 )
etiqueta_resultado . lugar ( y = 200 , x = 20 )
# enlazar eventos
comboBox_idiomas . enlazar ( "<<ComboboxSelected>>" , seleccionarIdioma )
ventana _ bucle principal ()