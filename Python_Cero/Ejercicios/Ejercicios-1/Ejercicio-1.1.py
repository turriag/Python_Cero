# crear un progrma donde se le pida al usuario la edad para poder votar

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("usted puede votar.")
elif edad <= 17 and edad >=0:
    print("usted no tiene la edad requerida para votarl.")
else:
    print("ERROR al digitar el numero.")
    
    
    


