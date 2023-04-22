#estructuras condicionales. para evaluar condiciones

numero = int(input("ingreso un numero entero = ")) #se convierte a entero porque sino no lo lee. el input arroja un string
#if(condicion), evaluamos la condicion, donde siempre la condicion es TRue al menos que se cambie o modifique la operacion

if(numero >0):
    print(f"el nmuero {numero} es mayor a 0 ")
else:
    print(f"El numero {numero} es menor a 0 ")


print("--------------------------")

print ("ingreso un numero entero = ")
numero = input()
numero= int(numero)

if(numero >0):
    print(f"el nmuero {numero} es mayor a 0 ")
else:
    print(f"El numero {numero} es menor a 0 ")

#hay que ejecutarlo en la temrinal python

print("--------------------------")
print ("ingreso un numero entero = ") #elif
numero = input()
numero= int(numero)

if(numero >0): #si se cumple, imprimir, no se cumplio, evaliar otra, no se cumple, imprimr else
    print(f"el nmuero {numero} es mayor a 0 ")
elif(numero ==0):
    print(f"El numero {numero} es igual 0 ")
else:
    print(f"El numero {numero} es menor a 0 ")
