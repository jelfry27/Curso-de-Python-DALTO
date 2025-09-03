# creando diccionarios con dict()
diccionario = dict(nombre="JE",apellido="NU")

diccionario1 = {frozenset(["JE","RA"]):"jaja"}

diccionario2 = dict.fromkeys(["nombre","apellido"])

diccionario3 = dict.fromkeys(["nombre","apellido"],"Nose")

print(diccionario)
print(diccionario1)
print(diccionario2)
print(diccionario3)
