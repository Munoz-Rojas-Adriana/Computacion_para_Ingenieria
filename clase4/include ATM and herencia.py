# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 21:35:06 2022

@author: ACER
"""

class TarjetaDeCridito:

    def __init__(self, banco, codigo, propietario, fechVenc):
        self.banco=banco
        self.codigo=codigo
        self.propietario=propietario
        self.fechVenc=fechVenc
    # metodos de la clase

    def activar(self):
        print(f"Tarjeta con codigo {self.codigo} activada!")
    def bloquear(self):
        print(f"tajeta con codigo {self.codig} Bloqueda")
    def pagar(self):
        password = input("Enter your pin code:")
        print(f"el passwor es!! {password} Producto Pagado")

# Crear 3 objetso para los bancos BNB, SOL y BCP

tarjBnb = TarjetaDeCridito('BNB', 1234, 'jhonny V', '12/12/24')
tarjSol = TarjetaDeCridito('Banco Sol', 1234, 'jhonny V', '12/12/24')
tarjSol = TarjetaDeCridito('Banco BCP', 1234, 'jhonny V', '12/12/24')
# pagar con la tarjet del bnb
tarjBnb.activar()
tarjBnb.pagar()


# implementacion clase Padre

class Animal:
    # Metodo Constructor
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Metodos
    def hablar(self):
        pass # palabra reservada que no hace nada
    def moverse(self):
        pass 
    def describeme(self):
        print(f"Soy animal de tipo {self.especie} edad {self.edad}")


# clase que heredan de la clase animal

class Perro(Animal):
    # sobre escritura de metodos
    def hablar(self):
        print("GUAUUU GUAUU")
    def moverse(self):
        print("Caminar en 4 patas")

class Vaca(Animal):
    def habla(self):
        print("muuu")
    def moverse(self):
        print ("vaca camina en 4 patas")


## instancias de objetos

roky= Perro("perro", 2)
roky.describeme()

doky= Perro("perro Pastor ALeman", 10)