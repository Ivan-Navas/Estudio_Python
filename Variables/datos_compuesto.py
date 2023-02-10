#*son datos que tienen datos simples o datos compuestos que se puedden agrupar
lista = ["hola",1,"Mundo",20]#*creacion de una lista
print(lista[1])#*para acceder a los datos por individual se usan las pocisiones entre [corchetes], desde 0, ej: puesto1=0, puesto2=1 etc...
tupla = ("hola",1,"Mundo",20)#*son parecidas a la slistas, pero se usan parentesis(las tuplas no se pueden modificar)
print(tupla[0])#*para imprimir individualmente si se usan los corchetes[]
#print("Hola mundo")#*condo undodigo se convierte en comentario se le conoce como comentar codigo(es un poco diferente a hacer un comentario, ya que el comentario solo es un mensaje, el codigo comentado es posiblemente codigo funcional)
conjunto = {"hola",12,3,"Mundo"}#*creacion de un conjunto es parecido a las tuplas(no se puede acceder al elemento por el indiuce (posición), los conjuntos no aceptan datos duplicados(no los muestra))
diccionario = {#*es parecido a las listas, pero los datos tienen un nombre que los identifica, por el cual se puede acceder al valor 
    'nombre': "Ivan",
    'edad': 20,
    'genero':"masculino"
}
print(diccionario['edad'])#*se accede al valor en especifico del diccionario