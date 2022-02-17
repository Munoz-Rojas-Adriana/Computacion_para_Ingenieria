# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:19:43 2022

@author: ACER
"""

#como abrir ventana

from tkinter import *
window = Tk()
window.title("1")

window.main.loop()

#como crear botones
from tkinter import *
#definimos funcion aejecutar al clic del botón
def hola():
    print("hola mundo!")
    
root = Tk()
#enlazamos la funcion a la accion del boton
Button(root, text="Clicame",comman=hola).pack()

roat.mainloop()


#como crear Label
from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Yo soy un Label")#creacion del Label
mi_Label.pack()
raiz.mainloop()


from tkinter import *
root = Tk()
Label =Label(root, text="gola mundo")
Label.pack()
root.mainloop()

   