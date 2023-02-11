diccionario = {
    "nombre":"ivan",
    "apellido": "Navas",
    "edad": 20  
} 

diccionario2 = {
    1:"hola",
    2:"mundo"
}
keys  = diccionario.keys()#*devuelve las calves(los "significados")(tambien sirve para iterar)
get = diccionario.get("nombre")#*devuelve el valor del identificador ingresado(la ventaja de usar get es que si el valor no se encuentra no arrojara error(retorna none))
#print(diccionario2[1])#*si se identifican con  numeros se puede llamar como si fuera una lista(pero no se comportara como lista)
diccionario2.clear()#*elimina todos los elementos del diccionario
diccionario.pop("edad")#*eliminan el valor indicado(si no esta, arroja error)
dicionario_ite = diccionario.items()#*retorna un diccionario iterable
print(diccionario)