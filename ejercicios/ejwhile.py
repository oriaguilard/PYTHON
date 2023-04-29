"""Tenemos una lista de números
[3, 5, 2, 8, 1, 10]
Se requiere encontrar el primer número par en la lista utilizando un bucle while."""

lista = [3, 5, 2, 8, 1, 10]

lista_pares=[]
i=0
while i < len(lista): #menor al largo de la lista
    if lista[i] %2 ==0: #si el valor de la lista divido entre 2 es igual a O
        print("el numero par es ", lista[i])
        print("el indice es ", [i])
        lista_pares.append(lista[i]) #muestra los numeros
        #break
    i = i+1  #si el contador se coloca en la linea 7, la linea 9 sería 1 en vez de 0

else:
    print("no se encontro numeros pares")
print(lista_pares)

"""Tenemos una lista de números
[3, 5, 2, 8, 1, 10]
calcular la suma de todos los numeros de la lista utilizando un bucle while."""


lista = [3, 5, 2, 8, 1, 10]
i=0
sum = 0 #cuando se sume o acumule se necesita una variable 

while i < len(lista):
    sum = sum + lista[i] 
    i = i+1
print(f"la suma es, {sum}")

"""Tienes la siguiente lista de números:
[45, 23, 67, 89, 12, 56, 78, 90]
Encontrar el número más grande en la lista utilizando un bucle for."""

lista = [45, 23, 67, 89, 12, 56, 78, 90]
num = lista[0]

for elemento in lista:
    if elemento > num: #i es el elemento 45/23/67/89/12/56/78/90
        num=elemento
print("el numero mayor es ", num)


lista = [45, 23, 12, 89, 12, 56, 78, 90]
mayor = lista[0]
menor = lista[0]
repetido = []

for elemento in lista:
    if elemento > mayor: #i es el elemento 45/23/67/89/12/56/78/90
        mayor =elemento
    if elemento < menor:
        menor = elemento
    if lista.count(elemento) > 1 and elemento not in repetido:
        repetido.append(elemento)
        print(lista.count(elemento))
    

print("mayor es ",num)
print ("menor es ", menor)
print ("la cantidad q se repite ", repetido)

lista = [25.50, 12.30, 36.40, 9.75, 15.20]
i = 0
suma =0

while i < len(lista):
    suma += lista[i]
    i+= 1
print(f"el valor total de la compra es {suma}")
print("con 10dcto quedaría en {:.2f}".format(suma * 0.9))



compradescuento = sum(lista)*.90
print (f"su compra es {sum(lista)}")
print (f"con descuento {compradescuento}")