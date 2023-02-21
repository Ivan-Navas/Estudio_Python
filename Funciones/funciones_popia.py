def Saludar(nombre):#*ceacion de una funcion (los parametros son basicamente una variable que solo existe dentro de la funcion)
    print("Hola soy " + nombre)
    
def Saludo(nombre, genero):
    genero = genero.lower()
    if(genero == "hombre"):
        print(f"Hola {nombre}, ¿Tu eres mi alumno?")
    elif(genero == "mujer"):
        print(f"Hola {nombre}, ¿Tu eres mi alumna?")


Saludo("Maria","mujer")
Saludo("Ivan","hombre")
