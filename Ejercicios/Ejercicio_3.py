#  Creando Una Funcion Que Nos Devuelva Numeros Primos
# Entre 0 y El Argumento Que Pasamos

def es_primo(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def primo_hasta(num):
    primos = []
    for i in range(3,num+1):
        resultado = es_primo(i)
        if resultado == True: primo_hasta.append(i)
    return primos

resultado1 = es_primo()
print(resultado1)



resultado2 = primo_hasta()
print(resultado2)

