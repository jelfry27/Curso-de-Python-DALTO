# Pedir Nombre Y Edad

# funcion para obtener el nombre del asitente y el profesor segun la edad.
def obtener_companeros(cantidad_de_companeros):
    
    # creando la lista
    companeros = []
    # ejecutando un for para pedir informacion
    for i in range(cantidad_de_companeros):
        nombre = input("Ingresa el nombre:")
        edad = int(input("Ingresa la edad:"))
        companero = (nombre, edad)
        
        # agregando la informacion
        companeros.append(companero)
        
    # ordenandolos de menor a mayor
    companeros.sort(key=lambda x:x[1])
    
    # companero[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    # para definir al asistenre y al profesor
    asistente = companeros[0][0]
    profesor = companeros[-1][0]
    
    # retornamos una tupla
    return asistente,profesor

# Desampaquetado
asistente,profesor = obtener_companeros(2)

# Mostrando Resultado
print(f'El Profesor es: {profesor} y su asistente es {asistente}')