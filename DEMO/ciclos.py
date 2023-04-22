#ciclos
#ejecutan isntrucciones repetidas hasta que se cumple una condicion o se finalice el ciclo

#ciclo for
#for i in data:
#instrucciones a realizar

frutas=["fresa","manzana","pera"]

for i in frutas:
    print(i)
print("--------------------------")
    
#for i in range(len(data)):
for i in range(1,6):
    print(i)
    
print("--------------------------")
for i in range(len(frutas)):
    print(i)
    
print("--------------------------")
for i in "python":
    print(i)

print("--------------------------")
for i in "python":
    i == "p"
    #continue
    print(i)

print("--------------------------")
for i in range(len("python")):
    print(i)
    
print("--------------------------")
#los elementos y la posicion
palabra = "python"
for i in range(len(palabra)):
    print(palabra[i])