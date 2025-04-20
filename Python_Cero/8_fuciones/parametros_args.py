# forma no optima de sumar valores 

def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return  numeros_sumados

resultado = suma([5,8,7,6,2,3,1])
print(f"El resultado de la suma de los elementos es: {resultado}")


# forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([5,8,7,6,2,3,1])
print(resultado2)

# utilizando el operador * como argumento (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tu numero es: {sum(numeros)}"

resultado = suma("luis",5,8,7,6,2,3,1)

print(resultado)