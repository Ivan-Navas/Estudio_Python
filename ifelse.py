contraseña = "Ivanrng"
constraseña_escrita = "Ian"

if contraseña == "Ivanrng":
    print("La contraseña  coincide")
    
else:
    print("La contraseña es incorrecta")
    
edad = 17

if edad >= 18:
    print("Ya eres mayor de edad")
    
elif edad >16:#*En caso de que no se cumpla la condicion anterior y se cumpla esta, solo se ejecutara esta, en caso de que se cumpla la anterior, esta no se ejecutara
    print("Aun no eres mayor de edad, pero estas cerca")
    
#*elif es else if
else:
    print("Eres menor de edad")
    
ingresos = 2000
gastos = 3000

if ingresos < gastos:
    print("Gastas mas de lo que ganas")