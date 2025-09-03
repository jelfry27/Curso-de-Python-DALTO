# def suma
def suma(a, b):
    return a+b

resultado1 = suma(5,3)
print(resultado1)

# Utilizando el parametro args
def suma(*numeros):
    return sum(numeros)

resultado2 = suma(4,5,7)
print(resultado2)

# Forma optima de sumar valores
def suma(numeros):
    return sum([*numeros])

resultado2 = suma([4,5,7])
print(resultado2)

# Utilizando el operadorn * como argumento (*args)
def suma(nombre,*numeros):
    return f"Hola {nombre}, la suma de los numeros es: {sum(numeros)}"

resultado3 = suma("J",4,5,7)
print(resultado3)







