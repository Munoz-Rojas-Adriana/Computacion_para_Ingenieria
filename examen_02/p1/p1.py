# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:47:27 2022

@author: ACER
"""


from tkinter import *

def InvertirTexto():
    text=str(inpt_tex.get())
    textInvertido = text[::-1]
    print(textInvertido)
    Label_result.confing(text=f"es palindromo: {textInvertido}")
    
    
window = Tk()
window.geometry('400x400')

Label_text=Label(window, text ="Entrar a WORLD:" )
input_text= Entry(window)
Label_result=Label(window, text="<<result>>")
button_res=Button(window, text="vaidate", command=lambda: InvertirTexto())

Label_text.place(x=10, y=10)
input_text.place(x=100, y=10)
Label_result.place(x=100, y=50) 
button_res.place(x=100, y =70)

window.mainloop   
