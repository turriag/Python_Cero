
# creando una función simple
# def saludar():
#     print("Hola luis, mi maestro ¿como andas?")
    
# # ejecutando la función simple
#saludar()

# crear una función que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "caballero"
    else:
        adjetivo = "titan"
    
    print(f"Hola {nombre}, mi {adjetivo} ¿como estas?") 
saludar("luis","hombre")
saludar("shandia","mujer")

# crear una función que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
password = crear_contraseña_random(4)
frase = f"tu contraseña nueva es: {password}"
print(frase)

# crear una función que nos retorne multiples valores   
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
# desempaquetando la función
password,primer_numero = crear_contraseña_random(254)

# mostrar los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El número utilizada para crearla fue: {primer_numero}")
