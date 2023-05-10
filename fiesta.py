"""Se solicita crear un programa en Python que permita llevar el registro de los invitados a una fiesta.
Para ello, se pide crear dos conjuntos (set): uno con los nombres de los invitados 
confirmados y otro con los nombres de los invitados que han llegado a la fiesta.
A medida que los invitados van llegando a la fiesta, se deben ir agregando 
sus nombres al conjunto de los que asistieron.
Además, se debe imprimir en pantalla la cantidad de invitados confirmados y
la cantidad de invitados que han asistido.Finalmente, se debe imprimir en pantalla 
el nombre de los invitados que confirmaron su asistencia pero aún 
no han llegado a la fiesta, es decir, los nombres que se encuentran en el conjunto 
de confirmados pero no en el conjunto de los que asistieron."""

#opcion1
"""invitados_confirmados = {"maria","adrian","eduardo","ernesto","sofia"}
invitados_asistentes = set ()

invitados_asistentes.add ("eduardo")
invitados_asistentes.add ("sofia")
invitados_asistentes.add ("maria")

print(f"los invitados confirmados son: ", len(invitados_confirmados))
print(f"los invitados asistentes son: ", len(invitados_asistentes))

#invitados_faltantes = invitados_confirmados - invitados_asistentes
#invitados_faltantes = invitados_confirmados.symmetric_difference(invitados_asistentes)
#invitados_faltantes = invitados_confirmados ^ invitados_asistentes

invitados_faltantes = invitados_confirmados.symmetric_difference(invitados_asistentes)
print("Los invitantes faltantes son: " ,invitados_faltantes)"""

#opcion2
def agregar_invitados_confirmados():
    set_confirmados = set()
    print("cuantos invitados confirmados desea ingresar")
    confirmados = input ("ingese la cantidad: ")
    for i in range(confirmados):
        set_confirmados.add(input(f"nombre del {i+1}er invitado: "))
    return set_confirmados

def agregar_invitados_asistentes(set_asistentes):
    print("ingrese el nombre del invitado: ", end="")
    set_asistentes.add(input())
    return set_asistentes

def cantidad_confirnados_o_asistentes(datos):
    print("la cantidad es ", len(datos))
    
def conocer_faltantes(invitados_confirmados, invitados_asistentes):
    faltantes = invitados_confirmados - invitados_asistentes
    print(f"los invitados faltantes son: ", faltantes)
    
