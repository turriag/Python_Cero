# creando una funcion de 3 parametros
def frase(nombre,apellido,abjetivo):
    return f"Hola {nombre} {apellido}, sos muy {abjetivo}"

# utilizando keword arguments
frase_resultante = frase(abjetivo = "capo",nombre = "luis",apellido = "turriago")

print(frase_resultante)

# creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,abjetivo = "tonto"):
    return f"hola {nombre} {apellido}, sos muy {abjetivo}"

frase_resultante1 = frase("luis","turriago","inteligente")
print(frase_resultante1)