"""En esta actividad trabajaremos con listas. Tomando la lista que se entrega a continuación, se
solicita realizar las siguientes acciones en el orden indicado:
1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.
La lista es:
1 mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]"""

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
mi_set = set (mi_lista)
print(mi_lista)
mi_lista = list(mi_set) #creando lista
print(mi_lista) 
mi_lista.sort() #ordenar
print(mi_lista)

#sorted(list(mi_set)) #se ahorraria linea 9/10/11

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
mi_lista = sorted(list(set(mi_lista)))
print(mi_lista)

