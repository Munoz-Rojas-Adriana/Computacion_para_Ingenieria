# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 21:19:10 2022

@author: ACER
"""

#comentarios en linea

"""
comentarios en linea
Linea 1
Linea 2
"""
#crear una constante
"""
NAME = 'Adriana'
FULL_NAME = 'adriana muñoz rojas'


print (NAME)
print (FULL_NAME)

# tipos de datos
entero = 90
print (f'el entero tiene valor de {entero}')
decimal = 6.14
print (f'el entero tiene valor de {decimal}')
caracter = 'J'
print (f'el entero tiene valor de {caracter}')
cadena = 'primera cadena'
print (f'el entero tiene valor de {cadena}')
cadena_2 = "segunda cadena"
print (f'el entero tiene valor de {cadena_2}')

booleano = False # valores True o False
print (f'el valor del decimal es {booleano}')
# lista
list=[1, 2, 3, 4]
print(f'el valor de La lista es : {list}')
# diccionario 
diccionario = {'nombre': 'adriana Muñoz Rojas' , "edad" : 20}
nombre = diccionario["nombre"]
edad = diccionario ["edad"]
print (f'el nombre es : {nombre} y du edad {edad}')

# entradas estandar

telefono = input("Ingrese el numero telefonico")
print (f'El ussuario ingreso ===>{telefono}')

# cast de tipos

a = int(input("Ingrease a :"))
b = int(input("Ingrease b :"))

print(f'resultado de sumar a + b = {a+b}')
"""
##IEstructuras de control
"""
anio = 2001
if anio <=2022:
    print("Anioes menor a 2022")
elif anio>= 1989:
    print ("anio es mayor na 1989")
else:
    print ("el anio no cumple con los rangos de 1989 o 2022")
   """ 
# estructura de control While

edad = 10
while edad <= 17:
    print(f'Menor de edad!!! {edad}')
    edad = edad + 1 # ---> edad += 1
    
    print(f'Mayor de edad {edad}')
    
    




