
# falto el profesor y los alumnos van a organizar la clase
# funcion para obterner el asistente y al profesor segun su edad

def obtener_compañeros(cantidad_conpañeros):
    
    #  crear la lista con los compañeros
    compañeros = []
    
    # ejecutando un for para pedir información de cada compañero
    for i in range(cantidad_conpañeros):
        nombre= input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero =(nombre,edad)
        
        #agregando la información a la lista
        compañeros.append(compañero)
        
    # ordenandolos de menor a mayor según su edad
    compañeros.sort(key=lambda x:x[1])
    
    # compañero[x] devuelve una dupla con (nombre,edad) y despues accedemos al nombre
    # para definir al asistente y al profesor
    asistente  = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    # retornamos una dupla
    return asistente,profesor
# desempaquetamos lo que nos retorna la función 
asistente,profesor = obtener_compañeros(5)

# mostrar el resultado 
print(f"El profesor es: {profesor} y su asistente es: {asistente}")
