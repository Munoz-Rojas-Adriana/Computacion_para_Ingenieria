# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:49:21 2022

@author: ACER
"""

# importar 
from tkinter import *

contador = 0

def incrementar():
   
    cont = int(input_text_contador.get())
    cont+=1
    input_text_contador.delete(0, end)
    input_text_contador.insert(0,str(cont))
def decrementar():
    
    cont = int(input_text_contador.get())
    cont-=1
    input_text_contador.delete(0, end)
    input_text_contador.insert(0,str(cont))
def reset():
    t
    cont = int(input_text_contador.get())
    cont=0
    input_text_contador.delete(0, end)
    input_text_contador.insert(0,str(cont))
    
# ventana

window = Tk()
window.geometry("500x300")
window.title("p1")

# crear Label

label_contador = Label(window, text="Contador:")

# crear text

input_text_contador = Entry(window)

# insert 

input_text_contador.insert(0,str(contador))
button_contar = Button(window, text="cont up", command=lambda: incrementar())
button_contar2 = Button(window, text="cont down", command=lambda: decrementar())
button_contar3 = Button(window, text="reset", command=lambda: reset())

# coordenadas
label_contador.place(x=10, y=10)
input_text_contador.place(x=80, y=10)
button_contar.place(x=220, y=10)
button_contar2.place(x=300, y=10)
button_contar3.place(x=400, y=10)


# no cerrar VENTANA

window.mainloop()
