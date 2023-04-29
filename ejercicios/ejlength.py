"""Pedir el ingreso de dos textos al usuario por consola y 
comparar si son iguales o del mismo tamaño"""


texto1 = input("Ingrese primer texto: ")
texto2 = input("Ingrese segundo texto: ")

if len(texto1) == len(texto2): #verifica la longitud
    if texto1 == texto2:
        print("textos iguales y mismo longuitud") #se cumple
    else:
        print("Textos diferentes y y misma longuitud")

else: #si no son iguales
    print("textos diferentes")
        
print("_________________________")    


texto1 = input("Ingrese primer texto: ")
texto2 = input("Ingrese segundo texto: ")

if len(texto1) == len(texto2): #verifica la longitud
    print("textos del mismo tamaño ") #se cumple
elif texto1 == texto2:
    print("Textos iguales")

else: #si no son iguales
    print("textos diferentes")