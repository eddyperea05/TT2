sumTotal = 0
sumTotalD = 0
repito = True
while(repito):
    numero = int(input("Ingrese un un numero: "))
    sum = 0
    registroTemp = ""
    sumTotal += numero
    if(numero != 0):
        for i in range(len(str(numero))):
            sum += int(str(numero)[i])
        print("La sumatoria de los digitos de ", numero, " es ", sum)
    else:
        repito = False
for i in range(len(str(sumTotal))):
    sumTotalD += int(str(sumTotal)[i])
print("La sumatoria de todos los numero es: ", sumTotal,
      " y la sumaria de sus digitos es: ", sumTotalD)
