"""Realizar el calculo de la hipotenusa requiriendo el ingreso 
del cateto a y cateto b por parte del usuario en consola"""

import math #importar libreria mat
cateto_a = float (input("Ingrese valor A del cateto del triangulo: ")) 
cateto_b = float (input("Ingrese valor B del cateto del triangulo: "))

hipotenusa = math.sqrt(cateto_a*cateto_a + cateto_b*cateto_b) #se ocupa sqrt para la raiz
print("La hipotenusa es:", hipotenusa)