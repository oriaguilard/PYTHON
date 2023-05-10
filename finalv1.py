# Definir variables y listas

lista_pers = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking',

              'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

magos = [lista_pers[0], lista_pers[2], lista_pers[5]]

cientificos = [lista_pers[1], lista_pers[3], lista_pers[6]]

otros = [lista_pers[4], lista_pers[7], lista_pers[8]]




# Definir funcion grandes magos





def hacer_grandioso(mago):

    """ Función llamada hacer_grandioso(), que modifique la lista de magos

    añadiendo la frase ‘El gran‘ antes del nombre de cada mago """

    i = 0

    for mago in magos:

        mago = "El gran " + mago

        magos[i] = mago

        i += 1

    return magos




# Definir función que imprime nombres





def imprimir_nombres(lista):

    """ Crear una función llamada imprimir_nombres(), que imprime el nombre

    de cada persona de la lista. """

    for persona in lista:

        print(f"{persona}")





# Definir función que imprime lo solicitado

def imprimir_listas(lista1, lista2, lista3, lista4):

    # Imprimir en pantalla la lista completa de nombres antes de ser modificados

    print(f"\nLa lista dada es: {lista1}")

    # Imprimir los nombres de los magos grandiosos,los nombres de los científicos, y los restantes

    print("\n** LOS GRANDIOSOS MAGOS SON: **")

    imprimir_nombres(hacer_grandioso(lista2))

    print("\n** LOS CIENTÍFICOS SON: **")

    imprimir_nombres(lista3)

    print("\n** LAS OTRAS PERSONAS SON: **")

    imprimir_nombres(lista4)





imprimir_listas(lista_pers, magos, cientificos, otros)