"""Realizar la ejecución de un menú utilizando el lenguaje Python, 
donde se le indiquen varias opciones a seleccionar por el usuario y 
una opción para salir del menú.
Utilizar ciclos y estructuras condicionales."""
import re #importar patrones

opcion = ""
patron = re.compile("(?<!\\S)\\d(?!\\S)") #patron declarado como string

while opcion !="5": #si es diferente de 5, termina el ciclo
    
    #opciones
    print("Bienvenido, menú:")
    print("1- opcion 1")
    print("2- opcion 2")
    print("3- opcion 3")
    print("4- opcion 4")
    print("5- Salir")
    print("ingrese una opcion")
    
    opcion = input() #leyendo la opcion ingresada
    if re.match(patron, opcion):
        
        if opcion == "1":
            print("realizando la opcion 1")
        elif opcion == "2":
            print("realizando la opcion 2")
        elif opcion == "3":
            print("realizando la opcion 3")
        elif opcion == "4":
            print("realizando la opcion 4")
        elif opcion == "5":
            print("Hasta luego")
            #break
        else:
            print("opcion invalida") #si no selecciona una opcion valida
    else:
        print("opcion invalida, valide el ingreso") #si no se cumple el patron
        
        
"""

while True: opcion = int(input("Hola, bienvenido\n " "1.- Saludar\n " "2.- preguntar que hay en la tele\n " "3.- que opinas de la música que escucho?\n" "4.- que estás sintiendo ahora?\n" "5.- Salir\n\n" "Ingresa una opción => ")) match opcion: case 1: print("Hola, que tal?") case 2: print("No hay nada bueno") case 3: print("Es buena música") case 4: print("Tengo hambre!") case 5: print("Nos vemos!") break case _: print("Esa opcion no es válida!")

"""