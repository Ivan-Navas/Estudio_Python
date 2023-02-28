# import modulo_saludar#*uso de un modulo con funcionalidades ( un modulo es un archivo .py)

#!si se quiere importar se debe tener en cuenta que no existan funciones y variables con el mismo nombre, porque purde generar errores

# import modulo_saludar as saludar#*permite darle un nombre a un modulo credo 

# from modulo_saludar import saludar #*permite importar una funcion de un modulo, sin la nececidad de tener que importar todo el modulo

# from modulo_saludar import saludar as saludando #*permite cambiarle el nombre a la funcion

# from modulo_saludar import * #*importa todo lo que se encuentre en el modulo(es consideado una mala practica, ya qur hace el programa pesado de forma imnecesaria)

# saludo = modulo_saludar.saludar()

# saludo2 = saludar.saludar()

# saludo3 = saludar()

# print(saludo3)

# from modulos2.modulo import Saludo#*cuando un modulo esta dentro de una carpeta

# print(Saludo(2))

import sys 
sys.path.append('D:\\Programacion\\ESTUDIO\\python\\modulo_fuera')#*se identifica la ruta de la carpeta
import modulo #*se importa el modulo deseado
print(modulo.Saludar())#*se utiliza una funcion que tiene el modulo
