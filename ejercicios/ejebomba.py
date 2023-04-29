"""Simulación de una bomba de tiempo. Irá el tiempo desde el 5 al 1 en decremento.
Al ejecutar el programa, se imprimirá el mensaje "Booom"""

import time

i=5

while i >=1:
    print(i)
    i-=1 #i=i-1
    time.sleep(1)
    print("boom")
    
"""for i in range(5,0,-1):
print(i)
print("Booom")"""