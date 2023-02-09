cadena1 = "hola,mundo,nuevo"
cadena2 = "¿Como vas?"
numero = "1212"

dir = dir(cadena1)#?muestra todos los metodos que se le pueden usar
upeer = cadena1.upper()#*convierte a mayusculas
lower = cadena1.lower()#*convierte a  minusculas
capitalize = cadena1.capitalize()#*convierte la primera letra a mayusculas(el resto siempre queda en minuscula)
flind = cadena1.find("mundo")#*verifica si se encuentra en el arreglo y retorna la posicion(si no esta retorna -1)(es case sensityve)(los espacios cuentan)
index = numero.index("2")#*funciona igual a find, pero si no encuentra el dato arroja un error
isnumeric = cadena1.isnumeric()#*verifica si es solo numeros(aunque este como si fuersa string, si son solo numeros sera true)
isalpha = cadena1.isalpha()#*verifica si es alfanumerico(solo son validos de la A a l  Z (no incluye los espacios))
count = cadena1.count("a")#*devuelve el numero de veces que se encuentra el dato exacto(sin importar si es la mitad de una palabra o frace EJ: hola mundo count(la mun) sera una ves ya que esta la frase (es las 2 ultimas letras de una y las 3 primeras de la otra e incluye los espacios))
len = len(cadena1)#?cuenta el numero de caracteres que tiene una cadena (incluidos los espacios)
srtartwith = cadena1.startswith("h")#*si empieza exactamente con el valor dado retorna true
endswith = cadena1.endswith("o")#*si termina exactamente con el valor dado retorna true
raplace = cadena1.replace("hola","chao")#*remplasa la cadena(si la encuentra, si no la encuentra retorna la orinal)
split= cadena1.split(",")#*separa la cadena cada ves que encuentra el dato dado
