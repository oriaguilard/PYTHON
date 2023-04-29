"""imprimir los nombres que tienen una longitud mayor que 5 caracteres"""

nombre = ["Juan", "María", "Pedro", "Ana", "Roberto", "Lucía", "Luisa"]

for lista in nombre:
    if len(lista) >= 5:
        print(lista)
        
"""crear una lista de numeros donde cada numero es la longitud de una palabra"""        

animal = ["gato", "perro", "elefante", "jirafa", "tigre"]

longuitudes = []
#opcion 1s
for temp in range(len(animal)): #recorremos hasta un rango necesario de la lista animal
    longuitudes.append(len(animal[temp]))
print(animal)
print(longuitudes)

#opcion 2
for temp in animal: #recorremos hasta un rango necesario de la lista animal
    longuitudes.append(len(temp))
    break
print(animal)
print(longuitudes)


"""una clave ingresada, coincida con una lista de passwords predefinida"""
password = "password"

#opcion 1
while True:
    clave = input("ingrese la clave: ")
    if clave == password:
        print("clave correcta")
        break #agregar el break para romper el ciclo porque es un True
    else:
        print("Clave no corresponde. Ingrese nuevamente: ")

#opcion 2
print("solo tiene 3 intentos")
intentos = 1
while intentos <=3:
    clave = input("ingrese la clave: ")
    
    if clave == password:
        print("clave correcta")
        intentos = 4
    elif intentos == 3:
        print("Cantidad intentos superados")
        intentos = 4
    else:
        print(f" Intento {intentos} Clave no corresponde")
        intentos += 1