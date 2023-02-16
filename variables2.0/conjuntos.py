conjunto = set(["dato1", "dato2"])#*creacioon de un conjunto dandole una lista

lista = ["dato1","dato2"]

conjuntos = set(lista)
print(type(conjuntos))

conjunto1 = frozenset(["dato1","dato2"])#*crea un conjunto que permite ingresarlo en otro conjunto
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)
#?TEORIA DE CONJUNTOS
#*si se tiene e conjunto A= 1,2,3 y el conjunto B=1,2,3,4,5 dependiendo la perpentiba se puede decir que: 
#*A: A es un conjunto y B es un super conjunto(porque B tiene todos los elementos de A y mas)
#*B: B es un conjunto y A es un subconjunto de B(porque todos los elementos de a estan en B pero no todos los elementos de B estan en A)

conjunto1 = {1,2,3,4,5}
conjunto2 = {1,2,3,4}

resultado1 =  conjunto2.issubset(conjunto1)#*verifica si el primer conjunto es subconjunto del segundo(retorna true o false)
resultado2 = conjunto1.issuperset(conjunto2)#*verifica si el primer conjunto es super conjunto del segundo

resultados1 =  conjunto2 <= conjunto1#*verifica si el primer conjunto es subconjunto del segundo(<=: verifica si es subconjunto > verifica si es superconjunto)
resultados2 =  conjunto1 > conjunto2#*verifica si el primer conjunto es super conjunto del segundo(<=: verifica si es subconjunto > verifica si es superconjunto)

resultado = conjunto1.isdisjoint(conjunto2)#*verifica si son completamente distintos( si por lo menos un ade los datos coincide retorna false, coso contrario retorna true)

print(resultado)
