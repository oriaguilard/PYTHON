#ciclo for
#se utiliza para recorrido de datos en listas, tuplas, diccionarios, set
#recorridos de texto string.
#se utiliza le metodo range() para obtener un rango
#len() para obtener el largo

#indice [0,1,2,3,4,5] desde 0 a n-1 siendo n la cantidad de elementos
lista = [1,2,3,4,5,6,1] #lista de 6 elementos

#recorriedo los elementos
for item in lista:
    print("1 recorriendo el elemento de la lista", item)
        
#recorriendo el indice
for item in range(len(lista)):
    print("2 recorriendo el indice de la lista", item)
        
for item in range(len(lista)):    
    print("ej1: recorriendo el elemento de la lista", lista[item])

#recorriendo el indice
for item in lista:
    print("eje2: recorriendo el indiceo de la lista", lista.index(item))
    
contador = 0
for item in lista:
    print("recorriendo el elemento de la lista", item)
    if item ==1:
        contador += 1
        print("existe el numero 1")
print(contador)
    
    
#diccionario
diccionario = {'a':1, 'b':2, 'c':3}

#obteniendo el valor de una key
for item in diccionario: 
    print("obteniento el valor de la clave", item) # a b c 
    
#obteniendo el value de una key
for item in diccionario: #obteniendo el valor de una key
    print("obteniento el valor de la clave", diccionario[item]) # 1 2 3
    
#obteniendo solo los valores
for item in diccionario.values(): #obteniendo el valor de una key
    print("obteniento el valor de la clave", item) # 1 2 3
    
#obteniendo solo los keys  o clave
for item in diccionario.items(): #obteniendo el valor de una key
    print("obteniento el elemento con clave:valor", item) # a b c