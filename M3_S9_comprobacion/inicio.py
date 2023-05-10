"""Crear una función que acepte 3 números como parámetros, sume todos los valores, y
adicionalmente reste el segundo y tercer parámetro al primero.
Al invocar la función, debemos pasarle los parámetros en forma de lista. Esta devolverá ambos
resultados en una tupla. Los resultados se deben imprimir en pantalla."""

import math

def suma (n1,n2,n3): #funciona suma
    suma1 = n1+n2+n3 #suma de todos los valores
    sumafinal = (n1-(n2+n3)) #resta del segundo y tercero por el primero
    return (suma1, sumafinal)

def sumab(lista): #version2
    suma1 = lista[0] + lista [1] + lista [2]
    sumafinal= lista[0] - (lista [1] + lista [2])
    return ( suma1, sumafinal)

#ingresar parametros como lista
lista=[1,2,3]
resultado = suma (*lista) #(*) desempaca cada elemento de la lista


resultado = suma (1,2,3)

#ciclo for para mostrar valor
a = 0 
for n in resultado:
    a = a + 1
    print(f"valor {a} : {n} ")
    
#entregar lista
print("Tupla:", suma(*lista)) #también se puede llamar a "resultado"
print("tupla v2:", sumab(lista) )
