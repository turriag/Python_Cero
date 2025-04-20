# Pide dos números y muestra cual es mayor, o si son iguales.

num1 = int(input("por favor, digite su número: "))
num2 = int(input("por favor, digite su número: "))

if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
elif num1 == num2:
    print("Los dos digitos son iguales")
else:
    print("hay un error, digite nuevamente")


