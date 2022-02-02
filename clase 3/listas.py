# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 07:15:26 2022

@author: ACER
"""

# lista en blanco
lista = []

#lista con elementos
ñistElementos = [1,3,4,5]

#acceder a los elementos
listAlumnos = ["adri","rither","jose","juan"]
alumnoPos_1 =listAlumnos[len(listAlumnos)-1] #'juan'
#obtener el tamanio de la lista
tamanioListaAlumnos = len(listAlumnos)
print("el tamaño de la lista alumnos es :",tamanioListaAlumnos)
#insertar elementos a una Lista
lista.appens(1)
lista.appens(2)
lista.appens(5)
# lista [1,2,3]
#lista [1,2,3,5]
# insertar un elemento en un indice de la lista
#insert (indice(0,tamanio_1),elemento)
lista.insert(2,3)
print(lista)
# eliminar elementos de una lista
# lista [1,2,3,5]
lista.pop(0)
# lista [2,3]
print(lista)
listaDocentes = ['jhonny','caballero','haku']
listaDocentes.remove('caballero')
#['jhonny', 'haku']
print(listaDocentes)

# iterar listas

for Docente in listaDocentes:
    print(Docente)
   
tamanioListaDocentes = len(listaDocentes)
for i in range(0, tamanioListaDocentes):
    print(listaDocentes[i])
    
