alto = int(input("Ingrese la altura del cuadrado "))
ancho = int(input("Ingrese la altura del cuadrado "))
cuadrado =""

for a in range (alto):
    if(cuadrado == ""):
        for b in range (ancho):
            cuadrado= cuadrado + "*"
    print(cuadrado)