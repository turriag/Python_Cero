ingreso_mensual = float(input("Ingrese su ingreso mensual: "))
gasto_mensual = float(input("Ingrese su gasto mensual: "))


if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien pa, estas bien")
    else:
        print("y pa, estas gastando una banda, hay que ver si te alcanza")
    
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("Estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("Estas bien en venezuela")

else:
    print("soy pobre")