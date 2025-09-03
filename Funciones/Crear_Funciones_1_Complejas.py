# Crear Una Funcion Que Tenga Parametro
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "Feminino"):
        adjetivo = "Reina"
    elif (sexo == "Masculino"):
        adjetivo == "Titan"
    else:
        adjetivo = 'amor'
    
    
    print(f"Hola {nombre}, mi {adjetivo} Que Haces? ")

saludar("BABY", "NENA")
saludar("Jelfry", "Masculino")
saludar("Karen", "Feminino")

# Crear Una Funcion que nos retorne valores

def crear_contrasena_radom(num):
    chars = "asdfgvbnm"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasena,num #return es para usarlo como variable

password,primer_numero = crear_contrasena_radom(8765)
print(password)
print("  ------------  ")
frase = f"Tu contrasena nueva es: {password}"
primer_dato = f"El Primer numero es: {primer_numero}"
print(frase)
