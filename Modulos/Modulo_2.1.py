# Importando Un Modulo Desde Una Carpeta Anterior

import sys

print(sys.path)

sys.path.append(r"C:\Users\sanch\Downloads\programation\PYTHON\Curso de Python DALTO\Modulos_A_Fueras")

import Modulo_0 as s

print(s.Saludo_personalizado("HOLA"))