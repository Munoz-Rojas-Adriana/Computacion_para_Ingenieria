# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:23:22 2022

@author: ACER
"""
#p3

from tkinter import *

def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()
    
def resta():
    r.set(float(n1.get()) - float(n2.get()))
    borrarr()
    
def producto():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()
    
    
def borar():
    n1.set("")
    n2.set("")
    
 #configuracion de la raiz

root=Tk()
root.config(bd=15) 

n1 =StringVar()
n2 =StringVar() 
r= StringVar()

Label(root,text="Numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root,text="Numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack()    
    
Label(root,text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()

Label(root, text="").pack() #separador

Button(root, text="sumar", command=sumar).pack(side="left")
Button(root, text="resta", command=resta).pack(side="left")
Button(root, text="producto", command=producto).pack(side="left")
         
#finalmente buble de la aplicacion
root.mainloop()  
  

    

    