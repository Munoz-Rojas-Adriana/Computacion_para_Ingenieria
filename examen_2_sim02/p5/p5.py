# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:39:13 2022

@author: ACER
"""

Clase  Vehiculo :
    
    def  __init__ ( self , color , marca ):
        uno mismo color  =  color
        uno mismo marca = marca
    def  mostrarse ( self ):
        print ( f"la marca { self . marca } y color { self . color } " )

Clase  Auto ( Vehículo ):
    def  __init__ ( self , color , marca , maxVelocidad ):
        súper (). __init__ ( color , marca )
        uno mismo maxVelocidad  =  maxVelocidad

clase  Bicicleta ( Vehiculo ):
    
    def  __init__ ( self , color , marca , tipoFreno ):
        súper (). __init__ ( color , marca )
        uno mismo tipoFreno = tipoFreno

 Persona de clase :
    
    def  __init__ ( self , nombre , ci , vehiculo ):
        uno mismo nombre = nombre
        uno mismo ci = ci
        uno mismo vehículo = vehículo
    def  mostrarDatos ( auto ):
        print ( f"persona { self . nombre } tiene como vehiculo { self . vehiculo . mostrarse () } " )

# como se usa todas estas clases

vici_phoenix  =  Bicicleta ( "negro" , "Phoenix" , "Tacos" )
carlos  =  Persona ( "Carlos Villarroel" , 75757 , vici_phoenix )
carlos _ mostrarDatos ()