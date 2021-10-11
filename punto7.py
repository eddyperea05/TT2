def calcularIva (neto,iva):
    if iva is None:
        iva = 21
    total = neto*(1+(iva/100))
    print("El total a pagar con iva es ", total)

def calcularIva (neto):
    iva = 21
    total = neto*(1+(iva/100))
    print("El total a pagar con iva es ", total)

neto = int(input("Ingrese el valor de la compra "))
iva = int(input("Ingrese el iva de la compra "))


#calcularIva(neto,iva) Para que el usuario ingrese el valor del iva
#calcularIva(neto,None) En caso que pase el iva errado
#calcularIva(neto) En caso de no pasar el iva como parametro