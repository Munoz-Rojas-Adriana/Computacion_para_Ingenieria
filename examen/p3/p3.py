# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:19:17 2022

@author: ACER
"""
"""
archnotas = open('notas.txt', 'r')
archestudiantes = open('estudiantes.txt', 'r')

lista_notas = archnotas.readlines()
lista_estudiantes = archestudiantes.readlines()

for i in range(len(lista_estudiantes)):
    lista_notas[i] = lista_notas[i].strip()
    lista_estudiantes = lista_estudiantes[i].strip()
    
     
archPrimer_Parcial= open('Primer_Parcial.txt', 'wt')  

archPrimer_Parcial.write(lista_notas[0]+" "+lista_estudiantes[0])
archPrimer_Parcial.write(lista_estudiantes[2]+" "+lista_notas[2])

for i in range(len(lista_notas)):
    archPrimer_Parcial.write(lista_notas[i]+" "+lista_estudiantes+"\n")
    

    
archPrimer_Parcial.close()
archnotas.close()
archestudiantes.close()
"""
listaEstudiantes = open ('estudiantes.txt',' r')
notas = open('notas.txt, r')
primerParcial= open('primer_parcial.txt','wt')
lista=listaEstudiantes.readlines()
for linea in lista:
    nota =notas.readline()
    primerParcial.write(linea+' '+nota)
    
listaEstudiantes.close()
notas.close()
primerParcial.close()

    


    