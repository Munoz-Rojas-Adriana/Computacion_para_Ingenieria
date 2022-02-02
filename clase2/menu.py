# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 23:35:58 2022

@author: ACER
"""
"""
crear un programa que registre nuevos alumno, liste los actuales alumno 
borre un alumno , el alumno tiene nombre y apellido
"""
# crear una list
list = []

salir = False

while salir !=True:
     print("----menu-----")
     print("1.- listar alumnos")
     print("2.- registrar alumno")
     print("3.- Quitar Alumno")
     print("4.-salir")
     print("------------")
     
     option = int(input("seleccione una option [1-2-3]"))
     
     
    #option 1 list de alumno
     if option == 1:
         print("la lista de alumnos es: ")
         for alumno in list:
             print(alumno)
             
       # option 2 agregar alumno
     elif option == 2:
         new_alumno = input("Ingrese el Nombre del Alumno:")
         
     elif option == 3:
         alum_quitar = input("Ingrese el nombre del Alumno a quitar:")
         list.remove(alum_quitar)
         print("se quitó de la lista", alum_quitar)
    
     elif option == 4:
         print("bye!!!")
         salir = True
         
     else:
         print("Porfavor digite una option corecta")
         
            
       



