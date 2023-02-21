#*son las que incluye python
lista = [1,2,3,4,5,6,7,8]

mayor = max(lista)#*busca el numero mas grande 

menor = min(lista)#*busca el numero menor

redondeado = round(30.51230,3)#*redondea al numero entero mas cercano(si es .5 o .50 .... se dedondeara hacia abajo)(si de agrega un a , se puede escojer el numero de decimales que se le quieren dejar(si se pone un acanidad mayor a la de decimales dejara todos menos el ultimo)(no lo redondeara) )

bool = bool()#*si el parametro esta vacio, es 0 o es False o  none, retorna False, si se le ingresa calcuer dato que tenga informacion retorna True

all = all(["hoal",{1,2,3}])#*funciona similar a bool pero todos los datos deben cumplir la condicion para ser True, y con que uno no lo haga sera false

suma = sum(lista)#*suma todos los numeros de un iterable (todos deben ser numeros o da error)

print(suma)