mail = input("Por favor ingrese un correo electronico: ")

if(mail.find('@') != -1):
    print("El correo electronico es valido")
else:
    print("El correo electronico es invalido")
