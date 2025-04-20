# Solicita un numero y muestra si es par o impar

num = int(input("por favor, digite un número: "))
if num % 2 == 0:
    print("el numero es par.")

elif num % 2 == 1:
    print("el numero es impar.")
    
else:
    print("solo se aceptan numeros positivos")
    