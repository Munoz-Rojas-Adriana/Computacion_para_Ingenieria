# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:44:21 2022

@author: ACER
"""

class Figura:
    
    def __init__(self, perimetro_, area_, color):
        
        self.perimetro = perimetro_
        self.area = area_
        
    @property
    def getPerimetro(self):
        return self.perimetro
    
    def getArea(self):
        return self.area
    
    def setPerimetro(self, nuevo_per):
        self.perimetro = nuevo_per
    
    def setArea(self, nueva_area):
        self.area = nueva_area
        
    def dibujar(self):
        pass
    
    def getColor(self):
        return self.color
    
    def setColor(self, nuevoColor):
        self.color = nuevoColor
    
    
    
class Circulo(Figura):
    
    
    def __init__(self, perimetro_, area_, radio, color):
        
        self.perimetro = perimetro_
        self.area = area_
        self.radio = radio
        self.color = color
        
    
    def getRadio(self):
        return self.radio
    
    def setRadio(self, nuevo_radio):
        self.radio = nuevo_radio
    


class Cuadrado(Figura):
    
    def __init__(self, perimetro_, area_, lado, color):
        
        self.perimetro = perimetro_
        self.area = area_
        self.lado = lado
        self.color = color
   
     
    def getLado(self):
        return self.lado
    
    def setLado(self, nuevo_lado):
        self.lado = nuevo_lado
        
  
    
  
class Rectangulo(Figura):
    
    def __init__(self, perimetro_, area_, base, altura, color):
        
        self.perimetro = perimetro_
        self.area = area_
        self.base = base
        self.altura = altura
        self.color = color
   
     
    def getBase(self):
        return self.base
    
    def setBase(self, nuevo_base):
        self.base = nuevo_base
        
    def getAltura(self):
        return self.altura
    
    def setAltura(self, nuevo_altura):
        self.altura = nuevo_altura