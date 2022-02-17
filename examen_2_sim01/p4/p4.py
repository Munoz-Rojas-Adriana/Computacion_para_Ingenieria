# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:19:10 2022

@author: ACER
"""

 dirección de la clase :
    def  __init__ ( self , Calle , Ciudad , Estado , Código Postal , País ):
        uno mismo calle = calle
        uno mismo Ciudad = Ciudad
        uno mismo Código Postal = Código Postal
        uno mismo País = País
    def  Validar ():
        imprimir ( "Validar" )
    def  OutputAsLabel ( auto ):
        print ( f"la dirección es { self . Street } " )

 Persona de clase :
    def  __init__ ( self , nombre , número de teléfono , dirección de correo electrónico , dirección ):
        uno mismo Nombre = Nombre
        uno mismo número de teléfono = número de teléfono
        uno mismo dirección de correo electrónico = dirección de correo electrónico
        uno mismo Dirección = Dirección
    def  PasePaqueteCompra ():
        imprimir ( "compra!!!" )
        

 Estudiante de clase ( Persona ):
    def  __init__ ( self , Name , PhoneNumber , EmailAddress , Adress , studentNumber , AvgMark ):
        # llama al metodo constructor de la clase padre
        súper (). __init__ ( Nombre , Número de teléfono , Dirección de correo electrónico , Dirección )
        uno mismo NúmeroEstudiante = NúmeroEstudiante
        uno mismo Marca Promedio = Marca Promedio
    def  es elegible para inscribirse ():
        print ( "es ilegible para inscribirse" )
    def  getSeminarsTOken ():
        imprimir ( "ficha" )
        
clase  Profesor ( Persona ):
    def  __init__ ( self , nombre , número de teléfono , dirección de correo electrónico , salario ):
        súper (). __init__ ( Nombre , Número de teléfono , Dirección de correo electrónico )
        uno mismo Salario = Salario
# usar las clases
adress_heroinas  =  Dirección ( "calle 10 de junio" , "Cochabamba" , "Texas" , 0000 , "Bolivia" )

estudiante_jhonny  =  Estudiante ( "jhonn" , 7777 , "jvm.corp@gmmgm.com" , dirección_heroinas , 1232 , 50 )

estudiante_jose  =  Student ( "Jose" , 7777 , "jvm.corp@gmmgm.com" , adress_heroinas , 1232 , 50 )