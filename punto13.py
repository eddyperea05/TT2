palabra = input("ingrese una palabra, para ver si es palindromo: ").lower()
aux = 0
for i in range(len(palabra)):
    if(palabra[i] == palabra[len(palabra)-i-1]):
        aux += 1
if(aux == len(palabra)):
    print("La palabra es palidromo")
else:
    print("La palabra no es palidromo")