numGanador = int(input("Ingrese el numero ganador de la loteria: "))
list = []
for i in range(len(str(numGanador))):
    list.append(str(numGanador)[i])
list.sort() 
print("Los numero ganadores en orden son: ",list)