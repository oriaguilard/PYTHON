"""se pide realizar una calculadora declarando funciones para cada tipo de
calculo. Realizar un menu con opciones para seleccionar que calculo se desea realizar
el ingreso es por consola, requerir al usuario la opcion y numero al que se realizararan el calculo.
verificar errores de ingreso
verificar division por cero"""

def suma (num1, num2):
    sumatoria=num1 + num2
    return sumatoria

def resta (num1: float, num2: float):
    return num1 - num2

def multiplicar (num1, num2) -> float:
    return num1 * num2

def dividir (num1 , num2):
    if num2 == 0:
        return None
    else:
        return num1 / num2
    
    
    
def opciones():
    
    print("bienvenido a la calculadora")
    print("1. suma")
    print("2. resta")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")
    print("Ingrese una opción: ")
    
#funcion calculadora, llevara el menu y realizara los calculos usando las funciones y estrcuturas condicionales.
def calculadora():
    
    while True: #mientras sea true o no exista un break se seguira ejecutando
        try:
    #requerir y mostrar opciones al usuario
            opciones () #invocar a la funcion para mostrar opciones al usuario
            
            #ingresar los valores de opcion
            opcion = input("1/2/3/4/5: ") #opciones
            num1 = float(input("ingrese el primer numero: "))
            num2 = float(input("ingrese el segundo numero: "))
            
            #evaluar opcion y seleccionar una funcion a realizar su se cumple la condicion
            match opcion:
                case '1':
                    resultado = suma (num1, num2)
                case '2':
                    resultado = resta (num1, num2)
                case '3':
                    resultado = multiplicar (num1, num2)
                case '4':
                    resultado = dividir (num1, num2)
                case '5': #return si es funcion #break si es ciclo
                    print("gracias por usar la calculadora")
                    break
                case _: #resultado = None
                    print ("opcion no valida, eliga una op valida")
                    
            if resultado is not None:
                print(f"el resultado de el calculo entre {num1} y {num2} es: {resultado}")
                        
        except Exception as e: #si sucede algun error, se imprime en consola el error
            print("Error: ", e)

calculadora()
    
    