#ciclo while
#ciclo while(condicion) condicion siempre se evalua True al menos se cambie


i=0
while i <= 5:
    i+=1 #contador
    print(f"imprimiendo el valor de i {i}") 
    
print("--------------------------")

i=0
while i <= 5:
    i+=1 #contador
    if i == 1:
        continue
    print(f"imprimiendo el valor de i {i} y probando continue")  
    
print("--------------------------")

i=0
while i <= 5:
    i+=1 #contador
    if i == 4:
        break
    print(f"imprimiendo el valor de i {i} y probando el break")  
    
while True:
    print("palabra")
    break