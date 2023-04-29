"""1 [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Si el primer número de la sublista es cero, omitir la impresión de toda la sublista.
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero."""

lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

#primera forma
for a , b, c in lista:
    if a ==0:
        continue
    elif b ==0:
        print(a,c)
    elif c == 0:
        print(a,b)
    else:
        print(a,b,c)
        
