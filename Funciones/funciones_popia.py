def Saludar(nombre):#*ceacion de una funcion (los parametros son basicamente una variable que solo existe dentro de la funcion)
    print("Hola soy " + nombre)
    
def Saludo(nombre, genero):
    genero = genero.lower()
    if(genero == "hombre"):
        print(f"Hola {nombre}, ¿Tu eres mi alumno?")
    elif(genero == "mujer"):
        print(f"Hola {nombre}, ¿Tu eres mi alumna?")

def sumar():
    numero1 = 20
    numero2 = 40
    resultado = numero1 + numero2
    return resultado#*return es lo que va a devolver una funcion, el hecho de que muestre en consola no quiere decir que esta retornando algo, ya  que el valor de la funcion será none si no retorna nada

def sumar_todo(nombre,*numeros):#*de esta forma tomara el valor de todos los elementos(si se quiere agregar mas parametros deben ser al inicio)
    return f" {nombre} El resultado de tu suma es  {sum(numeros)}"#*suma todos los valores de un iterable

#print(sumar_todo("Ivan, ",1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))#*cuando se tiene mas parametros, se iran asignando en orden, seran la lista que tomara *numeros

def prueba (nombre,edad, apellido = "Navas"):#*se puede dar valor por defecto a un parametro (si se define otra vez al momento de llamar la funcion tomara ese nuevo valor(se debe identificar el nombre del parametro, no se puede hacer solo por la posicion))
    return f"{nombre} {apellido} {edad} "

prueba2 = prueba(edad = 20 ,nombre = "Ivan", apellido = "navas")#*forzar un argumento: se espesifica el nombre del parametro y se dice a que sera igual de esta manera no importara el orden en que se definan
print(prueba2)