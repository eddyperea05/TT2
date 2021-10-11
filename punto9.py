def minimocomundivisor(numero1, numero2):
    
    resultado = 0
    while(numero2 > 0):
        resultado = numero2
        numero2 = numero1 % numero2
        numero1 = resultado
    return numero1

def minimocomunmultiplo(numero1, numero2):
    if numero1 > numero2:
        divisor = numero1
    else:
       divisor  = numero2
    while (divisor  % numero1 != 0) or (divisor  % numero2 != 0):
        divisor  += 1
    return divisor 

print(minimocomundivisor(20,50))
print(minimocomunmultiplo(20,50))