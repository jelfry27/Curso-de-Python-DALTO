# Creando un set()
conjunto0 = set(["JEL1","JEL2"])

# Frozenset (Conjunto Dentro De Otro Conjunto)
conjunto1 = frozenset(["JEL 1", "JEL 2"])
conjunto2 = {conjunto1, "JEL 2"}

print(conjunto0)
print(conjunto1)
print(conjunto2)

conjunto3 = {1,3,5,7}
conjunto4 = {1,3,5}

# Verificar Conjuntos
# Verificar SubConjuntos

resultado0 = conjunto3.issubset(conjunto4)
resultado1 = conjunto3 <= conjunto4

# Verificando SuperConjuntos
resultado2 = conjunto3.issuperset(conjunto4)
resultado3 = conjunto3 > conjunto4

print(resultado0)
print(resultado1)
print(resultado2)
print(resultado3)






