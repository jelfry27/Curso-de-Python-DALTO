# CONJUNTOS
numeros = {10,12,14,18}
animales = {"perro","gato","loro","cocodrilo"}

# Literando dos Conjuntos "Mismo Tamano, Diferente Tiempo"

for numero in numeros:
    resultado = numero * 20
    print(f'Ahora la variable numero es: {resultado}')


for animal in animales:
    print(f'Ahora la variable animal es: {animal}')

print("---------------------")

# Literando dos conjuntos "Mismo Tamano, Mismo Tiempo"

for numero,animal in zip(numeros,animales):
    print(f'recorrido lista 2: {numero}')
    print(f'recorrido lista 1: {animal}')
    
# Pass
for num in range(100,200):
    print(num)

print("---------------------")

#Forma correcta de recorer un conjuntos
for numA in enumerate(numeros):
    indice = numA[0]
    valor = numA[1]
    print(f'El indece es: {indice} y el valor es: {valor}')

    print("---------------------")

# Usando else
for numero in numeros:
    print(f'Ejecutando el bucle: {numero}')

else:
    print("---------------------")
    print("El bucle: TERMINO")



