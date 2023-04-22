"""Requerimos eliminar todas las vocales de la palabra 
“paralelepípedo”, e imprimir en pantalla las
consonantes restantes y su posición dentro de dicha palabra."""

#declarar valiable que almacene la palabra
palabra = "paralelepípedo"
consonante = ""

#range() convierte cada uno de los elementos en indice
for i in range(len(palabra)):
    if palabra[i] not in "aeiouAEIOUáéíóú":
        consonante += palabra[i]
        print(f"LA letra {palabra[i]} se encuentra en la posicion {i}")
print (consonante)


print("--------------------------")

palabra = "paralelepípedo"
consonante = ""
patron = "aeiouAEIOUáéíóú"

for i in range(len(palabra)):
    if palabra[i] not in patron:
        consonante += palabra[i]
        print(f"LA letra {palabra[i]} se encuentra en la posicion {i}")
print (consonante)