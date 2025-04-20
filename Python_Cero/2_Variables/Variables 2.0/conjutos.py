
# # creando un conjunto con set()
conjunto = set(["Dato 1"])

# metiendo un conjunto dentro de otro conjunto 
conjunto1 = frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1, "dato 3"}
print(conjunto2)

# teoria de conjuntos

conjunto_one =  {1, 3, 5, 7}
conjunto_two = {1, 3, 7,}

# verificamos si es un subconjunto
resultado = conjunto_two.issubset(conjunto_one)
resultado = conjunto_two <= conjunto_one

#  verificando si es un superconjunto
resultado1 = conjunto_two.issuperset(conjunto_one)
resultado1 = conjunto_two > conjunto_one


# verificar si hay algun número en comun
resultado = conjunto_two.isdisjoint(conjunto_one)
print(resultado)

