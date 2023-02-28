import sys
sys.path.append('D:\\Programacion\\ESTUDIO\\python\\modulo_saludo')
sys.path.append('D:\\Programacion\\ESTUDIO\\python\\modulo_suma')

import saludo, suma

print(saludo.Saludo("Ivan"))
print(f"Resultado {suma.Suma(20,20)}")