"""Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar.
En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar
subcondiciones; en su lugar, usar condiciones anidadas."""

num = int(input("ingrese un numero: "))

if num > 0:
    if num % 2 ==0:
        print("el numero positivo es par")
    else:
        print("el numero positivo es impar")
elif num <0:
    if num % 2 ==0:
        print("el numero negativo es par")
    else:
        print("el numero negativo es impar")
else:
    print("el numero es 0")