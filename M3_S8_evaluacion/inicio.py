"""Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
1 [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
• Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
• Finalmente, imprimiremos en pantalla el diccionario resultante.
Ejemplo de impresión en pantalla:
A:[1, 2, 3]"""

lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

diccionario = dict()
otro_diccionario = dict()
claves = ["a","b","c","d"]

contador = 0 #conocer posicion de la lista para las claves y agregar elementos al diccionario

for temp in lista: 
    #insentar nombre_dicionarrio[clave] = valor
    diccionario[claves[contador]] = temp #una forma diccionario[lista[indice]] = elemento que se recorre
    otro_diccionario[claves[lista.index(temp)]] = temp #segunda forma
    contador +=1
    if temp[0] == 0: 
        continue 
    for num in temp: 
        if num == 0: 
            continue 
        print(num)
print (diccionario)
print (otro_diccionario)