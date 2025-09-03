frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "JELFRY_"
numeros = [2,5,8,11]

for fruta in frutas:
    print(fruta)

print("------------------------")

# Evitando que se coma una granada
for fruta in frutas:
    if fruta == 'granada':
        continue    
    print(f" Me voy a comer esta {fruta}")

print("------------------------")

# Evitar que continue el bucle (El else no se ejecuta)
for fruta in frutas:
    if fruta == 'pera':
        break    
    print(f" Me voy a comer esta {fruta}")
else:
    print("Termina")

print("------------------------")

# Recorrer una cadena de texto

for letra in cadena:
    print(letra)

print("------------------------")

# Numeros Multiplicados
numeros_duplicado = [x*2 for x in numeros]
print(numeros_duplicado)

print("------------------------")

# Numeros divididos
numeros_divididos = [x/2 for x in numeros]
print(numeros_divididos)

# Numeros al cubo
numeros_al_cubo = [x**2 for x in numeros]
print(numeros_al_cubo)


print("Bucles Terminado")


