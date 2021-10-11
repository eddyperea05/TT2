def frecuencia(numero, digito):
    contador = 0
    while numero != 0:
        Digito = numero % 10
        if Digito == digito:
            contador += 1
        numero = numero//10
    return contador


numero1 = int(input("ingrese un Número: "))
digito = int(input("Ingrese un Dígito: "))
print("La Frecuencia del dígito en el número:", frecuencia(numero1, digito))
