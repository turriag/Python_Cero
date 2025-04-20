
#Creando una lista (se puede modificar)
lista = ["luis turriago", "Barranquilla", True, 1.85, "luis turriago"]

#Creamos una dupla (no se puede modificar)
tupla = ("luis turriago", "Barranquilla", True, 1.85, "luis turriago")

#Esto es valido
lista[1] = "Ibagué"

#Esto no es valido
#tupla[1] = "Ibagué"

#Creamos un conjunto (set) (no se puede haceder a los elementos por su indice, no almacena datos duplicados)
conjunto = {"luis turriago", "Barranquilla", True, 1.85, "luis turriago"}

#print(conjunto[1]) -> No se puede acceder a los elementos por su indice

# Creamos un diccionario (almacena datos en pares clave-valor)
diccionario = {
    "nombre": "luis turriago",
    "ciudad": "Barranquilla",
    "estoy_emocionado": True,
    "altura": 1.85,
    "duplicado": "luis turriago",
}

print(diccionario["nombre"])  # Accedemos al valor de la clave "nombre"