#List
lista = ["JELFRY","PROGRAMACION",True,1.81]
tupla = ("JELFRY","PROGRAMACION",True,1.81)
conjunto = {"JELFRY","PROGRAMACION",True,1.81}
conjunto2 = {"JELFRYA","PROGRAMACION","PROGRAMACION",True,1.81}
diccionario = {
    'nombre' : "JelFRY",
    'canal' : "JelFRY_CANAL",
    'esta_emocionado' : True,
    'altura' : 1.84,
    'dato_duplicad' :"JelFRY"
}

# puedo cambiar las listas "orden"
# no puedo cambiar las tuplas "orden"
# puedo cambiar los conjuntos "no orden" "no elementos duplicados" "no puedo hacer un print a una secion del conjunto"

lista[1] = "HACKING"

print(lista[1])
print(tupla[3])
print(conjunto)
print(conjunto2)
print(diccionario['nombre'])
print(diccionario['altura'] + 0.5 )