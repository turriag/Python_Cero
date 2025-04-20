diccionario = {
    "nombre": "luis",
    "apellido": "turriago",
    "edad": 19,
    "ciudad": "barranquilla",
    
}

# nos devuelve un objeto dict_items 
claves = diccionario.items() # devuelve una vista de los elementos del diccionario
print(claves)

# obteniendo un elemento con get()
print(diccionario.get("nombre")) # devuelve el valor del elemento, si no se encuentra devuelve None

# eliminando un elemento del diccionario
diccionario.pop("nombre") # elimina el elemento del diccionario
print(diccionario)

# eliminar todo del diccionario
diccionario.clear() # elimina todos los elementos del diccionario
print(diccionario)

