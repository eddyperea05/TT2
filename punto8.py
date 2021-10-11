nombre = input('Ingrese su nombre ')
edad = int(input('Ingrese su edad '))
direccion = input('Ingrese su dirección')
telefono = int(input('Ingrese su numero de telefono '))
persona = {'nombre': nombre, 'edad': edad,
           'direccion': direccion, 'telefono': telefono}

print("Su nombre es:", nombre, "tiene", edad, "años""vive en",
      direccion, "Su numero de telefono es:", telefono)
