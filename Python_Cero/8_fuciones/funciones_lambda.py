
numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

# creando una función lambda para multiplicar por dos 
multiplicar_por_dos = lambda x : x*2

# creando funcion comun que diga si es par o no 
# def es_par(num):
#     if (num%2==0):
#         return True

# #usar filter con una funcion comun 
# num_pares = filter(es_par,numeros)
#print(list(num_pares))

#creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))

