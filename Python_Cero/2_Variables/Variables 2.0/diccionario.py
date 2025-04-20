
# crear diccionarios con dict()

diccionario = dict(nombre="luis",apellido="turriago",ciudad="barranquilla")
print(diccionario)

# las listas no pueden ser claves y usamos frozanset para meter conjuntos
familias = {
    frozenset(["garcia", "lopez"]): "medellin",
    frozenset(["turriago", "serrano"]): "ibague"
}

# Buscar de qué ciudad es esta combinación
consulta = frozenset(["serrano", "turriago"])
print(familias[consulta])  


# creando diccionarios con fromkeys() valor por defecto: None
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"], "No se")

print(diccionario)
