# LISTAS Y TUPLAS
numeros = [10,12,14,18]
animales = ["perro","gato","loro","cocodrilo"]

# Literando dos lista o tuplas "Mismo Tamano, Diferente Tiempo"

for numero in numeros:
    resultado = numero * 20
    print(f'Ahora la variable numero es: {resultado}')


for animal in animales:
    print(f'Ahora la variable animal es: {animal}')

print("---------------------")

# Literando dos lista o tuplas "Mismo Tamano, Mismo Tiempo"

for numero,animal in zip(numeros,animales):
    print(f'recorrido lista 2: {numero}')
    print(f'recorrido lista 1: {animal}')
    
# Pass
for num in range(100,200):
    print(num)

print("---------------------")

#Forma correcta de recorer una lista o tuplas
for numA in enumerate(numeros):
    indice = numA[0]
    valor = numA[1]
    print(f'El indece es: {indice} y el valor es: {valor}')

#Forma incorrecta de recorer una lista o tuplas
for numB in range(len(numeros)):
    print(numeros[numB])

print("---------------------")

# Usando else
for numero in numeros:
    print(f'Ejecutando el bucle: {numero}')

else:
    print("---------------------")
    print("El bucle: TERMINO")



