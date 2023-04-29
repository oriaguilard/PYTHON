"""La resistencia dentro de un circuito paralelo se calcula como: 
RT= 1/((1 /R1)+(1/R2)+(1/R3)+(1/Rn))

Donde: 
● RT es la resistencia total. 
● R1 es la resistencia 1.
● R2 es la resistencia 2.
● R3 es la resistencia 3.
● Rn la n-ésima resistencia.

Realizar el código en Python para calcular la resistencia total del circuito."""

"""validar el ingreso de cada resistencia, que sea mayor que 0,
validar errores, y utilizar funciones"""

#funcion para validar el ingreso de la resistencia en float
def validate_input_float(texto):

#ingreso de valores
    while True:
        try:
            r = float(input(texto))
            if r > 0:
                abs(r)
                return r
            else:
                print("el valor es menor a 0")
        except Exception as error: #exception es una clase para errores
            print("Ha ocurrido un error en el ingeso", error)
            print("Ha ocurrido un error. Ingrese nuevamente un valor") 
        
r_1 = validate_input_float("ingrese la resistencia 1: ")
r_2 = validate_input_float("ingrese la resistencia 2: ")
r_3 = validate_input_float("ingrese la resistencia 3: ")

rt = (1/((1 /r_1)+(1/r_2)+(1/r_3)))

print("La resistencia total es: {:.3f}".format(rt)) 