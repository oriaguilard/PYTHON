"""Se solicita crear un diccionario en Python para almacenar los precios de diferentes productos en una tienda en línea.
Las claves del diccionario serán los nombres de los productos y los valores serán los precios de los productos.
A continuación, se solicita recorrer el diccionario e imprimir los productos cuyos precios son superiores a 50 dólares. Finalmente, 
se debe calcular el precio total de los productos cuyos nombres empiezan
con la letra 'C' y mostrarlo en pantalla.
precios = {'camisa': 30, 'pantalon': 50, 'zapatos': 80, 'calcetines': 10, 'chaqueta': 100}"""

precios = {'camisa': 30, 
        'pantalon': 50, 
        'zapatos': 80, 
        'calcetines': 10, 
        'chaqueta': 100}

for producto,precio in precios.items(): #items para clave y values para valor
    #print(producto, precio)
    if precio >= 50:
        print("los productos mayor a 50 son: ",producto)

preciototal=0
cantproducto=0
for producto,precio in precios.items():
    if producto[0] == "c":
        preciototal += precio 
        cantproducto+=1 #contador para sacar el promedio //cuenta la cantidad de letras C
print("el precio total con letra C es: ", preciototal)
print("el promedio es: ", preciototal/cantproducto)
    