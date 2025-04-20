#creando las listas
frutas = ["banana","manzana","fresa","ciruela","pera","naranja","durazno"]
cadena = "hola luis"
numeros = [2,5,8,10]


#evitando que se coma una ciruela con la sentencia continue
for fruta in frutas:
    if fruta == "ciruela":
        continue
    print(f"Me voy a comer una: {fruta}")
print( )
    
#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")
    if fruta == "fresa":
        break
else:
    print("bucle terminado")

#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    

#for en una sola linea de código (duplicamos los números)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

