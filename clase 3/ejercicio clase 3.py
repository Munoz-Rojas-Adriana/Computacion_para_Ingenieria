lista = [1, 3 , 5 , 100]

# dado la lista "lista" encontrar el elemento mayor 

mayor = 0 
for i in range(len(lista)):
    if lista[i] > mayor:
        mayor=lista[i]
print(mayor)        

# dada la lista "lista" mostrar el promedio

prom = 0 
for i in range(len(lista)):
    prom = prom + lista[i]
prom = prom / (len(lista))
print(prom)

