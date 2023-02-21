otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedios= 4
dalto_curso= 1.5
diferencia_duracion_min =  round(dalto_curso / otros_cursos_min *100,2)
diferencia_duracion_max =  round(dalto_curso  / otros_cursos_max *100, 2)
diferencia_duracion_pro = round(dalto_curso / otros_cursos_promedios *100, 2) 

print(f"El curso de dalto dura un {diferencia_duracion_min}% menos que el mas rapido")
print(f"El curso de dalto dura un {diferencia_duracion_max}% menos que el mas tardado")
print(f"El curso de dalto dura un {diferencia_duracion_pro}% menos que el promedio")



