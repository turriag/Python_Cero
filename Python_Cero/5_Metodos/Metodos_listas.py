# creamos una lista con list()
lista = list(["luis", "turriago", 19, 1.75])

# devuelve la cantidad de elementos de la lista
print(len(lista))

# agregando un elemento a la lista
lista.append("luis")
print(lista)

#agregando un elemento a la lista en un indice especifico
lista.insert(0, "david")
print(lista)

# agregando varios elementos a la lista
lista.extend(["serrano", "barranquilla"])
print(lista)

# eliminar un elemento de la lista (por su indice)
lista.pop(2) # -1 para eliminar el ultimo, -2 para eliminar el penultimo, etc
print(lista)

# ordenar la lista de forma ascendente (si usamos el parametro reverse = True, la ordena de 
# forma descendente)
lista1 = list([9, 6, 3, 4, 5, 2, 7, 8, 1])
lista1.sort()
print(lista1)

# invirtiendo los elementos de una lista
lista1.reverse()
print(lista1)

# verificamos si un elemento se encuentra en la lista
print(lista.index("serrano")) # devuelve el indice del elemento, si no se encuentra lanza un error

# eliminando un elemento de la lista (por su valor) 
lista.remove("luis") # si no se encuentra lanza un error
print(lista)

# elimina todos los elementos de la lista
lista.clear()   
print(lista)

