otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedios= 4
dalto_curso= 1.5
diferencia_duracion_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_duracion_max = 100 - dalto_curso *1000 // otros_cursos_max / 10
diferencia_duracion_pro = 100 - dalto_curso / otros_cursos_promedios * 100

print(f"El curso de dalto dura un {diferencia_duracion_min}% menos que el mas rapido")
print(f"El curso de dalto dura un {diferencia_duracion_max}% menos que el mas tardado")
print(f"El curso de dalto dura un {diferencia_duracion_pro}% menos que el promedio")



