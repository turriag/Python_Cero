
animales = ("perro","gato","loro","pez")

# recorriendo la lista animal
for animal in animales:
    print(f"La variable animal es: {animal}")
    
    
numeros = (10, 12, 13, 20)

#recorriendo la lista numeros y multiplicando cada valor por 2
for numero in numeros:
    resultado = numero * 2
    print(resultado)

# iterando dos listas del mismo tamaño al mismo tiempo    
for animal,numero in zip(numeros,animales):
    print(f"recorriendo la lista 1: {animal}")
    print(f"recorriendo la lista 2: {numero}")
    
    
# forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])
    

# forma correcta de recorrer una lista con su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El idice es: {indice} y el valor es: {valor}")
    

# usamos el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
# todo lo anterior funciona exactamente igual para duplas
    