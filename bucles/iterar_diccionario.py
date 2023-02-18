diccionario = {
    "nombre": "ivan",
    "apellido": "Navas",
    "edad": 20
}

for di in diccionario:#*Siempre muestra la clave del diccionario( sin importar el nombre que se le dé)
    print(di)
    
for di in diccionario.items():#*de esta manera entrega una tupla de clave valor se puede acceder a cada uno de los datos como un arreglo de JS
    print(di[1])
