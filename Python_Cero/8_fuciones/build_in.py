
numeros = [4,7,1,42,15]

# encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# redondiando a 6 decimales
numero = round(12.345678,2)
print(numero)

# retorna False -> 0, vacio, False, None \ True -> distinto a 0, True, cadena, datos no vacios
resultado_bool = bool("hola luis")
print(resultado_bool)

# retorna True, si todos los valores son verdaderos
resultado_all = all([100,True,[344,23]])
print(resultado_all)

# suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)
