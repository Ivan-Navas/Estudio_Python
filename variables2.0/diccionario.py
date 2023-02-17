diccionario = dict(nombre="ivan", apellido="navas",edad=20)#*creacion de un diccionario usando dict

print(diccionario["nombre"])

diccionario2 = dict.fromkeys(["nombre","edad"])#*crea un diccionario vacio

diccionario2["nombre"] = "ivan"#*asi se le da el valor al diccionario

print(diccionario2)