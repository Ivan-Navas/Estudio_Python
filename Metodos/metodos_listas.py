lista2 = list({1,2,3,4,5,6,7,8,9,0})
lista = list({"mundo",12,"hola",True})#*retorna una lista (la retorna en difernte orden)
len = len(lista)#*retorna el numero de elementos de una lista
lista.append("tiro")#*agrega un elemento a la lista (la lista original se modifica)
lista.insert(2,"yaaaa")#*agrega un elemento en la pocision indicada
lista.extend({"12,3,4,5"})#*agrega varios elementos  a la lista (debe ser otra lista)
lista.pop(1)#*elimina el elemento que se encuentre en  la posicion indicada(si se quiere eliminar el ultimo se usa -1)
lista.remove("hola")#*elimina el elemento por el valor(si lo lo encuentra lanza una escepcion)
#lista.clear()#*elimina todos los elementos de la lista 
lista2.sort()#*ordena los elemntos de menor a mayor(si incluye los voleanos, tienen prioridad EJ: False, True, 20,44 )  (no debe haber cadenas de texto)
lista2.sort(reverse=True)#*le da la vueta a los elementos ordenados(de menor a mator, boleanos despues)
lista2.reverse()#*invierte la lista
print(lista2)
