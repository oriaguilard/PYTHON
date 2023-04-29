"""Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
orden de mayor a meno"""

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))

if len(set({num1,num2,num3})) !=3: #con el set considero 3 numeros de un mismo largo//condicion diferente
    print("debe ingresar numeros diferentes")
else:
    ordenados = sorted([num1,num2,num3],reverse=True) #reserve sería a lo inverso, mayor a menor
    print(ordenados)