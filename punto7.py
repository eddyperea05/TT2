def calcularIva (neto,iva):
    total = neto*(1+(iva/100))
    print("El total a pagar con iva es ", total)

neto = int(input("Ingrese el valor de la compra "))
iva = int(input("Ingrese el iva de la compra "))


calcularIva(neto,iva)
