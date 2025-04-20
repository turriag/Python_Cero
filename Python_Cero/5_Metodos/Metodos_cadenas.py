cadena1 = "mi,nombre,es,luis,david,turriago"
cadena2 = "bienvenidos a python"

#convertir a mayusculas
print(cadena1.upper())

#convertir a minusculas
print(cadena1.lower())  

#primera letra en mayusculas
print(cadena1.capitalize())

#buscamos una cadena en otra cadena, si no hay concidencia devuelve -1
print(cadena1.find("luis")) 

#buscamos una cadena en otra cadena, si no hay concidencia lanza un error
print(cadena1.index("luis"))

#si es numerico, devolvemos  true, sino devolvemos false
print(cadena1.isnumeric())

#si es alfanumerico, devolvemos  true, sino devolvemos false
print(cadena1.isalpha())

#contamos concidencias de una cadena dentro de otra cadena, devuelve la cantidad de concidencias
print(cadena1.count("u"))

#contamos cuantos caracteres tiene una cadena
print(len(cadena1))

#verificamos si una cadena empieza con otra cadena, si es asi devuelve true
print(cadena1.startswith("minombre"))

#verificamos si una cadena termina con otra cadena, si es asi devuelve true
print(cadena1.endswith("turriago"))

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 por el valor 2     
cadena_nueva = cadena1.replace(",", " ")
cadena_nueva_2 = cadena_nueva.capitalize()

print(cadena_nueva_2)

#separar cadenas con la cadena que le pasemos
cadema_separada = cadena1.split(",")
print(cadema_separada)





