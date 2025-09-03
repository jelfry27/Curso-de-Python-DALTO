# Funcion De 3 Parametros
def frase (nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido} eres un {adjetivo}'

frease_resul = frase("J","N",5)
print(frease_resul)

# Misma Funcion Con Parametro opcional y valor por defecto
def frase2 (nombre,apellido,adjetivo = "R"):
    return f'Hola {nombre} {apellido} eres un {adjetivo}'


frease_resul1 = frase2("J","N","S")
print(frease_resul1)