"""Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos
números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos
números como parámetros y regrese el resultado en forma de tupla de su suma, resta,
multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta,
Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función
creada anteriormente"""

import math

def suma (n1,n2):
    return n1+n2

def resta (n1,n2):
    return n1-n2

def multiplicar (n1,n2):
    return n1*n2
    
def dividir (n1,n2):
    return n1//n2 # (//) resultado en entero

def tupla (n1,n2):
    return (suma(n1,n2), resta(n1,n2), multiplicar(n1,n2), dividir(n1,n2))

resultado = tupla(4,2) #lo acumulamos para llamarlo en el diccionario
print(resultado) 

diccionario = { #creando un diccionario
    'suma': resultado[0],
    'resta': resultado[1],
    'multiplicar': resultado[2],
    'dividir':resultado[3]
}
print(diccionario) #resultado del diccionario