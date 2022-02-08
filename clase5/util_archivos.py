# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 22:03:29 2022

@author: ACER
"""

# Manejar archivos
"""
listaNumeros.txt
1 
2
3<-
4
5
"""
# leer Linea por linea un archivo
numeros = open ('listaNumeros.txt', 'r')
print(numeros.readline()) # imprime 1 en la pantalla
numeros.readline()
print(numeros.readline())# imprime 3

# Leer lineas de un archivo  y da como resulta un array ['','']

res = numeros.readlines() # retorna un array con el contenido del archivo
print(res)

# anexa archivos

archivo = open ('listaProfes.txt', 'a')
archivo.write('nuevo DOcente') # agrea nuevas lineas a un archivo
archivo.close()

#pregunta 1

palabra=input("Ingrese una palabra:")
sum = 0
for char in palabra:
    sum=sum+1

print(f"el numero de caracteres de {palabra} es: {sum}")

#pregunta 2

lista = [10,20,30,10,5, 1, 3, 5, 4]
listPares=[]
listImpares=[]
for num in lista:
    if num % 2 == 0:
        # es par
        listPares.append(num)
    else:
        listImpares.append(num)

print(lista)
print(listPares)
print(listImpares)

#pregunta 3

def deNumero_aLista(num):
    lista = []
    while num > 0:
        lista.append(int(num%10))
    return lista
def invertir_lista(lista):
    new_lista =[]
    tam_lista = len(lista)
    while tam_lista > 0:
        new_lista.append(lista[tam_lista-1])
    return new_lista
def esPalindromo(num):
    lista= deNumero_aLista(num)
    lista_invertida= invertir_lista(lista)
    if lista ==lista_invertida:
        print("SI ES PALINDROMO")
    else:
        print("NO ES PALINDROMO")
        
esPalindromo(12321)
        
#INGENIERO PREGUNTA 3

# invertir números
def  invertirNumer ( numero ):
    numeroInvertido = 0
    mientras_numero >  0 :
        numeroInvertido =  10  *  numeroInvertido  +  numero  %  10
        número  //= 10
    volver  numeroInvertido

# llamada a la funcion
entrada  =  int ( entrada ( "ingrese un numero:" ))
numInv  =  invertirNumero ( entrada )
if  entrada  ==  numInv :
    print ( "el numero es palindromo" )
más :
    print ( "el numero no es palindromo" )
    
 #ingeniero pregunt 4
 
 
#Pedir una cadena al usuario y mostrar la cadena invertida (crear una funcion invertirPalabra)
# Hola
def  invertirCadena ( palabra ):
    
    resolución = ''
    índice  =  len ( palabra )
    
    mientras que  el índice  >  0 :
        ultimo_caracter  =  palabra [ index - 1 ]
        res  =  res  +  ultimo_caracter  # concatenar
        índice =  índice  -  1
    volver  res

entrada =  input ( "ingrese una palabra:" )
palabraInvertida  =  invertirCadena ( entrada )
imprimir ( palabra Invertida )

cadena1 = "hola"
cadena2 = "mundo"
caracter_espacio =  " "
mensaje  =  cadena1  +   caracter_espacion  +  cadena2
# hola mundo
imprimir ( mensaje )

 
 