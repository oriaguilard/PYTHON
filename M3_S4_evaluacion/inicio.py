"""Requerimos crear un registro de datos personales de tres personas.
Los datos que se necesitan
son: su nombre, apellido y teléfono. 
Para ello, generaremos un diccionario para cada una de las
personas con los datos mencionados, y luego los almacenaremos dentro de una 
lista. Finalmente, imprimiremos en pantalla la lista."""

persona_uno = {'nombre':'Orianna','apellido':'Aguilar','telefono':999999 }
persona_dos = {
    'nombre':'Adrian',
    'apellido':'Franco',
    'telefono':999999
}
persona_tres = {
    'nombre':'Victor',
    'apellido':'Peñafiel',
    'telefono':999999
}

una_lista= [persona_uno, persona_dos, persona_tres]
print(una_lista)

#para llamar un diccionario por
diccionario = {}
diccionario.update(persona_uno)
print(diccionario)

#crear un diccionario dentro de otro
personas ={
    "persona_uno" : {'nombre':'Orianna','apellido':'Aguilar','telefono':999999 },
    
    "persona_dos" : {
    'nombre':'Adrian',
    'apellido':'Franco',
    'telefono':999999 
    },
    "persona_tres" : {
    'nombre':'Victor',
    'apellido':'Peñafiel',
    'telefono':999999
    }
}
print(personas["persona_dos"]["apellido"])
print(personas["persona_uno"]["nombre"])