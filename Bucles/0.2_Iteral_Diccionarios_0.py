diccionario = {
    "nombre": "JELFRY",
    "apellido": "NUNEZ",
    "subs": 100000
}


# recorriendo diccionario para obtener las claves
for key in diccionario.items():
    key
    print(f"La clave es: {key}")

# recorriendo diccionario con items() para obtener las claves y los valores
for dato in diccionario.items():
    key = dato[0]
    value = dato[1]
    print(f"La clave es: {key} y el valor es: {value}")