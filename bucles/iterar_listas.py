animales  = ["Perro","Gato","Loro","Tigre","Lobo"]
edades = [13,2,1,6,8]

for animal in animales:#*recorre la lilsta de animales y la variable en cada vuelta tomara el valor del dato que este en esa posision 
    print(animal)
    
for animal,edad in zip(animales,edades):#*recorre 2 listas al mismo tiempo(pueden ser mas de 2, deben tener el mismo tamaño)
    print(f"El animal es: {animal} que tiene una edad de: {edad}")

for numero in range(1,11):#*recorre el rango espesificado(sin incluir el ultimo numero, si solo se ingresa un numero, sera de 0 a ese numero(si el numero es negativo o cero(0) no mostrara nada))
    print(numero)
    
for dato in enumerate(animales):#retorna el valor y el indice
    print(dato)
    
for dato in animales:
    print(dato)
else:#*despues de que el bucle termine se ejecutara(aunque el bucle este vacio)
    print("El bucle termino")