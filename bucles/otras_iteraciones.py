frutas = ["Mazana","Naranja","Pera","Uva","Mango","Fresa"]

for fruta in frutas:
    if fruta == "Pera":
        continue #*hace que el bucle se salte la vuenlta (en este caso cuando se cumple la condicion)
    print(f"Me gusta la {fruta}")

for fruta in frutas:
    if fruta == "Uva":
        break #*hace que se termine el bucle(aunque le falten vueltas)(si se usa un else despues de el bucle tampoco lo ejecutara)
    print(fruta)
    
#?recorrer e iterar son sinonimos

cadena = "Hola mundo"

for caracter in cadena:
    print(caracter)
    
lista = [1,2,3,4]
lista_duplicada = [x*2 for x in lista]#*crea un bucle for en un sola linea, x se multiplicara x 2, y el valor de x sera el los valores de la lista
print(lista_duplicada)