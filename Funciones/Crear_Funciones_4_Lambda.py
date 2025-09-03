# Creando Funcione Lambda Para Multiplicar
multiplicar_por_dos = lambda x : x*2

def multiplicar_por_dos(x):
    return x*2

print(multiplicar_por_dos(2.5))


numeros = [1,2,3,4,5,6,7,8,9,10]

#Creando Funcion Que Diga Los Pares
def es_par(num):
    if (num%2==0):
        return True

numero_pares_1 = filter(es_par,numeros)

print(list(numero_pares_1))

#Creando Funcion Que Diga Los Impares

numero_pares_2 = filter(lambda numero:numero%2 == 1,numeros)
print(list(numero_pares_2))

 
