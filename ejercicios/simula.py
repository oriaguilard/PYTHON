"""simula un programa que permite a los usuarios
adivinar una palabra secreta"""

import random
palabrassecretas = ["arroz", "pollo", "arepa", "queso"]
adivinar = random.choice(palabrassecretas) #palabra para adivinar
print(adivinar)
intentos = 5
turno = 0
ingreso = ""

while adivinar != ingreso and turno < intentos: 
    ingreso = input("ingrese una palabra") #declaracion
    turno += 1
    if ingreso == adivinar:
        print(f"Haz encontrado la palabra secreta en el intento {turno} ")
    elif turno == intentos:
        print(f"No te quedan intentos. La palabra era {adivinar}")
    else:
        print(f"intenta nuevamente. Vas en el turno {turno} ")
