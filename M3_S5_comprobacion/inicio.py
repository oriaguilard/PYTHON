"""Requerimos calcular el factorial de un número, asignarlo a una variable, y 
luego imprimirla. Sabiendo que el factorial es el resultado de la multiplicación 
de todos los enteros positivos que hay entre un número y uno. 
Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1."""

#variable qie acumule el valor ingresado
num = 0

#ciclo para pedir el ingreso del numero y que sea positivo
while True: 
    num = int (input ("ingrese un numero entero positivo: "))
    if num >0: #si el num es mayor a 0 se cumple
        break
    
"""el factorial es el resultado de la multiplicación
de todos los enteros positivos que hay entre un número y uno.  """

factorial = 1
i = 1
while True:
    factorial *= i #acumulando el factorial por cada valor del iterador
    i += 1 #cambia el valor del iterador
    if i > num:
        break
print(f"el factorial de {num} es: {factorial}")