datos = {"dato1", "dato2", "dato3", "dato4", "dato5"}
numeros = {1,2,3,4,5,6,7,8,}


for dato in datos:
    print("Usando for: "+dato)
    
for dato in datos:
    print("Usando for y else: " + dato)
else:
    print("se muestra al final")

for dato in enumerate(datos):
    print(dato)