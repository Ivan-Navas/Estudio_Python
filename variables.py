#*Las variables son espacios en memoria donfe se almacenan datos
numero = 2#*variable numerica
cadena = "Hola mundo"#*variable de cadena de texto
boleano = True#*variable de boleano(true false)
flot = 2,4#*variable de float(nuemros con desimales)
nombre = "Ivan"
edad =20
informacion = f"Me llamo {nombre}"#*con f antes de la cadena de texto, se puede concatenar variables usando {corchetes} (lo convierte a texto, sin importar el dato se sea antes)
#?fstrings es vasicamente lo que permite concatenar variables usando {corchetes}
print(informacion)
del numero#*elimina la variable(Si hay una variable que utilice ese dato antes de que se eliminara, la variable que utiliza ese dato no se afectara,Ej se crea la variable mensaje = "hola " despues se crea la variable mensaje2 = "mundo", luego se imprime la variable mensje concatenada con mensaje2, luego se elimina mensaje; el mensaje impreso funcionara normal, ya que se elinmino despues de que se usara esa variable )
mensaje = "Hola "
mensaje2 = "mundo"
print (f"{mensaje}{mensaje2}")
print("Hola " + "mundo")
del mensaje
print("mu" in mensaje2)#*Verfica si el dato ingresado se encuentra en la variable especificada sin importar si es una parte de una palabra, o la palabra completa, con que este el dato exactamente mostrara true si no esta muestra false()
print("ma" not in mensaje2)#*Funciona parecino a in, pero en el caso que no este muestra true, si esta muestra false
nombre_completo = "Ivan ramiro nvas guerrero"#*en python cuando se escrive el nombre de una variable que tiene mas de una palabra se usa snake_case(entre cada palabra se usa un guin bajo( _ ))