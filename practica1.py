#*comentarios en python
print("Hola mundo")#*Imprimir un mensaje
a = 4#*Creacion de una variable(No es necesario ingresar el tipo de variable)
b = 2
c= a + b
print (c)
nombre = "Ivan"#*Creacion de una variable de tipo string(No es necesario ingresar el tipo de la variable)
edad = 20
info = "Mi nombre es: " + nombre + " y tengo " + str(edad) + " años"#*Se crea una variable con otras variables concatenadas(si hay strings con variables numericas se debe combertir el numero a string con str())
print (info)#*se imprime una variable(no se ponen comillas como con los mensajes)
#*Para limpiar la consola se usa clear
cadena1 = "comillas dobles" 
cadena2 = 'comillas simples'
cadena3 = """comillas triples"""
print("""Tus datos son:
      Nombre: ivan 
      Edad: 20""")#*Permite ingresar un mensajes en varias lineas de codigo
#*En python  es importante la identacion
#?identación:  Basicamente es el espacio que se desja deste el principio de la linea de codigo hasta que se empieza a escribir(Normalmente vscode usa 4 espacios)
#?Datos boleanos: son basicamente true y false, en pyton se escribe la primera en mayuscula(True False)