"""Dada la siguiente lista de nombres:
• Harry Houdini
• Newton
• David Blaine
• Hawking
• Messi
• Teller
• Einstein
• Pele
• Juanes
Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y
Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y
escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
frase ‘El gran‘ antes del nombre de cada mago.
Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la
lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego
imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes"""

"""1- crear 3 listas vacias (magos, cientificos, otros)
2.- hacer un for que almacene segun corresponde
3.- hacer las funciones solicitadas"""


#(paso 3) escribir una función llamada hacer_grandioso(), que modifique la lista de magos 
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = 'el gran ' + magos[i]

#Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la lista.
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

#crear funcion para crear lista nueva
def crear_listas(magos, cientificos, otros, nombres):
#paso 2
    for nombre in nombres:
        if nombre in ['Harry Houdini','David Blaine','Teller']:
            magos.append(nombre)
        elif nombre in ['Newton', 'Hawking', 'Einstein' ]:
            cientificos.append(nombre)
        else:
            otros.append(nombre)

#defina la lista de nombres (paso 1)
nombres = ['Harry Houdini', 'Newton', 
        'David Blaine', 'Hawking','Messi',
        'Teller','Einstein','Pele','Juanes']
#creamos 3 grupos diferentes para cada nombre
magos = []
cientificos = []
otros = []

crear_listas(magos, cientificos, otros, nombres)

diccionario={'magos': magos,
            'cientificos':cientificos,
            'otros':otros,
            'nombres':nombres}

print('El diccionario sería: ')
print(diccionario)

#imprimir la lista completa de personajes
print('Lista completa: ')
imprimir_nombres(nombres)

#imprimir la lista de "el gran"+magos
print('Lista los grandes magos: ')
hacer_grandioso(magos)
imprimir_nombres(magos)

#imprimir laas otras listas
print('Lista de los cientificos: ')
imprimir_nombres(cientificos)
print('Lista de los otros: ')
imprimir_nombres(otros)