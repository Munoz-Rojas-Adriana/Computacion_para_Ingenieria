#PARES
def digitos_pares():
    pares = []
    
    for n in range(200, 501):
        cadena = str(n)
        
        if  int(cadena[1]) % 2 == 0 and int(cadena[2]) % 2 == 0:
            pares.append(cadena)
            
    return pares 
        
resultado = digitos_pares()
        
print(", ".join(resultado))


#IMPARES
def digitos_pares():
    pares = []
    
    for n in range(100, 401):
        cadena = str(n)
        
        if int(cadena[0]) % 2 != 0 and int(cadena[2]) % 2 == 0 and int(cadena[2]) % 1 == 0:
            pares.append(cadena)
            
            return pares 
        
resultado = digitos_pares()
        
print(", ".join(resultado))


    
     
     

        

        

        
        
        