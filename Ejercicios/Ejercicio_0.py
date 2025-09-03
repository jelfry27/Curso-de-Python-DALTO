Otros_curso_min = 2.5
Otros_curso_max = 7
Otros_curso_promedio = 4
Curso_P = 5
Curso = 1.5


print("  -----------------")
print("   El Curso Demora   ")
diferencia_con_min = 100 - Curso / Otros_curso_min * 100 
print(f'- Curso Dalto {diferencia_con_min}% menos')

diferencia_con_max = 100 - Curso / Otros_curso_max * 100 
print(f'- Curso Dalto {diferencia_con_max}% menos')

diferencia_con_max_0 = 100 - Curso * 1000 // Otros_curso_max / 10
print(f'- Curso Dalto {diferencia_con_max_0}% menos')
print("  -----------------")

diferencia_con_promedio = 100 - Curso / Otros_curso_promedio * 100 
print(f'- Curso Dalto {diferencia_con_promedio}% menos')

tiempo_vacio_promedio = 100 - Otros_curso_promedio * 1000 // Curso_P / 10
print(f'- Cursos Promedio {diferencia_con_promedio}% Tiempo')
print("  -----------------")

tiempo_vacio_promedio = 100 - Otros_curso_promedio * 1000 // Curso / 10
print(f'- Curso_Tiempo_Ahorado {diferencia_con_promedio}% Tiempo')

print(f'- Curso_Equivale_A: {Otros_curso_promedio / Curso * 10}% Horas')
print("  -----------------")

print(f'- Curso_Equivale_A: {Otros_curso_promedio / Curso * 100 // Curso / 10}% Horas')

print(f'- Curso_Equivale_A: { Curso * 100 // Otros_curso_promedio / 10}% Horas')
print("  -----------------")


